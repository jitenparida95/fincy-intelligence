import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

st.set_page_config(
    page_title="Unilever APAC | CFO Command Centre",
    page_icon="📊",
    layout="wide",
)

# ── THEME ─────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#94a3b8"),
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis=dict(gridcolor="#1e2a3a"),
    yaxis=dict(gridcolor="#1e2a3a"),
)

# ── DATA LOAD ─────────────────────────────────────
@st.cache_data
def load_data():
    if os.path.exists("unilever_fpna.csv"):
        return pd.read_csv("unilever_fpna.csv")
    return pd.DataFrame()

df = load_data()
if df.empty:
    st.error("Upload CSV")
    st.stop()

# ── KPIs ──────────────────────────────────────────
nr = df["Net_Revenue_AUD000"].sum()
gp = df["Gross_Profit_AUD000"].sum()
ebitda = df["EBITDA_AUD000"].sum()
cogs = df["COGS_AUD000"].sum()
opex = df["OPEX_AUD000"].sum()

# ── CHART 1 ───────────────────────────────────────
c1, c2, c3 = st.columns(3)

with c1:
    rev = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
    fig = go.Figure()
    fig.add_bar(x=rev["Market"], y=rev["Net_Revenue_AUD000"], name="Revenue")
    fig.add_bar(x=rev["Market"], y=rev["Gross_Profit_AUD000"], name="GP")
    fig.add_bar(x=rev["Market"], y=rev["EBITDA_AUD000"], name="EBITDA")

    fig.update_layout(**PLOTLY_LAYOUT, barmode="group", title="P&L by Market")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().reset_index()
    fig2 = go.Figure(go.Bar(x=cat["Net_Revenue_AUD000"], y=cat["Category"], orientation="h"))
    fig2.update_layout(**PLOTLY_LAYOUT, title="Revenue by Category")
    st.plotly_chart(fig2, use_container_width=True)

with c3:
    wfall = {
        "Base NR": df["Base_NR_AUD000"].sum(),
        "Trade Promo": -df["Trade_Promo_AUD000"].sum(),
        "Net Revenue": nr,
        "COGS": -cogs,
        "Gross Profit": gp,
        "OPEX": -opex,
        "EBITDA": ebitda,
    }

    fig3 = go.Figure(go.Bar(
        x=list(wfall.keys()),
        y=list(wfall.values())
    ))

    fig3.update_layout(**PLOTLY_LAYOUT, title="P&L Bridge")
    fig3.update_xaxes(tickangle=-30)

    st.plotly_chart(fig3, use_container_width=True)

# ── TREND CHART (FIXED) ───────────────────────────
trend = df.groupby(["Year","Month_Num","Month"])[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
trend = trend.sort_values(["Year","Month_Num"])
trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"]

fig4 = go.Figure()

fig4.add_scatter(x=trend["Period"], y=trend["Net_Revenue_AUD000"], mode="lines", name="Revenue")
fig4.add_scatter(x=trend["Period"], y=trend["Gross_Profit_AUD000"], mode="lines", name="GP")
fig4.add_scatter(x=trend["Period"], y=trend["EBITDA_AUD000"], mode="lines", name="EBITDA")

fig4.update_layout(**PLOTLY_LAYOUT, title="Monthly Trend")

# ✅ FIXED indentation + axis handling
fig4.update_xaxes(tickangle=-45, nticks=12)

st.plotly_chart(fig4, use_container_width=True)

# ── AI CFO (GEMINI KEPT) ─────────────────────────
def ai_cfo(question):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "No API Key"

    import google.generativeai as genai
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are CFO.
    Revenue: {nr}
    GP: {gp}
    EBITDA: {ebitda}

    Question: {question}
    Give insights.
    """

    res = model.generate_content(prompt)
    return res.text

st.markdown("## 🤖 AI CFO")
q = st.text_input("Ask question")
if st.button("Ask"):
    st.write(ai_cfo(q))