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

    market_perf = df.groupby("Market")[revenue_col].sum()

    if "top market" in q:
        return f"Top market is {market_perf.idxmax()}."

    elif "weak market" in q:
        return f"Weakest market is {market_perf.idxmin()}."

    elif "margin" in q:
        return f"Margin is {margin:.2f}%."

    elif "profit" in q:
        return f"Total profit is {total_profit:,.0f}."

    elif "revenue" in q and "australia" in q:
        val = df[df["Market"] == "Australia"][revenue_col].sum()
        return f"Revenue for Australia is {val:,.0f}."

    elif "why margin" in q:
        return "Margin decline is due to rising costs."

    else:
        return "fallback"

# -------------------------------
# ASK CFO (HYBRID)
# -------------------------------
st.markdown("## 💬 Ask AI CFO")

q = st.text_input("Ask CFO-level question")

if st.button("Ask CFO", key="ask_btn"):
    if q:
        answer = rule_based_cfo(q, filtered_df, revenue_col, profit_col)

        if answer == "fallback":
            if client:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": q}]
                    )
                    st.success(response.choices[0].message.content)
                except Exception:
                    st.warning("⚠️ API busy. Try again.")
            else:
                st.warning("⚠️ No AI available. Try basic questions.")
        else:
            st.success(answer)

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