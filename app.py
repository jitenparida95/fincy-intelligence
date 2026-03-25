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

# ------------------ LOAD DATA ------------------
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

# ------------------ DASHBOARD ------------------
st.title("📊 AI CFO Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"{total_revenue:,.0f}")
col2.metric("Profit", f"{total_profit:,.0f}")
col3.metric("Margin %", f"{margin:.2f}")

# ------------------ CHARTS ------------------
st.subheader("📊 Revenue by Market")
st.bar_chart(df.groupby("Market")["Net_Revenue_AUD000"].sum())

st.subheader("💰 Profit by Market")
st.bar_chart(df.groupby("Market")["Gross_Profit_AUD000"].sum())

st.subheader("📈 Trend")
trend = df.groupby("Year")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum()
st.line_chart(trend)

# ------------------ VARIANCE ------------------
st.subheader("📉 Variance Analysis")

rev_var, profit_var = 0, 0

if df["Year"].nunique() >= 2:
    years = sorted(df["Year"].unique())
    prev, curr = years[0], years[-1]

    prev_df = df[df["Year"] == prev]
    curr_df = df[df["Year"] == curr]

    rev_var = curr_df["Net_Revenue_AUD000"].sum() - prev_df["Net_Revenue_AUD000"].sum()
    profit_var = curr_df["Gross_Profit_AUD000"].sum() - prev_df["Gross_Profit_AUD000"].sum()

    st.write(f"Revenue Change: {rev_var:,.0f}")
    st.write(f"Profit Change: {profit_var:,.0f}")

    st.bar_chart(pd.DataFrame({
        "Metric": ["Revenue", "Profit"],
        "Variance": [rev_var, profit_var]
    }).set_index("Metric"))

# ------------------ DRIVER ANALYSIS ------------------
st.subheader("🧠 Driver Analysis")

if margin < 50:
    st.warning("⚠️ Margin pressure observed")
else:
    st.success("✅ Healthy margin")

if rev_var > 0:
    st.info("Growth driven by revenue expansion")
else:
    st.error("Revenue decline risk")

# ------------------ BOARD COMMENTARY ------------------
st.subheader("📋 Board Commentary")

if st.button("Generate Commentary"):
    st.write(f"""
    Revenue changed by {rev_var:,.0f} and profit by {profit_var:,.0f}.
    Margin stands at {margin:.2f}%.

    Growth driven by {'revenue expansion' if rev_var>0 else 'decline'}.
    Focus areas: cost control, market optimization.
    """)

# ------------------ RULE BASED CFO ------------------
def rule_based_cfo(q):
    q = q.lower()

    if "revenue australia" in q:
        val = df[df["Market"]=="Australia"]["Net_Revenue_AUD000"].sum()
        return f"Revenue for Australia is {val:,.0f}"

    if "total revenue" in q or "revenue" == q.strip():
        return f"Total revenue is {total_revenue:,.0f}"

    if "profit" in q:
        return f"Total profit is {total_profit:,.0f}"

    if "margin" in q:
        return f"Margin is {margin:.2f}%"

    if "top market" in q:
        return df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmax()

    if "risk" in q:
        return df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmin()

    if "variance" in q:
        return f"Revenue variance {rev_var:,.0f}, Profit variance {profit_var:,.0f}"

    if "focus" in q:
        return "Focus on improving weak markets and scaling strong ones"

    return "Try: revenue, profit, margin, variance, top market"

# ------------------ AI CFO ------------------
def ai_cfo_answer(question):
    if client is None:
        return "⚠️ AI unavailable (no API key)"

    try:
        prompt = f"""
        You are a CFO.

        Revenue: {total_revenue}
        Profit: {total_profit}
        Margin: {margin:.2f}

        Question: {question}

        Answer like a strategic finance leader.
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.3
        )

        return res.choices[0].message.content

    except:
        return "⚠️ AI unavailable (quota exceeded)"

# ------------------ ASK CFO ------------------
st.subheader("💬 Ask AI CFO")

question = st.text_input("Ask CFO-level question")

if st.button("Ask CFO") or question:

    rule_ans = rule_based_cfo(question)
    ai_ans = ai_cfo_answer(question)

    st.subheader("📊 Rule-Based Answer")
    st.success(rule_ans)

    st.subheader("🤖 AI CFO Insight")
    st.info(ai_ans)

    st.subheader("📌 CFO Action Plan")
    st.write("""
    - Improve margin through cost optimization  
    - Scale high-performing markets  
    - Fix weak market performance  
    """)