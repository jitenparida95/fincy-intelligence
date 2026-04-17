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

/* ── PROGRESS STORAGE ──────────────────────────────────────── */
var PROGRESS_KEY = 'fincy_learn_v2';

function loadProgress() {
  try {
    var raw = localStorage.getItem(PROGRESS_KEY);
    return raw ? JSON.parse(raw) : {
      completedLessons: [],   // ['l01_01_01', ...]
      completedStages:  [],   // ['stage_01', ...]
      currentStage: 'stage_01',
      currentLesson: null,
      totalPoints: 0
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
  if (stagePct === 100) {
    html += '<div style="margin-top:20px;background:rgba(74,222,128,0.08);border:1px solid var(--green);' +
      'padding:14px 18px;text-align:center;">' +
      '<div style="color:var(--green);font-family:IBM Plex Mono,monospace;font-size:0.56rem;' +
      'letter-spacing:0.1em;text-transform:uppercase;">🎉 Stage Complete!</div>' +
      (stageIdx < FINCY_COURSE.stages.length-1 ?
        '<div style="margin-top:8px;"><button class="lh-btn lh-btn-green" onclick="window.FincyLH.loadStage(' + (stageIdx+1) + ')">Unlock Stage ' + (stageIdx+2) + ' →</button></div>' : '') +
      '</div>';
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
  var msgs = [
    { role: 'system', content: sysPrompt },
    { role: 'user',   content: userText }
  ];

  if (!groqKey) {
    // Fallback — redirect to Fincy app
    setTimeout(function() {
      output.innerHTML =
        'For AI-powered lesson responses, open Fincy Intelligence app → Learning Hub.<br><br>' +
        '<a href="https://fincy-intelligence.streamlit.app/?m=learning" target="_blank" ' +
        'style="color:var(--gold);font-family:IBM Plex Mono,monospace;font-size:0.65rem;' +
        'letter-spacing:0.08em;text-transform:uppercase;">Open Full Learning Hub →</a>';
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
  })
  .catch(function(e){
    output.innerHTML = '<span style="color:var(--red);">Error: ' + e.message + '</span>';
  });
}

/* ── MARK COMPLETE ─────────────────────────────────────────── */
function markComplete(lessonId, stageIdx, moduleIdx, lessonIdx) {
  var p = loadProgress();
  if (p.completedLessons.indexOf(lessonId) < 0) {
    p.completedLessons.push(lessonId);
    p.totalPoints += 10;
  }
  // Check if stage is now complete
  var stage = FINCY_COURSE.stages[stageIdx];
  var allLessons = [];
  stage.modules.forEach(function(m){ m.lessons.forEach(function(l){ allLessons.push(l.id); }); });
  if (allLessons.every(function(id){ return p.completedLessons.indexOf(id) >= 0; })) {
    if (p.completedStages.indexOf(stage.id) < 0) p.completedStages.push(stage.id);
  }
  saveProgress(p);
  updateProgressBars();
  // Reload lesson view with complete badge
  loadLesson(stageIdx, moduleIdx, lessonIdx);
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

  // Temporarily override activeLesson ai_prompt for project
  _activeLesson = { ai_prompt: project.ai_prompt, id: 'project_' + stageIdx + '_' + moduleIdx };
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

/* ── INJECT INTERACTIVE ELEMENTS into existing LH cards ───── */
function initLearningHub() {
  injectEngineStyles();
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
  loadStage:       loadStage,
  loadModule:      loadModule,
  loadLesson:      loadLesson,
  handleAIRequest: handleAIRequest,
  markComplete:    markComplete,
  loadProject:     loadProject,
  useExample:      useExample,
  closeModal:      closeModal,
  resetProgress:   function(){
    localStorage.removeItem(PROGRESS_KEY);
    updateProgressBars();
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
