import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fincy Intelligence | AI CFO Platform",
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

section[data-testid="stSidebar"] {
  background: #0d1117;
  border-right: 1px solid #1e2a3a;
}
section[data-testid="stSidebar"] * { color: #94a3b8 !important; }
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 { color: #38bdf8 !important; }

button[data-testid="collapsedControl"] {
  background: #0ea5e9 !important;
  border-radius: 0 6px 6px 0 !important;
  color: #fff !important;
  top: 50% !important;
}
button[data-testid="collapsedControl"] svg { fill: #fff !important; }

.main .block-container { padding: 1.5rem 2rem; max-width: 100%; }

.dash-header { text-align: center; margin-bottom: 25px; }
.dash-title {
  font-size: 3.2rem; font-weight: 800; margin-bottom: 8px;
  background: linear-gradient(90deg, #38bdf8, #6366f1);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.dash-sub { font-size: 1rem; margin-bottom: 6px; margin-top: 8px; }
.sub-muted { color: #94a3b8; }
.sub-highlight { color: #38bdf8; font-weight: 600; }
.dash-author { font-size: 0.9rem; color: #94a3b8; margin-top: 4px; }

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

.section-label {
  font-family: 'Syne', sans-serif; font-size: 0.7rem;
  letter-spacing: 3px; text-transform: uppercase; color: #38bdf8;
  margin: 1.5rem 0 0.75rem; border-left: 3px solid #38bdf8; padding-left: 10px;
}

.commentary-box {
  background: #0d1117; border: 1px solid #1e2a3a; border-left: 3px solid #38bdf8;
  border-radius: 10px; padding: 18px 20px; font-size: 0.82rem; line-height: 1.8; color: #cbd5e1;
}
.commentary-box strong { color: #38bdf8; }
.ai-answer {
  background: #0f172a; border: 1px solid #1e3a5f;
  border-radius: 10px; padding: 16px 20px; font-size: 0.82rem; line-height: 1.8; color: #bae6fd;
}

.stButton > button {
  background: #0ea5e9; color: #fff; border: none; border-radius: 6px;
  font-family: 'DM Mono', monospace; font-size: 0.75rem; letter-spacing: 1px;
  padding: 8px 20px; transition: background 0.2s;
}
.stButton > button:hover { background: #38bdf8; }

.stTextInput input {
  background: #0d1117 !important; border: 1px solid #1e2a3a !important;
  color: #e2e8f0 !important; border-radius: 6px !important;
  font-family: 'DM Mono', monospace !important;
}

div[data-testid="metric-container"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: visible !important; }

div[data-testid="stSidebar"] button:first-child {
  background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
  color: #ffffff !important; font-weight: 700 !important; border-radius: 10px !important;
}
div[data-testid="stSidebar"] button:last-child {
  background: linear-gradient(135deg, #ff4b2b, #ff416c) !important;
  color: #ffffff !important; font-weight: 700 !important; border-radius: 10px !important;
}

.mapper-box {
  background: #0d1117; border: 1px solid #1e2a3a; border-left: 3px solid #6366f1;
  border-radius: 10px; padding: 20px; margin-bottom: 20px;
}

/* Module selector cards */
.module-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-top: 28px; max-width: 860px; margin-left: auto; margin-right: auto;
}
.module-card {
  background: #0d1117; border: 1px solid #1e2a3a; border-radius: 14px;
  padding: 28px 24px; cursor: pointer; transition: border-color 0.25s, transform 0.25s;
  text-align: left;
}
.module-card:hover { border-color: var(--mc, #38bdf8); transform: translateY(-3px); }
.module-card::before { content:''; display:block; width:32px; height:3px; background:var(--mc,#38bdf8); border-radius:2px; margin-bottom:14px; }
.module-icon { font-size: 1.8rem; margin-bottom: 10px; }
.module-title { font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; color:#f0f6ff; margin-bottom:6px; }
.module-desc { font-size:0.75rem; color:#64748b; line-height:1.7; }
.module-badge { display:inline-block; margin-top:10px; font-size:0.6rem; letter-spacing:2px; text-transform:uppercase; color:var(--mc,#38bdf8); border:1px solid var(--mc,#38bdf8); padding:2px 8px; border-radius:4px; }

/* Recon styles */
.recon-match { color:#34d399; font-weight:600; }
.recon-break { color:#f87171; font-weight:600; }
.recon-summary { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:1.5rem; }
.rag-green { background:#052e16; border:1px solid #34d399; border-radius:8px; padding:14px; text-align:center; }
.rag-amber { background:#1c1400; border:1px solid #facc15; border-radius:8px; padding:14px; text-align:center; }
.rag-red   { background:#1f0707; border:1px solid #f87171; border-radius:8px; padding:14px; text-align:center; }
.rag-blue  { background:#0a1628; border:1px solid #38bdf8; border-radius:8px; padding:14px; text-align:center; }
.rag-label { font-size:0.6rem; letter-spacing:2px; text-transform:uppercase; color:#64748b; margin-bottom:6px; }
.rag-value { font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:700; }

/* Budget tracker styles */
.rag-pill-green { display:inline-block; background:#052e16; color:#34d399; border:1px solid #34d399; border-radius:100px; padding:2px 10px; font-size:0.65rem; letter-spacing:1px; }
.rag-pill-amber { display:inline-block; background:#1c1400; color:#facc15; border:1px solid #facc15; border-radius:100px; padding:2px 10px; font-size:0.65rem; letter-spacing:1px; }
.rag-pill-red   { display:inline-block; background:#1f0707; color:#f87171; border:1px solid #f87171; border-radius:100px; padding:2px 10px; font-size:0.65rem; letter-spacing:1px; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE INIT ─────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "col_map" not in st.session_state:
    st.session_state.col_map = {}
if "mapping_confirmed" not in st.session_state:
    st.session_state.mapping_confirmed = False
if "active_module" not in st.session_state:
    st.session_state.active_module = None

PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Mono, monospace", color="#94a3b8", size=11),
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
)
AXIS = dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", tickfont=dict(size=10))
PALETTE = ["#38bdf8","#818cf8","#34d399","#fb923c","#f472b6","#a78bfa","#facc15","#2dd4bf"]

# ── REQUIRED COLUMNS ──────────────────────────────────────────────────────────
REQUIRED_COLS = {
    "Net_Revenue":      "Net Revenue",
    "Gross_Profit":     "Gross Profit",
    "EBITDA":           "EBITDA",
    "COGS":             "COGS",
    "OPEX":             "OPEX",
    "Volume_Units":     "Volume / Units",
    "Base_NR":          "Base Net Revenue",
    "Trade_Promo":      "Trade Promo Spend",
    "Budget_NR":        "Budget Net Revenue",
    "Variance_NR":      "NR Variance vs Budget",
    "PY_NR":            "Prior Year Net Revenue",
}

OPTIONAL_DIMS = {
    "Year":     "Year",
    "Quarter":  "Quarter",
    "Month":    "Month",
    "Month_Num":"Month Number (for sorting)",
    "Market":   "Market / Region",
    "Category": "Category",
    "Brand":    "Brand",
    "Channel":  "Channel",
    "Type":     "Type",
}


# ══════════════════════════════════════════════════════════════════════════════
# PDF GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
def generate_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []
    content.append(Paragraph("<b>Fincy Intelligence - CFO Report</b>", styles["Title"]))
    content.append(Spacer(1, 12))
    for line in text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 8))
    doc.build(content)
    buffer.seek(0)
    return buffer


def fmt_m(v):
    return f"{v/1000:,.1f}M" if abs(v) >= 1000 else f"{v:,.0f}K"

def dc(v): return "pos" if v > 0 else ("neg" if v < 0 else "neu")

def safe_col(df, col, default=0):
    return df[col] if col in df.columns else pd.Series([default] * len(df))


# ══════════════════════════════════════════════════════════════════════════════
# MODULE SELECTOR — HOME SCREEN
# ══════════════════════════════════════════════════════════════════════════════
def show_module_selector():
    st.markdown("""
    <div style="text-align:center; padding: 48px 20px 20px;">
      <div style="font-size:3rem; font-weight:800; background:linear-gradient(90deg,#38bdf8,#6366f1);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:10px;">
        Fincy Intelligence
      </div>
      <div style="color:#94a3b8; font-size:0.9rem; margin-bottom:6px;">
        AI-Powered CFO Decision Platform · Select a module to begin
      </div>
      <div style="color:#475569; font-size:0.72rem;">By Jitendra Parida · Founder, Fincy AI</div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 4, 1])
    with col_c:
        st.markdown("""
        <div class="module-grid">
          <div class="module-card" style="--mc:#38bdf8">
            <div class="module-icon">📊</div>
            <div class="module-title">FP&A Intelligence</div>
            <div class="module-desc">Upload your P&L CSV and get instant KPI dashboards, variance analysis, board commentary, and AI CFO insights powered by Llama 3.1.</div>
            <div class="module-badge">Core Module</div>
          </div>
          <div class="module-card" style="--mc:#34d399">
            <div class="module-icon">🔁</div>
            <div class="module-title">Reconciliation Engine</div>
            <div class="module-desc">Upload two data sources — ERP vs Bank, System A vs System B — and auto-match rows, flag breaks, and download unmatched items instantly.</div>
            <div class="module-badge">New</div>
          </div>
          <div class="module-card" style="--mc:#facc15">
            <div class="module-icon">🎯</div>
            <div class="module-title">Budget vs Actuals Tracker</div>
            <div class="module-desc">RAG-status variance tracker with month-by-month drill-down, traffic light reporting, and AI-generated commentary for your board pack.</div>
            <div class="module-badge">New</div>
          </div>
          <div class="module-card" style="--mc:#f472b6">
            <div class="module-icon">💡</div>
            <div class="module-title">Cost Intelligence</div>
            <div class="module-desc">Deep-dive COGS and OPEX analysis with benchmark flags, cost-per-unit trends, and AI-driven cost reduction recommendations.</div>
            <div class="module-badge">New</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button("📊 FP&A Intelligence", use_container_width=True):
                st.session_state.active_module = "fpa"
                st.rerun()
        with c2:
            if st.button("🔁 Reconciliation Engine", use_container_width=True):
                st.session_state.active_module = "recon"
                st.rerun()
        with c3:
            if st.button("🎯 Budget vs Actuals", use_container_width=True):
                st.session_state.active_module = "budget"
                st.rerun()
        with c4:
            if st.button("💡 Cost Intelligence", use_container_width=True):
                st.session_state.active_module = "cost"
                st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1: FP&A INTELLIGENCE (original code — unchanged)
# ══════════════════════════════════════════════════════════════════════════════

def upload_section():
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px;">
      <div style="font-size:3rem; font-weight:800; background:linear-gradient(90deg,#38bdf8,#6366f1);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:10px;">
        Fincy Intelligence
      </div>
      <div style="color:#94a3b8; font-size:0.9rem; margin-bottom:30px;">
        FP&A Intelligence · Upload your P&L data to begin
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        uploaded = st.file_uploader(
            "📂 Upload your Financial Data (CSV)",
            type=["csv"],
            help="Upload any CSV with financial data. You'll map columns in the next step."
        )
        st.markdown("""
        <div style="color:#475569; font-size:0.72rem; margin-top:10px; text-align:center;">
          Your data stays in your session only. Nothing is stored on our servers.
        </div>
        """, unsafe_allow_html=True)
        if st.button("← Back to Modules", use_container_width=True):
            st.session_state.active_module = None
            st.rerun()
    return uploaded


def column_mapper(df):
    st.markdown('<div class="section-label">Map Your Columns</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mapper-box">
      <div style="color:#94a3b8; font-size:0.8rem; margin-bottom:12px;">
        Match your CSV columns to the financial metrics Fincy Intelligence needs.<br>
        <span style="color:#f87171">★ Required</span> &nbsp;|&nbsp;
        <span style="color:#94a3b8">○ Optional (enables richer analysis)</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    csv_cols = ["— skip —"] + list(df.columns)
    col_map = {}

    st.markdown("#### ★ Financial Metrics (Required)")
    r1, r2, r3 = st.columns(3)
    req_items = list(REQUIRED_COLS.items())

    for i, (key, label) in enumerate(req_items):
        col = [r1, r2, r3][i % 3]
        with col:
            guess = next((c for c in df.columns if key.lower().replace("_","") in c.lower().replace("_","")), csv_cols[0])
            default_idx = csv_cols.index(guess) if guess in csv_cols else 0
            col_map[key] = st.selectbox(f"★ {label}", csv_cols, index=default_idx, key=f"map_{key}")

    st.markdown("#### ○ Dimensions (Optional but Recommended)")
    d1, d2, d3 = st.columns(3)
    dim_items = list(OPTIONAL_DIMS.items())

    for i, (key, label) in enumerate(dim_items):
        col = [d1, d2, d3][i % 3]
        with col:
            guess = next((c for c in df.columns if key.lower() in c.lower()), "— skip —")
            default_idx = csv_cols.index(guess) if guess in csv_cols else 0
            col_map[key] = st.selectbox(f"○ {label}", csv_cols, index=default_idx, key=f"map_{key}")

    confirm = st.button("✅ Confirm Mapping & Launch Dashboard", use_container_width=True)
    return col_map, confirm


def apply_mapping(df_raw, col_map):
    rename = {}
    for internal, csv_col in col_map.items():
        if csv_col and csv_col != "— skip —":
            rename[csv_col] = internal
    df = df_raw.rename(columns=rename)
    return df


def build_sidebar(df_raw, col_map):
    with st.sidebar:
        row_count = len(df_raw)
        st.markdown(f"""
<div class="dash-header">
  <div class="dash-title">Fincy Intelligence</div>
  <div class="dash-sub">
    <span class="sub-highlight">AI CFO</span> |
    <span class="sub-highlight">Data Intelligence</span> |
    <span class="sub-highlight">FP&A Engine</span> |
    <span class="sub-muted">{row_count:,} Rows</span>
  </div>
  <div class="dash-author">By Jitendra Parida · Founder, Fincy AI</div>
</div>
""", unsafe_allow_html=True)

        def filt(label, key):
            if key in col_map and col_map[key] != "— skip —" and key in df_raw.columns:
                opts = ["All"] + sorted(df_raw[key].dropna().unique().tolist())
                return st.selectbox(label, opts)
            return "All"

        f_year     = filt("🗓️ Year",     "Year")
        f_quarter  = filt("📊 Quarter",  "Quarter")
        f_market   = filt("🌍 Market",   "Market")
        f_category = filt("🏷️ Category", "Category")
        f_brand    = filt("💎 Brand",    "Brand")
        f_channel  = filt("🛒 Channel",  "Channel")
        f_type     = filt("📄 Type",     "Type")

        st.markdown("---")

        if st.button("🏠 Back to Modules", use_container_width=True):
            for key in ["df_raw", "col_map", "mapping_confirmed", "chat_history"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.session_state.active_module = None
            st.rerun()

        if st.button("🔄 Upload New Data", use_container_width=True):
            for key in ["df_raw", "col_map", "mapping_confirmed", "chat_history"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

        st.markdown("### 💬 Ask the AI CFO")
        st.caption("Powered by Groq (Llama 3.1)")
        question = st.text_input("", placeholder="e.g. Why is margin declining?")

        col1, col2 = st.columns([2, 1])
        with col1:
            ask_btn = st.button("🚀 Ask CFO", use_container_width=True)
        with col2:
            clear_btn = st.button("🧹 Clear", use_container_width=True)

        if clear_btn:
            st.session_state.chat_history = []

    return f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type, question, ask_btn


def apply_filters(df, col_map, f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type):
    if f_year     != "All" and "Year"     in df.columns: df = df[df["Year"]     == int(f_year)]
    if f_quarter  != "All" and "Quarter"  in df.columns: df = df[df["Quarter"]  == f_quarter]
    if f_market   != "All" and "Market"   in df.columns: df = df[df["Market"]   == f_market]
    if f_category != "All" and "Category" in df.columns: df = df[df["Category"] == f_category]
    if f_brand    != "All" and "Brand"    in df.columns: df = df[df["Brand"]    == f_brand]
    if f_channel  != "All" and "Channel"  in df.columns: df = df[df["Channel"]  == f_channel]
    if f_type     != "All" and "Type"     in df.columns: df = df[df["Type"]     == f_type]
    return df


def calc_kpis(df):
    def s(col): return safe_col(df, col).sum()
    nr        = s("Net_Revenue")
    gp        = s("Gross_Profit")
    ebitda    = s("EBITDA")
    cogs      = s("COGS")
    opex      = s("OPEX")
    volume    = s("Volume_Units")
    base_nr   = s("Base_NR")
    trade_pr  = s("Trade_Promo")
    budget_nr = s("Budget_NR")
    var_nr    = s("Variance_NR")
    py_nr     = s("PY_NR")

    gp_margin     = gp / nr * 100      if nr     else 0
    ebitda_margin = ebitda / nr * 100  if nr     else 0
    cogs_pct      = cogs / nr * 100    if nr     else 0
    opex_pct      = opex / nr * 100    if nr     else 0
    trade_pct     = trade_pr / base_nr * 100 if base_nr else 0
    yoy_growth    = (nr - py_nr) / py_nr * 100 if py_nr  else 0
    budget_ach    = nr / budget_nr * 100 if budget_nr else 0
    var_pct       = var_nr / budget_nr * 100 if budget_nr else 0

    return dict(
        nr=nr, gp=gp, ebitda=ebitda, cogs=cogs, opex=opex,
        volume=volume, base_nr=base_nr, trade_pr=trade_pr,
        budget_nr=budget_nr, var_nr=var_nr, py_nr=py_nr,
        gp_margin=gp_margin, ebitda_margin=ebitda_margin,
        cogs_pct=cogs_pct, opex_pct=opex_pct, trade_pct=trade_pct,
        yoy_growth=yoy_growth, budget_ach=budget_ach, var_pct=var_pct
    )


def render_dashboard(df, col_map, k):
    top_market = df.groupby("Market")["Net_Revenue"].sum().idxmax() if "Market" in df.columns and not df.empty else "N/A"
    top_brand  = df.groupby("Brand")["Net_Revenue"].sum().idxmax()  if "Brand"  in df.columns and not df.empty else "N/A"
    risk_mkt   = df.groupby("Market")["Variance_NR"].sum().idxmin() if "Market" in df.columns and "Variance_NR" in df.columns and not df.empty else "N/A"

    st.markdown("""
<div style="text-align:center;margin-top:10px;margin-bottom:20px;">
  <div style="font-size:1.8rem;font-weight:700;color:#38bdf8;letter-spacing:1px;">
    Data & Intelligence Insights
  </div>
  <div style="font-size:0.8rem;color:#94a3b8;margin-top:4px;">
    Real-time FP&A performance powered by AI
  </div>
</div>
""", unsafe_allow_html=True)

    arrow = "▲" if k["yoy_growth"] > 0 else "▼"
    cogs_class = "neg" if k["cogs_pct"] > 55 else "pos"
    opex_class = "neg" if k["opex_pct"] > 20 else "pos"

    st.markdown('<div class="section-label">P&L Headline</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-label">Net Revenue</div>
    <div class="kpi-value">{fmt_m(k['nr'])}</div>
    <div class="kpi-delta {dc(k['yoy_growth'])}">{arrow} {abs(k['yoy_growth']):.1f}% YoY</div>
  </div>
  <div class="kpi-card" style="--accent:#34d399">
    <div class="kpi-label">Gross Profit</div>
    <div class="kpi-value">{fmt_m(k['gp'])}</div>
    <div class="kpi-delta {dc(k['gp_margin']-50)}">GP Margin {k['gp_margin']:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#818cf8">
    <div class="kpi-label">EBITDA</div>
    <div class="kpi-value">{fmt_m(k['ebitda'])}</div>
    <div class="kpi-delta {dc(k['ebitda_margin']-30)}">EBITDA Margin {k['ebitda_margin']:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#fb923c">
    <div class="kpi-label">COGS</div>
    <div class="kpi-value">{fmt_m(k['cogs'])}</div>
    <div class="kpi-delta {cogs_class}">COGS % NR {k['cogs_pct']:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#f472b6">
    <div class="kpi-label">OPEX</div>
    <div class="kpi-value">{fmt_m(k['opex'])}</div>
    <div class="kpi-delta {opex_class}">OPEX % NR {k['opex_pct']:.1f}%</div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Commercial Performance</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid-2">
  <div class="kpi-card" style="--accent:#facc15">
    <div class="kpi-label">Volume Units</div>
    <div class="kpi-value">{k['volume']/1000:,.0f}K</div>
    <div class="kpi-delta neu">Total sold units</div>
  </div>
  <div class="kpi-card" style="--accent:#2dd4bf">
    <div class="kpi-label">Budget Achievement</div>
    <div class="kpi-value">{k['budget_ach']:.1f}%</div>
    <div class="kpi-delta {dc(k['budget_ach']-100)}">vs Budget {fmt_m(k['budget_nr'])}</div>
  </div>
  <div class="kpi-card" style="--accent:#a78bfa">
    <div class="kpi-label">NR Variance vs Bdgt</div>
    <div class="kpi-value">{fmt_m(k['var_nr'])}</div>
    <div class="kpi-delta {dc(k['var_nr'])}">{k['var_pct']:+.1f}% vs budget</div>
  </div>
  <div class="kpi-card" style="--accent:#f87171">
    <div class="kpi-label">Trade Promo Spend</div>
    <div class="kpi-value">{fmt_m(k['trade_pr'])}</div>
    <div class="kpi-delta {'neg' if k['trade_pct']>10 else 'pos'}">TPR% {k['trade_pct']:.1f}% of Base NR</div>
  </div>
  <div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-label">YoY Growth</div>
    <div class="kpi-value">{k['yoy_growth']:+.1f}%</div>
    <div class="kpi-delta {dc(k['yoy_growth'])}">PY NR {fmt_m(k['py_nr'])}</div>
  </div>
</div>""", unsafe_allow_html=True)

    # Charts Row 1
    st.markdown('<div class="section-label">Revenue & Profit Breakdown</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 2, 1.5])

    with c1:
        if "Market" in df.columns:
            rev_mkt = df.groupby("Market")[["Net_Revenue","Gross_Profit","EBITDA"]].sum().reset_index()
            fig1 = go.Figure()
            for col, color, name in zip(
                ["Net_Revenue","Gross_Profit","EBITDA"],
                ["#38bdf8","#34d399","#818cf8"],
                ["Net Revenue","Gross Profit","EBITDA"]
            ):
                if col in rev_mkt.columns:
                    fig1.add_bar(x=rev_mkt["Market"], y=rev_mkt[col], name=name, marker_color=color)
            fig1.update_layout(**PLOTLY_BASE, title="P&L by Market", barmode="group", height=280, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("Map 'Market' column for this chart.")

    with c2:
        if "Category" in df.columns and "Net_Revenue" in df.columns:
            rev_cat = df.groupby("Category")["Net_Revenue"].sum().reset_index().sort_values("Net_Revenue", ascending=True)
            fig2 = go.Figure(go.Bar(
                x=rev_cat["Net_Revenue"], y=rev_cat["Category"], orientation="h",
                marker_color=PALETTE[:len(rev_cat)],
                text=rev_cat["Net_Revenue"].apply(fmt_m),
                textposition="auto", textfont=dict(size=10, color="#fff")
            ))
            fig2.update_layout(**PLOTLY_BASE, title="Net Revenue by Category", height=280, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Map 'Category' column for this chart.")

    with c3:
        nr, gp_v, ebitda_v = k['nr'], k['gp'], k['ebitda']
        base_nr_v, trade_pr_v, cogs_v, opex_v = k['base_nr'], k['trade_pr'], k['cogs'], k['opex']
        wfall = {"Base NR": base_nr_v, "Trade Promo": -trade_pr_v, "Net Revenue": nr,
                 "COGS": -cogs_v, "Gross Profit": gp_v, "OPEX": -opex_v, "EBITDA": ebitda_v}
        labels, values = list(wfall.keys()), list(wfall.values())
        fig3 = go.Figure(go.Bar(
            x=labels, y=values,
            marker_color=["#38bdf8" if v > 0 else "#f87171" for v in values]
        ))
        fig3.update_layout(**PLOTLY_BASE, title="P&L Bridge", height=280,
                           xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
        st.plotly_chart(fig3, use_container_width=True)

    # Charts Row 2
    st.markdown('<div class="section-label">Trend & Mix Analysis</div>', unsafe_allow_html=True)
    c4, c5 = st.columns([3, 2])

    with c4:
        has_trend = all(c in df.columns for c in ["Year","Month_Num","Month","Net_Revenue"])
        if has_trend:
            trend = df.groupby(["Year","Month_Num","Month"])[
                [c for c in ["Net_Revenue","Gross_Profit","EBITDA"] if c in df.columns]
            ].sum().reset_index().sort_values(["Year","Month_Num"])
            trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"]
            fig4 = go.Figure()
            for col, color, name in zip(
                ["Net_Revenue","Gross_Profit","EBITDA"],
                ["#38bdf8","#34d399","#818cf8"],
                ["Net Revenue","Gross Profit","EBITDA"]
            ):
                if col in trend.columns:
                    fig4.add_scatter(x=trend["Period"], y=trend[col], mode="lines",
                                     name=name, line=dict(color=color, width=2))
            fig4.update_layout(**PLOTLY_BASE, title="Monthly Trend: Revenue → EBITDA", height=280,
                               xaxis=dict(tickangle=-45, nticks=12, **AXIS), yaxis=AXIS)
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("Map Year, Month, Month_Num, and Net Revenue columns for trend chart.")

    with c5:
        if "Channel" in df.columns and "Net_Revenue" in df.columns:
            ch_mix = df.groupby("Channel")["Net_Revenue"].sum().reset_index()
            fig5 = go.Figure(go.Pie(
                labels=ch_mix["Channel"], values=ch_mix["Net_Revenue"],
                hole=0.55, marker=dict(colors=PALETTE, line=dict(color="#0d1117", width=2)),
                textinfo="label+percent", textfont=dict(size=10),
            ))
            fig5.update_layout(**PLOTLY_BASE, title="Revenue Mix by Channel", height=280, showlegend=False)
            st.plotly_chart(fig5, use_container_width=True)
        else:
            st.info("Map 'Channel' column for this chart.")

    # Charts Row 3
    st.markdown('<div class="section-label">Brand & Variance Intelligence</div>', unsafe_allow_html=True)
    c6, c7 = st.columns([3, 2])

    brand_kpi = None
    with c6:
        if "Brand" in df.columns and "Net_Revenue" in df.columns:
            brand_kpi = df.groupby("Brand").agg(
                NR=("Net_Revenue","sum"), GP=("Gross_Profit","sum") if "Gross_Profit" in df.columns else ("Net_Revenue","sum"),
                Budget=("Budget_NR","sum") if "Budget_NR" in df.columns else ("Net_Revenue","sum"),
                Variance=("Variance_NR","sum") if "Variance_NR" in df.columns else ("Net_Revenue","sum")
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
        else:
            st.info("Map 'Brand' column for this chart.")

    with c7:
        if "Market" in df.columns and "Variance_NR" in df.columns:
            var_mkt = df.groupby("Market")["Variance_NR"].sum().reset_index().sort_values("Variance_NR")
            fig7 = go.Figure(go.Bar(
                x=var_mkt["Variance_NR"], y=var_mkt["Market"], orientation="h",
                marker_color=["#f87171" if v < 0 else "#34d399" for v in var_mkt["Variance_NR"]],
                text=var_mkt["Variance_NR"].apply(lambda x: f"{x:+,.0f}"),
                textposition="auto", textfont=dict(size=10, color="#fff")
            ))
            fig7.update_layout(**PLOTLY_BASE, title="NR Variance vs Budget by Market", height=300,
                               xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig7, use_container_width=True)
        else:
            st.info("Map 'Market' and 'Variance NR' columns for this chart.")

    # Brand Scorecard
    if brand_kpi is not None and "Brand" in df.columns and "Net_Revenue" in df.columns:
        st.markdown('<div class="section-label">Brand Scorecard</div>', unsafe_allow_html=True)
        scorecard = brand_kpi[["Brand","NR","GP","GP_Margin","Budget","Variance","Bdgt_Ach"]].copy()
        scorecard.columns = ["Brand","Net Rev (K)","Gross Profit (K)","GP Margin %","Budget (K)","Variance (K)","Budget Ach %"]
        for col in ["Net Rev (K)","Gross Profit (K)","Budget (K)","Variance (K)"]:
            scorecard[col] = scorecard[col].apply(lambda x: f"{x:,.0f}")
        scorecard["GP Margin %"]  = scorecard["GP Margin %"].apply(lambda x: f"{x:.1f}%")
        scorecard["Budget Ach %"] = scorecard["Budget Ach %"].apply(lambda x: f"{x:.1f}%")
        st.dataframe(scorecard, use_container_width=True, hide_index=True)

    # Board Commentary
    st.markdown('<div class="section-label">Board Commentary</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="commentary-box">
  <strong>Executive Summary</strong><br>
  Net Revenue stands at <strong>{fmt_m(k['nr'])}</strong> with YoY growth of <strong>{k['yoy_growth']:+.1f}%</strong>
  against a prior year base of {fmt_m(k['py_nr'])}.
  Budget achievement is <strong>{k['budget_ach']:.1f}%</strong> with an NR variance of <strong>{fmt_m(k['var_nr'])}</strong>.<br><br>

  <strong>Profitability</strong><br>
  Gross Profit Margin of <strong>{k['gp_margin']:.1f}%</strong> {'exceeds' if k['gp_margin'] > 50 else 'is below'} the 50% benchmark.
  EBITDA Margin at <strong>{k['ebitda_margin']:.1f}%</strong>. COGS at {k['cogs_pct']:.1f}% of NR;
  OPEX at {k['opex_pct']:.1f}% of NR. Trade Promo intensity at {k['trade_pct']:.1f}% of Base NR.<br><br>

  <strong>Market & Brand</strong><br>
  <strong>{top_market}</strong> is the top-performing market. <strong>{top_brand}</strong> leads brand revenue.
  <strong>{risk_mkt}</strong> shows the highest budget shortfall and requires corrective action.<br><br>

  <strong>Actions Required</strong><br>
  1. Review trade promo ROI in underperforming markets. &nbsp;
  2. Accelerate online channel growth — currently highest-margin channel. &nbsp;
  3. Tighten OPEX in markets below EBITDA threshold.
</div>""", unsafe_allow_html=True)

    return top_market, top_brand, risk_mkt


def rule_cfo(q, k, top_market, top_brand, risk_mkt, df):
    q = q.lower()
    if "top market"  in q: return "Top market by revenue: " + str(top_market)
    if "top brand"   in q: return "Top brand by revenue: " + str(top_brand)
    if "risk"        in q: return "Highest budget risk market: " + str(risk_mkt)
    if "revenue"     in q: return "Total Net Revenue: " + fmt_m(k['nr'])
    if "profit"      in q: return f"Gross Profit: {fmt_m(k['gp'])} | GP Margin: {k['gp_margin']:.1f}%"
    if "ebitda"      in q: return f"EBITDA: {fmt_m(k['ebitda'])} | EBITDA Margin: {k['ebitda_margin']:.1f}%"
    if "margin"      in q: return f"GP Margin: {k['gp_margin']:.1f}% | EBITDA Margin: {k['ebitda_margin']:.1f}%"
    if "variance"    in q: return f"NR Variance vs Budget: {fmt_m(k['var_nr'])} ({k['var_pct']:+.1f}%)"
    if "budget"      in q: return f"Budget Achievement: {k['budget_ach']:.1f}% | Variance: {fmt_m(k['var_nr'])}"
    if "cogs"        in q: return f"COGS: {fmt_m(k['cogs'])} ({k['cogs_pct']:.1f}% of NR)"
    if "opex"        in q: return f"OPEX: {fmt_m(k['opex'])} ({k['opex_pct']:.1f}% of NR)"
    if "trade"       in q: return f"Trade Promo: {fmt_m(k['trade_pr'])} ({k['trade_pct']:.1f}% of Base NR)"
    if "volume"      in q: return f"Total Volume: {k['volume']/1000:,.0f}K units"
    if "growth"      in q: return f"YoY Revenue Growth: {k['yoy_growth']:+.1f}%"
    if "channel"     in q and "Channel" in df.columns:
        top_ch = df.groupby("Channel")["Net_Revenue"].sum().idxmax()
        return "Top channel by revenue: " + str(top_ch)
    if "category"    in q and "Category" in df.columns:
        top_cat = df.groupby("Category")["Net_Revenue"].sum().idxmax()
        return "Top category: " + str(top_cat)
    return "Try: revenue, profit, ebitda, margin, variance, budget, cogs, opex, trade, volume, growth, channel, brand, category, top market, risk"


def ai_cfo(question, k, top_market, top_brand, risk_mkt):
    from groq import Groq
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "⚠️ No GROQ_API_KEY found. Set it in your environment or Streamlit secrets."
    try:
        client = Groq(api_key=api_key)
        prompt = f"""
You are a world-class CFO providing decision intelligence. Be concise and incisive.

KPI Summary:
- Net Revenue: {fmt_m(k['nr'])} | YoY: {k['yoy_growth']:.1f}%
- Gross Profit: {fmt_m(k['gp'])} | GP Margin: {k['gp_margin']:.1f}%
- EBITDA: {fmt_m(k['ebitda'])} | EBITDA Margin: {k['ebitda_margin']:.1f}%
- COGS % NR: {k['cogs_pct']:.1f}% | OPEX % NR: {k['opex_pct']:.1f}%
- Budget Achievement: {k['budget_ach']:.1f}% | Variance: {fmt_m(k['var_nr'])}
- Trade Promo Intensity: {k['trade_pct']:.1f}%
- Top Market: {top_market} | At-Risk Market: {risk_mkt}
- Top Brand: {top_brand}

Question: {question}

Give 2-3 CFO-level insights with recommended actions.
"""
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return chat.choices[0].message.content
    except Exception as e:
        return "Groq error: " + str(e)


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2: RECONCILIATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
def run_reconciliation():
    with st.sidebar:
        st.markdown("""
<div style="font-size:1.4rem;font-weight:800;color:#34d399;margin-bottom:4px;">🔁 Recon Engine</div>
<div style="color:#64748b;font-size:0.72rem;margin-bottom:16px;">Match · Break · Reconcile</div>
""", unsafe_allow_html=True)
        if st.button("🏠 Back to Modules", use_container_width=True):
            st.session_state.active_module = None
            for k in ["recon_df1","recon_df2","recon_done"]:
                st.session_state.pop(k, None)
            st.rerun()
        st.markdown("---")
        tolerance = st.number_input("Amount Tolerance (±)", min_value=0.0, value=0.01, step=0.01,
                                     help="Values within this range will be treated as matched")
        match_key_hint = st.text_input("Match Key Column Name", value="",
                                        placeholder="e.g. Invoice_No, Transaction_ID")

    st.markdown("""
<div style="text-align:center;padding:24px 0 16px;">
  <div style="font-size:2rem;font-weight:800;color:#34d399;">🔁 Reconciliation Engine</div>
  <div style="color:#64748b;font-size:0.82rem;margin-top:6px;">
    Upload two data sources · Auto-match · Flag breaks · Download exceptions
  </div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-label">Source A (e.g. ERP / System 1)</div>', unsafe_allow_html=True)
        file1 = st.file_uploader("Upload Source A (CSV)", type=["csv"], key="recon_file1")
    with col2:
        st.markdown('<div class="section-label">Source B (e.g. Bank / System 2)</div>', unsafe_allow_html=True)
        file2 = st.file_uploader("Upload Source B (CSV)", type=["csv"], key="recon_file2")

    if not file1 or not file2:
        st.markdown("""
<div class="commentary-box" style="margin-top:20px;opacity:0.6;font-size:0.75rem;">
  ↑ Upload both CSV files above to begin reconciliation.<br><br>
  <strong>What this module does:</strong><br>
  • Matches rows between two data sources on a common key (e.g. Invoice No, Transaction ID)<br>
  • Flags amount differences beyond your tolerance threshold<br>
  • Identifies records in Source A missing from Source B and vice versa<br>
  • Produces a downloadable exceptions report<br><br>
  <strong>Use cases:</strong> ERP vs Bank statement · GL vs Sub-ledger · PO vs Invoice · Intercompany recon
</div>""", unsafe_allow_html=True)
        return

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    st.markdown('<div class="section-label">Configure Match Key & Amount Columns</div>', unsafe_allow_html=True)
    mc1, mc2, mc3 = st.columns(3)

    all_cols1 = list(df1.columns)
    all_cols2 = list(df2.columns)
    common_cols = [c for c in all_cols1 if c in all_cols2]

    with mc1:
        # Try to auto-detect a good key column
        key_guess = next((c for c in common_cols if any(k in c.lower() for k in
                         ["id","no","number","ref","invoice","transaction","code"])), common_cols[0] if common_cols else all_cols1[0])
        match_key = st.selectbox("Match Key Column", common_cols if common_cols else all_cols1,
                                  index=common_cols.index(key_guess) if key_guess in common_cols else 0)
    with mc2:
        num_cols1 = [c for c in all_cols1 if pd.api.types.is_numeric_dtype(df1[c])]
        amt_guess1 = next((c for c in num_cols1 if any(k in c.lower() for k in ["amount","amt","value","total","net"])), num_cols1[0] if num_cols1 else all_cols1[0])
        amt_col1 = st.selectbox("Amount Column (Source A)", num_cols1 if num_cols1 else all_cols1,
                                 index=num_cols1.index(amt_guess1) if amt_guess1 in num_cols1 else 0)
    with mc3:
        num_cols2 = [c for c in all_cols2 if pd.api.types.is_numeric_dtype(df2[c])]
        amt_guess2 = next((c for c in num_cols2 if any(k in c.lower() for k in ["amount","amt","value","total","net"])), num_cols2[0] if num_cols2 else all_cols2[0])
        amt_col2 = st.selectbox("Amount Column (Source B)", num_cols2 if num_cols2 else all_cols2,
                                 index=num_cols2.index(amt_guess2) if amt_guess2 in num_cols2 else 0)

    if st.button("🔁 Run Reconciliation", use_container_width=True):
        # Merge on key
        merged = pd.merge(
            df1[[match_key, amt_col1]].rename(columns={amt_col1: "Amt_A"}),
            df2[[match_key, amt_col2]].rename(columns={amt_col2: "Amt_B"}),
            on=match_key, how="outer", indicator=True
        )

        def classify(row):
            if row["_merge"] == "left_only":  return "Missing in B"
            if row["_merge"] == "right_only": return "Missing in A"
            diff = abs(row["Amt_A"] - row["Amt_B"])
            if diff <= tolerance:              return "Matched"
            return "Amount Break"

        merged["Status"] = merged.apply(classify, axis=1)
        merged["Difference"] = merged["Amt_A"].fillna(0) - merged["Amt_B"].fillna(0)

        total       = len(merged)
        matched     = (merged["Status"] == "Matched").sum()
        breaks      = (merged["Status"] == "Amount Break").sum()
        missing_b   = (merged["Status"] == "Missing in B").sum()
        missing_a   = (merged["Status"] == "Missing in A").sum()
        match_rate  = matched / total * 100 if total else 0
        total_break = merged.loc[merged["Status"] == "Amount Break", "Difference"].abs().sum()

        # Summary KPIs
        st.markdown('<div class="section-label">Reconciliation Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="recon-summary">
  <div class="rag-green"><div class="rag-label">Matched</div><div class="rag-value" style="color:#34d399;">{matched:,}</div><div style="font-size:0.65rem;color:#34d399;">{match_rate:.1f}% match rate</div></div>
  <div class="rag-red"><div class="rag-label">Amount Breaks</div><div class="rag-value" style="color:#f87171;">{breaks:,}</div><div style="font-size:0.65rem;color:#f87171;">Diff: {total_break:,.2f}</div></div>
  <div class="rag-amber"><div class="rag-label">Missing in B</div><div class="rag-value" style="color:#facc15;">{missing_b:,}</div><div style="font-size:0.65rem;color:#facc15;">In A only</div></div>
  <div class="rag-blue"><div class="rag-label">Missing in A</div><div class="rag-value" style="color:#38bdf8;">{missing_a:,}</div><div style="font-size:0.65rem;color:#38bdf8;">In B only</div></div>
</div>""", unsafe_allow_html=True)

        # Match rate chart
        fig_donut = go.Figure(go.Pie(
            labels=["Matched", "Amount Break", "Missing in B", "Missing in A"],
            values=[matched, breaks, missing_b, missing_a],
            hole=0.65,
            marker=dict(colors=["#34d399","#f87171","#facc15","#38bdf8"],
                        line=dict(color="#0d1117", width=2)),
            textinfo="label+percent", textfont=dict(size=10)
        ))
        fig_donut.add_annotation(text=f"{match_rate:.0f}%<br>Matched",
                                  x=0.5, y=0.5, showarrow=False,
                                  font=dict(size=16, color="#f0f6ff", family="Syne"))
        fig_donut.update_layout(**PLOTLY_BASE, title="Reconciliation Status", height=300, showlegend=True)

        ch1, ch2 = st.columns([1, 2])
        with ch1:
            st.plotly_chart(fig_donut, use_container_width=True)
        with ch2:
            # Difference waterfall by status
            diff_by_status = merged.groupby("Status")["Difference"].sum().reset_index()
            fig_bar = go.Figure(go.Bar(
                x=diff_by_status["Status"],
                y=diff_by_status["Difference"],
                marker_color=["#34d399" if v >= 0 else "#f87171" for v in diff_by_status["Difference"]],
                text=diff_by_status["Difference"].apply(lambda x: f"{x:+,.2f}"),
                textposition="auto"
            ))
            fig_bar.update_layout(**PLOTLY_BASE, title="Net Difference by Status", height=300, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig_bar, use_container_width=True)

        # Exceptions table
        exceptions = merged[merged["Status"] != "Matched"].copy()
        if not exceptions.empty:
            st.markdown('<div class="section-label">Exceptions Detail</div>', unsafe_allow_html=True)

            status_filter = st.multiselect("Filter by Status", ["Amount Break","Missing in B","Missing in A"],
                                            default=["Amount Break","Missing in B","Missing in A"])
            filtered_exc = exceptions[exceptions["Status"].isin(status_filter)]
            st.dataframe(filtered_exc.drop(columns=["_merge"]), use_container_width=True, hide_index=True)

            csv_exc = filtered_exc.drop(columns=["_merge"]).to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Exceptions Report (CSV)", csv_exc,
                               file_name="Fincy_Recon_Exceptions.csv", mime="text/csv")
        else:
            st.success("🎉 Perfect reconciliation — no exceptions found!")

        # Full output
        st.markdown('<div class="section-label">Full Reconciliation Output</div>', unsafe_allow_html=True)
        st.dataframe(merged.drop(columns=["_merge"]), use_container_width=True, hide_index=True)
        full_csv = merged.drop(columns=["_merge"]).to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Full Recon Output (CSV)", full_csv,
                           file_name="Fincy_Recon_Full.csv", mime="text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3: BUDGET VS ACTUALS TRACKER
# ══════════════════════════════════════════════════════════════════════════════
def run_budget_tracker():
    with st.sidebar:
        st.markdown("""
<div style="font-size:1.4rem;font-weight:800;color:#facc15;margin-bottom:4px;">🎯 Budget Tracker</div>
<div style="color:#64748b;font-size:0.72rem;margin-bottom:16px;">RAG · Variance · Board Pack</div>
""", unsafe_allow_html=True)
        if st.button("🏠 Back to Modules", use_container_width=True):
            st.session_state.active_module = None
            for k in ["budget_df"]:
                st.session_state.pop(k, None)
            st.rerun()
        st.markdown("---")
        green_thresh = st.slider("Green threshold (%)", 90, 100, 95)
        amber_thresh = st.slider("Amber threshold (%)", 70, 95, 80)

    st.markdown("""
<div style="text-align:center;padding:24px 0 16px;">
  <div style="font-size:2rem;font-weight:800;color:#facc15;">🎯 Budget vs Actuals Tracker</div>
  <div style="color:#64748b;font-size:0.82rem;margin-top:6px;">
    RAG status · Month-by-month drill · Board-ready commentary
  </div>
</div>
""", unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1,2,1])
    with col_c:
        bfile = st.file_uploader("📂 Upload Budget vs Actuals CSV", type=["csv"], key="budget_file",
                                  help="CSV with columns for Period, Actual, Budget (and optionally Category, Market, Brand)")
        st.markdown("""
<div style="color:#475569;font-size:0.68rem;margin-top:8px;text-align:center;">
  Needs at minimum: a Period/Month column, an Actual column, a Budget column
</div>""", unsafe_allow_html=True)

    if not bfile:
        st.markdown("""
<div class="commentary-box" style="margin-top:20px;opacity:0.6;font-size:0.75rem;">
  ↑ Upload your Budget vs Actuals CSV above.<br><br>
  <strong>What this module does:</strong><br>
  • Calculates variance (£/$ and %) for every row<br>
  • RAG-status flags each line: Green (on/above budget) · Amber (close) · Red (below)<br>
  • Month-by-month trend chart of actual vs budget<br>
  • Category/brand drill-down with variance waterfall<br>
  • Auto-generates board-pack commentary<br>
  • Downloadable RAG report (CSV + PDF)<br><br>
  <strong>Use cases:</strong> Monthly board pack · MBR · QBR · Investor reporting
</div>""", unsafe_allow_html=True)
        return

    df = pd.read_csv(bfile)
    st.markdown('<div class="section-label">Map Columns</div>', unsafe_allow_html=True)
    csv_cols = list(df.columns)

    bc1, bc2, bc3, bc4 = st.columns(4)
    with bc1:
        period_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["period","month","date","year","quarter"])), csv_cols[0])
        period_col = st.selectbox("Period / Month Column", csv_cols, index=csv_cols.index(period_guess))
    with bc2:
        actual_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["actual","actuals","act","real"])), csv_cols[0])
        actual_col = st.selectbox("Actual Column", csv_cols, index=csv_cols.index(actual_guess))
    with bc3:
        budget_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["budget","plan","target","bdgt"])), csv_cols[0])
        budget_col = st.selectbox("Budget Column", csv_cols, index=csv_cols.index(budget_guess))
    with bc4:
        dim_opts = ["— none —"] + csv_cols
        dim_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["category","brand","market","segment","dept"])), "— none —")
        dim_col = st.selectbox("Dimension (optional)", dim_opts, index=dim_opts.index(dim_guess) if dim_guess in dim_opts else 0)

    if st.button("🎯 Run Budget Tracker", use_container_width=True):
        df["_Actual"]  = pd.to_numeric(df[actual_col], errors="coerce").fillna(0)
        df["_Budget"]  = pd.to_numeric(df[budget_col], errors="coerce").fillna(0)
        df["_Var_Abs"] = df["_Actual"] - df["_Budget"]
        df["_Var_Pct"] = df.apply(lambda r: r["_Var_Abs"] / r["_Budget"] * 100 if r["_Budget"] else 0, axis=1)
        df["_Ach_Pct"] = df.apply(lambda r: r["_Actual"] / r["_Budget"] * 100 if r["_Budget"] else 0, axis=1)

        def rag(ach):
            if ach >= green_thresh: return "🟢 Green"
            if ach >= amber_thresh: return "🟡 Amber"
            return "🔴 Red"
        df["_RAG"] = df["_Ach_Pct"].apply(rag)

        total_actual  = df["_Actual"].sum()
        total_budget  = df["_Budget"].sum()
        total_var     = total_actual - total_budget
        total_ach     = total_actual / total_budget * 100 if total_budget else 0
        green_count   = (df["_RAG"] == "🟢 Green").sum()
        red_count     = (df["_RAG"] == "🔴 Red").sum()
        amber_count   = (df["_RAG"] == "🟡 Amber").sum()

        # Summary KPIs
        st.markdown('<div class="section-label">Budget Performance Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="recon-summary">
  <div class="{'rag-green' if total_var>=0 else 'rag-red'}">
    <div class="rag-label">Total Actual</div>
    <div class="rag-value" style="color:{'#34d399' if total_var>=0 else '#f87171'};">{fmt_m(total_actual)}</div>
    <div style="font-size:0.65rem;color:#64748b;">vs Budget {fmt_m(total_budget)}</div>
  </div>
  <div class="{'rag-green' if total_var>=0 else 'rag-red'}">
    <div class="rag-label">Variance</div>
    <div class="rag-value" style="color:{'#34d399' if total_var>=0 else '#f87171'};">{total_var:+,.0f}</div>
    <div style="font-size:0.65rem;color:{'#34d399' if total_var>=0 else '#f87171'};">{total_ach:.1f}% achieved</div>
  </div>
  <div class="rag-green">
    <div class="rag-label">🟢 On Track</div>
    <div class="rag-value" style="color:#34d399;">{green_count}</div>
    <div style="font-size:0.65rem;color:#34d399;">lines</div>
  </div>
  <div class="rag-red">
    <div class="rag-label">🔴 Off Track</div>
    <div class="rag-value" style="color:#f87171;">{red_count}</div>
    <div style="font-size:0.65rem;color:#f87171;">{amber_count} amber</div>
  </div>
</div>""", unsafe_allow_html=True)

        # Trend chart
        st.markdown('<div class="section-label">Actual vs Budget by Period</div>', unsafe_allow_html=True)
        period_grp = df.groupby(period_col)[["_Actual","_Budget","_Var_Abs"]].sum().reset_index()
        fig_trend = go.Figure()
        fig_trend.add_bar(x=period_grp[period_col], y=period_grp["_Budget"],
                          name="Budget", marker_color="rgba(99,102,241,0.4)")
        fig_trend.add_bar(x=period_grp[period_col], y=period_grp["_Actual"],
                          name="Actual", marker_color="#38bdf8")
        fig_trend.add_scatter(x=period_grp[period_col], y=period_grp["_Var_Abs"],
                              name="Variance", mode="lines+markers",
                              line=dict(color="#facc15", width=2, dash="dot"),
                              yaxis="y2")
        fig_trend.update_layout(**PLOTLY_BASE, title="Actual vs Budget by Period",
                                barmode="overlay", height=320,
                                xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS,
                                yaxis2=dict(overlaying="y", side="right", gridcolor="#1e2a3a",
                                            tickfont=dict(size=10), title_text="Variance"))
        st.plotly_chart(fig_trend, use_container_width=True)

        # Dimension breakdown
        if dim_col != "— none —":
            st.markdown('<div class="section-label">Variance by Dimension</div>', unsafe_allow_html=True)
            dim_grp = df.groupby(dim_col)[["_Actual","_Budget","_Var_Abs"]].sum().reset_index()
            dim_grp["_Ach_Pct"] = dim_grp["_Actual"] / dim_grp["_Budget"] * 100
            dim_grp["_RAG"] = dim_grp["_Ach_Pct"].apply(rag)
            dim_grp = dim_grp.sort_values("_Var_Abs")
            fig_dim = go.Figure(go.Bar(
                x=dim_grp["_Var_Abs"], y=dim_grp[dim_col], orientation="h",
                marker_color=["#f87171" if v < 0 else "#34d399" for v in dim_grp["_Var_Abs"]],
                text=dim_grp["_Var_Abs"].apply(lambda x: f"{x:+,.0f}"),
                textposition="auto"
            ))
            fig_dim.update_layout(**PLOTLY_BASE, title=f"Variance by {dim_col}", height=300, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig_dim, use_container_width=True)

        # RAG table
        st.markdown('<div class="section-label">Line-by-Line RAG Status</div>', unsafe_allow_html=True)
        display_cols = [period_col, actual_col, budget_col, "_Var_Abs", "_Var_Pct", "_Ach_Pct", "_RAG"]
        if dim_col != "— none —":
            display_cols = [period_col, dim_col, actual_col, budget_col, "_Var_Abs", "_Var_Pct", "_Ach_Pct", "_RAG"]
        rag_display = df[display_cols].copy()
        rag_display.columns = [c.replace("_Var_Abs","Variance £").replace("_Var_Pct","Var %").replace("_Ach_Pct","Achievement %").replace("_RAG","RAG Status") for c in rag_display.columns]
        st.dataframe(rag_display, use_container_width=True, hide_index=True)

        # Board commentary
        top_over  = period_grp.loc[period_grp["_Var_Abs"].idxmax(), period_col]
        top_under = period_grp.loc[period_grp["_Var_Abs"].idxmin(), period_col]
        st.markdown('<div class="section-label">Auto-Generated Board Commentary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="commentary-box">
  <strong>Budget Performance — Board Summary</strong><br>
  Total actuals of <strong>{fmt_m(total_actual)}</strong> against a budget of <strong>{fmt_m(total_budget)}</strong>,
  delivering a {'favourable' if total_var >= 0 else 'adverse'} variance of <strong>{total_var:+,.0f}</strong>
  ({total_ach:.1f}% budget achievement).<br><br>
  <strong>RAG Overview:</strong> {green_count} lines on track (Green), {amber_count} lines at risk (Amber),
  {red_count} lines off track (Red).<br><br>
  <strong>Period Highlights:</strong> <strong>{top_over}</strong> delivered the strongest performance vs budget.
  <strong>{top_under}</strong> recorded the largest shortfall and requires management attention.<br><br>
  <strong>Recommended Actions:</strong><br>
  1. Investigate root cause for {top_under} — is this a phasing issue or structural underperformance?<br>
  2. Replicate success factors from {top_over} across underperforming periods.<br>
  3. Escalate all 🔴 Red lines to business owners for corrective action plans.
</div>""", unsafe_allow_html=True)

        # Download
        csv_out = rag_display.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download RAG Report (CSV)", csv_out,
                           file_name="Fincy_Budget_RAG_Report.csv", mime="text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 4: COST INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_cost_intelligence():
    with st.sidebar:
        st.markdown("""
<div style="font-size:1.4rem;font-weight:800;color:#f472b6;margin-bottom:4px;">💡 Cost Intelligence</div>
<div style="color:#64748b;font-size:0.72rem;margin-bottom:16px;">COGS · OPEX · Benchmarks · AI Insights</div>
""", unsafe_allow_html=True)
        if st.button("🏠 Back to Modules", use_container_width=True):
            st.session_state.active_module = None
            for k in ["cost_df"]:
                st.session_state.pop(k, None)
            st.rerun()
        st.markdown("---")
        cogs_benchmark = st.slider("COGS Benchmark (% of Revenue)", 20, 80, 50)
        opex_benchmark = st.slider("OPEX Benchmark (% of Revenue)", 5, 40, 20)

    st.markdown("""
<div style="text-align:center;padding:24px 0 16px;">
  <div style="font-size:2rem;font-weight:800;color:#f472b6;">💡 Cost Intelligence</div>
  <div style="color:#64748b;font-size:0.82rem;margin-top:6px;">
    Deep-dive COGS & OPEX · Benchmark flags · AI cost reduction recommendations
  </div>
</div>
""", unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1,2,1])
    with col_c:
        cfile = st.file_uploader("📂 Upload Cost Data CSV", type=["csv"], key="cost_file",
                                  help="CSV with Revenue, COGS, OPEX columns and optional dimensions")

    if not cfile:
        st.markdown("""
<div class="commentary-box" style="margin-top:20px;opacity:0.6;font-size:0.75rem;">
  ↑ Upload your cost data CSV above.<br><br>
  <strong>What this module does:</strong><br>
  • Calculates COGS % and OPEX % of revenue for every row<br>
  • Benchmarks each line against your target thresholds (configurable in sidebar)<br>
  • Identifies your most and least cost-efficient segments<br>
  • Trend analysis of cost ratios over time<br>
  • AI-generated cost reduction recommendations<br>
  • Downloadable cost efficiency report<br><br>
  <strong>Use cases:</strong> Supply chain cost review · Manufacturing cost control · SG&A benchmarking · Procurement analysis
</div>""", unsafe_allow_html=True)
        return

    df = pd.read_csv(cfile)
    st.markdown('<div class="section-label">Map Columns</div>', unsafe_allow_html=True)
    csv_cols = list(df.columns)

    cc1, cc2, cc3, cc4, cc5 = st.columns(5)
    with cc1:
        rev_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["revenue","net_rev","netsales","sales"])), csv_cols[0])
        rev_col = st.selectbox("Revenue Column", csv_cols, index=csv_cols.index(rev_guess))
    with cc2:
        cogs_guess = next((c for c in csv_cols if "cog" in c.lower() or "cost_of" in c.lower()), csv_cols[0])
        cogs_col = st.selectbox("COGS Column", csv_cols, index=csv_cols.index(cogs_guess))
    with cc3:
        opex_guess = next((c for c in csv_cols if "opex" in c.lower() or "operating" in c.lower()), csv_cols[0])
        opex_col = st.selectbox("OPEX Column", csv_cols, index=csv_cols.index(opex_guess))
    with cc4:
        period_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["period","month","date","year","quarter"])), csv_cols[0])
        period_col = st.selectbox("Period Column", csv_cols, index=csv_cols.index(period_guess))
    with cc5:
        dim_opts = ["— none —"] + csv_cols
        dim_guess = next((c for c in csv_cols if any(k in c.lower() for k in ["category","brand","market","segment","sku","product"])), "— none —")
        dim_col = st.selectbox("Segment / SKU (optional)", dim_opts, index=dim_opts.index(dim_guess) if dim_guess in dim_opts else 0)

    if st.button("💡 Run Cost Intelligence", use_container_width=True):
        df["_Rev"]  = pd.to_numeric(df[rev_col],  errors="coerce").fillna(0)
        df["_COGS"] = pd.to_numeric(df[cogs_col], errors="coerce").fillna(0)
        df["_OPEX"] = pd.to_numeric(df[opex_col], errors="coerce").fillna(0)
        df["_GP"]   = df["_Rev"] - df["_COGS"]
        df["_EBITDA"] = df["_GP"] - df["_OPEX"]
        df["_COGS_Pct"] = df.apply(lambda r: r["_COGS"] / r["_Rev"] * 100 if r["_Rev"] else 0, axis=1)
        df["_OPEX_Pct"] = df.apply(lambda r: r["_OPEX"] / r["_Rev"] * 100 if r["_Rev"] else 0, axis=1)
        df["_GP_Margin"] = df.apply(lambda r: r["_GP"] / r["_Rev"] * 100 if r["_Rev"] else 0, axis=1)

        def cost_flag(cogs_pct, opex_pct):
            if cogs_pct > cogs_benchmark or opex_pct > opex_benchmark: return "⚠️ Above Benchmark"
            return "✅ Within Benchmark"
        df["_Flag"] = df.apply(lambda r: cost_flag(r["_COGS_Pct"], r["_OPEX_Pct"]), axis=1)

        tot_rev    = df["_Rev"].sum()
        tot_cogs   = df["_COGS"].sum()
        tot_opex   = df["_OPEX"].sum()
        tot_gp     = df["_GP"].sum()
        tot_ebitda = df["_EBITDA"].sum()
        avg_cogs_pct = tot_cogs / tot_rev * 100 if tot_rev else 0
        avg_opex_pct = tot_opex / tot_rev * 100 if tot_rev else 0
        avg_gp_margin = tot_gp / tot_rev * 100 if tot_rev else 0
        above_bench = (df["_Flag"] == "⚠️ Above Benchmark").sum()

        # Summary KPIs
        st.markdown('<div class="section-label">Cost Performance Summary</div>', unsafe_allow_html=True)
        cogs_ok = avg_cogs_pct <= cogs_benchmark
        opex_ok = avg_opex_pct <= opex_benchmark
        st.markdown(f"""
<div class="recon-summary">
  <div class="{'rag-green' if cogs_ok else 'rag-red'}">
    <div class="rag-label">COGS % Revenue</div>
    <div class="rag-value" style="color:{'#34d399' if cogs_ok else '#f87171'};">{avg_cogs_pct:.1f}%</div>
    <div style="font-size:0.65rem;color:#64748b;">Benchmark: {cogs_benchmark}%</div>
  </div>
  <div class="{'rag-green' if opex_ok else 'rag-red'}">
    <div class="rag-label">OPEX % Revenue</div>
    <div class="rag-value" style="color:{'#34d399' if opex_ok else '#f87171'};">{avg_opex_pct:.1f}%</div>
    <div style="font-size:0.65rem;color:#64748b;">Benchmark: {opex_benchmark}%</div>
  </div>
  <div class="rag-green">
    <div class="rag-label">GP Margin</div>
    <div class="rag-value" style="color:#34d399;">{avg_gp_margin:.1f}%</div>
    <div style="font-size:0.65rem;color:#34d399;">Gross Profit</div>
  </div>
  <div class="{'rag-red' if above_bench > 0 else 'rag-green'}">
    <div class="rag-label">Above Benchmark</div>
    <div class="rag-value" style="color:{'#f87171' if above_bench > 0 else '#34d399'};">{above_bench}</div>
    <div style="font-size:0.65rem;color:#64748b;">lines flagged</div>
  </div>
</div>""", unsafe_allow_html=True)

        # Cost structure chart
        st.markdown('<div class="section-label">Cost Structure Breakdown</div>', unsafe_allow_html=True)
        ch1, ch2 = st.columns(2)
        with ch1:
            period_grp = df.groupby(period_col)[["_Rev","_COGS","_OPEX","_GP"]].sum().reset_index()
            period_grp["_COGS_Pct"] = period_grp["_COGS"] / period_grp["_Rev"] * 100
            period_grp["_OPEX_Pct"] = period_grp["_OPEX"] / period_grp["_Rev"] * 100
            period_grp["_GP_Margin"] = period_grp["_GP"] / period_grp["_Rev"] * 100

            fig_trend = go.Figure()
            fig_trend.add_scatter(x=period_grp[period_col], y=period_grp["_COGS_Pct"],
                                   name="COGS %", mode="lines+markers",
                                   line=dict(color="#f87171", width=2))
            fig_trend.add_scatter(x=period_grp[period_col], y=period_grp["_OPEX_Pct"],
                                   name="OPEX %", mode="lines+markers",
                                   line=dict(color="#facc15", width=2))
            fig_trend.add_scatter(x=period_grp[period_col], y=period_grp["_GP_Margin"],
                                   name="GP Margin %", mode="lines+markers",
                                   line=dict(color="#34d399", width=2))
            fig_trend.add_hline(y=cogs_benchmark, line_dash="dot", line_color="#f87171",
                                annotation_text=f"COGS Benchmark {cogs_benchmark}%")
            fig_trend.add_hline(y=opex_benchmark, line_dash="dot", line_color="#facc15",
                                annotation_text=f"OPEX Benchmark {opex_benchmark}%")
            fig_trend.update_layout(**PLOTLY_BASE, title="Cost Ratios Over Time", height=320,
                                    xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
            st.plotly_chart(fig_trend, use_container_width=True)

        with ch2:
            # Cost waterfall
            waterfall_vals = [tot_rev, -tot_cogs, tot_gp, -tot_opex, tot_ebitda]
            waterfall_lbls = ["Revenue", "COGS", "Gross Profit", "OPEX", "EBITDA"]
            fig_wf = go.Figure(go.Bar(
                x=waterfall_lbls, y=waterfall_vals,
                marker_color=["#38bdf8","#f87171","#34d399","#facc15","#818cf8"]
            ))
            fig_wf.update_layout(**PLOTLY_BASE, title="Cost Waterfall", height=320, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig_wf, use_container_width=True)

        # Segment breakdown
        if dim_col != "— none —":
            st.markdown('<div class="section-label">Cost Efficiency by Segment</div>', unsafe_allow_html=True)
            seg_grp = df.groupby(dim_col)[["_Rev","_COGS","_OPEX","_GP"]].sum().reset_index()
            seg_grp["_COGS_Pct"]  = seg_grp["_COGS"] / seg_grp["_Rev"] * 100
            seg_grp["_OPEX_Pct"]  = seg_grp["_OPEX"] / seg_grp["_Rev"] * 100
            seg_grp["_GP_Margin"] = seg_grp["_GP"]   / seg_grp["_Rev"] * 100
            seg_grp = seg_grp.sort_values("_GP_Margin", ascending=False)

            fig_seg = go.Figure()
            fig_seg.add_bar(x=seg_grp[dim_col], y=seg_grp["_COGS_Pct"],
                            name="COGS %", marker_color="#f87171")
            fig_seg.add_bar(x=seg_grp[dim_col], y=seg_grp["_OPEX_Pct"],
                            name="OPEX %", marker_color="#facc15")
            fig_seg.add_scatter(x=seg_grp[dim_col], y=seg_grp["_GP_Margin"],
                                name="GP Margin %", mode="lines+markers",
                                line=dict(color="#34d399", width=2), yaxis="y2")
            fig_seg.add_hline(y=cogs_benchmark, line_dash="dot", line_color="#f87171")
            fig_seg.update_layout(**PLOTLY_BASE, title=f"Cost Efficiency by {dim_col}",
                                  barmode="stack", height=320, xaxis=AXIS, yaxis=AXIS,
                                  yaxis2=dict(overlaying="y", side="right", gridcolor="#1e2a3a", tickfont=dict(size=10)))
            st.plotly_chart(fig_seg, use_container_width=True)

        # Flagged lines
        flagged = df[df["_Flag"] == "⚠️ Above Benchmark"]
        if not flagged.empty:
            st.markdown('<div class="section-label">⚠️ Lines Above Benchmark</div>', unsafe_allow_html=True)
            show_cols = [period_col, rev_col, cogs_col, opex_col, "_COGS_Pct", "_OPEX_Pct", "_GP_Margin", "_Flag"]
            if dim_col != "— none —":
                show_cols = [period_col, dim_col] + show_cols[1:]
            st.dataframe(flagged[show_cols], use_container_width=True, hide_index=True)

        # AI Recommendations via Groq
        st.markdown('<div class="section-label">🧠 AI Cost Reduction Recommendations</div>', unsafe_allow_html=True)
        worst_seg = ""
        if dim_col != "— none —" and "seg_grp" in dir():
            worst_seg = str(seg_grp.loc[seg_grp["_COGS_Pct"].idxmax(), dim_col])

        if st.button("🧠 Get AI Cost Insights", use_container_width=True):
            try:
                from groq import Groq
                api_key = os.getenv("GROQ_API_KEY")
                if not api_key:
                    st.warning("⚠️ No GROQ_API_KEY found. Set it in Streamlit secrets.")
                else:
                    client = Groq(api_key=api_key)
                    prompt = f"""
You are a world-class CFO and cost management expert.

Cost Analysis Summary:
- Total Revenue: {fmt_m(tot_rev)}
- COGS: {fmt_m(tot_cogs)} ({avg_cogs_pct:.1f}% of revenue) | Benchmark: {cogs_benchmark}%
- OPEX: {fmt_m(tot_opex)} ({avg_opex_pct:.1f}% of revenue) | Benchmark: {opex_benchmark}%
- GP Margin: {avg_gp_margin:.1f}%
- Lines above benchmark: {above_bench}
- Highest cost segment: {worst_seg if worst_seg else 'N/A'}

Provide 3 specific, actionable cost reduction recommendations with expected impact.
Focus on supply chain, procurement, and operational efficiency.
Be concise and CFO-level sharp.
"""
                    with st.spinner("AI is analysing your cost structure..."):
                        chat = client.chat.completions.create(
                            model="llama-3.1-8b-instant",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.3
                        )
                    st.markdown('<div class="ai-answer">' + chat.choices[0].message.content + '</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Groq error: {e}")
        else:
            st.markdown("""
<div class="commentary-box" style="opacity:0.5;font-size:0.75rem;">
  ← Click "Get AI Cost Insights" to get AI-powered cost reduction recommendations based on your data.
</div>""", unsafe_allow_html=True)

        # Download
        dl_cols = [c for c in [period_col, dim_col if dim_col != "— none —" else None, rev_col, cogs_col, opex_col, "_COGS_Pct", "_OPEX_Pct", "_GP_Margin", "_Flag"] if c]
        csv_out = df[dl_cols].to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Cost Intelligence Report (CSV)", csv_out,
                           file_name="Fincy_Cost_Intelligence.csv", mime="text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP ROUTER
# ══════════════════════════════════════════════════════════════════════════════

module = st.session_state.active_module

# No module selected → show home screen
if module is None:
    show_module_selector()
    st.stop()

# ── MODULE: FP&A INTELLIGENCE ─────────────────────────────────────────────────
if module == "fpa":
    if "df_raw" not in st.session_state:
        uploaded = upload_section()
        if uploaded:
            st.session_state.df_raw = pd.read_csv(uploaded)
            st.session_state.mapping_confirmed = False
            st.rerun()
        st.stop()

    df_raw = st.session_state.df_raw

    if not st.session_state.mapping_confirmed:
        st.markdown(f"""
        <div style="text-align:center; padding:20px 0 10px;">
          <div style="font-size:2rem; font-weight:800; color:#38bdf8;">Fincy Intelligence</div>
          <div style="color:#94a3b8; font-size:0.85rem;">Step 2 of 2 · Map your columns</div>
        </div>
        """, unsafe_allow_html=True)
        col_map, confirmed = column_mapper(df_raw)
        if confirmed:
            st.session_state.col_map = col_map
            st.session_state.mapping_confirmed = True
            st.rerun()
        st.stop()

    col_map   = st.session_state.col_map
    df_mapped = apply_mapping(df_raw, col_map)
    f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type, question, ask_btn = build_sidebar(df_mapped, col_map)
    df        = apply_filters(df_mapped, col_map, f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type)

    if df.empty:
        st.warning("No data for selected filters.")
        st.stop()

    k = calc_kpis(df)
    top_market, top_brand, risk_mkt = render_dashboard(df, col_map, k)

    if st.session_state.chat_history:
        st.markdown("## 💬 CFO Chat History")
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f"""
            <div style="background:#111827;padding:12px;border-radius:10px;margin-bottom:10px">
                <b>👤 You:</b> {chat['question']}<br><br>
                <b>🧠 AI CFO:</b><br>{chat['answer']}
            </div>
            """, unsafe_allow_html=True)

    if ask_btn and question:
        st.markdown("### 🤖 AI CFO Insight")
        st.markdown("📊 Rule-Based Answer")
        st.markdown('<div class="commentary-box">' + rule_cfo(question, k, top_market, top_brand, risk_mkt, df) + '</div>', unsafe_allow_html=True)
        st.markdown("🧠 AI CFO")
        with st.spinner("AI CFO is thinking..."):
            ai_ans = ai_cfo(question, k, top_market, top_brand, risk_mkt)
        st.markdown('<div class="ai-answer">' + ai_ans + '</div>', unsafe_allow_html=True)
        st.session_state.chat_history.append({"question": question, "answer": ai_ans})
        if ai_ans:
            pdf = generate_pdf(ai_ans)
            st.download_button(label="📄 Download CFO Report", data=pdf,
                               file_name="Fincy_CFO_Report.pdf", mime="application/pdf")
    else:
        st.markdown("""
        <div class="commentary-box" style="opacity:0.5;font-size:0.75rem">
        ← Type a question in the sidebar and click <strong>Ask CFO</strong>.<br>
        Try: revenue, profit, ebitda, margin, variance, budget, growth, top market, risk…
        </div>
        """, unsafe_allow_html=True)

# ── MODULE: RECONCILIATION ────────────────────────────────────────────────────
elif module == "recon":
    run_reconciliation()

# ── MODULE: BUDGET TRACKER ────────────────────────────────────────────────────
elif module == "budget":
    run_budget_tracker()

# ── MODULE: COST INTELLIGENCE ─────────────────────────────────────────────────
elif module == "cost":
    run_cost_intelligence()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;font-size:0.6rem;color:#1e2a3a;letter-spacing:2px">
  FINCY INTELLIGENCE · AI CFO PLATFORM · CONFIDENTIAL · FP&A DECISION ENGINE
</div>""", unsafe_allow_html=True)
