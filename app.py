import os
import io
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

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=IBM+Plex+Mono:wght@300;400;500&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

html,body,[class*="css"]{font-family:'IBM Plex Sans',sans-serif;background:#0a0a08;color:#e8e2d4;}

section[data-testid="stSidebar"]{background:#101010;border-right:1px solid #242420;}
section[data-testid="stSidebar"] *{color:#a09880 !important;}
section[data-testid="stSidebar"] h2,section[data-testid="stSidebar"] h3{color:#c9a84c !important;}

.main .block-container{padding:1.2rem 1.6rem;max-width:100%;}

.stButton>button{background:#c9a84c;color:#0a0a08;border:none;font-family:'IBM Plex Mono',monospace;font-size:0.72rem;letter-spacing:0.08em;font-weight:500;padding:9px 22px;transition:background 0.2s;}
.stButton>button:hover{background:#e8c96a;color:#0a0a08;}

.stTextInput input{background:#101010 !important;border:1px solid #242420 !important;color:#e8e2d4 !important;font-family:'IBM Plex Mono',monospace !important;}
.stTextInput input:focus{border-color:#c9a84c !important;}

.stSelectbox>div>div{background:#101010 !important;border:1px solid #242420 !important;color:#e8e2d4 !important;}

div[data-testid="metric-container"]{display:none;}
#MainMenu{visibility:hidden;}footer{visibility:hidden;}
header{visibility:visible !important;}

.fin-title{font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:#fafaf8;margin-bottom:4px;}
.fin-sub{font-family:'IBM Plex Mono',monospace;font-size:0.65rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;}
.fin-gold{color:#c9a84c;}

.kpi-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:1.4rem;}
.kpi-grid-2{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:1.6rem;}
.kpi-card{background:#101010;border:1px solid #242420;padding:15px 16px;position:relative;overflow:hidden;transition:border-color 0.2s;}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:1.5px;background:var(--ac);}
.kpi-label{font-family:'IBM Plex Mono',monospace;font-size:0.58rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-bottom:6px;}
.kpi-value{font-family:'Playfair Display',serif;font-size:1.55rem;font-weight:700;color:#fafaf8;}
.kpi-delta{font-family:'IBM Plex Mono',monospace;font-size:0.65rem;margin-top:4px;}
.pos{color:#4ade80;}.neg{color:#f87171;}.neu{color:#5a5648;}

.sec-label{font-family:'IBM Plex Mono',monospace;font-size:0.62rem;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c;margin:1.4rem 0 0.65rem;border-left:2px solid #c9a84c;padding-left:10px;}

.box{background:#101010;border:1px solid #242420;border-left:2px solid #c9a84c;padding:16px 18px;font-size:0.8rem;line-height:1.85;color:#a09880;}
.box strong{color:#c9a84c;}
.ai-box{background:#0d0d0a;border:1px solid #2a2a20;padding:15px 18px;font-size:0.8rem;line-height:1.85;color:#c9a84c;}

.rag-row{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:1.4rem;}
.rag-g{background:#051a0a;border:1px solid #4ade80;padding:13px;text-align:center;}
.rag-a{background:#1a1200;border:1px solid #fbbf24;padding:13px;text-align:center;}
.rag-r{background:#1a0505;border:1px solid #f87171;padding:13px;text-align:center;}
.rag-b{background:#060e1a;border:1px solid #60a5fa;padding:13px;text-align:center;}
.rag-lbl{font-family:'IBM Plex Mono',monospace;font-size:0.54rem;letter-spacing:0.14em;text-transform:uppercase;color:#5a5648;margin-bottom:5px;}
.rag-val{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;}

.mapper-box{background:#101010;border:1px solid #242420;border-left:2px solid #818cf8;padding:18px;margin-bottom:18px;}

/* MODULE SELECTOR */
.mod-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:24px;max-width:820px;margin-left:auto;margin-right:auto;}
.mod-sel{background:#101010;border:1px solid #242420;padding:26px 22px;position:relative;overflow:hidden;transition:border-color 0.2s;}
.mod-sel::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--mc,#c9a84c);}
.mod-sel-icon{font-size:1.6rem;margin-bottom:10px;}
.mod-sel-title{font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#fafaf8;margin-bottom:6px;}
.mod-sel-desc{font-size:0.75rem;color:#5a5648;line-height:1.7;}
.mod-sel-badge{font-family:'IBM Plex Mono',monospace;display:inline-block;margin-top:9px;font-size:0.54rem;letter-spacing:0.16em;text-transform:uppercase;color:var(--mc,#c9a84c);border:1px solid var(--mc,#c9a84c);padding:2px 7px;}

@media(max-width:768px){
  .kpi-grid,.kpi-grid-2{grid-template-columns:repeat(2,1fr);}
  .mod-grid{grid-template-columns:1fr;}
  .rag-row{grid-template-columns:repeat(2,1fr);}
  .main .block-container{padding:1rem;}
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ─────────────────────────────────────────────────────────────
for k,v in [("chat_history",[]),("col_map",{}),("mapping_confirmed",False),("active_module",None)]:
    if k not in st.session_state: st.session_state[k]=v

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
PLOTLY_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Mono, monospace", color="#5a5648", size=10),
    margin=dict(l=10,r=10,t=28,b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=9)),
)
AXIS = dict(gridcolor="#1a1a16", linecolor="#1a1a16", tickfont=dict(size=9))
PALETTE = ["#c9a84c","#4ade80","#818cf8","#f472b6","#fb923c","#60a5fa","#fbbf24","#2dd4bf"]

REQUIRED_COLS = {
    "Net_Revenue":"Net Revenue","Gross_Profit":"Gross Profit","EBITDA":"EBITDA",
    "COGS":"COGS","OPEX":"OPEX","Volume_Units":"Volume / Units","Base_NR":"Base Net Revenue",
    "Trade_Promo":"Trade Promo Spend","Budget_NR":"Budget Net Revenue",
    "Variance_NR":"NR Variance vs Budget","PY_NR":"Prior Year Net Revenue",
}
OPTIONAL_DIMS = {
    "Year":"Year","Quarter":"Quarter","Month":"Month","Month_Num":"Month Number (sorting)",
    "Market":"Market / Region","Category":"Category","Brand":"Brand","Channel":"Channel","Type":"Type",
}

def fmt_m(v):
    if abs(v)>=1_000_000: return f"{v/1_000_000:,.1f}M"
    if abs(v)>=1_000: return f"{v/1_000:,.1f}K"
    return f"{v:,.0f}"
def dc(v): return "pos" if v>0 else("neg" if v<0 else "neu")
def safe_col(df,col,default=0): return df[col] if col in df.columns else pd.Series([default]*len(df))
def generate_pdf(text):
    buf=BytesIO(); doc=SimpleDocTemplate(buf); styles=getSampleStyleSheet(); content=[]
    content.append(Paragraph("<b>Fincy Intelligence — CFO Report</b>",styles["Title"])); content.append(Spacer(1,12))
    for line in text.split("\n"):
        if line.strip(): content.append(Paragraph(line,styles["Normal"])); content.append(Spacer(1,8))
    doc.build(content); buf.seek(0); return buf


# ══════════════════════════════════════════════════════════════════════════════
# EMBEDDED SAMPLE DATA
# ══════════════════════════════════════════════════════════════════════════════

SAMPLE_FMCG_CSV = """Year,Quarter,Month,Month_Num,Market,Brand,Channel,Category,Net_Revenue,Gross_Profit,EBITDA,COGS,OPEX,Volume_Units,Base_NR,Trade_Promo,Budget_NR,Variance_NR,PY_NR
2023,Q1,Jan,1,UK,Alpha,Online,Haircare,1200,660,300,540,360,12000,1350,-150,1150,50,1100
2023,Q1,Jan,1,UK,Beta,Retail,Skincare,980,490,200,490,290,9800,1100,-120,1000,-20,950
2023,Q1,Jan,1,DE,Alpha,Online,Haircare,870,435,180,435,255,8700,980,-110,850,20,820
2023,Q1,Jan,1,DE,Gamma,B2B,Bodycare,650,325,130,325,195,6500,730,-80,620,30,610
2023,Q1,Jan,1,FR,Beta,Retail,Skincare,780,390,155,390,235,7800,880,-100,760,20,740
2023,Q1,Feb,2,UK,Alpha,Online,Haircare,1250,688,312,563,375,12500,1400,-150,1200,50,1140
2023,Q1,Feb,2,UK,Beta,Retail,Skincare,1020,510,210,510,300,10200,1150,-130,1050,-30,980
2023,Q1,Feb,2,DE,Alpha,Online,Haircare,900,450,185,450,265,9000,1010,-110,880,20,840
2023,Q1,Feb,2,DE,Gamma,B2B,Bodycare,680,340,136,340,204,6800,760,-80,650,30,630
2023,Q1,Feb,2,FR,Beta,Retail,Skincare,810,405,162,405,243,8100,910,-100,790,20,760
2023,Q1,Mar,3,UK,Alpha,Online,Haircare,1300,715,325,585,390,13000,1450,-150,1250,50,1180
2023,Q1,Mar,3,UK,Beta,Retail,Skincare,1060,530,218,530,312,10600,1200,-140,1100,-40,1010
2023,Q1,Mar,3,DE,Alpha,Online,Haircare,930,465,191,465,274,9300,1040,-110,910,20,860
2023,Q1,Mar,3,DE,Gamma,B2B,Bodycare,700,350,140,350,210,7000,790,-90,670,30,650
2023,Q1,Mar,3,FR,Beta,Retail,Skincare,840,420,168,420,252,8400,945,-105,820,20,780
2023,Q2,Apr,4,UK,Alpha,Online,Haircare,1320,726,330,594,396,13200,1480,-160,1280,40,1200
2023,Q2,Apr,4,UK,Beta,Retail,Skincare,1080,540,222,540,318,10800,1220,-140,1120,-40,1030
2023,Q2,Apr,4,DE,Alpha,Online,Haircare,950,475,195,475,280,9500,1060,-110,930,20,880
2023,Q2,Apr,4,DE,Gamma,B2B,Bodycare,720,360,144,360,216,7200,810,-90,690,30,670
2023,Q2,Apr,4,FR,Beta,Retail,Skincare,860,430,172,430,258,8600,965,-105,840,20,800
2023,Q2,May,5,UK,Alpha,Online,Haircare,1350,743,338,608,405,13500,1510,-160,1300,50,1220
2023,Q2,May,5,UK,Beta,Retail,Skincare,1100,550,226,550,324,11000,1240,-140,1140,-40,1050
2023,Q2,May,5,DE,Alpha,Online,Haircare,970,485,199,485,286,9700,1080,-110,950,20,900
2023,Q2,May,5,DE,Gamma,B2B,Bodycare,740,370,148,370,222,7400,830,-90,710,30,690
2023,Q2,May,5,FR,Beta,Retail,Skincare,880,440,176,440,264,8800,990,-110,860,20,820
2023,Q2,Jun,6,UK,Alpha,Online,Haircare,1380,759,345,621,414,13800,1540,-160,1320,60,1250
2023,Q2,Jun,6,UK,Beta,Retail,Skincare,1120,560,230,560,330,11200,1260,-140,1160,-40,1070
2023,Q2,Jun,6,DE,Alpha,Online,Haircare,990,495,203,495,292,9900,1100,-110,970,20,920
2023,Q2,Jun,6,DE,Gamma,B2B,Bodycare,760,380,152,380,228,7600,850,-90,730,30,710
2023,Q2,Jun,6,FR,Beta,Retail,Skincare,900,450,180,450,270,9000,1010,-110,880,20,840
2024,Q1,Jan,1,UK,Alpha,Online,Haircare,1380,759,345,621,414,13800,1540,-160,1350,30,1200
2024,Q1,Jan,1,UK,Beta,Retail,Skincare,1100,550,226,550,324,11000,1240,-140,1120,-20,980
2024,Q1,Jan,1,DE,Alpha,Online,Haircare,1010,505,207,505,298,10100,1130,-120,980,30,870
2024,Q1,Jan,1,DE,Gamma,B2B,Bodycare,760,380,152,380,228,7600,850,-90,730,30,650
2024,Q1,Jan,1,FR,Beta,Retail,Skincare,920,460,184,460,276,9200,1030,-110,890,30,780
2024,Q1,Feb,2,UK,Alpha,Online,Haircare,1420,781,355,639,426,14200,1580,-160,1390,30,1250
2024,Q1,Feb,2,UK,Beta,Retail,Skincare,1140,570,234,570,336,11400,1280,-140,1160,-20,1020
2024,Q1,Feb,2,DE,Alpha,Online,Haircare,1040,520,213,520,307,10400,1160,-120,1010,30,900
2024,Q1,Feb,2,DE,Gamma,B2B,Bodycare,790,395,158,395,237,7900,885,-95,760,30,680
2024,Q1,Feb,2,FR,Beta,Retail,Skincare,950,475,190,475,285,9500,1065,-115,920,30,810
2024,Q1,Mar,3,UK,Alpha,Online,Haircare,1460,803,365,657,438,14600,1620,-160,1430,30,1300
2024,Q1,Mar,3,UK,Beta,Retail,Skincare,1180,590,242,590,348,11800,1320,-140,1200,-20,1060
2024,Q1,Mar,3,DE,Alpha,Online,Haircare,1070,535,219,535,316,10700,1190,-120,1040,30,930
2024,Q1,Mar,3,DE,Gamma,B2B,Bodycare,820,410,164,410,246,8200,920,-100,790,30,700
2024,Q1,Mar,3,FR,Beta,Retail,Skincare,980,490,196,490,294,9800,1100,-120,950,30,840
2024,Q2,Apr,4,UK,Alpha,Online,Haircare,1490,820,373,671,447,14900,1650,-160,1460,30,1320
2024,Q2,Apr,4,UK,Beta,Retail,Skincare,1200,600,246,600,354,12000,1350,-150,1220,-20,1080
2024,Q2,Apr,4,DE,Alpha,Online,Haircare,1090,545,223,545,322,10900,1210,-120,1060,30,950
2024,Q2,Apr,4,DE,Gamma,B2B,Bodycare,840,420,168,420,252,8400,940,-100,810,30,720
2024,Q2,Apr,4,FR,Beta,Retail,Skincare,1000,500,200,500,300,10000,1120,-120,970,30,860
2024,Q2,May,5,UK,Alpha,Online,Haircare,1520,836,380,684,456,15200,1680,-160,1490,30,1350
2024,Q2,May,5,UK,Beta,Retail,Skincare,1230,615,252,615,363,12300,1380,-150,1250,-20,1100
2024,Q2,May,5,DE,Alpha,Online,Haircare,1110,555,227,555,328,11100,1230,-120,1080,30,970
2024,Q2,May,5,DE,Gamma,B2B,Bodycare,860,430,172,430,258,8600,960,-100,830,30,740
2024,Q2,May,5,FR,Beta,Retail,Skincare,1020,510,204,510,306,10200,1140,-120,990,30,880
2024,Q2,Jun,6,UK,Alpha,Online,Haircare,1550,853,388,698,465,15500,1710,-160,1520,30,1380
2024,Q2,Jun,6,UK,Beta,Retail,Skincare,1260,630,258,630,372,12600,1410,-150,1280,-20,1120
2024,Q2,Jun,6,DE,Alpha,Online,Haircare,1130,565,231,565,334,11300,1250,-120,1100,30,990
2024,Q2,Jun,6,DE,Gamma,B2B,Bodycare,880,440,176,440,264,8800,980,-100,850,30,760
2024,Q2,Jun,6,FR,Beta,Retail,Skincare,1040,520,208,520,312,10400,1160,-120,1010,30,900
"""

SAMPLE_BUDGET_CSV = """Period,Category,Actual,Budget,Prior_Year
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
Aug-2024,OPEX,876,900,860
Sep-2024,OPEX,930,940,884
Oct-2024,OPEX,960,960,900
Nov-2024,OPEX,990,980,920
Dec-2024,OPEX,1020,1000,950
"""

SAMPLE_RECON_A_CSV = """Invoice_ID,Vendor,Amount_ERP,Date
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
INV-014,Supplier B,12750.00,2024-02-08
INV-015,Supplier E,7400.00,2024-02-10
"""

SAMPLE_RECON_B_CSV = """Invoice_ID,Vendor,Amount_Bank,Date
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
INV-014,Supplier B,12750.00,2024-02-09
INV-015,Supplier E,7400.00,2024-02-11
INV-016,Supplier F,3900.00,2024-02-14
"""

SAMPLE_COST_CSV = """Period,SKU,Market,Revenue,COGS,OPEX
Jan-2024,SKU-A,UK,4200,1890,840
Jan-2024,SKU-B,UK,3100,1550,620
Jan-2024,SKU-C,DE,2800,1540,560
Jan-2024,SKU-D,DE,1900,1140,380
Jan-2024,SKU-E,FR,2200,990,440
Feb-2024,SKU-A,UK,4350,1958,870
Feb-2024,SKU-B,UK,3200,1760,640
Feb-2024,SKU-C,DE,2900,1595,580
Feb-2024,SKU-D,DE,1950,1170,390
Feb-2024,SKU-E,FR,2280,1026,456
Mar-2024,SKU-A,UK,4500,2025,900
Mar-2024,SKU-B,UK,3300,1815,660
Mar-2024,SKU-C,DE,3000,1650,600
Mar-2024,SKU-D,DE,2000,1200,400
Mar-2024,SKU-E,FR,2350,1058,470
Apr-2024,SKU-A,UK,4600,2070,920
Apr-2024,SKU-B,UK,3350,1843,670
Apr-2024,SKU-C,DE,3050,1678,610
Apr-2024,SKU-D,DE,2050,1230,410
Apr-2024,SKU-E,FR,2400,1080,480
May-2024,SKU-A,UK,4480,2016,896
May-2024,SKU-B,UK,3280,1804,656
May-2024,SKU-C,DE,2980,1639,596
May-2024,SKU-D,DE,2020,1212,404
May-2024,SKU-E,FR,2350,1058,470
Jun-2024,SKU-A,UK,4350,1958,870
Jun-2024,SKU-B,UK,3180,1749,636
Jun-2024,SKU-C,DE,2900,1595,580
Jun-2024,SKU-D,DE,1980,1188,396
Jun-2024,SKU-E,FR,2290,1031,458
"""


# ══════════════════════════════════════════════════════════════════════════════
# HOME — MODULE SELECTOR
# ══════════════════════════════════════════════════════════════════════════════
def show_home():
    st.markdown("""
<div style="text-align:center;padding:40px 20px 24px;">
  <div class="fin-title">Fincy Intelligence</div>
  <div class="fin-sub">AI-POWERED CFO DECISION PLATFORM · SELECT A MODULE</div>
  <div style="font-size:0.78rem;color:#5a5648;margin-top:6px;font-family:'IBM Plex Mono',monospace;">By Jitendra Parida · Senior FP&amp;A Analyst</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""
<div class="mod-grid">
  <div class="mod-sel" style="--mc:#c9a84c">
    <div class="mod-sel-icon">📊</div>
    <div class="mod-sel-title">FP&amp;A Intelligence</div>
    <div class="mod-sel-desc">Instant P&amp;L dashboards, variance analysis, AI CFO chat, and board-ready PDF reports from any CSV — in under 60 seconds.</div>
    <div class="mod-sel-badge">Core Module</div>
  </div>
  <div class="mod-sel" style="--mc:#4ade80">
    <div class="mod-sel-icon">🔁</div>
    <div class="mod-sel-title">Reconciliation Engine</div>
    <div class="mod-sel-desc">Upload ERP vs Bank, GL vs Sub-ledger, or PO vs Invoice. Auto-match, flag breaks, and download exceptions in seconds.</div>
    <div class="mod-sel-badge">New</div>
  </div>
  <div class="mod-sel" style="--mc:#fbbf24">
    <div class="mod-sel-icon">🎯</div>
    <div class="mod-sel-title">Budget vs Actuals Tracker</div>
    <div class="mod-sel-desc">RAG-status tracker with prior year overlays, trend detection, and AI-generated board commentary in minutes.</div>
    <div class="mod-sel-badge">New</div>
  </div>
  <div class="mod-sel" style="--mc:#f472b6">
    <div class="mod-sel-icon">💡</div>
    <div class="mod-sel-title">Cost Intelligence</div>
    <div class="mod-sel-desc">COGS and OPEX benchmarking with segment efficiency scores and AI-driven cost reduction recommendations.</div>
    <div class="mod-sel-badge">New</div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("📊 FP&A Intelligence", use_container_width=True):
            st.session_state.active_module = "fpa"; st.rerun()
    with c2:
        if st.button("🔁 Reconciliation", use_container_width=True):
            st.session_state.active_module = "recon"; st.rerun()
    with c3:
        if st.button("🎯 Budget Tracker", use_container_width=True):
            st.session_state.active_module = "budget"; st.rerun()
    with c4:
        if st.button("💡 Cost Intelligence", use_container_width=True):
            st.session_state.active_module = "cost"; st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1: FP&A INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_fpa():
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="fin-title" style="font-size:1.4rem;">📊 FP&A</div>', unsafe_allow_html=True)
        st.markdown('<div class="fin-sub">P&L · VARIANCE · AI CFO</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True):
            for k in ["df_raw","col_map","mapping_confirmed","chat_history"]:
                st.session_state.pop(k,None)
            st.session_state.active_module=None; st.rerun()
        if "df_raw" in st.session_state:
            if st.button("🔄 Upload New Data", use_container_width=True):
                for k in ["df_raw","col_map","mapping_confirmed","chat_history"]:
                    st.session_state.pop(k,None)
                st.rerun()

    # Upload
    if "df_raw" not in st.session_state:
        st.markdown("""
<div style="text-align:center;padding:48px 20px;">
  <div class="fin-title">FP&amp;A Intelligence</div>
  <div class="fin-sub" style="margin-top:8px;">UPLOAD YOUR P&amp;L DATA TO BEGIN</div>
</div>""", unsafe_allow_html=True)
        cl,cc,cr = st.columns([1,2,1])
        with cc:
            uploaded = st.file_uploader("📂 Upload Financial Data (CSV)", type=["csv"],
                help="Upload any P&L CSV. You'll map your columns in the next step.")
            st.markdown("<div style='text-align:center;margin:12px 0;font-size:0.72rem;color:#5a5648;font-family:\"IBM Plex Mono\",monospace;'>— OR —</div>", unsafe_allow_html=True)
            use_sample = st.button("📊 Use FMCG Sample Data", use_container_width=True)

        if use_sample:
            st.session_state.df_raw = pd.read_csv(io.StringIO(SAMPLE_FMCG_CSV))
            st.session_state.mapping_confirmed = False; st.rerun()
        if uploaded:
            st.session_state.df_raw = pd.read_csv(uploaded)
            st.session_state.mapping_confirmed = False; st.rerun()
        st.stop()

    df_raw = st.session_state.df_raw

    # Column mapping
    if not st.session_state.mapping_confirmed:
        st.markdown('<div style="text-align:center;padding:20px 0 10px;"><div class="fin-title" style="font-size:1.6rem;">Map Your Columns</div><div class="fin-sub" style="margin-top:6px;">STEP 2 OF 2 · MATCH CSV COLUMNS TO FINCY METRICS</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="mapper-box"><div style="font-size:0.78rem;color:#a09880;">Match your CSV columns to the metrics Fincy needs.<br><span style="color:#f87171;">★ Required</span> &nbsp;|&nbsp; <span style="color:#5a5648;">○ Optional (enables richer analysis)</span></div></div>', unsafe_allow_html=True)
        csv_cols = ["— skip —"] + list(df_raw.columns)
        col_map = {}
        st.markdown("**★ Financial Metrics (Required)**")
        r1,r2,r3 = st.columns(3)
        for i,(key,label) in enumerate(REQUIRED_COLS.items()):
            col=[r1,r2,r3][i%3]
            with col:
                guess = next((c for c in df_raw.columns if key.lower().replace("_","") in c.lower().replace("_","")), "— skip —")
                di = csv_cols.index(guess) if guess in csv_cols else 0
                col_map[key] = st.selectbox(f"★ {label}", csv_cols, index=di, key=f"map_{key}")
        st.markdown("**○ Dimensions (Optional but recommended)**")
        d1,d2,d3 = st.columns(3)
        for i,(key,label) in enumerate(OPTIONAL_DIMS.items()):
            col=[d1,d2,d3][i%3]
            with col:
                guess = next((c for c in df_raw.columns if key.lower() in c.lower()), "— skip —")
                di = csv_cols.index(guess) if guess in csv_cols else 0
                col_map[key] = st.selectbox(f"○ {label}", csv_cols, index=di, key=f"map_{key}")
        if st.button("✅ Confirm Mapping & Launch Dashboard", use_container_width=True):
            st.session_state.col_map = col_map
            st.session_state.mapping_confirmed = True; st.rerun()
        st.stop()

    # Apply mapping and filters
    col_map = st.session_state.col_map
    rename = {v:k for k,v in col_map.items() if v and v!="— skip —"}
    df_mapped = df_raw.rename(columns=rename)

    with st.sidebar:
        def filt(label,key):
            if key in col_map and col_map[key]!="— skip —" and key in df_mapped.columns:
                opts=["All"]+sorted(df_mapped[key].dropna().unique().tolist())
                return st.selectbox(label,opts)
            return "All"
        st.markdown("### Filters")
        fy=filt("🗓️ Year","Year"); fq=filt("📊 Quarter","Quarter"); fm=filt("🌍 Market","Market")
        fc=filt("🏷️ Category","Category"); fb=filt("💎 Brand","Brand")
        fch=filt("🛒 Channel","Channel"); ft=filt("📄 Type","Type")
        st.markdown("---")
        st.markdown("### 💬 Ask the AI CFO")
        st.caption("Powered by Groq · Llama 3.1")
        question = st.text_input("", placeholder="e.g. Why is margin declining?")
        c1,c2=st.columns([2,1])
        with c1: ask_btn=st.button("🚀 Ask CFO",use_container_width=True)
        with c2: clear_btn=st.button("🧹 Clear",use_container_width=True)
        if clear_btn: st.session_state.chat_history=[]

    df=df_mapped.copy()
    if fy!="All" and "Year" in df.columns: df=df[df["Year"]==int(fy)]
    if fq!="All" and "Quarter" in df.columns: df=df[df["Quarter"]==fq]
    if fm!="All" and "Market" in df.columns: df=df[df["Market"]==fm]
    if fc!="All" and "Category" in df.columns: df=df[df["Category"]==fc]
    if fb!="All" and "Brand" in df.columns: df=df[df["Brand"]==fb]
    if fch!="All" and "Channel" in df.columns: df=df[df["Channel"]==fch]
    if ft!="All" and "Type" in df.columns: df=df[df["Type"]==ft]

    if df.empty: st.warning("No data for selected filters."); st.stop()

    def s(col): return safe_col(df,col).sum()
    nr=s("Net_Revenue"); gp=s("Gross_Profit"); ebitda=s("EBITDA"); cogs=s("COGS"); opex=s("OPEX")
    vol=s("Volume_Units"); base_nr=s("Base_NR"); trade=s("Trade_Promo")
    bdgt=s("Budget_NR"); var_nr=s("Variance_NR"); py=s("PY_NR")
    gpm=gp/nr*100 if nr else 0; ebitdam=ebitda/nr*100 if nr else 0
    cogsp=cogs/nr*100 if nr else 0; opexp=opex/nr*100 if nr else 0
    tradep=trade/base_nr*100 if base_nr else 0
    yoy=(nr-py)/py*100 if py else 0; bach=nr/bdgt*100 if bdgt else 0
    varp=var_nr/bdgt*100 if bdgt else 0

    top_market=df.groupby("Market")["Net_Revenue"].sum().idxmax() if "Market" in df.columns and not df.empty else "N/A"
    top_brand=df.groupby("Brand")["Net_Revenue"].sum().idxmax() if "Brand" in df.columns and not df.empty else "N/A"
    risk_mkt=df.groupby("Market")["Variance_NR"].sum().idxmin() if "Market" in df.columns and "Variance_NR" in df.columns and not df.empty else "N/A"

    st.markdown('<div style="text-align:center;margin-bottom:20px;"><div class="fin-title" style="font-size:1.5rem;">FP&amp;A Intelligence</div><div class="fin-sub">REAL-TIME P&amp;L PERFORMANCE · AI-POWERED</div></div>', unsafe_allow_html=True)

    arrow="▲" if yoy>0 else "▼"
    st.markdown('<div class="sec-label">P&L Headline</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card" style="--ac:#c9a84c"><div class="kpi-label">Net Revenue</div><div class="kpi-value">{fmt_m(nr)}</div><div class="kpi-delta {dc(yoy)}">{arrow} {abs(yoy):.1f}% YoY</div></div>
  <div class="kpi-card" style="--ac:#4ade80"><div class="kpi-label">Gross Profit</div><div class="kpi-value">{fmt_m(gp)}</div><div class="kpi-delta {dc(gpm-50)}">GP Margin {gpm:.1f}%</div></div>
  <div class="kpi-card" style="--ac:#818cf8"><div class="kpi-label">EBITDA</div><div class="kpi-value">{fmt_m(ebitda)}</div><div class="kpi-delta {dc(ebitdam-30)}">Margin {ebitdam:.1f}%</div></div>
  <div class="kpi-card" style="--ac:#fb923c"><div class="kpi-label">COGS</div><div class="kpi-value">{fmt_m(cogs)}</div><div class="kpi-delta {'neg' if cogsp>55 else 'pos'}">COGS% {cogsp:.1f}%</div></div>
  <div class="kpi-card" style="--ac:#f472b6"><div class="kpi-label">OPEX</div><div class="kpi-value">{fmt_m(opex)}</div><div class="kpi-delta {'neg' if opexp>20 else 'pos'}">OPEX% {opexp:.1f}%</div></div>
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-label">Commercial Performance</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="kpi-grid-2">
  <div class="kpi-card" style="--ac:#fbbf24"><div class="kpi-label">Volume Units</div><div class="kpi-value">{vol/1000:,.0f}K</div><div class="kpi-delta neu">Total units</div></div>
  <div class="kpi-card" style="--ac:#2dd4bf"><div class="kpi-label">Budget Achievement</div><div class="kpi-value">{bach:.1f}%</div><div class="kpi-delta {dc(bach-100)}">vs {fmt_m(bdgt)}</div></div>
  <div class="kpi-card" style="--ac:#a78bfa"><div class="kpi-label">NR Variance</div><div class="kpi-value">{fmt_m(var_nr)}</div><div class="kpi-delta {dc(var_nr)}">{varp:+.1f}% vs budget</div></div>
  <div class="kpi-card" style="--ac:#f87171"><div class="kpi-label">Trade Promo</div><div class="kpi-value">{fmt_m(trade)}</div><div class="kpi-delta {'neg' if tradep>10 else 'pos'}">TPR {tradep:.1f}%</div></div>
  <div class="kpi-card" style="--ac:#c9a84c"><div class="kpi-label">YoY Growth</div><div class="kpi-value">{yoy:+.1f}%</div><div class="kpi-delta {dc(yoy)}">PY {fmt_m(py)}</div></div>
</div>""", unsafe_allow_html=True)

    # Charts
    st.markdown('<div class="sec-label">Revenue & Profit Breakdown</div>', unsafe_allow_html=True)
    c1,c2,c3=st.columns([2,2,1.5])
    with c1:
        if "Market" in df.columns:
            rm=df.groupby("Market")[["Net_Revenue","Gross_Profit","EBITDA"]].sum().reset_index()
            fig=go.Figure()
            for col,color,name in zip(["Net_Revenue","Gross_Profit","EBITDA"],["#c9a84c","#4ade80","#818cf8"],["Net Revenue","Gross Profit","EBITDA"]):
                if col in rm.columns: fig.add_bar(x=rm["Market"],y=rm[col],name=name,marker_color=color)
            fig.update_layout(**PLOTLY_BASE,title="P&L by Market",barmode="group",height=280,xaxis=AXIS,yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)
    with c2:
        if "Category" in df.columns and "Net_Revenue" in df.columns:
            rc=df.groupby("Category")["Net_Revenue"].sum().reset_index().sort_values("Net_Revenue",ascending=True)
            fig=go.Figure(go.Bar(x=rc["Net_Revenue"],y=rc["Category"],orientation="h",
                marker_color=PALETTE[:len(rc)],text=rc["Net_Revenue"].apply(fmt_m),textposition="auto"))
            fig.update_layout(**PLOTLY_BASE,title="Revenue by Category",height=280,xaxis=AXIS,yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)
    with c3:
        wfall={"Base NR":base_nr,"Trade Promo":-trade,"Net Revenue":nr,"COGS":-cogs,"Gross Profit":gp,"OPEX":-opex,"EBITDA":ebitda}
        fig=go.Figure(go.Bar(x=list(wfall.keys()),y=list(wfall.values()),
            marker_color=["#c9a84c" if v>0 else "#f87171" for v in wfall.values()]))
        fig.update_layout(**PLOTLY_BASE,title="P&L Bridge",height=280,xaxis=dict(tickangle=-30,**AXIS),yaxis=AXIS)
        st.plotly_chart(fig,use_container_width=True)

    st.markdown('<div class="sec-label">Trend & Mix Analysis</div>', unsafe_allow_html=True)
    c4,c5=st.columns([3,2])
    with c4:
        if all(c in df.columns for c in ["Year","Month_Num","Month","Net_Revenue"]):
            trend=df.groupby(["Year","Month_Num","Month"])[[c for c in ["Net_Revenue","Gross_Profit","EBITDA"] if c in df.columns]].sum().reset_index().sort_values(["Year","Month_Num"])
            trend["Period"]=trend["Year"].astype(str)+"-"+trend["Month"]
            fig=go.Figure()
            for col,color,name in zip(["Net_Revenue","Gross_Profit","EBITDA"],["#c9a84c","#4ade80","#818cf8"],["Net Revenue","Gross Profit","EBITDA"]):
                if col in trend.columns: fig.add_scatter(x=trend["Period"],y=trend[col],mode="lines",name=name,line=dict(color=color,width=2))
            fig.update_layout(**PLOTLY_BASE,title="Monthly Trend: Revenue → EBITDA",height=280,xaxis=dict(tickangle=-45,nticks=12,**AXIS),yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)
    with c5:
        if "Channel" in df.columns and "Net_Revenue" in df.columns:
            ch=df.groupby("Channel")["Net_Revenue"].sum().reset_index()
            fig=go.Figure(go.Pie(labels=ch["Channel"],values=ch["Net_Revenue"],hole=0.55,
                marker=dict(colors=PALETTE,line=dict(color="#0a0a08",width=2)),textinfo="label+percent",textfont=dict(size=9)))
            fig.update_layout(**PLOTLY_BASE,title="Revenue Mix by Channel",height=280,showlegend=False)
            st.plotly_chart(fig,use_container_width=True)

    # Board commentary
    st.markdown('<div class="sec-label">Board Commentary</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="box">
  <strong>Executive Summary</strong><br>
  Net Revenue stands at <strong>{fmt_m(nr)}</strong> with YoY growth of <strong>{yoy:+.1f}%</strong> against PY base of {fmt_m(py)}.
  Budget achievement is <strong>{bach:.1f}%</strong> with NR variance of <strong>{fmt_m(var_nr)}</strong>.<br><br>
  <strong>Profitability</strong><br>
  GP Margin of <strong>{gpm:.1f}%</strong> {'exceeds' if gpm>50 else 'is below'} the 50% benchmark.
  EBITDA Margin at <strong>{ebitdam:.1f}%</strong>. COGS at {cogsp:.1f}% NR; OPEX at {opexp:.1f}% NR. Trade Promo intensity {tradep:.1f}%.<br><br>
  <strong>Market &amp; Brand</strong><br>
  <strong>{top_market}</strong> is the top-performing market. <strong>{top_brand}</strong> leads brand revenue.
  <strong>{risk_mkt}</strong> shows the highest budget shortfall — requires corrective action.<br><br>
  <strong>Actions</strong><br>
  1. Review trade promo ROI in underperforming markets.&nbsp;
  2. Accelerate online channel growth — highest-margin channel.&nbsp;
  3. Tighten OPEX in markets below EBITDA threshold.
</div>""", unsafe_allow_html=True)

    # AI CFO
    if st.session_state.chat_history:
        st.markdown("### 💬 CFO Chat History")
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f'<div class="box" style="margin-bottom:10px;"><b>You:</b> {chat["question"]}<br><br><b>AI CFO:</b><br>{chat["answer"]}</div>', unsafe_allow_html=True)

    if ask_btn and question:
        st.markdown("### 🤖 AI CFO")
        with st.spinner("AI CFO is thinking..."):
            try:
                from groq import Groq
                api_key=os.getenv("GROQ_API_KEY")
                if not api_key:
                    ai_ans="⚠️ No GROQ_API_KEY found. Set it in Streamlit secrets."
                else:
                    client=Groq(api_key=api_key)
                    prompt=f"""You are a world-class CFO. Be concise and incisive.
KPIs: NR={fmt_m(nr)} YoY={yoy:.1f}% | GP={fmt_m(gp)} GPM={gpm:.1f}% | EBITDA={fmt_m(ebitda)} Margin={ebitdam:.1f}%
COGS={cogsp:.1f}%NR | OPEX={opexp:.1f}%NR | Budget Ach={bach:.1f}% | Variance={fmt_m(var_nr)}
Trade Promo={tradep:.1f}% | Top Market={top_market} | Risk Market={risk_mkt} | Top Brand={top_brand}
Question: {question}
Give 2-3 CFO-level insights with recommended actions."""
                    chat=client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role":"user","content":prompt}],temperature=0.3)
                    ai_ans=chat.choices[0].message.content
            except Exception as e:
                ai_ans=f"Error: {e}"
        st.markdown(f'<div class="ai-box">{ai_ans}</div>', unsafe_allow_html=True)
        st.session_state.chat_history.append({"question":question,"answer":ai_ans})
        pdf=generate_pdf(ai_ans)
        st.download_button("📄 Download CFO Report (PDF)", data=pdf, file_name="Fincy_CFO_Report.pdf", mime="application/pdf")
    elif not ask_btn:
        st.markdown('<div class="box" style="opacity:0.5;font-size:0.74rem;">← Type a question in the sidebar and click Ask CFO. Try: revenue, margin, variance, budget, growth, top market, risk</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2: RECONCILIATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
def run_recon():
    with st.sidebar:
        st.markdown('<div class="fin-title" style="font-size:1.4rem;color:#4ade80;">🔁 Recon</div>', unsafe_allow_html=True)
        st.markdown('<div class="fin-sub">MATCH · BREAK · EXCEPTIONS</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True):
            st.session_state.active_module=None; st.rerun()
        tolerance=st.number_input("Amount Tolerance (±)", min_value=0.0, value=0.01, step=0.01,
            help="Amounts within this range are treated as matched")

    st.markdown('<div style="text-align:center;padding:24px 0 16px;"><div class="fin-title" style="font-size:1.5rem;color:#4ade80;">🔁 Reconciliation Engine</div><div class="fin-sub" style="margin-top:6px;">UPLOAD TWO SOURCES · AUTO-MATCH · FLAG BREAKS · DOWNLOAD EXCEPTIONS</div></div>', unsafe_allow_html=True)

    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="sec-label">Source A (ERP / System 1)</div>', unsafe_allow_html=True)
        f1=st.file_uploader("Upload Source A (CSV)", type=["csv"], key="rf1")
        if st.button("📊 Use ERP Sample (Source A)", use_container_width=True, key="rs1"):
            st.session_state["recon_sample_a"]=True
    with c2:
        st.markdown('<div class="sec-label">Source B (Bank / System 2)</div>', unsafe_allow_html=True)
        f2=st.file_uploader("Upload Source B (CSV)", type=["csv"], key="rf2")
        if st.button("📊 Use Bank Sample (Source B)", use_container_width=True, key="rs2"):
            st.session_state["recon_sample_b"]=True

    use_a = st.session_state.get("recon_sample_a", False)
    use_b = st.session_state.get("recon_sample_b", False)

    df1 = pd.read_csv(io.StringIO(SAMPLE_RECON_A_CSV)) if (use_a and not f1) else (pd.read_csv(f1) if f1 else None)
    df2 = pd.read_csv(io.StringIO(SAMPLE_RECON_B_CSV)) if (use_b and not f2) else (pd.read_csv(f2) if f2 else None)

    if df1 is None or df2 is None:
        st.markdown("""
<div class="box" style="margin-top:20px;opacity:0.6;font-size:0.74rem;">
  ↑ Upload both files or click the sample data buttons above.<br><br>
  <strong>Use cases:</strong> ERP vs Bank · GL vs Sub-ledger · PO vs Invoice · Intercompany recon<br>
  <strong>Outputs:</strong> Match rate · Amount breaks · Missing records · Exceptions CSV
</div>""", unsafe_allow_html=True)
        return

    cols1,cols2=list(df1.columns),list(df2.columns)
    common=[c for c in cols1 if c in cols2]

    st.markdown('<div class="sec-label">Configure Match</div>', unsafe_allow_html=True)
    mc1,mc2,mc3=st.columns(3)
    with mc1:
        kg=next((c for c in common if any(k in c.lower() for k in ["id","no","number","ref","invoice"])), common[0] if common else cols1[0])
        match_key=st.selectbox("Match Key Column", common if common else cols1, index=common.index(kg) if kg in common else 0)
    with mc2:
        n1=[c for c in cols1 if pd.api.types.is_numeric_dtype(df1[c])]
        ag1=next((c for c in n1 if any(k in c.lower() for k in ["amount","amt","value","erp"])), n1[0] if n1 else cols1[0])
        amt1=st.selectbox("Amount Column (Source A)", n1 if n1 else cols1, index=n1.index(ag1) if ag1 in n1 else 0)
    with mc3:
        n2=[c for c in cols2 if pd.api.types.is_numeric_dtype(df2[c])]
        ag2=next((c for c in n2 if any(k in c.lower() for k in ["amount","amt","value","bank"])), n2[0] if n2 else cols2[0])
        amt2=st.selectbox("Amount Column (Source B)", n2 if n2 else cols2, index=n2.index(ag2) if ag2 in n2 else 0)

    if st.button("🔁 Run Reconciliation", use_container_width=True):
        merged=pd.merge(
            df1[[match_key,amt1]].rename(columns={amt1:"Amt_A"}),
            df2[[match_key,amt2]].rename(columns={amt2:"Amt_B"}),
            on=match_key, how="outer", indicator=True
        )
        def classify(r):
            if r["_merge"]=="left_only": return "Missing in B"
            if r["_merge"]=="right_only": return "Missing in A"
            return "Matched" if abs(r["Amt_A"]-r["Amt_B"])<=tolerance else "Amount Break"
        merged["Status"]=merged.apply(classify,axis=1)
        merged["Difference"]=merged["Amt_A"].fillna(0)-merged["Amt_B"].fillna(0)

        total=len(merged)
        matched=(merged["Status"]=="Matched").sum()
        breaks=(merged["Status"]=="Amount Break").sum()
        mb=(merged["Status"]=="Missing in B").sum()
        ma=(merged["Status"]=="Missing in A").sum()
        mrate=matched/total*100 if total else 0
        total_break=merged.loc[merged["Status"]=="Amount Break","Difference"].abs().sum()

        st.markdown('<div class="sec-label">Reconciliation Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="rag-row">
  <div class="rag-g"><div class="rag-lbl">Matched</div><div class="rag-val" style="color:#4ade80;">{matched:,}</div><div style="font-size:0.6rem;color:#4ade80;">{mrate:.1f}% match rate</div></div>
  <div class="rag-r"><div class="rag-lbl">Amount Breaks</div><div class="rag-val" style="color:#f87171;">{breaks:,}</div><div style="font-size:0.6rem;color:#f87171;">Diff: {total_break:,.2f}</div></div>
  <div class="rag-a"><div class="rag-lbl">Missing in B</div><div class="rag-val" style="color:#fbbf24;">{mb:,}</div><div style="font-size:0.6rem;color:#fbbf24;">In A only</div></div>
  <div class="rag-b"><div class="rag-lbl">Missing in A</div><div class="rag-val" style="color:#60a5fa;">{ma:,}</div><div style="font-size:0.6rem;color:#60a5fa;">In B only</div></div>
</div>""", unsafe_allow_html=True)

        ch1,ch2=st.columns([1,2])
        with ch1:
            fig=go.Figure(go.Pie(labels=["Matched","Amount Break","Missing in B","Missing in A"],
                values=[matched,breaks,mb,ma],hole=0.62,
                marker=dict(colors=["#4ade80","#f87171","#fbbf24","#60a5fa"],line=dict(color="#0a0a08",width=2)),
                textinfo="label+percent",textfont=dict(size=9)))
            fig.add_annotation(text=f"{mrate:.0f}%<br>Matched",x=0.5,y=0.5,showarrow=False,font=dict(size=14,color="#fafaf8",family="Playfair Display"))
            fig.update_layout(**PLOTLY_BASE,title="Recon Status",height=280,showlegend=False)
            st.plotly_chart(fig,use_container_width=True)
        with ch2:
            dbs=merged.groupby("Status")["Difference"].sum().reset_index()
            fig=go.Figure(go.Bar(x=dbs["Status"],y=dbs["Difference"],
                marker_color=["#4ade80" if v>=0 else "#f87171" for v in dbs["Difference"]],
                text=dbs["Difference"].apply(lambda x:f"{x:+,.2f}"),textposition="auto"))
            fig.update_layout(**PLOTLY_BASE,title="Net Difference by Status",height=280,xaxis=AXIS,yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)

        exc=merged[merged["Status"]!="Matched"].copy()
        if not exc.empty:
            st.markdown('<div class="sec-label">Exceptions Detail</div>', unsafe_allow_html=True)
            sf=st.multiselect("Filter Status",["Amount Break","Missing in B","Missing in A"],default=["Amount Break","Missing in B","Missing in A"])
            fe=exc[exc["Status"].isin(sf)]
            st.dataframe(fe.drop(columns=["_merge"]),use_container_width=True,hide_index=True)
            st.download_button("📥 Download Exceptions (CSV)", fe.drop(columns=["_merge"]).to_csv(index=False).encode(), "Fincy_Recon_Exceptions.csv", "text/csv")
        else:
            st.success("🎉 Perfect reconciliation — no exceptions found!")

        st.markdown('<div class="sec-label">Full Reconciliation Output</div>', unsafe_allow_html=True)
        st.dataframe(merged.drop(columns=["_merge"]),use_container_width=True,hide_index=True)
        st.download_button("📥 Download Full Recon Output (CSV)", merged.drop(columns=["_merge"]).to_csv(index=False).encode(), "Fincy_Recon_Full.csv", "text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3: BUDGET vs ACTUALS TRACKER
# ══════════════════════════════════════════════════════════════════════════════
def run_budget():
    with st.sidebar:
        st.markdown('<div class="fin-title" style="font-size:1.4rem;color:#fbbf24;">🎯 Budget Tracker</div>', unsafe_allow_html=True)
        st.markdown('<div class="fin-sub">RAG · VARIANCE · BOARD PACK</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True):
            st.session_state.active_module=None; st.rerun()
        green_t=st.slider("🟢 Green threshold (%)", 90, 100, 95)
        amber_t=st.slider("🟡 Amber threshold (%)", 70, 95, 80)

    st.markdown('<div style="text-align:center;padding:24px 0 16px;"><div class="fin-title" style="font-size:1.5rem;color:#fbbf24;">🎯 Budget vs Actuals Tracker</div><div class="fin-sub" style="margin-top:6px;">RAG STATUS · PRIOR YEAR · AI TREND ANALYSIS</div></div>', unsafe_allow_html=True)

    cl,cc,cr=st.columns([1,2,1])
    with cc:
        bfile=st.file_uploader("📂 Upload Budget vs Actuals CSV", type=["csv"], key="bfile",
            help="Needs Period, Actual, Budget columns. Prior Year optional.")
        if st.button("📊 Use Budget Sample Data", use_container_width=True, key="bsample"):
            st.session_state["budget_use_sample"]=True

    use_sample=st.session_state.get("budget_use_sample",False)
    df = pd.read_csv(io.StringIO(SAMPLE_BUDGET_CSV)) if (use_sample and not bfile) else (pd.read_csv(bfile) if bfile else None)

    if df is None:
        st.markdown("""
<div class="box" style="margin-top:20px;opacity:0.6;font-size:0.74rem;">
  ↑ Upload your Budget vs Actuals CSV or use the sample data button above.<br><br>
  <strong>Needs:</strong> Period column · Actual column · Budget column<br>
  <strong>Optional:</strong> Prior Year column · Dimension column (Category / Market / Brand)<br>
  <strong>Outputs:</strong> RAG status · YoY chart · AI trend analysis · Board commentary · CSV export
</div>""", unsafe_allow_html=True)
        return

    csv_cols=list(df.columns)
    st.markdown('<div class="sec-label">Map Columns</div>', unsafe_allow_html=True)
    bc1,bc2,bc3,bc4,bc5=st.columns(5)
    with bc1:
        pg=next((c for c in csv_cols if any(k in c.lower() for k in ["period","month","date","year","quarter"])), csv_cols[0])
        period_col=st.selectbox("Period Column", csv_cols, index=csv_cols.index(pg))
    with bc2:
        ag=next((c for c in csv_cols if any(k in c.lower() for k in ["actual","actuals","act"])), csv_cols[0])
        actual_col=st.selectbox("Actual Column", csv_cols, index=csv_cols.index(ag))
    with bc3:
        bg=next((c for c in csv_cols if any(k in c.lower() for k in ["budget","plan","target"])), csv_cols[0])
        budget_col=st.selectbox("Budget Column", csv_cols, index=csv_cols.index(bg))
    with bc4:
        py_opts=["— none —"]+csv_cols
        pyg=next((c for c in csv_cols if any(k in c.lower() for k in ["prior","previous","py","last","ly"])), "— none —")
        py_col=st.selectbox("Prior Year (optional)", py_opts, index=py_opts.index(pyg) if pyg in py_opts else 0)
    with bc5:
        dim_opts=["— none —"]+csv_cols
        dg=next((c for c in csv_cols if any(k in c.lower() for k in ["category","brand","market","segment","dept"])), "— none —")
        dim_col=st.selectbox("Dimension (optional)", dim_opts, index=dim_opts.index(dg) if dg in dim_opts else 0)

    if st.button("🎯 Run Budget Tracker", use_container_width=True):
        df["_A"]=pd.to_numeric(df[actual_col],errors="coerce").fillna(0)
        df["_B"]=pd.to_numeric(df[budget_col],errors="coerce").fillna(0)
        df["_V"]=df["_A"]-df["_B"]
        df["_VP"]=df.apply(lambda r:r["_V"]/r["_B"]*100 if r["_B"] else 0,axis=1)
        df["_AP"]=df.apply(lambda r:r["_A"]/r["_B"]*100 if r["_B"] else 0,axis=1)
        has_py=py_col!="— none —"
        if has_py:
            df["_PY"]=pd.to_numeric(df[py_col],errors="coerce").fillna(0)
            df["_YoY"]=df.apply(lambda r:(r["_A"]-r["_PY"])/r["_PY"]*100 if r["_PY"] else 0,axis=1)

        def rag(a): return "🟢 Green" if a>=green_t else ("🟡 Amber" if a>=amber_t else "🔴 Red")
        df["_RAG"]=df["_AP"].apply(rag)

        ta=df["_A"].sum(); tb=df["_B"].sum(); tv=ta-tb
        tach=ta/tb*100 if tb else 0
        tpy=df["_PY"].sum() if has_py else 0
        tyoy=(ta-tpy)/tpy*100 if has_py and tpy else 0
        gc=(df["_RAG"]=="🟢 Green").sum(); rc=(df["_RAG"]=="🔴 Red").sum(); ac=(df["_RAG"]=="🟡 Amber").sum()

        # Trend direction
        py_cols_list = ["_A","_B","_V","_PY"] if has_py else ["_A","_B","_V"]
        pg=df.groupby(period_col)[py_cols_list].sum().reset_index()
        trend_dir = "improving" if len(pg)>=3 and pg["_V"].iloc[-1]>pg["_V"].iloc[0] else "deteriorating"

        st.markdown('<div class="sec-label">Budget Performance Summary</div>', unsafe_allow_html=True)
        yoy_color = "#4ade80" if tyoy>=0 else "#f87171"
        yoy_class = "rag-g" if tyoy>=0 else "rag-r"
        yoy_cell = f'<div class="{yoy_class}"><div class="rag-lbl">YoY Growth</div><div class="rag-val" style="color:{yoy_color};">{tyoy:+.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">vs PY {fmt_m(tpy)}</div></div>' if has_py else ""
        st.markdown(f"""
<div class="rag-row">
  <div class="{'rag-g' if tv>=0 else 'rag-r'}"><div class="rag-lbl">Total Actual</div><div class="rag-val" style="color:{'#4ade80' if tv>=0 else '#f87171'};">{fmt_m(ta)}</div><div style="font-size:0.6rem;color:#5a5648;">vs Budget {fmt_m(tb)}</div></div>
  <div class="{'rag-g' if tv>=0 else 'rag-r'}"><div class="rag-lbl">Variance</div><div class="rag-val" style="color:{'#4ade80' if tv>=0 else '#f87171'};">{tv:+,.0f}</div><div style="font-size:0.6rem;color:{'#4ade80' if tv>=0 else '#f87171'};">{tach:.1f}% achieved</div></div>
  <div class="rag-g"><div class="rag-lbl">🟢 On Track</div><div class="rag-val" style="color:#4ade80;">{gc}</div><div style="font-size:0.6rem;color:#4ade80;">{ac} amber</div></div>
  <div class="rag-r"><div class="rag-lbl">🔴 Off Track</div><div class="rag-val" style="color:#f87171;">{rc}</div><div style="font-size:0.6rem;color:#5a5648;">lines</div></div>
</div>""", unsafe_allow_html=True)

        # Trend chart
        st.markdown('<div class="sec-label">Actual vs Budget vs Prior Year</div>', unsafe_allow_html=True)
        fig=go.Figure()
        fig.add_bar(x=pg[period_col],y=pg["_B"],name="Budget",marker_color="rgba(99,102,241,0.35)")
        fig.add_bar(x=pg[period_col],y=pg["_A"],name="Actual",marker_color="#c9a84c")
        if has_py and "_PY" in pg.columns:
            fig.add_scatter(x=pg[period_col],y=pg["_PY"],name="Prior Year",mode="lines+markers",
                line=dict(color="#fbbf24",width=2,dash="dash"),marker=dict(size=5))
        fig.add_scatter(x=pg[period_col],y=pg["_V"],name="Variance",mode="lines+markers",
            line=dict(color="#f87171",width=2,dash="dot"),yaxis="y2")
        fig.update_layout(**PLOTLY_BASE,title="Actual vs Budget vs Prior Year",barmode="overlay",height=340,
            xaxis=dict(tickangle=-30,**AXIS),yaxis=AXIS,
            yaxis2=dict(overlaying="y",side="right",gridcolor="#1a1a16",tickfont=dict(size=9),title_text="Variance"))
        st.plotly_chart(fig,use_container_width=True)

        # Dimension chart
        if dim_col!="— none —":
            st.markdown('<div class="sec-label">Variance by Dimension</div>', unsafe_allow_html=True)
            dg_data=df.groupby(dim_col)[["_A","_B","_V"]].sum().reset_index().sort_values("_V")
            fig=go.Figure(go.Bar(x=dg_data["_V"],y=dg_data[dim_col],orientation="h",
                marker_color=["#f87171" if v<0 else "#4ade80" for v in dg_data["_V"]],
                text=dg_data["_V"].apply(lambda x:f"{x:+,.0f}"),textposition="auto"))
            fig.update_layout(**PLOTLY_BASE,title=f"Variance by {dim_col}",height=280,xaxis=AXIS,yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)

        # RAG Table
        st.markdown('<div class="sec-label">Line-by-Line RAG Status</div>', unsafe_allow_html=True)
        dcols=[period_col,actual_col,budget_col,"_V","_VP","_AP","_RAG"]
        if has_py: dcols=[period_col,actual_col,budget_col,py_col,"_V","_VP","_AP","_YoY","_RAG"]
        if dim_col!="— none —": dcols=[period_col,dim_col]+dcols[1:]
        disp=df[[c for c in dcols if c in df.columns]].copy()
        disp.columns=[c.replace("_V","Variance").replace("_VP","Var%").replace("_AP","Achiev%").replace("_RAG","RAG").replace("_YoY","YoY%") for c in disp.columns]
        st.dataframe(disp,use_container_width=True,hide_index=True)

        # Board commentary
        top_over=pg.loc[pg["_V"].idxmax(),period_col]; top_under=pg.loc[pg["_V"].idxmin(),period_col]
        py_line=f" Against prior year, actuals are <strong>{tyoy:+.1f}%</strong> YoY (PY base {fmt_m(tpy)})." if has_py else ""
        st.markdown('<div class="sec-label">Board Commentary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="box">
  <strong>Budget Performance Summary</strong><br>
  Total actuals of <strong>{fmt_m(ta)}</strong> vs budget of <strong>{fmt_m(tb)}</strong> —
  {'favourable' if tv>=0 else 'adverse'} variance of <strong>{tv:+,.0f}</strong> ({tach:.1f}% achievement).{py_line}<br><br>
  <strong>RAG:</strong> {gc} Green · {ac} Amber · {rc} Red. Trend over latest periods: <strong>{trend_dir}</strong>.<br><br>
  <strong>Highlights:</strong> <strong>{top_over}</strong> strongest period vs budget. <strong>{top_under}</strong> largest shortfall — requires attention.<br><br>
  <strong>Actions:</strong><br>
  1. Investigate {top_under} — phasing issue or structural underperformance?<br>
  2. Replicate {top_over} success factors across underperforming periods.<br>
  3. Escalate all 🔴 Red lines to business owners for corrective action plans.
</div>""", unsafe_allow_html=True)

        # AI Deep Insights
        st.markdown('<div class="sec-label">🧠 AI CFO — Historical Trend Analysis</div>', unsafe_allow_html=True)
        if st.button("🧠 Get AI Budget Insights", use_container_width=True, key="bai"):
            try:
                from groq import Groq
                api_key=os.getenv("GROQ_API_KEY")
                if not api_key:
                    st.warning("⚠️ No GROQ_API_KEY. Set in Streamlit secrets.")
                else:
                    period_lines=[]
                    for _,row in pg.iterrows():
                        line=f"  {row[period_col]}: Actual={row['_A']:,.0f}, Budget={row['_B']:,.0f}, Var={row['_V']:+,.0f} ({row['_A']/row['_B']*100 if row['_B'] else 0:.1f}%)"
                        if has_py and "_PY" in row: line+=f", PY={row['_PY']:,.0f} (YoY {(row['_A']-row['_PY'])/row['_PY']*100 if row['_PY'] else 0:+.1f}%)"
                        period_lines.append(line)
                    last=pg.iloc[-1]; prev=pg.iloc[-2] if len(pg)>1 else None
                    mom=f"MoM: {last[period_col]} vs {prev[period_col]}: {last['_A']-prev['_A']:+,.0f}" if prev is not None else ""
                    prompt=f"""You are a CFO. Analyse this Budget vs Actuals data with historical trends.
SUMMARY: Actual={fmt_m(ta)} | Budget={fmt_m(tb)} | Var={tv:+,.0f} | Ach={tach:.1f}% | Trend={trend_dir}
{f"YoY={tyoy:+.1f}% vs PY={fmt_m(tpy)}" if has_py else ""}
{mom}
Best period: {top_over} | Worst: {top_under}

PERIOD-BY-PERIOD DATA:
{chr(10).join(period_lines)}

1. Key trends — are variances accelerating or decelerating?
2. Compare current vs prior year — growing or contracting?
3. Top 2-3 periods needing urgent CFO attention and why.
4. 3 specific actions to close the budget gap or sustain over-performance.
5. If deteriorating, early warning and corrective timeline.
Be concise, data-driven, CFO-level sharp. Use actual numbers."""
                    with st.spinner("AI CFO is analysing historical trends..."):
                        client=Groq(api_key=api_key)
                        chat=client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role":"user","content":prompt}],temperature=0.25)
                    st.markdown(f'<div class="ai-box">{chat.choices[0].message.content}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Groq error: {e}")
        else:
            st.markdown('<div class="box" style="opacity:0.5;font-size:0.72rem;">← Click to get AI analysis using your period data, prior year comparisons, and trend detection.</div>', unsafe_allow_html=True)

        st.download_button("📥 Download RAG Report (CSV)", disp.to_csv(index=False).encode(), "Fincy_Budget_RAG.csv", "text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 4: COST INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════════════
def run_cost():
    with st.sidebar:
        st.markdown('<div class="fin-title" style="font-size:1.4rem;color:#f472b6;">💡 Cost Intel</div>', unsafe_allow_html=True)
        st.markdown('<div class="fin-sub">COGS · OPEX · BENCHMARKS · AI</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🏠 Module Home", use_container_width=True):
            st.session_state.active_module=None; st.rerun()
        cogs_bench=st.slider("COGS Benchmark (% Rev)", 20, 80, 50)
        opex_bench=st.slider("OPEX Benchmark (% Rev)", 5, 40, 20)

    st.markdown('<div style="text-align:center;padding:24px 0 16px;"><div class="fin-title" style="font-size:1.5rem;color:#f472b6;">💡 Cost Intelligence</div><div class="fin-sub" style="margin-top:6px;">COGS · OPEX BENCHMARKING · AI COST REDUCTION</div></div>', unsafe_allow_html=True)

    cl,cc,cr=st.columns([1,2,1])
    with cc:
        cfile=st.file_uploader("📂 Upload Cost Data CSV", type=["csv"], key="cfile",
            help="CSV with Revenue, COGS, OPEX columns and optional Period/Segment")
        if st.button("📊 Use Cost Sample Data", use_container_width=True, key="csample"):
            st.session_state["cost_use_sample"]=True

    use_sample=st.session_state.get("cost_use_sample",False)
    df = pd.read_csv(io.StringIO(SAMPLE_COST_CSV)) if (use_sample and not cfile) else (pd.read_csv(cfile) if cfile else None)

    if df is None:
        st.markdown("""
<div class="box" style="margin-top:20px;opacity:0.6;font-size:0.74rem;">
  ↑ Upload your cost data CSV or use the sample data button above.<br><br>
  <strong>Needs:</strong> Revenue column · COGS column · OPEX column<br>
  <strong>Optional:</strong> Period column · Segment / SKU / Market column<br>
  <strong>Outputs:</strong> COGS% &amp; OPEX% vs benchmarks · Flagged lines · Cost waterfall · AI recommendations
</div>""", unsafe_allow_html=True)
        return

    csv_cols=list(df.columns)
    st.markdown('<div class="sec-label">Map Columns</div>', unsafe_allow_html=True)
    cc1,cc2,cc3,cc4,cc5=st.columns(5)
    with cc1:
        rg=next((c for c in csv_cols if any(k in c.lower() for k in ["revenue","net_rev","sales"])), csv_cols[0])
        rev_col=st.selectbox("Revenue", csv_cols, index=csv_cols.index(rg))
    with cc2:
        cg=next((c for c in csv_cols if "cog" in c.lower()), csv_cols[0])
        cogs_col=st.selectbox("COGS", csv_cols, index=csv_cols.index(cg))
    with cc3:
        og=next((c for c in csv_cols if "opex" in c.lower() or "operating" in c.lower()), csv_cols[0])
        opex_col=st.selectbox("OPEX", csv_cols, index=csv_cols.index(og))
    with cc4:
        ppg=next((c for c in csv_cols if any(k in c.lower() for k in ["period","month","date","year"])), csv_cols[0])
        period_col=st.selectbox("Period", csv_cols, index=csv_cols.index(ppg))
    with cc5:
        dim_opts=["— none —"]+csv_cols
        dg=next((c for c in csv_cols if any(k in c.lower() for k in ["sku","category","brand","market","segment","product"])), "— none —")
        dim_col=st.selectbox("Segment/SKU (optional)", dim_opts, index=dim_opts.index(dg) if dg in dim_opts else 0)

    if st.button("💡 Run Cost Intelligence", use_container_width=True):
        df["_R"]=pd.to_numeric(df[rev_col],errors="coerce").fillna(0)
        df["_C"]=pd.to_numeric(df[cogs_col],errors="coerce").fillna(0)
        df["_O"]=pd.to_numeric(df[opex_col],errors="coerce").fillna(0)
        df["_GP"]=df["_R"]-df["_C"]; df["_EB"]=df["_GP"]-df["_O"]
        df["_CP"]=df.apply(lambda r:r["_C"]/r["_R"]*100 if r["_R"] else 0,axis=1)
        df["_OP"]=df.apply(lambda r:r["_O"]/r["_R"]*100 if r["_R"] else 0,axis=1)
        df["_GPM"]=df.apply(lambda r:r["_GP"]/r["_R"]*100 if r["_R"] else 0,axis=1)
        df["_Flag"]=df.apply(lambda r:"⚠️ Above Bench" if r["_CP"]>cogs_bench or r["_OP"]>opex_bench else "✅ Within Bench",axis=1)

        tr=df["_R"].sum(); tc=df["_C"].sum(); to=df["_O"].sum()
        tgp=df["_GP"].sum(); teb=df["_EB"].sum()
        acp=tc/tr*100 if tr else 0; aop=to/tr*100 if tr else 0; agpm=tgp/tr*100 if tr else 0
        above=(df["_Flag"]=="⚠️ Above Bench").sum()

        st.markdown('<div class="sec-label">Cost Performance Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="rag-row">
  <div class="{'rag-g' if acp<=cogs_bench else 'rag-r'}"><div class="rag-lbl">COGS % Revenue</div><div class="rag-val" style="color:{'#4ade80' if acp<=cogs_bench else '#f87171'};">{acp:.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">Benchmark: {cogs_bench}%</div></div>
  <div class="{'rag-g' if aop<=opex_bench else 'rag-r'}"><div class="rag-lbl">OPEX % Revenue</div><div class="rag-val" style="color:{'#4ade80' if aop<=opex_bench else '#f87171'};">{aop:.1f}%</div><div style="font-size:0.6rem;color:#5a5648;">Benchmark: {opex_bench}%</div></div>
  <div class="rag-g"><div class="rag-lbl">GP Margin</div><div class="rag-val" style="color:#4ade80;">{agpm:.1f}%</div><div style="font-size:0.6rem;color:#4ade80;">Gross Profit</div></div>
  <div class="{'rag-r' if above>0 else 'rag-g'}"><div class="rag-lbl">Above Benchmark</div><div class="rag-val" style="color:{'#f87171' if above>0 else '#4ade80'};">{above}</div><div style="font-size:0.6rem;color:#5a5648;">lines flagged</div></div>
</div>""", unsafe_allow_html=True)

        # Cost trend chart
        st.markdown('<div class="sec-label">Cost Ratios Over Time</div>', unsafe_allow_html=True)
        ch1,ch2=st.columns(2)
        with ch1:
            pg=df.groupby(period_col)[["_R","_C","_O","_GP"]].sum().reset_index()
            pg["_CP"]=pg["_C"]/pg["_R"]*100; pg["_OP"]=pg["_O"]/pg["_R"]*100; pg["_GPM"]=pg["_GP"]/pg["_R"]*100
            fig=go.Figure()
            fig.add_scatter(x=pg[period_col],y=pg["_CP"],name="COGS %",mode="lines+markers",line=dict(color="#f87171",width=2))
            fig.add_scatter(x=pg[period_col],y=pg["_OP"],name="OPEX %",mode="lines+markers",line=dict(color="#fbbf24",width=2))
            fig.add_scatter(x=pg[period_col],y=pg["_GPM"],name="GP Margin %",mode="lines+markers",line=dict(color="#4ade80",width=2))
            fig.add_hline(y=cogs_bench,line_dash="dot",line_color="#f87171",annotation_text=f"COGS Bench {cogs_bench}%")
            fig.add_hline(y=opex_bench,line_dash="dot",line_color="#fbbf24",annotation_text=f"OPEX Bench {opex_bench}%")
            fig.update_layout(**PLOTLY_BASE,title="Cost Ratios Over Time",height=300,xaxis=dict(tickangle=-30,**AXIS),yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)
        with ch2:
            wf_data={"Revenue":tr,"COGS":-tc,"Gross Profit":tgp,"OPEX":-to,"EBITDA":teb}
            fig=go.Figure(go.Bar(x=list(wf_data.keys()),y=list(wf_data.values()),
                marker_color=["#c9a84c","#f87171","#4ade80","#fbbf24","#818cf8"]))
            fig.update_layout(**PLOTLY_BASE,title="Cost Waterfall",height=300,xaxis=AXIS,yaxis=AXIS)
            st.plotly_chart(fig,use_container_width=True)

        # Segment breakdown
        if dim_col!="— none —":
            st.markdown('<div class="sec-label">Cost Efficiency by Segment</div>', unsafe_allow_html=True)
            sg=df.groupby(dim_col)[["_R","_C","_O","_GP"]].sum().reset_index()
            sg["_CP"]=sg["_C"]/sg["_R"]*100; sg["_OP"]=sg["_O"]/sg["_R"]*100; sg["_GPM"]=sg["_GP"]/sg["_R"]*100
            sg=sg.sort_values("_GPM",ascending=False)
            fig=go.Figure()
            fig.add_bar(x=sg[dim_col],y=sg["_CP"],name="COGS %",marker_color="#f87171")
            fig.add_bar(x=sg[dim_col],y=sg["_OP"],name="OPEX %",marker_color="#fbbf24")
            fig.add_scatter(x=sg[dim_col],y=sg["_GPM"],name="GP Margin %",mode="lines+markers",
                line=dict(color="#4ade80",width=2),yaxis="y2")
            fig.add_hline(y=cogs_bench,line_dash="dot",line_color="#f87171")
            fig.update_layout(**PLOTLY_BASE,title=f"Cost Efficiency by {dim_col}",barmode="stack",height=300,
                xaxis=AXIS,yaxis=AXIS,yaxis2=dict(overlaying="y",side="right",gridcolor="#1a1a16",tickfont=dict(size=9)))
            st.plotly_chart(fig,use_container_width=True)

        # Flagged lines
        flagged=df[df["_Flag"]=="⚠️ Above Bench"]
        if not flagged.empty:
            st.markdown('<div class="sec-label">⚠️ Lines Above Benchmark</div>', unsafe_allow_html=True)
            show=[period_col,rev_col,cogs_col,opex_col,"_CP","_OP","_GPM","_Flag"]
            if dim_col!="— none —": show=[period_col,dim_col]+show[1:]
            st.dataframe(flagged[[c for c in show if c in flagged.columns]],use_container_width=True,hide_index=True)

        # AI Recommendations
        st.markdown('<div class="sec-label">🧠 AI Cost Reduction Recommendations</div>', unsafe_allow_html=True)
        worst_seg=""
        if dim_col!="— none —" and len(sg)>0:
            worst_seg=str(sg.loc[sg["_CP"].idxmax(),dim_col])
        if st.button("🧠 Get AI Cost Insights", use_container_width=True, key="cai"):
            try:
                from groq import Groq
                api_key=os.getenv("GROQ_API_KEY")
                if not api_key:
                    st.warning("⚠️ No GROQ_API_KEY. Set in Streamlit secrets.")
                else:
                    client=Groq(api_key=api_key)
                    prompt=f"""You are a CFO and cost management expert.
Cost Summary: Revenue={fmt_m(tr)} | COGS={fmt_m(tc)} ({acp:.1f}%, Bench {cogs_bench}%) | OPEX={fmt_m(to)} ({aop:.1f}%, Bench {opex_bench}%)
GP Margin={agpm:.1f}% | Lines above benchmark: {above} | Highest cost segment: {worst_seg or 'N/A'}
Provide 3 specific, actionable cost reduction recommendations with expected impact.
Focus on supply chain, procurement, and operational efficiency. Be concise and CFO-level sharp."""
                    with st.spinner("Analysing cost structure..."):
                        chat=client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role":"user","content":prompt}],temperature=0.3)
                    st.markdown(f'<div class="ai-box">{chat.choices[0].message.content}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Groq error: {e}")
        else:
            st.markdown('<div class="box" style="opacity:0.5;font-size:0.72rem;">← Click to get AI cost reduction recommendations based on your data.</div>', unsafe_allow_html=True)

        dl_cols=[c for c in [period_col,dim_col if dim_col!="— none —" else None,rev_col,cogs_col,opex_col,"_CP","_OP","_GPM","_Flag"] if c]
        st.download_button("📥 Download Cost Report (CSV)", df[[c for c in dl_cols if c in df.columns]].to_csv(index=False).encode(), "Fincy_Cost_Intelligence.csv", "text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════
mod = st.session_state.active_module

if mod is None:
    show_home()
elif mod == "fpa":
    run_fpa()
elif mod == "recon":
    run_recon()
elif mod == "budget":
    run_budget()
elif mod == "cost":
    run_cost()

st.markdown('<br><div style="text-align:center;font-family:\'IBM Plex Mono\',monospace;font-size:0.52rem;color:#242420;letter-spacing:0.14em;">FINCY INTELLIGENCE · AI CFO PLATFORM · BUILT BY JITENDRA PARIDA</div>', unsafe_allow_html=True)
