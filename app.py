import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# Safe API init
client = None
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -------------------------------
# LOAD DATA
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("unilever_fpna.csv")

revenue_col = [c for c in df.columns if "Revenue" in c][0]
profit_col = [c for c in df.columns if "Profit" in c][0]

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filters")

market = st.sidebar.selectbox("Market", ["All"] + list(df["Market"].unique()))
brand = st.sidebar.selectbox("Brand", ["All"] + list(df["Brand"].unique()))
year = st.sidebar.selectbox("Year", ["All"] + list(df["Year"].unique()))

filtered_df = df.copy()

if market != "All":
    filtered_df = filtered_df[filtered_df["Market"] == market]

if brand != "All":
    filtered_df = filtered_df[filtered_df["Brand"] == brand]

if year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == year]

# -------------------------------
# KPI
# -------------------------------
total_rev = filtered_df[revenue_col].sum()
total_profit = filtered_df[profit_col].sum()
margin = (total_profit / total_rev * 100) if total_rev else 0

# -------------------------------
# HEADER
# -------------------------------
st.title("💼 CFO FP&A Dashboard")

c1, c2, c3 = st.columns(3)
c1.metric("Revenue", f"{total_rev:,.0f}")
c2.metric("Profit", f"{total_profit:,.0f}")
c3.metric("Margin %", f"{margin:.2f}%")

# -------------------------------
# AUTO INSIGHTS (NO API)
# -------------------------------
st.markdown("## 🤖 AI CFO Auto Insights")

market_perf = filtered_df.groupby("Market")[revenue_col].sum()

if not market_perf.empty:
    st.success(f"🏆 Top Market: {market_perf.idxmax()}")
    st.error(f"📉 Weak Market: {market_perf.idxmin()}")

# -------------------------------
# CHARTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    yearly = filtered_df.groupby("Year")[revenue_col].sum().reset_index()
    st.plotly_chart(px.line(yearly, x="Year", y=revenue_col), use_container_width=True)

with col2:
    mp = filtered_df.groupby("Market")[profit_col].sum().reset_index()
    st.plotly_chart(px.bar(mp, x="Market", y=profit_col), use_container_width=True)

# -------------------------------
# VARIANCE ANALYSIS
# -------------------------------
st.markdown("## 📊 Variance Analysis")

yearly_full = df.groupby("Year")[[revenue_col, profit_col]].sum().sort_index()

rev_change = 0
profit_change = 0

if len(yearly_full) >= 2:
    rev_change = yearly_full.iloc[-1][revenue_col] - yearly_full.iloc[-2][revenue_col]
    profit_change = yearly_full.iloc[-1][profit_col] - yearly_full.iloc[-2][profit_col]

    st.write(f"Revenue Change: {rev_change:,.0f}")
    st.write(f"Profit Change: {profit_change:,.0f}")

# -------------------------------
# VARIANCE AI (SAFE)
# -------------------------------
if st.button("Explain Variance", key="var_btn"):
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": f"Explain revenue change {rev_change} and profit change {profit_change}"
                }]
            )
            st.info(response.choices[0].message.content)
        except Exception:
            st.warning("⚠️ API busy. Showing basic insight.")
            st.info("Revenue and profit changes indicate business performance trend.")
    else:
        st.info("Revenue and profit changes indicate business performance trend.")

# -------------------------------
# BOARD COMMENTARY
# -------------------------------
st.markdown("## 🧾 Board Commentary")

if st.button("Generate Board Report", key="board_btn"):
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": f"Revenue {total_rev}, Profit {total_profit}, Margin {margin}"
                }]
            )
            st.success(response.choices[0].message.content)
        except Exception:
            st.warning("⚠️ API busy. Showing summary.")
            st.success("Business shows stable growth. Monitor margin closely.")
    else:
        st.success("Business shows stable growth. Monitor margin closely.")

# -------------------------------
# DRIVER ANALYSIS
# -------------------------------
st.markdown("## 🧠 Driver Analysis")

if margin < 50:
    st.warning("⚠️ Margin pressure observed")
else:
    st.success("👍 Strong margin performance")

st.write("📈 Growth driven by revenue expansion")

# -------------------------------
# RULE-BASED CFO ENGINE
# -------------------------------
def rule_based_cfo(question, df, revenue_col, profit_col):
    q = question.lower()

    total_rev = df[revenue_col].sum()
    total_profit = df[profit_col].sum()
    margin = (total_profit / total_rev * 100) if total_rev else 0

    market_rev = df.groupby("Market")[revenue_col].sum()
    market_profit = df.groupby("Market")[profit_col].sum()

    yearly = df.groupby("Year")[[revenue_col, profit_col]].sum().sort_index()

    # ---------------------------
    # MARKET QUESTIONS
    # ---------------------------
    if "top market" in q:
        top = market_rev.idxmax()
        val = market_rev.max()
        return f"Top market is {top} with revenue {val:,.0f}."

    if "weak market" in q or "lowest market" in q or "risky" in q:
        low = market_profit.idxmin()
        return f"Risky/weak market is {low} due to lowest profitability."

    if "revenue" in q and "australia" in q:
        val = df[df["Market"] == "Australia"][revenue_col].sum()
        return f"Revenue for Australia is {val:,.0f}."

    # ---------------------------
    # PROFIT / MARGIN
    # ---------------------------
    if "margin" in q:
        return f"Current margin is {margin:.2f}%. Pressure observed due to cost growth."

    if "why margin" in q or "margin declining" in q:
        return "Margin is declining because costs are increasing faster than revenue growth."

    if "profit" in q:
        return f"Total profit is {total_profit:,.0f}."

    # ---------------------------
    # YoY COMPARISON
    # ---------------------------
    if "compare" in q and "profit" in q:
        if len(yearly) >= 2:
            last = yearly.iloc[-1][profit_col]
            prev = yearly.iloc[-2][profit_col]
            diff = last - prev
            return f"Profit changed from {prev:,.0f} to {last:,.0f} ({diff:+,.0f})."

    if "2022" in q and "2023" in q:
        if 2022 in yearly.index and 2023 in yearly.index:
            p1 = yearly.loc[2022][profit_col]
            p2 = yearly.loc[2023][profit_col]
            return f"Profit increased from {p1:,.0f} in 2022 to {p2:,.0f} in 2023."

    # ---------------------------
    # VARIANCE / GROWTH
    # ---------------------------
    if "variance" in q:
        if len(yearly) >= 2:
            rev_diff = yearly.iloc[-1][revenue_col] - yearly.iloc[-2][revenue_col]
            profit_diff = yearly.iloc[-1][profit_col] - yearly.iloc[-2][profit_col]
            return f"Revenue variance is {rev_diff:,.0f} and profit variance is {profit_diff:,.0f}."

    if "growth" in q:
        return "Growth is driven by strong revenue expansion in key markets."

    # ---------------------------
    # GENERAL BUSINESS INSIGHT
    # ---------------------------
    if "performance" in q:
        return "Business shows stable performance with key markets driving growth."

    return "fallback"

# -------------------------------
# ASK CFO (FIXED)
# -------------------------------
st.markdown("## 💬 Ask AI CFO")

# session state to store answer
if "cfo_answer" not in st.session_state:
    st.session_state.cfo_answer = ""

question = st.text_input("Ask CFO-level question")

if st.button("Ask CFO"):
    if question:

        answer = rule_based_cfo(question)

        # RULE BASED
        if answer != "fallback":
            st.session_state.cfo_answer = answer

        # AI FALLBACK
        else:
            if client:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": question}]
                    )
                    st.session_state.cfo_answer = response.choices[0].message.content
                except:
                    st.session_state.cfo_answer = "⚠️ AI busy. Try again."
            else:
                st.session_state.cfo_answer = "⚠️ Ask about revenue, profit, margin, markets."

# ✅ ALWAYS DISPLAY ANSWER
if st.session_state.cfo_answer:
    st.success(st.session_state.cfo_answer)


# -------------------------------
# SCENARIO PLANNING
# -------------------------------
st.markdown("## 🎛️ Scenario Planning")

rev_slider = st.slider("Revenue Change %", -20, 30, 5)
cost_slider = st.slider("Cost Change %", -20, 30, 5)

base_cost = total_rev - total_profit

new_rev = total_rev * (1 + rev_slider / 100)
new_cost = base_cost * (1 + cost_slider / 100)

new_profit = new_rev - new_cost
new_margin = (new_profit / new_rev * 100) if new_rev else 0

st.write(f"Revenue: {new_rev:,.0f}")
st.write(f"Profit: {new_profit:,.0f}")
st.write(f"Margin: {new_margin:.2f}%")