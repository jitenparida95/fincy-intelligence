import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# ── PAGE CONFIG ─────────────────────────────
st.set_page_config(
    page_title="CFO Command Centre",
    page_icon="📊",
    layout="wide"
)

# ── STYLE ─────────────────────────────
st.markdown("""
<style>
body {background-color:#0d1117;color:#e6edf3;}
.kpi {background:#111827;padding:15px;border-radius:10px}
</style>
""", unsafe_allow_html=True)

# ── LOAD DATA ─────────────────────────────
@st.cache_data
def load():
    if os.path.exists("unilever_fpna.csv"):
        return pd.read_csv("unilever_fpna.csv")
    return pd.DataFrame()

df = load()
if df.empty:
    st.error("Upload CSV")
    st.stop()

# ── KPIs ─────────────────────────────
nr = df["Net_Revenue_AUD000"].sum()
gp = df["Gross_Profit_AUD000"].sum()
ebitda = df["EBITDA_AUD000"].sum()
cogs = df["COGS_AUD000"].sum()
opex = df["OPEX_AUD000"].sum()

# ── HEADER ─────────────────────────────
st.title("📊 CFO Command Centre")

# ── KPI CARDS ─────────────────────────────
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Net Revenue", f"AUD {nr:,.0f}")
c2.metric("Gross Profit", f"AUD {gp:,.0f}")
c3.metric("EBITDA", f"AUD {ebitda:,.0f}")
c4.metric("COGS", f"AUD {cogs:,.0f}")
c5.metric("OPEX", f"AUD {opex:,.0f}")

# ── CHARTS ─────────────────────────────
st.subheader("Revenue & Profit Breakdown")
col1,col2,col3 = st.columns(3)

# P&L by Market
with col1:
    rev = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
    fig = go.Figure()
    fig.add_bar(x=rev["Market"], y=rev["Net_Revenue_AUD000"], name="Revenue")
    fig.add_bar(x=rev["Market"], y=rev["Gross_Profit_AUD000"], name="GP")
    fig.add_bar(x=rev["Market"], y=rev["EBITDA_AUD000"], name="EBITDA")
    fig.update_layout(barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# Category
with col2:
    cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().reset_index()
    fig2 = go.Figure(go.Bar(x=cat["Net_Revenue_AUD000"], y=cat["Category"], orientation="h"))
    st.plotly_chart(fig2, use_container_width=True)

# P&L Bridge (FIXED)
with col3:
    wfall = {
        "Base NR": df["Base_NR_AUD000"].sum(),
        "Trade Promo": -df["Trade_Promo_AUD000"].sum(),
        "Net Revenue": nr,
        "COGS": -cogs,
        "Gross Profit": gp,
        "OPEX": -opex,
        "EBITDA": ebitda,
    }
    fig3 = go.Figure(go.Bar(x=list(wfall.keys()), y=list(wfall.values())))
    fig3.update_xaxes(tickangle=-30)
    st.plotly_chart(fig3, use_container_width=True)

# ── TREND (FIXED) ─────────────────────────────
st.subheader("Trend Analysis")

trend = df.groupby(["Year","Month_Num","Month"])[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
trend = trend.sort_values(["Year","Month_Num"])
trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"]

fig4 = go.Figure()
fig4.add_scatter(x=trend["Period"], y=trend["Net_Revenue_AUD000"], name="Revenue")
fig4.add_scatter(x=trend["Period"], y=trend["Gross_Profit_AUD000"], name="GP")
fig4.add_scatter(x=trend["Period"], y=trend["EBITDA_AUD000"], name="EBITDA")

fig4.update_xaxes(tickangle=-45)
st.plotly_chart(fig4, use_container_width=True)

# ── BRAND SCORECARD ─────────────────────────────
st.subheader("Brand Scorecard")

brand = df.groupby("Brand").agg(
    Revenue=("Net_Revenue_AUD000","sum"),
    GP=("Gross_Profit_AUD000","sum")
).reset_index()

st.dataframe(brand, use_container_width=True)

# ── AI CFO (GEMINI) ─────────────────────────────
st.subheader("🤖 AI CFO")

def ai_cfo(q):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "⚠️ Add GOOGLE_API_KEY"

    import google.generativeai as genai
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are CFO.
    Revenue: {nr}
    GP: {gp}
    EBITDA: {ebitda}

    Question: {q}
    Give insights.
    """

    res = model.generate_content(prompt)
    return res.text

q = st.text_input("Ask CFO")
if st.button("Ask"):
    st.write(ai_cfo(q))