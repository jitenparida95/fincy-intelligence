import streamlit as st
import pandas as pd
import os

# ------------------ OPENAI SETUP ------------------
try:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key) if api_key else None
except:
    client = None

# ------------------ LOAD DATA (SAFE) ------------------
def load_data():
    try:
        return pd.read_csv("data.csv")
    except:
        uploaded = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded:
            return pd.read_csv(uploaded)
        else:
            return pd.DataFrame({
                "Year":[2022,2023,2023,2024,2024],
                "Market":["Australia","Australia","Indonesia","Vietnam","Philippines"],
                "Net_Revenue_AUD000":[50000,59410,32000,21000,27000],
                "Gross_Profit_AUD000":[25000,29000,15000,9000,12000]
            })

df = load_data()

# ------------------ FILTERS ------------------
st.sidebar.header("Filters")

market_filter = st.sidebar.selectbox("Market", ["All"] + list(df["Market"].unique()))
year_filter = st.sidebar.selectbox("Year", ["All"] + list(df["Year"].unique()))

if market_filter != "All":
    df = df[df["Market"] == market_filter]

if year_filter != "All":
    df = df[df["Year"] == year_filter]

# ------------------ METRICS ------------------
total_revenue = df["Net_Revenue_AUD000"].sum()
total_profit = df["Gross_Profit_AUD000"].sum()
margin = (total_profit / total_revenue) * 100 if total_revenue else 0

# ------------------ DASHBOARD CHARTS ------------------
st.title("📊 AI CFO Dashboard")

st.subheader("📊 Revenue by Market")
rev_chart = df.groupby("Market")["Net_Revenue_AUD000"].sum()
st.bar_chart(rev_chart)

st.subheader("💰 Profit by Market")
profit_chart = df.groupby("Market")["Gross_Profit_AUD000"].sum()
st.bar_chart(profit_chart)

st.subheader("📈 Revenue vs Profit Trend")
trend = df.groupby("Year")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum()
st.line_chart(trend)

# ------------------ VARIANCE ANALYSIS ------------------
st.subheader("📉 Variance Analysis")

if "Year" in df.columns and df["Year"].nunique() >= 2:
    years = sorted(df["Year"].unique())
    prev, curr = years[0], years[-1]

    prev_df = df[df["Year"] == prev]
    curr_df = df[df["Year"] == curr]

    rev_var = curr_df["Net_Revenue_AUD000"].sum() - prev_df["Net_Revenue_AUD000"].sum()
    profit_var = curr_df["Gross_Profit_AUD000"].sum() - prev_df["Gross_Profit_AUD000"].sum()

    st.write(f"Revenue Change: {rev_var:,.0f}")
    st.write(f"Profit Change: {profit_var:,.0f}")

    if rev_var > 0:
        st.success("Revenue increased YoY")
    else:
        st.error("Revenue declined YoY")

# ------------------ DRIVER ANALYSIS ------------------
st.subheader("🧠 Driver Analysis")

if margin < 50:
    st.warning("⚠️ Margin pressure observed")
else:
    st.success("✅ Healthy margins")

st.info("Growth driven by revenue expansion")

# ------------------ RULE BASED CFO ------------------
def rule_based_cfo(question):
    q = question.lower()

    if "australia" in q and "revenue" in q:
        val = df[df["Market"]=="Australia"]["Net_Revenue_AUD000"].sum()
        return f"Revenue for Australia is {val:,.0f}"

    if "total revenue" in q or "revenue" == q.strip():
        return f"Total revenue is {total_revenue:,.0f}"

    if "total profit" in q:
        return f"Total profit is {total_profit:,.0f}"

    if "margin" in q:
        return f"Current margin is {margin:.2f}%"

    if "top market" in q:
        top = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmax()
        return f"Top market is {top}"

    if "risk" in q:
        low = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmin()
        return f"Weakest market is {low}"

    if "where" in q or "focus" in q:
        return "Focus on improving weak markets and scaling strong ones"

    if "variance" in q:
        return f"Revenue variance {rev_var:,.0f}, Profit variance {profit_var:,.0f}"

    return "Try: total revenue, profit, margin, top market"

# ------------------ AI CFO ------------------
def ai_cfo_answer(question, df):
    if client is None:
        return "⚠️ Add OpenAI API key in secrets"

    try:
        # Build strong business context
        total_revenue = df["Net_Revenue_AUD000"].sum()
        total_profit = df["Gross_Profit_AUD000"].sum()
        margin = (total_profit / total_revenue) * 100 if total_revenue else 0

        market_summary = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum()

        context = f"""
        You are a WORLD-CLASS CFO (FP&A Leader).

        Financial Summary:
        - Total Revenue: {total_revenue}
        - Total Profit: {total_profit}
        - Margin: {margin:.2f}%

        Market Performance:
        {market_summary.to_string()}

        Your role:
        - Explain WHY things are happening
        - Identify RISKS
        - Identify OPPORTUNITIES
        - Suggest ACTIONS

        Be concise, sharp, executive-level.
        """

        prompt = f"{context}\n\nQuestion: {question}\n\nAnswer like a CFO:"

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI error: {e}"

# ------------------ ASK CFO ------------------
st.subheader("💬 Ask AI CFO")

question = st.text_input("Ask CFO-level question")
ask = st.button("Ask CFO")

if question:
    rule_ans = rule_based_cfo(question)
    ai_ans = ai_cfo_answer(question, df)

    st.subheader("📊 Rule-Based Answer")
    st.success(rule_ans)

    st.subheader("🤖 AI CFO Insight")
    st.info(ai_ans)

elif ask:
    st.warning("Enter a question")