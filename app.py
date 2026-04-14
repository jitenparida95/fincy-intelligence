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

def _get_groq_key() -> str:
    """Get Groq API key — tries Streamlit secrets first, then env var."""
    try:
        k = st.secrets.get("GROQ_API_KEY", "")
        if k: return k
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY", "")


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
if _qp and _qp in ("fpa", "recon", "budget", "cost"):
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
def show_home():
    page_header("AI-POWERED CFO DECISION PLATFORM")

    # Value prop strip
    st.markdown("""
<div style="background:#101010;border:1px solid #1e1e18;border-left:3px solid #c9a84c;
padding:14px 20px;margin-bottom:32px;display:flex;align-items:center;gap:20px;flex-wrap:wrap;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#c9a84c;flex-shrink:0;">Free 7-Day Trial</div>
  <div style="width:1px;height:14px;background:#2a2a20;flex-shrink:0;"></div>
  <div style="font-size:0.8rem;color:#a09880;font-weight:300;">
    All 4 modules · P&amp;L Intelligence · Reconciliation · Budget Tracker · Cost Analysis
  </div>
  <div style="margin-left:auto;font-family:'IBM Plex Mono',monospace;font-size:0.55rem;
  color:#3a3a34;letter-spacing:0.1em;">No credit card · No code · Session isolated</div>
</div>""", unsafe_allow_html=True)

    # ── Full HTML module cards with embedded launch links ──────────────────────
    # Each card is a single <a> tag — clicking anywhere on the card navigates
    # via ?m=xxx query param, which is handled at the top of the app.
    app_url = "https://fincy-intelligence.streamlit.app"

    st.markdown(f"""
<style>
.mod-home-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:2px;background:#1e1e18;}}
.mod-home-card{{
  display:block;background:#101010;padding:0;text-decoration:none;
  position:relative;overflow:hidden;transition:background 0.2s;
}}
.mod-home-card:hover{{background:#141410;}}
.mod-home-card::before{{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--mc);
}}
.mod-home-body{{padding:28px 26px 0;}}
.mod-home-icon{{font-size:1.9rem;margin-bottom:12px;display:block;}}
.mod-home-badge{{
  font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.18em;
  text-transform:uppercase;color:var(--mc);border:1px solid var(--mc);
  padding:2px 8px;display:inline-block;margin-bottom:14px;
}}
.mod-home-title{{
  font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;
  color:#fafaf8;margin-bottom:9px;line-height:1.2;
}}
.mod-home-desc{{font-size:0.76rem;color:#5a5648;line-height:1.75;margin-bottom:12px;}}
.mod-home-tags{{
  font-family:'IBM Plex Mono',monospace;font-size:0.5rem;color:#3a3a34;
  letter-spacing:0.08em;margin-bottom:20px;
}}
.mod-home-btn{{
  display:block;
  background:var(--mc);color:#0a0a08;
  font-family:'IBM Plex Mono',monospace;font-size:0.68rem;font-weight:600;
  letter-spacing:0.08em;text-transform:uppercase;
  padding:13px 26px;text-align:left;margin:0;
  border-top:1px solid rgba(0,0,0,0.15);
  transition:opacity 0.15s;
}}
.mod-home-card:hover .mod-home-btn{{opacity:0.88;}}
@media(max-width:640px){{
  .mod-home-grid{{grid-template-columns:1fr;}}
}}
</style>

<div class="mod-home-grid">

  <a class="mod-home-card" href="{app_url}/?m=fpa" target="_self" style="--mc:#c9a84c;">
    <div class="mod-home-body">
      <span class="mod-home-icon">📊</span>
      <div class="mod-home-badge">Core Module</div>
      <div class="mod-home-title">FP&amp;A Intelligence</div>
      <div class="mod-home-desc">Instant P&amp;L dashboards, variance analysis, brand scorecards, and AI CFO chat from any CSV — in 60 seconds.</div>
      <div class="mod-home-tags">10+ KPIs · 7 Charts · AI CFO · PDF Export</div>
    </div>
    <div class="mod-home-btn">→ Launch FP&amp;A Intelligence</div>
  </a>

  <a class="mod-home-card" href="{app_url}/?m=recon" target="_self" style="--mc:#4ade80;">
    <div class="mod-home-body">
      <span class="mod-home-icon">🔁</span>
      <div class="mod-home-badge">New</div>
      <div class="mod-home-title">Reconciliation Engine</div>
      <div class="mod-home-desc">Upload ERP vs Bank, GL vs Sub-ledger, or PO vs Invoice. Auto-match, flag breaks, download exceptions.</div>
      <div class="mod-home-tags">Auto-Match · Break Flags · Exceptions CSV</div>
    </div>
    <div class="mod-home-btn">→ Launch Reconciliation Engine</div>
  </a>

  <a class="mod-home-card" href="{app_url}/?m=budget" target="_self" style="--mc:#fbbf24;">
    <div class="mod-home-body">
      <span class="mod-home-icon">🎯</span>
      <div class="mod-home-badge">New</div>
      <div class="mod-home-title">Budget vs Actuals Tracker</div>
      <div class="mod-home-desc">RAG-status tracker with prior year overlays, trend detection, and AI-generated board commentary in minutes.</div>
      <div class="mod-home-tags">RAG Status · Prior Year · AI Trend Analysis</div>
    </div>
    <div class="mod-home-btn">→ Launch Budget Tracker</div>
  </a>

  <a class="mod-home-card" href="{app_url}/?m=cost" target="_self" style="--mc:#f472b6;">
    <div class="mod-home-body">
      <span class="mod-home-icon">💡</span>
      <div class="mod-home-badge">New</div>
      <div class="mod-home-title">Cost Intelligence</div>
      <div class="mod-home-desc">COGS and OPEX benchmarking with segment efficiency scores and AI-driven cost reduction recommendations.</div>
      <div class="mod-home-tags">Benchmarks · Flagged Lines · AI Recommendations</div>
    </div>
    <div class="mod-home-btn">→ Launch Cost Intelligence</div>
  </a>

</div>""", unsafe_allow_html=True)

    # AI CFO status check — show warning if key not set
    _k = _get_groq_key()
    if not _k:
        st.markdown("""
<div style="background:#150404;border:1px solid #f87171;border-left:3px solid #f87171;
padding:12px 18px;margin-bottom:14px;display:flex;align-items:center;gap:14px;">
  <div style="font-size:1.2rem;flex-shrink:0;">⚠️</div>
  <div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;
    text-transform:uppercase;color:#f87171;margin-bottom:4px;">AI CFO Not Configured</div>
    <div style="font-size:0.76rem;color:#a09880;font-weight:300;">
      GROQ_API_KEY is missing. The AI CFO button will not work in any module.<br>
      <strong style="color:#fafaf8;">Fix:</strong> Streamlit Dashboard → Your app →
      ⋮ Settings → Secrets → add <code style="color:#c9a84c;">GROQ_API_KEY = "gsk_..."</code>
      · Get a free key at <a href="https://console.groq.com" target="_blank"
      style="color:#c9a84c;">console.groq.com ↗</a>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

    # Founder + privacy trust strip
    st.markdown("""
<div style="margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:1px;
background:#1e1e18;border:1px solid #1e1e18;margin-bottom:1px;">
  <div style="background:#101010;padding:18px 22px;display:flex;align-items:center;gap:14px;">
    <div style="width:38px;height:38px;background:#1a1a12;border:1px solid #c9a84c;
    border-radius:50%;display:flex;align-items:center;justify-content:center;
    font-family:'Playfair Display',serif;font-size:0.9rem;color:#c9a84c;flex-shrink:0;">JP</div>
    <div>
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.12em;
      text-transform:uppercase;color:#c9a84c;margin-bottom:3px;">Built by a Finance Practitioner</div>
      <div style="font-size:0.76rem;color:#a09880;font-weight:300;line-height:1.5;">
        Jitendra Parida · Senior FP&amp;A Analyst · IBM / Reckitt<br>
        <span style="color:#5a5648;font-size:0.68rem;">6+ years FMCG finance · MENARP &amp; Africa markets</span>
      </div>
      <div style="margin-top:5px;">
        <a href="https://www.linkedin.com/in/jitendraparida95/" target="_blank"
        style="font-family:'IBM Plex Mono',monospace;font-size:0.52rem;letter-spacing:0.1em;
        text-transform:uppercase;color:#c9a84c;text-decoration:none;">View LinkedIn ↗</a>
      </div>
    </div>
  </div>
  <div style="background:#101010;padding:18px 22px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.56rem;letter-spacing:0.12em;
    text-transform:uppercase;color:#4ade80;margin-bottom:8px;">🔒 Data Privacy</div>
    <div style="font-size:0.74rem;color:#a09880;font-weight:300;line-height:1.65;">
      Your data <strong style="color:#e8e2d4;">never leaves your session.</strong>
      No server storage. No cross-tenant access. Every upload is processed
      in-memory and discarded when you close the tab.
    </div>
    <div style="margin-top:7px;font-family:'IBM Plex Mono',monospace;font-size:0.52rem;
    letter-spacing:0.08em;color:#3a3a34;">Session-isolated · No logging · No sharing</div>
  </div>
</div>""", unsafe_allow_html=True)

    # Stats row
    st.markdown("""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1px;
background:#1e1e18;border:1px solid #1e1e18;">
  <div style="background:#101010;padding:18px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#c9a84c;">4</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-top:4px;">AI Modules</div>
  </div>
  <div style="background:#101010;padding:18px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#c9a84c;">10+</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-top:4px;">KPI Metrics</div>
  </div>
  <div style="background:#101010;padding:18px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#c9a84c;">60s</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-top:4px;">To Insights</div>
  </div>
  <div style="background:#101010;padding:18px;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.7rem;font-weight:900;color:#c9a84c;">0</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.5rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-top:4px;">Code Needed</div>
  </div>
</div>
<div style="margin-top:28px;border-top:1px solid #1a1a14;padding-top:16px;
font-family:'IBM Plex Mono',monospace;font-size:0.5rem;color:#2a2a24;
letter-spacing:0.12em;text-align:center;">
FINCY INTELLIGENCE · AI CFO PLATFORM · CONFIDENTIAL · FP&amp;A DECISION ENGINE
</div>""", unsafe_allow_html=True)



def ai_cfo_section(context_str: str, module_key: str, placeholder: str = "Ask about this data…"):
    """Renders an inline AI CFO chat panel for any module. Works on Streamlit Cloud + local."""
    st.markdown('''<div class="sec-label">🧠 AI CFO — Ask About This Data</div>''', unsafe_allow_html=True)

    # ── Key check ─────────────────────────────────────────────────────────────
    api_key = _get_groq_key()
    if not api_key:
        st.markdown("""
<div style="background:#150404;border:1px solid #f87171;border-left:3px solid #f87171;
padding:12px 16px;font-size:0.76rem;color:#a09880;font-weight:300;">
<strong style="color:#f87171;">AI CFO not available</strong> — GROQ_API_KEY is missing.<br>
Add it in Streamlit Dashboard → Your app → ⋮ Settings → Secrets:
<code style="color:#c9a84c;">GROQ_API_KEY = "gsk_..."</code>
· Free key at <a href="https://console.groq.com" target="_blank" style="color:#c9a84c;">console.groq.com ↗</a>
</div>""", unsafe_allow_html=True)
        return

    hist_key = f"chat_{module_key}"
    if hist_key not in st.session_state:
        st.session_state[hist_key] = []

    # ── Chat history ──────────────────────────────────────────────────────────
    if st.session_state[hist_key]:
        for chat in reversed(st.session_state[hist_key][-3:]):
            st.markdown(f'''
<div class="box" style="margin-bottom:8px;">
<span style="color:#3a3a34;font-size:0.62rem;font-family:\'IBM Plex Mono\',monospace;">YOU:</span>
{chat["q"]}<br><br>
<span style="color:#3a3a34;font-size:0.62rem;font-family:\'IBM Plex Mono\',monospace;">AI CFO:</span><br>
{chat["a"]}
</div>''', unsafe_allow_html=True)

    # ── Input row ─────────────────────────────────────────────────────────────
    qa1, qa2, qa3 = st.columns([4, 1, 1])
    with qa1:
        question = st.text_input("", placeholder=placeholder,
                                 key=f"ai_q_{module_key}", label_visibility="collapsed")
    with qa2:
        ask = st.button("🚀 Ask CFO", use_container_width=True, key=f"ai_ask_{module_key}")
    with qa3:
        if st.button("🧹", use_container_width=True, key=f"ai_clear_{module_key}"):
            st.session_state[hist_key] = []
            st.rerun()

    # ── Response ──────────────────────────────────────────────────────────────
    if ask and question.strip():
        with st.spinner("AI CFO analysing…"):
            try:
                from groq import Groq
                client = Groq(api_key=api_key)
                prompt = (
                    "You are a world-class CFO analyst. Be concise and sharp — 2-3 insights max.\n\n"
                    f"Data context: {context_str}\n\n"
                    f"Question: {question.strip()}\n\n"
                    "Answer with CFO-level insights and specific recommended actions. "
                    "Use bullet points. Reference specific numbers from the context."
                )
                resp = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=600,
                    temperature=0.3)
                ans = resp.choices[0].message.content
            except Exception as e:
                ans = f"⚠️ Error calling Groq API: {e}"
        st.markdown(f'''<div class="ai-box">{ans}</div>''', unsafe_allow_html=True)
        st.session_state[hist_key].append({"q": question.strip(), "a": ans})
    elif not ask:
        st.markdown('''<div class="box" style="opacity:0.4;font-size:0.72rem;">
Ask the AI CFO anything about this data — "What are the key risks?",
"Where should we focus?", "What actions do you recommend?"
</div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1 — FP&A INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_fpa():
    # ── Sidebar ──────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 📊 FP&A Intelligence")
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
        page_header("FP&A INTELLIGENCE", "Upload Data")

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
    page_header("FP&A INTELLIGENCE", "P&L Dashboard")

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

    # Inline AI CFO
    fpa_ctx = f"NR={fmt_m(nr)} YoY={yoy:.1f}% | GP={fmt_m(gp)} GPM={gpm:.1f}% | EBITDA={fmt_m(ebitda)} {ebitdam:.1f}% | COGS {cogsp:.1f}%NR | OPEX {opexp:.1f}%NR | Budget Ach {bach:.1f}% | Var {fmt_m(var)} | Top Market={top_mkt} | Risk={risk_mkt} | Top Brand={top_brand}"
    ai_cfo_section(fpa_ctx, "fpa", "e.g. Why is margin declining? Which market needs attention?")
    if st.button("📄 Download Board Commentary (PDF)", key="fpa_pdf"):
        pdf = generate_pdf(f"Fincy Intelligence — FP&A Board Report\n\nNet Revenue: {fmt_m(nr)} | YoY: {yoy:+.1f}%\nGP Margin: {gpm:.1f}% | EBITDA: {ebitdam:.1f}%\nTop Market: {top_mkt} | Risk Market: {risk_mkt}")
        st.download_button("📄 Download PDF", data=pdf, file_name="Fincy_FPA_Report.pdf", mime="application/pdf", key="fpa_pdf_dl")


# ══════════════════════════════════════════════════════════════════════════════
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
Upload two CSVs (ERP vs Bank, GL vs Sub-ledger, PO vs Invoice). Select match key columns.
If your key is not unique, add more columns to build a composite key.
For bank/ERP: use <strong style="color:#fafaf8;">Category + Date + Amount</strong> as a
3-part key for the most accurate result — zero false breaks.
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
\u2191 Upload both files above or click the sample buttons.<br><br>
<strong>Use cases:</strong> ERP vs Bank \u00b7 GL vs Sub-ledger \u00b7 PO vs Invoice \u00b7 Intercompany<br>
<strong>Output:</strong> Match rate \u00b7 Amount breaks \u00b7 Missing records \u00b7 Exceptions CSV
</div>""", unsafe_allow_html=True)
        return

    cols1  = list(df1.columns)
    cols2  = list(df2.columns)
    common = [c for c in cols1 if c in cols2]

    # ── Column selectors ──────────────────────────────────────────────────────
    st.markdown('<div class="sec-label">Configure Match</div>', unsafe_allow_html=True)
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        kg   = next((c for c in common if any(k in c.lower()
               for k in ["id","no","number","ref","invoice","trans","prefix","type","cat"])),
               common[0] if common else cols1[0])
        mkey = st.selectbox("Match Key Column (1st)", common if common else cols1,
                            index=common.index(kg) if kg in common else 0, key="recon_mkey")
    with mc2:
        n1   = [c for c in cols1 if pd.api.types.is_numeric_dtype(df1[c])]
        ag1  = next((c for c in n1 if any(k in c.lower()
               for k in ["amount","amt","erp","value","total","n_amount"])), n1[0] if n1 else cols1[0])
        a1_col = st.selectbox("Amount (Source A)", n1 if n1 else cols1,
                              index=n1.index(ag1) if ag1 in n1 else 0, key="recon_a1")
    with mc3:
        n2   = [c for c in cols2 if pd.api.types.is_numeric_dtype(df2[c])]
        ag2  = next((c for c in n2 if any(k in c.lower()
               for k in ["amount","amt","bank","value","total","n_amount"])), n2[0] if n2 else cols2[0])
        a2_col = st.selectbox("Amount (Source B)", n2 if n2 else cols2,
                              index=n2.index(ag2) if ag2 in n2 else 0, key="recon_a2")

    # ── Duplicate-key detection ───────────────────────────────────────────────
    dup_a = int(df1[mkey].duplicated().sum())
    dup_b = int(df2[mkey].duplicated().sum())
    secondary_key = None
    tertiary_key  = None

    if dup_a > 0 or dup_b > 0:
        st.markdown(f"""
<div style="background:#150f00;border:1px solid #fbbf24;border-left:3px solid #fbbf24;
padding:12px 18px;margin-bottom:12px;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#fbbf24;margin-bottom:6px;">\u26a0\ufe0f Match Key Has Duplicates</div>
  <div style="font-size:0.76rem;color:#a09880;font-weight:300;">
    <strong style="color:#fafaf8;">{mkey}</strong> is not a unique transaction ID \u2014
    Source A has <strong style="color:#fbbf24;">{dup_a} duplicate</strong> values,
    Source B has <strong style="color:#fbbf24;">{dup_b} duplicate</strong> values.<br>
    Matching on a non-unique column causes a cartesian product producing thousands of
    false Amount Breaks. Add 1\u20132 more columns to build a composite key.<br><br>
    <strong style="color:#4ade80;">\U0001f4a1 Best practice:</strong>
    Use <em>Category + Date + Amount</em> as a 3-part key for zero false breaks.
  </div>
</div>""", unsafe_allow_html=True)

        sk_opts = ["\u2014 none \u2014"] + [c for c in common if c != mkey]
        # Auto-suggest: exact date column first, then partial match, avoid pure "year"
        date_guess = next(
            (c for c in sk_opts if c.lower() in ["transactiondate","date","trans_date","tran_date"]),
            next((c for c in sk_opts if any(k in c.lower()
                  for k in ["transact","date","period","month"]) and "year" not in c.lower()),
            next((c for c in sk_opts if any(k in c.lower() for k in ["date","period","month","year"])),
            sk_opts[0])))
        secondary_key_raw = st.selectbox(
            "2nd Key Column (e.g. transaction date)",
            sk_opts,
            index=sk_opts.index(date_guess) if date_guess in sk_opts else 0,
            key="recon_mkey2")
        secondary_key = secondary_key_raw if secondary_key_raw != "\u2014 none \u2014" else None

        # 3rd key — auto-suggest the amount column for highest accuracy
        amtcol_guess = next(
            (c for c in common if c == a1_col or any(k in c.lower()
             for k in ["amount","amt","n_amount"])), None)
        tk_opts = ["\u2014 none \u2014"] + [c for c in common
                  if c not in [mkey, secondary_key_raw or ""]]
        tk_default = amtcol_guess if amtcol_guess in tk_opts else tk_opts[0]
        tertiary_key_raw = st.selectbox(
            "3rd Key Column (e.g. amount \u2014 highest accuracy)",
            tk_opts,
            index=tk_opts.index(tk_default) if tk_default in tk_opts else 0,
            key="recon_mkey3",
            help="Using amount as 3rd key matches by value not row position, eliminating false breaks")
        tertiary_key = tertiary_key_raw if tertiary_key_raw != "\u2014 none \u2014" else None

    if st.button("\U0001f501 Run Reconciliation", use_container_width=True, key="run_recon"):

        # 1. Build composite match key
        def _mk(df, p, s=None, t=None):
            k = df[p].astype(str).str.strip()
            if s: k = k + "\xa7" + df[s].astype(str).str.strip()
            if t: k = k + "\xa7" + df[t].astype(str).str.strip()
            return k

        _df1 = df1.copy(); _df2 = df2.copy()
        _df1["_mk"] = _mk(_df1, mkey, secondary_key, tertiary_key)
        _df2["_mk"] = _mk(_df2, mkey, secondary_key, tertiary_key)

        # 2. Within-group sequence (handles legitimate duplicate rows positionally)
        _df1["_sq"] = _df1.groupby("_mk").cumcount()
        _df2["_sq"] = _df2.groupby("_mk").cumcount()
        _df1["_fk"] = _df1["_mk"] + "\xa7" + _df1["_sq"].astype(str)
        _df2["_fk"] = _df2["_mk"] + "\xa7" + _df2["_sq"].astype(str)

        # 3. Merge keeping all original columns from both sides
        b_rename = {c: c+"_B" for c in _df2.columns
                    if c in _df1.columns and c not in ["_mk","_sq","_fk",a2_col]}
        left  = _df1.drop(columns=["_mk","_sq"]).rename(columns={a1_col:"Amt_A"})
        right = _df2.drop(columns=["_mk","_sq"]).rename(
                    columns={**{a2_col:"Amt_B"}, **b_rename})
        merged = pd.merge(left, right, on="_fk", how="outer", indicator=True)

        # 4. Classify
        def classify(r):
            if r["_merge"] == "left_only":  return "Missing in B"
            if r["_merge"] == "right_only": return "Missing in A"
            a = r["Amt_A"]; b = r["Amt_B"]
            if pd.isna(a) or pd.isna(b): return "Amount Break"
            return "Matched" if abs(float(a)-float(b)) <= tolerance else "Amount Break"

        merged["Status"]     = merged.apply(classify, axis=1)
        merged["Difference"] = merged["Amt_A"].fillna(0) - merged["Amt_B"].fillna(0)

        # 5. Fill NaN columns from the B side for "Missing in A" / "Missing in B" rows
        #    For Missing in A: A-side columns are NaN — fill from B-side equivalents
        #    For Missing in B: B-side columns are NaN — already have A-side values
        for orig_col in list(df1.columns):
            b_col = orig_col + "_B"
            if b_col in merged.columns and orig_col in merged.columns:
                merged[orig_col] = merged[orig_col].fillna(merged[b_col])

        # 6. Build clean output columns (all original cols + amounts + status + diff)
        drop_internal = {"_fk","_merge"} | {c for c in merged.columns if c.endswith("_B")}
        meta_cols = [c for c in merged.columns if c not in drop_internal
                     and c not in ["Amt_A","Amt_B","Status","Difference"]]
        merged_out = merged[[c for c in meta_cols + ["Amt_A","Amt_B","Status","Difference"]
                              if c in merged.columns]].copy()

        # 7. Summary stats
        total   = len(merged_out)
        matched = int((merged_out["Status"]=="Matched").sum())
        breaks  = int((merged_out["Status"]=="Amount Break").sum())
        miss_b  = int((merged_out["Status"]=="Missing in B").sum())
        miss_a  = int((merged_out["Status"]=="Missing in A").sum())
        mrate   = matched/total*100 if total else 0
        t_break = float(merged_out.loc[merged_out["Status"]=="Amount Break","Difference"].abs().sum())

        # 8. Key banner
        key_parts = [k for k in [mkey, secondary_key, tertiary_key] if k]
        if len(key_parts) > 1:
            st.markdown(f"""<div style="background:#041508;border:1px solid #4ade80;
padding:9px 16px;margin-bottom:12px;font-family:'IBM Plex Mono',monospace;
font-size:0.6rem;letter-spacing:0.1em;color:#4ade80;">
\u2713 {len(key_parts)}-part composite key: <strong>{" + ".join(key_parts)}</strong>
</div>""", unsafe_allow_html=True)

        # 9. KPI cards
        st.markdown('<div class="sec-label">Reconciliation Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="rag-row">
<div class="rag-g"><div class="rag-lbl">Matched</div>
  <div class="rag-val" style="color:#4ade80;">{matched:,}</div>
  <div style="font-size:0.6rem;color:#4ade80;">{mrate:.1f}% match rate</div></div>
<div class="{"rag-r" if breaks>0 else "rag-g"}"><div class="rag-lbl">Amount Breaks</div>
  <div class="rag-val" style="color:{"#f87171" if breaks>0 else "#4ade80"};">{breaks:,}</div>
  <div style="font-size:0.6rem;color:#5a5648;">Diff: {t_break:,.2f}</div></div>
<div class="{"rag-a" if miss_b>0 else "rag-g"}"><div class="rag-lbl">Missing in B</div>
  <div class="rag-val" style="color:{"#fbbf24" if miss_b>0 else "#4ade80"};">{miss_b:,}</div>
  <div style="font-size:0.6rem;color:#5a5648;">In A only</div></div>
<div class="{"rag-b" if miss_a>0 else "rag-g"}"><div class="rag-lbl">Missing in A</div>
  <div class="rag-val" style="color:{"#60a5fa" if miss_a>0 else "#4ade80"};">{miss_a:,}</div>
  <div style="font-size:0.6rem;color:#5a5648;">In B only</div></div>
</div>""", unsafe_allow_html=True)

        # 10. Charts
        ch1, ch2 = st.columns([1, 2])
        with ch1:
            nz_labs = [l for l,v in zip(["Matched","Amount Break","Missing in B","Missing in A"],
                                        [matched,breaks,miss_b,miss_a]) if v>0]
            nz_vals = [v for v in [matched,breaks,miss_b,miss_a] if v>0]
            nz_clrs = [c for c,v in zip(["#4ade80","#f87171","#fbbf24","#60a5fa"],
                                        [matched,breaks,miss_b,miss_a]) if v>0]
            fig = go.Figure(go.Pie(labels=nz_labs, values=nz_vals, hole=0.62,
                marker=dict(colors=nz_clrs, line=dict(color="#0a0a08",width=2)),
                textinfo="label+percent", textfont=dict(size=9)))
            fig.add_annotation(text=f"{mrate:.0f}%<br>Matched", x=0.5, y=0.5,
                               showarrow=False,
                               font=dict(size=13,color="#fafaf8",family="Playfair Display"))
            fig.update_layout(**PLOTLY_BASE, title="Reconciliation Status",
                              height=270, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        with ch2:
            dbs = merged_out.groupby("Status")["Difference"].sum().reset_index()
            clrs = {"Matched":"#4ade80","Amount Break":"#f87171",
                    "Missing in B":"#fbbf24","Missing in A":"#60a5fa"}
            fig = go.Figure(go.Bar(x=dbs["Status"], y=dbs["Difference"],
                marker_color=[clrs.get(s,"#5a5648") for s in dbs["Status"]],
                text=dbs["Difference"].apply(lambda x: f"{x:+,.2f}"),textposition="auto"))
            fig.update_layout(**PLOTLY_BASE, title="Net Difference by Status",
                              height=270, xaxis=AXIS, yaxis=AXIS)
            st.plotly_chart(fig, use_container_width=True)

        # 11. Exceptions
        exc = merged_out[merged_out["Status"] != "Matched"].copy()
        if not exc.empty:
            st.markdown('<div class="sec-label">Exceptions Detail</div>', unsafe_allow_html=True)
            exc_types = [t for t in ["Amount Break","Missing in B","Missing in A"]
                         if t in exc["Status"].values]
            sf = st.multiselect("Filter Status", exc_types, default=exc_types, key="recon_sf")
            fe = exc[exc["Status"].isin(sf)]
            st.dataframe(fe, use_container_width=True, hide_index=True)
            st.download_button("\U0001f4e5 Download Exceptions (CSV)",
                               fe.to_csv(index=False).encode(),
                               "Fincy_Recon_Exceptions.csv","text/csv",key="dl_exc")
        else:
            st.success("\U0001f389 Perfect reconciliation \u2014 no exceptions found!")

        # 12. Full output
        st.markdown('<div class="sec-label">Full Reconciliation Output</div>', unsafe_allow_html=True)
        st.dataframe(merged_out, use_container_width=True, hide_index=True)
        st.download_button("\U0001f4e5 Download Full Recon Output (CSV)",
                           merged_out.to_csv(index=False).encode(),
                           "Fincy_Recon_Full.csv","text/csv",key="dl_full")

        # 13. AI CFO
        recon_ctx = (f"Reconciliation: {total} records | "
                     f"Matched={matched} ({mrate:.1f}%) | "
                     f"Amount Breaks={breaks} (total diff={t_break:,.0f}) | "
                     f"Missing in B={miss_b} | Missing in A={miss_a} | "
                     f"Key: {' + '.join(key_parts)}")
        ai_cfo_section(recon_ctx, "recon",
            "e.g. What caused the missing records? Which breaks need urgent attention?")


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
# MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════
_mod = st.session_state.active_module

if   _mod is None:      show_home()
elif _mod == "fpa":     run_fpa()
elif _mod == "recon":   run_recon()
elif _mod == "budget":  run_budget()
elif _mod == "cost":    run_cost()

st.markdown("""
<div style="margin-top:40px;border-top:1px solid #1a1a14;padding-top:16px;
font-family:'IBM Plex Mono',monospace;font-size:0.52rem;color:#2a2a24;
letter-spacing:0.12em;text-align:center;">
FINCY INTELLIGENCE · AI CFO PLATFORM · BUILT BY JITENDRA PARIDA · SENIOR FP&amp;A ANALYST
</div>""", unsafe_allow_html=True)
