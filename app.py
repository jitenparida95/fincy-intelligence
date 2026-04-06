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

if "col_map" not in st.session_state:
    st.session_state.col_map = {}

if "mapping_confirmed" not in st.session_state:
    st.session_state.mapping_confirmed = False


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
</style>
""", unsafe_allow_html=True)

PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Mono, monospace", color="#94a3b8", size=11),
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
)
AXIS = dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", tickfont=dict(size=10))
PALETTE = ["#38bdf8","#818cf8","#34d399","#fb923c","#f472b6","#a78bfa","#facc15","#2dd4bf"]

# ── REQUIRED COLUMNS (internal names → display names) ────────────────────────
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

# ── FILE UPLOAD ───────────────────────────────────────────────────────────────
def upload_section():
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px;">
      <div style="font-size:3rem; font-weight:800; background:linear-gradient(90deg,#38bdf8,#6366f1);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:10px;">
        Fincy Intelligence
      </div>
      <div style="color:#94a3b8; font-size:0.9rem; margin-bottom:30px;">
        AI-Powered CFO Decision Intelligence · Upload your financial data to begin
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
    return uploaded


# ── COLUMN MAPPER ─────────────────────────────────────────────────────────────
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
            # Auto-detect best guess
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


# ── APPLY MAPPING ─────────────────────────────────────────────────────────────
def apply_mapping(df_raw, col_map):
    """Rename mapped columns to internal standard names."""
    rename = {}
    for internal, csv_col in col_map.items():
        if csv_col and csv_col != "— skip —":
            rename[csv_col] = internal
    df = df_raw.rename(columns=rename)
    return df


def safe_col(df, col, default=0):
    return df[col] if col in df.columns else pd.Series([default] * len(df))


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
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

        # Reset data
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


# ── FILTERS ───────────────────────────────────────────────────────────────────
def apply_filters(df, col_map, f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type):
    if f_year     != "All" and "Year"     in df.columns: df = df[df["Year"]     == int(f_year)]
    if f_quarter  != "All" and "Quarter"  in df.columns: df = df[df["Quarter"]  == f_quarter]
    if f_market   != "All" and "Market"   in df.columns: df = df[df["Market"]   == f_market]
    if f_category != "All" and "Category" in df.columns: df = df[df["Category"] == f_category]
    if f_brand    != "All" and "Brand"    in df.columns: df = df[df["Brand"]    == f_brand]
    if f_channel  != "All" and "Channel"  in df.columns: df = df[df["Channel"]  == f_channel]
    if f_type     != "All" and "Type"     in df.columns: df = df[df["Type"]     == f_type]
    return df


# ── KPI CALCS ─────────────────────────────────────────────────────────────────
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


def fmt_m(v):
    return f"{v/1000:,.1f}M" if abs(v) >= 1000 else f"{v:,.0f}K"

def dc(v): return "pos" if v > 0 else ("neg" if v < 0 else "neu")


# ── DASHBOARD ─────────────────────────────────────────────────────────────────
def render_dashboard(df, col_map, k):
    # Detect top/risk dims
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

    # ── KPI ROW 1 ─────────────────────────────────────────────────────────────
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

    # ── KPI ROW 2 ─────────────────────────────────────────────────────────────
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

    # ── CHARTS ROW 1 ──────────────────────────────────────────────────────────
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

    # ── CHARTS ROW 2 ──────────────────────────────────────────────────────────
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

    # ── CHARTS ROW 3 ──────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Brand & Variance Intelligence</div>', unsafe_allow_html=True)
    c6, c7 = st.columns([3, 2])

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

    # ── BRAND SCORECARD ───────────────────────────────────────────────────────
    if "Brand" in df.columns and "Net_Revenue" in df.columns:
        st.markdown('<div class="section-label">Brand Scorecard</div>', unsafe_allow_html=True)
        scorecard = brand_kpi[["Brand","NR","GP","GP_Margin","Budget","Variance","Bdgt_Ach"]].copy()
        scorecard.columns = ["Brand","Net Rev (K)","Gross Profit (K)","GP Margin %","Budget (K)","Variance (K)","Budget Ach %"]
        for col in ["Net Rev (K)","Gross Profit (K)","Budget (K)","Variance (K)"]:
            scorecard[col] = scorecard[col].apply(lambda x: f"{x:,.0f}")
        scorecard["GP Margin %"]  = scorecard["GP Margin %"].apply(lambda x: f"{x:.1f}%")
        scorecard["Budget Ach %"] = scorecard["Budget Ach %"].apply(lambda x: f"{x:.1f}%")
        st.dataframe(scorecard, use_container_width=True, hide_index=True)

    # ── BOARD COMMENTARY ──────────────────────────────────────────────────────
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


# ── AI CFO ────────────────────────────────────────────────────────────────────
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
# MAIN APP FLOW
# ══════════════════════════════════════════════════════════════════════════════

# Step 1: Upload
if "df_raw" not in st.session_state:
    uploaded = upload_section()
    if uploaded:
        st.session_state.df_raw = pd.read_csv(uploaded)
        st.session_state.mapping_confirmed = False
        st.rerun()
    st.stop()

df_raw = st.session_state.df_raw

# Step 2: Column Mapping
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

# Step 3: Dashboard
col_map = st.session_state.col_map
df_mapped = apply_mapping(df_raw, col_map)

# Sidebar
f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type, question, ask_btn = build_sidebar(df_mapped, col_map)

# Filter
df = apply_filters(df_mapped, col_map, f_year, f_quarter, f_market, f_category, f_brand, f_channel, f_type)

if df.empty:
    st.warning("No data for selected filters.")
    st.stop()

# KPIs
k = calc_kpis(df)

# Render
top_market, top_brand, risk_mkt = render_dashboard(df, col_map, k)

# ── CHAT HISTORY ──────────────────────────────────────────────────────────────
if st.session_state.chat_history:
    st.markdown("## 💬 CFO Chat History")
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"""
        <div style="background:#111827;padding:12px;border-radius:10px;margin-bottom:10px">
            <b>👤 You:</b> {chat['question']}<br><br>
            <b>🧠 AI CFO:</b><br>{chat['answer']}
        </div>
        """, unsafe_allow_html=True)

# ── AI CFO SECTION ────────────────────────────────────────────────────────────
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
        st.download_button(
            label="📄 Download CFO Report",
            data=pdf,
            file_name="Fincy_CFO_Report.pdf",
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
  FINCY INTELLIGENCE · AI CFO PLATFORM · CONFIDENTIAL · FP&A DECISION ENGINE
</div>""", unsafe_allow_html=True)
