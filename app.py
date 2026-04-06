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
    page_title="Fincy Intelligence | CFO Command Centre",
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
.dash-sub { font-size: 1.05rem; margin-bottom: 6px; }
.sub-muted { color: #94a3b8; }
.dash-sub { font-size: 1rem; margin-top: 8px; }
.dash-author { font-size: 0.9rem; color: #94a3b8; margin-top: 4px; }
.sub-highlight { color: #38bdf8; font-weight: 600; }
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
.badge {
  display: inline-block; background: #0f172a; border: 1px solid #1e2a3a;
  border-radius: 4px; padding: 2px 8px; font-size: 0.6rem; letter-spacing: 1.5px;
  color: #475569; text-transform: uppercase;
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
.upload-box {
  background: #0d1117; border: 2px dashed #1e3a5f; border-radius: 12px;
  padding: 24px; text-align: center; margin-bottom: 20px;
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
</style>
""", unsafe_allow_html=True)

# ── PLOTLY BASE THEME ─────────────────────────────────────────────────────────
PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Mono, monospace", color="#94a3b8", size=11),
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
)
AXIS = dict(gridcolor="#1e2a3a", linecolor="#1e2a3a", tickfont=dict(size=10))
PALETTE = ["#38bdf8","#818cf8","#34d399","#fb923c","#f472b6","#a78bfa","#facc15","#2dd4bf"]

# ══════════════════════════════════════════════════════════════════════════════
# ── CSV UPLOAD & COLUMN MAPPING SECTION ──────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

# Required columns for Fincy to work
REQUIRED_COLS = {
    "Net_Revenue_AUD000": "Net Revenue",
    "Gross_Profit_AUD000": "Gross Profit",
    "EBITDA_AUD000": "EBITDA",
    "COGS_AUD000": "COGS",
    "OPEX_AUD000": "OPEX",
    "Volume_Units": "Volume / Units",
    "Base_NR_AUD000": "Base Net Revenue",
    "Trade_Promo_AUD000": "Trade Promo Spend",
    "Budget_NR_AUD000": "Budget Net Revenue",
    "Variance_NR_AUD000": "NR Variance vs Budget",
    "PY_NR_AUD000": "Prior Year Net Revenue",
    "Year": "Year",
    "Quarter": "Quarter",
    "Month": "Month",
    "Month_Num": "Month Number",
    "Market": "Market / Region",
    "Category": "Category",
    "Brand": "Brand",
    "Channel": "Channel",
    "Type": "Type",
}

def show_upload_section():
    """Renders the CSV upload + column mapping UI. Returns mapped DataFrame or None."""

    st.markdown("""
    <div style="text-align:center; margin: 30px 0 10px;">
      <div style="font-size:2rem; font-weight:800; background: linear-gradient(90deg,#38bdf8,#6366f1);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
        Fincy Intelligence
      </div>
      <div style="color:#94a3b8; font-size:0.85rem; margin-top:6px;">
        Upload your P&L data to get started
      </div>
    </div>
    """, unsafe_allow_html=True)

    tab2, tab1 = st.tabs(["📋 Use Demo Data", "📂 Upload Your CSV"])

    with tab1:

        # ── SAMPLE TEMPLATE DOWNLOAD ─────────────────────────────────────
        sample_data = {
            "Year": [2024, 2024, 2024],
            "Quarter": ["Q1", "Q1", "Q2"],
            "Month": ["Jan", "Feb", "Mar"],
            "Month_Num": [1, 2, 3],
            "Market": ["India", "India", "India"],
            "Category": ["Home Care", "Home Care", "Personal Care"],
            "Brand": ["Brand A", "Brand B", "Brand A"],
            "Channel": ["Modern Trade", "E-Commerce", "Modern Trade"],
            "Type": ["Actual", "Actual", "Actual"],
            "Net_Revenue_AUD000": [5000, 4200, 5500],
            "Gross_Profit_AUD000": [2500, 2100, 2750],
            "EBITDA_AUD000": [1500, 1200, 1650],
            "COGS_AUD000": [2500, 2100, 2750],
            "OPEX_AUD000": [1000, 900, 1100],
            "Volume_Units": [10000, 8500, 11000],
            "Base_NR_AUD000": [5200, 4400, 5700],
            "Trade_Promo_AUD000": [200, 200, 200],
            "Budget_NR_AUD000": [5100, 4300, 5600],
            "Variance_NR_AUD000": [-100, -100, -100],
            "PY_NR_AUD000": [4800, 4000, 5200],
        }
        import io
        sample_df = __import__("pandas").DataFrame(sample_data)
        csv_buffer = io.StringIO()
        sample_df.to_csv(csv_buffer, index=False)
        csv_bytes = csv_buffer.getvalue().encode()

        col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
        with col_dl2:
            st.download_button(
                label="📥 Download Sample CSV Template",
                data=csv_bytes,
                file_name="fincy_sample_template.csv",
                mime="text/csv",
                use_container_width=True,
                help="Download this template, fill in your data, then upload below"
            )
            st.caption("👆 Fill this template with your data, then upload below")

        st.markdown("""
        <div class="upload-box">
          <div style="font-size:2rem;">📊</div>
          <div style="color:#38bdf8; font-weight:600; margin:8px 0;">Upload your P&L CSV or Excel file</div>
          <div style="color:#64748b; font-size:0.75rem;">Supports .csv and .xlsx · Max 200MB</div>
        </div>
        """, unsafe_allow_html=True)

        uploaded = st.file_uploader(
            "Drop your file here",
            type=["csv", "xlsx"],
            label_visibility="collapsed"
        )

        if uploaded:
            try:
                if uploaded.name.endswith(".xlsx"):
                    raw = pd.read_excel(uploaded)
                else:
                    raw = pd.read_csv(uploaded)

                st.success(f"✅ Loaded **{len(raw):,} rows** × **{len(raw.columns)} columns**")

                with st.expander("👁️ Preview your data (first 5 rows)"):
                    st.dataframe(raw.head(), use_container_width=True)

                # ── COLUMN MAPPING ────────────────────────────────────────
                st.markdown("### 🗂️ Map Your Columns to Fincy Fields")
                st.caption("Match your column names to what Fincy expects. Skip any that don't apply.")

                user_cols = ["-- Skip --"] + list(raw.columns)
                mapping = {}

                col_pairs = list(REQUIRED_COLS.items())
                # Display in 2-column grid
                for i in range(0, len(col_pairs), 2):
                    c1, c2 = st.columns(2)
                    for col_widget, (fincy_col, label) in zip([c1, c2], col_pairs[i:i+2]):
                        with col_widget:
                            # Auto-detect: try to find a matching column name
                            auto = next(
                                (c for c in raw.columns if fincy_col.lower().replace("_aud000","").replace("_","") in c.lower().replace(" ","")),
                                "-- Skip --"
                            )
                            selected = st.selectbox(
                                f"**{label}**",
                                user_cols,
                                index=user_cols.index(auto) if auto in user_cols else 0,
                                key=f"map_{fincy_col}"
                            )
                            if selected != "-- Skip --":
                                mapping[fincy_col] = selected

                if st.button("🚀 Launch Fincy with My Data", use_container_width=True):
                    # Validate minimum required columns
                    min_required = ["Net_Revenue_AUD000", "Year", "Market"]
                    missing = [REQUIRED_COLS[m] for m in min_required if m not in mapping]
                    if missing:
                        st.error(f"⚠️ Please map at minimum: **{', '.join(missing)}**")
                    else:
                        # Build mapped dataframe
                        df_mapped = pd.DataFrame()
                        for fincy_col, user_col in mapping.items():
                            df_mapped[fincy_col] = raw[user_col]

                        # Fill missing optional columns with 0
                        for col in REQUIRED_COLS:
                            if col not in df_mapped.columns:
                                df_mapped[col] = 0

                        # Ensure numeric columns
                        numeric_cols = [c for c in REQUIRED_COLS if c not in ["Year","Quarter","Month","Month_Num","Market","Category","Brand","Channel","Type"]]
                        for col in numeric_cols:
                            df_mapped[col] = pd.to_numeric(df_mapped[col], errors="coerce").fillna(0)

                        # Ensure Month_Num exists
                        if "Month_Num" not in mapping and "Month" in mapping:
                            month_map = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
                                        "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
                            df_mapped["Month_Num"] = df_mapped["Month"].map(month_map).fillna(0).astype(int)

                        st.session_state["fincy_data"] = df_mapped
                        st.session_state["company_name"] = uploaded.name.replace(".csv","").replace(".xlsx","").title()
                        st.session_state["show_upload"] = False
                        st.rerun()

            except Exception as e:
                st.error(f"Error reading file: {e}")

    with tab2:
        st.info("📌 Click below to load the sample FMCG APAC P&L dataset.")
        if st.button("▶️ Launch Demo Dashboard", use_container_width=True):
            for demo_path in ["unilever_fpna.csv", "data.csv"]:
                if os.path.exists(demo_path):
                    st.session_state["fincy_data"] = pd.read_csv(demo_path)
                    st.session_state["company_name"] = "FMCG Co. APAC"
                    st.session_state["show_upload"] = False
                    st.rerun()
            st.error("⚠️ Demo file not found on server.")

    return None


# ══════════════════════════════════════════════════════════════════════════════
# ── MAIN APP LOGIC ────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

# Auto-load demo data on first visit; show upload screen if flagged or no demo file
if st.session_state.get("show_upload", False):
    show_upload_section()
    st.stop()

if "fincy_data" not in st.session_state:
    loaded = False
    for demo_path in ["unilever_fpna.csv", "data.csv"]:
        if os.path.exists(demo_path):
            st.session_state["fincy_data"] = pd.read_csv(demo_path)
            st.session_state["company_name"] = "FMCG Co. APAC"
            loaded = True
            break
    if not loaded:
        show_upload_section()
        st.stop()

df_raw = st.session_state["fincy_data"]
company_name = st.session_state.get("company_name", "Your Company")

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
<div class="dash-header">
  <div class="dash-title">Fincy Intelligence</div>
  <div class="dash-sub">
    <span class="sub-highlight">AI CFO</span> |
    <span class="sub-highlight">Data Intelligence</span> |
    <span class="sub-highlight">FP&A Engine</span> |
    <span class="sub-muted">{len(df_raw):,} Transactions</span>
  </div>
  <div class="dash-author">By Jitendra Parida • Founder, Fincy AI & Data Intelligence</div>
</div>
""", unsafe_allow_html=True)

    # Reset / Upload new data button
    if st.button("📂 Upload New Data", use_container_width=True):
        for key in ["fincy_data", "company_name", "chat_history"]:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state["show_upload"] = True
        st.rerun()

    st.markdown("---")

    def filt(label, col):
        if col not in df_raw.columns:
            return "All"
        opts = ["All"] + sorted(df_raw[col].dropna().unique().tolist())
        return st.selectbox(label, opts)

    f_year     = filt("🗓️ Year", "Year")
    f_quarter  = filt("📊 Quarter", "Quarter")
    f_market   = filt("🌍 Market", "Market")
    f_category = filt("🏷️ Category", "Category")
    f_brand    = filt("💎 Brand", "Brand")
    f_channel  = filt("🛒 Channel", "Channel")
    f_type     = filt("📄 Type", "Type")

    st.markdown("---")

    st.markdown("### 💬 Ask the AI CFO")
    st.caption("Powered by Groq (LLaMA 3)")
    st.caption("💡 Try: revenue, margin, growth, risk, variance...")

    question = st.text_input("", placeholder="e.g. Why is margin declining?")

    col1, col2 = st.columns([2, 1])
    with col1:
        ask_btn = st.button("🚀 Ask CFO", use_container_width=True)
    with col2:
        clear_btn = st.button("🧹 Clear", use_container_width=True)

    if clear_btn:
        st.session_state.chat_history = []

# ── FILTER ────────────────────────────────────────────────────────────────────
df = df_raw.copy()
if f_year     != "All": df = df[df["Year"]     == int(f_year)]     if "Year"     in df.columns else df
if f_quarter  != "All": df = df[df["Quarter"]  == f_quarter]       if "Quarter"  in df.columns else df
if f_market   != "All": df = df[df["Market"]   == f_market]        if "Market"   in df.columns else df
if f_category != "All": df = df[df["Category"] == f_category]      if "Category" in df.columns else df
if f_brand    != "All": df = df[df["Brand"]    == f_brand]         if "Brand"    in df.columns else df
if f_channel  != "All": df = df[df["Channel"]  == f_channel]       if "Channel"  in df.columns else df
if f_type     != "All": df = df[df["Type"]     == f_type]          if "Type"     in df.columns else df

if df.empty:
    st.warning("No data for selected filters."); st.stop()

# ── SAFE COLUMN SUM ───────────────────────────────────────────────────────────
def safe_sum(col):
    return df[col].sum() if col in df.columns else 0

nr        = safe_sum("Net_Revenue_AUD000")
gp        = safe_sum("Gross_Profit_AUD000")
ebitda    = safe_sum("EBITDA_AUD000")
cogs      = safe_sum("COGS_AUD000")
opex      = safe_sum("OPEX_AUD000")
volume    = safe_sum("Volume_Units")
base_nr   = safe_sum("Base_NR_AUD000")
trade_pr  = safe_sum("Trade_Promo_AUD000")
budget_nr = safe_sum("Budget_NR_AUD000")
var_nr    = safe_sum("Variance_NR_AUD000")
py_nr     = safe_sum("PY_NR_AUD000")

gp_margin     = gp / nr * 100        if nr       else 0
ebitda_margin = ebitda / nr * 100    if nr       else 0
cogs_pct      = cogs / nr * 100      if nr       else 0
opex_pct      = opex / nr * 100      if nr       else 0
trade_pct     = trade_pr / base_nr * 100 if base_nr else 0
yoy_growth    = (nr - py_nr) / py_nr * 100 if py_nr  else 0
budget_ach    = nr / budget_nr * 100 if budget_nr else 0
var_pct       = var_nr / budget_nr * 100 if budget_nr else 0

def dc(v): return "pos" if v > 0 else ("neg" if v < 0 else "neu")
def fmt_m(v): return f"AUD {v/1000:,.1f}M" if abs(v) >= 1000 else f"AUD {v:,.0f}K"

top_market = df.groupby("Market")["Net_Revenue_AUD000"].sum().idxmax() if "Market" in df.columns else "N/A"
top_brand  = df.groupby("Brand")["Net_Revenue_AUD000"].sum().idxmax()  if "Brand"  in df.columns else "N/A"
risk_mkt   = df.groupby("Market")["Variance_NR_AUD000"].sum().idxmin() if "Market" in df.columns and "Variance_NR_AUD000" in df.columns else "N/A"

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center; margin-top:10px; margin-bottom:20px;">
  <div style="font-size:1.8rem; font-weight:700; color:#38bdf8; letter-spacing:1px;">
    {company_name} · Data & Intelligence Insights
  </div>
  <div style="font-size:0.8rem; color:#94a3b8; margin-top:4px;">
    Real-time FP&A performance powered by AI
  </div>
</div>
""", unsafe_allow_html=True)

# ── KPI ROW 1 ─────────────────────────────────────────────────────────────────
arrow = "▲" if yoy_growth > 0 else "▼"
yoy_text = f"{abs(yoy_growth):.1f}% YoY"
cogs_class = "neg" if cogs_pct > 55 else "pos"
opex_class = "neg" if opex_pct > 20 else "pos"

st.markdown('<div class="section-label">P&L Headline</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-label">Net Revenue</div>
    <div class="kpi-value">{fmt_m(nr)}</div>
    <div class="kpi-delta {dc(yoy_growth)}">{arrow} {yoy_text}</div>
  </div>
  <div class="kpi-card" style="--accent:#34d399">
    <div class="kpi-label">Gross Profit</div>
    <div class="kpi-value">{fmt_m(gp)}</div>
    <div class="kpi-delta {dc(gp_margin-50)}">GP Margin {gp_margin:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#818cf8">
    <div class="kpi-label">EBITDA</div>
    <div class="kpi-value">{fmt_m(ebitda)}</div>
    <div class="kpi-delta {dc(ebitda_margin-30)}">EBITDA Margin {ebitda_margin:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#fb923c">
    <div class="kpi-label">COGS</div>
    <div class="kpi-value">{fmt_m(cogs)}</div>
    <div class="kpi-delta {cogs_class}">COGS % NR {cogs_pct:.1f}%</div>
  </div>
  <div class="kpi-card" style="--accent:#f472b6">
    <div class="kpi-label">OPEX</div>
    <div class="kpi-value">{fmt_m(opex)}</div>
    <div class="kpi-delta {opex_class}">OPEX % NR {opex_pct:.1f}%</div>
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
    if "Market" in df.columns:
        rev_mkt = df.groupby("Market")[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index()
        fig1 = go.Figure()
        for col, color in zip(["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"],["#38bdf8","#34d399","#818cf8"]):
            fig1.add_bar(x=rev_mkt["Market"], y=rev_mkt[col], name=col.replace("_AUD000","").replace("_"," "), marker_color=color)
        fig1.update_layout(**PLOTLY_BASE, title="P&L by Market", barmode="group", height=280, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig1, use_container_width=True)

with c2:
    if "Category" in df.columns:
        rev_cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().reset_index().sort_values("Net_Revenue_AUD000", ascending=True)
        fig2 = go.Figure(go.Bar(
            x=rev_cat["Net_Revenue_AUD000"], y=rev_cat["Category"], orientation="h",
            marker_color=PALETTE[:len(rev_cat)],
            text=rev_cat["Net_Revenue_AUD000"].apply(fmt_m),
            textposition="auto", textfont=dict(size=10, color="#fff")
        ))
        fig2.update_layout(**PLOTLY_BASE, title="Net Revenue by Category", height=280, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig2, use_container_width=True)

with c3:
    wfall = {"Base NR": base_nr, "Trade Promo": -trade_pr, "Net Revenue": nr, "COGS": -cogs, "Gross Profit": gp, "OPEX": -opex, "EBITDA": ebitda}
    labels = list(wfall.keys())
    values = list(wfall.values())
    fig3 = go.Figure(go.Bar(x=labels, y=values, marker_color=["#38bdf8" if v > 0 else "#f87171" for v in values]))
    fig3.update_layout(**PLOTLY_BASE, title="P&L Bridge", height=280, xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
    st.plotly_chart(fig3, use_container_width=True)

# ── CHARTS ROW 2 ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Trend & Mix Analysis</div>', unsafe_allow_html=True)
c4, c5 = st.columns([3, 2])

with c4:
    if "Month_Num" in df.columns and "Month" in df.columns:
        trend = df.groupby(["Year","Month_Num","Month"])[["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"]].sum().reset_index().sort_values(["Year","Month_Num"])
        trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"].astype(str)
        fig4 = go.Figure()
        for col, color, name in zip(["Net_Revenue_AUD000","Gross_Profit_AUD000","EBITDA_AUD000"],["#38bdf8","#34d399","#818cf8"],["Net Revenue","Gross Profit","EBITDA"]):
            fig4.add_scatter(x=trend["Period"], y=trend[col], mode="lines", name=name, line=dict(color=color, width=2))
        fig4.update_layout(**PLOTLY_BASE, title="Monthly Trend: Revenue → EBITDA", height=280, xaxis=dict(tickangle=-45, nticks=12, **AXIS), yaxis=AXIS)
        st.plotly_chart(fig4, use_container_width=True)

with c5:
    if "Channel" in df.columns:
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
    if "Brand" in df.columns:
        brand_kpi = df.groupby("Brand").agg(
            NR=("Net_Revenue_AUD000","sum"), GP=("Gross_Profit_AUD000","sum"),
            Budget=("Budget_NR_AUD000","sum"), Variance=("Variance_NR_AUD000","sum")
        ).reset_index()
        brand_kpi["GP_Margin"] = (brand_kpi["GP"] / brand_kpi["NR"] * 100).round(1)
        brand_kpi["Bdgt_Ach"]  = (brand_kpi["NR"] / brand_kpi["Budget"] * 100).round(1)
        brand_kpi = brand_kpi.sort_values("NR", ascending=False)

        fig6 = make_subplots(specs=[[{"secondary_y": True}]])
        fig6.add_bar(x=brand_kpi["Brand"], y=brand_kpi["NR"], name="Net Revenue", marker_color="#38bdf8", secondary_y=False)
        fig6.add_scatter(x=brand_kpi["Brand"], y=brand_kpi["GP_Margin"], mode="lines+markers", name="GP Margin %",
                         line=dict(color="#34d399", width=2), marker=dict(size=8), secondary_y=True)
        fig6.update_layout(**PLOTLY_BASE, title="Brand: Revenue vs GP Margin", height=300, xaxis=AXIS, yaxis=AXIS)
        fig6.update_yaxes(title_text="GP Margin %", secondary_y=True, gridcolor="#1e2a3a")
        st.plotly_chart(fig6, use_container_width=True)

with c7:
    if "Market" in df.columns and "Variance_NR_AUD000" in df.columns:
        var_mkt = df.groupby("Market")["Variance_NR_AUD000"].sum().reset_index().sort_values("Variance_NR_AUD000")
        fig7 = go.Figure(go.Bar(
            x=var_mkt["Variance_NR_AUD000"], y=var_mkt["Market"], orientation="h",
            marker_color=["#f87171" if v < 0 else "#34d399" for v in var_mkt["Variance_NR_AUD000"]],
            text=var_mkt["Variance_NR_AUD000"].apply(lambda x: f"{x:+,.0f}"),
            textposition="auto", textfont=dict(size=10, color="#fff")
        ))
        fig7.update_layout(**PLOTLY_BASE, title="NR Variance vs Budget by Market", height=300, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig7, use_container_width=True)

# ── BRAND SCORECARD ───────────────────────────────────────────────────────────
if "Brand" in df.columns:
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
  EBITDA Margin at <strong>{ebitda_margin:.1f}%</strong>. COGS at {cogs_pct:.1f}% of NR; OPEX at {opex_pct:.1f}% of NR.
  Trade Promo intensity at {trade_pct:.1f}% of Base NR.<br><br>
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
    if "top market"  in q: return "Top market by revenue: " + str(top_market)
    if "top brand"   in q: return "Top brand by revenue: " + str(top_brand)
    if "risk"        in q: return "Highest budget risk market: " + str(risk_mkt)
    if "revenue"     in q: return "Total Net Revenue: " + fmt_m(nr)
    if "profit"      in q: return "Gross Profit: " + fmt_m(gp) + " | GP Margin: " + f"{gp_margin:.1f}%"
    if "ebitda"      in q: return "EBITDA: " + fmt_m(ebitda) + " | EBITDA Margin: " + f"{ebitda_margin:.1f}%"
    if "margin"      in q: return "GP Margin: " + f"{gp_margin:.1f}%" + " | EBITDA Margin: " + f"{ebitda_margin:.1f}%"
    if "variance"    in q: return "NR Variance vs Budget: " + fmt_m(var_nr) + f" ({var_pct:+.1f}%)"
    if "budget"      in q: return "Budget Achievement: " + f"{budget_ach:.1f}%" + " | Variance: " + fmt_m(var_nr)
    if "cogs"        in q: return "COGS: " + fmt_m(cogs) + f" ({cogs_pct:.1f}% of NR)"
    if "opex"        in q: return "OPEX: " + fmt_m(opex) + f" ({opex_pct:.1f}% of NR)"
    if "trade"       in q: return "Trade Promo: " + fmt_m(trade_pr) + f" ({trade_pct:.1f}% of Base NR)"
    if "volume"      in q: return "Total Volume: " + f"{volume/1000:,.0f}K units"
    if "growth"      in q: return "YoY Revenue Growth: " + f"{yoy_growth:+.1f}%"
    if "channel"     in q:
        top_ch = df.groupby("Channel")["Net_Revenue_AUD000"].sum().idxmax() if "Channel" in df.columns else "N/A"
        return "Top channel by revenue: " + str(top_ch)
    if "category"    in q:
        top_cat = df.groupby("Category")["Net_Revenue_AUD000"].sum().idxmax() if "Category" in df.columns else "N/A"
        return "Top category: " + str(top_cat)
    return "Try: revenue, profit, ebitda, margin, variance, budget, cogs, opex, trade, volume, growth, channel, brand, category, top market, risk"

# ── GROQ AI CFO ───────────────────────────────────────────────────────────────
def ai_cfo(question):
    from groq import Groq
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "⚠️ No GROQ_API_KEY found in environment."
    try:
        client = Groq(api_key=api_key)
        prompt = f"""
You are the CFO of {company_name}. Provide concise, incisive financial insights.

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

Give 2-3 CFO-level insights with specific actions and projected financial impact.
"""
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return chat.choices[0].message.content
    except Exception as e:
        return "Groq error: " + str(e)

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
    st.markdown('<div class="commentary-box">' + rule_cfo(question) + '</div>', unsafe_allow_html=True)
    st.markdown("🧠 AI CFO")
    with st.spinner("AI CFO is thinking..."):
        ai_ans = ai_cfo(question)
    st.markdown('<div class="ai-answer">' + ai_ans + '</div>', unsafe_allow_html=True)
    st.session_state.chat_history.append({"question": question, "answer": ai_ans})
    if ai_ans:
        pdf = generate_pdf(ai_ans)
        st.download_button(label="📄 Download CFO Report", data=pdf, file_name="CFO_Report.pdf", mime="application/pdf")
else:
    st.markdown("""
    <div class="commentary-box" style="opacity:0.5;font-size:0.75rem">
    ← Type a question in the sidebar and click <strong>Ask CFO</strong>.<br>
    Try: revenue, profit, ebitda, margin, variance, budget, growth, top market, risk…
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align:center;font-size:0.6rem;color:#1e2a3a;letter-spacing:2px">
  {company_name.upper()} · CFO COMMAND CENTRE · CONFIDENTIAL · FINCY INTELLIGENCE PLATFORM
</div>""", unsafe_allow_html=True)
