import os
import io
import urllib.request
import json as _json
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
    initial_sidebar_state="collapsed",   # collapsed on mobile
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=IBM+Plex+Mono:wght@300;400;500&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

/* ── Reset & base ── */
html,body,[class*="css"]{
  font-family:'IBM Plex Sans',sans-serif;
  background:#0a0a08 !important;
  color:#e8e2d4 !important;
  -webkit-font-smoothing:antialiased;
}
.stApp{background:#0a0a08 !important;}
.stApp>div{background:#0a0a08 !important;}

/* ── Hide ALL Streamlit chrome ── */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden !important; height:0 !important; min-height:0 !important;}
[data-testid="stHeader"]{display:none !important;}
[data-testid="stToolbar"]{display:none !important;}
.stDeployButton{display:none !important;}
div[data-testid="stDecoration"]{display:none !important;}

/* ── Main content — generous top padding so nothing clips ── */
.main .block-container{
  padding-top:2.5rem !important;
  padding-bottom:2rem;
  padding-left:2rem;
  padding-right:2rem;
  max-width:100%;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"]{background:#101010;border-right:1px solid #242420;}
section[data-testid="stSidebar"] *{color:#a09880 !important;}
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{color:#c9a84c !important;}
section[data-testid="stSidebar"] .stMarkdown p{color:#a09880 !important;}
section[data-testid="stSidebar"] caption{color:#5a5648 !important;}

/* ── Buttons ── */
.stButton>button{
  background:#c9a84c;color:#0a0a08;border:none;
  font-family:'IBM Plex Mono',monospace;font-size:0.72rem;
  letter-spacing:0.08em;font-weight:500;padding:10px 24px;
  transition:background 0.2s;border-radius:0;
}
.stButton>button:hover{background:#e8c96a;color:#0a0a08;}
.stButton>button:focus{box-shadow:none;outline:1px solid #c9a84c;}

/* ── Sidebar buttons different style ── */
section[data-testid="stSidebar"] .stButton>button{
  background:#1a1a14 !important;color:#a09880 !important;
  border:1px solid #2a2a24 !important;font-size:0.68rem !important;
}
section[data-testid="stSidebar"] .stButton>button:hover{
  border-color:#c9a84c !important;color:#c9a84c !important;
  background:#1a1a14 !important;
}

/* ── Form inputs ── */
.stTextInput input, .stTextInput textarea{
  background:#101010 !important;border:1px solid #2a2a24 !important;
  color:#e8e2d4 !important;font-family:'IBM Plex Mono',monospace !important;
  border-radius:0 !important;padding:10px 12px !important;
}
.stTextInput input:focus{border-color:#c9a84c !important;box-shadow:none !important;}
.stSelectbox>div>div{
  background:#101010 !important;border:1px solid #2a2a24 !important;
  color:#e8e2d4 !important;border-radius:0 !important;
}
.stFileUploader{background:#101010;border:1px solid #2a2a24;}
.stFileUploader label{color:#a09880 !important;}

/* ── Alert / info ── */
.stAlert{border-radius:0;border-left:2px solid #c9a84c;}

/* ── Hide native metric ── */
div[data-testid="metric-container"]{display:none;}

/* ── Typography classes ── */
.fin-title{
  font-family:'Playfair Display',serif !important;
  font-weight:900 !important;color:#fafaf8 !important;line-height:1.05 !important;
  display:block !important;opacity:1 !important;visibility:visible !important;
}
.fin-sub{
  font-family:'IBM Plex Mono',monospace;
  font-size:0.62rem;letter-spacing:0.18em;
  text-transform:uppercase;color:#5a5648;
}
.sec-label{
  font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
  letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c;
  margin:1.4rem 0 0.7rem;border-left:2px solid #c9a84c;padding-left:10px;
}

/* ── KPI cards ── */
.kpi-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:1.4rem;}
.kpi-grid-2{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:1.6rem;}
.kpi-card{
  background:#101010;border:1px solid #242420;padding:16px;
  position:relative;overflow:hidden;
}
.kpi-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1.5px;background:var(--ac,#c9a84c);
}
.kpi-label{font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-bottom:6px;}
.kpi-value{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:#fafaf8;}
.kpi-delta{font-family:'IBM Plex Mono',monospace;font-size:0.62rem;margin-top:4px;}
.pos{color:#4ade80;}.neg{color:#f87171;}.neu{color:#5a5648;}

/* ── Commentary boxes ── */
.box{
  background:#101010;border:1px solid #242420;border-left:2px solid #c9a84c;
  padding:16px 18px;font-size:0.8rem;line-height:1.85;color:#a09880;
}
.box strong{color:#c9a84c;}
.ai-box{
  background:#0d0d0a;border:1px solid #2a2a20;border-left:2px solid #4ade80;
  padding:15px 18px;font-size:0.8rem;line-height:1.85;color:#c8e6c9;
}
.mapper-box{
  background:#101010;border:1px solid #242420;border-left:2px solid #818cf8;
  padding:18px;margin-bottom:18px;
}

/* ── RAG summary row ── */
.rag-row{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:1.4rem;}
.rag-g{background:#051a0a;border:1px solid #4ade80;padding:14px;text-align:center;}
.rag-a{background:#1a1200;border:1px solid #fbbf24;padding:14px;text-align:center;}
.rag-r{background:#1a0505;border:1px solid #f87171;padding:14px;text-align:center;}
.rag-b{background:#060e1a;border:1px solid #60a5fa;padding:14px;text-align:center;}
.rag-lbl{font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-bottom:5px;}
.rag-val{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;}

/* ── Module home cards ── */
.mod-grid{
  display:grid;grid-template-columns:repeat(2,1fr);gap:1px;
  background:#242420;border:1px solid #242420;
  max-width:900px;margin:0 auto;
}
.mod-card{
  background:#101010;padding:32px 28px;
  position:relative;overflow:hidden;transition:background 0.2s;
}
.mod-card:hover{background:#141410;}
.mod-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--mc,#c9a84c);}
.mod-icon{font-size:1.8rem;margin-bottom:12px;display:block;}
.mod-title{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;color:#fafaf8;margin-bottom:8px;}
.mod-desc{font-size:0.76rem;color:#5a5648;line-height:1.75;margin-bottom:16px;}
.mod-badge{
  font-family:'IBM Plex Mono',monospace;display:inline-block;
  font-size:0.52rem;letter-spacing:0.16em;text-transform:uppercase;
  color:var(--mc,#c9a84c);border:1px solid var(--mc,#c9a84c);padding:2px 8px;
  margin-bottom:16px;
}
.mod-btn{
  display:inline-block;
  font-family:'IBM Plex Mono',monospace;font-size:0.62rem;letter-spacing:0.1em;
  text-transform:uppercase;background:var(--mc,#c9a84c);color:#0a0a08;
  padding:8px 18px;text-decoration:none;font-weight:500;
  border:none;cursor:pointer;transition:opacity 0.2s;
}
.mod-btn:hover{opacity:0.85;}

/* ── Signup form ── */
.signup-wrap{
  max-width:480px;margin:0 auto;
  background:#101010;border:1px solid #242420;padding:40px 36px;position:relative;
}
.signup-wrap::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:#c9a84c;}
.signup-eyebrow{font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.2em;text-transform:uppercase;color:#c9a84c;margin-bottom:10px;}
.signup-title{font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:700;color:#fafaf8;margin-bottom:6px;}
.signup-sub{font-size:0.8rem;color:#a09880;margin-bottom:24px;line-height:1.65;font-weight:300;}

/* ── Mobile ── */
@media(max-width:768px){
  .main .block-container{padding-top:2rem !important;padding-left:1rem;padding-right:1rem;}
  .kpi-grid,.kpi-grid-2{grid-template-columns:repeat(2,1fr);}
  .rag-row{grid-template-columns:repeat(2,1fr);}
  .mod-grid{grid-template-columns:1fr;}
}
@media(max-width:480px){
  .kpi-grid,.kpi-grid-2{grid-template-columns:repeat(2,1fr);}
  .main .block-container{padding-left:0.8rem;padding-right:0.8rem;}
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ─────────────────────────────────────────────────────────────
_defaults = {
    "active_module": None,
    "signed_up": True,   # Signup handled on landing page only
    "pending_module": None,
    "chat_history": [],
    "col_map": {},
    "mapping_confirmed": False,
    "recon_sample_a": False,
    "recon_sample_b": False,
    "budget_use_sample": False,
    "cost_use_sample": False,
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Mono, monospace", color="#5a5648", size=10),
    margin=dict(l=10, r=10, t=28, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=9)),
)
AXIS = dict(gridcolor="#1a1a16", linecolor="#1a1a16", tickfont=dict(size=9))
PAL  = ["#c9a84c","#4ade80","#818cf8","#f472b6","#fb923c","#60a5fa","#fbbf24","#2dd4bf"]

REQUIRED_COLS = {
    "Net_Revenue":"Net Revenue","Gross_Profit":"Gross Profit","EBITDA":"EBITDA",
    "COGS":"COGS","OPEX":"OPEX","Volume_Units":"Volume / Units",
    "Base_NR":"Base Net Revenue","Trade_Promo":"Trade Promo Spend",
    "Budget_NR":"Budget Net Revenue","Variance_NR":"NR Variance vs Budget",
    "PY_NR":"Prior Year Net Revenue",
}
OPTIONAL_DIMS = {
    "Year":"Year","Quarter":"Quarter","Month":"Month",
    "Month_Num":"Month Number (sorting)","Market":"Market / Region",
    "Category":"Category","Brand":"Brand","Channel":"Channel","Type":"Type",
}

def fmt_m(v):
    if abs(v) >= 1_000_000: return f"{v/1_000_000:,.1f}M"
    if abs(v) >= 1_000:     return f"{v/1_000:,.1f}K"
    return f"{v:,.0f}"

def dc(v): return "pos" if v > 0 else ("neg" if v < 0 else "neu")

def safe_col(df, col, default=0):
    return df[col] if col in df.columns else pd.Series([default]*len(df))

def generate_pdf(text):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf)
    styles = getSampleStyleSheet()
    content = [Paragraph("<b>Fincy Intelligence — CFO Report</b>", styles["Title"]), Spacer(1,12)]
    for line in text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 8))
    doc.build(content)
    buf.seek(0)
    return buf

def send_to_formspree(name, email, company, role, linkedin):
    """Post signup data to Formspree → Jitenparida95@gmail.com"""
    try:
        payload = _json.dumps({
            "_subject": f"New Fincy Signup: {name}",
            "name": name, "email": email,
            "company": company or "N/A", "role": role or "N/A",
            "linkedin": linkedin or "N/A", "_replyto": email,
        }).encode()
        req = urllib.request.Request(
            "https://formspree.io/f/mvzvybpr",
            data=payload,
            headers={"Content-Type":"application/json","Accept":"application/json"},
            method="POST"
        )
        urllib.request.urlopen(req, timeout=6)
    except Exception:
        pass  # Never block the user


# ── QUERY PARAM ROUTING — HTML card clicks set ?m=xxx ────────────────────────
_qp = st.query_params.get("m", None)
if _qp and _qp in ("fpa","recon","budget","cost","dataanalyst","personal","cashflow"):
    if st.session_state.active_module != _qp:
        st.session_state.active_module = _qp
    st.query_params.clear()   # clean URL after routing


# ══════════════════════════════════════════════════════════════════════════════
# SAMPLE DATA
# ══════════════════════════════════════════════════════════════════════════════
SAMPLE_FMCG = """Year,Quarter,Month,Month_Num,Market,Brand,Channel,Category,Net_Revenue,Gross_Profit,EBITDA,COGS,OPEX,Volume_Units,Base_NR,Trade_Promo,Budget_NR,Variance_NR,PY_NR
2023,Q1,Jan,1,UK,Alpha,Online,Haircare,1200,660,300,540,360,12000,1350,150,1150,50,1100
2023,Q1,Jan,1,UK,Beta,Retail,Skincare,980,490,200,490,290,9800,1100,120,1000,-20,950
2023,Q1,Jan,1,DE,Alpha,Online,Haircare,870,435,180,435,255,8700,980,110,850,20,820
2023,Q1,Jan,1,DE,Gamma,B2B,Bodycare,650,325,130,325,195,6500,730,80,620,30,610
2023,Q1,Jan,1,FR,Beta,Retail,Skincare,780,390,155,390,235,7800,880,100,760,20,740
2023,Q1,Feb,2,UK,Alpha,Online,Haircare,1250,687,311,563,376,12500,1400,150,1200,50,1140
2023,Q1,Feb,2,UK,Beta,Retail,Skincare,1020,510,210,510,300,10200,1150,130,1050,-30,980
2023,Q1,Feb,2,DE,Alpha,Online,Haircare,900,450,185,450,265,9000,1010,110,880,20,840
2023,Q1,Feb,2,DE,Gamma,B2B,Bodycare,680,340,136,340,204,6800,760,80,650,30,630
2023,Q1,Feb,2,FR,Beta,Retail,Skincare,810,405,162,405,243,8100,910,100,790,20,760
2023,Q1,Mar,3,UK,Alpha,Online,Haircare,1300,715,325,585,390,13000,1450,150,1250,50,1180
2023,Q1,Mar,3,UK,Beta,Retail,Skincare,1060,530,218,530,312,10600,1200,140,1100,-40,1010
2023,Q1,Mar,3,DE,Alpha,Online,Haircare,930,465,191,465,274,9300,1040,110,910,20,860
2023,Q1,Mar,3,DE,Gamma,B2B,Bodycare,700,350,140,350,210,7000,790,90,670,30,650
2023,Q1,Mar,3,FR,Beta,Retail,Skincare,840,420,168,420,252,8400,945,105,820,20,780
2024,Q1,Jan,1,UK,Alpha,Online,Haircare,1380,759,345,621,414,13800,1540,160,1350,30,1200
2024,Q1,Jan,1,UK,Beta,Retail,Skincare,1100,550,226,550,324,11000,1240,140,1120,-20,980
2024,Q1,Jan,1,DE,Alpha,Online,Haircare,1010,505,207,505,298,10100,1130,120,980,30,870
2024,Q1,Jan,1,DE,Gamma,B2B,Bodycare,760,380,152,380,228,7600,850,90,730,30,650
2024,Q1,Jan,1,FR,Beta,Retail,Skincare,920,460,184,460,276,9200,1030,110,890,30,780
2024,Q1,Feb,2,UK,Alpha,Online,Haircare,1420,781,355,639,426,14200,1580,160,1390,30,1250
2024,Q1,Feb,2,UK,Beta,Retail,Skincare,1140,570,234,570,336,11400,1280,140,1160,-20,1020
2024,Q1,Feb,2,DE,Alpha,Online,Haircare,1040,520,213,520,307,10400,1160,120,1010,30,900
2024,Q1,Feb,2,DE,Gamma,B2B,Bodycare,790,395,158,395,237,7900,885,95,760,30,680
2024,Q1,Feb,2,FR,Beta,Retail,Skincare,950,475,190,475,285,9500,1065,115,920,30,810
2024,Q1,Mar,3,UK,Alpha,Online,Haircare,1460,803,365,657,438,14600,1620,160,1430,30,1300
2024,Q1,Mar,3,UK,Beta,Retail,Skincare,1180,590,242,590,348,11800,1320,140,1200,-20,1060
2024,Q1,Mar,3,DE,Alpha,Online,Haircare,1070,535,219,535,316,10700,1190,120,1040,30,930
2024,Q1,Mar,3,DE,Gamma,B2B,Bodycare,820,410,164,410,246,8200,920,100,790,30,700
2024,Q1,Mar,3,FR,Beta,Retail,Skincare,980,490,196,490,294,9800,1100,120,950,30,840
"""

SAMPLE_BUDGET = """Period,Category,Actual,Budget,Prior_Year
Jan-2024,Revenue,4250,4100,3980
Feb-2024,Revenue,4380,4200,4050
Mar-2024,Revenue,4520,4500,4200
Apr-2024,Revenue,4600,4600,4300
May-2024,Revenue,4480,4700,4350
Jun-2024,Revenue,4350,4800,4400
Jul-2024,Revenue,4200,4600,4250
Aug-2024,Revenue,4380,4500,4300
Sep-2024,Revenue,4650,4700,4420
Oct-2024,Revenue,4800,4800,4500
Nov-2024,Revenue,4950,4900,4600
Dec-2024,Revenue,5100,5000,4750
Jan-2024,COGS,1900,1850,1790
Feb-2024,COGS,1960,1890,1820
Mar-2024,COGS,2030,2025,1890
Apr-2024,COGS,2070,2070,1940
May-2024,COGS,2016,2115,1960
Jun-2024,COGS,1958,2160,1980
Jul-2024,COGS,1890,2070,1913
Aug-2024,COGS,1971,2025,1935
Sep-2024,COGS,2093,2115,1989
Oct-2024,COGS,2160,2160,2025
Nov-2024,COGS,2228,2205,2070
Dec-2024,COGS,2295,2250,2138
Jan-2024,OPEX,850,820,800
Feb-2024,OPEX,876,840,810
Mar-2024,OPEX,904,900,840
Apr-2024,OPEX,920,920,860
May-2024,OPEX,896,940,870
Jun-2024,OPEX,870,960,880
Jul-2024,OPEX,840,920,850
Aug-2024,OPEX,862,905,860
Sep-2024,OPEX,895,940,875
Oct-2024,OPEX,920,960,890
Nov-2024,OPEX,945,980,900
Dec-2024,OPEX,975,1000,920
"""

SAMPLE_RECON_A = """Invoice_ID,Vendor,Amount_ERP,Date
INV-001,Supplier A,12500.00,2024-01-05
INV-002,Supplier B,8750.50,2024-01-08
INV-003,Supplier C,15200.00,2024-01-10
INV-004,Supplier A,9800.00,2024-01-12
INV-005,Supplier D,6300.75,2024-01-15
INV-006,Supplier B,11400.00,2024-01-18
INV-007,Supplier C,7650.00,2024-01-20
INV-008,Supplier A,13900.50,2024-01-22
INV-009,Supplier E,5200.00,2024-01-25
INV-010,Supplier B,9100.00,2024-01-28
INV-011,Supplier D,4800.25,2024-02-01
INV-012,Supplier A,16500.00,2024-02-03
INV-013,Supplier C,8200.00,2024-02-05
"""

SAMPLE_RECON_B = """Invoice_ID,Vendor,Amount_Bank,Date
INV-001,Supplier A,12500.00,2024-01-07
INV-002,Supplier B,8900.50,2024-01-09
INV-003,Supplier C,15200.00,2024-01-11
INV-004,Supplier A,9800.00,2024-01-13
INV-006,Supplier B,11400.00,2024-01-19
INV-007,Supplier C,7650.00,2024-01-21
INV-008,Supplier A,14200.50,2024-01-23
INV-009,Supplier E,5200.00,2024-01-26
INV-010,Supplier B,9100.00,2024-01-29
INV-011,Supplier D,4800.25,2024-02-02
INV-012,Supplier A,16500.00,2024-02-04
INV-013,Supplier C,8200.00,2024-02-06
INV-016,Supplier F,3900.00,2024-02-14
"""

SAMPLE_COST = """Period,SKU,Market,Revenue,COGS,OPEX
Jan-2024,SKU-A,UK,4200,1890,756
Jan-2024,SKU-B,UK,3100,1550,698
Jan-2024,SKU-C,DE,2800,1540,644
Jan-2024,SKU-D,FR,1900,1140,494
Feb-2024,SKU-A,UK,4350,1958,762
Feb-2024,SKU-B,UK,3200,1760,720
Feb-2024,SKU-C,DE,2900,1595,667
Feb-2024,SKU-D,FR,1950,1170,507
Mar-2024,SKU-A,UK,4500,2025,765
Mar-2024,SKU-B,UK,3300,1815,726
Mar-2024,SKU-C,DE,3000,1650,690
Mar-2024,SKU-D,FR,2000,1200,520
Apr-2024,SKU-A,UK,4600,2070,782
Apr-2024,SKU-B,UK,3350,1843,738
Apr-2024,SKU-C,DE,3050,1678,702
Apr-2024,SKU-D,FR,2050,1230,534
May-2024,SKU-A,UK,4480,2016,762
May-2024,SKU-B,UK,3280,1804,754
May-2024,SKU-C,DE,2980,1639,716
May-2024,SKU-D,FR,2020,1212,525
Jun-2024,SKU-A,UK,4350,1958,739
Jun-2024,SKU-B,UK,3180,1749,762
Jun-2024,SKU-C,DE,2900,1595,696
Jun-2024,SKU-D,FR,1980,1188,515
"""


# ══════════════════════════════════════════════════════════════════════════════
# SHARED: page header (shown on every page)
# ══════════════════════════════════════════════════════════════════════════════
def page_header(subtitle="AI-POWERED CFO DECISION PLATFORM", module=""):
    """Renders sticky nav bar + forced-visible page title on every screen."""
    # Back button — visible at top of every module page
    if st.session_state.get("active_module"):
        if st.button("⬅ All Modules", key=f"back_btn_{subtitle[:6].replace(' ','_')}",
                     help="Return to module selection"):
            st.session_state.active_module = None
            st.rerun()
    mod_tag = f'<span style="color:#3a3a34;font-weight:400;"> · {module}</span>' if module else ""
    st.markdown(f"""
<div style="background:#0f0f0c;border-bottom:1px solid #1e1e18;padding:0 28px;
height:52px;display:flex;align-items:center;justify-content:space-between;
margin:-2.5rem -2rem 2rem -2rem;position:sticky;top:0;z-index:100;">
  <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;
  color:#c9a84c;display:flex;align-items:center;gap:8px;">
    <span style="font-size:0.8rem;opacity:0.6;">◆</span>
    Fincy Intelligence{mod_tag}
  </div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.54rem;
  letter-spacing:0.14em;text-transform:uppercase;color:#3a3a34;">AI CFO Platform</div>
</div>
<div style="border-bottom:1px solid #1e1e18;padding-bottom:20px;margin-bottom:28px;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.2em;
  text-transform:uppercase;color:#c9a84c;margin-bottom:10px;">{subtitle}</div>
  <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;
  color:#fafaf8 !important;line-height:1.05;letter-spacing:-0.01em;">
    Fincy <em style="color:#c9a84c;font-style:italic;">Intelligence</em>
  </div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;color:#3a3a34;
  margin-top:6px;letter-spacing:0.1em;">
    By Jitendra Parida · Senior FP&amp;A Analyst · IBM / Reckitt &nbsp;·&nbsp;
    <a href="https://www.linkedin.com/in/jitendraparida95/" target="_blank"
    style="color:#c9a84c;text-decoration:none;">LinkedIn ↗</a>
  </div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIGNUP GATE  (shown on first module entry)
# ══════════════════════════════════════════════════════════════════════════════
def show_signup():
    page_header("GET FREE ACCESS — 7-DAY TRIAL · ALL 4 MODULES")

    _, col, _ = st.columns([1, 1.6, 1])
    with col:
        st.markdown("""
<div class="signup-wrap">
  <div class="signup-eyebrow">Free Access · No Credit Card</div>
  <div class="signup-title">Get Instant Access</div>
  <div class="signup-sub">
    Enter your details to unlock all 4 modules free for 7 days.<br>
    No spam. Unsubscribe anytime. Your data never leaves your session.
  </div>
</div>""", unsafe_allow_html=True)

        with st.form("signup_form", clear_on_submit=False):
            name     = st.text_input("Full Name *",    placeholder="Your Name")
            email    = st.text_input("Work Email *",   placeholder="you@company.com")
            company  = st.text_input("Company",        placeholder="IBM, Reckitt, Unilever…")
            role     = st.text_input("Role",           placeholder="FP&A Manager, CFO, Finance Analyst…")
            linkedin = st.text_input("LinkedIn URL",   placeholder="linkedin.com/in/yourprofile")

            go = st.form_submit_button("→  Get Free Access", use_container_width=True)

            if go:
                name  = name.strip()
                email = email.strip()
                if not name:
                    st.error("Please enter your full name.")
                elif not email or "@" not in email:
                    st.error("Please enter a valid work email.")
                else:
                    send_to_formspree(name, email, company.strip(), role.strip(), linkedin.strip())
                    st.session_state.signed_up     = True
                    st.session_state.active_module = st.session_state.pending_module
                    st.session_state.pending_module = None
                    st.success(f"Welcome, {name}! Taking you in…")
                    st.rerun()

        st.markdown("""
<div style="text-align:center;font-family:'IBM Plex Mono',monospace;font-size:0.54rem;
color:#3a3a34;margin-top:12px;letter-spacing:0.08em;">
🔒 Safe &amp; private · Data stays in your session · No server storage
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, bc, _ = st.columns([1, 1.6, 1])
    with bc:
        if st.button("← Back to Module Selection", use_container_width=True, key="signup_back"):
            st.session_state.pending_module = None
            st.session_state.active_module  = None
            st.rerun()


def goto_module(mod_key):
    """Route through signup if not signed up yet."""
    if st.session_state.signed_up:
        st.session_state.active_module = mod_key
    else:
        st.session_state.pending_module = mod_key
        st.session_state.active_module  = "__signup__"
    st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# HOME — MODULE SELECTOR
# ══════════════════════════════════════════════════════════════════════════════
def show_global_chat():
    """Floating 'Chat with Fincy' available on every screen (req §7)."""
    api_key = _get_groq_key()

    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '''<div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;
letter-spacing:0.12em;text-transform:uppercase;color:#c9a84c;margin-bottom:8px;">
💬 Chat with Fincy</div>''', unsafe_allow_html=True)

        chat_q = st.text_input("Ask Fincy anything…", key="global_chat_input",
                               placeholder="e.g. How does reconciliation work?",
                               label_visibility="collapsed")
        send = st.button("Send →", use_container_width=True, key="global_chat_send")

        if send and chat_q.strip():
            if not api_key:
                reply = ("AI CFO offline — add GROQ_API_KEY to Streamlit Secrets. "
                         "Get a free key at console.groq.com")
            else:
                try:
                    from groq import Groq
                    sys_prompt = (
                        "You are Fincy, an AI CFO assistant built on Groq Llama 3.1. "
                        "Answer questions about: platform features, finance basics, "
                        "tax logic (India FY 2024-25), how to use modules, and general FP&A. "
                        "Be concise (max 3 sentences), helpful, and professional."
                    )
                    history_msgs = [{"role":"system","content":sys_prompt}]
                    for (q, a) in st.session_state.chat_history[-4:]:
                        history_msgs.append({"role":"user",      "content": q})
                        history_msgs.append({"role":"assistant", "content": a})
                    history_msgs.append({"role":"user","content":chat_q.strip()})
                    resp = Groq(api_key=api_key).chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=history_msgs,
                        max_tokens=300,
                        temperature=0.3
                    )
                    reply = resp.choices[0].message.content
                except Exception as e:
                    reply = f"Error: {e}"
            st.session_state.chat_history.append((chat_q.strip(), reply))
            st.rerun()

        if st.session_state.chat_history:
            st.markdown("---")
            for (q, a) in reversed(st.session_state.chat_history[-3:]):
                st.markdown(f'''<div style="font-size:0.72rem;color:#5a5648;
margin-bottom:2px;">You: {q}</div>
<div style="font-size:0.72rem;color:#a09880;background:#101010;
padding:6px 10px;margin-bottom:8px;border-left:2px solid #c9a84c;">
Fincy: {a}</div>''', unsafe_allow_html=True)
            if st.button("🗑️ Clear chat", key="clear_global_chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()


def show_home():
    page_header("AI-POWERED CFO DECISION PLATFORM")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #c9a84c;
padding:14px 20px;margin-bottom:28px;display:flex;align-items:center;gap:20px;flex-wrap:wrap;">
  <span style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#c9a84c;">Free 7-Day Trial</span>
  <span style="width:1px;height:14px;background:#2a2a20;"></span>
  <span style="font-size:0.8rem;color:#a09880;font-weight:300;">
    6 AI modules · FP&amp;A Decision Intelligence · Reconciliation · Cost Intelligence
    · Data Analysis Agent · Personal Finance · Cash Flow Intelligence
  </span>
  <span style="margin-left:auto;font-family:'IBM Plex Mono',monospace;font-size:0.52rem;
  color:#3a3a34;">Session isolated · No code · No credit card</span>
</div>""", unsafe_allow_html=True)

    # ── 6-card grid (plain st.markdown, no f-string — CSS braces safe) ──────
    app_url = "https://fincy-intelligence.streamlit.app"
    cards_html = """
<style>
.mhg{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#1e1e18;}
.mhc{display:block;background:#101010;padding:0;text-decoration:none;
  position:relative;overflow:hidden;transition:background .18s,transform .18s;}
.mhc:hover{background:#141410;transform:translateY(-2px);}
.mhc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--mc);}
.mhb{padding:22px 20px 0;}
.mhi{font-size:1.5rem;margin-bottom:9px;display:block;}
.mhbdg{font-family:'IBM Plex Mono',monospace;font-size:0.48rem;letter-spacing:0.15em;
  text-transform:uppercase;color:var(--mc);border:1px solid var(--mc);
  padding:2px 8px;display:inline-block;margin-bottom:10px;}
.mht{font-family:'Playfair Display',serif;font-size:0.94rem;font-weight:700;
  color:#fafaf8;margin-bottom:6px;line-height:1.2;}
.mhd{font-size:0.74rem;color:#a09880;line-height:1.68;margin-bottom:8px;font-weight:300;}
.mhk{font-family:'IBM Plex Mono',monospace;font-size:0.47rem;color:#5a5648;
  letter-spacing:0.07em;margin-bottom:14px;}
.mhbtn{display:block;background:var(--mc);color:#0a0a08;
  font-family:'IBM Plex Mono',monospace;font-size:0.62rem;font-weight:700;
  letter-spacing:0.06em;text-transform:uppercase;padding:11px 18px;
  border-top:1px solid rgba(0,0,0,0.18);transition:opacity .15s;}
.mhc:hover .mhbtn{opacity:0.85;}
@media(max-width:900px){.mhg{grid-template-columns:repeat(2,1fr);}}
@media(max-width:540px){.mhg{grid-template-columns:1fr;}}
</style>
""" + f"""
<div class="mhg">
  <a class="mhc" href="{app_url}/?m=fpa" target="_self" style="--mc:#c9a84c;">
    <div class="mhb"><span class="mhi">📊</span>
      <div class="mhbdg">Core · Decision Suite</div>
      <div class="mht">FP&amp;A Decision Intelligence</div>
      <div class="mhd">Complete P&amp;L suite — dashboards, variance analysis, budget vs actuals, and AI CFO. From any CSV in 60 seconds.</div>
      <div class="mhk">P&amp;L · Variance · Budget Snapshot · AI CFO</div>
    </div>
    <div class="mhbtn">→ Launch FP&amp;A Decision Intelligence</div>
  </a>
  <a class="mhc" href="{app_url}/?m=recon" target="_self" style="--mc:#4ade80;">
    <div class="mhb"><span class="mhi">🔁</span>
      <div class="mhbdg">Reconciliation</div>
      <div class="mht">Reconciliation Engine</div>
      <div class="mhd">ERP vs Bank, GL vs Sub-ledger, PO vs Invoice. 3-part composite key — zero false breaks. Exceptions CSV.</div>
      <div class="mhk">Composite Key · Auto-Match · Exceptions · AI CFO</div>
    </div>
    <div class="mhbtn">→ Launch Reconciliation Engine</div>
  </a>

  <a class="mhc" href="{app_url}/?m=cost" target="_self" style="--mc:#f472b6;">
    <div class="mhb"><span class="mhi">💡</span>
      <div class="mhbdg">Cost Analysis</div>
      <div class="mht">Cost Intelligence</div>
      <div class="mhd">COGS and OPEX benchmarking with segment efficiency scores, waterfall charts, and AI cost reduction recommendations.</div>
      <div class="mhk">Benchmarks · Flagged Lines · Waterfall · AI CFO</div>
    </div>
    <div class="mhbtn">→ Launch Cost Intelligence</div>
  </a>

  <a class="mhc" href="{app_url}/?m=dataanalyst" target="_self" style="--mc:#2dd4bf;">
    <div class="mhb"><span class="mhi">🤖</span>
      <div class="mhbdg">AI Agent · New</div>
      <div class="mht">Data Analysis Agent</div>
      <div class="mhd">Upload any financial dataset. Auto-profiles data, runs statistics, builds correlation heatmaps, answers anything in plain English.</div>
      <div class="mhk">Auto Profiling · Correlation · Charts · AI CFO</div>
    </div>
    <div class="mhbtn">→ Launch Data Agent</div>
  </a>
  <a class="mhc" href="{app_url}/?m=personal" target="_self" style="--mc:#a78bfa;">
    <div class="mhb"><span class="mhi">💰</span>
      <div class="mhbdg">Personal · New</div>
      <div class="mht">Personal Finance Engine</div>
      <div class="mhd">Ask "Can I afford a ₹20,000 phone?" Enter your income and savings profile. Get Safe / Moderate / Risky decision with exact savings impact and AI recommendation.</div>
      <div class="mhk">Safe/Moderate/Risky · Savings Impact · AI Advisor</div>
    </div>
    <div class="mhbtn">→ Launch Personal Finance</div>
  </a>
  <a class="mhc" href="{app_url}/?m=cashflow" target="_self" style="--mc:#06b6d4;">
    <div class="mhb"><span class="mhi">💧</span>
      <div class="mhbdg">New</div>
      <div class="mht">Cash Flow Intelligence</div>
      <div class="mhd">Upload your monthly cash flow statement. Get instant liquidity health, burn rate, runway analysis, and AI CFO insights on where your cash is going.</div>
      <div class="mhk">Liquidity · Burn Rate · Runway · AI CFO</div>
    </div>
    <div class="mhbtn">→ Launch Cash Flow Intelligence</div>
  </a>
</div>"""
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown("""
<div style="margin-top:2px;display:grid;grid-template-columns:1fr 1fr;gap:1px;
background:#1e1e18;border:1px solid #1e1e18;margin-bottom:2px;">
  <div style="background:#101010;padding:15px 18px;display:flex;align-items:center;gap:12px;">
    <div style="width:34px;height:34px;background:#1a1a12;border:1px solid #c9a84c;
    border-radius:50%;display:flex;align-items:center;justify-content:center;
    font-family:'Playfair Display',serif;font-size:0.85rem;color:#c9a84c;flex-shrink:0;">JP</div>
    <div>
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.12em;
      text-transform:uppercase;color:#c9a84c;margin-bottom:3px;">Founder · Jitendra Parida</div>
      <div style="font-size:0.74rem;color:#a09880;font-weight:300;">
        Jitendra Parida · Senior FP&amp;A Analyst · IBM / Reckitt &nbsp;·&nbsp;
        <a href="https://www.linkedin.com/in/jitendraparida95/" target="_blank"
        style="color:#c9a84c;text-decoration:none;">LinkedIn ↗</a>
      </div>
    </div>
  </div>
  <div style="background:#101010;padding:15px 18px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#4ade80;margin-bottom:5px;">🔒 Data Privacy</div>
    <div style="font-size:0.73rem;color:#a09880;font-weight:300;line-height:1.6;">
      Data <strong style="color:#e8e2d4;">never leaves your session.</strong>
      No server storage. Session-isolated. No logging.
    </div>
  </div>
</div>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:1px;background:#1e1e18;
border:1px solid #1e1e18;margin-bottom:2px;">
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">6</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">AI Modules</div>
  </div>
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">20+</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">KPI Metrics</div>
  </div>
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">60s</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">To Insights</div>
  </div>
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">2</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">AI Agents</div>
  </div>
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">0</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">Code Needed</div>
  </div>
  <div style="background:#101010;padding:13px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#c9a84c;">∞</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.43rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#5a5648;margin-top:3px;">Questions</div>
  </div>
</div>
<div style="margin-top:24px;border-top:1px solid #1a1a14;padding-top:14px;
font-family:'IBM Plex Mono',monospace;font-size:0.48rem;color:#2a2a24;
letter-spacing:0.12em;text-align:center;">
FINCY INTELLIGENCE · AI CFO PLATFORM · CONFIDENTIAL · FP&amp;A DECISION ENGINE
</div>""", unsafe_allow_html=True)

def _get_groq_key():
    """st.secrets first (Streamlit Cloud), os.getenv fallback (local)."""
    try:
        k = st.secrets.get("GROQ_API_KEY", "") or ""
        if k: return k
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY", "") or ""


def ai_cfo_section(context_str, module_key, placeholder="Ask about this data…"):
    """Inline AI CFO — Problem / Insight / Action format. All modules."""
    st.markdown('''<div class="sec-label">🧠 AI CFO — Ask About This Data</div>''',
                unsafe_allow_html=True)
    api_key = _get_groq_key()
    if not api_key:
        st.markdown("""
<div style="background:#150404;border:1px solid #f87171;border-left:3px solid #f87171;
padding:11px 16px;font-size:0.76rem;color:#a09880;">
<strong style="color:#f87171;">AI CFO offline</strong> — GROQ_API_KEY not found.<br>
Go to Streamlit Dashboard → Your app → ⋮ Settings → Secrets and add:<br>
<code style="color:#c9a84c;">GROQ_API_KEY = "gsk_..."</code>
&nbsp;·&nbsp; Free key: <a href="https://console.groq.com" target="_blank"
style="color:#c9a84c;">console.groq.com ↗</a>
</div>""", unsafe_allow_html=True)
        return

    hist_key = f"chat_{module_key}"
    if hist_key not in st.session_state:
        st.session_state[hist_key] = []

    for chat in reversed(st.session_state[hist_key][-3:]):
        st.markdown(f'''
<div class="box" style="margin-bottom:10px;">
<span style="color:#5a5648;font-size:0.58rem;font-family:'IBM Plex Mono',monospace;
letter-spacing:0.12em;text-transform:uppercase;">You</span><br>
<span style="font-size:0.82rem;color:#e8e2d4;">{chat["q"]}</span><br><br>
<span style="color:#c9a84c;font-size:0.58rem;font-family:'IBM Plex Mono',monospace;
letter-spacing:0.12em;text-transform:uppercase;">AI CFO</span><br>
<span style="font-size:0.81rem;color:#a09880;line-height:1.85;">{chat["a"]}</span>
</div>''', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([5,1,1])
    with c1:
        question = st.text_input("", placeholder=placeholder,
                                 key=f"ai_q_{module_key}", label_visibility="collapsed")
    with c2:
        ask = st.button("🚀 Ask CFO", use_container_width=True, key=f"ai_ask_{module_key}")
    with c3:
        if st.button("🗑️", use_container_width=True, key=f"ai_clr_{module_key}",
                     help="Clear"):
            st.session_state[hist_key] = []
            st.rerun()

    if ask and question.strip():
        with st.spinner("AI CFO analysing…"):
            try:
                from groq import Groq
                prompt = (
                    "You are a CFO with 20+ years experience in FP&A, corporate finance, and strategic decision-making. "
                    "You are advising a CEO. Be direct, data-driven, and ruthlessly specific.\n\n"
                    f"FINANCIAL DATA CONTEXT:\n{context_str}\n\n"
                    f"QUESTION: {question.strip()}\n\n"
                    "Respond in this EXACT structured format:\n\n"
                    "**Key Insights** (max 3, numbered)\n"
                    "- Use specific numbers and % from the data above\n"
                    "- No basic concept explanations\n\n"
                    "**Risks Identified**\n"
                    "- Flag what could go wrong, with magnitude\n\n"
                    "**Opportunities**\n"
                    "- Where to improve profit/cashflow, with estimated impact\n\n"
                    "**Action Items — Next 30 Days** (specific, measurable)\n"
                    "👉 **Problem:** [exact issue with numbers]\n"
                    "👉 **Insight:** [root cause]\n"
                    "👉 **Action:** [what to do, by when, target metric]\n\n"
                    "**Strategic Recommendation**\n"
                    "- One clear sentence a CEO should act on immediately\n\n"
                    "Rules: no fluff, no basic explanations, every point must reference specific numbers."
                )
                resp = Groq(api_key=api_key).chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role":"user","content":prompt}],
                    max_tokens=800, temperature=0.25)
                ans = resp.choices[0].message.content
            except Exception as e:
                ans = f"⚠️ Groq API error: {e}"
        st.markdown(f'''<div class="ai-box" style="line-height:1.85;">{ans}</div>''',
                    unsafe_allow_html=True)
        st.session_state[hist_key].append({"q":question.strip(),"a":ans})
        # PDF download of this AI CFO response
        try:
            _pdf_content = f"FINCY INTELLIGENCE — AI CFO REPORT\n{'='*50}\n\n"
            _pdf_content += f"Module: {module_key.upper()}\n"
            _pdf_content += f"Question: {question.strip()}\n\n"
            _pdf_content += f"AI CFO Analysis:\n{ans}\n\n"
            _pdf_content += f"Data Context:\n{context_str[:500]}..."
            _pdf_bytes = generate_pdf(_pdf_content)
            st.download_button(
                "📄 Download AI CFO Report (PDF)",
                data=_pdf_bytes,
                file_name=f"Fincy_AI_CFO_{module_key}_Report.pdf",
                mime="application/pdf",
                key=f"pdf_dl_{module_key}_{len(st.session_state[hist_key])}"
            )
        except Exception:
            pass
    elif not ask:
        st.markdown('''<div class="box" style="opacity:0.45;font-size:0.74rem;">
💡 Ask anything. Each answer gives:<br>
👉 <strong>Problem</strong> — specific issue with numbers<br>
👉 <strong>Insight</strong> — root cause<br>
👉 <strong>Action</strong> — concrete next step
</div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1 — FP&A INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_fpa():
    # ── Sidebar ──────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 📊 FP&A Decision Intelligence")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="fpa_home"):
            for k in ["df_raw","col_map","mapping_confirmed","chat_history"]:
                st.session_state.pop(k, None)
            st.session_state.active_module = None
            st.rerun()
        if "df_raw" in st.session_state and st.session_state.mapping_confirmed:
            if st.button("🔄 Upload New Data", use_container_width=True, key="fpa_new"):
                for k in ["df_raw","col_map","mapping_confirmed","chat_history"]:
                    st.session_state.pop(k, None)
                st.rerun()

    # ── Step 1: Upload ────────────────────────────────────────────────────────
    if "df_raw" not in st.session_state:
        page_header("FP&A DECISION INTELLIGENCE", "Upload Data")

        st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #818cf8;
padding:12px 18px;margin-bottom:22px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#818cf8;margin-bottom:4px;">Step 1</div>
  <div style="font-size:0.75rem;color:#a09880;font-weight:300;">Upload any P&amp;L CSV or use the FMCG sample to explore instantly</div></div>
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#818cf8;margin-bottom:4px;">Step 2</div>
  <div style="font-size:0.75rem;color:#a09880;font-weight:300;">Map your CSV columns to Revenue, GP, EBITDA — auto-detected in most cases</div></div>
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#818cf8;margin-bottom:4px;">Step 3</div>
  <div style="font-size:0.75rem;color:#a09880;font-weight:300;">Dashboard is live — 10+ KPIs, 7 charts, AI CFO answering your questions</div></div>
</div>""", unsafe_allow_html=True)

        _, cc, _ = st.columns([1, 2, 1])
        with cc:
            use_sample = st.button(
                "📊 Use FMCG Sample Data  (no upload needed)",
                use_container_width=True, key="fpa_sample")

            st.markdown("""<div style="text-align:center;margin:14px 0 10px;
font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:#3a3a34;letter-spacing:0.1em;">
— or upload your own CSV —</div>""", unsafe_allow_html=True)

            uploaded = st.file_uploader(
                "Upload Financial Data (CSV)", type=["csv"], key="fpa_upload",
                help="Any P&L CSV. You'll map columns in the next step.")

            st.markdown("""<div style="margin-top:12px;background:#041508;border:1px solid rgba(74,222,128,0.15);
padding:10px 14px;font-family:'IBM Plex Mono',monospace;font-size:0.56rem;
color:#4ade80;letter-spacing:0.08em;text-align:center;">
🔒 Your data stays in your browser session only · Never stored on any server · Discarded on tab close
</div>""", unsafe_allow_html=True)

        if use_sample:
            st.session_state.df_raw = pd.read_csv(io.StringIO(SAMPLE_FMCG))
            st.session_state.mapping_confirmed = False
            st.session_state.col_map = {}
            st.rerun()
        if uploaded is not None:
            try:
                st.session_state.df_raw = pd.read_csv(uploaded)
                if st.session_state.df_raw.empty:
                    st.error("⚠️ Your file appears to be empty. Please check and re-upload.")
                    st.session_state.pop("df_raw", None)
                else:
                    st.session_state.mapping_confirmed = False
                    st.session_state.col_map = {}
                    st.rerun()
            except Exception as e:
                st.error(f"⚠️ Could not read your CSV: {e}\n\nPlease check the file is a valid CSV and try again.")
        st.stop()

    df_raw = st.session_state.df_raw

    # ── Step 2: Column Mapper ─────────────────────────────────────────────────
    if not st.session_state.mapping_confirmed:
        page_header(f"MAP COLUMNS · {len(df_raw):,} ROWS", "Column Mapper")

        st.markdown("""<div class="mapper-box">
<div style="font-size:0.78rem;color:#a09880;line-height:1.75;">
Match your CSV columns to the metrics Fincy needs.<br>
<span style="color:#f87171;">★ Required</span> — map as many as you have &nbsp;|&nbsp;
<span style="color:#5a5648;">○ Optional</span> — enables richer charts, filters and drill-downs.
</div></div>""", unsafe_allow_html=True)

        csv_cols = ["— skip —"] + list(df_raw.columns)
        col_map  = {}

        st.markdown("##### ★ Financial Metrics")
        r1, r2, r3 = st.columns(3)
        for i, (key, label) in enumerate(REQUIRED_COLS.items()):
            c = [r1, r2, r3][i % 3]
            with c:
                g  = next((x for x in df_raw.columns
                           if key.lower().replace("_","") in x.lower().replace("_","")), "— skip —")
                di = csv_cols.index(g) if g in csv_cols else 0
                col_map[key] = st.selectbox(f"★ {label}", csv_cols, index=di, key=f"map_{key}")

        st.markdown("##### ○ Dimensions (optional — enables filters & drill-downs)")
        d1, d2, d3 = st.columns(3)
        for i, (key, label) in enumerate(OPTIONAL_DIMS.items()):
            c = [d1, d2, d3][i % 3]
            with c:
                g  = next((x for x in df_raw.columns if key.lower() in x.lower()), "— skip —")
                di = csv_cols.index(g) if g in csv_cols else 0
                col_map[key] = st.selectbox(f"○ {label}", csv_cols, index=di, key=f"map_{key}")

        st.markdown("<br>", unsafe_allow_html=True)
        _, mc, _ = st.columns([1, 2, 1])
        with mc:
            if st.button("✅  Confirm Mapping & Launch Dashboard →",
                         use_container_width=True, key="confirm_map"):
                st.session_state.col_map           = col_map
                st.session_state.mapping_confirmed = True
                st.rerun()
        st.stop()

    # ── Step 3: Dashboard ─────────────────────────────────────────────────────
    col_map   = st.session_state.col_map
    rename    = {v: k for k, v in col_map.items() if v and v != "— skip —"}
    df_mapped = df_raw.rename(columns=rename)

    # Sidebar filters
    with st.sidebar:
        st.markdown("### Filters")
        def filt(label, key):
            if key in col_map and col_map[key] != "— skip —" and key in df_mapped.columns:
                opts = ["All"] + sorted(df_mapped[key].dropna().unique().tolist())
                return st.selectbox(label, opts, key=f"filt_{key}")
            return "All"
        fy  = filt("🗓️ Year",      "Year")
        fq  = filt("📊 Quarter",   "Quarter")
        fm  = filt("🌍 Market",    "Market")
        fc  = filt("🏷️ Category",  "Category")
        fb  = filt("💎 Brand",     "Brand")
        fch = filt("🛒 Channel",   "Channel")
        ft  = filt("📄 Type",      "Type")
        st.markdown("---")
        st.caption("💡 AI CFO available below the dashboard")

    # Apply filters
    df = df_mapped.copy()
    if fy  != "All" and "Year"     in df.columns: df = df[df["Year"]     == int(fy)]
    if fq  != "All" and "Quarter"  in df.columns: df = df[df["Quarter"]  == fq]
    if fm  != "All" and "Market"   in df.columns: df = df[df["Market"]   == fm]
    if fc  != "All" and "Category" in df.columns: df = df[df["Category"] == fc]
    if fb  != "All" and "Brand"    in df.columns: df = df[df["Brand"]    == fb]
    if fch != "All" and "Channel"  in df.columns: df = df[df["Channel"]  == fch]
    if ft  != "All" and "Type"     in df.columns: df = df[df["Type"]     == ft]
    if df.empty: st.warning("No data for selected filters."); st.stop()

    def s(col): return safe_col(df, col).sum()
    nr   = s("Net_Revenue"); gp   = s("Gross_Profit"); ebitda = s("EBITDA")
    cogs = s("COGS");        opex = s("OPEX");         vol    = s("Volume_Units")
    bnr  = s("Base_NR");     trd  = s("Trade_Promo");  bdgt   = s("Budget_NR")
    var  = s("Variance_NR"); py   = s("PY_NR")

    gpm    = gp/nr*100    if nr   else 0
    ebitdam= ebitda/nr*100 if nr  else 0
    cogsp  = cogs/nr*100  if nr   else 0
    opexp  = opex/nr*100  if nr   else 0
    tradep = abs(trd)/bnr*100 if bnr else 0
    yoy    = (nr-py)/py*100 if py else 0
    bach   = nr/bdgt*100  if bdgt else 0
    varp   = var/bdgt*100 if bdgt else 0

    top_mkt  = df.groupby("Market")["Net_Revenue"].sum().idxmax() \
               if "Market" in df.columns and not df.empty else "N/A"
    top_brand= df.groupby("Brand")["Net_Revenue"].sum().idxmax() \
               if "Brand"  in df.columns and not df.empty else "N/A"
    risk_mkt = df.groupby("Market")["Variance_NR"].sum().idxmin() \
               if "Market" in df.columns and "Variance_NR" in df.columns and not df.empty else "N/A"

    # Header
    page_header("FP&A DECISION INTELLIGENCE", "P&L Dashboard")

    # KPI Row 1
    arrow = "▲" if yoy > 0 else "▼"
    st.markdown('<div class="sec-label">P&L Headline</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid">
<div class="kpi-card" style="--ac:#c9a84c"><div class="kpi-label">Net Revenue</div><div class="kpi-value">{fmt_m(nr)}</div><div class="kpi-delta {dc(yoy)}">{arrow} {abs(yoy):.1f}% YoY</div></div>
<div class="kpi-card" style="--ac:#4ade80"><div class="kpi-label">Gross Profit</div><div class="kpi-value">{fmt_m(gp)}</div><div class="kpi-delta {dc(gpm-50)}">GP Margin {gpm:.1f}%</div></div>
<div class="kpi-card" style="--ac:#818cf8"><div class="kpi-label">EBITDA</div><div class="kpi-value">{fmt_m(ebitda)}</div><div class="kpi-delta {dc(ebitdam-30)}">Margin {ebitdam:.1f}%</div></div>
<div class="kpi-card" style="--ac:#fb923c"><div class="kpi-label">COGS</div><div class="kpi-value">{fmt_m(cogs)}</div><div class="kpi-delta {'neg' if cogsp>55 else 'pos'}">COGS% {cogsp:.1f}%</div></div>
<div class="kpi-card" style="--ac:#f472b6"><div class="kpi-label">OPEX</div><div class="kpi-value">{fmt_m(opex)}</div><div class="kpi-delta {'neg' if opexp>20 else 'pos'}">OPEX% {opexp:.1f}%</div></div>
</div>""", unsafe_allow_html=True)

    # KPI Row 2
    st.markdown('<div class="sec-label">Commercial Performance</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid-2">
<div class="kpi-card" style="--ac:#fbbf24"><div class="kpi-label">Volume Units</div><div class="kpi-value">{vol/1000:,.0f}K</div><div class="kpi-delta neu">Total units</div></div>
<div class="kpi-card" style="--ac:#2dd4bf"><div class="kpi-label">Budget Achiev.</div><div class="kpi-value">{bach:.1f}%</div><div class="kpi-delta {dc(bach-100)}">vs {fmt_m(bdgt)}</div></div>
<div class="kpi-card" style="--ac:#a78bfa"><div class="kpi-label">NR Variance</div><div class="kpi-value">{fmt_m(var)}</div><div class="kpi-delta {dc(var)}">{varp:+.1f}% vs budget</div></div>
<div class="kpi-card" style="--ac:#f87171"><div class="kpi-label">Trade Promo</div><div class="kpi-value">{fmt_m(trd)}</div><div class="kpi-delta {'neg' if tradep>10 else 'pos'}">TPR {tradep:.1f}%</div></div>
<div class="kpi-card" style="--ac:#c9a84c"><div class="kpi-label">YoY Growth</div><div class="kpi-value">{yoy:+.1f}%</div><div class="kpi-delta {dc(yoy)}">PY {fmt_m(py)}</div></div>
</div>""", unsafe_allow_html=True)

    # Charts Row 1
    st.markdown('<div class="sec-label">Revenue & Profit Breakdown</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 2, 1.5])
    with c1:
        if "Market" in df.columns:
            rm = df.groupby("Market")[["Net_Revenue","Gross_Profit","EBITDA"]].sum().reset_index()
            fig = go.Figure()
            for col, color, name in zip(
                    ["Net_Revenue","Gross_Profit","EBITDA"],
                    ["#c9a84c","#4ade80","#818cf8"],
                    ["Net Revenue","Gross Profit","EBITDA"]):
                if col in rm.columns:
                    fig.add_bar(x=rm["Market"], y=rm[col], name=name, marker_color=color)
            fig.update_layout(**PLOTLY_BASE, title="P&L by Market", barmode="group",
                              height=280, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)
    with c2:
        if "Category" in df.columns and "Net_Revenue" in df.columns:
            rc = df.groupby("Category")["Net_Revenue"].sum().reset_index().sort_values("Net_Revenue")
            fig = go.Figure(go.Bar(x=rc["Net_Revenue"], y=rc["Category"], orientation="h",
                marker_color=PAL[:len(rc)],
                text=rc["Net_Revenue"].apply(fmt_m), textposition="auto"))
            fig.update_layout(**PLOTLY_BASE, title="Revenue by Category",
                              height=280, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)
    with c3:
        wfall = {"Base NR": bnr, "Trade Promo": -trd, "Net Revenue": nr,
                 "COGS": -cogs, "Gross Profit": gp, "OPEX": -opex, "EBITDA": ebitda}
        fig = go.Figure(go.Bar(x=list(wfall.keys()), y=list(wfall.values()),
            marker_color=["#c9a84c" if v > 0 else "#f87171" for v in wfall.values()]))
        fig.update_layout(**PLOTLY_BASE, title="P&L Bridge", height=280,
                          xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)

    # Charts Row 2
    st.markdown('<div class="sec-label">Trend & Mix Analysis</div>', unsafe_allow_html=True)
    c4, c5 = st.columns([3, 2])
    with c4:
        if all(c in df.columns for c in ["Year","Month_Num","Month","Net_Revenue"]):
            cols_to_group = [c for c in ["Net_Revenue","Gross_Profit","EBITDA"] if c in df.columns]
            trend = df.groupby(["Year","Month_Num","Month"])[cols_to_group].sum().reset_index()\
                      .sort_values(["Year","Month_Num"])
            trend["Period"] = trend["Year"].astype(str) + "-" + trend["Month"]
            fig = go.Figure()
            for col, color, name in zip(
                    ["Net_Revenue","Gross_Profit","EBITDA"],
                    ["#c9a84c","#4ade80","#818cf8"],
                    ["Net Revenue","Gross Profit","EBITDA"]):
                if col in trend.columns:
                    fig.add_scatter(x=trend["Period"], y=trend[col], mode="lines",
                                    name=name, line=dict(color=color, width=2))
            fig.update_layout(**PLOTLY_BASE, title="Monthly Trend: Revenue → EBITDA",
                              height=280, xaxis=dict(tickangle=-45, nticks=12, **AXIS), yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Map Year, Month, Month_Num columns to see the trend chart.")
    with c5:
        if "Channel" in df.columns and "Net_Revenue" in df.columns:
            ch = df.groupby("Channel")["Net_Revenue"].sum().reset_index()
            fig = go.Figure(go.Pie(labels=ch["Channel"], values=ch["Net_Revenue"], hole=0.55,
                marker=dict(colors=PAL, line=dict(color="#0a0a08", width=2)),
                textinfo="label+percent", textfont=dict(size=9)))
            fig.update_layout(**PLOTLY_BASE, title="Revenue Mix by Channel",
                              height=280, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    # Board Commentary
    st.markdown('<div class="sec-label">Board Commentary</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="box">
<strong>Executive Summary</strong><br>
Net Revenue of <strong>{fmt_m(nr)}</strong> — YoY growth <strong>{yoy:+.1f}%</strong> vs PY base {fmt_m(py)}.
Budget achievement <strong>{bach:.1f}%</strong>, NR variance <strong>{fmt_m(var)}</strong>.<br><br>
<strong>Profitability</strong><br>
GP Margin <strong>{gpm:.1f}%</strong> ({'above' if gpm>50 else 'below'} 50% benchmark).
EBITDA Margin <strong>{ebitdam:.1f}%</strong>. COGS {cogsp:.1f}% NR · OPEX {opexp:.1f}% NR · Trade Promo {tradep:.1f}% Base NR.<br><br>
<strong>Market &amp; Brand</strong><br>
<strong>{top_mkt}</strong> top market. <strong>{top_brand}</strong> leads brand revenue.
<strong>{risk_mkt}</strong> highest budget shortfall — requires corrective action.<br><br>
<strong>Actions Required</strong><br>
1. Review trade promo ROI in underperforming markets.<br>
2. Accelerate online channel growth — highest-margin channel.<br>
3. Tighten OPEX in markets below EBITDA threshold.
</div>""", unsafe_allow_html=True)

    # ── Budget vs Actuals Snapshot ────────────────────────────────────────
    if bdgt > 0:
        st.markdown('<div class="sec-label">Budget vs Actuals Snapshot</div>',
                    unsafe_allow_html=True)
        _var_str  = ("+" if nr >= bdgt else "") + fmt_m(nr - bdgt)
        _var_col  = "#4ade80" if nr >= bdgt else "#f87171"
        _ach_col  = "#4ade80" if bach >= 100 else "#fbbf24"
        _yoy_col  = "#4ade80" if yoy >= 0 else "#f87171"
        st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:16px;">
  <div class="kpi-card" style="--ac:{_var_col}">
    <div class="kpi-label">Actual vs Budget</div>
    <div class="kpi-value" style="color:{_var_col};">{_var_str}</div>
    <div class="kpi-delta">Achieved {nr/bdgt*100:.1f}%</div>
  </div>
  <div class="kpi-card" style="--ac:#c9a84c">
    <div class="kpi-label">Variance %</div>
    <div class="kpi-value" style="color:{_var_col};">{varp:+.1f}%</div>
    <div class="kpi-delta">vs Budget</div>
  </div>
  <div class="kpi-card" style="--ac:{_ach_col}">
    <div class="kpi-label">Budget Achievement</div>
    <div class="kpi-value" style="color:{_ach_col};">{bach:.1f}%</div>
    <div class="kpi-delta">Target: 100%</div>
  </div>
  <div class="kpi-card" style="--ac:{_yoy_col}">
    <div class="kpi-label">YoY Growth</div>
    <div class="kpi-value" style="color:{_yoy_col};">{yoy:+.1f}%</div>
    <div class="kpi-delta">vs Prior Year</div>
  </div>
</div>""", unsafe_allow_html=True)

    # Inline AI CFO
    fpa_ctx = f"NR={fmt_m(nr)} YoY={yoy:.1f}% | GP={fmt_m(gp)} GPM={gpm:.1f}% | EBITDA={fmt_m(ebitda)} {ebitdam:.1f}% | COGS {cogsp:.1f}%NR | OPEX {opexp:.1f}%NR | Budget Ach {bach:.1f}% | Var {fmt_m(var)} | Top Market={top_mkt} | Risk={risk_mkt} | Top Brand={top_brand}"
    ai_cfo_section(fpa_ctx, "fpa", "e.g. Why is margin declining? Which market needs attention?")
    if st.button("📄 Download Board Commentary (PDF)", key="fpa_pdf"):
        pdf = generate_pdf(f"Fincy Intelligence — FP&A Board Report\n\nNet Revenue: {fmt_m(nr)} | YoY: {yoy:+.1f}%\nGP Margin: {gpm:.1f}% | EBITDA: {ebitdam:.1f}%\nTop Market: {top_mkt} | Risk Market: {risk_mkt}")
        st.download_button("📄 Download PDF", data=pdf, file_name="Fincy_FPA_Report.pdf", mime="application/pdf", key="fpa_pdf_dl")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2 — RECONCILIATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
def run_recon():
    with st.sidebar:
        st.markdown("### 🔁 Reconciliation")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="recon_home"):
            for k in ["recon_sample_a","recon_sample_b"]:
                st.session_state[k] = False
            st.session_state.active_module = None
            st.rerun()
        tolerance = st.number_input("Amount Tolerance (±)", min_value=0.0,
                                    value=0.01, step=0.01,
                                    help="Amounts within this range = Matched")

    page_header("RECONCILIATION ENGINE", "Match & Flag")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #4ade80;
padding:11px 18px;margin-bottom:18px;font-size:0.76rem;color:#a09880;font-weight:300;">
<span style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
text-transform:uppercase;color:#4ade80;">How it works: </span>
Upload two CSVs — e.g. ERP export and Bank statement. Both need a common ID column
(Invoice ID, Transaction ID etc.) and an amount column. Fincy auto-matches rows,
flags amount breaks and missing records, and downloads a clean exceptions report.
</div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="sec-label">Source A — ERP / System 1</div>', unsafe_allow_html=True)
        f1 = st.file_uploader("Upload Source A (CSV)", type=["csv"], key="rf1")
        if st.button("📊 Use ERP Sample (Source A)", use_container_width=True, key="rs1"):
            st.session_state.recon_sample_a = True
            st.rerun()
    with c2:
        st.markdown('<div class="sec-label">Source B — Bank / System 2</div>', unsafe_allow_html=True)
        f2 = st.file_uploader("Upload Source B (CSV)", type=["csv"], key="rf2")
        if st.button("📊 Use Bank Sample (Source B)", use_container_width=True, key="rs2"):
            st.session_state.recon_sample_b = True
            st.rerun()

    use_a = st.session_state.recon_sample_a
    use_b = st.session_state.recon_sample_b
    def _safe_csv(fileobj, fallback_str):
        if fileobj is None: return pd.read_csv(io.StringIO(fallback_str))
        try:
            result = pd.read_csv(fileobj)
            if result.empty: st.error("⚠️ Uploaded file is empty."); return None
            return result
        except Exception as e:
            st.error(f"⚠️ Could not read CSV: {e}"); return None
    df1 = _safe_csv(f1 if f1 else None, SAMPLE_RECON_A) if (use_a or f1) else None
    df2 = _safe_csv(f2 if f2 else None, SAMPLE_RECON_B) if (use_b or f2) else None

    if df1 is None or df2 is None:
        st.markdown("""<div class="box" style="opacity:0.6;font-size:0.74rem;">
↑ Upload both files above or click the sample buttons.<br><br>
<strong>Use cases:</strong> ERP vs Bank · GL vs Sub-ledger · PO vs Invoice · Intercompany<br>
<strong>Output:</strong> Match rate · Amount breaks · Missing records · Exceptions CSV
</div>""", unsafe_allow_html=True)
        return

    cols1   = list(df1.columns)
    cols2   = list(df2.columns)
    common  = [c for c in cols1 if c in cols2]

    # ── Key column config ────────────────────────────────────────────────────
    st.markdown('<div class="sec-label">Configure Match</div>', unsafe_allow_html=True)
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        kg   = next((c for c in common if any(k in c.lower()
               for k in ["id","no","number","ref","invoice","trans"])), common[0] if common else cols1[0])
        mkey = st.selectbox("Match Key Column", common if common else cols1,
                            index=common.index(kg) if kg in common else 0, key="recon_mkey")
    with mc2:
        n1  = [c for c in cols1 if pd.api.types.is_numeric_dtype(df1[c])]
        ag1 = next((c for c in n1 if any(k in c.lower()
              for k in ["amount","amt","erp","value","total"])), n1[0] if n1 else cols1[0])
        a1_col = st.selectbox("Amount (Source A)", n1 if n1 else cols1,
                              index=n1.index(ag1) if ag1 in n1 else 0, key="recon_a1")
    with mc3:
        n2  = [c for c in cols2 if pd.api.types.is_numeric_dtype(df2[c])]
        ag2 = next((c for c in n2 if any(k in c.lower()
              for k in ["amount","amt","bank","value","total"])), n2[0] if n2 else cols2[0])
        a2_col = st.selectbox("Amount (Source B)", n2 if n2 else cols2,
                              index=n2.index(ag2) if ag2 in n2 else 0, key="recon_a2")

    # ── Duplicate key detection & composite key builder ──────────────────────
    dup_a = df1[mkey].duplicated().sum()
    dup_b = df2[mkey].duplicated().sum()

    secondary_key = None
    tertiary_key  = None
    if dup_a > 0 or dup_b > 0:
        st.markdown(f"""
<div style="background:#150f00;border:1px solid #fbbf24;border-left:3px solid #fbbf24;
padding:12px 18px;margin-bottom:12px;">
<div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;
text-transform:uppercase;color:#fbbf24;margin-bottom:6px;">⚠️ Match Key Has Duplicates</div>
<div style="font-size:0.76rem;color:#a09880;font-weight:300;">
<strong style="color:#fafaf8;">{mkey}</strong> is not a unique transaction ID —
Source A has <strong style="color:#fbbf24;">{dup_a} duplicate</strong> values,
Source B has <strong style="color:#fbbf24;">{dup_b} duplicate</strong> values.<br>
Matching on a non-unique column alone causes a cartesian product, producing thousands of
false Amount Breaks. Add one or two more columns to build a composite key.
<br><br>
<strong style="color:#fafaf8;">💡 Tip for bank/ERP reconciliation:</strong>
Use <em>Category + Date + Amount</em> as a 3-part key for the most accurate match.
</div>
</div>""", unsafe_allow_html=True)

        sk_opts = ["— none —"] + [c for c in common if c != mkey]
        # Auto-suggest date as second key
        date_guess = next((c for c in sk_opts if any(k in c.lower()
                      for k in ["date","period","month","year","trans"])), sk_opts[0])
        secondary_key_raw = st.selectbox(
            "2nd Key Column (e.g. transaction date)",
            sk_opts, index=sk_opts.index(date_guess) if date_guess in sk_opts else 0,
            key="recon_mkey2")
        secondary_key = secondary_key_raw if secondary_key_raw != "— none —" else None

        tk_opts = ["— none —"] + [c for c in common if c not in [mkey, secondary_key_raw]]
        tertiary_key_raw = st.selectbox(
            "3rd Key Column (e.g. amount — for highest accuracy)",
            tk_opts, index=0, key="recon_mkey3",
            help="Adding amount as a 3rd key achieves zero amount-breaks when amounts uniquely identify transactions")
        tertiary_key = tertiary_key_raw if tertiary_key_raw != "— none —" else None

    if st.button("🔁 Run Reconciliation", use_container_width=True, key="run_recon"):

        # ── Build match key (up to 3 columns) ───────────────────────────────
        def make_key(df, primary, secondary=None, tertiary=None):
            k = df[primary].astype(str)
            if secondary: k = k + "||" + df[secondary].astype(str)
            if tertiary:  k = k + "||" + df[tertiary].astype(str)
            return k

        df1["_match_key"] = make_key(df1, mkey, secondary_key, tertiary_key)
        df2["_match_key"] = make_key(df2, mkey, secondary_key, tertiary_key)

        # ── Add within-group sequence to handle legitimate duplicate rows ────
        # e.g. same vendor paid same amount twice on same date → both are valid
        df1["_seq"] = df1.groupby("_match_key").cumcount()
        df2["_seq"] = df2.groupby("_match_key").cumcount()
        df1["_full_key"] = df1["_match_key"] + "||" + df1["_seq"].astype(str)
        df2["_full_key"] = df2["_match_key"] + "||" + df2["_seq"].astype(str)

        # ── Build left/right with correct column renaming ────────────────────
        # Exclude a2_col from b_rename so it becomes Amt_B (not Amt_B + n_amount_B clash)
        _df1 = df1.copy(); _df2 = df2.copy()
        b_rename = {c: c+"_B" for c in _df2.columns
                    if c in _df1.columns and c not in ["_match_key","_seq","_full_key", a2_col]}
        left  = _df1.drop(columns=["_match_key","_seq"]).rename(columns={a1_col:"Amt_A"})
        right = _df2.drop(columns=["_match_key","_seq"]).rename(
                    columns={**{a2_col:"Amt_B"}, **b_rename})
        merged = pd.merge(left, right, on="_full_key", how="outer", indicator=True)

        def classify(r):
            if r["_merge"] == "left_only":  return "Missing in B"
            if r["_merge"] == "right_only": return "Missing in A"
            a, b = r["Amt_A"], r["Amt_B"]
            if pd.isna(a) or pd.isna(b): return "Amount Break"
            return "Matched" if abs(float(a)-float(b)) <= tolerance else "Amount Break"

        merged["Status"]     = merged.apply(classify, axis=1)
        merged["Difference"] = merged["Amt_A"].fillna(0) - merged["Amt_B"].fillna(0)

        # Fill NaN key columns for Missing-in-A rows from B-side equivalents
        for _col in [mkey, secondary_key, tertiary_key]:
            if not _col: continue
            _bcol = _col + "_B"
            if _bcol in merged.columns and _col in merged.columns:
                merged[_col] = merged[_col].fillna(merged[_bcol])
        # Also fill non-key original columns
        for _orig in list(_df1.columns):
            _bc = _orig + "_B"
            if _bc in merged.columns and _orig in merged.columns:
                merged[_orig] = merged[_orig].fillna(merged[_bc])

        # Clean output: key cols + amounts + status + diff (drop internal + _B cols)
        _drop = {"_full_key","_merge"} | {c for c in merged.columns if c.endswith("_B")}
        _meta = [c for c in merged.columns if c not in _drop
                 and c not in ["Amt_A","Amt_B","Status","Difference"]]
        out_cols = _meta + ["Amt_A","Amt_B","Status","Difference"]
        merged_out = merged[[c for c in out_cols if c in merged.columns]].copy()

        total   = len(merged_out)
        matched = (merged_out["Status"]=="Matched").sum()
        breaks  = (merged_out["Status"]=="Amount Break").sum()
        miss_b  = (merged_out["Status"]=="Missing in B").sum()
        miss_a  = (merged_out["Status"]=="Missing in A").sum()
        mrate   = matched/total*100 if total else 0
        t_break = merged_out.loc[merged_out["Status"]=="Amount Break","Difference"].abs().sum()

        # Show composite key info
        key_parts = [k for k in [mkey, secondary_key, tertiary_key] if k]
        if len(key_parts) > 1:
            key_display = " + ".join(key_parts)
            st.markdown(f"""<div style="background:#041508;border:1px solid #4ade80;
padding:9px 16px;margin-bottom:12px;font-family:'IBM Plex Mono',monospace;
font-size:0.6rem;letter-spacing:0.1em;color:#4ade80;">
✓ {len(key_parts)}-part composite key: <strong>{key_display}</strong>
</div>""", unsafe_allow_html=True)

        st.markdown('<div class="sec-label">Reconciliation Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="rag-row">
<div class="rag-g"><div class="rag-lbl">Matched</div><div class="rag-val" style="color:#4ade80;">{matched:,}</div><div style="font-size:0.6rem;color:#4ade80;">{mrate:.1f}% match rate</div></div>
<div class="rag-r"><div class="rag-lbl">Amount Breaks</div><div class="rag-val" style="color:#f87171;">{breaks:,}</div><div style="font-size:0.6rem;color:#f87171;">Diff: {t_break:,.2f}</div></div>
<div class="rag-a"><div class="rag-lbl">Missing in B</div><div class="rag-val" style="color:#fbbf24;">{miss_b:,}</div><div style="font-size:0.6rem;color:#fbbf24;">In A only</div></div>
<div class="rag-b"><div class="rag-lbl">Missing in A</div><div class="rag-val" style="color:#60a5fa;">{miss_a:,}</div><div style="font-size:0.6rem;color:#60a5fa;">In B only</div></div>
</div>""", unsafe_allow_html=True)

        ch1, ch2 = st.columns([1, 2])
        with ch1:
            fig = go.Figure(go.Pie(
                labels=["Matched","Amount Break","Missing in B","Missing in A"],
                values=[matched, breaks, miss_b, miss_a], hole=0.62,
                marker=dict(colors=["#4ade80","#f87171","#fbbf24","#60a5fa"],
                            line=dict(color="#0a0a08", width=2)),
                textinfo="label+percent", textfont=dict(size=9)))
            fig.add_annotation(text=f"{mrate:.0f}%<br>Matched", x=0.5, y=0.5,
                               showarrow=False,
                               font=dict(size=13, color="#fafaf8", family="Playfair Display"))
            fig.update_layout(**PLOTLY_BASE, title="Reconciliation Status",
                              height=270, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        with ch2:
            dbs = merged_out.groupby("Status")["Difference"].sum().reset_index()
            fig = go.Figure(go.Bar(x=dbs["Status"], y=dbs["Difference"],
                marker_color=["#4ade80" if v >= 0 else "#f87171" for v in dbs["Difference"]],
                text=dbs["Difference"].apply(lambda x: f"{x:+,.2f}"), textposition="auto"))
            fig.update_layout(**PLOTLY_BASE, title="Net Difference by Status",
                              height=270, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)

        exc = merged_out[merged_out["Status"] != "Matched"].copy()
        if not exc.empty:
            st.markdown('<div class="sec-label">Exceptions Detail</div>', unsafe_allow_html=True)
            sf = st.multiselect("Filter Status",
                                ["Amount Break","Missing in B","Missing in A"],
                                default=["Amount Break","Missing in B","Missing in A"],
                                key="recon_sf")
            fe = exc[exc["Status"].isin(sf)]
            st.dataframe(fe, use_container_width=True, hide_index=True)
            st.download_button("📥 Download Exceptions (CSV)",
                               fe.to_csv(index=False).encode(),
                               "Fincy_Recon_Exceptions.csv", "text/csv")
        else:
            st.success("🎉 Perfect reconciliation — no exceptions found!")

        st.markdown('<div class="sec-label">Full Reconciliation Output</div>', unsafe_allow_html=True)
        st.dataframe(merged_out, use_container_width=True, hide_index=True)
        st.download_button("📥 Download Full Recon Output (CSV)",
                           merged_out.to_csv(index=False).encode(),
                           "Fincy_Recon_Full.csv", "text/csv")

        # AI CFO — inside the button block so vars are in scope
        recon_ctx = (f"Reconciliation: {total} records | "
                     f"Matched={matched} ({mrate:.1f}%) | "
                     f"Amount Breaks={breaks} (total diff={t_break:,.0f}) | "
                     f"Missing in B={miss_b} | Missing in A={miss_a} | "
                     f"Key used: {'+'.join([k for k in [mkey,secondary_key,tertiary_key] if k])}")
        ai_cfo_section(recon_ctx, "recon",
            "e.g. What caused the missing records? Which breaks need urgent action?")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3 — BUDGET vs ACTUALS TRACKER
# ══════════════════════════════════════════════════════════════════════════════
def run_budget():
    with st.sidebar:
        st.markdown("### 🎯 Budget Tracker")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="budget_home"):
            st.session_state.budget_use_sample = False
            st.session_state.active_module = None
            st.rerun()
        green_t = st.slider("🟢 Green (%)", 90, 100, 95, key="gt")
        amber_t = st.slider("🟡 Amber (%)", 70, 95,  80, key="at")

    page_header("BUDGET vs ACTUALS", "RAG Tracker")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #fbbf24;
padding:11px 18px;margin-bottom:18px;font-size:0.76rem;color:#a09880;font-weight:300;">
<span style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
text-transform:uppercase;color:#fbbf24;">How it works: </span>
Upload a CSV with Period, Actual, and Budget columns (+ optional Prior Year).
Fincy auto-maps columns, computes RAG status per line, draws trend charts,
and the AI CFO writes board commentary — all in under 30 seconds.
</div>""", unsafe_allow_html=True)

    _, cc, _ = st.columns([1, 2, 1])
    with cc:
        if st.button("📊 Use Budget Sample Data  (no upload needed)",
                     use_container_width=True, key="budget_sample"):
            st.session_state.budget_use_sample = True
            st.rerun()
        st.markdown("""<div style="text-align:center;margin:12px 0 8px;
font-family:'IBM Plex Mono',monospace;font-size:0.6rem;color:#3a3a34;">
— or upload your own —</div>""", unsafe_allow_html=True)
        bfile = st.file_uploader("Upload Budget vs Actuals CSV", type=["csv"],
                                 key="bfile", help="Needs Period, Actual, Budget columns")

    use_s = st.session_state.budget_use_sample
    if use_s and not bfile:
        df = pd.read_csv(io.StringIO(SAMPLE_BUDGET))
    elif bfile:
        try:
            df = pd.read_csv(bfile)
            if df.empty:
                st.error("⚠️ Uploaded file is empty. Please check and re-upload.")
                df = None
        except Exception as e:
            st.error(f"⚠️ Could not read your CSV: {e}. Ensure it is a valid comma-separated file.")
            df = None
    else:
        df = None

    if df is None:
        st.markdown("""<div class="box" style="opacity:0.6;font-size:0.74rem;">
↑ Upload your CSV or click the sample button above.<br><br>
<strong>Needs:</strong> Period · Actual · Budget columns &nbsp;|&nbsp;
<strong>Optional:</strong> Prior Year · Dimension (Category / Market / Brand)<br>
<strong>Output:</strong> RAG status per line · YoY chart · AI trend analysis · Board commentary · CSV
</div>""", unsafe_allow_html=True)
        return

    csv_cols = list(df.columns)
    st.markdown('<div class="sec-label">Map Columns</div>', unsafe_allow_html=True)
    bc1, bc2, bc3, bc4, bc5 = st.columns(5)
    with bc1:
        pg = next((c for c in csv_cols if any(k in c.lower()
             for k in ["period","month","date","year","quarter"])), csv_cols[0])
        per_col = st.selectbox("Period", csv_cols, index=csv_cols.index(pg), key="b_per")
    with bc2:
        ag = next((c for c in csv_cols if any(k in c.lower()
             for k in ["actual","actuals","act"])), csv_cols[0])
        act_col = st.selectbox("Actual", csv_cols, index=csv_cols.index(ag), key="b_act")
    with bc3:
        bg = next((c for c in csv_cols if any(k in c.lower()
             for k in ["budget","plan","target"])), csv_cols[0])
        bud_col = st.selectbox("Budget", csv_cols, index=csv_cols.index(bg), key="b_bud")
    with bc4:
        py_opts = ["— none —"] + csv_cols
        pyg     = next((c for c in csv_cols if any(k in c.lower()
                  for k in ["prior","previous","py","last","ly"])), "— none —")
        py_col  = st.selectbox("Prior Year (opt)", py_opts,
                               index=py_opts.index(pyg) if pyg in py_opts else 0, key="b_py")
    with bc5:
        dim_opts = ["— none —"] + csv_cols
        dg       = next((c for c in csv_cols if any(k in c.lower()
                   for k in ["category","brand","market","segment","dept"])), "— none —")
        dim_col  = st.selectbox("Dimension (opt)", dim_opts,
                                index=dim_opts.index(dg) if dg in dim_opts else 0, key="b_dim")

    run_clicked = st.button("🎯 Run Budget Tracker", use_container_width=True, key="run_budget")
    if run_clicked:
        st.session_state["_budget_df"]      = df.copy()
        st.session_state["_budget_cols"]    = (per_col, act_col, bud_col, py_col, dim_col)
        st.session_state["_budget_ready"]   = True

    if not st.session_state.get("_budget_ready"):
        st.markdown('''<div class="box" style="opacity:0.5;font-size:0.74rem;">
← Configure columns above and click Run Budget Tracker to generate the dashboard.
</div>''', unsafe_allow_html=True)
        return

    df      = st.session_state["_budget_df"].copy()
    per_col, act_col, bud_col, py_col, dim_col = st.session_state["_budget_cols"]

    df["_A"] = pd.to_numeric(df[act_col], errors="coerce").fillna(0)
    df["_B"] = pd.to_numeric(df[bud_col], errors="coerce").fillna(0)
    df["_V"] = df["_A"] - df["_B"]
    df["_VP"]= df.apply(lambda r: r["_V"]/r["_B"]*100 if r["_B"] else 0, axis=1)
    df["_AP"]= df.apply(lambda r: r["_A"]/r["_B"]*100 if r["_B"] else 0, axis=1)

    has_py = py_col != "— none —"
    if has_py:
        df["_PY"] = pd.to_numeric(df[py_col], errors="coerce").fillna(0)
        df["_YoY"]= df.apply(lambda r: (r["_A"]-r["_PY"])/r["_PY"]*100 if r["_PY"] else 0, axis=1)

    def rag(a): return "🟢 Green" if a >= green_t else ("🟡 Amber" if a >= amber_t else "🔴 Red")
    df["_RAG"] = df["_AP"].apply(rag)

    ta   = df["_A"].sum(); tb = df["_B"].sum(); tv = ta - tb
    tach = ta/tb*100 if tb else 0
    tpy  = df["_PY"].sum() if has_py else 0
    tyoy = (ta-tpy)/tpy*100 if has_py and tpy else 0
    gc   = (df["_RAG"]=="🟢 Green").sum()
    rc   = (df["_RAG"]=="🔴 Red").sum()
    ac   = (df["_RAG"]=="🟡 Amber").sum()

    # Period grouping
    py_cols_g = ["_A","_B","_V","_PY"] if has_py else ["_A","_B","_V"]
    pg_df = df.groupby(per_col)[py_cols_g].sum().reset_index()
    trend_dir = "improving" if len(pg_df) >= 3 and \
                pg_df["_V"].iloc[-1] > pg_df["_V"].iloc[0] else "deteriorating"

    # Summary KPIs
    st.markdown('<div class="sec-label">Budget Performance Summary</div>', unsafe_allow_html=True)
    yoy_class = "rag-g" if tyoy >= 0 else "rag-r"
    yoy_color = "#4ade80" if tyoy >= 0 else "#f87171"
    yoy_cell  = f'<div class="{yoy_class}"><div class="rag-lbl">YoY Growth</div><div class="rag-val" style="color:{yoy_color};">{tyoy:+.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">vs PY {fmt_m(tpy)}</div></div>' if has_py else ""
    tv_class  = "rag-g" if tv >= 0 else "rag-r"
    tv_color  = "#4ade80" if tv >= 0 else "#f87171"
    st.markdown(f"""
<div class="rag-row">
<div class="{tv_class}"><div class="rag-lbl">Total Actual</div><div class="rag-val" style="color:{tv_color};">{fmt_m(ta)}</div><div style="font-size:0.6rem;color:#5a5648;">vs Budget {fmt_m(tb)}</div></div>
<div class="{tv_class}"><div class="rag-lbl">Variance</div><div class="rag-val" style="color:{tv_color};">{tv:+,.0f}</div><div style="font-size:0.6rem;color:{tv_color};">{tach:.1f}% achieved</div></div>
{yoy_cell}
<div class="rag-g"><div class="rag-lbl">🟢 On Track</div><div class="rag-val" style="color:#4ade80;">{gc}</div><div style="font-size:0.6rem;color:#4ade80;">{ac} amber</div></div>
<div class="rag-r"><div class="rag-lbl">🔴 Off Track</div><div class="rag-val" style="color:#f87171;">{rc}</div><div style="font-size:0.6rem;color:#5a5648;">lines</div></div>
</div>""", unsafe_allow_html=True)

    # Trend chart
    st.markdown('<div class="sec-label">Actual vs Budget vs Prior Year</div>', unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_bar(x=pg_df[per_col], y=pg_df["_B"], name="Budget", marker_color="rgba(99,102,241,0.35)")
    fig.add_bar(x=pg_df[per_col], y=pg_df["_A"], name="Actual", marker_color="#c9a84c")
    if has_py and "_PY" in pg_df.columns:
        fig.add_scatter(x=pg_df[per_col], y=pg_df["_PY"], name="Prior Year", mode="lines+markers",
                        line=dict(color="#fbbf24", width=2, dash="dash"), marker=dict(size=5))
    fig.add_scatter(x=pg_df[per_col], y=pg_df["_V"], name="Variance", mode="lines+markers",
                    line=dict(color="#f87171", width=2, dash="dot"), yaxis="y2")
    fig.update_layout(**PLOTLY_BASE, title="Actual vs Budget vs Prior Year",
                      barmode="overlay", height=340,
                      xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS,
                      yaxis2=dict(overlaying="y", side="right", gridcolor="#1a1a16",
                                  tickfont=dict(size=9), title_text="Variance"))
    st.plotly_chart(fig, use_container_width=True)

    # Dimension chart
    if dim_col != "— none —":
        st.markdown('<div class="sec-label">Variance by Dimension</div>', unsafe_allow_html=True)
        dg_data = df.groupby(dim_col)[["_A","_B","_V"]].sum().reset_index().sort_values("_V")
        fig = go.Figure(go.Bar(
            x=dg_data["_V"], y=dg_data[dim_col], orientation="h",
            marker_color=["#f87171" if v < 0 else "#4ade80" for v in dg_data["_V"]],
            text=dg_data["_V"].apply(lambda x: f"{x:+,.0f}"), textposition="auto"))
        fig.update_layout(**PLOTLY_BASE, title=f"Variance by {dim_col}",
                          height=280, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)

    # RAG Table
    st.markdown('<div class="sec-label">Line-by-Line RAG Status</div>', unsafe_allow_html=True)
    dcols = [per_col, act_col, bud_col, "_V", "_VP", "_AP", "_RAG"]
    if has_py:  dcols = [per_col, act_col, bud_col, py_col, "_V", "_VP", "_AP", "_YoY", "_RAG"]
    if dim_col != "— none —": dcols = [per_col, dim_col] + dcols[1:]
    disp = df[[c for c in dcols if c in df.columns]].copy()
    rename_map = {"_V":"Variance","_VP":"Var%","_AP":"Achiev%","_YoY":"YoY%","_RAG":"RAG"}
    disp.columns = [rename_map.get(c, c) for c in disp.columns]
    st.dataframe(disp, use_container_width=True, hide_index=True)

    # Board commentary
    top_over  = pg_df.loc[pg_df["_V"].idxmax(), per_col]
    top_under = pg_df.loc[pg_df["_V"].idxmin(), per_col]
    py_line   = f" Against prior year: <strong>{tyoy:+.1f}%</strong> YoY (PY {fmt_m(tpy)})." if has_py else ""
    st.markdown('<div class="sec-label">Auto-Generated Board Commentary</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="box">
<strong>Budget Performance Summary</strong><br>
Total actuals <strong>{fmt_m(ta)}</strong> vs budget <strong>{fmt_m(tb)}</strong> —
{'favourable' if tv>=0 else 'adverse'} variance <strong>{tv:+,.0f}</strong> ({tach:.1f}% achievement).{py_line}<br><br>
<strong>RAG:</strong> {gc} Green · {ac} Amber · {rc} Red. Trend (last periods): <strong>{trend_dir}</strong>.<br><br>
<strong>Highlights:</strong> <strong>{top_over}</strong> strongest vs budget.
<strong>{top_under}</strong> largest shortfall — management attention required.<br><br>
<strong>Actions:</strong><br>
1. Investigate {top_under} — phasing issue or structural underperformance?<br>
2. Replicate {top_over} success factors across underperforming periods.<br>
3. Escalate all 🔴 Red lines to business owners for corrective action plans.
</div>""", unsafe_allow_html=True)

    # AI CFO inline — replaces old button-only pattern
    budget_ctx = (f"Budget vs Actuals: Actual={fmt_m(ta)} Budget={fmt_m(tb)} "
                  f"Variance={tv:+,.0f} Achievement={tach:.1f}% "
                  f"RAG=Green:{gc} Amber:{ac} Red:{rc} Trend={trend_dir} "
                  f"Best period={top_over} Worst={top_under}"
                  + (f" YoY={tyoy:+.1f}% vs PY={fmt_m(tpy)}" if has_py else ""))
    ai_cfo_section(budget_ctx, "budget",
        "e.g. Which periods need attention? What caused the variance? What actions do you recommend?")
    st.download_button("📥 Download RAG Report (CSV)", disp.to_csv(index=False).encode(),
                       "Fincy_Budget_RAG.csv", "text/csv")



# ══════════════════════════════════════════════════════════════════════════════
# MODULE 4 — COST INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_cost():
    with st.sidebar:
        st.markdown("### 💡 Cost Intelligence")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="cost_home"):
            st.session_state.cost_use_sample = False
            st.session_state.active_module   = None
            st.rerun()
        cogs_bench = st.slider("COGS Benchmark (% Rev)", 20, 80, 50, key="cb")
        opex_bench = st.slider("OPEX Benchmark (% Rev)",  5, 40, 20, key="ob")

    page_header("COST INTELLIGENCE", "Benchmarking")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #f472b6;
padding:11px 18px;margin-bottom:18px;font-size:0.76rem;color:#a09880;font-weight:300;">
<span style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
text-transform:uppercase;color:#f472b6;">How it works: </span>
Upload a CSV with Revenue, COGS, and OPEX columns (+ optional Period and Segment/SKU).
Set your own COGS and OPEX benchmarks in the sidebar. Fincy flags every line above
threshold, draws efficiency charts, and the AI CFO gives specific cost reduction actions.
</div>""", unsafe_allow_html=True)

    _, cc, _ = st.columns([1, 2, 1])
    with cc:
        if st.button("📊 Use Cost Sample Data  (no upload needed)",
                     use_container_width=True, key="cost_sample"):
            st.session_state.cost_use_sample = True
            st.rerun()
        st.markdown("""<div style="text-align:center;margin:12px 0 8px;
font-family:'IBM Plex Mono',monospace;font-size:0.6rem;color:#3a3a34;">
— or upload your own —</div>""", unsafe_allow_html=True)
        cfile = st.file_uploader("Upload Cost Data CSV", type=["csv"],
                                 key="cfile", help="Revenue, COGS, OPEX columns + optional Period/Segment")

    use_s = st.session_state.cost_use_sample
    if use_s and not cfile:
        df = pd.read_csv(io.StringIO(SAMPLE_COST))
    elif cfile:
        try:
            df = pd.read_csv(cfile)
            if df.empty:
                st.error("⚠️ Uploaded file is empty. Please check and re-upload.")
                df = None
        except Exception as e:
            st.error(f"⚠️ Could not read your CSV: {e}. Ensure it is a valid comma-separated file.")
            df = None
    else:
        df = None

    if df is None:
        st.markdown("""<div class="box" style="opacity:0.6;font-size:0.74rem;">
↑ Upload your cost data CSV or click the sample button above.<br><br>
<strong>Needs:</strong> Revenue · COGS · OPEX columns<br>
<strong>Optional:</strong> Period · Segment / SKU / Market<br>
<strong>Output:</strong> Cost ratios vs benchmarks · Flagged lines · Waterfall · AI recommendations
</div>""", unsafe_allow_html=True)
        return

    csv_cols = list(df.columns)
    st.markdown('<div class="sec-label">Map Columns</div>', unsafe_allow_html=True)
    cc1, cc2, cc3, cc4, cc5 = st.columns(5)
    with cc1:
        rg  = next((c for c in csv_cols if any(k in c.lower()
              for k in ["revenue","net_rev","sales"])), csv_cols[0])
        rev_col  = st.selectbox("Revenue", csv_cols, index=csv_cols.index(rg), key="c_rev")
    with cc2:
        cg  = next((c for c in csv_cols if "cog" in c.lower()), csv_cols[0])
        cogs_col = st.selectbox("COGS", csv_cols, index=csv_cols.index(cg), key="c_cogs")
    with cc3:
        og  = next((c for c in csv_cols if "opex" in c.lower() or "operating" in c.lower()), csv_cols[0])
        opex_col = st.selectbox("OPEX", csv_cols, index=csv_cols.index(og), key="c_opex")
    with cc4:
        ppg = next((c for c in csv_cols if any(k in c.lower()
              for k in ["period","month","date","year"])), csv_cols[0])
        per_col  = st.selectbox("Period", csv_cols, index=csv_cols.index(ppg), key="c_per")
    with cc5:
        dim_opts = ["— none —"] + csv_cols
        dg       = next((c for c in csv_cols if any(k in c.lower()
                   for k in ["sku","category","brand","market","segment","product"])), "— none —")
        dim_col  = st.selectbox("Segment/SKU (opt)", dim_opts,
                                index=dim_opts.index(dg) if dg in dim_opts else 0, key="c_dim")

    run_clicked = st.button("💡 Run Cost Intelligence", use_container_width=True, key="run_cost")
    if run_clicked:
        st.session_state["_cost_df"]    = df.copy()
        st.session_state["_cost_cols"]  = (per_col, rev_col, cogs_col, opex_col, dim_col)
        st.session_state["_cost_ready"] = True

    if not st.session_state.get("_cost_ready"):
        st.markdown('''<div class="box" style="opacity:0.5;font-size:0.74rem;">
← Configure columns above and click Run Cost Intelligence to generate the dashboard.
</div>''', unsafe_allow_html=True)
        return

    df     = st.session_state["_cost_df"].copy()
    per_col, rev_col, cogs_col, opex_col, dim_col = st.session_state["_cost_cols"]

    df["_R"]  = pd.to_numeric(df[rev_col],  errors="coerce").fillna(0)
    df["_C"]  = pd.to_numeric(df[cogs_col], errors="coerce").fillna(0)
    df["_O"]  = pd.to_numeric(df[opex_col], errors="coerce").fillna(0)
    df["_GP"] = df["_R"] - df["_C"]
    df["_EB"] = df["_GP"] - df["_O"]
    df["_CP"] = df.apply(lambda r: r["_C"]/r["_R"]*100 if r["_R"] else 0, axis=1)
    df["_OP"] = df.apply(lambda r: r["_O"]/r["_R"]*100 if r["_R"] else 0, axis=1)
    df["_GPM"]= df.apply(lambda r: r["_GP"]/r["_R"]*100 if r["_R"] else 0, axis=1)
    df["_Flag"]= df.apply(
        lambda r: "⚠️ Above Bench" if r["_CP"]>cogs_bench or r["_OP"]>opex_bench else "✅ Within Bench",
        axis=1)

    tr  = df["_R"].sum();  tc  = df["_C"].sum();  to  = df["_O"].sum()
    tgp = df["_GP"].sum(); teb = df["_EB"].sum()
    acp = tc/tr*100 if tr else 0
    aop = to/tr*100 if tr else 0
    agpm= tgp/tr*100 if tr else 0
    above = (df["_Flag"]=="⚠️ Above Bench").sum()

    st.markdown('<div class="sec-label">Cost Performance Summary</div>', unsafe_allow_html=True)
    cogs_ok = acp <= cogs_bench; opex_ok = aop <= opex_bench
    st.markdown(f"""
<div class="rag-row">
<div class="{'rag-g' if cogs_ok else 'rag-r'}"><div class="rag-lbl">COGS % Revenue</div><div class="rag-val" style="color:{'#4ade80' if cogs_ok else '#f87171'};">{acp:.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">Bench: {cogs_bench}%</div></div>
<div class="{'rag-g' if opex_ok else 'rag-r'}"><div class="rag-lbl">OPEX % Revenue</div><div class="rag-val" style="color:{'#4ade80' if opex_ok else '#f87171'};">{aop:.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">Bench: {opex_bench}%</div></div>
<div class="rag-g"><div class="rag-lbl">GP Margin</div><div class="rag-val" style="color:#4ade80;">{agpm:.1f}%</div><div style="font-size:0.6rem;color:#4ade80;">Gross Profit</div></div>
<div class="{'rag-r' if above>0 else 'rag-g'}"><div class="rag-lbl">Above Benchmark</div><div class="rag-val" style="color:{'#f87171' if above>0 else '#4ade80'};">{above}</div><div style="font-size:0.6rem;color:#5a5648;">lines flagged</div></div>
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-label">Cost Ratios Over Time</div>', unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    with ch1:
        pg = df.groupby(per_col)[["_R","_C","_O","_GP"]].sum().reset_index()
        pg["_CP"] = pg["_C"]/pg["_R"]*100; pg["_OP"] = pg["_O"]/pg["_R"]*100
        pg["_GPM"]= pg["_GP"]/pg["_R"]*100
        fig = go.Figure()
        fig.add_scatter(x=pg[per_col], y=pg["_CP"],  name="COGS %",
                        mode="lines+markers", line=dict(color="#f87171", width=2))
        fig.add_scatter(x=pg[per_col], y=pg["_OP"],  name="OPEX %",
                        mode="lines+markers", line=dict(color="#fbbf24", width=2))
        fig.add_scatter(x=pg[per_col], y=pg["_GPM"], name="GP Margin %",
                        mode="lines+markers", line=dict(color="#4ade80", width=2))
        fig.add_hline(y=cogs_bench, line_dash="dot", line_color="#f87171",
                      annotation_text=f"COGS Bench {cogs_bench}%")
        fig.add_hline(y=opex_bench, line_dash="dot", line_color="#fbbf24",
                      annotation_text=f"OPEX Bench {opex_bench}%")
        fig.update_layout(**PLOTLY_BASE, title="Cost Ratios Over Time", height=300,
                          xaxis=dict(tickangle=-30, **AXIS), yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)
    with ch2:
        wf = {"Revenue":tr,"COGS":-tc,"Gross Profit":tgp,"OPEX":-to,"EBITDA":teb}
        fig = go.Figure(go.Bar(x=list(wf.keys()), y=list(wf.values()),
            marker_color=["#c9a84c","#f87171","#4ade80","#fbbf24","#818cf8"]))
        fig.update_layout(**PLOTLY_BASE, title="Cost Waterfall", height=300,
                          xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)

    if dim_col != "— none —":
        st.markdown('<div class="sec-label">Cost Efficiency by Segment</div>', unsafe_allow_html=True)
        sg = df.groupby(dim_col)[["_R","_C","_O","_GP"]].sum().reset_index()
        sg["_CP"] = sg["_C"]/sg["_R"]*100; sg["_OP"] = sg["_O"]/sg["_R"]*100
        sg["_GPM"]= sg["_GP"]/sg["_R"]*100
        sg = sg.sort_values("_GPM", ascending=False)
        fig = go.Figure()
        fig.add_bar(x=sg[dim_col], y=sg["_CP"], name="COGS %", marker_color="#f87171")
        fig.add_bar(x=sg[dim_col], y=sg["_OP"], name="OPEX %", marker_color="#fbbf24")
        fig.add_scatter(x=sg[dim_col], y=sg["_GPM"], name="GP Margin %",
                        mode="lines+markers", line=dict(color="#4ade80", width=2), yaxis="y2")
        fig.add_hline(y=cogs_bench, line_dash="dot", line_color="#f87171")
        fig.update_layout(**PLOTLY_BASE, title=f"Cost Efficiency by {dim_col}",
                          barmode="stack", height=300, xaxis=AXIS, yaxis=AXIS,
                          yaxis2=dict(overlaying="y", side="right",
                                      gridcolor="#1a1a16", tickfont=dict(size=9)))
        st.plotly_chart(fig, use_container_width=True)
    else:
        sg = None

    flagged = df[df["_Flag"]=="⚠️ Above Bench"]
    if not flagged.empty:
        st.markdown('<div class="sec-label">⚠️ Lines Above Benchmark</div>', unsafe_allow_html=True)
        show = [per_col, rev_col, cogs_col, opex_col, "_CP", "_OP", "_GPM", "_Flag"]
        if dim_col != "— none —": show = [per_col, dim_col] + show[1:]
        st.dataframe(flagged[[c for c in show if c in flagged.columns]],
                     use_container_width=True, hide_index=True)

    # AI CFO inline
    worst_seg = str(sg.loc[sg["_CP"].idxmax(), dim_col]) if sg is not None and len(sg) > 0 else "N/A"
    cost_ctx = (f"Cost Intelligence: Revenue={fmt_m(tr)} COGS={fmt_m(tc)} ({acp:.1f}% vs bench {cogs_bench}%) "
                f"OPEX={fmt_m(to)} ({aop:.1f}% vs bench {opex_bench}%) GP Margin={agpm:.1f}% "
                f"Lines above benchmark={above} Highest cost segment={worst_seg}")
    ai_cfo_section(cost_ctx, "cost",
        "e.g. Where can we cut costs? Which SKU is least efficient? What's the priority action?")

    dl_cols = [c for c in [per_col, dim_col if dim_col != "— none —" else None,
               rev_col, cogs_col, opex_col, "_CP", "_OP", "_GPM", "_Flag"] if c]
    st.download_button("📥 Download Cost Report (CSV)",
                       df[[c for c in dl_cols if c in df.columns]].to_csv(index=False).encode(),
                       "Fincy_Cost_Intelligence.csv", "text/csv")


# ══════════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 5 — DATA ANALYSIS AGENT
# ══════════════════════════════════════════════════════════════════════════════
def run_dataanalyst():
    with st.sidebar:
        st.markdown("### 🤖 Data Analysis Agent")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="da_home"):
            for k in ["_da_df","_da_ready"]:
                st.session_state.pop(k, None)
            st.session_state.active_module = None
            st.rerun()
        if st.session_state.get("_da_ready"):
            if st.button("🔄 Load New Dataset", use_container_width=True, key="da_new"):
                for k in ["_da_df","_da_ready"]:
                    st.session_state.pop(k, None)
                st.rerun()
        st.markdown("---")
        st.caption("AI Agent · Groq Llama 3.1")

    page_header("DATA ANALYSIS AGENT", "Ask Anything")

    if not st.session_state.get("_da_ready"):
        st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #2dd4bf;
padding:12px 18px;margin-bottom:18px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;">
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#2dd4bf;margin-bottom:4px;">Step 1</div>
  <div style="font-size:0.74rem;color:#a09880;font-weight:300;">Upload any financial CSV — no template needed</div></div>
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#2dd4bf;margin-bottom:4px;">Step 2</div>
  <div style="font-size:0.74rem;color:#a09880;font-weight:300;">Agent auto-profiles your data instantly</div></div>
  <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#2dd4bf;margin-bottom:4px;">Step 3</div>
  <div style="font-size:0.74rem;color:#a09880;font-weight:300;">Ask anything — get executive summary</div></div>
</div>""", unsafe_allow_html=True)

        _, cc, _ = st.columns([1,2,1])
        with cc:
            da_file = st.file_uploader("Upload Any Financial CSV", type=["csv"], key="da_up")
            st.markdown('''<div style="text-align:center;margin:8px 0 5px;
font-family:'IBM Plex Mono',monospace;font-size:0.56rem;color:#3a3a34;">— or use FMCG sample —</div>''',
                        unsafe_allow_html=True)
            if st.button("📊 Use FMCG Sample", use_container_width=True, key="da_smpl"):
                st.session_state["_da_df"]    = pd.read_csv(io.StringIO(SAMPLE_FMCG))
                st.session_state["_da_ready"] = True
                st.rerun()
        if da_file:
            try:
                st.session_state["_da_df"]    = pd.read_csv(da_file)
                st.session_state["_da_ready"] = True
                st.rerun()
            except Exception as e:
                st.error(f"⚠️ {e}")
        return

    df = st.session_state["_da_df"]
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()
    missing  = int(df.isnull().sum().sum())
    dups     = int(df.duplicated().sum())

    st.markdown('<div class="sec-label">Automatic Data Profile</div>', unsafe_allow_html=True)
    _mc = "#f87171" if missing > 0 else "#4ade80"
    _dc2 = "#fbbf24" if dups > 0 else "#4ade80"
    st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px;">
  <div class="kpi-card" style="--ac:#2dd4bf"><div class="kpi-label">Rows</div>
    <div class="kpi-value">{len(df):,}</div></div>
  <div class="kpi-card" style="--ac:#818cf8"><div class="kpi-label">Columns</div>
    <div class="kpi-value">{len(df.columns)}</div></div>
  <div class="kpi-card" style="--ac:#c9a84c"><div class="kpi-label">Numeric Cols</div>
    <div class="kpi-value">{len(num_cols)}</div></div>
  <div class="kpi-card" style="--ac:{_mc}"><div class="kpi-label">Missing Values</div>
    <div class="kpi-value" style="color:{_mc};">{missing:,}</div>
    <div class="kpi-delta">{"⚠️ Nulls" if missing>0 else "✅ Complete"}</div></div>
  <div class="kpi-card" style="--ac:{_dc2}"><div class="kpi-label">Duplicate Rows</div>
    <div class="kpi-value" style="color:{_dc2};">{dups:,}</div>
    <div class="kpi-delta">{"⚠️ Found" if dups>0 else "✅ None"}</div></div>
</div>""", unsafe_allow_html=True)

    if num_cols:
        st.markdown('<div class="sec-label">Statistical Summary</div>', unsafe_allow_html=True)
        st.dataframe(df[num_cols].describe().round(2), use_container_width=True)

    if len(num_cols) >= 2:
        st.markdown('<div class="sec-label">Distribution Analysis</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        for i, col in enumerate(num_cols[:2]):
            with (c1 if i==0 else c2):
                fig = go.Figure(go.Histogram(x=df[col].dropna(), nbinsx=20,
                    marker_color="#2dd4bf", marker_line=dict(color="#0a0a08",width=0.5)))
                fig.update_layout(**PLOTLY_BASE, title=f"Distribution: {col}",
                                  height=240, xaxis=AXIS, yaxis=AXIS)
                st.plotly_chart(fig, use_container_width=True)

    if len(num_cols) >= 3:
        st.markdown('<div class="sec-label">Correlation Matrix</div>', unsafe_allow_html=True)
        corr = df[num_cols[:8]].corr().round(2)
        fig = go.Figure(go.Heatmap(
            z=corr.values, x=corr.columns.tolist(), y=corr.index.tolist(),
            colorscale=[[0,"#f87171"],[0.5,"#101010"],[1,"#4ade80"]],
            zmin=-1, zmax=1,
            text=corr.values.round(2), texttemplate="%{text}", textfont=dict(size=9)))
        fig.update_layout(**PLOTLY_BASE, title="Numeric Column Correlations", height=320)
        st.plotly_chart(fig, use_container_width=True)

    if cat_cols and num_cols:
        st.markdown('<div class="sec-label">Category Breakdown</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        for i, cat in enumerate(cat_cols[:2]):
            with (c1 if i==0 else c2):
                if df[cat].nunique() <= 20:
                    gb = df.groupby(cat)[num_cols[0]].sum().sort_values(ascending=False)
                    fig = go.Figure(go.Bar(x=gb.index.tolist(), y=gb.values.tolist(),
                        marker_color=PAL[:len(gb)],
                        text=[f"{v:,.0f}" for v in gb.values], textposition="auto"))
                    fig.update_layout(**PLOTLY_BASE,
                        title=f"{num_cols[0]} by {cat}", height=260, xaxis=AXIS, yaxis=AXIS)
                    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="sec-label">Data Preview (first 50 rows)</div>',
                unsafe_allow_html=True)
    st.dataframe(df.head(50), use_container_width=True, hide_index=True)
    st.download_button("📥 Download Data (CSV)", df.to_csv(index=False).encode(),
                       "Fincy_DataAnalysis.csv","text/csv")

    profile_str = (f"Dataset: {len(df)} rows x {len(df.columns)} cols | "
                   f"Numeric: {', '.join(num_cols[:5])} | "
                   f"Category: {', '.join(cat_cols[:4])} | "
                   f"Missing: {missing} | Dups: {dups}")
    if num_cols:
        profile_str += f" | Stats: {df[num_cols].describe().to_string()[:400]}"
    ai_cfo_section(profile_str, "dataanalyst",
        "e.g. What are the key trends? Which categories drive performance? Any anomalies?")




# ══════════════════════════════════════════════════════════════════════════════
# MODULE 6 — PERSONAL FINANCE DECISION ENGINE
# ══════════════════════════════════════════════════════════════════════════════

# ── Tax engine helpers (India-specific, FY 2024-25) ───────────────────────────

def _calc_old_tax(taxable_income):
    """Old regime slabs FY 2024-25."""
    if taxable_income <= 250000:  return 0
    tax = 0
    slabs = [(250000,500000,0.05),(500000,1000000,0.20),(1000000,float("inf"),0.30)]
    prev = 0
    for lo, hi, rate in [(0,250000,0),(250000,500000,0.05),(500000,1000000,0.20),(1000000,float("inf"),0.30)]:
        if taxable_income > lo:
            tax += min(taxable_income, hi) * rate - lo * rate
    # Rebate 87A: if income <=500000, no tax
    if taxable_income <= 500000: return 0
    # Surcharge & cess (simplified)
    return tax * 1.04  # 4% cess

def _calc_new_tax(income):
    """New regime slabs FY 2024-25 (Budget 2024)."""
    slabs = [
        (300000,  0.00),
        (600000,  0.05),
        (900000,  0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float("inf"), 0.30)
    ]
    # Standard deduction ₹75,000 under new regime
    taxable = max(0, income - 75000)
    if taxable <= 300000: return 0
    tax = 0
    prev_limit = 0
    limits = [300000,600000,900000,1200000,1500000]
    rates  = [0.00, 0.05, 0.10, 0.15, 0.20, 0.30]
    for i, rate in enumerate(rates):
        lo = limits[i-1] if i > 0 else 0
        hi = limits[i] if i < len(limits) else float("inf")
        if taxable <= lo: break
        taxable_in_slab = min(taxable, hi) - lo
        tax += taxable_in_slab * rate
    # Rebate 87A: if income <=700000, no tax under new regime
    if income <= 700000: return 0
    return tax * 1.04  # 4% cess

def _extract_amount(q):
    """Robust amount extraction: handles K, lakh, cr, ₹ symbols, plain numbers."""
    import re
    q_lower = q.lower()
    best = 0
    patterns = [
        (r"₹?\s*(\d+(?:\.\d+)?)\s*(?:lakh|l\b)",   lambda m: float(m.group(1)) * 100000),
        (r"₹?\s*(\d+(?:\.\d+)?)\s*(?:cr(?:ore)?\b)", lambda m: float(m.group(1)) * 10000000),
        (r"₹?\s*(\d+(?:\.\d+)?)\s*k\b",              lambda m: float(m.group(1)) * 1000),
        (r"₹\s*(\d+(?:,\d+)*)",                          lambda m: float(m.group(1).replace(",",""))),
        (r"\b(\d{4,})\b",                                lambda m: float(m.group(1))),
    ]
    for pat, fn in patterns:
        for m in re.finditer(pat, q_lower):
            try:
                v = fn(m)
                if v > best: best = v
            except: pass
    return best

def _spending_alert(income, expense):
    """Overspending detection."""
    if income <= 0: return None, None
    pct = expense / income * 100
    if pct >= 80:
        return "🚨 HIGH RISK", f"You are spending {pct:.1f}% of income. Overspending detected — immediate review needed."
    elif pct >= 60:
        return "⚠️ WARNING", f"You are spending {pct:.1f}% of income. Approaching the 80% danger threshold."
    else:
        return "✅ HEALTHY", f"Spending at {pct:.1f}% of income — within safe limits."

def _wealth_projection(monthly_surplus, current_savings, annual_return=0.08):
    """Simple wealth projection at 8% annual return."""
    import math
    results = {}
    for years in [1, 3, 5, 10]:
        months = years * 12
        r = annual_return / 12
        if r > 0:
            fv = current_savings * (1+r)**months + monthly_surplus * ((1+r)**months - 1) / r
        else:
            fv = current_savings + monthly_surplus * months
        results[years] = fv
    return results



# ── Confidence Engine (req §2) ────────────────────────────────────────────────
def _confidence_score(ud):
    """Dynamic confidence 50–95% based on data completeness."""
    s = 50
    if ud.get("income"):  s += 10
    if ud.get("expense"): s += 10
    if ud.get("savings"): s += 10
    if ud.get("goal"):    s += 10
    if ud.get("invest"):  s += 10
    return min(s, 95)

def _confidence_label(score):
    if score >= 80: return f"🟢 High ({score}%) — strong data foundation"
    if score >= 60: return f"🟡 Medium ({score}%) — add more data to improve accuracy"
    return             f"🔴 Low ({score}%) — limited data, treat as directional only"

# ── Assumptions constants (req §3) ────────────────────────────────────────────
AI_ASSUMPTIONS = {
    "Expected return": "8% annual (diversified equity)",
    "Inflation":       "5% (India CPI average)",
    "Income growth":   "Stable (no increment assumed)",
    "Tax rules":       "FY 2024-25 India (Budget 2024)",
}
AI_DISCLAIMER = (
    "This AI CFO recommendation is based on your inputs and standard assumptions. "
    "For major financial decisions, consult a professional advisor."
)




# ─────────────────────────────────────────────────────────────────────────────
# AI CFO ENGINE — Unified cross-module intelligence (Personal Finance brain)
# mode: "decision" | "tax" | "wealth" | "alert"
# Connects spending -> tax -> wealth in every response.
# ─────────────────────────────────────────────────────────────────────────────
def _call_ai_cfo_engine(mode, user_data, question="", extra_context=""):
    api_key = _get_groq_key()
    if not api_key:
        return ("AI CFO offline. Add GROQ_API_KEY to Streamlit Secrets.", "UNKNOWN")

    income   = user_data.get("income", 0)
    expense  = user_data.get("expense", 0)
    savings  = user_data.get("savings", 0)
    invest   = user_data.get("invest", 0)
    fixed    = user_data.get("fixed", 0)
    goal     = user_data.get("goal", "")
    m_inc    = income / 12 if income else 0
    surplus  = user_data.get("surplus", m_inc - expense)
    sav_rate = (surplus / m_inc * 100) if m_inc else 0
    spend_pct= (expense / m_inc * 100) if m_inc else 0
    gap80    = max(0, 150000 - invest)

    profile = (
        "ANNUAL INCOME: Rs" + "{:,}".format(int(income)) +
        " (Monthly: Rs" + "{:,.0f}".format(m_inc) + ")\n" +
        "MONTHLY EXPENSES: Rs" + "{:,}".format(int(expense)) +
        " (" + "{:.1f}".format(spend_pct) + "% of income)\n" +
        "MONTHLY SURPLUS: Rs" + "{:,.0f}".format(surplus) +
        " (" + "{:.1f}".format(sav_rate) + "% savings rate)\n" +
        "CURRENT SAVINGS: Rs" + "{:,}".format(int(savings)) + "\n" +
        "80C INVESTMENTS: Rs" + "{:,}".format(int(invest)) +
        " (gap: Rs" + "{:,}".format(int(gap80)) + ")\n" +
        "FIXED EXPENSES: Rs" + "{:,}".format(int(fixed)) + "/month\n" +
        "FINANCIAL GOAL: " + str(goal) + "\n" +
        "EXTRA CONTEXT: " + str(extra_context)
    )

    if mode == "decision":
        prompt = "\n".join([
            "You are an AI Personal CFO — senior financial advisor, tax expert, and wealth coach.",
            "Connect ALL dimensions: spending to tax to wealth in every answer.",
            "",
            "USER FINANCIAL PROFILE:",
            profile,
            "",
            "USER QUESTION: " + question,
            "",
            "Respond in this EXACT unified format:",
            "",
            "AI CFO Insight:",
            "[Direct yes/no answer with reasoning in 2 sentences using Rs numbers]",
            "",
            "Impact Summary:",
            "- Decision Impact: [exact Rs savings change]",
            "- Tax Impact: [80C opportunity or tax implication if any]",
            "- Wealth Impact: [effect on goal timeline with months or years]",
            "",
            "Recommendation:",
            "[One specific action with a Rs number and timeframe]",
            "",
            "Cross-Module Link:",
            "[How this decision connects spending to tax to long-term wealth in one sentence]",
            "",
            "Rules: Rs symbols on all numbers, reference profile data, no generic advice.",
        ])

    elif mode == "tax":
        prompt = "\n".join([
            "You are an AI tax strategist and wealth advisor with 20+ years in Indian finance.",
            "",
            "USER FINANCIAL PROFILE:",
            profile,
            "",
            "Analyse this user's tax situation and connect it to spending and wealth:",
            "",
            "AI CFO Tax Insight:",
            "[Which regime is better and the exact tax saving in Rs]",
            "",
            "Impact Summary:",
            "- Tax Saving Opportunity: [Rs amount if they optimise 80C and 80D]",
            "- Spending Link: [how current expenses affect tax position]",
            "- Wealth Link: [if they invest tax savings, 5yr compounding impact]",
            "",
            "Top 3 Tax Actions (ranked by Rs impact):",
            "1. [Action + exact Rs tax saved]",
            "2. [Action + exact Rs tax saved]",
            "3. [Action + exact Rs tax saved]",
            "",
            "Strategic Recommendation:",
            "[One sentence linking tax optimisation to their financial goal]",
            "",
            "Rules: use FY 2024-25 slabs, reference actual numbers from profile, be specific.",
        ])

    elif mode == "wealth":
        prompt = "\n".join([
            "You are an AI wealth coach and CFO advisor.",
            "Analyse savings rate, investment behaviour, and provide personalised wealth strategy.",
            "",
            "USER FINANCIAL PROFILE:",
            profile,
            "",
            "Provide a comprehensive wealth analysis:",
            "",
            "AI CFO Wealth Insight:",
            "[Savings rate assessment vs 20 percent benchmark with gap in Rs/month]",
            "",
            "Impact Summary:",
            "- Savings Rate: [current vs recommended, Rs gap per month]",
            "- Tax-Wealth Link: [if 80C gap of Rs" + "{:,}".format(int(gap80)) + " is invested, impact on wealth]",
            "- Goal Progress: [on track or behind, by how many months based on numbers]",
            "",
            "Wealth Building Actions:",
            "1. [SIP or investment recommendation with Rs amount and instrument]",
            "2. [Expense optimisation with Rs impact on savings rate]",
            "3. [Tax plus wealth combo action]",
            "",
            "30-Day Plan:",
            "[Specific steps this week and this month to improve financial health]",
            "",
            "Rules: compound growth numbers, realistic targets, link tax savings to investments.",
        ])

    elif mode == "alert":
        prompt = "\n".join([
            "You are an AI financial risk monitor for a personal finance platform.",
            "Analyse this user's financial profile and generate intelligent personalised alerts.",
            "",
            "USER FINANCIAL PROFILE:",
            profile,
            "",
            "Generate 2-3 smart financial alerts. For EACH alert:",
            "[Risk emoji] Alert Title - Risk: HIGH or MEDIUM or LOW",
            "[Alert message with specific Rs numbers]",
            "Action: [exact step to take with Rs target]",
            "",
            "Then conclude with:",
            "Overall Financial Health: STRONG or MODERATE or AT RISK - [one sentence why]",
            "",
            "Rules: reference actual numbers, link spending to tax to wealth,",
            "no generic advice, every alert must have a specific Rs action.",
        ])
    else:
        return ("Unknown AI CFO mode.", "UNKNOWN")

    # ── CFO reasoning footer appended to every prompt (req §1,2,3,5,12) ───────
    conf  = _confidence_score(user_data)
    c_lbl = _confidence_label(conf)
    reasoning_footer = (
        "\n\nCFO Reasoning (MUST include these sections in your response):\n"
        "- Income Analysis: [comment on income vs expenses ratio]\n"
        "- Expense Analysis: [spending % of income and risk signal]\n"
        "- Savings Impact: [exact Rs change to savings and emergency fund]\n"
        "- Tax Impact: [80C gap, best regime, tax saving opportunity]\n"
        "- Wealth Impact: [effect on long-term goal with timeline]\n\n"
        "Assumptions Used:\n"
        "- Expected return: 8% annual (diversified equity)\n"
        "- Inflation: 5% (India CPI average)\n"
        "- Income growth: stable (no increment assumed)\n"
        "- Tax rules: FY 2024-25 India (Budget 2024)\n\n"
        "Confidence Score: " + c_lbl + "\n\n"
        "Why this recommendation?\n"
        "[1-2 plain-English sentences: why this is right for this specific user]\n\n"
        "Disclaimer: This AI CFO recommendation is based on your inputs and "
        "standard assumptions. For major financial decisions, consult a professional advisor."
    )
    prompt = prompt + reasoning_footer
    try:
        from groq import Groq
        resp = Groq(api_key=api_key).chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.25
        )
        answer = resp.choices[0].message.content
        risk = "MEDIUM"
        if mode == "alert":
            au = answer.upper()
            if "RISK: HIGH" in au or "AT RISK" in au:  risk = "HIGH"
            elif "RISK: LOW" in au or "STRONG" in au:  risk = "LOW"
        return answer, risk
    except Exception as e:
        return ("AI CFO Engine error: " + str(e)), "UNKNOWN"


def run_personal():
    with st.sidebar:
        st.markdown("### 💰 Personal Finance")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="pf_home"):
            for k in ["_pf_income","_pf_expense","_pf_savings","_pf_fixed",
                      "_pf_goal","_pf_setup","_pf_invest","_pf_regime"]:
                st.session_state.pop(k, None)
            st.session_state.active_module = None
            st.rerun()
        st.markdown("---")
        st.caption("AI Personal CFO · Tax Advisor · Wealth Coach")

    page_header("PERSONAL FINANCE DECISION ENGINE", "CFO · Tax Advisor · Wealth Coach")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #a78bfa;
padding:12px 18px;margin-bottom:18px;font-size:0.76rem;color:#a09880;font-weight:300;">
<span style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
text-transform:uppercase;color:#a78bfa;">Your Personal AI CFO: </span>
Ask financial questions · Compare tax regimes · Get overspending alerts · Project wealth.
Supports <strong style="color:#e8e2d4;">K (thousands), lakh, crore</strong> — e.g. "Can I buy a 60K phone?" or "Invest 1.5 lakh?"
</div>""", unsafe_allow_html=True)

    # ── Step 1: Financial Profile ─────────────────────────────────────────────
    if not st.session_state.get("_pf_setup"):
        st.markdown('<div class="sec-label">Step 1 — Your Financial Profile</div>',
                    unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            income  = st.number_input("💵 Annual Income (₹)", min_value=0,
                                      value=960000, step=10000, key="pf_inc",
                                      help="Annual gross income e.g. 9,60,000 = ₹80K/month")
            expense = st.number_input("💸 Monthly Expenses (₹)", min_value=0,
                                      value=50000, step=1000, key="pf_exp")
            savings = st.number_input("🏦 Current Savings (₹)", min_value=0,
                                      value=30000, step=1000, key="pf_sav")
        with c2:
            invest  = st.number_input("📈 Annual Investments for 80C (₹)", min_value=0,
                                      value=50000, step=5000, key="pf_inv",
                                      help="PF, ELSS, LIC, PPF etc. (max ₹1,50,000 for deduction)")
            fixed   = st.number_input("🔒 Fixed Monthly Expenses (₹)", min_value=0,
                                      value=30000, step=1000, key="pf_fix",
                                      help="EMI, rent, insurance — cannot reduce")
            goal    = st.text_input("🎯 Financial Goal",
                                    value="Save ₹5L in 12 months", key="pf_goal_inp")
            regime  = st.radio("Preferred Tax Regime", ["Compare Both","Old Regime","New Regime"],
                               key="pf_regime_inp", horizontal=True)

        if st.button("✅ Set My Financial Profile", use_container_width=True, key="pf_confirm"):
            if income <= 0:
                st.error("Please enter your annual income.")
            else:
                monthly_inc = income / 12
                st.session_state.update({
                    "_pf_income":  income,       # annual
                    "_pf_expense": expense,      # monthly
                    "_pf_savings": savings,
                    "_pf_fixed":   fixed,
                    "_pf_goal":    goal,
                    "_pf_invest":  invest,
                    "_pf_regime":  regime,
                    "_pf_setup":   True,
                })
                st.rerun()
        return

    # ── Load profile ──────────────────────────────────────────────────────────
    income   = st.session_state["_pf_income"]     # annual
    expense  = st.session_state["_pf_expense"]    # monthly
    savings  = st.session_state["_pf_savings"]
    fixed    = st.session_state["_pf_fixed"]
    goal     = st.session_state["_pf_goal"]
    invest   = st.session_state.get("_pf_invest", 0)
    regime   = st.session_state.get("_pf_regime", "Compare Both")
    m_income = income / 12
    surplus  = m_income - expense

    # ── TAB LAYOUT ────────────────────────────────────────────────────────────
    tabs = st.tabs(["💬 Decision Engine", "🧾 Tax Advisor", "📈 Wealth Coach", "⚠️ Alerts"])

    # ════════════════════════════════════════════════════════════════
    # TAB 1 — DECISION ENGINE
    # ════════════════════════════════════════════════════════════════
    with tabs[0]:
        st.markdown('<div class="sec-label">Your Financial Profile</div>',
                    unsafe_allow_html=True)
        _sur_col = "#4ade80" if surplus > 0 else "#f87171"
        _sr_pct  = savings / m_income * 100 if m_income else 0
        st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:14px;">
  <div class="kpi-card" style="--ac:#a78bfa">
    <div class="kpi-label">Monthly Income</div>
    <div class="kpi-value">₹{m_income:,.0f}</div>
    <div class="kpi-delta">₹{income:,.0f}/yr</div>
  </div>
  <div class="kpi-card" style="--ac:#f87171">
    <div class="kpi-label">Monthly Expenses</div>
    <div class="kpi-value">₹{expense:,}</div>
    <div class="kpi-delta">{expense/m_income*100:.1f}% of income</div>
  </div>
  <div class="kpi-card" style="--ac:{_sur_col}">
    <div class="kpi-label">Monthly Surplus</div>
    <div class="kpi-value" style="color:{_sur_col};">₹{surplus:,.0f}</div>
    <div class="kpi-delta">{surplus/m_income*100:.1f}% of income</div>
  </div>
  <div class="kpi-card" style="--ac:#c9a84c">
    <div class="kpi-label">Current Savings</div>
    <div class="kpi-value">₹{savings:,}</div>
  </div>
  <div class="kpi-card" style="--ac:#4ade80">
    <div class="kpi-label">Savings Ratio</div>
    <div class="kpi-value">{_sr_pct:.1f}%</div>
    <div class="kpi-delta">of monthly income</div>
  </div>
</div>""", unsafe_allow_html=True)

        if st.button("✏️ Edit Profile", key="pf_edit"):
            st.session_state["_pf_setup"] = False
            st.rerun()

        st.markdown('<div class="sec-label">Ask Your Financial Question</div>',
                    unsafe_allow_html=True)

        # Quick presets
        qc1,qc2,qc3,qc4 = st.columns(4)
        preset_q = None
        with qc1:
            if st.button("📱 Buy Gadget",    use_container_width=True, key="pf_q1"):
                preset_q = "Can I afford a ₹20,000 phone this month?"
        with qc2:
            if st.button("✈️ Travel",         use_container_width=True, key="pf_q2"):
                preset_q = "Should I go on a ₹15,000 weekend trip?"
        with qc3:
            if st.button("📈 Invest",         use_container_width=True, key="pf_q3"):
                preset_q = "Can I invest ₹10,000 in mutual funds this month?"
        with qc4:
            if st.button("🛒 Big Purchase",   use_container_width=True, key="pf_q4"):
                preset_q = "Can I buy a ₹50,000 laptop right now?"
        if preset_q:
            st.session_state["_pf_preset"] = preset_q

        default_q = st.session_state.get("_pf_preset", "")
        user_q = st.text_input(
            "Ask:", value=default_q,
            placeholder="e.g. Can I afford a 60K phone? Should I invest 1.5 lakh?",
            key="pf_question", label_visibility="collapsed")

        if st.button("🔍 Analyze", use_container_width=True, key="pf_analyze"):
            if not user_q.strip():
                st.warning("Please enter a question.")
                st.stop()

            # ── Fixed robust amount extraction ───────────────────────────
            amount = _extract_amount(user_q)

            # ── Decision logic ───────────────────────────────────────────
            if savings > 0 and amount > 0:
                pct_sav = amount / savings * 100
                if amount <= savings * 0.30:
                    decision, dcol, dbg = "SAFE ✅",     "#4ade80", "rgba(74,222,128,0.08)"
                elif amount <= savings * 0.60:
                    decision, dcol, dbg = "MODERATE ⚠️", "#fbbf24", "rgba(251,191,36,0.08)"
                else:
                    decision, dcol, dbg = "RISKY ❌",    "#f87171", "rgba(248,113,113,0.08)"
            elif amount == 0:
                decision, dcol, dbg = "ADVISORY 💡", "#a78bfa", "rgba(167,139,250,0.08)"
                pct_sav = 0
            else:
                decision, dcol, dbg = "RISKY ❌",    "#f87171", "rgba(248,113,113,0.08)"
                pct_sav = 100

            remaining = max(0, savings - amount)
            months_needed = (amount / surplus) if surplus > 0 else float("inf")

            # ── Decision card ─────────────────────────────────────────────
            months_line = (f'<div style="margin-top:10px;font-size:0.74rem;color:#5a5648;">'
                           f'Months of surplus to cover: <strong style="color:#e8e2d4;">{months_needed:.1f}</strong></div>'
                           if amount > 0 and surplus > 0 else "")
            st.markdown(f"""
<div style="background:{dbg};border:2px solid {dcol};padding:20px 24px;margin:14px 0;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.16em;
  text-transform:uppercase;color:#5a5648;margin-bottom:8px;">Financial Decision</div>
  <div style="font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:900;
  color:{dcol};margin-bottom:10px;">{decision}</div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
    <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;text-transform:uppercase;
    color:#5a5648;margin-bottom:3px;">Amount Detected</div>
    <div style="font-size:1rem;font-weight:600;color:#e8e2d4;">
    {"₹{:,.0f}".format(amount) if amount > 0 else "N/A — Advisory question"}</div></div>
    <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;text-transform:uppercase;
    color:#5a5648;margin-bottom:3px;">Savings Impact</div>
    <div style="font-size:1rem;font-weight:600;color:{dcol};">
    {"{:.1f}%".format(pct_sav) if amount > 0 else "—"}</div></div>
    <div><div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;text-transform:uppercase;
    color:#5a5648;margin-bottom:3px;">Savings After</div>
    <div style="font-size:1rem;font-weight:600;color:#e8e2d4;">₹{remaining:,.0f}</div></div>
  </div>
  {months_line}
</div>""", unsafe_allow_html=True)

            # ── AI CFO Engine — unified decision+tax+wealth response ─────────
            _ud = {"income":income,"expense":expense,"savings":savings,
                   "invest":invest,"fixed":fixed,"goal":goal,"surplus":surplus}
            old_t = _calc_old_tax(max(0, income - 150000 - invest))
            new_t = _calc_new_tax(income)
            wp    = _wealth_projection(max(0,surplus), savings)
            _xctx = (
                "Decision=" + decision +
                " | Amount=Rs" + "{:,.0f}".format(amount) +
                " | Savings impact=" + "{:.1f}".format(pct_sav) + "%" +
                " | Old tax=Rs" + "{:,.0f}".format(old_t) +
                " | New tax=Rs" + "{:,.0f}".format(new_t) +
                " | 3yr wealth=Rs" + "{:,.0f}".format(wp[3])
            )
            with st.spinner("AI CFO Engine analysing…"):
                ai_ans, _ = _call_ai_cfo_engine(
                    "decision", _ud,
                    question=user_q.strip(),
                    extra_context=_xctx
                )
            st.markdown(f'''<div class="ai-box" style="line-height:1.85;">{ai_ans}</div>''',
                        unsafe_allow_html=True)

            # ── "Why this?" expandable reasoning (req §5) ───────────────────
            _conf = _confidence_score(_ud)
            with st.expander("👉 Why this recommendation? — View full reasoning & assumptions"):
                st.markdown(f"""
<div style="font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.12em;
text-transform:uppercase;color:#c9a84c;margin-bottom:10px;">Confidence Score</div>
<div style="font-size:0.82rem;color:#a09880;margin-bottom:14px;">{_confidence_label(_conf)}</div>
<div style="font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.12em;
text-transform:uppercase;color:#c9a84c;margin-bottom:10px;">Assumptions Used</div>
<div style="font-size:0.78rem;color:#a09880;line-height:1.9;">
• Expected return: 8% annual (diversified equity)<br>
• Inflation: 5% (India CPI average)<br>
• Income growth: stable (no increment assumed)<br>
• Tax rules: FY 2024-25 India (Budget 2024)
</div>
<div style="margin-top:14px;font-size:0.74rem;color:#5a5648;border-top:1px solid #1e1e18;
padding-top:10px;">⚠️ This AI CFO recommendation is based on your inputs and standard assumptions.
For major financial decisions, consult a professional advisor.</div>
""", unsafe_allow_html=True)

            try:
                _pdf_text = (f"FINCY — PERSONAL FINANCE DECISION REPORT\n{'='*50}\n\n"
                             f"Question: {user_q}\nDecision: {decision}\n"
                             f"Amount: Rs{amount:,.0f} | Savings Impact: {pct_sav:.1f}%\n"
                             f"Remaining Savings: Rs{remaining:,.0f}\n\n"
                             f"AI CFO Analysis:\n{ai_ans}\n\n"
                             f"Profile: Income=Rs{income:,}/yr | Expenses=Rs{expense:,}/mo | "
                             f"Savings=Rs{savings:,} | Goal={goal}")
                st.download_button("📄 Download Finance Report (PDF)",
                                   data=generate_pdf(_pdf_text),
                                   file_name="Fincy_Personal_Finance_Report.pdf",
                                   mime="application/pdf", key="pf_pdf")
            except Exception:
                pass

            st.session_state.pop("_pf_preset", None)

    # ════════════════════════════════════════════════════════════════
    # TAB 2 — TAX ADVISOR
    # ════════════════════════════════════════════════════════════════
    with tabs[1]:
        st.markdown('<div class="sec-label">India Tax Calculator — FY 2024-25</div>',
                    unsafe_allow_html=True)

        t1, t2, t3 = st.columns(3)
        with t1:
            tax_income = st.number_input("Annual Income (₹)", min_value=0,
                                         value=income, step=10000, key="tax_inc")
        with t2:
            sec80c  = st.number_input("Section 80C Investments (₹)", min_value=0,
                                      value=min(invest, 150000), max_value=150000,
                                      step=5000, key="tax_80c",
                                      help="PF, ELSS, LIC, PPF, NSC — max ₹1,50,000")
        with t3:
            sec80d  = st.number_input("Section 80D — Health Insurance (₹)", min_value=0,
                                      value=25000, max_value=100000,
                                      step=5000, key="tax_80d",
                                      help="Self+Family up to ₹25,000; parents up to ₹50,000")

        hra_exempt = st.number_input("HRA Exemption (₹, if applicable)", min_value=0,
                                      value=0, step=5000, key="tax_hra",
                                      help="Actual HRA received minus 10% of basic salary")

        # Calculate
        total_deductions_old = min(sec80c, 150000) + sec80d + hra_exempt + 50000  # +50K std deduction
        taxable_old = max(0, tax_income - total_deductions_old)
        old_tax     = _calc_old_tax(taxable_old)
        new_tax     = _calc_new_tax(tax_income)
        saving_diff = abs(old_tax - new_tax)
        better_reg  = "Old Regime" if old_tax < new_tax else "New Regime"
        better_col  = "#4ade80"
        worse_col   = "#f87171"

        st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0;">
  <div class="kpi-card" style="--ac:#c9a84c">
    <div class="kpi-label">Old Regime Tax</div>
    <div class="kpi-value" style="color:{'#4ade80' if old_tax < new_tax else '#f87171'};">
      ₹{old_tax:,.0f}</div>
    <div class="kpi-delta">Deductions: ₹{total_deductions_old:,.0f}</div>
  </div>
  <div class="kpi-card" style="--ac:#818cf8">
    <div class="kpi-label">New Regime Tax</div>
    <div class="kpi-value" style="color:{'#4ade80' if new_tax < old_tax else '#f87171'};">
      ₹{new_tax:,.0f}</div>
    <div class="kpi-delta">Std deduction: ₹75,000</div>
  </div>
  <div class="kpi-card" style="--ac:#4ade80">
    <div class="kpi-label">Better Regime</div>
    <div class="kpi-value" style="color:#4ade80;">{better_reg}</div>
    <div class="kpi-delta">Saves ₹{saving_diff:,.0f}</div>
  </div>
</div>""", unsafe_allow_html=True)

        # Visual comparison bar
        max_tax = max(old_tax, new_tax, 1)
        old_pct = old_tax / max_tax * 100
        new_pct = new_tax / max_tax * 100
        st.markdown(f"""
<div style="background:#101010;border:1px solid #1e1e18;padding:16px;margin-bottom:16px;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.12em;
  text-transform:uppercase;color:#5a5648;margin-bottom:12px;">Tax Comparison Visual</div>
  <div style="margin-bottom:10px;">
    <div style="font-size:0.74rem;color:#a09880;margin-bottom:4px;">Old Regime — ₹{old_tax:,.0f}</div>
    <div style="background:#1e1e18;height:22px;border-radius:0;position:relative;">
      <div style="background:{'#4ade80' if old_tax<new_tax else '#f87171'};width:{old_pct:.1f}%;
      height:100%;display:flex;align-items:center;padding-left:8px;">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;
        color:#0a0a08;font-weight:700;">{old_pct:.0f}%</span>
      </div>
    </div>
  </div>
  <div>
    <div style="font-size:0.74rem;color:#a09880;margin-bottom:4px;">New Regime — ₹{new_tax:,.0f}</div>
    <div style="background:#1e1e18;height:22px;border-radius:0;position:relative;">
      <div style="background:{'#4ade80' if new_tax<old_tax else '#f87171'};width:{new_pct:.1f}%;
      height:100%;display:flex;align-items:center;padding-left:8px;">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;
        color:#0a0a08;font-weight:700;">{new_pct:.0f}%</span>
      </div>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

        # Tax Saving Recommendations
        st.markdown('<div class="sec-label">💡 Smart Tax Saving Recommendations</div>',
                    unsafe_allow_html=True)
        recs = []
        gap_80c = 150000 - min(sec80c, 150000)
        if gap_80c > 0:
            tax_save = gap_80c * 0.20  # approx 20% bracket
            recs.append(f"📌 Invest ₹{gap_80c:,.0f} more in 80C (ELSS/PPF) → save ₹{tax_save:,.0f} tax")
        if sec80d < 25000:
            recs.append(f"📌 Get health insurance — 80D deduction of ₹{25000-sec80d:,.0f} more possible")
        if old_tax > new_tax and sec80c < 100000:
            recs.append("📌 Old Regime is better for you — maximise 80C to widen the savings gap")
        if new_tax < old_tax and tax_income > 1500000:
            recs.append("📌 New Regime saves you tax — fewer deductions to track, simpler filing")
        if not recs:
            recs.append("✅ You are already in the optimal tax position for your income level")
        recs.append(f"📌 Monthly tax provision: ₹{min(old_tax,new_tax)/12:,.0f} (set aside from salary)")

        for r in recs:
            st.markdown(f"""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #c9a84c;
padding:10px 14px;margin-bottom:8px;font-size:0.78rem;color:#a09880;">{r}</div>""",
                        unsafe_allow_html=True)

        # ── AI CFO Engine: Tax + Wealth + Spending cross-module analysis ────────
        st.markdown('<div class="sec-label">🧠 AI CFO Tax Intelligence</div>',
                    unsafe_allow_html=True)
        with st.spinner("AI CFO analysing your tax situation…"):
            _ud_tax = {"income":tax_income,"expense":expense,"savings":savings,
                       "invest":sec80c,"fixed":fixed,"goal":goal,"surplus":surplus}
            _xctx_tax = (
                "Old regime tax=Rs" + "{:,.0f}".format(int(old_tax)) +
                " | New regime tax=Rs" + "{:,.0f}".format(int(new_tax)) +
                " | Better=" + better_reg +
                " | Saving=Rs" + "{:,.0f}".format(int(saving_diff)) +
                " | 80C invested=Rs" + "{:,}".format(int(sec80c)) +
                " | 80D=Rs" + "{:,}".format(int(sec80d))
            )
            tax_ai_ans, _ = _call_ai_cfo_engine(
                "tax", _ud_tax, extra_context=_xctx_tax
            )
        st.markdown(f'''<div class="ai-box" style="line-height:1.85;">{tax_ai_ans}</div>''',
                    unsafe_allow_html=True)

        # ── ITR Filing Integration (req §6) ─────────────────────────────────────
        st.markdown('<div class="sec-label">🧾 Ready to File Your ITR?</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
<div style="background:#0a0d10;border:1px solid #06b6d4;border-left:4px solid #06b6d4;
padding:16px 20px;margin-bottom:14px;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.54rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#06b6d4;margin-bottom:8px;">File on the Official Portal</div>
  <div style="font-size:0.78rem;color:#a09880;line-height:1.7;font-weight:300;">
    Based on our analysis, you save <strong style="color:#4ade80;">₹{saving_diff:,.0f}</strong>
    by choosing the <strong style="color:#e8e2d4;">{better_reg}</strong>.
    File your ITR now on the Government's official e-filing portal.
  </div>
  <div style="margin-top:10px;font-size:0.68rem;color:#5a5648;">
    ⚠️ Fincy provides analysis only. Filing must be completed on the official Income Tax portal.
    Consult a CA for complex tax situations.
  </div>
</div>""", unsafe_allow_html=True)
        st.link_button(
            "🚀 File ITR on Official Portal →",
            "https://www.incometax.gov.in/iec/foportal/",
        )
        st.caption("Fincy provides tax analysis. Filing is done exclusively on the official Income Tax portal.")

        # Tax PDF
        try:
            tax_report = (f"FINCY — TAX COMPARISON REPORT FY 2024-25\n{'='*50}\n\n"
                          f"Annual Income: ₹{tax_income:,}\n"
                          f"80C Investments: ₹{sec80c:,} | 80D: ₹{sec80d:,}\n\n"
                          f"Old Regime Tax: ₹{old_tax:,.0f} (Taxable: ₹{taxable_old:,.0f})\n"
                          f"New Regime Tax: ₹{new_tax:,.0f}\n"
                          f"Better Regime: {better_reg} — saves ₹{saving_diff:,.0f}\n\n"
                          f"Recommendations:\n" + "\n".join(recs))
            st.download_button("📄 Download Tax Report (PDF)",
                               data=generate_pdf(tax_report),
                               file_name="Fincy_Tax_Report.pdf",
                               mime="application/pdf", key="tax_pdf")
        except Exception:
            pass

    # ════════════════════════════════════════════════════════════════
    # TAB 3 — WEALTH COACH
    # ════════════════════════════════════════════════════════════════
    with tabs[2]:
        st.markdown('<div class="sec-label">Wealth Building Dashboard</div>',
                    unsafe_allow_html=True)

        sav_rate = (surplus / m_income * 100) if m_income > 0 else 0
        proj     = _wealth_projection(max(0, surplus), savings)

        # Savings rate gauge
        sr_col = "#4ade80" if sav_rate >= 20 else ("#fbbf24" if sav_rate >= 10 else "#f87171")
        sr_msg = ("✅ Excellent — on track for wealth building" if sav_rate >= 20 else
                  "⚠️ Moderate — aim for 20%+" if sav_rate >= 10 else
                  "❌ Low — prioritise cutting expenses")

        st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:16px;">
  <div class="kpi-card" style="--ac:{sr_col}">
    <div class="kpi-label">Savings Rate</div>
    <div class="kpi-value" style="color:{sr_col};">{sav_rate:.1f}%</div>
    <div class="kpi-delta">{sr_msg[:20]}</div>
  </div>
  <div class="kpi-card" style="--ac:#c9a84c">
    <div class="kpi-label">Monthly Surplus</div>
    <div class="kpi-value">₹{surplus:,.0f}</div>
    <div class="kpi-delta">investable each month</div>
  </div>
  <div class="kpi-card" style="--ac:#818cf8">
    <div class="kpi-label">In 3 Years</div>
    <div class="kpi-value">₹{proj[3]/100000:.1f}L</div>
    <div class="kpi-delta">at 8% annual return</div>
  </div>
  <div class="kpi-card" style="--ac:#4ade80">
    <div class="kpi-label">In 10 Years</div>
    <div class="kpi-value">₹{proj[10]/100000:.1f}L</div>
    <div class="kpi-delta">at 8% annual return</div>
  </div>
</div>""", unsafe_allow_html=True)

        # Wealth projection chart
        years_list  = [1, 3, 5, 10]
        wealth_vals = [proj[y] for y in years_list]
        fig = go.Figure(go.Bar(
            x=[f"{y}yr" for y in years_list],
            y=wealth_vals,
            marker_color=["#a78bfa","#818cf8","#c9a84c","#4ade80"],
            text=[f"₹{v/100000:.1f}L" for v in wealth_vals],
            textposition="auto"))
        fig.update_layout(**PLOTLY_BASE, title="Wealth Projection at 8% Returns",
                          height=260, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)

        # Wealth insights
        st.markdown('<div class="sec-label">Wealth Building Insights</div>',
                    unsafe_allow_html=True)
        w_insights = [
            f"📊 Current savings rate: {sav_rate:.1f}% — {'above' if sav_rate>=20 else 'below'} the 20% wealth-building threshold",
            f"📈 At ₹{surplus:,.0f}/month surplus, you accumulate ₹{proj[3]/100000:.1f}L in 3 years at 8% returns",
            f"🎯 Goal: {goal}",
        ]
        if sav_rate < 20:
            shortfall = (0.20 - sav_rate/100) * m_income
            w_insights.append(f"💡 Increase monthly savings by ₹{shortfall:,.0f} to reach 20% savings rate")
        if surplus > 5000:
            sip_5yr = _wealth_projection(surplus*0.5, 0)[5]
            w_insights.append(f"💡 Invest 50% of surplus (₹{surplus*0.5:,.0f}) in SIP → ₹{sip_5yr/100000:.1f}L in 5 years")

        for ins in w_insights:
            st.markdown(f"""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #a78bfa;
padding:10px 14px;margin-bottom:8px;font-size:0.78rem;color:#a09880;">{ins}</div>""",
                        unsafe_allow_html=True)

        # ── AI CFO Engine: Wealth + Tax + Spending unified strategy ─────────
        st.markdown('<div class="sec-label">🧠 AI CFO Wealth Strategy</div>',
                    unsafe_allow_html=True)
        with st.spinner("AI CFO building your wealth strategy…"):
            _ud_w = {"income":income,"expense":expense,"savings":savings,
                     "invest":invest,"fixed":fixed,"goal":goal,"surplus":surplus}
            _xctx_w = (
                "Savings rate=" + "{:.1f}".format(sav_rate) + "%" +
                " | 1yr projection=Rs" + "{:,.0f}".format(proj[1]) +
                " | 5yr projection=Rs" + "{:,.0f}".format(proj[5]) +
                " | 10yr projection=Rs" + "{:,.0f}".format(proj[10])
            )
            wealth_ai_ans, _ = _call_ai_cfo_engine(
                "wealth", _ud_w, extra_context=_xctx_w
            )
        st.markdown(f'''<div class="ai-box" style="line-height:1.85;">{wealth_ai_ans}</div>''',
                    unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 4 — ALERTS
    # ════════════════════════════════════════════════════════════════
    with tabs[3]:
        st.markdown('<div class="sec-label">Financial Health Alerts</div>',
                    unsafe_allow_html=True)

        alert_level, alert_msg = _spending_alert(m_income, expense)
        alert_col = {"🚨 HIGH RISK":"#f87171","⚠️ WARNING":"#fbbf24","✅ HEALTHY":"#4ade80"}.get(
            alert_level, "#5a5648")

        st.markdown(f"""
<div style="background:rgba(0,0,0,0.3);border:2px solid {alert_col};
padding:18px 22px;margin-bottom:16px;">
  <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;
  color:{alert_col};margin-bottom:8px;">{alert_level}</div>
  <div style="font-size:0.82rem;color:#a09880;line-height:1.7;">{alert_msg}</div>
</div>""", unsafe_allow_html=True)

        alerts = []
        spend_pct = expense/m_income*100 if m_income else 0
        if spend_pct >= 80:
            alerts.append(("🚨","HIGH","Spending ≥80% of income — emergency budget review required"))
        elif spend_pct >= 60:
            alerts.append(("⚠️","WARN",f"Spending at {spend_pct:.1f}% — reduce discretionary by ₹{expense*0.1:,.0f}"))
        if surplus < 5000 and surplus >= 0:
            alerts.append(("⚠️","WARN",f"Very low surplus (₹{surplus:,.0f}) — emergency fund at risk"))
        if surplus < 0:
            alerts.append(("🚨","HIGH",f"Negative surplus! Expenses exceed income by ₹{abs(surplus):,.0f}/month"))
        if savings < m_income * 3:
            alerts.append(("⚠️","WARN",f"Emergency fund low — target 3-6 months income = ₹{m_income*3:,.0f}"))
        if invest < 50000 and income > 500000:
            alerts.append(("💡","INFO",f"Only ₹{invest:,} in 80C investments — you can save more tax"))
        if not any(a[1]=="HIGH" for a in alerts):
            alerts.append(("✅","OK","No critical financial risks detected in your profile"))

        for icon, level, msg in alerts:
            _ac = {"HIGH":"#f87171","WARN":"#fbbf24","INFO":"#818cf8","OK":"#4ade80"}.get(level,"#5a5648")
            st.markdown(f"""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid {_ac};
padding:10px 14px;margin-bottom:8px;font-size:0.78rem;color:#a09880;">
{icon} {msg}</div>""", unsafe_allow_html=True)

        # ── AI CFO Engine: Groq-powered smart alerts ─────────────────────────
        st.markdown('<div class="sec-label">🧠 AI CFO Smart Alerts</div>',
                    unsafe_allow_html=True)
        with st.spinner("AI CFO monitoring your finances…"):
            _ud_al = {"income":income,"expense":expense,"savings":savings,
                      "invest":invest,"fixed":fixed,"goal":goal,"surplus":surplus}
            _xctx_al = (
                "Spending pct=" + "{:.1f}".format(spend_pct) + "%" +
                " | Static alerts=" + str(len(alerts)) +
                " | High risk count=" + str(sum(1 for a in alerts if a[1]=="HIGH")) +
                " | Emergency fund ratio=" + "{:.1f}".format(savings/max(m_income,1))
            )
            alert_ai_ans, ai_risk = _call_ai_cfo_engine(
                "alert", _ud_al, extra_context=_xctx_al
            )
        _alert_border = {"HIGH":"#f87171","MEDIUM":"#fbbf24","LOW":"#4ade80"}.get(ai_risk,"#5a5648")
        st.markdown(f'''<div class="ai-box" style="line-height:1.85;border-left:3px solid {_alert_border};">{alert_ai_ans}</div>''',
                    unsafe_allow_html=True)

        # Summary health score
        risk_count = sum(1 for a in alerts if a[1]=="HIGH")
        warn_count = sum(1 for a in alerts if a[1]=="WARN")
        health_score = max(0, 100 - risk_count*30 - warn_count*10)
        hs_col = "#4ade80" if health_score>=70 else ("#fbbf24" if health_score>=50 else "#f87171")
        st.markdown(f"""
<div style="margin-top:16px;background:#101010;border:1px solid #1e1e18;padding:16px;
text-align:center;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#5a5648;margin-bottom:6px;">Financial Health Score</div>
  <div style="font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:900;
  color:{hs_col};">{health_score}/100</div>
  <div style="font-size:0.74rem;color:#5a5648;margin-top:4px;">
  {"Excellent" if health_score>=80 else "Good" if health_score>=60 else "Needs Attention" if health_score>=40 else "Critical"}</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 7 — CASH FLOW INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
SAMPLE_CASHFLOW = """Month,Opening_Balance,Operating_Inflows,Operating_Outflows,Investing_Inflows,Investing_Outflows,Financing_Inflows,Financing_Outflows
Jan-2024,500000,850000,620000,0,45000,0,80000
Feb-2024,605000,920000,680000,0,0,0,80000
Mar-2024,765000,1050000,710000,15000,0,200000,80000
Apr-2024,1160000,880000,650000,0,120000,0,80000
May-2024,1190000,960000,700000,0,0,0,80000
Jun-2024,1370000,1100000,760000,0,55000,0,80000
Jul-2024,1575000,820000,640000,0,0,0,80000
Aug-2024,1675000,900000,680000,25000,0,0,80000
Sep-2024,1840000,1080000,730000,0,90000,0,80000
Oct-2024,2020000,950000,700000,0,0,0,80000
Nov-2024,2190000,1020000,750000,0,0,100000,80000
Dec-2024,2480000,1200000,820000,0,200000,0,80000"""


def run_cashflow():
    with st.sidebar:
        st.markdown("### 💧 Cash Flow Intelligence")
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True, key="cf_home"):
            for k in ["_cf_df","_cf_ready"]:
                st.session_state.pop(k, None)
            st.session_state.active_module = None
            st.rerun()
        if st.session_state.get("_cf_ready"):
            if st.button("🔄 Load New Data", use_container_width=True, key="cf_new"):
                for k in ["_cf_df","_cf_ready"]:
                    st.session_state.pop(k, None)
                st.rerun()
        st.markdown("---")
        st.caption("Cash Flow · Liquidity · Burn Rate")

    page_header("CASH FLOW INTELLIGENCE", "Liquidity & Forecasting")

    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #06b6d4;
padding:12px 18px;margin-bottom:18px;font-size:0.76rem;color:#a09880;font-weight:300;">
<span style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.14em;
text-transform:uppercase;color:#06b6d4;">How it works: </span>
Upload a monthly cash flow CSV with Opening Balance, Operating, Investing, and Financing
inflows/outflows. Get instant liquidity health, burn rate, runway analysis, and AI CFO
insights on where your cash is going and how to protect it.
<strong style="color:#e8e2d4;"> Columns needed:</strong>
Month · Opening_Balance · Operating_Inflows · Operating_Outflows ·
Investing/Financing columns (optional).
</div>""", unsafe_allow_html=True)

    # ── Upload ─────────────────────────────────────────────────────────────────
    if not st.session_state.get("_cf_ready"):
        _, cc, _ = st.columns([1, 2, 1])
        with cc:
            cf_file = st.file_uploader("Upload Cash Flow CSV", type=["csv"], key="cf_upload")
            st.markdown('''<div style="text-align:center;margin:8px 0 4px;
font-family:'IBM Plex Mono',monospace;font-size:0.56rem;color:#3a3a34;">— or use sample —</div>''',
                        unsafe_allow_html=True)
            if st.button("💧 Use Sample Cash Flow Data",
                         use_container_width=True, key="cf_sample"):
                st.session_state["_cf_df"]    = pd.read_csv(io.StringIO(SAMPLE_CASHFLOW))
                st.session_state["_cf_ready"] = True
                st.rerun()
        if cf_file:
            try:
                st.session_state["_cf_df"]    = pd.read_csv(cf_file)
                st.session_state["_cf_ready"] = True
                st.rerun()
            except Exception as e:
                st.error(f"⚠️ Could not read CSV: {e}")
        else:
            st.markdown("""<div class="box" style="opacity:0.6;font-size:0.74rem;">
↑ Upload your cash flow CSV or use the sample data.<br><br>
<strong>Use cases:</strong> Monthly cash flow statement · Liquidity planning · Burn rate ·
Runway forecasting · Operating cash health<br>
<strong>Output:</strong> Net cash flow · Burn rate · Runway months · Closing balance trend · AI CFO
</div>""", unsafe_allow_html=True)
        return

    df = st.session_state["_cf_df"].copy()
    cols = list(df.columns)

    # ── Auto-detect columns ────────────────────────────────────────────────────
    def _find(keywords, fallback=None):
        return next((c for c in cols if any(k in c.lower() for k in keywords)), fallback)

    period_col = _find(["month","period","date","quarter"], cols[0])
    open_col   = _find(["opening","open_bal","begin"], None)
    op_in      = _find(["operating_in","op_in","oper_in","operating_inflow"], None)
    op_out     = _find(["operating_out","op_out","oper_out","operating_out"], None)
    inv_in     = _find(["investing_in","inv_in"], None)
    inv_out    = _find(["investing_out","inv_out"], None)
    fin_in     = _find(["financing_in","fin_in"], None)
    fin_out    = _find(["financing_out","fin_out"], None)

    # Convert to numeric
    for c in [open_col, op_in, op_out, inv_in, inv_out, fin_in, fin_out]:
        if c and c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    # ── Compute cash flow components ──────────────────────────────────────────
    df["_op_net"]  = (df[op_in].fillna(0)  if op_in  else 0) - (df[op_out].fillna(0)  if op_out  else 0)
    df["_inv_net"] = (df[inv_in].fillna(0) if inv_in else 0) - (df[inv_out].fillna(0) if inv_out else 0)
    df["_fin_net"] = (df[fin_in].fillna(0) if fin_in else 0) - (df[fin_out].fillna(0) if fin_out else 0)
    df["_net_cf"]  = df["_op_net"] + df["_inv_net"] + df["_fin_net"]

    # Closing balance
    if open_col:
        df["_close"] = df[open_col] + df["_net_cf"]
    else:
        df["_close"] = df["_net_cf"].cumsum()

    # ── KPI computation ────────────────────────────────────────────────────────
    total_op_in   = df["_op_net"].clip(lower=0).sum()
    total_op_out  = (-df["_op_net"]).clip(lower=0).sum()
    avg_monthly_net = df["_net_cf"].mean()
    total_net_cf  = df["_net_cf"].sum()
    closing_bal   = df["_close"].iloc[-1]
    opening_bal   = df[open_col].iloc[0] if open_col else 0
    avg_monthly_burn = (-df["_net_cf"]).clip(lower=0).mean()

    # Positive cash months
    pos_months = int((df["_net_cf"] > 0).sum())
    neg_months = int((df["_net_cf"] <= 0).sum())

    # Runway (months of current balance at burn rate)
    runway = (closing_bal / avg_monthly_burn) if avg_monthly_burn > 0 else float("inf")

    # Operating cash conversion %
    op_inflow_total = df[op_in].sum() if op_in else 1
    op_cf_pct = (df["_op_net"].sum() / op_inflow_total * 100) if op_inflow_total else 0

    # ── Summary KPIs ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-label">Cash Flow Summary</div>', unsafe_allow_html=True)
    _net_col = "#4ade80" if total_net_cf >= 0 else "#f87171"
    _avg_col = "#4ade80" if avg_monthly_net >= 0 else "#f87171"
    _rwy_col = "#4ade80" if runway > 12 else ("#fbbf24" if runway > 6 else "#f87171")

    st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin-bottom:16px;">
  <div class="kpi-card" style="--ac:#06b6d4">
    <div class="kpi-label">Closing Balance</div>
    <div class="kpi-value">{fmt_m(closing_bal)}</div>
    <div class="kpi-delta">vs open {fmt_m(opening_bal)}</div>
  </div>
  <div class="kpi-card" style="--ac:{_net_col}">
    <div class="kpi-label">Total Net CF</div>
    <div class="kpi-value" style="color:{_net_col};">{fmt_m(total_net_cf)}</div>
    <div class="kpi-delta">{"Inflow" if total_net_cf>=0 else "Outflow"}</div>
  </div>
  <div class="kpi-card" style="--ac:{_avg_col}">
    <div class="kpi-label">Avg Monthly</div>
    <div class="kpi-value" style="color:{_avg_col};">{fmt_m(avg_monthly_net)}</div>
    <div class="kpi-delta">net cash flow</div>
  </div>
  <div class="kpi-card" style="--ac:{_rwy_col}">
    <div class="kpi-label">Runway</div>
    <div class="kpi-value" style="color:{_rwy_col};">
      {"∞" if runway == float("inf") else f"{runway:.0f}mo"}</div>
    <div class="kpi-delta">at current burn</div>
  </div>
  <div class="kpi-card" style="--ac:#4ade80">
    <div class="kpi-label">Positive Months</div>
    <div class="kpi-value">{pos_months}</div>
    <div class="kpi-delta">of {len(df)} total</div>
  </div>
  <div class="kpi-card" style="--ac:#c9a84c">
    <div class="kpi-label">Op CF Conversion</div>
    <div class="kpi-value">{op_cf_pct:.1f}%</div>
    <div class="kpi-delta">of operating inflows</div>
  </div>
</div>""", unsafe_allow_html=True)

    # ── Charts ────────────────────────────────────────────────────────────────
    c1, c2 = st.columns(2)
    with c1:
        # Net cash flow waterfall by month
        clrs = ["#4ade80" if v >= 0 else "#f87171" for v in df["_net_cf"]]
        fig = go.Figure(go.Bar(
            x=df[period_col].tolist(), y=df["_net_cf"].tolist(),
            marker_color=clrs,
            text=[f"{fmt_m(v)}" for v in df["_net_cf"]],
            textposition="auto"))
        fig.update_layout(**PLOTLY_BASE, title="Monthly Net Cash Flow",
                          height=280, xaxis=AXIS, yaxis=AXIS)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Closing balance trend
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df[period_col].tolist(), y=df["_close"].tolist(),
            fill="tozeroy", fillcolor="rgba(6,182,212,0.08)",
            line=dict(color="#06b6d4", width=2),
            name="Closing Balance"))
        fig.update_layout(**PLOTLY_BASE, title="Closing Balance Trend",
                          height=280, xaxis=AXIS, yaxis=AXIS, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # ── Cash flow waterfall (operating/investing/financing) ───────────────────
    if op_in and op_out:
        st.markdown('<div class="sec-label">Cash Flow Breakdown</div>',
                    unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3:
            op_total  = df["_op_net"].sum()
            inv_total = df["_inv_net"].sum()
            fin_total = df["_fin_net"].sum()
            cats  = ["Operating","Investing","Financing"]
            vals  = [op_total, inv_total, fin_total]
            bclrs = ["#4ade80" if v >= 0 else "#f87171" for v in vals]
            fig = go.Figure(go.Bar(
                x=cats, y=vals,
                marker_color=bclrs,
                text=[fmt_m(v) for v in vals], textposition="auto"))
            fig.update_layout(**PLOTLY_BASE, title="CF by Category (Total)",
                              height=240, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)
        with c4:
            # Cash conversion donut: op cf / total inflows
            op_in_total  = df[op_in].sum() if op_in else 0
            op_out_total = df[op_out].sum() if op_out else 0
            op_retained  = max(0, op_in_total - op_out_total)
            op_spent     = max(0, op_out_total)
            if op_in_total > 0:
                fig = go.Figure(go.Pie(
                    labels=["Retained (Net CF)","Operating Costs"],
                    values=[op_retained, op_spent], hole=0.55,
                    marker=dict(colors=["#4ade80","#f87171"],
                                line=dict(color="#0a0a08",width=2)),
                    textinfo="label+percent", textfont=dict(size=9)))
                fig.add_annotation(
                    text=f"{op_cf_pct:.0f}%<br>retained",
                    x=0.5, y=0.5, showarrow=False,
                    font=dict(size=12, color="#fafaf8",
                              family="Playfair Display"))
                fig.update_layout(**PLOTLY_BASE,
                                  title="Operating Cash Conversion",
                                  height=240, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

    # ── Data table ────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-label">Detailed Cash Flow Statement</div>',
                unsafe_allow_html=True)
    display_df = df[[period_col]].copy()
    if open_col:  display_df["Opening Balance"] = df[open_col]
    display_df["Operating Net"] = df["_op_net"]
    display_df["Investing Net"] = df["_inv_net"]
    display_df["Financing Net"] = df["_fin_net"]
    display_df["Net Cash Flow"] = df["_net_cf"]
    display_df["Closing Balance"] = df["_close"]
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.download_button("📥 Download Cash Flow Report (CSV)",
                       display_df.to_csv(index=False).encode(),
                       "Fincy_CashFlow_Report.csv", "text/csv")

    # ── AI CFO ────────────────────────────────────────────────────────────────
    cf_ctx = (f"Cash Flow Analysis: {len(df)} months | "
              f"Closing Balance={fmt_m(closing_bal)} | "
              f"Total Net CF={fmt_m(total_net_cf)} | "
              f"Avg Monthly Net={fmt_m(avg_monthly_net)} | "
              f"Runway={runway:.0f} months | "
              f"Positive months={pos_months}/{len(df)} | "
              f"Operating CF Conversion={op_cf_pct:.1f}% | "
              f"Burn rate={fmt_m(avg_monthly_burn)}/month")
    ai_cfo_section(cf_ctx, "cashflow",
        "e.g. Is my cash position healthy? Where is cash leaking? How do I improve runway?")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════
_mod = st.session_state.active_module

# ── Chat with Fincy — always-on sidebar chatbot ─────────────────────────────
show_global_chat()

if   _mod is None:           show_home()
elif _mod == "fpa":          run_fpa()
elif _mod == "recon":        run_recon()
elif _mod == "budget":       run_budget()
elif _mod == "cost":         run_cost()
elif _mod == "dataanalyst":  run_dataanalyst()
elif _mod == "personal":     run_personal()
elif _mod == "cashflow":     run_cashflow()

st.markdown("""
<div style="margin-top:40px;border-top:1px solid #1a1a14;padding-top:16px;
font-family:'IBM Plex Mono',monospace;font-size:0.52rem;color:#2a2a24;
letter-spacing:0.12em;text-align:center;">
FINCY INTELLIGENCE · AI CFO PLATFORM · FOUNDER: JITENDRA PARIDA · SENIOR FP&amp;A ANALYST
</div>""", unsafe_allow_html=True)
