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
def rule_based_cfo(question):
    q = question.lower()

    market_rev = filtered_df.groupby("Market")[revenue_col].sum()
    market_profit = filtered_df.groupby("Market")[profit_col].sum()

    # 🔥 HANDLE GENERIC QUESTIONS
    if "revenue" in q and "market" not in q:
        return f"Total revenue is {total_rev:,.0f}"

    if "profit" in q and "compare" not in q:
        return f"Total profit is {total_profit:,.0f}"

    if "margin" in q:
        return f"Current margin is {margin:.2f}%. Likely impacted by cost increase."

    if "top market" in q:
        return f"Top market is {market_rev.idxmax()}"

    if "weak" in q or "risk" in q:
        return f"Weakest market is {market_profit.idxmin()}"

    if "australia" in q:
        val = filtered_df[filtered_df["Market"] == "Australia"][revenue_col].sum()
        return f"Revenue for Australia is {val:,.0f}"

    if "growth" in q:
        return "Growth is driven by strong revenue expansion."

    if "variance" in q:
        return f"Revenue variance {rev_var:,.0f}, Profit variance {profit_var:,.0f}"

    return "fallback"

# -------------------------------
# ASK AI CFO (FIXED VERSION)
# -------------------------------

st.subheader("💬 Ask AI CFO")

question = st.text_input("Ask CFO-level question", key="cfo_input")

def rule_based_cfo(q, df):
    q = q.lower()

    total_revenue = df["Net_Revenue_AUD000"].sum()
    total_profit = df["Gross_Profit_AUD000"].sum()
    margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

    # Market aggregation
    market_rev = df.groupby("Market")["Net_Revenue_AUD000"].sum()
    market_profit = df.groupby("Market")["Gross_Profit_AUD000"].sum()

    top_market = market_rev.idxmax()
    weak_market = market_rev.idxmin()

    # -------- BASIC --------
    if "total revenue" in q or q.strip() == "revenue":
        return f"Total revenue is {total_revenue:,.0f}"

    if "total profit" in q or q.strip() == "profit":
        return f"Total profit is {total_profit:,.0f}"

    if "margin" in q:
        return f"Current margin is {margin:.2f}%"

    # -------- MARKET --------
    if "australia" in q:
        val = market_rev.get("Australia", 0)
        return f"Revenue for Australia is {val:,.0f}"

    if "indonesia" in q:
        val = market_profit.get("Indonesia", 0)
        return f"Profit for Indonesia is {val:,.0f}"

    if "top market" in q:
        return f"Top market by revenue is {top_market}"

    if "weak" in q or "underperform" in q:
        return f"Weakest market is {weak_market}"

    # -------- VARIANCE --------
    if "variance" in q or "change" in q:
        yearly = df.groupby("Year")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum()

        if len(yearly) >= 2:
            rev_var = yearly.iloc[-1]["Net_Revenue_AUD000"] - yearly.iloc[-2]["Net_Revenue_AUD000"]
            profit_var = yearly.iloc[-1]["Gross_Profit_AUD000"] - yearly.iloc[-2]["Gross_Profit_AUD000"]

            return f"Revenue change: {rev_var:,.0f}, Profit change: {profit_var:,.0f}"

        return "Not enough data for variance analysis"

    # -------- INSIGHTS --------
    if "why margin" in q:
        return "Margin pressure likely due to rising costs or lower pricing."

    if "improve margin" in q:
        return "Focus on cost optimization, pricing strategy, and high-margin markets."

    if "risk" in q:
        return f"Key risk: Underperformance in {weak_market} market."

    if "opportunity" in q:
        return f"Biggest opportunity lies in scaling {top_market} market."

    if "growth" in q:
        return "Growth is primarily driven by revenue expansion."

    if "where should we focus" in q:
        return f"Focus on improving performance in {weak_market} and scaling {top_market}"

    if "explain profit" in q:
        return f"Total profit is {total_profit:,.0f}. Driven by revenue and cost structure."

    # -------- FALLBACK --------
    return "Try asking: revenue, profit, margin, top market, australia revenue"


# ✅ ENTER KEY FIX
if question:
    answer = rule_based_cfo(question, df)
    st.success(answer)

# Optional button (still works)
if st.button("Ask CFO"):
    if question:
        answer = rule_based_cfo(question, df)
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