import streamlit as st
import pandas as pd
import os

# ------------------ OPENAI SETUP ------------------
try:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = None
except:
    client = None

# ------------------ LOAD DATA ------------------
df = pd.read_csv("your_file.csv")  # <-- keep your file name

# ------------------ BASIC METRICS ------------------
total_revenue = df["Net_Revenue_AUD000"].sum()
total_profit = df["Gross_Profit_AUD000"].sum()
margin = (total_profit / total_revenue) * 100

# ------------------ RULE BASED CFO ------------------
def rule_based_cfo(question):
    q = question.lower()

    if "revenue" in q and "australia" in q:
        val = df[df["Market"] == "Australia"]["Net_Revenue_AUD000"].sum()
        return f"Revenue for Australia is {val:,.0f}"

    elif "total revenue" in q:
        return f"Total revenue is {total_revenue:,.0f}"

    elif "total profit" in q:
        return f"Total profit is {total_profit:,.0f}"

    elif "margin" in q:
        return f"Current margin is {margin:.2f}%"

    elif "top market" in q:
        top = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmax()
        return f"Top market is {top}"

    elif "risk" in q:
        low = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmin()
        return f"Weakest market is {low}"

    elif "where" in q or "focus" in q:
        return "Focus on improving low performing markets and scaling strong ones"

    elif "profit change" in q or "variance" in q:
        return f"Revenue: {total_revenue:,.0f}, Profit: {total_profit:,.0f}"

    else:
        return "Try: total revenue, total profit, margin, top market"

# ------------------ AI CFO ------------------
def ai_cfo_answer(question, df):
    if client is None:
        return "⚠️ AI not configured (Add API key in Streamlit secrets)"

    try:
        summary = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum().to_string()

        prompt = f"""
        You are a CFO.

        Data:
        {summary}

        Question: {question}

        Give short business insight.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI error: {str(e)}"

# ------------------ UI ------------------
st.title("📊 AI CFO Dashboard")

# Sidebar Filters (keep yours if already exists)
market = st.sidebar.selectbox("Market", ["All"] + list(df["Market"].unique()))

if market != "All":
    df = df[df["Market"] == market]

# ------------------ DRIVER ANALYSIS ------------------
st.subheader("🧠 Driver Analysis")

if margin < 50:
    st.warning("⚠️ Margin pressure observed")
else:
    st.success("✅ Healthy margins")

st.info("Growth driven by revenue expansion")

# ------------------ ASK CFO ------------------
st.subheader("💬 Ask AI CFO")

question = st.text_input("Ask CFO-level question")

ask = st.button("Ask CFO")

# 🔥 KEY FIX: ENTER + BUTTON BOTH WORK
if question:

    rule_ans = rule_based_cfo(question)
    ai_ans = ai_cfo_answer(question, df)

    st.markdown("### 📊 Rule-Based Answer")
    st.success(rule_ans)

    st.markdown("### 🤖 AI CFO Insight")
    st.info(ai_ans)

elif ask:
    st.warning("Please enter a question")