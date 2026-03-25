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

# ------------------ SAFE DATA LOAD ------------------
def load_data():
    try:
        return pd.read_csv("data.csv")  # if exists in repo
    except:
        uploaded = st.file_uploader("Upload CSV (Net_Revenue_AUD000, Gross_Profit_AUD000, Market)", type=["csv"])
        if uploaded:
            return pd.read_csv(uploaded)
        else:
            # fallback dummy data (so app NEVER breaks)
            return pd.DataFrame({
                "Market": ["Australia","Indonesia","Vietnam","Philippines","New Zealand"],
                "Net_Revenue_AUD000": [59410, 32000, 21000, 27000, 20000],
                "Gross_Profit_AUD000": [29000, 15000, 9000, 12000, 10000]
            })

df = load_data()

# ------------------ METRICS ------------------
total_revenue = df["Net_Revenue_AUD000"].sum()
total_profit = df["Gross_Profit_AUD000"].sum()
margin = (total_profit / total_revenue) * 100 if total_revenue else 0

# ------------------ RULE BASED CFO ------------------
def rule_based_cfo(question):
    q = question.lower()

    if "australia" in q and "revenue" in q:
        val = df[df["Market"]=="Australia"]["Net_Revenue_AUD000"].sum()
        return f"Revenue for Australia is {val:,.0f}"

    if "total revenue" in q or "revenue" == q.strip():
        return f"Total revenue is {total_revenue:,.0f}"

    if "total profit" in q or "profit" == q.strip():
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
        return "Focus on improving low-performing markets and scaling strong ones"

    if "profit change" in q or "variance" in q:
        return f"Revenue: {total_revenue:,.0f}, Profit: {total_profit:,.0f}"

    return "Try: total revenue, total profit, margin, top market"

# ------------------ AI CFO ------------------
def ai_cfo_answer(question, df):
    if client is None:
        return "⚠️ AI not configured (add API key in Streamlit secrets)"

    try:
        summary = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000"]].sum().to_string()

        prompt = f"""
You are a CFO.

Data:
{summary}

Question: {question}

Give sharp business insight in 2-3 lines.
"""

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.3
        )

        return res.choices[0].message.content

    except Exception as e:
        return "⚠️ AI error. Showing rule-based answer."

# ------------------ UI ------------------
st.title("📊 AI CFO Dashboard")

# Filters
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

# ENTER + BUTTON BOTH WORK
if question:

    rule_ans = rule_based_cfo(question)
    ai_ans = ai_cfo_answer(question, df)

    st.markdown("### 📊 Rule-Based Answer")
    st.success(rule_ans)

    st.markdown("### 🤖 AI CFO Insight")
    st.info(ai_ans)

elif ask:
    st.warning("Enter a question")