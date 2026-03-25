import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("unilever_fpna.csv")  # default demo data

# Auto-detect columns
revenue_col = [col for col in df.columns if "Revenue" in col][0]
profit_col = [col for col in df.columns if "Profit" in col][0]

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("📊 Filters")

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
# KPI CALCULATIONS
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
# TOP / WEAK MARKET
# -------------------------------
market_perf = filtered_df.groupby("Market")[revenue_col].sum()

top_market = market_perf.idxmax()
low_market = market_perf.idxmin()

st.success(f"🏆 Top Market: {top_market}")
st.error(f"📉 Weak Market: {low_market}")

# -------------------------------
# CHARTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    yearly = filtered_df.groupby("Year")[revenue_col].sum().reset_index()
    fig = px.line(yearly, x="Year", y=revenue_col, title="Revenue Trend")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    market_profit = filtered_df.groupby("Market")[profit_col].sum().reset_index()
    fig2 = px.bar(market_profit, x="Market", y=profit_col, title="Profit by Market")
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# VARIANCE ANALYSIS
# -------------------------------
st.subheader("📊 Variance Analysis")

yearly_full = df.groupby("Year")[[revenue_col, profit_col]].sum().sort_index()

if len(yearly_full) >= 2:
    rev_change = yearly_full.iloc[-1][revenue_col] - yearly_full.iloc[-2][revenue_col]
    profit_change = yearly_full.iloc[-1][profit_col] - yearly_full.iloc[-2][profit_col]

    st.write(f"Revenue Change: {rev_change:,.0f}")
    st.write(f"Profit Change: {profit_change:,.0f}")

# -------------------------------
# DRIVER ANALYSIS
# -------------------------------
st.subheader("🧠 Driver Analysis")

if margin > 50:
    st.write("👍 Strong profitability")
else:
    st.write("⚠️ Margin pressure observed")

if rev_change > 0:
    st.write("📈 Growth driven by revenue expansion")

# -------------------------------
# MARKET CONTRIBUTION
# -------------------------------
st.subheader("🌍 Market Contribution")

top3 = market_perf.sort_values(ascending=False).head(3)
bottom3 = market_perf.sort_values().head(3)

st.write("Top 3 Markets")
st.dataframe(top3)

st.write("Bottom 3 Markets")
st.dataframe(bottom3)

# -------------------------------
# CFO COMMENTARY
# -------------------------------
st.subheader("📋 CFO Commentary")

st.write("👉 Business shows stable growth")
st.write(f"👉 {top_market} driving performance")
st.write(f"👉 {low_market} needs attention")

# -------------------------------
# ASK CFO (RULE-BASED AI)
# -------------------------------
st.subheader("💬 Ask CFO")

question = st.text_input("Ask anything (CFO level)")

def cfo_agent(q):
    q = q.lower()
    response = []

    if "profit growth" in q:
        response.append("Profit growth is driven primarily by revenue expansion")

    if "price" in q or "volume" in q:
        response.append("Growth appears volume-driven due to consistent revenue scaling")

    if "margin" in q:
        response.append("Margin pressure observed due to cost increase")

    if "underperform" in q:
        response.append(f"{low_market} is underperforming")

    if "risk" in q:
        response.append("High dependency on top market is a key risk")

    if "forecast" in q:
        response.append("Business expected to continue growth trend")

    if "cost" in q:
        response.append("Cost control required to protect margins")

    if "summary" in q:
        response.append("Strong revenue growth with moderate margin pressure")

    if not response:
        response.append("Ask about profit, revenue, risk, or strategy")

    return response

if question:
    answers = cfo_agent(question)
    for ans in answers:
        st.write("👉", ans)

# -------------------------------
# BUDGET VS ACTUAL
# -------------------------------
st.subheader("💰 Budget vs Actual")

budget_rev = total_rev * 0.95
budget_profit = total_profit * 0.95

st.metric("Revenue Variance", f"{total_rev - budget_rev:,.0f}")
st.metric("Profit Variance", f"{total_profit - budget_profit:,.0f}")

# -------------------------------
# FORECASTING
# -------------------------------
st.subheader("📈 Forecast")

if len(yearly_full) >= 2:
    growth = (yearly_full.iloc[-1][revenue_col] - yearly_full.iloc[-2][revenue_col]) / yearly_full.iloc[-2][revenue_col]
    forecast_rev = yearly_full.iloc[-1][revenue_col] * (1 + growth)

    st.write(f"Forecast Revenue: {forecast_rev:,.0f}")

# -------------------------------
# SCENARIO PLANNING
# -------------------------------
st.subheader("🎛️ Scenario Planning")

rev_change = st.slider("Revenue Change %", -20, 30, 5)
cost_change = st.slider("Cost Change %", -20, 30, 5)

base_cost = total_rev - total_profit

new_rev = total_rev * (1 + rev_change/100)
new_cost = base_cost * (1 + cost_change/100)

new_profit = new_rev - new_cost
new_margin = (new_profit / new_rev * 100) if new_rev else 0

st.write(f"Revenue: {new_rev:,.0f}")
st.write(f"Profit: {new_profit:,.0f}")
st.write(f"Margin: {new_margin:.2f}%")

from openai import OpenAI

client = OpenAI(api_key=st.secrets["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"])

st.markdown("## 🧠 Ask AI CFO")

user_question = st.text_input("Ask any CFO-level question")

ask_clicked = st.button("Ask AI CFO")

if ask_clicked:

    if user_question.strip() == "":
        st.warning("Enter a question bro 👀")

    else:
        with st.spinner("Thinking like a CFO..."):

            context = f"""
            You are a CFO analyzing business performance.

            Total Revenue: {df[revenue_col].sum()}
            Total Profit: {df[profit_col].sum()}
            Margin: {(df[profit_col].sum()/df[revenue_col].sum())*100:.2f}%

            Markets: {df['Market'].unique().tolist()}
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": context},
                        {"role": "user", "content": user_question}
                    ]
                )

                answer = response.choices[0].message.content

                st.markdown("### 💡 CFO Insight")
                st.success(answer)

            except Exception as e:
                st.error(f"API Error: {e}")