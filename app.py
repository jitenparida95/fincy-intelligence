import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(layout="wide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -------------------------------
# LOAD DATA
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("unilever_fpna.csv")

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
# AI CFO AUTO INSIGHTS
# -------------------------------
st.markdown("## 🤖 AI CFO Auto Insights")

if st.button("Generate Insights", key="insight_btn"):
    with st.spinner("Generating insights..."):
        st.success(f"🏆 Top Market: {filtered_df.groupby('Market')[revenue_col].sum().idxmax()}")
        st.error(f"📉 Weak Market: {filtered_df.groupby('Market')[revenue_col].sum().idxmin()}")

# -------------------------------
# CHARTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    yearly = filtered_df.groupby("Year")[revenue_col].sum().reset_index()
    st.plotly_chart(px.line(yearly, x="Year", y=revenue_col, title="Revenue Trend"), use_container_width=True)

with col2:
    market_profit = filtered_df.groupby("Market")[profit_col].sum().reset_index()
    st.plotly_chart(px.bar(market_profit, x="Market", y=profit_col, title="Profit by Market"), use_container_width=True)

# -------------------------------
# VARIANCE ANALYSIS
# -------------------------------
st.markdown("## 📊 Variance Analysis")

yearly_full = df.groupby("Year")[[revenue_col, profit_col]].sum().sort_index()

if len(yearly_full) >= 2:
    rev_change = yearly_full.iloc[-1][revenue_col] - yearly_full.iloc[-2][revenue_col]
    profit_change = yearly_full.iloc[-1][profit_col] - yearly_full.iloc[-2][profit_col]

    st.write(f"Revenue Change: {rev_change:,.0f}")
    st.write(f"Profit Change: {profit_change:,.0f}")

if st.button("Explain Variance", key="variance_btn"):
    with st.spinner("Explaining like CFO..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Revenue change: {rev_change}, Profit change: {profit_change}"},
                {"role": "user", "content": "Explain variance in CFO style"}
            ]
        )
        st.info(response.choices[0].message.content)

# -------------------------------
# BOARD COMMENTARY
# -------------------------------
st.markdown("## 🧾 Board Commentary")

if st.button("Generate Board Report", key="board_btn"):
    with st.spinner("Writing board report..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Revenue: {total_rev}, Profit: {total_profit}, Margin: {margin:.2f}%"},
                {"role": "user", "content": "Write board-level summary"}
            ]
        )
        st.success(response.choices[0].message.content)

# -------------------------------
# DRIVER ANALYSIS
# -------------------------------
st.markdown("## 🧠 Driver Analysis")

if margin > 50:
    st.write("👍 Strong profitability")
else:
    st.write("⚠️ Margin pressure observed")

if len(yearly_full) >= 2 and rev_change > 0:
    st.write("📈 Growth driven by revenue expansion")

# -------------------------------
# MARKET CONTRIBUTION
# -------------------------------
st.markdown("## 🌍 Market Contribution")

market_perf = filtered_df.groupby("Market")[revenue_col].sum()

st.write("Top 3 Markets")
st.dataframe(market_perf.sort_values(ascending=False).head(3))

st.write("Bottom 3 Markets")
st.dataframe(market_perf.sort_values().head(3))

# -------------------------------
# CFO COMMENTARY
# -------------------------------
st.markdown("## 📋 CFO Commentary")

top_market = market_perf.idxmax()
low_market = market_perf.idxmin()

st.write("👉 Business shows stable growth")
st.write(f"👉 {top_market} driving performance")
st.write(f"👉 {low_market} needs attention")

# -------------------------------
# ASK AI CFO
# -------------------------------
st.markdown("## 💬 Ask AI CFO")

question = st.text_input("Ask CFO-level question")

if st.button("Ask AI CFO", key="ask_btn"):

    if question.strip() == "":
        st.warning("Enter a question")

    else:
        with st.spinner("Thinking like CFO..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": f"Revenue: {total_rev}, Profit: {total_profit}, Margin: {margin:.2f}%"},
                        {"role": "user", "content": question}
                    ]
                )
                st.success(response.choices[0].message.content)

            except Exception as e:
                st.error(f"API Error: {e}")

# -------------------------------
# FORECAST + SCENARIO
# -------------------------------
st.markdown("## 🎛️ Scenario Planning")

rev_change_pct = st.slider("Revenue Change %", -20, 30, 5)
cost_change_pct = st.slider("Cost Change %", -20, 30, 5)

base_cost = total_rev - total_profit

new_rev = total_rev * (1 + rev_change_pct/100)
new_cost = base_cost * (1 + cost_change_pct/100)

new_profit = new_rev - new_cost
new_margin = (new_profit / new_rev * 100) if new_rev else 0

st.write(f"Revenue: {new_rev:,.0f}")
st.write(f"Profit: {new_profit:,.0f}")
st.write(f"Margin: {new_margin:.2f}%")