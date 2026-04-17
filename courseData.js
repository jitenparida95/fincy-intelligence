/* ============================================================
   FINCY LEARNING HUB — Course Data + Interactive Engine
   Version 2.0 | Vanilla JS | No frameworks | Groq AI
   ============================================================ */

'use strict';

/* ── COURSE DATA STRUCTURE ─────────────────────────────────── */
var FINCY_COURSE = {

  stages: [

    /* ═══════════════════════════════════════════════════════
       STAGE 01 — BEGINNER: AI in Finance Basics
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_01',
      badge: '01 / BEGINNER',
      color: '#c9a84c',
      title: 'AI in Finance Basics',
      tagline: 'Understand what AI is and why it changes everything for finance professionals.',
      unlocked: true,   // always open
      modules: [

        {
          id: 'm01_01',
          title: 'What is AI? (For Finance People)',
          lessons: [
            {
              id: 'l01_01_01',
              title: 'LLMs Explained in Finance Terms',
              explanation: 'A Large Language Model (LLM) like Llama or GPT is a system trained on billions of documents. It can read your question and generate a relevant, structured answer — like a very well-read analyst who never sleeps. In finance, this means you can ask "Why is EBITDA declining?" and get a CFO-level response in seconds.',
              example: 'You upload a P&L CSV to Fincy and ask: "Which market has the worst margin trend?" The LLM reads the data context and replies: "Germany — EBITDA margin fell from 18% to 11% in Q3, driven by COGS inflation (+7%) and flat volume." That is an LLM working for you.',
              task: 'In the box below, write one finance question you wish your team could answer faster. Then click Ask AI to see how an LLM responds.',
              ai_prompt: 'You are a senior FP&A analyst. The user is a finance professional learning about AI. They will ask a finance question. Answer it in 3-4 sentences as if you were their AI CFO — direct, with numbers, no fluff.',
              expected_output: 'A concise, professional finance answer with specific reasoning.'
            },
            {
              id: 'l01_01_02',
              title: 'AI Agents vs LLMs — What\'s the difference?',
              explanation: 'An LLM answers questions. An AI Agent takes actions. Fincy\'s Data Analysis Agent is an AI Agent — it reads your CSV, runs statistics, builds charts, and writes commentary without you telling it each step. Think of an LLM as a smart advisor and an Agent as a smart employee.',
              example: 'LLM: "Your DSO is high." Agent: reads your AR data → calculates DSO → flags customers over 60 days → generates a collections priority list → saves it to CSV. One click. Zero Excel.',
              task: 'Name one repetitive finance task in your job that takes more than 2 hours. Then ask AI how an agent could automate it.',
              ai_prompt: 'You are an AI automation expert for Finance teams. The user will describe a repetitive finance task. Explain step by step how an AI agent could automate it, with specific tools (Python, Pandas, Groq, etc). Be practical and specific.',
              expected_output: 'A step-by-step automation plan with specific tools named.'
            }
          ],
          project: {
            title: 'Mini Project: Write Your First AI Finance Prompt',
            instructions: 'Write a prompt that you could use daily in your finance job. It should: (1) describe your role, (2) provide financial context, (3) ask a specific question. Use the template: "You are a [role]. Given [context with numbers], [specific question]?"',
            ai_prompt: 'You are a prompt engineering coach for Finance professionals. The user will share their first AI prompt. Evaluate it on: clarity (1-5), specificity (1-5), context richness (1-5). Then give an improved version. Be encouraging but direct.'
          }
        },

        {
          id: 'm01_02',
          title: 'How Fincy Uses AI (Under the Hood)',
          lessons: [
            {
              id: 'l01_02_01',
              title: 'Groq + Llama 3.1 — The Engine Inside Fincy',
              explanation: 'Fincy uses Groq\'s inference API with Llama 3.1 (8B instant model). Groq is hardware-accelerated — responses come in under 1 second. Llama 3.1 is Meta\'s open-source model, which means no OpenAI dependency and no per-token cost explosion.',
              example: 'When you ask the Fincy AI CFO "Why is my gross margin below 50%?" — Fincy sends your CSV summary + question to Groq → Llama 3.1 analyses it → response arrives in 800ms → displayed on screen. The whole pipeline is 3 API calls.',
              task: 'Ask AI: "How does a Groq API call work? Give me the Python code for a simple finance query."',
              ai_prompt: 'You are a Python developer teaching finance professionals. Show the exact Python code to call the Groq API with a finance system prompt. Use llama-3.1-8b-instant. Include: API key setup, system prompt for a CFO assistant, user message, and how to print the response. Keep it under 25 lines with comments.',
              expected_output: 'Working Python code with comments, under 25 lines.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 02 — INTERMEDIATE: Automating Finance Work
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_02',
      badge: '02 / INTERMEDIATE',
      color: '#4ade80',
      title: 'Automating Finance Work',
      tagline: 'Use Python and AI to eliminate hours of manual work every month.',
      unlocked: false,
      modules: [
        {
          id: 'm02_01',
          title: 'Python for Finance — The 20% You Need',
          lessons: [
            {
              id: 'l02_01_01',
              title: 'Pandas for FP&A — Read, Filter, Summarise',
              explanation: 'Pandas is a Python library that works like Excel but 100× faster and scriptable. You can read a CSV, filter by market, group by brand, and calculate variance in 5 lines. Once scripted, it runs every month in 2 seconds instead of 2 hours.',
              example: 'import pandas as pd\ndf = pd.read_csv("pl_data.csv")\ndf["Variance"] = df["Actual"] - df["Budget"]\nsummary = df.groupby("Market")["Variance"].sum().sort_values()\nprint(summary)',
              task: 'Ask AI to write a Pandas script that calculates budget variance by market from a CSV file with columns: Market, Brand, Actual_Revenue, Budget_Revenue.',
              ai_prompt: 'You are a Python/Pandas expert for finance professionals. Write a complete, runnable Python script that: reads a CSV with columns Market, Brand, Actual_Revenue, Budget_Revenue; calculates Variance and Variance%; groups by Market; sorts worst performers first; prints a clean summary table. Add comments on each line explaining what it does.',
              expected_output: 'A complete, runnable Python script with line-by-line comments.'
            },
            {
              id: 'l02_01_02',
              title: 'Automating Monthly Close Commentary',
              explanation: 'The most time-consuming part of month-end is writing variance commentary. AI can do this in seconds. You provide the numbers; the AI writes the narrative in CFO-ready language. This is the highest-ROI automation in FP&A.',
              example: 'Prompt: "EBITDA missed budget by ₹2.3M (−8%). Revenue was in line (+0.2%) but COGS spiked due to freight costs (+12% YoY) and promotional spending was 15% over plan. Write a 3-sentence board pack commentary."',
              task: 'Write a variance commentary prompt for your own P&L situation (use real or hypothetical numbers). Ask AI to generate board-ready commentary.',
              ai_prompt: 'You are a senior FP&A manager writing a board pack. The user will give you financial variance data. Write concise, professional variance commentary in exactly 3 sentences: 1) Headline performance vs budget, 2) Key driver explanation with numbers, 3) Outlook/action. Use CFO language. No bullet points. No fluff.',
              expected_output: '3 sentences of professional board pack commentary.'
            }
          ],
          project: {
            title: 'Mini Project: Build a Variance Commentary Generator',
            instructions: 'Create a prompt that takes any P&L data and generates commentary. Test it with 3 different scenarios: (1) Revenue miss, (2) Margin beat, (3) OPEX overrun. Share your best prompt and the AI output.',
            ai_prompt: 'You are a prompt engineering mentor for FP&A analysts. The user has created a variance commentary prompt. Test it against 3 scenarios they provide and rate the output quality. Then suggest one improvement to the prompt structure that would make it more reusable across any P&L situation.'
          }
        },
        {
          id: 'm02_02',
          title: 'Automating Reconciliation',
          lessons: [
            {
              id: 'l02_02_01',
              title: 'ERP vs Bank — The Logic Behind Fincy Recon',
              explanation: 'Reconciliation is matching two datasets and finding differences. Fincy does this with a composite key (transaction prefix + date + amount). In Python, this is a pandas merge on multiple columns. Understanding this lets you build your own reconciliation for any two data sources.',
              example: 'df_merge = pd.merge(erp_df, bank_df, on=["prefix","date","amount"], how="outer", indicator=True)\nmatched = df_merge[df_merge["_merge"]=="both"]\nmissing = df_merge[df_merge["_merge"]!="both"]',
              task: 'Ask AI: "How do I reconcile two CSV files in Python using pandas merge? Give me code that shows matched, unmatched, and amount differences."',
              ai_prompt: 'You are a Python expert teaching reconciliation automation to finance professionals. Write complete Python code that: loads two CSV files (ERP and Bank), merges them on a common ID column, classifies each row as Matched / Amount Break / Missing in A / Missing in B, calculates the difference, and exports an exceptions report. Include comments. Use realistic column names.',
              expected_output: 'Complete Python reconciliation script with exception classification.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 03 — ADVANCED: Build AI Finance Tools
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_03',
      badge: '03 / ADVANCED',
      color: '#818cf8',
      title: 'Build AI Finance Tools',
      tagline: 'Build and deploy your own Fincy-style tool using Streamlit + Groq.',
      unlocked: false,
      modules: [
        {
          id: 'm03_01',
          title: 'Streamlit — Finance Dashboards in Python',
          lessons: [
            {
              id: 'l03_01_01',
              title: 'Your First Streamlit Finance Dashboard',
              explanation: 'Streamlit turns Python scripts into web apps. No HTML. No CSS. No JavaScript needed. You write Python, Streamlit renders a shareable web app. Fincy Intelligence is built on Streamlit — the entire UI you see is Python code.',
              example: 'import streamlit as st\nimport pandas as pd\n\nst.title("My FP&A Dashboard")\nfile = st.file_uploader("Upload P&L CSV")\nif file:\n    df = pd.read_csv(file)\n    st.metric("Total Revenue", f"₹{df.Revenue.sum():,.0f}")\n    st.dataframe(df)',
              task: 'Ask AI to write a complete Streamlit app that uploads a CSV and shows: total revenue, top 5 markets by revenue, and a bar chart. Copy the code and try running it locally.',
              ai_prompt: 'You are a Streamlit developer building finance tools. Write a complete, runnable Streamlit app (app.py) that: lets the user upload a CSV, auto-detects a Revenue column, shows 3 KPI metrics (total revenue, average, max), displays a bar chart of top 10 rows by revenue using Plotly, and adds a data table below. Include all imports. Use dark theme colors. Add comments.',
              expected_output: 'Complete runnable app.py for a Streamlit finance dashboard.'
            }
          ],
          project: {
            title: 'Mini Project: Build Your Own AI CFO Module',
            instructions: 'Build a single Streamlit module that: (1) Uploads a CSV, (2) Shows 3 KPIs, (3) Has an "Ask AI CFO" text box that calls Groq, (4) Displays the AI response. This is exactly how each Fincy module is built. Deploy it to share.streamlit.io and share the link.',
            ai_prompt: 'You are a senior Streamlit developer. The user will describe their module idea. Write the complete app.py code for their specific use case, integrating Groq API for the AI CFO section. Make it production-ready with proper error handling and loading spinners.'
          }
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 04 — EXPERT: Prompt Engineering for CFOs
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_04',
      badge: '04 / EXPERT',
      color: '#2dd4bf',
      title: 'Prompt Engineering for CFOs',
      tagline: 'Write prompts that extract CFO-quality insights every time.',
      unlocked: false,
      modules: [
        {
          id: 'm04_01',
          title: '5 CFO Prompt Templates',
          lessons: [
            {
              id: 'l04_01_01',
              title: 'The Anatomy of a Perfect Finance Prompt',
              explanation: 'A great finance prompt has 4 parts: (1) Role — "You are a CFO with 20yr experience", (2) Context — actual numbers from your data, (3) Format — exactly what output you want, (4) Rules — constraints like "no fluff, use percentages". Missing any part drops quality by 50%.',
              example: '"You are a CFO advising a CEO. EBITDA margin is 12% vs 18% budget. Revenue grew 8% YoY but COGS rose 15%. Write a 2-paragraph board pack commentary: first paragraph = what happened with numbers, second paragraph = what we will do about it. No bullet points. Executive tone."',
              task: 'Take one of your real finance reports from last month. Extract the key numbers. Build a prompt using the 4-part structure above. Ask AI to generate the commentary.',
              ai_prompt: 'You are a prompt engineering coach for CFOs and FP&A leaders. The user will share a finance prompt they built. Score it: Role (0-25), Context (0-25), Format (0-25), Rules (0-25) = total /100. Then rewrite it to score 90+. Explain each improvement you made.',
              expected_output: 'Score out of 100, then an improved prompt with explanation.'
            },
            {
              id: 'l04_01_02',
              title: 'Prompt Template: Variance Commentary',
              explanation: 'This is the highest-ROI prompt for FP&A analysts. Use it every month-end. Feed it your actuals vs budget numbers and get board-ready commentary in seconds. The key is giving it the exact format your CFO expects.',
              example: 'TEMPLATE:\n"You are a senior FP&A analyst. Write board pack variance commentary.\nActuals: Revenue ₹{X}M, EBITDA ₹{Y}M, Margin {Z}%\nBudget: Revenue ₹{A}M, EBITDA ₹{B}M, Margin {C}%\nKey drivers: [list 2-3 drivers]\nFormat: 3 sentences. Sentence 1: headline. Sentence 2: drivers. Sentence 3: outlook.\nTone: professional, direct, no jargon."',
              task: 'Fill in the template with your own numbers (real or hypothetical). Click Ask AI to generate your commentary. Compare it to what you would have written manually.',
              ai_prompt: 'You are a CFO. Use EXACTLY this format for your response: HEADLINE: [one sentence with numbers] | DRIVERS: [one sentence with 2 specific causes] | OUTLOOK: [one sentence with next action]. No other text. No bullet points. Use the numbers the user provides.',
              expected_output: 'HEADLINE: ... | DRIVERS: ... | OUTLOOK: ...'
            },
            {
              id: 'l04_01_03',
              title: 'Prompt Template: Cash Flow Risk Alert',
              explanation: 'Cash flow risk prompts need to be specific about timing. The AI needs to know DSO, payment terms, and upcoming obligations to give useful alerts — not generic advice.',
              example: '"You are a treasury analyst. Current cash: ₹50M. DSO: 72 days (target 45). Upcoming payments: Vendor A ₹12M (30 days), Payroll ₹8M (15 days), Tax ₹5M (45 days). Identify top 2 cash risks and give specific collection actions for each. Format: Risk | Amount at risk | Action | Timeline."',
              task: 'Create a cash flow risk prompt using your company\'s approximate DSO, upcoming obligations, and cash position. Ask AI for specific risk alerts.',
              ai_prompt: 'You are a treasury and cash flow specialist. Analyse the user\'s cash position data and identify the top 2-3 risks. Format each risk as: RISK: [name] | AMOUNT: [₹ at risk] | PROBABILITY: High/Medium/Low | ACTION: [specific step with person responsible and deadline]. Be specific. Use the numbers provided.',
              expected_output: 'Structured risk alerts with RISK | AMOUNT | PROBABILITY | ACTION format.'
            }
          ],
          project: {
            title: 'Capstone: Build Your Personal AI CFO Prompt Library',
            instructions: 'Create a "Prompt Library" document with 5 prompts for your specific finance role. Each prompt should: (1) have a name, (2) work every month without modification (just fill in numbers), (3) produce output your CFO would approve. Submit your best prompt and the AI output for peer review.',
            ai_prompt: 'You are a CFO and prompt engineering expert. The user will share a prompt from their personal finance prompt library. Evaluate it on: reusability (1-5), output quality (1-5), CFO-readiness (1-5). Score total /15. Then suggest the one change that would make the biggest improvement. Be specific about what words to change.'
          }
        }
      ]
    }
  ]
};

/* ══════════════════════════════════════════════════════════════
   FINCY LEARNING HUB — Enhancement Pack v3.0
   NEW: Streak System · Badges · Templates · Resume Output · Share
   ══════════════════════════════════════════════════════════════ */

/* ── BADGE DEFINITIONS ─────────────────────────────────────── */
var BADGES = [
  {
    id:        'first_lesson',
    emoji:     '🌱',
    title:     'First Step',
    desc:      'Complete your first lesson',
    color:     '#c9a84c',
    condition: function(p){ return p.completedLessons.length >= 1; }
  },
  {
    id:        'stage1_done',
    emoji:     '🥉',
    title:     'Beginner',
    desc:      'Complete Stage 01 — AI in Finance Basics',
    color:     '#c9a84c',
    condition: function(p){ return p.completedStages.indexOf('stage_01') >= 0; }
  },
  {
    id:        'stage2_done',
    emoji:     '🥈',
    title:     'Intermediate',
    desc:      'Complete Stage 02 — Automating Finance Work',
    color:     '#4ade80',
    condition: function(p){ return p.completedStages.indexOf('stage_02') >= 0; }
  },
  {
    id:        'stage3_done',
    emoji:     '🥇',
    title:     'Advanced',
    desc:      'Complete Stage 03 — Build AI Finance Tools',
    color:     '#818cf8',
    condition: function(p){ return p.completedStages.indexOf('stage_03') >= 0; }
  },
  {
    id:        'expert',
    emoji:     '🏆',
    title:     'AI CFO Expert',
    desc:      'Complete all 4 stages — full certification',
    color:     '#2dd4bf',
    condition: function(p){
      return ['stage_01','stage_02','stage_03','stage_04'].every(function(s){
        return p.completedStages.indexOf(s) >= 0;
      });
    }
  },
  {
    id:        'streak3',
    emoji:     '🔥',
    title:     '3-Day Streak',
    desc:      'Learn 3 days in a row',
    color:     '#f97316',
    condition: function(p){ return (p.streakDays || 0) >= 3; }
  },
  {
    id:        'streak7',
    emoji:     '⚡',
    title:     'Weekly Warrior',
    desc:      'Learn 7 days in a row',
    color:     '#fbbf24',
    condition: function(p){ return (p.streakDays || 0) >= 7; }
  },
  {
    id:        'half_done',
    emoji:     '⭐',
    title:     'Halfway There',
    desc:      'Complete 50% of all lessons',
    color:     '#a78bfa',
    condition: function(p){
      var t = 0;
      FINCY_COURSE.stages.forEach(function(s){ s.modules.forEach(function(m){ t += m.lessons.length; }); });
      return t > 0 && p.completedLessons.length >= Math.ceil(t/2);
    }
  },
  {
    id:        'project_done',
    emoji:     '🔬',
    title:     'Builder',
    desc:      'Complete your first mini project',
    color:     '#06b6d4',
    condition: function(p){ return (p.completedProjects || []).length >= 1; }
  }
];

/* ── DOWNLOADABLE TEMPLATES PER STAGE ─────────────────────── */
var STAGE_TEMPLATES = {
  stage_01: [
    {
      name: 'AI Finance Prompt Template',
      filename: 'ai_finance_prompt_template.txt',
      description: 'Starter template for writing effective AI finance prompts',
      content: [
        'FINCY INTELLIGENCE — AI FINANCE PROMPT TEMPLATE',
        '================================================',
        '',
        'ROLE: You are a [Senior FP&A Analyst / CFO / Finance Controller]',
        'with [X] years experience in [industry/sector].',
        '',
        'CONTEXT:',
        '- Period: [Month/Quarter/Year]',
        '- Revenue: [Actual vs Budget vs PY]',
        '- EBITDA: [Actual vs Budget vs PY]',
        '- Key variance: [+/-X% vs budget due to Y]',
        '',
        'TASK: [Specific question or output needed]',
        '',
        'FORMAT:',
        '- Output: [Commentary / Table / Code / Summary]',
        '- Length: [X sentences / X bullet points]',
        '- Tone: [Executive / Technical / Operational]',
        '',
        'RULES:',
        '- Use specific numbers and percentages',
        '- No generic advice',
        '- Reference the data provided above',
        '- [Any other constraints]',
        '',
        '================================================',
        'Built with Fincy Intelligence | fincyintelligence.com',
      ].join('\n')
    },
    {
      name: 'Groq API Starter Code',
      filename: 'groq_api_starter.py',
      description: 'Python code to call Groq API for finance queries',
      content: [
        '# FINCY INTELLIGENCE — Groq API Starter',
        '# Install: pip install groq',
        '# Get free key: https://console.groq.com',
        '',
        'from groq import Groq',
        '',
        'client = Groq(api_key="your_groq_key_here")',
        '',
        'def ask_ai_cfo(question, financial_context=""):',
        '    """Ask a finance question and get CFO-quality answer."""',
        '    prompt = f"""You are a CFO with 20 years of FP&A experience.',
        '    Financial context: {financial_context}',
        '    Question: {question}',
        '    Answer directly with specific numbers. No fluff."""',
        '',
        '    response = client.chat.completions.create(',
        '        model="llama-3.1-8b-instant",',
        '        messages=[{"role": "user", "content": prompt}],',
        '        max_tokens=400,',
        '        temperature=0.25',
        '    )',
        '    return response.choices[0].message.content',
        '',
        '# Example usage',
        'context = "Revenue: Rs42.8M (+8% YoY). EBITDA: Rs12.1M (margin 28.3%)."',
        'answer  = ask_ai_cfo("What is driving the margin improvement?", context)',
        'print(answer)',
      ].join('\n')
    }
  ],
  stage_02: [
    {
      name: 'Variance Analysis Script',
      filename: 'variance_analysis.py',
      description: 'Ready-to-run Pandas script for budget variance analysis',
      content: [
        '# FINCY INTELLIGENCE — Variance Analysis Script',
        '# Columns needed: Market, Brand, Actual_Revenue, Budget_Revenue',
        '# Install: pip install pandas tabulate',
        '',
        'import pandas as pd',
        '',
        'def run_variance_analysis(filepath):',
        '    df = pd.read_csv(filepath)',
        '',
        '    # Calculate variance',
        '    df["Variance"]   = df["Actual_Revenue"] - df["Budget_Revenue"]',
        '    df["Variance_Pct"] = (df["Variance"] / df["Budget_Revenue"] * 100).round(1)',
        '    df["RAG"] = df["Variance_Pct"].apply(',
        '        lambda x: "GREEN" if x >= -2 else ("AMBER" if x >= -10 else "RED")',
        '    )',
        '',
        '    # Summary by market',
        '    summary = df.groupby("Market").agg(',
        '        Actual=("Actual_Revenue","sum"),',
        '        Budget=("Budget_Revenue","sum"),',
        '        Variance=("Variance","sum")',
        '    ).reset_index()',
        '    summary["Var_Pct"] = (summary["Variance"]/summary["Budget"]*100).round(1)',
        '    summary = summary.sort_values("Var_Pct")',
        '',
        '    print("\\n=== VARIANCE ANALYSIS BY MARKET ===")',
        '    print(summary.to_string(index=False))',
        '    print(f"\\nTotal Variance: {df.Variance.sum():,.0f}")',
        '    return summary',
        '',
        '# Usage',
        'run_variance_analysis("your_data.csv")',
      ].join('\n')
    },
    {
      name: 'Month-End Commentary Prompt',
      filename: 'month_end_commentary_prompt.txt',
      description: 'Reusable AI prompt for automated variance commentary',
      content: [
        'FINCY INTELLIGENCE — Month-End Commentary Prompt',
        '================================================',
        '',
        'SYSTEM: You are a Senior FP&A Manager writing a board pack.',
        '',
        'DATA (fill in each month):',
        'Period: [Month Year]',
        'Revenue Actual: [Rs X.XM] vs Budget: [Rs X.XM] = [+/-X%]',
        'Gross Margin Actual: [X%] vs Budget: [X%] = [+/-X pp]',
        'EBITDA Actual: [Rs X.XM] vs Budget: [Rs X.XM] = [+/-X%]',
        'OPEX Actual: [Rs X.XM] vs Budget: [Rs X.XM] = [+/-X%]',
        'Key drivers: [list 2-3 main causes]',
        '',
        'OUTPUT FORMAT (3 sentences only):',
        '1. HEADLINE: [metric] [vs/missed/beat] budget by [X%] in [Period].',
        '2. DRIVERS: Performance was driven by [cause 1] (+/-X%) and [cause 2] (+/-X%).',
        '3. OUTLOOK: [Corrective action / sustained trend / risk to watch] in [next period].',
        '',
        'RULES: No bullet points. Executive tone. Use Rs/% symbols.',
        '================================================',
      ].join('\n')
    }
  ],
  stage_03: [
    {
      name: 'Streamlit Finance App Template',
      filename: 'fincy_module_template.py',
      description: 'Complete Streamlit template to build your own AI finance module',
      content: [
        '# FINCY INTELLIGENCE — Module Template',
        '# Built following the Fincy architecture',
        '# Install: pip install streamlit pandas plotly groq reportlab',
        '',
        'import streamlit as st',
        'import pandas as pd',
        'import plotly.express as px',
        'from groq import Groq',
        '',
        'st.set_page_config(page_title="My Finance Module", layout="wide")',
        '',
        '# ── AI CFO Function ──',
        'def ask_ai_cfo(question, data_summary):",',
        '    api_key = st.secrets.get("GROQ_API_KEY", "")',
        '    if not api_key: return "Add GROQ_API_KEY to Streamlit Secrets."',
        '    try:',
        '        resp = Groq(api_key=api_key).chat.completions.create(',
        '            model="llama-3.1-8b-instant",',
        '            messages=[',
        '                {"role":"system","content":"You are an AI CFO. Be direct and data-driven."},',
        '                {"role":"user","content":f"Data: {data_summary}\\nQuestion: {question}"}',
        '            ],',
        '            max_tokens=400, temperature=0.25',
        '        )',
        '        return resp.choices[0].message.content',
        '    except Exception as e: return f"Error: {e}"',
        '',
        '# ── Main App ──',
        'st.title("My AI Finance Module")',
        'file = st.file_uploader("Upload CSV", type="csv")',
        '',
        'if file:',
        '    df = pd.read_csv(file)',
        '    st.dataframe(df.head())',
        '',
        '    # KPIs (customise these)',
        '    col1, col2, col3 = st.columns(3)',
        '    with col1: st.metric("Total", f"{df.iloc[:,1].sum():,.0f}")',
        '    with col2: st.metric("Average", f"{df.iloc[:,1].mean():,.1f}")',
        '    with col3: st.metric("Max", f"{df.iloc[:,1].max():,.0f}")',
        '',
        '    # Chart',
        '    fig = px.bar(df.head(10), x=df.columns[0], y=df.columns[1])',
        '    st.plotly_chart(fig, use_container_width=True)',
        '',
        '    # AI CFO',
        '    st.subheader("Ask AI CFO")',
        '    q = st.text_input("Your question:")',
        '    if st.button("Ask") and q:',
        '        with st.spinner("AI CFO thinking..."):',
        '            answer = ask_ai_cfo(q, df.describe().to_string())',
        '        st.info(answer)',
      ].join('\n')
    }
  ],
  stage_04: [
    {
      name: 'CFO Prompt Library',
      filename: 'cfo_prompt_library.txt',
      description: '5 production-ready CFO prompts for FP&A professionals',
      content: [
        'FINCY INTELLIGENCE — CFO Prompt Library',
        'Built for Senior FP&A Analysts | Version 1.0',
        '=============================================',
        '',
        'PROMPT 1: VARIANCE COMMENTARY',
        '------------------------------',
        'You are a Senior FP&A Manager. Write board pack variance commentary.',
        'Actuals: Revenue Rs{X}M, EBITDA Rs{Y}M, Margin {Z}%',
        'Budget: Revenue Rs{A}M, EBITDA Rs{B}M, Margin {C}%',
        'Key drivers: {list drivers}',
        'Format: HEADLINE | DRIVERS | OUTLOOK. 3 sentences. No bullet points.',
        '',
        'PROMPT 2: CASH FLOW RISK ALERT',
        '------------------------------',
        'You are a treasury analyst. Current cash: Rs{X}M. DSO: {Y} days.',
        'Upcoming: {list obligations with amounts and dates}.',
        'Format: RISK | AMOUNT | PROBABILITY | ACTION. Top 3 risks only.',
        '',
        'PROMPT 3: COST REDUCTION ANALYSIS',
        '-----------------------------------',
        'You are a CFO. OPEX is Rs{X}M vs budget Rs{Y}M (+{Z}%).',
        'Breakdown: {cost categories with amounts}.',
        'Identify top 3 cost reduction opportunities. Format: ITEM | SAVING | ACTION.',
        '',
        'PROMPT 4: BUDGET REFORECAST NARRATIVE',
        '---------------------------------------',
        'You are a Finance Director. Q{X} actuals: {summary}.',
        'Reforecast for Q{Y}: revenue Rs{A}M, EBITDA Rs{B}M.',
        'Write a 2-paragraph CFO narrative: 1) Why we are reforecasting, 2) Assumptions.',
        '',
        'PROMPT 5: BOARD PACK EXECUTIVE SUMMARY',
        '---------------------------------------',
        'You are a CFO presenting to the board.',
        'Period: {month}. Key metrics: {list 5-6 KPIs with actuals vs budget}.',
        'Write a 150-word executive summary covering: performance, risks, priorities.',
        '=============================================',
        'Fincy Intelligence | fincyintelligence.com',
      ].join('\n')
    }
  ]
};

/* ── RESUME PROJECT OUTPUTS PER STAGE ─────────────────────── */
var RESUME_OUTPUTS = {
  stage_01: {
    title: 'Resume Line: AI in Finance',
    bullet: 'Completed "AI in Finance Basics" certification — proficient in LLMs, AI agents, Groq API, and FP&A AI use cases (Fincy Intelligence, 2026)',
    linkedin: 'Completed Fincy Intelligence Stage 01: AI in Finance Basics. Now proficient in applying LLMs and AI agents to FP&A workflows including variance analysis, reconciliation, and CFO decision support. #FPandA #AI #Finance',
    skills: ['AI/LLM Fundamentals', 'Groq API', 'FP&A Automation', 'AI Prompt Writing'],
    project_desc: 'Wrote first AI finance prompt and validated LLM output quality for FP&A use cases'
  },
  stage_02: {
    title: 'Resume Line: Finance Automation',
    bullet: 'Automated FP&A workflows using Python/Pandas — reduced variance commentary time from 2 hours to <60 seconds using AI (Fincy Intelligence, 2026)',
    linkedin: 'Just completed Fincy Intelligence Stage 02: Automating Finance Work. Built Python/Pandas scripts for variance analysis and automated month-end commentary using Groq AI. #Python #FPandA #Automation',
    skills: ['Python', 'Pandas', 'Finance Automation', 'AI Commentary Generation', 'Reconciliation Scripting'],
    project_desc: 'Built automated variance commentary generator; reconciliation script handling ERP vs Bank matching'
  },
  stage_03: {
    title: 'Resume Line: AI Finance Tool Builder',
    bullet: 'Built and deployed AI-powered finance dashboard using Streamlit + Groq (production app at share.streamlit.io) — demonstrates end-to-end AI product development (2026)',
    linkedin: 'Completed Fincy Intelligence Stage 03: Build AI Finance Tools. Deployed a Streamlit-based AI CFO module to production. Finance + Python + AI = future-proof career. #Streamlit #FinTech #AI',
    skills: ['Streamlit', 'Plotly', 'Groq API Integration', 'AI Product Development', 'Python Deployment'],
    project_desc: 'Designed and deployed Streamlit finance app with AI CFO integration, live on Streamlit Cloud'
  },
  stage_04: {
    title: 'Resume Line: AI Prompt Engineering',
    bullet: 'Certified in CFO-level prompt engineering — built personal AI prompt library of 5 reusable FP&A templates, adopted in monthly reporting workflow (Fincy Intelligence, 2026)',
    linkedin: 'AI CFO Expert certification complete (Fincy Intelligence). Built a personal prompt library of 5 production-ready FP&A prompts. AI is not replacing finance professionals — it is multiplying our output 10x. #PromptEngineering #CFO #FPandA',
    skills: ['Prompt Engineering', 'CFO Communication', 'AI Strategy', 'Finance AI Integration'],
    project_desc: 'Created 5-prompt AI CFO library validated against real P&L scenarios; peer-reviewed output'
  }
};


/* ── STREAK SYSTEM ─────────────────────────────────────────── */

function updateStreak() {
  var p   = loadProgress();
  var now = new Date();
  var today = now.toISOString().slice(0,10);          // "2026-04-17"

  p.lastActiveDate = p.lastActiveDate || null;
  p.streakDays     = p.streakDays     || 0;
  p.streakStart    = p.streakStart    || today;

  if (p.lastActiveDate === today) {
    // Already logged today — no change
  } else if (p.lastActiveDate) {
    var yesterday = new Date(now);
    yesterday.setDate(yesterday.getDate() - 1);
    var yStr = yesterday.toISOString().slice(0,10);
    if (p.lastActiveDate === yStr) {
      p.streakDays++;                   // consecutive day
    } else {
      p.streakDays  = 1;               // streak broken
      p.streakStart = today;
    }
  } else {
    p.streakDays = 1;
    p.streakStart = today;
  }
  p.lastActiveDate = today;
  saveProgress(p);
  return p.streakDays;
}

function getStreakDisplay() {
  var p = loadProgress();
  var days = p.streakDays || 0;
  var emoji = days >= 7 ? '⚡' : (days >= 3 ? '🔥' : '💧');
  return { days: days, emoji: emoji };
}

/* ── BADGE ENGINE ──────────────────────────────────────────── */

function checkAndAwardBadges() {
  var p    = loadProgress();
  p.badges = p.badges || [];
  var newBadges = [];

  BADGES.forEach(function(badge) {
    if (p.badges.indexOf(badge.id) < 0 && badge.condition(p)) {
      p.badges.push(badge.id);
      newBadges.push(badge);
    }
  });

  if (newBadges.length > 0) {
    saveProgress(p);
    newBadges.forEach(function(badge) {
      showBadgeToast(badge);
    });
  }
  return newBadges;
}

function showBadgeToast(badge) {
  var toast = document.createElement('div');
  toast.style.cssText = (
    'position:fixed;bottom:90px;right:24px;z-index:10000;' +
    'background:#101010;border:1px solid ' + badge.color + ';' +
    'padding:14px 18px;max-width:260px;' +
    'animation:lhFadeIn 0.3s ease;box-shadow:0 4px 20px rgba(0,0,0,0.6);'
  );
  toast.innerHTML = (
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:' + badge.color + ';margin-bottom:6px;">🏅 Badge Unlocked!</div>' +
    '<div style="font-size:1.2rem;margin-bottom:4px;">' + badge.emoji + '</div>' +
    '<div style="font-size:0.82rem;font-weight:700;color:#fafaf8;margin-bottom:3px;">' + badge.title + '</div>' +
    '<div style="font-size:0.72rem;color:#a09880;">' + badge.desc + '</div>'
  );
  document.body.appendChild(toast);
  setTimeout(function(){ toast.remove(); }, 4000);
}

function getBadgePanel() {
  var p = loadProgress();
  p.badges = p.badges || [];
  var html = '<div style="display:flex;flex-wrap:wrap;gap:10px;">';
  BADGES.forEach(function(badge) {
    var earned  = p.badges.indexOf(badge.id) >= 0;
    html += (
      '<div style="background:' + (earned ? 'rgba(0,0,0,0.4)' : 'var(--s)') + ';' +
      'border:1px solid ' + (earned ? badge.color : 'var(--b)') + ';' +
      'padding:12px 14px;text-align:center;width:100px;opacity:' + (earned ? '1' : '0.35') + ';">' +
      '<div style="font-size:1.4rem;">' + badge.emoji + '</div>' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;letter-spacing:0.08em;' +
      'text-transform:uppercase;color:' + (earned ? badge.color : 'var(--text3)') + ';margin-top:5px;">' +
      badge.title + '</div>' +
      (earned ? '<div style="font-size:0.58rem;color:var(--green);margin-top:3px;">✓ Earned</div>' : '') +
      '</div>'
    );
  });
  html += '</div>';
  return html;
}

/* ── TEMPLATE DOWNLOADER ───────────────────────────────────── */

function downloadTemplate(stageId, tplIdx) {
  var templates = STAGE_TEMPLATES[stageId];
  if (!templates || !templates[tplIdx]) return;
  var tpl  = templates[tplIdx];
  var blob = new Blob([tpl.content], { type: 'text/plain;charset=utf-8' });
  var url  = URL.createObjectURL(blob);
  var a    = document.createElement('a');
  a.href   = url;
  a.download = tpl.filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function getTemplatePanel(stageId) {
  var templates = STAGE_TEMPLATES[stageId] || [];
  if (templates.length === 0) return '';
  var html = (
    '<div style="margin-top:20px;background:#0a0a08;border:1px solid var(--b);padding:16px 18px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:var(--gold);margin-bottom:12px;">📥 Stage Templates</div>' +
    '<div style="display:flex;flex-direction:column;gap:8px;">'
  );
  templates.forEach(function(tpl, i) {
    html += (
      '<div style="display:flex;align-items:center;justify-content:space-between;' +
      'background:var(--s);padding:10px 14px;gap:12px;">' +
      '<div>' +
      '<div style="font-size:0.78rem;color:var(--white);margin-bottom:2px;">' + tpl.name + '</div>' +
      '<div style="font-size:0.66rem;color:var(--text3);">' + tpl.description + '</div>' +
      '</div>' +
      '<button class="lh-btn lh-btn-ghost" style="white-space:nowrap;padding:6px 12px;font-size:0.56rem;" ' +
      'onclick="window.FincyLH.downloadTemplate(\'' + stageId + '\',' + i + ')">↓ Download</button>' +
      '</div>'
    );
  });
  html += '</div></div>';
  return html;
}

/* ── RESUME OUTPUT PANEL ───────────────────────────────────── */

function getResumePanel(stageId) {
  var r = RESUME_OUTPUTS[stageId];
  if (!r) return '';
  return (
    '<div style="margin-top:20px;background:#0a0a08;border:1px solid #4ade80;' +
    'border-left:4px solid #4ade80;padding:18px 20px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:#4ade80;margin-bottom:12px;">📄 Resume-Ready Output</div>' +

    '<div style="margin-bottom:14px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;color:var(--text3);' +
    'letter-spacing:0.1em;text-transform:uppercase;margin-bottom:5px;">CV / Resume Bullet</div>' +
    '<div id="resumeBullet_' + stageId + '" style="background:var(--s);padding:10px 12px;' +
    'font-size:0.78rem;color:#e8e2d4;line-height:1.7;border-left:2px solid #4ade80;">' +
    r.bullet + '</div>' +
    '<button class="lh-btn lh-btn-ghost" style="margin-top:6px;padding:5px 12px;font-size:0.54rem;" ' +
    'onclick="window.FincyLH.copyText(\'resumeBullet_' + stageId + '\')">📋 Copy</button>' +
    '</div>' +

    '<div style="margin-bottom:14px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;color:var(--text3);' +
    'letter-spacing:0.1em;text-transform:uppercase;margin-bottom:5px;">LinkedIn Post</div>' +
    '<div id="linkedinPost_' + stageId + '" style="background:var(--s);padding:10px 12px;' +
    'font-size:0.76rem;color:#a09880;line-height:1.75;">' +
    r.linkedin + '</div>' +
    '<button class="lh-btn lh-btn-ghost" style="margin-top:6px;padding:5px 12px;font-size:0.54rem;" ' +
    'onclick="window.FincyLH.copyText(\'linkedinPost_' + stageId + '\')">📋 Copy</button>' +
    '</div>' +

    '<div>' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;color:var(--text3);' +
    'letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px;">Skills to Add</div>' +
    '<div style="display:flex;flex-wrap:wrap;gap:6px;">' +
    r.skills.map(function(s){
      return '<span style="background:rgba(74,222,128,0.1);border:1px solid rgba(74,222,128,0.2);' +
             'color:#4ade80;font-family:IBM Plex Mono,monospace;font-size:0.52rem;' +
             'letter-spacing:0.06em;padding:3px 9px;">' + s + '</span>';
    }).join('') +
    '</div></div>' +

    '</div>'
  );
}

/* ── SHARE PROJECT FEATURE ─────────────────────────────────── */

function getSharePanel(stageId, projectTitle) {
  var r    = RESUME_OUTPUTS[stageId] || {};
  var text = encodeURIComponent(
    'I just completed "' + projectTitle + '" on Fincy Intelligence — ' +
    'an AI CFO learning platform for Finance professionals. ' + (r.linkedin || '') +
    ' Try it free: https://jitenparida95.github.io/fincy-intelligence/#learning'
  );
  var url    = encodeURIComponent('https://jitenparida95.github.io/fincy-intelligence/#learning');
  var liText = encodeURIComponent(r.linkedin || 'Completed a project on Fincy Intelligence!');

  return (
    '<div style="margin-top:16px;background:#0a0a08;border:1px solid var(--b);padding:16px 18px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:var(--gold);margin-bottom:12px;">🚀 Share Your Achievement</div>' +
    '<div style="display:flex;gap:8px;flex-wrap:wrap;">' +

    '<a href="https://www.linkedin.com/shareArticle?mini=true&url=' + url + '&title=' + liText + '" ' +
    'target="_blank" style="display:inline-block;background:#0077B5;color:#fff;' +
    'font-family:IBM Plex Mono,monospace;font-size:0.6rem;font-weight:700;letter-spacing:0.08em;' +
    'text-transform:uppercase;padding:8px 16px;text-decoration:none;">in Share on LinkedIn</a>' +

    '<a href="https://twitter.com/intent/tweet?text=' + text + '" ' +
    'target="_blank" style="display:inline-block;background:#1DA1F2;color:#fff;' +
    'font-family:IBM Plex Mono,monospace;font-size:0.6rem;font-weight:700;letter-spacing:0.08em;' +
    'text-transform:uppercase;padding:8px 16px;text-decoration:none;">𝕏 Share on X</a>' +

    '<button onclick="window.FincyLH.copyShareLink()" ' +
    'class="lh-btn lh-btn-ghost" style="padding:8px 14px;font-size:0.58rem;">🔗 Copy Link</button>' +

    '</div>' +
    '<div style="font-size:0.68rem;color:var(--text3);margin-top:8px;">' +
    'Sharing helps other finance professionals discover AI tools.</div>' +
    '</div>'
  );
}



/* ── PROGRESS STORAGE ──────────────────────────────────────── */
var PROGRESS_KEY = 'fincy_learn_v2';

function loadProgress() {
  try {
    var raw = localStorage.getItem(PROGRESS_KEY);
    return raw ? JSON.parse(raw) : {
      completedLessons:       [],
      completedStages:        [],
      completedProjects:      [],
      currentStage:           'stage_01',
      currentLesson:          null,
      totalPoints:            0,
      streakDays:             0,
      lastActiveDate:         null,
      badges:                 [],
      // v4.0 additions
      xp:                     0,
      level:                  1,
      dailyGoal:              2,
      lessonsCompletedToday:  0,
      lastDayDate:            null,
      savedWork:              [],
      aiMemory:               []
    };
  } catch(e) { return { completedLessons:[], completedStages:[], currentStage:'stage_01', currentLesson:null, totalPoints:0 }; }
}

function saveProgress(prog) {
  try { localStorage.setItem(PROGRESS_KEY, JSON.stringify(prog)); } catch(e) {}
}

function getCompletedCount() {
  var p = loadProgress();
  var total = 0;
  FINCY_COURSE.stages.forEach(function(s){ s.modules.forEach(function(m){ total += m.lessons.length; }); });
  return { done: p.completedLessons.length, total: total };
}

function isLessonDone(lessonId) { return loadProgress().completedLessons.indexOf(lessonId) >= 0; }

function isStageUnlocked(stageIdx) {
  if (stageIdx === 0) return true;
  var prev = FINCY_COURSE.stages[stageIdx - 1];
  var p = loadProgress();
  var allLessons = [];
  prev.modules.forEach(function(m){ m.lessons.forEach(function(l){ allLessons.push(l.id); }); });
  return allLessons.every(function(id){ return p.completedLessons.indexOf(id) >= 0; });
}

/* ── UI ENGINE ─────────────────────────────────────────────── */
var _activeStage  = null;
var _activeLesson = null;
var _activeModule = null;

/* Inject engine styles once */
function injectEngineStyles() {
  if (document.getElementById('lh-engine-styles')) return;
  var s = document.createElement('style');
  s.id = 'lh-engine-styles';
  s.textContent = [
    '/* Fincy Learning Engine styles — injected */',
    '.lh-modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:8000;',
    '  display:flex;align-items:center;justify-content:center;padding:20px;animation:lhFadeIn 0.2s ease;}',
    '@keyframes lhFadeIn{from{opacity:0}to{opacity:1}}',
    '.lh-modal{background:#101010;border:1px solid #2e2e28;max-width:760px;width:100%;',
    '  max-height:88vh;overflow-y:auto;position:relative;}',
    '.lh-modal-hdr{background:#0f0f0c;border-bottom:1px solid #1e1e18;padding:16px 20px;',
    '  display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:1;}',
    '.lh-modal-title{font-family:IBM Plex Mono,monospace;font-size:0.56rem;letter-spacing:0.16em;',
    '  text-transform:uppercase;color:var(--gold);}',
    '.lh-close{background:none;border:none;color:var(--text3);cursor:pointer;font-size:1.1rem;',
    '  padding:0 4px;transition:color 0.2s;}',
    '.lh-close:hover{color:var(--white);}',
    '.lh-modal-body{padding:24px 28px;}',
    '.lh-lesson-nav{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px;}',
    '.lh-lesson-btn{background:var(--s);border:1px solid var(--b);color:var(--text2);',
    '  font-family:IBM Plex Mono,monospace;font-size:0.58rem;letter-spacing:0.06em;',
    '  padding:7px 12px;cursor:pointer;transition:all 0.2s;display:flex;gap:6px;align-items:center;}',
    '.lh-lesson-btn.done{border-color:var(--green);color:var(--green);}',
    '.lh-lesson-btn.active{background:var(--gold);color:var(--bg);border-color:var(--gold);}',
    '.lh-lesson-btn:hover:not(.active){border-color:var(--gold);color:var(--gold);}',
    '.lh-section{margin-bottom:20px;}',
    '.lh-section-label{font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.14em;',
    '  text-transform:uppercase;color:var(--gold);margin-bottom:8px;}',
    '.lh-section-body{font-size:0.82rem;color:var(--text2);line-height:1.85;font-weight:300;}',
    '.lh-code{background:var(--bg);border:1px solid var(--b);border-left:3px solid var(--gold);',
    '  padding:14px 16px;font-family:IBM Plex Mono,monospace;font-size:0.72rem;color:#c9a84c;',
    '  line-height:1.7;white-space:pre-wrap;margin:8px 0;}',
    '.lh-input{width:100%;background:var(--bg);border:1px solid var(--b);color:var(--text);',
    '  font-family:IBM Plex Mono,monospace;font-size:0.76rem;padding:10px 14px;',
    '  resize:vertical;min-height:80px;box-sizing:border-box;outline:none;transition:border-color 0.2s;}',
    '.lh-input:focus{border-color:var(--gold);}',
    '.lh-btn{font-family:IBM Plex Mono,monospace;font-size:0.62rem;font-weight:700;',
    '  letter-spacing:0.08em;text-transform:uppercase;padding:10px 20px;cursor:pointer;',
    '  border:none;transition:all 0.2s;}',
    '.lh-btn-gold{background:var(--gold);color:var(--bg);}',
    '.lh-btn-gold:hover{background:var(--gold2);}',
    '.lh-btn-ghost{background:transparent;border:1px solid var(--b2);color:var(--text2);}',
    '.lh-btn-ghost:hover{border-color:var(--gold);color:var(--gold);}',
    '.lh-btn-green{background:#4ade80;color:#0a0a08;}',
    '.lh-btn-green:hover{background:#22c55e;}',
    '.lh-btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}',
    '.lh-ai-box{background:var(--s);border:1px solid var(--b);border-left:3px solid var(--gold);',
    '  padding:16px 18px;font-size:0.8rem;color:var(--text2);line-height:1.85;',
    '  min-height:60px;margin-top:8px;white-space:pre-wrap;}',
    '.lh-progress-bar{background:var(--b);height:6px;margin:8px 0;}',
    '.lh-progress-fill{height:100%;transition:width 0.4s ease;background:var(--gold);}',
    '.lh-complete-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(74,222,128,0.1);',
    '  border:1px solid var(--green);color:var(--green);font-family:IBM Plex Mono,monospace;',
    '  font-size:0.52rem;letter-spacing:0.1em;text-transform:uppercase;padding:4px 10px;}',
    '.lh-module-list{display:flex;flex-direction:column;gap:8px;}',
    '.lh-module-card{background:var(--s);border:1px solid var(--b);padding:16px 18px;cursor:pointer;',
    '  transition:border-color 0.2s;}',
    '.lh-module-card:hover{border-color:var(--gold);}',
    '.lh-spinner{display:inline-block;width:14px;height:14px;border:2px solid var(--b2);',
    '  border-top-color:var(--gold);border-radius:50%;animation:lhSpin 0.8s linear infinite;',
    '  vertical-align:middle;margin-right:6px;}',
    '@keyframes lhSpin{to{transform:rotate(360deg)}}',
    '.lh-locked{opacity:0.4;cursor:not-allowed;pointer-events:none;}',
    '.lh-stage-progress{font-family:IBM Plex Mono,monospace;font-size:0.5rem;',
    '  letter-spacing:0.08em;text-transform:uppercase;color:var(--text3);margin-top:6px;}',
    /* Badge toast animation */
    '@keyframes lhSlideIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}',
    '.lh-badge-toast{animation:lhSlideIn 0.3s ease;}',
    /* Resume panel */
    '.lh-resume-panel{background:#0a0a08;border:1px solid #4ade80;border-left:4px solid #4ade80;padding:18px 20px;margin-top:20px;}',
    /* Share buttons */
    '.lh-share-btn{display:inline-block;padding:8px 16px;font-family:IBM Plex Mono,monospace;',
    '  font-size:0.6rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;',
    '  text-decoration:none;cursor:pointer;border:none;transition:opacity 0.2s;}',
    '.lh-share-btn:hover{opacity:0.85;}',
  ].join('\n');
  document.head.appendChild(s);
}

/* ── MODAL SYSTEM ──────────────────────────────────────────── */
function openModal(html, title) {
  closeModal();
  var overlay = document.createElement('div');
  overlay.className = 'lh-modal-overlay';
  overlay.id = 'lhEngineModal';
  overlay.innerHTML = '<div class="lh-modal">' +
    '<div class="lh-modal-hdr">' +
    '<span class="lh-modal-title">' + title + '</span>' +
    '<button class="lh-close" onclick="window.FincyLH.closeModal()">✕</button>' +
    '</div>' +
    '<div class="lh-modal-body" id="lhModalBody">' + html + '</div>' +
    '</div>';
  overlay.addEventListener('click', function(e){ if(e.target===overlay) closeModal(); });
  document.body.appendChild(overlay);
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  var m = document.getElementById('lhEngineModal');
  if (m) { m.remove(); document.body.style.overflow = ''; }
}

function refreshModal(html) {
  var b = document.getElementById('lhModalBody');
  if (b) b.innerHTML = html;
}

/* ── STAGE LOADER ──────────────────────────────────────────── */
function loadStage(stageIdx) {
  injectEngineStyles();
  var stage = FINCY_COURSE.stages[stageIdx];
  if (!stage) return;

  if (!isStageUnlocked(stageIdx)) {
    openModal(
      '<div style="text-align:center;padding:32px 0;">' +
      '<div style="font-size:2rem;margin-bottom:12px;">🔒</div>' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.62rem;color:var(--text3);' +
      'letter-spacing:0.1em;text-transform:uppercase;margin-bottom:10px;">Stage Locked</div>' +
      '<div style="font-size:0.84rem;color:var(--text2);line-height:1.7;">' +
      'Complete all lessons in Stage ' + stageIdx + ' to unlock this stage.</div>' +
      '<div style="margin-top:20px;">' +
      '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.loadStage(' + (stageIdx-1) + ')">← Go to Stage ' + stageIdx + '</button>' +
      '</div></div>',
      '◆ ' + stage.badge + ' — Locked'
    );
    return;
  }

  _activeStage = stageIdx;

  var count = getCompletedCount();
  var pct   = count.total > 0 ? Math.round(count.done / count.total * 100) : 0;

  // Count stage-specific lessons
  var stageDone = 0, stageTotal = 0;
  stage.modules.forEach(function(m){
    m.lessons.forEach(function(l){
      stageTotal++;
      if (isLessonDone(l.id)) stageDone++;
    });
  });
  var stagePct = stageTotal > 0 ? Math.round(stageDone / stageTotal * 100) : 0;

  var html = '<div style="margin-bottom:16px;">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--text3);' +
    'letter-spacing:0.1em;text-transform:uppercase;">Stage Progress</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--gold);">' +
    stageDone + '/' + stageTotal + ' lessons</span>' +
    '</div>' +
    '<div class="lh-progress-bar"><div class="lh-progress-fill" style="width:' + stagePct + '%;' +
    'background:' + stage.color + ';"></div></div>' +
    '</div>' +
    '<p style="font-size:0.8rem;color:var(--text2);margin-bottom:24px;">' + stage.tagline + '</p>' +
    '<div class="lh-module-list">';

  stage.modules.forEach(function(mod, mi) {
    var modDone = mod.lessons.filter(function(l){ return isLessonDone(l.id); }).length;
    html += '<div class="lh-module-card" onclick="window.FincyLH.loadModule(' + stageIdx + ',' + mi + ')">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;">' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.1em;' +
      'text-transform:uppercase;color:' + stage.color + ';margin-bottom:4px;">Module ' + (mi+1) + '</div>' +
      (modDone === mod.lessons.length && mod.lessons.length > 0 ?
        '<span class="lh-complete-badge">✓ Complete</span>' : '') +
      '</div>' +
      '<div style="font-size:0.86rem;color:var(--white);font-weight:600;margin-bottom:4px;">' +
      mod.title + '</div>' +
      '<div style="font-size:0.72rem;color:var(--text3);">' + mod.lessons.length + ' lessons' +
      (mod.project ? ' + mini project' : '') + '</div>' +
      '</div>';
  });

  html += '</div>';
  // Templates panel always visible
  html += getTemplatePanel(stage.id);

  // Resume + Share only when stage complete
  if (stagePct === 100) {
    html += '<div style="margin-top:20px;background:rgba(74,222,128,0.08);border:1px solid var(--green);' +
      'padding:14px 18px;text-align:center;">' +
      '<div style="color:var(--green);font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
      'letter-spacing:0.1em;text-transform:uppercase;">🎉 Stage Complete!</div>' +
      (stageIdx < FINCY_COURSE.stages.length-1 ?
        '<div style="margin-top:8px;"><button class="lh-btn lh-btn-green" onclick="window.FincyLH.loadStage(' + (stageIdx+1) + ')">Unlock Stage ' + (stageIdx+2) + ' →</button></div>' : '') +
      '</div>';
    html += getResumePanel(stage.id);
    html += getSharePanel(stage.id, stage.title);
  }

  openModal(html, '◆ ' + stage.badge + ' — ' + stage.title);
}

/* ── MODULE LOADER ─────────────────────────────────────────── */
function loadModule(stageIdx, moduleIdx) {
  var stage = FINCY_COURSE.stages[stageIdx];
  var mod   = stage.modules[moduleIdx];
  _activeModule = { stageIdx: stageIdx, moduleIdx: moduleIdx };

  var html = '<button class="lh-btn lh-btn-ghost" style="margin-bottom:16px;" ' +
    'onclick="window.FincyLH.loadStage(' + stageIdx + ')">← Back to Stage</button>' +
    '<div style="font-size:0.86rem;color:var(--text2);margin-bottom:20px;line-height:1.7;">' +
    'Select a lesson to begin:</div>' +
    '<div class="lh-lesson-nav">';

  mod.lessons.forEach(function(lesson, li) {
    var done = isLessonDone(lesson.id);
    html += '<button class="lh-lesson-btn' + (done ? ' done' : '') + '" ' +
      'onclick="window.FincyLH.loadLesson(' + stageIdx + ',' + moduleIdx + ',' + li + ')">' +
      (done ? '✓ ' : '') + (li+1) + '. ' + lesson.title + '</button>';
  });

  html += '</div>';

  if (mod.project) {
    html += '<div style="margin-top:20px;background:#0d0b18;border:1px solid #818cf8;' +
      'padding:14px 18px;">' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.12em;' +
      'text-transform:uppercase;color:#818cf8;margin-bottom:6px;">🔬 Mini Project</div>' +
      '<div style="font-size:0.8rem;color:var(--text2);">' + mod.project.title + '</div>' +
      '<div style="margin-top:8px;">' +
      '<button class="lh-btn lh-btn-ghost" ' +
      'onclick="window.FincyLH.loadProject(' + stageIdx + ',' + moduleIdx + ')">Start Project →</button>' +
      '</div></div>';
  }

  refreshModal(html);
}

/* ── LESSON LOADER ─────────────────────────────────────────── */
function loadLesson(stageIdx, moduleIdx, lessonIdx) {
  var stage  = FINCY_COURSE.stages[stageIdx];
  var mod    = stage.modules[moduleIdx];
  var lesson = mod.lessons[lessonIdx];
  _activeLesson = lesson;

  var done = isLessonDone(lesson.id);

  var html =
    '<button class="lh-btn lh-btn-ghost" style="margin-bottom:16px;" ' +
    'onclick="window.FincyLH.loadModule(' + stageIdx + ',' + moduleIdx + ')">← Back to Module</button>' +
    (done ? '<div style="margin-bottom:14px;"><span class="lh-complete-badge">✓ Lesson Complete</span></div>' : '') +

    // Nav between lessons
    _lessonNavHtml(stageIdx, moduleIdx, lessonIdx) +

    '<div class="lh-section">' +
    '<div class="lh-section-label">📖 Explanation</div>' +
    '<div class="lh-section-body">' + lesson.explanation + '</div>' +
    '</div>' +

    '<div class="lh-section">' +
    '<div class="lh-section-label">💡 Real-World Example</div>' +
    '<div class="lh-code">' + escHtml(lesson.example) + '</div>' +
    '</div>' +

    '<div class="lh-section">' +
    '<div class="lh-section-label">✏️ Your Task</div>' +
    '<div class="lh-section-body" style="margin-bottom:10px;">' + lesson.task + '</div>' +
    '<textarea class="lh-input" id="lhTaskInput" placeholder="Type your question or answer here…"></textarea>' +
    '<div class="lh-btn-row">' +
    '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.handleAIRequest()">🚀 Ask AI</button>' +
    '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.useExample(' + stageIdx + ',' + moduleIdx + ',' + lessonIdx + ')">Use Example</button>' +
    (done ? '' : '<button class="lh-btn lh-btn-green" onclick="window.FincyLH.markComplete(\'' + lesson.id + '\',' + stageIdx + ',' + moduleIdx + ',' + lessonIdx + ')">✓ Mark Complete</button>') +
    '</div>' +
    '</div>' +

    '<div class="lh-section">' +
    '<div class="lh-section-label">🧠 AI Response</div>' +
    '<div class="lh-ai-box" id="lhAIOutput">' +
    '<span style="color:var(--text3);font-family:IBM Plex Mono,monospace;font-size:0.62rem;">' +
    'Ask a question above → AI CFO responds here</span></div>' +
    '</div>' +

    '<div class="lh-section" style="border-top:1px solid var(--b);padding-top:14px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.1em;' +
    'text-transform:uppercase;color:var(--text3);margin-bottom:6px;">Expected output</div>' +
    '<div style="font-size:0.74rem;color:var(--text3);font-style:italic;">' + lesson.expected_output + '</div>' +
    '</div>';

  refreshModal(html);
}

function _lessonNavHtml(si, mi, li) {
  var mod = FINCY_COURSE.stages[si].modules[mi];
  var prev = li > 0 ? li - 1 : null;
  var next = li < mod.lessons.length - 1 ? li + 1 : null;
  return '<div style="display:flex;justify-content:space-between;margin-bottom:18px;">' +
    (prev !== null ?
      '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.loadLesson(' + si + ',' + mi + ',' + prev + ')">← Previous</button>' :
      '<span></span>') +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--text3);">' +
    'Lesson ' + (li+1) + ' of ' + mod.lessons.length + '</span>' +
    (next !== null ?
      '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.loadLesson(' + si + ',' + mi + ',' + next + ')">Next →</button>' :
      '<span></span>') +
    '</div>';
}

/* ── AI REQUEST HANDLER ────────────────────────────────────── */
function handleAIRequest() {
  if (!_activeLesson) return;
  var input  = document.getElementById('lhTaskInput');
  var output = document.getElementById('lhAIOutput');
  if (!input || !output) return;

  var userText = (input.value || '').trim();
  if (!userText) {
    output.innerHTML = '<span style="color:#fbbf24;">Please type a question or answer first.</span>';
    return;
  }

  output.innerHTML = '<span class="lh-spinner"></span> AI CFO thinking…';

  var groqKey = window.GROQ_KEY || '';
  var sysPrompt = _activeLesson.ai_prompt;

  // v4: Build messages with AI memory (last 3 conversations)
  var msgs = handleAIMemory(sysPrompt, userText);

  if (!groqKey) {
    setTimeout(function() {
      var fallback = (
        'For AI-powered lesson responses, open Fincy Intelligence app.' +
        ' <a href="https://fincy-intelligence.streamlit.app/?m=learning" target="_blank" ' +
        'style="color:var(--gold);font-family:IBM Plex Mono,monospace;font-size:0.65rem;' +
        'letter-spacing:0.08em;text-transform:uppercase;">Open Full Learning Hub →</a>'
      );
      output.innerHTML = fallback;
      saveUserWork(userText, fallback);  // v4: save even fallback responses
    }, 600);
    return;
  }

  fetch('https://api.groq.com/openai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + groqKey
    },
    body: JSON.stringify({
      model: 'llama-3.1-8b-instant',
      messages: msgs,
      max_tokens: 600,
      temperature: 0.35
    })
  })
  .then(function(r){ return r.json(); })
  .then(function(d){
    var ans = (d.choices && d.choices[0] && d.choices[0].message)
      ? d.choices[0].message.content
      : 'No response. Try again.';
    output.textContent = ans;

    // v4: Save work automatically
    saveUserWork(userText, ans);

    // v4: Store in AI memory for context
    _storeAIMemory(userText, ans);

    // v4: Show psychological hook after AI responds
    _showPsychHook(output);

    // v4: Mark project complete for Builder badge
    if (_activeLesson && _activeLesson.isProject) {
      var p = loadProgress();
      p.completedProjects = p.completedProjects || [];
      var pid = _activeLesson.id;
      if (p.completedProjects.indexOf(pid) < 0) {
        p.completedProjects.push(pid);
        saveProgress(p);
        checkAndAwardBadges();
      }
    }
  })
  .catch(function(e){
    output.innerHTML = '<span style="color:var(--red);">Error: ' + e.message + '</span>';
  });
}

/* ── MARK COMPLETE ─────────────────────────────────────────── */
function markComplete(lessonId, stageIdx, moduleIdx, lessonIdx) {
  var p       = loadProgress();
  var isNew   = p.completedLessons.indexOf(lessonId) < 0;

  if (isNew) {
    p.completedLessons.push(lessonId);
    p.totalPoints += 10;
  }

  // Stage completion check
  var stage = FINCY_COURSE.stages[stageIdx];
  var allLessons = [];
  stage.modules.forEach(function(m){ m.lessons.forEach(function(l){ allLessons.push(l.id); }); });
  var stageJustDone = allLessons.every(function(id){ return p.completedLessons.indexOf(id) >= 0; });
  if (stageJustDone && p.completedStages.indexOf(stage.id) < 0) {
    p.completedStages.push(stage.id);
  }

  saveProgress(p);
  updateStreak();
  handleDailySystem();       // v4: daily goal tracking
  updateXP(10, stageJustDone ? 100 : 0);  // v4: XP + level
  checkAndAwardBadges();
  updateProgressBars();
  updateStreakDisplay();

  // Rebuild lesson view with complete state + auto-next
  var html = _lessonCompleteHtml(lessonId, stageIdx, moduleIdx, lessonIdx, stageJustDone);
  refreshModal(html);
}

/* Lesson complete view — shows celebration + next action */
function _lessonCompleteHtml(lessonId, si, mi, li, stageJustDone) {
  var stage = FINCY_COURSE.stages[si];
  var mod   = stage.modules[mi];
  var lesson = mod.lessons[li];
  var p     = loadProgress();

  // Psychological hook — rotates randomly
  var hooks = [
    'You just automated a 2-hour task. 🤖',
    'This is a CFO-level skill. Very few analysts have it. 📊',
    'Top 10% of FP&A professionals use this exact technique.',
    'This skill can increase your salary by ₹2-5L. Keep going.',
    'Senior managers spend hours on this. You can now do it in 60 seconds.',
    'You are building skills most finance teams will not have for 5 years.',
    'Every lesson here is a line you can add to your CV. 🏆'
  ];
  var hook = hooks[Math.floor(Math.random() * hooks.length)];

  // Auto-next logic
  var hasNextLesson = li < mod.lessons.length - 1;
  var hasNextModule = mi < stage.modules.length - 1;
  var hasNextStage  = si < FINCY_COURSE.stages.length - 1;

  var nextBtn = '';
  if (stageJustDone) {
    nextBtn = (
      '<div style="text-align:center;margin-top:20px;">' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;letter-spacing:0.14em;' +
      'text-transform:uppercase;color:#2dd4bf;margin-bottom:12px;">🚀 Stage Complete!</div>' +
      (hasNextStage ?
        '<button class="lh-btn lh-btn-green" ' +
        'onclick="window.FincyLH.loadStage(' + (si+1) + ')">Unlock Stage ' + (si+2) + ' →</button>' :
        '<div style="color:var(--gold);font-size:0.88rem;font-weight:700;">🏆 All stages complete. You are an AI CFO Expert.</div>'
      ) + '</div>'
    );
  } else if (hasNextLesson) {
    nextBtn = (
      '<div style="text-align:center;margin-top:16px;">' +
      '<button class="lh-btn lh-btn-gold" ' +
      'onclick="window.FincyLH.goToNextLesson(' + si + ',' + mi + ',' + li + ')">Continue to next lesson →</button>' +
      '</div>'
    );
  } else if (hasNextModule) {
    nextBtn = (
      '<div style="text-align:center;margin-top:16px;">' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.1em;' +
      'text-transform:uppercase;color:#4ade80;margin-bottom:8px;">🎉 Module Complete!</div>' +
      '<button class="lh-btn lh-btn-gold" ' +
      'onclick="window.FincyLH.loadModule(' + si + ',' + (mi+1) + ')">Start next module →</button>' +
      '</div>'
    );
  }

  // Daily goal progress
  var doneToday  = p.lessonsCompletedToday || 0;
  var dailyGoal  = p.dailyGoal || 2;
  var goalPct    = Math.min(Math.round(doneToday / dailyGoal * 100), 100);
  var goalDone   = doneToday >= dailyGoal;

  return (
    '<div style="text-align:center;padding:16px 0 8px;">' +
    '<div style="font-size:2.2rem;margin-bottom:8px;">' + (stageJustDone ? '🏆' : '✅') + '</div>' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.58rem;letter-spacing:0.16em;' +
    'text-transform:uppercase;color:var(--green);margin-bottom:4px;">Lesson Complete!</div>' +
    '<div style="font-size:0.8rem;color:#c9a84c;font-weight:700;margin-bottom:16px;">+10 XP Earned 🚀' +
    (stageJustDone ? '  +100 XP Stage Bonus!' : '') + '</div>' +
    '</div>' +

    // Psychological hook
    '<div style="background:rgba(201,168,76,0.08);border:1px solid rgba(201,168,76,0.2);' +
    'padding:12px 16px;text-align:center;margin-bottom:16px;font-size:0.8rem;color:var(--text2);">' +
    hook + '</div>' +

    // Daily goal bar
    '<div style="margin-bottom:16px;">' +
    '<div style="display:flex;justify-content:space-between;margin-bottom:4px;">' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;color:var(--text3);' +
    'letter-spacing:0.1em;text-transform:uppercase;">' +
    (goalDone ? '🎯 Daily goal complete!' : 'Today: ' + doneToday + '/' + dailyGoal + ' lessons') +
    '</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;color:var(--gold);">' +
    goalPct + '%</span>' +
    '</div>' +
    '<div class="lh-progress-bar"><div class="lh-progress-fill" style="width:' + goalPct + '%;' +
    'background:' + (goalDone ? '#4ade80' : 'var(--gold)') + ';transition:width 0.6s ease;"></div></div>' +
    '</div>' +

    // Lesson title + back button
    '<div style="margin-bottom:16px;">' +
    '<span class="lh-complete-badge">✓ ' + lesson.title + '</span>' +
    '</div>' +

    // Nav back
    '<div class="lh-btn-row" style="justify-content:center;">' +
    '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.loadModule(' + si + ',' + mi + ')">← Back to Module</button>' +
    '</div>' +
    nextBtn
  );
}

/* ── PROJECT LOADER ────────────────────────────────────────── */
function loadProject(stageIdx, moduleIdx) {
  var stage   = FINCY_COURSE.stages[stageIdx];
  var project = stage.modules[moduleIdx].project;
  if (!project) return;

  var html =
    '<button class="lh-btn lh-btn-ghost" style="margin-bottom:16px;" ' +
    'onclick="window.FincyLH.loadModule(' + stageIdx + ',' + moduleIdx + ')">← Back to Module</button>' +
    '<div style="background:#0d0b18;border:1px solid #818cf8;padding:14px 18px;margin-bottom:18px;">' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:#818cf8;margin-bottom:6px;">🔬 Mini Project</div>' +
    '<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:700;' +
    'color:var(--white);margin-bottom:10px;">' + project.title + '</div>' +
    '<div style="font-size:0.8rem;color:var(--text2);line-height:1.8;">' + project.instructions + '</div>' +
    '</div>' +
    '<div class="lh-section">' +
    '<div class="lh-section-label">✏️ Your Work</div>' +
    '<textarea class="lh-input" id="lhTaskInput" placeholder="Share your project output here…" style="min-height:120px;"></textarea>' +
    '<div class="lh-btn-row">' +
    '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.handleAIRequest()">🚀 Get AI Feedback</button>' +
    '</div></div>' +
    '<div class="lh-section">' +
    '<div class="lh-section-label">🧠 AI Feedback</div>' +
    '<div class="lh-ai-box" id="lhAIOutput">' +
    '<span style="color:var(--text3);font-family:IBM Plex Mono,monospace;font-size:0.62rem;">Submit your work above to get expert AI feedback</span>' +
    '</div></div>';

  // Add share panel at bottom of project
  var stage = FINCY_COURSE.stages[stageIdx];
  html += getSharePanel(stage.id, project.title);
  html += getResumePanel(stage.id);

  // Track project completion on "Get AI Feedback" click
  _activeLesson = {
    ai_prompt: project.ai_prompt,
    id: 'project_' + stageIdx + '_' + moduleIdx,
    isProject: true,
    stageId: stage.id
  };
  refreshModal(html);
}

/* ── USE EXAMPLE ───────────────────────────────────────────── */
function useExample(si, mi, li) {
  var lesson = FINCY_COURSE.stages[si].modules[mi].lessons[li];
  var inp = document.getElementById('lhTaskInput');
  if (inp) inp.value = lesson.example;
}

/* ── PROGRESS BAR UPDATE (on page) ────────────────────────── */
function updateProgressBars() {
  var count = getCompletedCount();
  var pct   = count.total > 0 ? Math.round(count.done / count.total * 100) : 0;

  // Update the main progress bar if it exists
  var bar = document.getElementById('lhOverallProgress');
  if (bar) bar.style.width = pct + '%';
  var lbl = document.getElementById('lhOverallLabel');
  if (lbl) lbl.textContent = count.done + '/' + count.total + ' lessons (' + pct + '%)';

  // Update per-stage progress badges
  FINCY_COURSE.stages.forEach(function(stage, si) {
    var stageDone = 0, stageTotal = 0;
    stage.modules.forEach(function(m){
      m.lessons.forEach(function(l){
        stageTotal++;
        if (isLessonDone(l.id)) stageDone++;
      });
    });
    var sBadge = document.getElementById('lh-stage-prog-' + si);
    if (sBadge) sBadge.textContent = stageDone + '/' + stageTotal + ' lessons';
    var sBar = document.getElementById('lh-stage-bar-' + si);
    if (sBar) sBar.style.width = (stageTotal > 0 ? Math.round(stageDone/stageTotal*100) : 0) + '%';
    var sBtn = document.getElementById('lh-stage-btn-' + si);
    if (sBtn) {
      if (!isStageUnlocked(si)) {
        sBtn.classList.add('lh-locked');
        sBtn.textContent = '🔒 Locked';
      } else {
        sBtn.classList.remove('lh-locked');
        sBtn.textContent = stageDone === stageTotal && stageTotal > 0 ? '✓ Review' : 'Start Stage ' + String(si+1).padStart(2,'0') + ' →';
      }
    }
  });
}

/* ── ESCAPE HTML ───────────────────────────────────────────── */
function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

/* ══════════════════════════════════════════════════════════════
   FINCY LEARNING HUB v4.0 — Addictive Daily Learning Engine
   New: Daily System · XP/Level · Save Work · AI Memory · Hooks
   ══════════════════════════════════════════════════════════════ */

/* ── FEATURE 1: DAILY LEARNING SYSTEM ─────────────────────── */

/**
 * handleDailySystem()
 * Call on every lesson complete.
 * Tracks daily goal, resets at midnight, shows streak messages.
 */
function handleDailySystem() {
  var p     = loadProgress();
  var today = new Date().toISOString().slice(0, 10);

  // New day — reset daily counter
  if (p.lastDayDate !== today) {
    if (p.lastDayDate) {
      // Check if they missed yesterday → streak already handled by updateStreak()
      // Show streak message
      var yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      var yStr = yesterday.toISOString().slice(0, 10);
      if (p.lastDayDate === yStr) {
        _showFloatingMsg("🔥 You're on a roll! " + (p.streakDays || 1) + " days in a row!");
      } else {
        _showFloatingMsg("You lost your streak 😬 — Start fresh today!");
      }
    }
    p.lessonsCompletedToday = 0;
    p.lastDayDate = today;
  }

  // Increment today's count
  p.lessonsCompletedToday = (p.lessonsCompletedToday || 0) + 1;

  // Daily goal reached?
  if (p.lessonsCompletedToday >= (p.dailyGoal || 2)) {
    p.xp = (p.xp || 0) + 20;  // bonus XP for hitting daily goal
    setTimeout(function() {
      _showFloatingMsg("🎯 Daily goal complete! +20 Bonus XP!");
    }, 2000);
  }

  saveProgress(p);
}

/* ── FEATURE 2: XP + LEVEL SYSTEM ─────────────────────────── */

/**
 * updateXP(lessonXP, bonusXP)
 * Awards XP, checks for level up, shows popup.
 * lessonXP = 10 per lesson, bonusXP = 100 for stage complete.
 */
function updateXP(lessonXP, bonusXP) {
  lessonXP = lessonXP || 0;
  bonusXP  = bonusXP  || 0;
  var totalXP  = lessonXP + bonusXP;
  if (totalXP <= 0) return;

  var p        = loadProgress();
  var oldLevel = Math.floor((p.xp || 0) / 100) + 1;
  p.xp         = (p.xp || 0) + totalXP;
  var newLevel = Math.floor(p.xp / 100) + 1;
  p.level      = newLevel;
  saveProgress(p);

  // XP gain toast
  _showXPToast(totalXP, newLevel > oldLevel ? newLevel : null);

  // Update level badge if on page
  var lvlEl = document.getElementById('lhLevelBadge');
  if (lvlEl) lvlEl.textContent = 'Lv.' + newLevel;
  var xpEl  = document.getElementById('lhXPLabel');
  if (xpEl)  xpEl.textContent  = p.xp + ' XP';
}

function _showXPToast(xp, newLevel) {
  var toast = document.createElement('div');
  toast.style.cssText = (
    'position:fixed;top:80px;right:24px;z-index:10001;' +
    'background:#101010;border:1px solid #c9a84c;' +
    'padding:12px 18px;min-width:200px;' +
    'animation:lhSlideIn 0.3s ease;box-shadow:0 4px 20px rgba(0,0,0,0.7);'
  );
  toast.innerHTML = (
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.58rem;font-weight:700;' +
    'color:#c9a84c;margin-bottom:4px;">+' + xp + ' XP Earned 🚀</div>' +
    (newLevel ?
      '<div style="font-size:0.82rem;color:#4ade80;font-weight:700;">⬆ Level Up! Now Lv.' + newLevel + '</div>' :
      '<div style="font-size:0.72rem;color:var(--text2);">' +
      Math.round(((loadProgress().xp || 0) % 100)) + '/100 XP to next level</div>'
    )
  );
  document.body.appendChild(toast);
  setTimeout(function(){ toast.remove(); }, 3500);
}

/* ── FEATURE 3: SAVE USER WORK ─────────────────────────────── */

/**
 * saveUserWork(userInput, aiOutput)
 * Auto-saves every AI interaction to localStorage.
 * Keeps last 50 items to avoid storage overflow.
 */
function saveUserWork(userInput, aiOutput) {
  if (!userInput || !aiOutput) return;
  var p     = loadProgress();
  p.savedWork = p.savedWork || [];

  p.savedWork.unshift({
    lessonId:  _activeLesson ? _activeLesson.id : 'unknown',
    lessonTitle: _activeLesson ? (_activeLesson.title || 'Lesson') : 'Lesson',
    userInput: userInput,
    aiOutput:  aiOutput,
    timestamp: new Date().toISOString()
  });

  // Keep last 50 only
  if (p.savedWork.length > 50) p.savedWork = p.savedWork.slice(0, 50);
  saveProgress(p);
}

/**
 * showMyWork()
 * Opens "My AI Work" panel in a modal — shows all saved interactions.
 */
function showMyWork() {
  var p     = loadProgress();
  var works = p.savedWork || [];

  if (works.length === 0) {
    openModal(
      '<div style="text-align:center;padding:32px 0;color:var(--text3);font-size:0.84rem;">' +
      'No saved work yet. Complete a lesson and ask AI — it will be saved here automatically.</div>',
      '◆ My AI Work'
    );
    return;
  }

  var html = (
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.1em;' +
    'text-transform:uppercase;color:var(--text3);margin-bottom:16px;">' +
    works.length + ' saved interactions — most recent first</div>' +
    '<div style="display:flex;flex-direction:column;gap:12px;">'
  );

  works.slice(0, 20).forEach(function(w, i) {
    var date = w.timestamp ? w.timestamp.slice(0,10) : '';
    html += (
      '<div style="background:var(--s);border:1px solid var(--b);border-left:3px solid var(--gold);' +
      'padding:14px 16px;">' +
      '<div style="display:flex;justify-content:space-between;margin-bottom:8px;">' +
      '<span style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;letter-spacing:0.1em;' +
      'text-transform:uppercase;color:var(--gold);">' + escHtml(w.lessonTitle || '') + '</span>' +
      '<span style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;color:var(--text3);">' + date + '</span>' +
      '</div>' +
      '<div style="font-size:0.72rem;color:var(--text3);margin-bottom:6px;font-style:italic;">' +
      '"' + escHtml((w.userInput || '').slice(0, 100)) + (w.userInput && w.userInput.length > 100 ? '…' : '') + '"</div>' +
      '<div style="font-size:0.78rem;color:var(--text2);line-height:1.7;margin-bottom:10px;' +
      'white-space:pre-wrap;" id="work_ai_' + i + '">' +
      escHtml((w.aiOutput || '').slice(0, 300)) + (w.aiOutput && w.aiOutput.length > 300 ? '…' : '') +
      '</div>' +
      '<div style="display:flex;gap:8px;">' +
      '<button class="lh-btn lh-btn-ghost" style="padding:5px 10px;font-size:0.52rem;" ' +
      'onclick="window.FincyLH.copyText(\'work_ai_' + i + '\')">📋 Copy Output</button>' +
      '<button class="lh-btn lh-btn-ghost" style="padding:5px 10px;font-size:0.52rem;" ' +
      'onclick="document.getElementById(\'lhTaskInput\') && (document.getElementById(\'lhTaskInput\').value=' +
      JSON.stringify(w.userInput || '') + '); window.FincyLH.closeModal();">↩ Reuse Prompt</button>' +
      '</div></div>'
    );
  });

  html += '</div>';
  openModal(html, '◆ My AI Work (' + works.length + ')');
}

/* ── FEATURE 4: AI MEMORY SYSTEM ──────────────────────────── */

/**
 * handleAIMemory(sysPrompt, userText)
 * Builds message array with last 3 conversations as context.
 * Returns messages array for Groq API.
 */
function handleAIMemory(sysPrompt, userText) {
  var p      = loadProgress();
  var memory = p.aiMemory || [];

  var msgs = [{ role: 'system', content: sysPrompt }];

  // Inject last 3 turns as context (6 messages: user+assistant each)
  var recent = memory.slice(-3);
  recent.forEach(function(turn) {
    if (turn.user) msgs.push({ role: 'user',      content: turn.user });
    if (turn.ai)   msgs.push({ role: 'assistant', content: turn.ai   });
  });

  msgs.push({ role: 'user', content: userText });
  return msgs;
}

/**
 * _storeAIMemory(userText, aiResponse)
 * Stores the latest exchange. Keeps last 3 only.
 */
function _storeAIMemory(userText, aiResponse) {
  var p      = loadProgress();
  p.aiMemory = p.aiMemory || [];
  p.aiMemory.push({
    lessonId: _activeLesson ? _activeLesson.id : 'unknown',
    user: userText,
    ai:   aiResponse.slice(0, 600)  // trim to avoid storage bloat
  });
  if (p.aiMemory.length > 3) p.aiMemory = p.aiMemory.slice(-3);
  saveProgress(p);
}

/* ── FEATURE 5: AUTO NEXT LESSON ──────────────────────────── */

/**
 * goToNextLesson(si, mi, li)
 * Advances to next lesson automatically.
 * Handles module and stage boundaries.
 */
function goToNextLesson(si, mi, li) {
  var stage = FINCY_COURSE.stages[si];
  var mod   = stage.modules[mi];

  if (li < mod.lessons.length - 1) {
    // Next lesson in same module
    loadLesson(si, mi, li + 1);
  } else if (mi < stage.modules.length - 1) {
    // First lesson of next module
    loadModule(si, mi + 1);
  } else if (si < FINCY_COURSE.stages.length - 1) {
    // Next stage
    loadStage(si + 1);
  } else {
    // All done!
    openModal(
      '<div style="text-align:center;padding:40px 20px;">' +
      '<div style="font-size:2.5rem;margin-bottom:12px;">🏆</div>' +
      '<div style="font-family:Playfair Display,serif;font-size:1.4rem;font-weight:900;' +
      'color:var(--gold);margin-bottom:10px;">Course Complete!</div>' +
      '<div style="font-size:0.84rem;color:var(--text2);line-height:1.8;max-width:400px;margin:0 auto;">' +
      'You have completed all 4 stages of the Fincy AI Finance certification. ' +
      'You are now in the top 5% of finance professionals in AI capability.</div>' +
      '<div style="margin-top:20px;display:flex;gap:10px;justify-content:center;">' +
      '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.showBadges()">View Your Badges →</button>' +
      '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.showMyWork()">View My AI Work →</button>' +
      '</div></div>',
      '◆ 🏆 Certification Complete'
    );
  }
}

/* ── FEATURE 6: PSYCHOLOGICAL HOOKS ───────────────────────── */

var _PSYCH_HOOKS = [
  'You just automated a 2-hour finance task. 🤖',
  'This is a CFO-level skill. Very few analysts have it. 📊',
  'Top 10% of FP&A professionals use this exact technique.',
  'This skill can increase your salary by ₹2-5L. Keep going. 💰',
  'Senior managers spend hours on this. You can do it in 60 seconds.',
  'You are building skills most finance teams will not have for 5 years.',
  'Every lesson here is a bullet point on your CV. 🏆',
  'McKinsey analysts use this approach in board presentations.',
  'You are now more productive than 80% of your peers in this skill.',
  'Finance + AI = the rarest combination in today\'s job market.'
];

function _showPsychHook(outputEl) {
  // Show after a short delay so user reads the AI response first
  setTimeout(function() {
    var hook = _PSYCH_HOOKS[Math.floor(Math.random() * _PSYCH_HOOKS.length)];
    var hookEl = document.createElement('div');
    hookEl.style.cssText = (
      'margin-top:10px;background:rgba(201,168,76,0.08);' +
      'border:1px solid rgba(201,168,76,0.2);' +
      'padding:10px 14px;font-size:0.76rem;color:var(--text2);' +
      'font-style:italic;animation:lhFadeIn 0.5s ease;'
    );
    hookEl.textContent = hook;
    if (outputEl && outputEl.parentNode) {
      outputEl.parentNode.insertBefore(hookEl, outputEl.nextSibling);
    }
  }, 1500);
}

/* ── FEATURE 7: FLOATING MESSAGE SYSTEM ───────────────────── */

function _showFloatingMsg(msg) {
  var el = document.createElement('div');
  el.style.cssText = (
    'position:fixed;bottom:140px;right:24px;z-index:10000;' +
    'background:#101010;border:1px solid var(--gold);' +
    'padding:12px 18px;max-width:280px;' +
    'font-size:0.78rem;color:var(--text2);' +
    'animation:lhSlideIn 0.3s ease;box-shadow:0 4px 20px rgba(0,0,0,0.6);'
  );
  el.textContent = msg;
  document.body.appendChild(el);
  setTimeout(function(){ el.remove(); }, 4000);
}

/* ── STREAK DISPLAY HELPERS ───────────────────────────────── */
function _buildStreakBadgeRowHtml() {
  var p   = loadProgress();
  var s   = getStreakDisplay();
  p.badges = p.badges || [];
  var earnedCount    = p.badges.length;
  var totalBadges    = BADGES.length;
  var xp             = p.xp || 0;
  var level          = Math.floor(xp / 100) + 1;
  var xpInLevel      = xp % 100;
  var doneToday      = p.lessonsCompletedToday || 0;
  var dailyGoal      = p.dailyGoal || 2;
  var goalDone       = doneToday >= dailyGoal;

  return (
    // Streak pill
    '<div style="display:flex;align-items:center;gap:8px;background:var(--s);' +
    'border:1px solid var(--b);padding:7px 14px;" title="Daily streak">' +
    '<span style="font-size:1rem;" id="streakEmoji">' + s.emoji + '</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
    'letter-spacing:0.1em;text-transform:uppercase;color:var(--gold);" id="streakLabel">' +
    s.days + ' day streak</span>' +
    '</div>' +
    // XP + Level pill
    '<div style="display:flex;align-items:center;gap:8px;background:var(--s);' +
    'border:1px solid var(--b);padding:7px 14px;" title="XP and Level">' +
    '<span style="font-size:0.9rem;">⚡</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
    'letter-spacing:0.1em;text-transform:uppercase;color:var(--gold);" id="lhLevelBadge">' +
    'Lv.' + level + '</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;' +
    'color:var(--text3);" id="lhXPLabel">' + xp + ' XP</span>' +
    '</div>' +
    // Daily goal pill
    '<div style="display:flex;align-items:center;gap:8px;background:var(--s);' +
    'border:1px solid ' + (goalDone ? 'var(--green)' : 'var(--b)') + ';padding:7px 14px;">' +
    '<span style="font-size:0.9rem;">' + (goalDone ? '✅' : '🎯') + '</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
    'letter-spacing:0.1em;text-transform:uppercase;' +
    'color:' + (goalDone ? 'var(--green)' : 'var(--gold)') + ';" id="dailyGoalLabel">' +
    doneToday + '/' + dailyGoal + ' today</span>' +
    '</div>' +
    // Badges pill
    '<div style="display:flex;align-items:center;gap:8px;background:var(--s);' +
    'border:1px solid var(--b);padding:7px 14px;cursor:pointer;" ' +
    'onclick="window.FincyLH.showBadges()" title="View all badges">' +
    '<span style="font-size:0.9rem;">🏅</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
    'letter-spacing:0.1em;text-transform:uppercase;color:var(--gold);">' +
    earnedCount + '/' + totalBadges + '</span>' +
    '</div>' +
    // My Work button
    '<div style="display:flex;align-items:center;gap:8px;background:var(--s);' +
    'border:1px solid var(--b);padding:7px 14px;cursor:pointer;" ' +
    'onclick="window.FincyLH.showMyWork()" title="View saved AI work">' +
    '<span style="font-size:0.9rem;">📁</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
    'letter-spacing:0.1em;text-transform:uppercase;color:var(--gold);" id="workCount">' +
    'My Work (' + ((p.savedWork || []).length) + ')</span>' +
    '</div>'
  );
}

function updateStreakDisplay() {
  var s  = getStreakDisplay();
  var p  = loadProgress();
  p.badges = p.badges || [];
  var xp    = p.xp || 0;
  var level = Math.floor(xp / 100) + 1;

  var upd = {
    streakEmoji:    s.emoji,
    streakLabel:    s.days + ' day streak',
    lhLevelBadge:  'Lv.' + level,
    lhXPLabel:     xp + ' XP',
    dailyGoalLabel: (p.lessonsCompletedToday || 0) + '/' + (p.dailyGoal || 2) + ' today',
    workCount:     'My Work (' + ((p.savedWork || []).length) + ')'
  };
  Object.keys(upd).forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.textContent = upd[id];
  });
  // Update daily goal border color
  var doneToday = p.lessonsCompletedToday || 0;
  var goalEl = document.getElementById('dailyGoalLabel');
  if (goalEl && goalEl.parentNode) {
    goalEl.parentNode.style.borderColor = doneToday >= (p.dailyGoal || 2) ? 'var(--green)' : 'var(--b)';
    goalEl.style.color = doneToday >= (p.dailyGoal || 2) ? 'var(--green)' : 'var(--gold)';
  }
}

/* ── INJECT INTERACTIVE ELEMENTS into existing LH cards ───── */
function initLearningHub() {
  injectEngineStyles();
  handleDailySystem();    // v4: run daily system check on every page load
  updateProgressBars();

  // Inject overall progress bar below the LH heading
  var lhSec = document.getElementById('learning');
  if (lhSec) {
    var existing = document.getElementById('lhOverallBar');
    if (!existing) {
      var count = getCompletedCount();
      var pct   = count.total > 0 ? Math.round(count.done / count.total * 100) : 0;
      var barEl = document.createElement('div');
      barEl.id  = 'lhOverallBar';
      barEl.style.cssText = 'margin:16px 0 0;padding:0 0 8px;';
      barEl.innerHTML =
        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">' +
        '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.12em;' +
        'text-transform:uppercase;color:var(--text3);">Overall Progress</span>' +
        '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--gold);" id="lhOverallLabel">' +
        count.done + '/' + count.total + ' lessons (' + pct + '%)</span>' +
        '</div>' +
        '<div class="lh-progress-bar"><div class="lh-progress-fill" id="lhOverallProgress" style="width:' + pct + '%;"></div></div>';

      // Insert after the "Why This Matters" banner
      var banner = lhSec.querySelector('[style*="818cf8"]');
      if (banner && banner.parentNode) {
        banner.parentNode.insertBefore(barEl, banner.nextSibling);
      } else {
        lhSec.insertBefore(barEl, lhSec.firstChild.nextSibling);
      }
    }
  }

  // ── Inject streak + badges row below the overall progress bar ──
  updateStreak();
  var streakBadgeRow = document.getElementById('lhStreakBadgeRow');
  if (!streakBadgeRow) {
    var sRow = document.createElement('div');
    sRow.id = 'lhStreakBadgeRow';
    sRow.style.cssText = 'display:flex;align-items:center;gap:14px;margin-bottom:16px;flex-wrap:wrap;';
    sRow.innerHTML = _buildStreakBadgeRowHtml();
    var overallBar = document.getElementById('lhOverallBar');
    if (overallBar && overallBar.parentNode) {
      overallBar.parentNode.insertBefore(sRow, overallBar.nextSibling);
    }
  }

  // Wire stage card buttons to loadStage()
  FINCY_COURSE.stages.forEach(function(stage, si) {
    var btn = document.getElementById('lh-stage-btn-' + si);
    if (btn) {
      btn.onclick = function(e) { e.stopPropagation(); window.FincyLH.loadStage(si); };
    }

    // Add progress bar to each card
    var stageDone = 0, stageTotal = 0;
    stage.modules.forEach(function(m){
      m.lessons.forEach(function(l){
        stageTotal++;
        if (isLessonDone(l.id)) stageDone++;
      });
    });
    var stagePct = stageTotal > 0 ? Math.round(stageDone/stageTotal*100) : 0;
    var progEl = document.getElementById('lh-stage-prog-' + si);
    if (progEl) progEl.textContent = stageDone + '/' + stageTotal + ' lessons';
    var barEl = document.getElementById('lh-stage-bar-' + si);
    if (barEl) barEl.style.width = stagePct + '%';
  });
}

/* ── PUBLIC API ────────────────────────────────────────────── */
window.FincyLH = {
  loadStage:        loadStage,
  loadModule:       loadModule,
  loadLesson:       loadLesson,
  handleAIRequest:  handleAIRequest,
  markComplete:     markComplete,
  loadProject:      loadProject,
  useExample:       useExample,
  closeModal:       closeModal,
  downloadTemplate: downloadTemplate,
  showBadges:       function(){ openModal(getBadgePanel(), '◆ Your Badges'); },
  copyText: function(elemId) {
    var el = document.getElementById(elemId);
    if (!el) return;
    var text = el.innerText || el.textContent || '';
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(function(){
        var btn = el.nextElementSibling;
        if (btn) { var orig=btn.textContent; btn.textContent='✓ Copied!'; setTimeout(function(){ btn.textContent=orig; }, 1500); }
      });
    } else {
      var ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand('copy'); document.body.removeChild(ta);
    }
  },
  copyShareLink: function() {
    var url = 'https://jitenparida95.github.io/fincy-intelligence/#learning';
    if (navigator.clipboard) navigator.clipboard.writeText(url);
    alert('Link copied: ' + url);
  },
  goToNextLesson:  goToNextLesson,
  showMyWork:      showMyWork,
  handleDailySystem: handleDailySystem,
  updateXP:        updateXP,
  saveUserWork:    saveUserWork,
  handleAIMemory:  handleAIMemory,
  resetProgress: function(){
    localStorage.removeItem(PROGRESS_KEY);
    updateProgressBars();
    updateStreakDisplay();
    closeModal();
    alert('Progress reset.');
  }
};

/* ── AUTO-INIT on DOM ready ────────────────────────────────── */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initLearningHub);
} else {
  initLearningHub();
}
