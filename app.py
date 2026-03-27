import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# --- CHAT MEMORY ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def generate_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    # 🔥 TITLE
    content.append(Paragraph("<b>Unilever APAC - CFO Report</b>", styles["Title"]))
    content.append(Spacer(1, 12))

    # 🔥 BODY
    for line in text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 8))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Unilever APAC | CFO Command Centre",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
  font-family: 'DM Mono', monospace;
  background-color: #080c14;
  color: #e2e8f0;
}

  /* ── Sidebar ── */
  section[data-testid="stSidebar"] {
    background: #0d1117;
    border-right: 1px solid #1e2a3a;
  }
  section[data-testid="stSidebar"] * { color: #94a3b8 !important; }
  section[data-testid="stSidebar"] .stSelectbox label,
  section[data-testid="stSidebar"] h2,
  section[data-testid="stSidebar"] h3 { color: #38bdf8 !important; }

  /* Make sidebar toggle button always visible & styled */
  button[data-testid="collapsedControl"] {
    background: #0ea5e9 !important;
    border-radius: 0 6px 6px 0 !important;
    color: #fff !important;
    top: 50% !important;
  }
  button[data-testid="collapsedControl"] svg { fill: #fff !important; }

  .main .block-container { padding: 1.5rem 2rem; max-width: 100%; }

  /* ── Header ── */
  .dash-header {
    display: flex; align-items: baseline; gap: 16px;
    border-bottom: 1px solid #1e2a3a; padding-bottom: 1rem; margin-bottom: 1.5rem;
  }
  .dash-title {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 2.2rem;

  background: linear-gradient(90deg, #00c6ff, #0072ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;

  letter-spacing: -0.5px;
}
  .sub-highlight {
  color: #38bdf8;
  font-weight: 600;
}

.sub-muted {
  color: #64748b;
  margin-left: 8px;
}
.dash-sub {
  font-size: 0.75rem;
  margin-top: 4px;
}
  /* ── KPI Cards ── */
  .kpi-grid  { display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-bottom: 1.5rem; }
  .kpi-grid-2{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-bottom: 1.8rem; }
  .kpi-card {
    background: #0d1117; border: 1px solid #1e2a3a; border-radius: 10px;
    padding: 16px 18px; position: relative; overflow: hidden; transition: border-color 0.2s;
  }
  .kpi-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: var(--accent);
  }
  .kpi-card:hover { border-color: var(--accent); }
  .kpi-label { font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: #64748b; margin-bottom: 6px; }
  .kpi-value { font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 700; color: #f0f6ff; }
  .kpi-delta { font-size: 0.7rem; margin-top: 4px; }
  .kpi-delta.pos { color: #34d399; }
  .kpi-delta.neg { color: #f87171; }
  .kpi-delta.neu { color: #94a3b8; }

  /* ── Section labels ── */
  .section-label {
    font-family: 'Syne', sans-serif; font-size: 0.7rem;
    letter-spacing: 3px; text-transform: uppercase; color: #38bdf8;
    margin: 1.5rem 0 0.75rem; border-left: 3px solid #38bdf8; padding-left: 10px;
  }

  /* ── Text boxes ── */
  .commentary-box {
    background: #0d1117; border: 1px solid #1e2a3a; border-left: 3px solid #38bdf8;
    border-radius: 10px; padding: 18px 20px; font-size: 0.82rem; line-height: 1.8; color: #cbd5e1;
  }
  .commentary-box strong { color: #38bdf8; }
  .ai-answer {
    background: #0f172a; border: 1px solid #1e3a5f;
    border-radius: 10px; padding: 16px 20px; font-size: 0.82rem; line-height: 1.8; color: #bae6fd;
  }

  /* ── Badge ── */
  .badge {
    display: inline-block; background: #0f172a; border: 1px solid #1e2a3a;
    border-radius: 4px; padding: 2px 8px; font-size: 0.6rem; letter-spacing: 1.5px;
    color: #475569; text-transform: uppercase;
  }

  /* ── Buttons ── */
  .stButton > button {
    background: #0ea5e9; color: #fff; border: none; border-radius: 6px;
    font-family: 'DM Mono', monospace; font-size: 0.75rem; letter-spacing: 1px;
    padding: 8px 20px; transition: background 0.2s;
  }
  .stButton > button:hover { background: #38bdf8; }

  /* ── Text input ── */
  .stTextInput input {
    background: #0d1117 !important; border: 1px solid #1e2a3a !important;
    color: #e2e8f0 !important; border-radius: 6px !important;
    font-family: 'DM Mono', monospace !important;
  }

  div[data-testid="metric-container"] { display: none; }
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: visible !important; }

/* ===== BUTTON HIGHLIGHT ===== */

/* Ask CFO Button */
div[data-testid="stSidebar"] button:first-child {
    background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
}

/* Clear Button */
div[data-testid="stSidebar"] button:last-child {
    background: linear-gradient(135deg, #ff4b2b, #ff416c) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── PLOTLY BASE THEME (no xaxis/yaxis — set per chart) ───────────────────────
PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Mono, monospace", color="#94a3b8", size=11),
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
)
AXIS = dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", tickfont=dict(size=10))
PALETTE = ["#38bdf8","#818cf8","#34d399","#fb923c","#f472b6","#a78bfa","#facc15","#2dd4bf"]

# ── DATA LOAD ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    for path in ["unilever_fpna.csv", "data.csv"]:
        if os.path.exists(path):
            return pd.read_csv(path)
    uploaded = st.file_uploader("Upload unilever_fpna.csv", type=["csv"])
    if uploaded:
        return pd.read_csv(uploaded)
    return pd.DataFrame()

df_raw = load_data()
if df_raw.empty:
    st.error("⚠️ Please upload unilever_fpna.csv to continue.")
    st.stop()

# --- SIDEBAR ---------------------------------------------------------------
with st.sidebar:

    # --- HEADER ---
    st.markdown("## ⚙️ Filters")
    st.caption("Use the ◀ arrow on the left edge to reopen if closed.")

    # --- FILTER FUNCTION ---
    def filt(label, col):
        opts = ["All"] + sorted(df_raw[col].dropna().unique().tolist())
        return st.selectbox(label, opts)

    # --- FILTERS ---
    f_year     = filt("🗓️ Year", "Year")
    f_quarter  = filt("📊 Quarter", "Quarter")
    f_market   = filt("🌍 Market", "Market")
    f_category = filt("🏷️ Category", "Category")
    f_brand    = filt("💎 Brand", "Brand")
    f_channel  = filt("🛒 Channel", "Channel")
    f_type     = filt("📄 Type", "Type")

    st.markdown("---")

    # --- AI CFO INPUT ---
    st.markdown("### 💬 Ask the AI CFO")
    st.caption("Powered by Google Gemini (free)")
    st.caption("💡 Try: revenue, margin, growth, risk, variance...")

    question = st.text_input(
        "",
        placeholder="e.g. Why is margin declining?"
    )

    # --- BUTTONS (UX OPTIMIZED) ---
    col1, col2 = st.columns([2, 1])  # 🔥 Bigger Ask button

    with col1:
        ask_btn = st.button("🚀 Ask CFO", use_container_width=True)

    with col2:
        clear_btn = st.button("🧹 Clear", use_container_width=True)

    # --- CLEAR CHAT SAFELY ---
    if clear_btn:
        if "chat_history" in st.session_state:
            st.session_state.chat_history = []

# ── FILTER ────────────────────────────────────────────────────────────────────
df = df_raw.copy()
if f_year     != "All": df = df[df["Year"]     == int(f_year)]
if f_quarter  != "All": df = df[df["Quarter"]  == f_quarter]
if f_market   != "All": df = df[df["Market"]   == f_market]
if f_category != "All": df = df[df["Category"] == f_category]
if f_brand    != "All": df = df[df["Brand"]    == f_brand]
if f_channel  != "All": df = df[df["Channel"]  == f_channel]
if f_type     != "All": df = df[df["Type"]     == f_type]

if df.empty:
    st.warning("No data for selected filters."); st.stop()

# ── KPI CALCS ─────────────────────────────────────────────────────────────────
nr        = df["Net_Revenue_AUD000"].sum()
gp        = df["Gross_Profit_AUD000"].sum()
ebitda    = df["EBITDA_AUD000"].sum()
cogs      = df["COGS_AUD000"].sum()
opex      = df["OPEX_AUD000"].sum()
volume    = df["Volume_Units"].sum()
base_nr   = df["Base_NR_AUD000"].sum()
trade_pr  = df["Trade_Promo_AUD000"].sum()
budget_nr = df["Budget_NR_AUD000"].sum()
var_nr    = df["Variance_NR_AUD000"].sum()
py_nr     = df["PY_NR_AUD000"].sum()

gp_margin     = gp / nr * 100      if nr     else 0
ebitda_margin = ebitda / nr * 100  if nr     else 0
cogs_pct      = cogs / nr * 100    if nr     else 0
opex_pct      = opex / nr * 100    if nr     else 0
trade_pct     = trade_pr / base_nr * 100 if base_nr else 0
yoy_growth    = (nr - py_nr) / py_nr * 100 if py_nr  else 0
budget_ach    = nr / budget_nr * 100 if budget_nr else 0
var_pct       = var_nr / budget_nr * 100 if budget_nr else 0

def dc(v): return "pos" if v > 0 else ("neg" if v < 0 else "neu")
def fmt_m(v): return f"AUD {v/1000:,.1f}M" if abs(v) >= 1000 else f"AUD {v:,.0f}K"

top_market = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmax()
top_brand  = df.groupby("Brand")["Net_Revenue_AUD000"].sum().idxmax()
risk_mkt   = df.groupby("Market")["Variance_NR_AUD000"].sum().idxmin()

# --- HEADER ---
st.markdown(f"""
<div class="dash-header" style="display:flex; align-items:center;">

  <div>
    <div class="dash-title">Fincy Intelligence</div>

    <div class="dash-sub">
      <span class="sub-highlight">AI CFO</span> |
      <span class="sub-highlight">Data Intelligence</span> |
      <span class="sub-highlight">FP&amp;A Decision Engine</span>
      <span class="sub-muted"> | {len(df):,} Transactions</span>
    </div>
  </div>

  <div style="margin-left:auto">
    <span class="badge">Live Dashboard</span>
  </div>

</div>
""", unsafe_allow_html=True)

# --- KPI ROW 1 ---
arrow = "▲" if yoy_growth > 0 else "▼"
yoy_text = f"{abs(yoy_growth):.1f}% YoY"

cogs_class = "neg" if cogs_pct > 55 else "pos"
opex_class = "neg" if opex_pct > 20 else "pos"

st.markdown(f"""
<div class="kpi-grid">

<div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-label">Net Revenue</div>
    <div class="kpi-value">{fmt_m(nr)}</div>
    <div class="kpi-delta {dc(yoy_growth)}">
        {arrow} {yoy_text}
    </div>
</div>

<div class="kpi-card" style="--accent:#fb923c">
    <div class="kpi-label">COGS</div>
    <div class="kpi-value">{fmt_m(cogs)}</div>
    <div class="kpi-delta {cogs_class}">
        COGS % NR {cogs_pct:.1f}%
    </div>
</div>

<div class="kpi-card" style="--accent:#f472b6">
    <div class="kpi-label">OPEX</div>
    <div class="kpi-value">{fmt_m(opex)}</div>
    <div class="kpi-delta {opex_class}">
        OPEX % NR {opex_pct:.1f}%
    </div>
</div>

</div>
""", unsafe_allow_html=True)

# ── KPI ROW 2 ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Commercial Performance</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="kpi-grid-2">
  <div class="kpi-card" style="--accent:#facc15">
    <div class="kpi-label">Volume Units</div>
    <div class="kpi-value">{volume/1000:,.0f}K</div>
    <div class="kpi-delta neu">Total sold units</div>
  </div>
  <div class="kpi-card" style="--accent:#2dd4bf">
    <div class="kpi-label">Budget Achievement</div>
    <div class="kpi-value">{budget_ach:.1f}%</div>
    <div class="kpi-delta {dc(budget_ach-100)}">vs Budget {fmt_m(budget_nr)}</div>
  </div>
  <div class="kpi-card" style="--accent:#a78bfa">
    <div class="kpi-label">NR Variance vs Bdgt</div>
    <div class="kpi-value">{fmt_m(var_nr)}</div>
    <div class="kpi-delta {dc(var_nr)}">{var_pct:+.1f}% vs budget</div>
  </div>
  <div class="kpi-card" style="--accent:#f87171">
    <div class="kpi-label">Trade Promo Spend</div>
    <div class="kpi-value">{fmt_m(trade_pr)}</div>
    <div class="kpi-delta {'neg' if trade_pct>10 else 'pos'}">TPR% {trade_pct:.1f}% of Base NR</div>
  </div>
  <div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-label">YoY Growth</div>
    <div class="kpi-value">{yoy_growth:+.1f}%</div>
    <div class="kpi-delta {dc(yoy_growth)}">PY NR {fmt_m(py_nr)}</div>
  </div>
</div>""", unsafe_allow_html=True)

# ── CHARTS ROW 1 ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Revenue & Profit Breakdown</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns([2, 2, 1.5])

with c1:
    rev_mkt = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
    fig1 = go.Figure()
    for col, color in zip(["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"],
                          ["#38bdf8","#34d399","#818cf8"]):
        fig1.add_bar(x=rev_mkt["Market"], y=rev_mkt[col],
                     name=col.replace("_AUD000","").replace("_"," "), marker_color=color)
    fig1.update_layout(**PLOTLY_BASE, title="P&L by Market", barmode="group", height=280,
                       xaxis=AXIS, yaxis=AXIS)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    rev_cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().reset_index().sort_values("Net_Revenue_AUD000", ascending=True)
    fig2 = go.Figure(go.Bar(
        x=rev_cat["Net_Revenue_AUD000"], y=rev_cat["Category"], orientation="h",
        marker_color=PALETTE[:len(rev_cat)],
        text=rev_cat["Net_Revenue_AUD000"].apply(fmt_m),
        textposition="auto", textfont=dict(size=10, color="#fff")
    ))
    fig2.update_layout(**PLOTLY_BASE, title="Net Revenue by Category", height=280,
                       xaxis=AXIS, yaxis=AXIS)
    st.plotly_chart(fig2, use_container_width=True)

with c3:
    wfall = {"Base NR": base_nr, "Trade Promo": -trade_pr, "Net Revenue": nr,
             "COGS": -cogs, "Gross Profit": gp, "OPEX": -opex, "EBITDA": ebitda}
    labels = list(wfall.keys())
    values = list(wfall.values())
    fig3 = go.Figure(go.Bar(
        x=labels, y=values,
        marker_color=["#38bdf8" if v > 0 else "#f87171" for v in values]
    ))
    fig3.update_layout(**PLOTLY_BASE, title="P&L Bridge", height=280,
                       xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
    st.plotly_chart(fig3, use_container_width=True)

# ── CHARTS ROW 2 ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Trend & Mix Analysis</div>', unsafe_allow_html=True)
c4, c5 = st.columns([3, 2])

with c4:
    trend = df.groupby(["Year","Month_Num","Month"])[
        ["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]
    ].sum().reset_index().sort_values(["Year","Month_Num"])
    trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"]
    fig4 = go.Figure()
    for col, color, name in zip(
        ["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"],
        ["#38bdf8","#34d399","#818cf8"],
        ["Net Revenue","Gross Profit","EBITDA"]
    ):
        fig4.add_scatter(x=trend["Period"], y=trend[col], mode="lines",
                         name=name, line=dict(color=color, width=2))
    fig4.update_layout(**PLOTLY_BASE, title="Monthly Trend: Revenue → EBITDA", height=280,
                       xaxis=dict(tickangle=-45, nticks=12, **AXIS), yaxis=AXIS)
    st.plotly_chart(fig4, use_container_width=True)

with c5:
    ch_mix = df.groupby("Channel")["Net_Revenue_AUD000"].sum().reset_index()
    fig5 = go.Figure(go.Pie(
        labels=ch_mix["Channel"], values=ch_mix["Net_Revenue_AUD000"],
        hole=0.55, marker=dict(colors=PALETTE, line=dict(color="#0d1117", width=2)),
        textinfo="label+percent", textfont=dict(size=10),
    ))
    fig5.update_layout(**PLOTLY_BASE, title="Revenue Mix by Channel", height=280, showlegend=False)
    st.plotly_chart(fig5, use_container_width=True)

# ── CHARTS ROW 3 ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Brand & Variance Intelligence</div>', unsafe_allow_html=True)
c6, c7 = st.columns([3, 2])

with c6:
    brand_kpi = df.groupby("Brand").agg(
        NR=("Net_Revenue_AUD000","sum"), GP=("Gross_Profit_AUD000","sum"),
        Budget=("Budget_NR_AUD000","sum"), Variance=("Variance_NR_AUD000","sum")
    ).reset_index()
    brand_kpi["GP_Margin"] = (brand_kpi["GP"] / brand_kpi["NR"] * 100).round(1)
    brand_kpi["Bdgt_Ach"]  = (brand_kpi["NR"] / brand_kpi["Budget"] * 100).round(1)
    brand_kpi = brand_kpi.sort_values("NR", ascending=False)

    fig6 = make_subplots(specs=[[{"secondary_y": True}]])
    fig6.add_bar(x=brand_kpi["Brand"], y=brand_kpi["NR"],
                 name="Net Revenue", marker_color="#38bdf8", secondary_y=False)
    fig6.add_scatter(x=brand_kpi["Brand"], y=brand_kpi["GP_Margin"],
                     mode="lines+markers", name="GP Margin %",
                     line=dict(color="#34d399", width=2), marker=dict(size=8), secondary_y=True)
    fig6.update_layout(**PLOTLY_BASE, title="Brand: Revenue vs GP Margin", height=300,
                       xaxis=AXIS, yaxis=AXIS)
    fig6.update_yaxes(title_text="GP Margin %", secondary_y=True, gridcolor="#1e2a3a")
    st.plotly_chart(fig6, use_container_width=True)

with c7:
    var_mkt = df.groupby("Market")["Variance_NR_AUD000"].sum().reset_index().sort_values("Variance_NR_AUD000")
    fig7 = go.Figure(go.Bar(
        x=var_mkt["Variance_NR_AUD000"], y=var_mkt["Market"], orientation="h",
        marker_color=["#f87171" if v < 0 else "#34d399" for v in var_mkt["Variance_NR_AUD000"]],
        text=var_mkt["Variance_NR_AUD000"].apply(lambda x: f"{x:+,.0f}"),
        textposition="auto", textfont=dict(size=10, color="#fff")
    ))
    fig7.update_layout(**PLOTLY_BASE, title="NR Variance vs Budget by Market", height=300,
                       xaxis=AXIS, yaxis=AXIS)
    st.plotly_chart(fig7, use_container_width=True)

# ── BRAND SCORECARD ───────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Brand Scorecard</div>', unsafe_allow_html=True)
scorecard = brand_kpi[["Brand","NR","GP","GP_Margin","Budget","Variance","Bdgt_Ach"]].copy()
scorecard.columns = ["Brand","Net Rev (K)","Gross Profit (K)","GP Margin %","Budget (K)","Variance (K)","Budget Ach %"]
for col in ["Net Rev (K)","Gross Profit (K)","Budget (K)","Variance (K)"]:
    scorecard[col] = scorecard[col].apply(lambda x: f"{x:,.0f}")
scorecard["GP Margin %"]  = scorecard["GP Margin %"].apply(lambda x: f"{x:.1f}%")
scorecard["Budget Ach %"] = scorecard["Budget Ach %"].apply(lambda x: f"{x:.1f}%")
st.dataframe(scorecard, use_container_width=True, hide_index=True)

# ── BOARD COMMENTARY ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Board Commentary</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="commentary-box">
  <strong>Executive Summary</strong><br>
  Net Revenue stands at <strong>{fmt_m(nr)}</strong> with YoY growth of <strong>{yoy_growth:+.1f}%</strong>
  against a prior year base of {fmt_m(py_nr)}.
  Budget achievement is <strong>{budget_ach:.1f}%</strong> with an NR variance of <strong>{fmt_m(var_nr)}</strong>.<br><br>

  <strong>Profitability</strong><br>
  Gross Profit Margin of <strong>{gp_margin:.1f}%</strong> {'exceeds' if gp_margin > 50 else 'is below'} the 50% benchmark.
  EBITDA Margin at <strong>{ebitda_margin:.1f}%</strong>. COGS at {cogs_pct:.1f}% of NR;
  OPEX at {opex_pct:.1f}% of NR. Trade Promo intensity at {trade_pct:.1f}% of Base NR.<br><br>

  <strong>Market & Brand</strong><br>
  <strong>{top_market}</strong> is the top-performing market. <strong>{top_brand}</strong> leads brand revenue.
  <strong>{risk_mkt}</strong> shows the highest budget shortfall and requires corrective action.<br><br>

  <strong>Actions Required</strong><br>
  1. Review trade promo ROI in underperforming markets. &nbsp;
  2. Accelerate online channel growth — currently highest-margin channel. &nbsp;
  3. Tighten OPEX in markets below EBITDA threshold.
</div>""", unsafe_allow_html=True)

# ── RULE-BASED CFO ────────────────────────────────────────────────────────────
def rule_cfo(q):
    q = q.lower()
    if "australia" in q and "revenue" in q:
        v = df[df["Market"]=="Australia"]["Net_Revenue_AUD000"].sum()
        return "Australia Net Revenue: " + fmt_m(v)
    if "top market"  in q: return "Top market by revenue: " + str(top_market)
    if "top brand"   in q: return "Top brand by revenue: " + str(top_brand)
    if "risk"        in q: return "Highest budget risk market: " + str(risk_mkt)
    if "revenue"     in q: return "Total Net Revenue: " + fmt_m(nr)
    if "profit"      in q: return "Gross Profit: " + fmt_m(gp) + " | GP Margin: " + "{:.1f}".format(gp_margin) + "%"
    if "ebitda"      in q: return "EBITDA: " + fmt_m(ebitda) + " | EBITDA Margin: " + "{:.1f}".format(ebitda_margin) + "%"
    if "margin"      in q: return "GP Margin: " + "{:.1f}".format(gp_margin) + "% | EBITDA Margin: " + "{:.1f}".format(ebitda_margin) + "%"
    if "variance"    in q: return "NR Variance vs Budget: " + fmt_m(var_nr) + " (" + "{:+.1f}".format(var_pct) + "%)"
    if "budget"      in q: return "Budget Achievement: " + "{:.1f}".format(budget_ach) + "% | Variance: " + fmt_m(var_nr)
    if "cogs"        in q: return "COGS: " + fmt_m(cogs) + " (" + "{:.1f}".format(cogs_pct) + "% of NR)"
    if "opex"        in q: return "OPEX: " + fmt_m(opex) + " (" + "{:.1f}".format(opex_pct) + "% of NR)"
    if "trade"       in q: return "Trade Promo: " + fmt_m(trade_pr) + " (" + "{:.1f}".format(trade_pct) + "% of Base NR)"
    if "volume"      in q: return "Total Volume: " + "{:,.0f}".format(volume/1000) + "K units"
    if "growth"      in q: return "YoY Revenue Growth: " + "{:+.1f}".format(yoy_growth) + "%"
    if "channel"     in q:
        top_ch = df.groupby("Channel")["Net_Revenue_AUD000"].sum().idxmax()
        return "Top channel by revenue: " + str(top_ch)
    if "category"    in q:
        top_cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().idxmax()
        return "Top category: " + str(top_cat)
    return "Try: revenue, profit, ebitda, margin, variance, budget, cogs, opex, trade, volume, growth, channel, brand, category, top market, risk"

# ——— Groq AI CFO ——————————————————————————————
def ai_cfo(question):
    import os
    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "No API key found"

    try:
        client = Groq(api_key=api_key)

        prompt = f"""
You are the CFO of Unilever APAC. Provide concise, incisive financial insights.

KPI Summary:
- Net Revenue: {fmt_m(nr)} | YoY: {yoy_growth:.1f}%
- Gross Profit: {fmt_m(gp)} | GP Margin: {gp_margin:.1f}%
- EBITDA: {fmt_m(ebitda)} | EBITDA Margin: {ebitda_margin:.1f}%
- COGS % NR: {cogs_pct:.1f}% | OPEX % NR: {opex_pct:.1f}%
- Budget Achievement: {budget_ach:.1f}% | Variance: {fmt_m(var_nr)}
- Trade Promo Intensity: {trade_pct:.1f}%
- Top Market: {top_market} | At-Risk Market: {risk_mkt}
- Top Brand: {top_brand}

Question: {question}

Give 2-3 CFO-level insights with actions.
"""

        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return chat.choices[0].message.content

    except Exception as e:
        return "Groq error: " + str(e)

# --- CHAT HISTORY DISPLAY ---

if st.session_state.chat_history:
    st.markdown("## 💬 CFO Chat History")

    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"""
        <div style="background:#111827;padding:12px;border-radius:10px;margin-bottom:10px">
            <b>👤 You:</b> {chat['question']}<br><br>
            <b>🧠 AI CFO:</b><br>{chat['answer']}
        </div>
        """, unsafe_allow_html=True)

# --- AI CFO SECTION ------------------------------------------------------

if ask_btn and question:

    st.markdown("### 🤖 AI CFO Insight")

    # Rule-Based
    st.markdown("📊 Rule-Based Answer")
    st.markdown('<div class="commentary-box">' + rule_cfo(question) + '</div>', unsafe_allow_html=True)

    # AI CFO
    st.markdown("🧠 AI CFO")
    with st.spinner("AI CFO is thinking..."):
        ai_ans = ai_cfo(question)

    # ✅ SHOW ANSWER
    st.markdown('<div class="ai-answer">' + ai_ans + '</div>', unsafe_allow_html=True)

    # ✅ SAVE CHAT (MOVE HERE)
    st.session_state.chat_history.append({
        "question": question,
        "answer": ai_ans
    })

    # ✅ PDF DOWNLOAD
    if ai_ans:
        pdf = generate_pdf(ai_ans)

        st.download_button(
            label="📄 Download CFO Report",
            data=pdf,
            file_name="CFO_Report.pdf",
            mime="application/pdf"
        )

else:
    st.markdown("""
    <div class="commentary-box" style="opacity:0.5;font-size:0.75rem">
    ← Type a question in the sidebar and click <strong>Ask CFO</strong>.<br>
    Try: revenue, profit, ebitda, margin, variance, budget, growth, top market, risk…
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;font-size:0.6rem;color:#1e2a3a;letter-spacing:2px">
  UNILEVER APAC · CFO COMMAND CENTRE · CONFIDENTIAL · FP&A INTELLIGENCE PLATFORM
</div>""", unsafe_allow_html=True)
