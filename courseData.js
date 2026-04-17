/* ============================================================
   FINCY LEARNING HUB — Course Data + Interactive Engine
   Version 2.0 | Vanilla JS | No frameworks | Groq AI
   ============================================================ */

'use strict';

/* ── COURSE DATA STRUCTURE ─────────────────────────────────── */
var FINCY_COURSE = {

  stages: [

    /* ═══════════════════════════════════════════════════════
       STAGE 01 — BEGINNER | 20 Lessons | AI in Finance Basics
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_01', badge: '01 / BEGINNER', color: '#c9a84c',
      title: 'AI in Finance Basics',
      tagline: 'Understand what AI is and why it changes everything for finance professionals.',
      unlocked: true,
      modules: [

        /* MODULE 1 */
        {
          id: 'm01_01', title: 'What is AI? (For Finance People)',
          lessons: [
            {
              id: 'l01_01_01', title: 'LLMs Explained in Finance Terms',
              level: 'beginner', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 1,
              explanation: 'A Large Language Model (LLM) like Llama or GPT is trained on billions of documents. It generates structured answers from your questions — like a tireless senior analyst. In finance, ask "Why is EBITDA declining?" and get a CFO-level response in seconds.',
              example: 'You upload a P&L CSV and ask: "Which market has the worst margin trend?" The LLM replies: "Germany — EBITDA margin fell from 18% to 11% in Q3, driven by COGS inflation (+7%) and flat volume."',
              task: 'Write one finance question you wish your team could answer faster. Click Ask AI to see how an LLM responds.',
              ai_prompt: 'You are a senior FP&A analyst. The user is a finance professional learning about AI. Answer their finance question in 3-4 sentences as an AI CFO — direct, with numbers, no fluff.',
              expected_output: 'A concise CFO-style finance answer with specific reasoning.'
            },
            {
              id: 'l01_01_02', title: 'AI Agents vs LLMs — What\'s the Difference?',
              level: 'beginner', type: 'concept',
              track: ['Automation'], difficulty_score: 1,
              explanation: 'An LLM answers questions. An AI Agent takes actions. Fincy\'s Data Analysis Agent reads your CSV, runs statistics, builds charts, and writes commentary — one click, zero Excel. LLM = smart advisor. Agent = smart employee.',
              example: 'LLM: "Your DSO is high." Agent: reads AR data → calculates DSO → flags customers over 60 days → generates collections priority list → saves CSV. One click.',
              task: 'Name one repetitive finance task taking 2+ hours. Ask AI how an agent could automate it.',
              ai_prompt: 'You are an AI automation expert for Finance teams. The user will describe a repetitive task. Explain step-by-step how an AI agent could automate it with specific tools (Python, Pandas, Groq). Be practical.',
              expected_output: 'Step-by-step automation plan with specific tools named.'
            },
            {
              id: 'l01_01_03', title: 'The 5 Finance Tasks AI Does Better Than Excel',
              level: 'beginner', type: 'concept',
              track: ['FP&A','Automation'], difficulty_score: 1,
              explanation: 'Excel is a calculator. AI is a reasoning engine. The 5 tasks where AI beats Excel: (1) Variance commentary — AI writes it in 3 seconds. (2) Anomaly detection — AI spots what you miss. (3) Scenario modeling — AI runs 100 scenarios instantly. (4) Reconciliation — AI matches across messy data. (5) Forecasting — AI incorporates patterns Excel cannot see.',
              example: 'A team using Excel for month-end commentary: 3 hours per analyst × 4 analysts = 12 hours. Same team using Fincy AI: 4 minutes total. The 12 hours are now spent on decisions, not writing.',
              task: 'Ask AI: "For my specific finance role, which of these 5 tasks would save me the most time? Give me a specific estimate in hours per month."',
              ai_prompt: 'You are a senior FP&A advisor. The user works in finance. Based on their role description, calculate which AI tasks would save them the most time. Give specific hour estimates per month for each of the 5 tasks (variance commentary, anomaly detection, scenario modeling, reconciliation, forecasting). Be specific and realistic.',
              expected_output: 'Ranked list of 5 tasks with specific hours saved per month for their role.'
            },
            {
              id: 'l01_01_04', title: 'Practical Task — Write Your First AI Finance Prompt',
              level: 'beginner', type: 'task',
              track: ['FP&A','CFO Strategy'], difficulty_score: 2,
              explanation: 'A great finance prompt has 4 parts: Role (who the AI should be), Context (your actual financial data), Task (what output you need), Format (exactly how it should look). Missing any part drops quality by 50%.',
              example: '"You are a CFO advising a CEO. EBITDA margin is 12% vs 18% budget. Revenue grew 8% YoY but COGS rose 15%. Write 2-paragraph board commentary: paragraph 1 = what happened with numbers, paragraph 2 = what we will do. No bullet points. Executive tone."',
              task: 'Write a prompt for a real finance task from your job using the 4-part structure (Role + Context + Task + Format). Then ask AI to evaluate it.',
              ai_prompt: 'You are a prompt engineering coach for CFOs. Score the user\'s finance prompt on: Role clarity (0-25), Data context (0-25), Task specificity (0-25), Format instructions (0-25). Total /100. Then rewrite it to score 90+. Show the improved version.',
              expected_output: 'Score /100 with improvement breakdown, then improved prompt.'
            },
            {
              id: 'l01_01_05', title: 'Case Study — How Fincy Saved 40 Hours/Month',
              level: 'beginner', type: 'case_study',
              track: ['FP&A'], difficulty_score: 2,
              explanation: 'Real case: An FP&A team at a consumer goods company spent 40 hours every month-end on variance commentary, reconciliation checks, and management reporting. After implementing AI tools (similar to Fincy), this dropped to 4 hours. The 36 hours freed were reinvested into strategic analysis that identified a ₹8M cost saving opportunity.',
              example: 'The team\'s workflow: Upload ERP data → AI runs variance analysis → AI writes commentary → Human reviews and adjusts → Board pack done. Total AI time: 12 minutes. Human review time: 48 minutes. Previous manual time: 40 hours.',
              task: 'Calculate the financial value of your own time saved. If you earn ₹15L/year and AI saves you 20 hours/month, what is the annual value? Ask AI to help you build the business case for your manager.',
              ai_prompt: 'You are a CFO helping a finance professional build a business case for AI tools. The user will share their salary and time savings estimate. Calculate: annual cost of current manual time, ROI of AI tools, productivity gain percentage, and write a 3-sentence business case they can send to their manager.',
              expected_output: 'Business case with Rs figures, ROI %, and a 3-sentence manager pitch.'
            }
          ],
          project: {
            title: 'Project: Map Your AI Opportunity',
            instructions: 'Create an "AI Opportunity Map" for your finance role. List your top 5 most time-consuming tasks, estimate hours per month, and describe how AI could automate or accelerate each. Use the AI to validate your estimates and add tasks you may have missed.',
            ai_prompt: 'You are a senior AI strategy consultant for Finance teams. Review the user\'s AI Opportunity Map. For each task: (1) validate their time estimate, (2) recommend the specific AI approach, (3) score the automation potential (1-5), (4) estimate % time reduction. Output a clean table with all these columns.'
          }
        },

        /* MODULE 2 */
        {
          id: 'm01_02', title: 'How Fincy Uses AI (Under the Hood)',
          lessons: [
            {
              id: 'l01_02_01', title: 'Groq + Llama 3.1 — The Engine Inside Fincy',
              level: 'beginner', type: 'concept',
              track: ['Automation'], difficulty_score: 1,
              explanation: 'Fincy uses Groq\'s inference API with Llama 3.1 (8B instant model). Groq is hardware-accelerated — responses in under 1 second. Llama 3.1 is Meta\'s open-source model — no OpenAI dependency, no per-token cost explosion. This is why Fincy can offer AI CFO capabilities at a fraction of ChatGPT\'s cost.',
              example: 'When you ask "Why is my gross margin below 50%?" — Fincy sends your CSV summary + question to Groq → Llama 3.1 analyses → response in 800ms → displayed on screen.',
              task: 'Ask AI: "How does a Groq API call work? Give me Python code for a simple finance query."',
              ai_prompt: 'You are a Python developer teaching finance professionals. Show exact Python code to call the Groq API with a finance CFO system prompt. Use llama-3.1-8b-instant. Include: API key setup, system prompt, user message, print response. Under 25 lines with comments.',
              expected_output: 'Working Python code under 25 lines with clear comments.'
            },
            {
              id: 'l01_02_02', title: 'Challenge — Design Your Own AI CFO',
              level: 'beginner', type: 'challenge',
              track: ['CFO Strategy'], difficulty_score: 3,
              explanation: 'Now you understand how AI works. Design what YOUR ideal AI CFO would do. What questions would it answer? What data would it need? What format would its output be? This is the thinking that separates AI-enabled CFOs from everyone else.',
              example: 'A well-designed AI CFO for an FMCG company: inputs = weekly sales data, competitor pricing, weather data. Outputs = demand forecast, promo ROI, distribution gap alerts. Decision support = go/no-go on price increases with margin impact.',
              task: 'Design your personal AI CFO. Describe: (1) The 3 most important questions it should answer, (2) What data it needs, (3) What format outputs should be in. Then ask AI to evaluate and improve your design.',
              ai_prompt: 'You are the Chief Technology Officer of Fincy Intelligence. Review the user\'s AI CFO design. Score it on: business impact (1-5), data feasibility (1-5), output clarity (1-5). Total /15. Then add 2 features they did not think of that would dramatically increase value. Be specific.',
              expected_output: 'Score /15 with detailed feedback plus 2 unexpected high-value additions.'
            },
            {
              id: 'l01_02_03', title: 'Simulation — You Are the AI CFO',
              level: 'beginner', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 3,
              explanation: 'Simulation: You are now acting as an AI CFO. A CEO gives you three financial questions. You must answer each within 60 seconds using structured CFO-style reasoning. This exercises your ability to think like an AI — structured, data-driven, decision-oriented.',
              example: 'CEO question: "Revenue is growing 8% but EBITDA is flat. Should I be worried?" AI CFO answer: "Yes — margin compression signals. COGS inflation or pricing power erosion. Priority: identify whether this is structural (COGS) or tactical (pricing). If COGS-driven, review supplier contracts this week. If pricing, test 3-5% price increase in one market."',
              task: 'The CEO asks you these 3 questions: (1) Cash is tight — should we delay capex or raise prices? (2) Sales team wants 15% more headcount — is now the right time? (3) EBITDA beat budget but cash flow missed — what is happening? Write your CFO response to all 3, then compare with what AI would say.',
              ai_prompt: 'You are a world-class CFO answering under pressure. Answer these 3 CEO questions concisely and decisively, using the format: ANSWER (one clear decision) | REASONING (2 specific data points) | ACTION (one measurable step with timeline). Be direct. No hedging.',
              expected_output: 'Three structured responses in ANSWER | REASONING | ACTION format.'
            }
          ],
          project: null
        }
,

        /* MODULE 3 — FP&A Fundamentals with AI */
        {
          id: 'm01_03', title: 'FP&A Fundamentals Supercharged by AI',
          lessons: [
            {
              id: 'l01_03_01', title: 'What is FP&A and Why AI Changes It Completely',
              level: 'beginner', type: 'concept',
              track: ['FP&A'], difficulty_score: 1,
              explanation: 'Financial Planning and Analysis (FP&A) is the function that provides management with financial insights for decision-making. Traditional FP&A: collect data → clean data → analyse → present. AI-powered FP&A: collect data → AI analyses → human validates → present. The human role shifts from data processing to insight validation and strategy.',
              example: 'Traditional: FP&A analyst spends 6 hours building a management pack in Excel. AI-powered: analyst uploads data to Fincy, AI generates pack in 4 minutes, analyst reviews and adjusts for context. 6 hours → 20 minutes. The analyst now has 5h40m for value-added work.',
              task: 'Describe your current FP&A reporting cycle. Ask AI to identify which steps could be AI-automated and estimate the time saving.',
              ai_prompt: 'You are a senior FP&A transformation consultant. The user will describe their reporting cycle. Identify each step that is: (A) fully automatable with AI today, (B) AI-assisted but needs human review, (C) requires human judgment only. For each automatable step, name the specific tool or approach. Calculate total time saving and express as percentage of current cycle time.',
              expected_output: 'Categorised list with automation approach per step + total % time saving.'
            },
            {
              id: 'l01_03_02', title: 'KPI Design — What Gets Measured Gets Managed',
              level: 'beginner', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 2,
              explanation: 'The best KPIs are leading indicators (predict future performance) not just lagging indicators (report past performance). Revenue is lagging. Pipeline conversion rate is leading. DSO is lagging. Days sales current is leading. AI can help identify which metrics in your data are most predictive of the outcomes you care about.',
              example: 'Bad KPI set: Revenue, EBITDA, Headcount (all lagging). Good KPI set: Revenue per FTE (efficiency), Customer acquisition cost vs LTV (economics), Cash conversion cycle (liquidity), Budget accuracy % (planning quality). AI can correlate 50+ metrics to find which ones actually predict EBITDA performance.',
              task: 'List your current 5 KPIs. Ask AI to identify which are leading vs lagging and suggest 3 better predictive KPIs for your business.',
              ai_prompt: 'You are a strategy and performance management expert. The user will share their KPIs. For each: classify as Leading or Lagging and explain why. Then suggest 3 new KPIs that are more predictive of their business outcomes, with data source for each and target-setting guidance.',
              expected_output: 'Leading/lagging classification per KPI + 3 new predictive KPIs with data sources.'
            },
            {
              id: 'l01_03_03', title: 'Budgeting vs Forecasting — Know the Difference',
              level: 'beginner', type: 'concept',
              track: ['FP&A'], difficulty_score: 2,
              explanation: 'Budget: annual commitment set at year start, used for performance evaluation. Forecast: rolling view of expected outcomes, updated as information changes. The best FP&A teams separate them — budget for accountability, rolling forecast for decision-making. AI makes rolling forecasting practical by automating the data refresh.',
              example: 'Budget (fixed): Revenue ₹180M for FY2026, set in October 2025. Rolling forecast (month 3): Revenue now expected ₹172M — market slower than expected. Decision: hold pricing to protect margin or cut price to recover volume? This is where FP&A adds value — the budget tells you there is a problem, the forecast tells you how big, the FP&A team tells you what to do.',
              task: 'Ask AI: "What is the difference between a budget, a rolling forecast, and a reforecast? Give me a practical example of when each is used in a consumer goods company."',
              ai_prompt: 'You are a CFO teaching FP&A fundamentals to an analyst. Explain: (1) Budget — definition, purpose, when set, limitations. (2) Rolling forecast — why it exists, cadence, advantages. (3) Reforecast — what triggers one, how it differs. Give a real example of all three in the same company in the same year showing why you need all three. End with: "The mistake most companies make is..."',
              expected_output: 'Three-part explanation with real example + common mistake identified.'
            },
            {
              id: 'l01_03_04', title: 'Working Capital — The Hidden Cash Lever',
              level: 'beginner', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 2,
              explanation: 'Working capital = Current Assets − Current Liabilities. More practically: Cash + Receivables + Inventory − Payables. Most companies focus on P&L (profits) but ignore working capital (cash timing). A company can be profitable and cash-negative. AI can model working capital scenarios and identify the fastest levers.',
              example: 'Company A: ₹50M profit. DSO 90 days, DPO 30 days, DIO 60 days. Cash conversion cycle = 120 days. Every ₹1M revenue growth locks up ₹0.33M cash. Growth is cash-negative.
Company B: same profit. DSO 45 days, DPO 60 days, DIO 30 days. CCC = 15 days. Growth is almost self-funding.',
              task: 'Calculate your Cash Conversion Cycle: DSO + DIO − DPO. Ask AI what it means for your business and how to improve it by 20 days.',
              ai_prompt: 'You are a CFO and working capital specialist. The user gives you their DSO, DIO, and DPO. Calculate their Cash Conversion Cycle. Benchmark against industry averages. Identify the biggest improvement opportunity. Model what a 20-day CCC reduction means in cash terms (assume ₹X revenue). Give 3 specific actions to achieve the improvement.',
              expected_output: 'CCC calculation + benchmark + cash impact of 20-day improvement + 3 actions.'
            }
          ],
          project: {
            title: 'Project: Design Your FP&A Dashboard',
            instructions: 'Design the ideal FP&A dashboard for your role. Specify: 5-8 KPIs, data sources for each, update frequency, and how AI would generate the commentary. Present as a mock layout (describe it) and ask AI to critique and improve it.',
            ai_prompt: 'You are a data visualisation and FP&A expert. The user has designed a management dashboard. Evaluate: completeness (are the right metrics here?), hierarchy (is most important information prominent?), actionability (does each metric drive a decision?), AI integration (where would AI add most value?). Score /20. Redesign the metric set to score 18+.'
          }
        },

        /* MODULE 4 — AI Thinking for Finance */
        {
          id: 'm01_04', title: 'AI Thinking for Finance Professionals',
          lessons: [
            {
              id: 'l01_04_01', title: 'How to Think Like an AI Prompt Engineer',
              level: 'beginner', type: 'task',
              track: ['FP&A','CFO Strategy'], difficulty_score: 2,
              explanation: 'Prompt engineering is not coding — it is structured communication. The same way a good manager gives clear briefs, a good prompt engineer gives AI clear instructions. Three principles: (1) Be specific — vague prompts give vague outputs. (2) Give context — AI cannot guess what it does not know. (3) Define the format — AI will use whatever format you specify.',
              example: 'Vague: "Analyse my P&L." → Generic analysis with no value.
Specific: "You are a CFO. Revenue is ₹42M (+8% YoY), EBITDA is ₹11M (margin 26.2% vs 28.0% budget). Identify the 2 most likely causes of margin compression and recommend a specific action for each with estimated impact." → Actionable, specific output.',
              task: 'Take a vague finance question you regularly ask. Rewrite it using the 3 principles (specific, context, format). Ask AI both versions and compare the quality of output.',
              ai_prompt: 'You are a prompt quality evaluator. The user gives you two versions of the same finance question — one vague, one improved. Compare the output quality you would generate from each. Rate each on: specificity (1-5), context richness (1-5), format clarity (1-5). Calculate improvement score. Explain in one sentence why the better prompt extracts more value.',
              expected_output: 'Side-by-side scores for both prompts + one-sentence insight.'
            },
            {
              id: 'l01_04_02', title: 'When NOT to Use AI — Judgment Over Automation',
              level: 'beginner', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 2,
              explanation: 'AI is powerful but not omniscient. It fails at: (1) Real-time data (it does not know what happened yesterday), (2) Qualitative judgments requiring relationship context ("Should we extend credit to this customer?"), (3) Novel situations with no precedent in training data. The best FP&A professionals know when to use AI and when human judgment is irreplaceable.',
              example: 'Use AI for: variance commentary (structured, pattern-based), scenario modelling (calculation-heavy), first draft of reports.
Do NOT use AI for: decisions involving confidential competitive intelligence, communications requiring personal relationship context, situations where the cost of error is catastrophic (never auto-post journal entries without review).',
              task: 'List 3 decisions you made last month. Ask AI to classify each as: "High AI value", "AI-assisted", or "Human judgment only" — and explain why.',
              ai_prompt: 'You are a CFO and AI ethics expert for finance. The user will describe 3 decisions they made recently. For each: classify as High AI value / AI-assisted / Human judgment only. Explain in 2 sentences why. Then give one example of a catastrophic mistake that could happen if AI was used inappropriately in a finance context.',
              expected_output: 'Classification for each decision with reasoning + cautionary example.'
            },
            {
              id: 'l01_04_03', title: 'Simulation — Interview: CFO Asks About AI',
              level: 'beginner', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 3,
              explanation: 'You are in a job interview for a Senior FP&A Analyst role. The CFO interviewer asks: "How do you see AI changing FP&A in the next 3 years? What have you personally done to prepare?" This is now a standard question at top companies. Your answer determines whether you are seen as forward-thinking or behind the curve.',
              example: 'Strong answer structure: (1) Acknowledge the trend with specifics — "AI will automate 60%+ of data processing in FP&A within 3 years." (2) Show personal preparation — "I have built AI-powered tools using Groq and Streamlit, automating variance analysis that previously took 2 hours." (3) Show strategic thinking — "The value shifts to insight generation and stakeholder influence, not data manipulation."',
              task: 'Write your answer to this interview question. Then ask AI to play the CFO interviewer and give you challenging follow-up questions.',
              ai_prompt: 'You are a demanding CFO interviewing a Senior FP&A candidate. They have just answered your question about AI in FP&A. Ask 4 follow-up questions that progressively test: (1) Depth of AI knowledge, (2) Practical experience with AI tools, (3) Critical thinking about AI limitations, (4) Strategic vision for FP&A. After each question, note what a weak vs strong candidate answer would look like.',
              expected_output: '4 follow-up questions with weak vs strong answer contrast.'
            },
            {
              id: 'l01_04_04', title: 'Challenge — Build the Business Case for AI in Your Team',
              level: 'beginner', type: 'challenge',
              track: ['CFO Strategy','FP&A'], difficulty_score: 4,
              explanation: 'Your manager asks you to justify implementing AI tools in your finance team. You need a business case with: (1) Quantified time saving, (2) Quality improvement evidence, (3) Cost of implementation, (4) ROI calculation, (5) Risk mitigation. This is a common real-world challenge — and AI can help you build it.',
              example: 'Business case structure: Current state cost (team size × hours on automatable tasks × hourly rate), Future state cost (tool cost + implementation + training), Annual saving, Payback period, Risk (data security, model accuracy, change management). A ₹5,000/month tool saving 80 hours/month at ₹1,000/hour = 16× ROI.',
              task: 'Build a 1-page business case for AI tools in your team. Use real or estimated numbers. Ask AI to stress-test your assumptions and identify weaknesses your CFO would spot.',
              ai_prompt: 'You are a CFO reviewing a business case for AI tool investment. The user presents their case. Play devil's advocate: identify the 3 weakest assumptions, the biggest risk they have understated, and the question the board will definitely ask that they have not answered. Then rewrite the executive summary in CFO language — punchy, number-driven, with a clear recommendation.',
              expected_output: '3 weak assumptions + biggest risk + board question + rewritten executive summary.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 02 — INTERMEDIATE | 25 Lessons | Finance Automation
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_02', badge: '02 / INTERMEDIATE', color: '#4ade80',
      title: 'Automating Finance Work',
      tagline: 'Eliminate manual work. Build automation that runs every month-end in seconds.',
      unlocked: false,
      modules: [

        /* MODULE 1 */
        {
          id: 'm02_01', title: 'Python for Finance — The 20% You Need',
          lessons: [
            {
              id: 'l02_01_01', title: 'Pandas for FP&A — Read, Filter, Summarise',
              level: 'intermediate', type: 'concept',
              track: ['Automation','FP&A'], difficulty_score: 2,
              explanation: 'Pandas is Excel but 100× faster and scriptable. Read a CSV, filter by market, group by brand, calculate variance — in 5 lines. Once scripted it runs every month in 2 seconds instead of 2 hours.',
              example: 'import pandas as pd\ndf = pd.read_csv("pl_data.csv")\ndf["Variance"] = df["Actual"] - df["Budget"]\nsummary = df.groupby("Market")["Variance"].sum().sort_values()\nprint(summary)',
              task: 'Ask AI to write a Pandas script calculating budget variance by market from a CSV with columns: Market, Brand, Actual_Revenue, Budget_Revenue.',
              ai_prompt: 'You are a Python/Pandas expert for finance professionals. Write a complete, runnable script that: reads a CSV with Market, Brand, Actual_Revenue, Budget_Revenue; calculates Variance and Variance%; groups by Market; sorts worst performers first; prints a clean table. Add comments on each line.',
              expected_output: 'Complete runnable script with line-by-line comments.'
            },
            {
              id: 'l02_01_02', title: 'Driver-Based Forecasting with Python',
              level: 'intermediate', type: 'concept',
              track: ['FP&A','Automation'], difficulty_score: 3,
              explanation: 'Driver-based forecasting links financial outputs to business drivers. Revenue = Volume × Price. COGS = Volume × Unit Cost. In Python, you define these relationships once and the model updates automatically when drivers change. This replaces static Excel forecast models.',
              example: 'volume = 1200  # units sold\nprice  = 850   # Rs per unit\ncogs_rate = 0.45\nrevenue = volume * price\ncogs    = revenue * cogs_rate\ngross_profit = revenue - cogs\nmargin_pct   = gross_profit / revenue * 100\nprint(f"Revenue: Rs{revenue:,} | GP: {margin_pct:.1f}%")',
              task: 'Build a driver-based model for your business. Define at least 4 drivers (e.g. volume, price, headcount, salary). Ask AI to write the Python code and then run a 10% volume decline scenario.',
              ai_prompt: 'You are a financial modelling expert. The user will describe their business drivers. Write Python code for a driver-based forecast model. Include: base case, +10% growth scenario, -10% decline scenario. Show output as a clean table with all 3 scenarios side by side. Add a "Key Insight" line explaining the most sensitive driver.',
              expected_output: 'Python driver model with 3-scenario output table and key insight.'
            },
            {
              id: 'l02_01_03', title: 'Automating Monthly Commentary',
              level: 'intermediate', type: 'task',
              track: ['FP&A','Automation'], difficulty_score: 2,
              explanation: 'The most time-consuming FP&A task is writing variance commentary. AI does this in seconds. You provide the numbers; the AI writes CFO-ready narrative. This is the highest-ROI automation in FP&A — typically 2 hours → 30 seconds.',
              example: 'Prompt: "EBITDA missed budget by ₹2.3M (−8%). Revenue was in line (+0.2%) but COGS spiked due to freight costs (+12% YoY) and promotional spending was 15% over plan. Write a 3-sentence board pack commentary."',
              task: 'Write a commentary prompt for your last month\'s actuals (real or hypothetical). Include revenue, margin, and 2 key drivers. Ask AI to generate board-ready commentary.',
              ai_prompt: 'You are a Senior FP&A Manager writing a board pack. User gives you financial variance data. Write exactly 3 sentences: 1) Headline vs budget with numbers. 2) Two specific driver explanations with percentages. 3) Outlook and corrective action. CFO language. No bullet points.',
              expected_output: '3 sentences of board-ready variance commentary.'
            },
            {
              id: 'l02_01_04', title: 'Margin Bridge Analysis — The CFO\'s Favourite Tool',
              level: 'intermediate', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 3,
              explanation: 'A margin bridge decomposes the change in gross margin into its components: Volume effect, Price effect, Mix effect, Cost effect. It answers "why did margin change?" with precision. CFOs use it to identify which lever to pull — price increase, cost reduction, or volume push.',
              example: 'Margin change: −3.2pp\nVolume effect: +1.1pp (sold more units)\nPrice effect: −2.0pp (price pressure)\nMix effect: +0.3pp (shifted to higher-margin SKUs)\nCost effect: −2.6pp (COGS inflation)\nTotal: −3.2pp ✓',
              task: 'You have: Prior year margin 54%, current year margin 49%. Revenue grew 6%, COGS grew 14%, volume grew 4%. Build a margin bridge and ask AI to identify the largest driver and recommend a corrective action.',
              ai_prompt: 'You are a CFO and financial modelling expert. Build a margin bridge from this data: PY margin 54%, CY margin 49%, revenue +6%, COGS +14%, volume +4%. Calculate Volume, Price, Mix, and Cost effects. Format as a table showing each effect in pp. Identify the largest driver. Give one specific corrective recommendation with expected margin recovery timeline.',
              expected_output: 'Margin bridge table in pp + largest driver identified + recommendation with timeline.'
            },
            {
              id: 'l02_01_05', title: 'Scenario Modelling — 3-Case Framework',
              level: 'intermediate', type: 'task',
              track: ['FP&A','CFO Strategy'], difficulty_score: 3,
              explanation: 'Every board needs to see 3 scenarios: Base (most likely), Bull (upside), Bear (downside). Effective scenario modelling identifies the key assumptions that differentiate each case and quantifies the range of outcomes. AI can generate all 3 in 10 seconds.',
              example: 'Base: Revenue ₹42.8M, EBITDA 28.3%\nBull: +15% volume, 30.1% EBITDA (price holds, no cost inflation)\nBear: −10% volume, 24.8% EBITDA (price pressure + COGS inflation +5%)',
              task: 'Define your current base case with 3 financial metrics. Ask AI to build Bull and Bear scenarios with specific assumptions and financial outcomes.',
              ai_prompt: 'You are a financial planning expert. The user gives you a base case. Build Bull and Bear scenarios. For each: state 3 key assumptions, show Revenue, EBITDA, Cash impact. Present as a clean 3-column table (Bear | Base | Bull). Add a "Trigger Events" row showing what would cause each scenario to materialise.',
              expected_output: '3-column scenario table with trigger events row.'
            },
            {
              id: 'l02_01_06', title: 'Case Study — FMCG Margin Collapse',
              level: 'intermediate', type: 'case_study',
              track: ['FP&A','CFO Strategy'], difficulty_score: 4,
              explanation: 'Real case study: A consumer goods company saw revenue flat at ₹180M but gross margin collapsed from 42% to 34% in one quarter. COGS increased 14% driven by commodity inflation. Marketing spend was held constant. The CFO needed to identify which markets and SKUs were destroying value.',
              example: 'The analysis revealed: 3 markets (representing 28% of revenue) were operating at negative contribution margin. The top 15 SKUs drove 80% of the margin decline. Price increases had lagged competitor moves by 90 days. Emergency action: immediate price increase on 8 SKUs + discontinue 4 loss-making SKUs.',
              task: 'You are the FP&A analyst on this case. Revenue is ₹180M, margin fell 8pp in one quarter. You have data by market and SKU. Write the AI prompt you would use to identify the root cause and recommend a recovery plan.',
              ai_prompt: 'You are a McKinsey-trained CFO who specialises in margin recovery. A consumer goods company\'s margin collapsed 8pp in one quarter. Revenue was flat at ₹180M. COGS rose 14%. Provide: (1) A structured root cause tree (4-5 potential causes with likelihood), (2) The 3 data analyses you would run first, (3) A 30/60/90 day recovery plan with specific margin targets. Use frameworks like waterfall analysis and contribution margin by segment.',
              expected_output: 'Root cause tree + 3 priority analyses + 90-day recovery plan with targets.'
            },
            {
              id: 'l02_01_07', title: 'Challenge — Fix the Business in 30 Days',
              level: 'intermediate', type: 'challenge',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'You are a new CFO. The business has: Revenue -8% vs budget, OPEX +12% vs budget, cash runway 5 months at current burn rate, 3 major customer contracts up for renewal next month. Make your 30-day plan.',
              example: 'A well-structured CFO response prioritises: (1) Cash conservation (immediate OPEX freeze, defer capex), (2) Revenue defence (personal calls to 3 at-risk customers), (3) Diagnostic (identify top 10 OPEX lines driving overspend), (4) Stakeholder management (board briefing with turnaround plan).',
              task: 'Write your 30-day CFO plan for this situation. Then ask AI to critique it and add what you missed.',
              ai_prompt: 'You are an experienced CFO who has led multiple business turnarounds. The user has written a 30-day plan for a business in distress. Critique it: (1) What did they get right (list 3 things), (2) What critical action is missing (list 2-3 gaps), (3) What is the biggest risk to their plan. Then rewrite the plan as a tight 10-point priority list in order of urgency. Each point must have a specific outcome target.',
              expected_output: 'Critique (right/missing/risks) + 10-point priority plan with outcome targets.'
            }
          ],
          project: {
            title: 'Project: Build a Variance Commentary Generator',
            instructions: 'Create a reusable AI prompt that takes any P&L data and generates board-ready commentary. Test it with 3 different scenarios: (1) Revenue miss + margin beat, (2) Revenue beat + OPEX overrun, (3) All metrics below budget. Your prompt must work without modification across all 3.',
            ai_prompt: 'You are a prompt engineering mentor for FP&A analysts. The user shares a variance commentary prompt. Test it against 3 scenarios they provide. Score output quality for each (1-5). Identify what structural improvement would make the prompt work for any P&L situation. Rewrite the prompt to score 5/5 across all scenarios.'
          }
        },

        /* MODULE 2 */
        {
          id: 'm02_02', title: 'Reconciliation & Accounting Automation',
          lessons: [
            {
              id: 'l02_02_01', title: 'ERP vs Bank — The Logic Behind Fincy Recon',
              level: 'intermediate', type: 'concept',
              track: ['Accounting','Automation'], difficulty_score: 2,
              explanation: 'Reconciliation matches two datasets and finds differences. Fincy uses a composite key (transaction prefix + date + amount). In Python: pandas merge on multiple columns. Understanding this lets you build reconciliation for any two data sources.',
              example: 'df_merge = pd.merge(erp_df, bank_df, on=["prefix","date","amount"], how="outer", indicator=True)\nmatched = df_merge[df_merge["_merge"]=="both"]\nmissing = df_merge[df_merge["_merge"]!="both"]',
              task: 'Ask AI: "How do I reconcile two CSV files in Python using pandas merge? Code that shows matched, unmatched, and amount differences."',
              ai_prompt: 'You are a Python expert teaching reconciliation automation. Write complete Python code that: loads two CSVs (ERP and Bank), merges on ID column, classifies each row as Matched / Amount Break / Missing in A / Missing in B, calculates differences, exports exceptions report. Use realistic column names. Add comments.',
              expected_output: 'Complete Python reconciliation script with exception classification.'
            },
            {
              id: 'l02_02_02', title: 'Intercompany Reconciliation — The Hard Problem',
              level: 'intermediate', type: 'concept',
              track: ['Accounting'], difficulty_score: 4,
              explanation: 'Intercompany reconciliation matches transactions between entities within the same group. The challenge: timing differences, currency conversion, different booking methods. A ₹1M intercompany sale by Entity A must appear as a ₹1M intercompany purchase in Entity B\'s books. Mismatches delay consolidation close by days.',
              example: 'Entity A books: IC Sale ₹1,000,000 on 28-Mar (USD 12,000 @ 83.3)\nEntity B books: IC Purchase ₹999,700 on 31-Mar (USD 12,000 @ 83.3 − bank charges ₹300)\nMismatch: ₹300 — reason: bank charges not separately recorded',
              task: 'Your intercompany recon shows 47 mismatches totalling ₹2.3M. Ask AI to categorise likely root causes and write a process to prevent them next month.',
              ai_prompt: 'You are a Group Consolidation Controller with 15 years of experience. The user has 47 intercompany mismatches totalling ₹2.3M. Categorise the most likely root causes (timing, FX, charges, booking errors — give % likelihood for each). Then write a 5-step prevention process for next month close. Include specific system controls and cut-off procedures.',
              expected_output: 'Root cause categorisation with % likelihood + 5-step prevention process.'
            },
            {
              id: 'l02_02_03', title: 'Accrual Automation — Month-End in 10 Minutes',
              level: 'intermediate', type: 'task',
              track: ['Accounting','Automation'], difficulty_score: 3,
              explanation: 'Accruals are estimates of costs incurred but not yet invoiced. Typical manual process: email every department for estimates → collect into spreadsheet → total → post journal entry. This takes 4-6 hours. Automated process: rules engine applies standard % accrual to spending categories → auto-posts journal → human reviews exceptions only.',
              example: 'Accrual rules engine:\n- Marketing events: 100% of signed contracts not yet invoiced\n- Consultancy: 80% of monthly retainer if no invoice received\n- Utilities: 3-month rolling average\n- Staff expenses: prior month actuals × 1.05',
              task: 'List 5 accrual categories in your business. Define the accrual rule for each. Ask AI to write the Python logic for an automated accrual calculator.',
              ai_prompt: 'You are a senior management accountant and Python developer. The user has defined 5 accrual categories with rules. Write Python code that: takes a dictionary of spending categories and their rules, calculates the accrual amount for each, outputs a journal entry-ready table with debit account, credit account, amount, and narration. Include error handling for missing data.',
              expected_output: 'Python accrual calculator that outputs a journal-entry-ready table.'
            },
            {
              id: 'l02_02_04', title: 'Simulation — Close the Books Under Pressure',
              level: 'intermediate', type: 'simulation',
              track: ['Accounting','CFO Strategy'], difficulty_score: 5,
              explanation: 'Simulation: It is 5pm on the last day of month-end close. You have 3 unresolved issues: (1) IC recon mismatch ₹800K with no explanation yet, (2) One accrual estimate is ₹2M higher than prior month with no supporting evidence, (3) A major customer payment ₹5M expected today has not been received. CFO needs numbers by 6pm. What do you do?',
              example: 'A well-structured response: IC mismatch → provisional journal with reversal posted, note to file. High accrual → review with department head in 10 mins, accept or reduce with documentation. Late payment → mark as debtor risk, exclude from EBITDA calculation, flag in commentary.',
              task: 'Write your decisions for all 3 situations and your communication plan to the CFO. Then ask AI to critique your approach.',
              ai_prompt: 'You are a CFO reviewing a Finance Manager\'s close decisions under time pressure. For each of 3 situations (IC mismatch ₹800K, unusual accrual ₹2M above prior month, missing customer payment ₹5M), assess: Did they apply the correct accounting treatment? What risk are they taking? What would you do differently? Score each decision 1-5 and give an overall Close Quality Score.',
              expected_output: 'Decision critique with accounting treatment assessment + Close Quality Score.'
            }
          ],
          project: {
            title: 'Project: Design Your Month-End Close Automation',
            instructions: 'Map your current month-end close process step by step. Identify which steps are: (1) Already automated, (2) Could be automated with Python/AI, (3) Require human judgment. For each automatable step, write the AI prompt or Python approach. Present as a "Close Automation Roadmap".',
            ai_prompt: 'You are an automation consultant for finance close processes. Review the user\'s close automation roadmap. Score each automation idea on: feasibility (1-5), time saving (1-5), risk (1-5). Calculate a priority score (feasibility + saving - risk). Rank the automations by priority. Add 2 automation opportunities they missed. Give an implementation sequence for 90 days.'
          }
        }
,

        /* MODULE 3 — CFO Strategy & Decisions */
        {
          id: 'm02_03', title: 'CFO Strategy: Data-Driven Financial Decisions',
          lessons: [
            {
              id: 'l02_03_01', title: 'Zero-Based Budgeting — Challenge Every Line',
              level: 'intermediate', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 3,
              explanation: 'Zero-Based Budgeting (ZBB) starts from zero each year — every expense must be justified from scratch, not just rolled forward from prior year. It eliminates budget baseline inflation but requires significant analytical effort. AI makes ZBB practical by automating the data collection and analysis, reducing the effort by 70%.',
              example: 'Traditional budgeting: prior year ₹12M OPEX + 5% inflation = ₹12.6M approved with minimal review.
ZBB: each of 200 cost lines reviewed. AI analyses spend data, identifies ₹1.8M in low-ROI spending, suggests reallocation. Final approved budget: ₹10.8M with better allocation. Saving: ₹1.8M or 14%.',
              task: 'Pick one OPEX category from your budget. Apply ZBB thinking: list every item, ask "What business outcome does this fund?", and ask AI to identify which items you could eliminate or reduce without impacting performance.',
              ai_prompt: 'You are a ZBB (Zero-Based Budgeting) specialist and CFO advisor. The user will share an OPEX category with line items. For each line: (1) Classify as Core (essential), Discretionary (reduce by 20%), or Elective (consider eliminating). (2) Suggest an alternative if eliminating. (3) Calculate potential saving. Present as a ZBB decision table with total saving and priority ranking.',
              expected_output: 'ZBB decision table with Core/Discretionary/Elective classification + total saving.'
            },
            {
              id: 'l02_03_02', title: 'EBITDA Bridge — Tell the Full Story',
              level: 'intermediate', type: 'task',
              track: ['FP&A'], difficulty_score: 3,
              explanation: 'An EBITDA bridge walks from prior year (or budget) EBITDA to current EBITDA, showing each driver's contribution. It is the most powerful single slide in any management pack. The structure: Starting EBITDA → Volume effect → Price effect → Mix effect → COGS changes → OPEX changes → Ending EBITDA. Every number must add up exactly.',
              example: 'PY EBITDA ₹28M → +Volume ₹3.2M → +Price ₹1.8M → −Mix ₹0.4M → −COGS inflation ₹5.1M → −OPEX ₹2.1M → CY EBITDA ₹25.4M. Net: −₹2.6M. Without the bridge, the CFO just sees "EBITDA fell ₹2.6M." With the bridge, they see exactly why and what to do.',
              task: 'Build an EBITDA bridge for your business using last month's actuals vs prior year. If you do not have the data, use: PY EBITDA ₹40M, Revenue +6%, COGS +10%, OPEX +4%, Volume +3%. Ask AI to build the bridge and provide narrative.',
              ai_prompt: 'You are a senior FP&A analyst building an EBITDA bridge. Take the user's inputs and: (1) Calculate each bridge component precisely, (2) Present as a waterfall table showing positive bars (green) and negative bars (red), (3) Write a 2-sentence narrative for each significant driver, (4) Identify the single most important action management should take based on the bridge. Format clearly for a board presentation.',
              expected_output: 'Waterfall table with values + 2-sentence narrative per driver + recommended action.'
            },
            {
              id: 'l02_03_03', title: 'Investment Appraisal — NPV and IRR for Non-Accountants',
              level: 'intermediate', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 4,
              explanation: 'When a business wants to invest (new factory, system, acquisition), it needs to compare the investment cost against future cash flows. NPV (Net Present Value) discounts future cash flows to today's value. IRR (Internal Rate of Return) finds the effective return %. Rule: invest if NPV > 0 or IRR > WACC (cost of capital).',
              example: 'Investment: ₹100M capex. Cash flows: Year 1 ₹20M, Year 2 ₹35M, Year 3 ₹40M, Year 4 ₹45M. Discount rate (WACC): 12%.
NPV = −100 + 20/1.12 + 35/1.12² + 40/1.12³ + 45/1.12⁴ = −100 + 17.86 + 27.90 + 28.47 + 28.60 = +₹2.83M.
NPV > 0 → invest. IRR ≈ 13.1% > WACC 12% → invest.',
              task: 'You are evaluating a ₹50M investment with cash flows: Y1 ₹8M, Y2 ₹15M, Y3 ₹20M, Y4 ₹22M, Y5 ₹20M. WACC is 10%. Ask AI to calculate NPV and IRR and give a recommendation.',
              ai_prompt: 'You are a corporate finance expert. Calculate NPV and IRR for this investment: ₹50M upfront, cash flows Y1-Y5 as user specifies, WACC 10%. Show all workings year by year. State whether NPV is positive and if IRR exceeds WACC. Give a clear go/no-go recommendation. Then run a sensitivity analysis: what if cash flows are 20% lower? Does the recommendation change?',
              expected_output: 'Year-by-year NPV calculation + IRR + recommendation + sensitivity analysis.'
            },
            {
              id: 'l02_03_04', title: 'Case Study — Private Equity CFO Under Pressure',
              level: 'intermediate', type: 'case_study',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Real case: A PE-backed consumer goods company was acquired at 8× EBITDA (₹400M enterprise value, EBITDA ₹50M). 18 months post-acquisition: EBITDA fell to ₹38M (−24%) due to market headwinds and integration costs. PE sponsor threatening to replace CEO and CFO. The CFO needs a credible recovery plan within 30 days to present to the board.',
              example: 'The CFO's 30-day action: (1) Immediate EBITDA bridge analysis to pinpoint exact causes. (2) Classify costs as structural vs temporary. (3) Identify ₹8M of OPEX that could be taken out within 6 months. (4) Revenue actions: price increase on premium SKUs (3-5% price increase = ₹1.5M EBITDA). (5) Working capital: DSO reduction from 78 to 55 days releases ₹12M cash. (6) Re-base 3-year plan showing return to ₹52M EBITDA by end of year 3.',
              task: 'You are the CFO in this scenario. EBITDA fell ₹12M in 18 months. Write your recovery plan and your opening statement to the board. Ask AI to challenge your plan from a PE investor perspective.',
              ai_prompt: 'You are a senior PE partner who has invested ₹400M in a business now underperforming. The CFO has just presented a recovery plan. Ask the 5 hardest questions a PE investor would ask, numbered. For each question: state what a weak CFO answer looks like vs a strong one. Then give your verdict: does this CFO keep their job? State your reasoning.',
              expected_output: '5 PE investor questions with weak/strong contrast + verdict with reasoning.'
            },
            {
              id: 'l02_03_05', title: 'Challenge — Turnaround Simulation',
              level: 'intermediate', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Simulation: You are the new CFO. Day 1. Revenue down 15% vs prior year. EBITDA −40%. Cash runway: 4 months. 280 employees. A competitor has approached about acquisition at a 30% discount to last valuation. The board wants your recommendation in 14 days: restructure or sell?',
              example: 'Framework: (1) Validate the cash position — is 4 months accurate? (2) Identify immediate OPEX savings achievable in 30 days. (3) Assess revenue recovery timeline — is the 15% decline structural or cyclical? (4) Model acquisition vs restructure NPV. (5) Consider stakeholder impact — employees, lenders, shareholders. (6) Recommend with clear conditions and milestones.',
              task: 'Write your 14-day assessment and recommendation: restructure or sell. Include your financial analysis and your key assumptions. Ask AI to play the board and challenge your recommendation.',
              ai_prompt: 'You are a board member and experienced turnaround specialist. The new CFO has just recommended either restructuring or selling the business. Challenge their recommendation with 4 hard questions. For each: what data would change your answer? What is the biggest risk in their plan? End with: "The one thing I need to see in the next 48 hours to support your recommendation is..."',
              expected_output: '4 board challenge questions + critical data needs + the one 48-hour requirement.'
            }
          ],
          project: {
            title: 'Project: Build a 3-Year Financial Model',
            instructions: 'Build a simple 3-year P&L model for a business. Define: revenue growth assumptions, margin trajectory, OPEX as % of revenue, EBITDA target. Model Base, Bull, Bear cases. Ask AI to review your assumptions and identify which is the most sensitive driver.',
            ai_prompt: 'You are a financial modelling expert reviewing a 3-year P&L model. Stress-test each assumption: which ones, if wrong by 10%, have the biggest impact on Year 3 EBITDA? Run sensitivity analysis on the top 3 assumptions. Identify if the model has any logical inconsistencies. Recommend one additional scenario the board would want to see that the analyst has not modelled.'
          }
        },

        /* MODULE 4 — Automation Deep Dive */
        {
          id: 'm02_04', title: 'Advanced Finance Automation',
          lessons: [
            {
              id: 'l02_04_01', title: 'Journal Entry Automation — From Rules to Code',
              level: 'intermediate', type: 'task',
              track: ['Accounting','Automation'], difficulty_score: 4,
              explanation: 'Recurring journal entries (depreciation, prepayments, accruals, intercompany) follow rules that can be coded. A rules engine processes the input data and generates the journal automatically. This eliminates 4-6 hours of monthly manual posting and reduces posting errors to near zero.',
              example: 'Depreciation journal rule:
- Source: asset register with cost and useful life
- Calculation: Monthly depreciation = (Cost − Residual) / (Useful Life × 12)
- Debit: Depreciation Expense (P&L)
- Credit: Accumulated Depreciation (Balance Sheet)
- Narration: Auto-generated: "Depreciation for [Asset Name] — Month [X]"',
              task: 'Choose one recurring journal entry in your close process. Define the rule (inputs, calculation, debit, credit, narration). Ask AI to write the Python code that generates this journal automatically.',
              ai_prompt: 'You are a Python developer and accountant. The user defines a recurring journal entry rule. Write complete Python code that: takes a CSV of input data, applies the accounting rule, generates a journal entry table with Debit Account, Credit Account, Amount, Cost Centre, Narration, and Posting Date. Export to CSV. Include validation (amounts balance to zero). Add error handling for missing data.',
              expected_output: 'Complete Python journal automation script with validation and CSV export.'
            },
            {
              id: 'l02_04_02', title: 'Workflow Automation — Connecting Finance Systems',
              level: 'intermediate', type: 'concept',
              track: ['Automation'], difficulty_score: 4,
              explanation: 'Modern finance workflows span multiple systems: ERP (SAP/Oracle), planning tool (Anaplan/Workday), reporting (Power BI), communication (email/Slack). Connecting them eliminates manual data transfer — the biggest source of errors and delays. Python can act as the integration layer between any two systems.',
              example: 'Automated month-end workflow:
8:00am: Python script runs → pulls actuals from ERP API → loads into planning database → triggers variance analysis → generates commentary draft → emails draft to FP&A team → team edits in Google Docs → AI formats for board → pack distributed. Total human time: 45 minutes. Previous: 2 days.',
              task: 'Map your 3 most disconnected finance systems. Ask AI to design a Python workflow that connects them automatically.',
              ai_prompt: 'You are a financial systems architect and Python developer. The user describes 3 disconnected finance systems. Design a Python integration workflow: (1) Data flow diagram (describe in text), (2) Key Python libraries needed (requests, pandas, schedule, smtplib), (3) Trigger and scheduling approach, (4) Error handling and alerting strategy, (5) A code snippet for the most critical integration step. Make it production-realistic.',
              expected_output: 'Integration workflow design + Python libraries + code snippet for critical step.'
            },
            {
              id: 'l02_04_03', title: 'AI-Powered Anomaly Detection in Finance',
              level: 'intermediate', type: 'concept',
              track: ['Automation','Accounting'], difficulty_score: 4,
              explanation: 'Anomaly detection finds unusual patterns in financial data that humans would miss. In finance: unexpectedly large transactions, unusual timing (posting on weekends), round-number entries (fraud signal), duplicate payments, accounts with unusual activity. AI processes millions of transactions and flags the top 0.1% for human review.',
              example: 'Pandas-based anomaly detection:
df["z_score"] = (df.amount − df.amount.mean()) / df.amount.std()
anomalies = df[df.z_score.abs() > 3]  # flag >3 standard deviations
round_numbers = df[df.amount % 1000 == 0]  # flag suspiciously round amounts
weekend_posts = df[pd.to_datetime(df.date).dt.dayofweek >= 5]  # flag weekend postings',
              task: 'Ask AI to write a Python anomaly detection script for a general ledger file. It should flag: large amounts (>3 std dev), round numbers, weekend postings, and duplicate entries.',
              ai_prompt: 'You are a forensic accountant and Python developer. Write a complete Python anomaly detection script for a general ledger CSV with columns: transaction_id, date, account, description, debit, credit, posted_by. Detect: (1) Statistical outliers (z-score > 3), (2) Round number postings (suspicious amounts divisible by 1000), (3) Weekend/holiday postings, (4) Duplicate transaction amounts within 7 days on same account, (5) Reversals (credit matching prior debit within 30 days). Output a priority-ranked exception report.',
              expected_output: 'Complete anomaly detection script with 5 detection types and priority-ranked output.'
            },
            {
              id: 'l02_04_04', title: 'Real Data Mode — Analyse Your Own CSV',
              level: 'intermediate', type: 'task',
              track: ['FP&A','Automation'], difficulty_score: 3,
              explanation: 'You now have the skills to analyse real financial data with AI. The workflow: upload your CSV → describe its structure → AI generates analysis code → you review and interpret results. This is the core Fincy Intelligence workflow applied to your own data.',
              example: 'User uploads 6-month P&L by market. AI auto-profiles: 847 rows, 12 columns, date range Apr-Sep, 8 markets, 3 product categories. AI then: calculates variance by market, identifies top 3 underperformers, generates commentary, flags 2 data quality issues (missing values in Germany column).',
              task: 'Export a financial report from your system (or use the Fincy sample data). Describe its structure to AI and ask for a complete analysis: data quality check, key variance identification, top 3 insights, and one recommendation.',
              ai_prompt: 'You are a senior data analyst and FP&A expert. The user describes a financial dataset. Provide: (1) Data quality assessment — what to check and how, (2) The 5 most important analyses to run, (3) Python code for the top 2 analyses, (4) Template for presenting insights to management, (5) 3 questions the data cannot answer that you would need additional data to address.',
              expected_output: 'Data quality checklist + 5 analyses + Python code for top 2 + insight template + data gaps.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 03 — ADVANCED | 25 Lessons | Build AI Finance Tools
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_03', badge: '03 / ADVANCED', color: '#818cf8',
      title: 'Build AI Finance Tools',
      tagline: 'Ship production tools. Build what other analysts only talk about.',
      unlocked: false,
      modules: [

        /* MODULE 1 */
        {
          id: 'm03_01', title: 'Streamlit + Groq — The Builder\'s Stack',
          lessons: [
            {
              id: 'l03_01_01', title: 'Your First Streamlit Finance Dashboard',
              level: 'advanced', type: 'concept',
              track: ['Automation'], difficulty_score: 3,
              explanation: 'Streamlit turns Python scripts into web apps. No HTML. No CSS. No JavaScript. You write Python, Streamlit renders a shareable app. Fincy Intelligence is entirely Streamlit — every chart, every AI response, every button is Python.',
              example: 'import streamlit as st\nimport pandas as pd\nst.title("My FP&A Dashboard")\nfile = st.file_uploader("Upload P&L CSV")\nif file:\n    df = pd.read_csv(file)\n    st.metric("Total Revenue", f"Rs{df.Revenue.sum():,.0f}")\n    st.dataframe(df)',
              task: 'Ask AI for a complete Streamlit app that uploads a CSV and shows: total revenue, top 5 markets, and a bar chart. Run it locally.',
              ai_prompt: 'You are a Streamlit developer building finance tools. Write a complete, runnable app.py that: uploads a CSV, auto-detects Revenue column, shows 3 KPI metrics, displays a Plotly bar chart of top 10 rows, adds a data table. Include all imports, use dark theme CSS, add comments.',
              expected_output: 'Complete runnable app.py with dark theme KPIs and chart.'
            },
            {
              id: 'l03_01_02', title: 'API Integration — Connect to Any Finance System',
              level: 'advanced', type: 'concept',
              track: ['Automation'], difficulty_score: 4,
              explanation: 'Real finance automation requires connecting to ERP systems, banking APIs, and data platforms. Every major system has a REST API. Python\'s requests library handles all of them. Once connected, you can pull data automatically — no manual exports, no CSV uploads.',
              example: 'import requests\n# Pull invoice data from ERP\nheaders = {"Authorization": "Bearer YOUR_ERP_TOKEN"}\nresp = requests.get("https://erp.company.com/api/invoices?status=pending", headers=headers)\ninvoices = resp.json()["data"]\ndf = pd.DataFrame(invoices)\nprint(f"Pending invoices: {len(df)} | Total: Rs{df.amount.sum():,.0f}")',
              task: 'Ask AI to design an API integration plan for connecting your ERP to a Python automation script. Include authentication, error handling, and data refresh scheduling.',
              ai_prompt: 'You are a senior Python developer specialising in finance system integration. Design a complete API integration blueprint for connecting an ERP system to a Python automation script. Include: authentication approach (OAuth vs API key), endpoint structure, error handling strategy, rate limiting, data refresh scheduling (cron/APScheduler), and a code template with all components. Make it production-ready.',
              expected_output: 'Complete API integration blueprint with production-ready code template.'
            },
            {
              id: 'l03_01_03', title: 'Excel → Python Transformation',
              level: 'advanced', type: 'task',
              track: ['Automation','FP&A'], difficulty_score: 3,
              explanation: 'Most finance teams run on Excel workbooks that took years to build. The transformation is not about replacing Excel — it is about automating the data layer while keeping the familiar outputs. Python handles data processing; Excel or Streamlit handles the output.',
              example: 'Excel workflow: Download ERP report → paste into Sheet1 → run 8 formulas → copy to pivot → format 4 charts → email PDF. Python equivalent: scheduled script runs at 8am → pulls ERP API → processes data → generates identical charts → emails PDF automatically. Time: 0 human minutes.',
              task: 'Take one Excel report you build every month. Describe its data sources, calculations, and output format. Ask AI to write the Python script that automates it completely.',
              ai_prompt: 'You are a Python automation expert for finance teams. The user will describe an Excel report they build manually. Write a complete Python script that: (1) simulates the data structure with sample data, (2) replicates all key calculations, (3) generates a PDF or Streamlit output matching the report format. Include xlsxwriter for Excel output and openpyxl for reading. Make it fully runnable.',
              expected_output: 'Complete Python script automating the described Excel report with sample data.'
            },
            {
              id: 'l03_01_04', title: 'Cash Flow Risk Modelling',
              level: 'advanced', type: 'case_study',
              track: ['CFO Strategy','FP&A'], difficulty_score: 4,
              explanation: 'Cash flow risk modelling identifies scenarios where the business runs out of cash and quantifies the probability and timing. A CFO-quality cash model tracks: operating cash flows by week, committed outflows (payroll, debt service, rent), receivables timing risk, and available facilities (revolving credit, factoring).',
              example: 'Cash runway analysis:\nCurrent cash: ₹85M\nWeekly burn rate: ₹6.2M (payroll ₹3.1M + COGS payments ₹2.1M + fixed ₹1.0M)\nExpected receivables: ₹40M (60% probability in next 3 weeks)\nRunway base case: 13.7 weeks\nRunway bear case (receivables delayed 3 weeks): 7.2 weeks',
              task: 'Build a 13-week cash flow model for your business. Define: opening cash, weekly operating receipts, weekly payments, and DSO assumption. Ask AI to calculate runway scenarios and flag risk weeks.',
              ai_prompt: 'You are a CFO and treasury specialist. Build a 13-week cash flow model from the user\'s inputs. Output: week-by-week table showing opening cash, receipts, payments, closing cash. Highlight weeks where cash falls below a minimum threshold (15% of average weekly payments). Calculate base, bull, bear runway. Flag the 3 highest risk weeks with specific actions to mitigate. Format as a professional CFO presentation.',
              expected_output: '13-week cash table with risk weeks highlighted + 3 specific mitigation actions.'
            },
            {
              id: 'l03_01_05', title: 'Capital Allocation — The CFO\'s Strategic Decision',
              level: 'advanced', type: 'case_study',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Capital allocation decides where the company invests its limited cash. Every CFO faces this: do we invest in growth, return cash to shareholders, pay down debt, or hold reserves? The framework: IRR vs WACC, payback period, strategic fit, and risk-adjusted return. AI can model all scenarios simultaneously.',
              example: 'Four capital allocation options:\nOption A: New market expansion — IRR 18%, payback 3.2 years, ₹200M capex\nOption B: Debt repayment — risk-free 8.5% return, immediate cash flow improvement\nOption C: Dividend — shareholder yield 4.2%, signals confidence\nOption D: Technology investment — IRR 24%, payback 4.5 years, ₹80M capex, strategic imperative',
              task: 'You have ₹300M to allocate. You have 4 options: factory expansion (IRR 16%), product development (IRR 22%), debt paydown (saves 9% interest), and acquisition target (IRR 28% if integration succeeds, 50% failure risk). Ask AI to build the allocation framework and recommend how to split the ₹300M.',
              ai_prompt: 'You are a CFO and capital allocation expert. The user has ₹300M to allocate across 4 options. Build a capital allocation framework that: (1) calculates risk-adjusted IRR for each option, (2) considers portfolio diversification, (3) applies WACC hurdle rate (assume 12%), (4) recommends an optimal allocation split with rationale. Present as a board-ready one-pager with your allocation recommendation and the logic behind it.',
              expected_output: 'Capital allocation framework with risk-adjusted IRRs + board-ready recommendation.'
            },
            {
              id: 'l03_01_06', title: 'Pricing Strategy — The Margin Lever Most Teams Miss',
              level: 'advanced', type: 'concept',
              track: ['CFO Strategy','FP&A'], difficulty_score: 4,
              explanation: 'A 1% price increase typically delivers 7-10× the profitability impact of a 1% volume increase. Yet most finance teams spend 90% of their time on cost and volume. Price elasticity analysis — how demand changes with price — is the most underused tool in FP&A.',
              example: 'Price elasticity = % change in demand / % change in price\nIf elasticity = −1.5: a 5% price increase → 7.5% volume decline\nNet revenue impact: +5% price × 92.5% volume = −2.4% net revenue\nBut: margin impact is much better because volume decline reduces COGS\nResult: margin improves even with volume loss if elasticity < 2.0',
              task: 'Your product has elasticity of −1.2. Current price ₹1,000, volume 50,000 units, gross margin 45%. Model the P&L impact of 5%, 10%, and 15% price increases. Ask AI to identify the optimal price point.',
              ai_prompt: 'You are a pricing strategy expert and CFO advisor. Model price elasticity scenarios for: elasticity −1.2, current price Rs1000, volume 50000, gross margin 45%. Calculate for 5%, 10%, 15% price increases: new volume, new revenue, new gross profit, new margin %. Show in a 4-column comparison table. Then recommend the optimal price point based on profit maximisation and explain the reasoning.',
              expected_output: '4-column price scenario table + optimal price recommendation with reasoning.'
            },
            {
              id: 'l03_01_07', title: 'Simulation — Run the Board Meeting',
              level: 'advanced', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Simulation: You are presenting to the board. Your company\'s Q3 results show revenue +4% but EBITDA −6% vs budget. The board will ask hard questions. You have 5 minutes to present results, explain the variance, and defend your Q4 outlook. The CEO is concerned. Three board members have read analyst reports suggesting a profit warning is needed.',
              example: 'Strong CFO opening: "Revenue at ₹42.8M beat budget by 2%. EBITDA at ₹8.1M missed by 8.3% — this is driven by three specific factors I will address. We have clear line of sight to Q4 recovery and I will take you through the specific actions we are taking." Then: drivers, actions, Q4 forecast, confidence level.',
              task: 'Prepare your 5-minute board presentation for Q3 results (revenue +4%, EBITDA −6% vs budget). Write the opening statement, key message, top 3 variance drivers, and Q4 outlook. Ask AI to play the board and challenge you.',
              ai_prompt: 'You are a challenging board member with 30 years of investment experience. The CFO (user) has just presented Q3 results with revenue +4% but EBITDA −6% vs budget. Ask 5 hard questions a board would ask, numbered. For each question: state the question, explain what a weak CFO answer looks like, then show what a strong CFO answer would be. Make the questions progressively harder. The last question should be about whether a profit warning is needed.',
              expected_output: '5 hard board questions with weak vs strong answer contrast for each.'
            }
          ],
          project: {
            title: 'Project: Build and Deploy Your Own AI CFO Module',
            instructions: 'Build a Streamlit module for your specific finance use case: (1) Choose a problem (variance analysis, cash flow, budget tracking, reconciliation), (2) Build the Streamlit app with CSV upload, KPIs, chart, and AI CFO question box, (3) Deploy to share.streamlit.io, (4) Share the live link. This becomes a portfolio project you can show in interviews.',
            ai_prompt: 'You are a senior Streamlit developer and portfolio coach. The user has built a finance AI module and deployed it. Review their description and: (1) suggest 3 features that would make it interview-worthy, (2) write the LinkedIn post announcing their project, (3) suggest the exact bullet point for their CV, (4) identify 3 companies/roles where this project would be most relevant. Make this feel like a career accelerator, not just a coding exercise.'
          }
        }
,

        /* MODULE 2 — Advanced Finance Tools & Strategy */
        {
          id: 'm03_02', title: 'Advanced AI Finance Applications',
          lessons: [
            {
              id: 'l03_02_01', title: 'Forecasting with Machine Learning',
              level: 'advanced', type: 'concept',
              track: ['FP&A','Automation'], difficulty_score: 4,
              explanation: 'Traditional forecasting: linear extrapolation or Excel regression. ML forecasting: pattern recognition across hundreds of variables simultaneously. For finance, the most practical ML approach is gradient boosting (XGBoost, LightGBM) — it handles mixed data types, missing values, and non-linear relationships that Excel cannot model.',
              example: 'Revenue forecast using ML:
Features: prior 12 months revenue, seasonality index, promotional spend, competitor pricing, weather index, economic indicators.
Model: XGBoost trained on 3 years of weekly data.
Result: MAPE (Mean Absolute Percentage Error) 4.2% vs statistical model 8.7% vs Excel trend 12.1%.
The ML model is 3× more accurate and captures promotions and weather effects automatically.',
              task: 'Ask AI to explain how you would build an ML forecast for your business revenue. What data would you need? What would the accuracy look like vs your current approach?',
              ai_prompt: 'You are a data science and FP&A expert. The user wants to build an ML revenue forecast. Design the full solution: (1) Data requirements — minimum 2 years of weekly data, external features to collect, (2) Model selection — why gradient boosting for finance data, (3) Python implementation overview with key libraries (scikit-learn, XGBoost), (4) How to interpret and present ML forecasts to non-technical management, (5) Realistic accuracy improvement vs current method. Give Python code skeleton for the training pipeline.',
              expected_output: 'Full ML forecast design + data requirements + Python skeleton + accuracy expectations.'
            },
            {
              id: 'l03_02_02', title: 'Building a Real-Time Finance Dashboard',
              level: 'advanced', type: 'task',
              track: ['Automation'], difficulty_score: 4,
              explanation: 'Real-time dashboards pull live data from source systems — no manual refresh needed. In Streamlit, you can use st.rerun() with a timer to auto-refresh. For finance, "real-time" typically means 15-minute or hourly refreshes during business hours. The data pipeline: Source system API → Python processing → Streamlit dashboard.',
              example: 'Real-time cash dashboard:
import streamlit as st, time
if st.button("Auto-refresh ON"):
    while True:
        cash_data = pull_from_erp_api()  # live API call
        st.metric("Current Cash", f"Rs{cash_data['balance']:,.0f}")
        st.metric("Daily Burn", f"Rs{cash_data['burn']:,.0f}")
        time.sleep(900)  # refresh every 15 minutes
        st.rerun()',
              task: 'Design a real-time finance dashboard for your business. What 3 metrics need live updates? What is the data source for each? Ask AI to write the Streamlit + API integration code.',
              ai_prompt: 'You are a senior Streamlit and finance systems developer. Build a real-time finance dashboard with: (1) Auto-refresh mechanism every 15 minutes, (2) 3 KPI metrics with live data (simulate with random data if no API), (3) Trend chart showing last 30 days, (4) Alert system — if any metric crosses threshold, show warning in red, (5) Download data button. Make it production-ready with error handling and loading state.',
              expected_output: 'Complete real-time Streamlit dashboard with auto-refresh, alerts, and download.'
            },
            {
              id: 'l03_02_03', title: 'NLP for Financial Documents — Extract Insights from Text',
              level: 'advanced', type: 'concept',
              track: ['Automation','FP&A'], difficulty_score: 4,
              explanation: 'Natural Language Processing (NLP) can extract structured information from unstructured text: contracts (payment terms, renewal dates, penalty clauses), analyst reports (sentiment, key metrics, risk factors), customer contracts (revenue recognition triggers), board minutes (decision log). This is one of the most underused AI applications in finance.',
              example: 'Contract NLP pipeline:
- Input: 200 supplier contracts as PDFs
- Extract: contract value, payment terms, renewal date, penalty clauses, auto-renewal provisions
- Output: structured database of all 200 contracts with risk flags
- Time: 12 minutes vs 3 weeks manual review
- Value found: 23 contracts with unfavourable auto-renewal terms totalling ₹45M',
              task: 'Describe one type of financial document your team reviews manually (invoices, contracts, reports). Ask AI to design an NLP extraction pipeline for it.',
              ai_prompt: 'You are an NLP engineer specialising in financial document processing. The user describes a document type. Design the extraction pipeline: (1) Document ingestion approach (PDF parsing with PyMuPDF/pdfplumber), (2) Key information to extract with examples, (3) Groq prompt for extraction, (4) Output data structure, (5) Quality validation step. Write a complete Python code example that extracts 5 key fields from a sample invoice using Groq API.',
              expected_output: 'Full NLP pipeline design + Python code extracting 5 fields from financial document.'
            },
            {
              id: 'l03_02_04', title: 'Case Study — Building Fincy from Scratch',
              level: 'advanced', type: 'case_study',
              track: ['Automation','CFO Strategy'], difficulty_score: 5,
              explanation: 'This is the story of how Fincy Intelligence was built — as a case study in building real AI finance tools. The problem: FP&A analysts spending 80% of time on data processing and 20% on insights. The solution: Streamlit app with 6 AI-powered modules, each solving a specific FP&A pain point. Built in 6 months by one FP&A analyst with no software engineering background.',
              example: 'Build sequence: (1) Month 1 — Learn Python basics + Pandas. (2) Month 2 — First Streamlit app with CSV upload. (3) Month 3 — Add Groq API integration. (4) Month 4 — Build reconciliation engine. (5) Month 5 — Add FP&A module + personal finance. (6) Month 6 — Polish, deploy, and launch. The key insight: building the tool teaches you FP&A and AI simultaneously.',
              task: 'Design your own finance tool idea. What problem would you solve? Who is the user? What data does it need? What AI does it use? Ask AI to build you a week-by-week 8-week roadmap.',
              ai_prompt: 'You are a startup advisor and technical mentor for finance professionals building their first AI tool. The user has described their tool idea. Build an 8-week development roadmap: Week 1-2 setup, Week 3-4 core functionality, Week 5-6 AI integration, Week 7-8 polish and launch. For each week: specific tasks, expected output, skills learned, and the one biggest risk. End with the single most important piece of advice for first-time builders.',
              expected_output: '8-week roadmap with tasks, outputs, skills, risks + one critical piece of advice.'
            },
            {
              id: 'l03_02_05', title: 'Simulation — You Are the CTO of Fincy',
              level: 'advanced', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Simulation: You are the CTO of a growing finance AI startup. You have 3 months of runway and need to decide: (A) Build a new AI feature users are asking for, (B) Improve existing reliability and performance, (C) Focus on sales and growth. The CEO wants your recommendation with technical and business justification.',
              example: 'Strong CTO reasoning: "If retention is below 80%, reliability wins. If retention is above 80% but growth is slow, new features win. If both are good, invest in growth infrastructure." This is the build vs reliability vs growth trilemma every tech company faces.',
              task: 'Write your CTO recommendation with technical and business reasoning. Then ask AI to challenge your decision from a VC investor perspective.',
              ai_prompt: 'You are a VC investor who has backed several finance AI startups. The CTO has just presented their 3-month plan. Challenge them: (1) What metric proves their choice is right after 30 days? (2) What is the opportunity cost of NOT doing one of the other two options? (3) How does this decision affect the next funding round? (4) What would make you reverse this decision in month 2? Give your honest assessment: is this the right call?',
              expected_output: '4 VC challenge questions + honest assessment of the decision.'
            }
          ],
          project: {
            title: 'Project: Build a Production-Ready Finance AI Tool',
            instructions: 'Build a complete, deployed finance AI tool with: CSV upload, at least 2 KPI metrics, 1 chart, AI CFO Q&A, error handling, and a professional UI. Deploy to Streamlit Cloud. This is your portfolio project — it should demonstrate that you can build production software, not just run code.',
            ai_prompt: 'You are a senior engineer and product reviewer. The user has built and deployed a finance AI tool. Review it across: (1) Technical quality — code structure, error handling, performance, (2) Product quality — does it solve a real problem?, (3) AI integration — is the AI adding real value?, (4) Presentation — could you show this in an interview? Score each /25, total /100. Give your 3 most important improvement recommendations. Write the product description they should put on their LinkedIn profile.'
          }
        },

        /* MODULE 3 — Financial Modelling Mastery */
        {
          id: 'm03_03', title: 'Financial Modelling Mastery with AI',
          lessons: [
            {
              id: 'l03_03_01', title: 'Three-Statement Model — The Foundation',
              level: 'advanced', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 4,
              explanation: 'The three-statement model links P&L, Balance Sheet, and Cash Flow Statement. Every transaction appears in all three. Understanding the linkages is the core skill of financial modelling — and AI can help you build and audit models far faster than Excel.',
              example: 'P&L: Net profit ₹50M → feeds into Retained Earnings on Balance Sheet → drives Operating Cash Flow on CashFlow. Depreciation: reduces P&L profit but adds back in Cash Flow (non-cash). Working capital changes: increase in Receivables reduces Cash Flow. The model must always balance: Assets = Liabilities + Equity.',
              task: 'Ask AI to explain the key linkages between the three financial statements using a simple example with specific numbers.',
              ai_prompt: 'You are a CFO teaching three-statement modelling to a senior analyst. Build a minimal example with real numbers: a company that earns ₹100M revenue, has ₹60M COGS, ₹20M OPEX, ₹5M depreciation, 25% tax rate. Show: (1) The P&L with net profit, (2) How net profit flows to the balance sheet, (3) How to build the cash flow statement from P&L and balance sheet changes, (4) The 3 checks that confirm the model is correct (balance sheet balances, retained earnings reconcile, cash flow closing = balance sheet cash).',
              expected_output: 'Three-statement example with numbers + 3 verification checks.'
            },
            {
              id: 'l03_03_02', title: 'LBO Modelling — How Private Equity Thinks',
              level: 'advanced', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'A Leveraged Buyout (LBO) model calculates the return to a PE investor who acquires a company using significant debt. The key drivers: purchase price (entry multiple), debt level, EBITDA growth, and exit multiple. Understanding LBO thinking makes you a better CFO — it forces you to think about value creation, debt capacity, and cash flow generation.',
              example: 'Simple LBO: Buy at 8× EBITDA (₹50M EBITDA = ₹400M enterprise value). 60% debt (₹240M), 40% equity (₹160M). EBITDA grows to ₹70M in 5 years (7% CAGR). Exit at 9× = ₹630M enterprise value. Less debt repaid ₹120M. Equity proceeds: ₹630M − ₹120M remaining debt = ₹510M. Return: ₹510M / ₹160M = 3.2× or ~26% IRR.',
              task: 'Model an LBO: Entry multiple 7×, EBITDA ₹30M, 50% debt, EBITDA grows 10%/yr for 5 years, exit at 8×. Ask AI to calculate the equity return and IRR.',
              ai_prompt: 'You are a PE associate and financial modelling expert. Model this LBO: entry 7× EBITDA, EBITDA ₹30M growing 10%/yr, 50% debt at 8% interest. Show year-by-year: EBITDA, debt balance, interest, free cash flow for debt repayment. Calculate exit value at 8× Year 5 EBITDA, equity proceeds, Money-on-Money (MoM) multiple, and IRR. Then: what entry multiple makes IRR = 20%? Show the sensitivity.',
              expected_output: 'Year-by-year LBO model + MoM + IRR + entry multiple sensitivity for 20% IRR.'
            },
            {
              id: 'l03_03_03', title: 'Challenge — Model a Real Acquisition',
              level: 'advanced', type: 'challenge',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Challenge: A competitor is for sale at ₹500M enterprise value. Their EBITDA is ₹60M (8.3× multiple). Your company has EBITDA of ₹80M and WACC of 11%. Synergies are estimated at ₹15M EBITDA in Year 3. Integration cost: ₹30M. Should you acquire?',
              example: 'Acquisition analysis framework: (1) Standalone value of target (DCF at WACC). (2) Add synergy value (NPV of ₹15M recurring from Year 3). (3) Compare sum to acquisition price. (4) Assess financing options and impact on leverage. (5) Consider strategic fit and execution risk.',
              task: 'Write your acquisition recommendation with financial analysis. Ask AI to build the synergy-adjusted valuation.',
              ai_prompt: 'You are an M&A advisor and CFO consultant. Build an acquisition analysis: target price ₹500M, EBITDA ₹60M, acquirer WACC 11%, synergies ₹15M/yr from Year 3, integration cost ₹30M. Calculate: (1) Target DCF standalone valuation, (2) NPV of synergies (assume 10-year horizon), (3) Synergy-adjusted fair value, (4) Acquisition premium paid vs fair value, (5) Blended leverage post-acquisition. Give a go/no-go recommendation with 3 conditions that must be met.',
              expected_output: 'Full acquisition valuation + go/no-go with 3 conditions.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 04 — EXPERT | 20 Lessons | Prompt Engineering for CFOs
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_04', badge: '04 / EXPERT', color: '#2dd4bf',
      title: 'Prompt Engineering for CFOs',
      tagline: 'Extract CFO-quality insights every time. Build your personal AI advantage.',
      unlocked: false,
      modules: [
        {
          id: 'm04_01', title: '5 CFO Prompt Templates',
          lessons: [
            {
              id: 'l04_01_01', title: 'The Anatomy of a Perfect Finance Prompt',
              level: 'advanced', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 3,
              explanation: 'A great finance prompt has 4 parts: (1) Role — "You are a CFO with 20yr experience", (2) Context — actual numbers from your data, (3) Format — exactly what output you want, (4) Rules — constraints like "no fluff, use percentages". Missing any part drops quality by 50%.',
              example: '"You are a CFO advising a CEO. EBITDA margin is 12% vs 18% budget. Revenue grew 8% YoY but COGS rose 15%. Write a 2-paragraph board pack commentary: first = what happened with numbers, second = what we will do about it. No bullet points. Executive tone."',
              task: 'Take a real finance report from last month. Extract key numbers. Build a prompt using the 4-part structure. Ask AI to generate the commentary.',
              ai_prompt: 'You are a prompt engineering coach for CFOs. Score the user\'s finance prompt: Role (0-25), Context (0-25), Format (0-25), Rules (0-25) = total /100. Rewrite it to score 90+. Explain each improvement.',
              expected_output: 'Score /100 + improved prompt with explanation.'
            },
            {
              id: 'l04_01_02', title: 'Prompt Template: Variance Commentary',
              level: 'advanced', type: 'task',
              track: ['FP&A'], difficulty_score: 3,
              explanation: 'The highest-ROI prompt for FP&A analysts. Use every month-end. Feed in actuals vs budget numbers and get board-ready commentary in seconds.',
              example: 'TEMPLATE:\n"You are a senior FP&A analyst. Write board pack variance commentary.\nActuals: Revenue Rs{X}M, EBITDA Rs{Y}M, Margin {Z}%\nBudget: Revenue Rs{A}M, EBITDA Rs{B}M, Margin {C}%\nKey drivers: [list 2-3 drivers]\nFormat: 3 sentences. Headline. Drivers. Outlook.\nTone: professional, direct, no jargon."',
              task: 'Fill in the template with your own numbers. Click Ask AI. Compare to what you would have written manually.',
              ai_prompt: 'You are a CFO. Use EXACTLY: HEADLINE: [one sentence with numbers] | DRIVERS: [one sentence with 2 specific causes] | OUTLOOK: [one sentence with next action]. No other text. Use the numbers the user provides.',
              expected_output: 'HEADLINE: ... | DRIVERS: ... | OUTLOOK: ...'
            },
            {
              id: 'l04_01_03', title: 'Prompt Template: Cash Flow Risk Alert',
              level: 'advanced', type: 'task',
              track: ['CFO Strategy'], difficulty_score: 3,
              explanation: 'Cash flow risk prompts need specific timing. The AI needs DSO, payment terms, and upcoming obligations to give useful alerts — not generic advice.',
              example: '"You are a treasury analyst. Current cash: Rs50M. DSO: 72 days (target 45). Upcoming: Vendor A Rs12M (30 days), Payroll Rs8M (15 days), Tax Rs5M (45 days). Identify top 2 cash risks. Format: Risk | Amount at risk | Action | Timeline."',
              task: 'Create a cash flow risk prompt using your approximate DSO, upcoming obligations, and cash position. Ask AI for specific risk alerts.',
              ai_prompt: 'You are a treasury specialist. Analyse the user\'s cash position data and identify top 2-3 risks. Format: RISK: [name] | AMOUNT: [Rs at risk] | PROBABILITY: High/Medium/Low | ACTION: [specific step with owner and deadline]. Use the numbers provided.',
              expected_output: 'Structured risk alerts with RISK | AMOUNT | PROBABILITY | ACTION format.'
            },
            {
              id: 'l04_01_04', title: 'Advanced Prompt: Strategic Decision Making',
              level: 'advanced', type: 'challenge',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'The most powerful finance prompts combine financial data with strategic context. They ask AI to reason through trade-offs, not just calculate outcomes. This is the difference between a reporting analyst and a strategic finance partner.',
              example: '"You are a CFO advising on whether to expand into Germany. Context: UK business EBITDA 24%, Germany market size 3× UK, entry cost Rs800M, 3-year breakeven. Current leverage ratio 2.1× EBITDA. Board has risk appetite for 2.5×. Consider: financing structure, phased entry, and downside scenario. Recommend: go/no-go with conditions."',
              task: 'Write a strategic decision prompt for a real decision your company faces. Include financial context, strategic context, constraints, and desired output format. Ask AI for a go/no-go recommendation.',
              ai_prompt: 'You are a McKinsey CFO advisor with expertise in strategic finance decisions. Review the user\'s strategic decision prompt and their question. Provide a structured go/no-go recommendation using: (1) Financial attractiveness score (1-10), (2) Strategic fit score (1-10), (3) Risk score (1-10), (4) Overall recommendation with 3 conditions that must be met. Finish with the one question that must be answered before the board decides.',
              expected_output: 'Go/no-go recommendation with 3 scores + conditions + the key decision question.'
            },
            {
              id: 'l04_01_05', title: 'Simulation — Build a Prompt Library in 30 Minutes',
              level: 'advanced', type: 'simulation',
              track: ['FP&A','CFO Strategy'], difficulty_score: 4,
              explanation: 'Simulation: You have been asked to build a prompt library for your finance team of 8 people. It needs to cover: month-end commentary, budget variance, cash flow alerts, cost analysis, and board presentations. Each prompt must work without modification when different people use it. You have 30 minutes.',
              example: 'An effective prompt library: standardised [BRACKETS] for variable inputs, clear output format specified, role and expertise level defined, rules that prevent common mistakes (no jargon, use Rs not INR, 3 sentences max for commentary).',
              task: 'Build a 5-prompt library for your finance team. Each prompt must use [BRACKETS] for variable inputs so any team member can use it. Ask AI to audit the library and score it for team usability.',
              ai_prompt: 'You are a Finance Technology Director auditing a team prompt library. Score each prompt on: (1) Clarity for non-expert users (1-5), (2) Consistency of output (1-5), (3) Coverage of edge cases (1-5). Give an overall Library Readiness Score /15. Identify the weakest prompt and rewrite it. Add one prompt the team is missing that would have high daily usage.',
              expected_output: 'Library audit with scores + weakest prompt rewrite + missing high-value prompt.'
            }
          ],
          project: {
            title: 'Capstone: Build Your Personal AI CFO Prompt Library',
            instructions: 'Create a "Prompt Library" document with 5 prompts for your specific finance role. Each must: (1) have a name, (2) use [BRACKET] variables, (3) work every month without modification, (4) produce CFO-approved output. Test each and share your best prompt + AI output.',
            ai_prompt: 'You are a CFO and prompt engineering expert. The user shares their prompt library. Evaluate on: reusability (1-5), output quality (1-5), CFO-readiness (1-5). Score /15. Suggest the one change making the biggest improvement. Write a reference card for the top prompt showing: when to use it, how to fill variables, example inputs, expected output.'
          }
        },

        /* MODULE 2 — Advanced Prompting + CFO Thinking */
        {
          id: 'm04_02', title: 'Advanced Prompting Techniques',
          lessons: [
            {
              id: 'l04_02_01', title: 'Chain-of-Thought Prompting for Finance',
              level: 'advanced', type: 'concept',
              track: ['FP&A','CFO Strategy'], difficulty_score: 4,
              explanation: 'Chain-of-Thought (CoT) prompting asks AI to show its reasoning step by step before giving the answer. For finance, this dramatically improves accuracy on complex calculations and reduces confident-sounding wrong answers. Add "Think step by step" or "Show your working" to any financial analysis prompt.',
              example: 'Without CoT: "What is the impact of 5% price increase on EBITDA if current revenue is ₹180M and EBITDA margin is 20%?" → AI might give wrong answer.
With CoT: Same question + "Think step by step, show all calculations." → AI: Step 1: Current EBITDA = ₹180M × 20% = ₹36M. Step 2: Price increase revenue impact = ₹180M × 5% = ₹9M (assuming no volume change). Step 3: COGS does not change. Step 4: New EBITDA = ₹36M + ₹9M = ₹45M. Step 5: New margin = ₹45M / ₹189M = 23.8%. The answer is correct because the model showed its working.',
              task: 'Take a financial calculation you often ask AI about. Ask it once normally, then again with "Think step by step and show all calculations." Compare the quality and accuracy of both responses.',
              ai_prompt: 'You are a prompt engineering expert specialising in financial calculations. Demonstrate chain-of-thought prompting on this problem: A company has revenue ₹200M, EBITDA margin 22%, DSO 65 days. If DSO reduces to 45 days, what is the cash release? Show your reasoning step by step, explaining each calculation and why it matters. Then give a one-sentence executive summary of the answer.',
              expected_output: 'Step-by-step chain-of-thought + executive summary.'
            },
            {
              id: 'l04_02_02', title: 'Few-Shot Prompting — Teaching AI Your Style',
              level: 'advanced', type: 'task',
              track: ['FP&A'], difficulty_score: 3,
              explanation: 'Few-shot prompting gives AI 2-3 examples of what you want before asking your question. For finance, this means showing AI your specific commentary style, format preferences, or analytical framework before asking it to generate new content. The result: AI mirrors your style exactly.',
              example: 'Few-shot prompt:
"Here are 2 examples of how I write variance commentary:
[Example 1]: Revenue delivered ₹42.8M, 4% ahead of budget, driven by Germany (+18%) partially offset by UK (−6%) on delayed promotions.
[Example 2]: EBITDA of ₹11.2M represents a margin of 26.1%, 190bps behind budget, driven entirely by COGS inflation (+12% vs flat budget assumption).
Now write commentary for: EBITDA ₹9.8M vs ₹11.5M budget (−15%), COGS overspend ₹1.2M, Revenue in line."',
              task: 'Write 2 examples of your own commentary style. Then use them as few-shot examples to ask AI to generate a new commentary in exactly your style.',
              ai_prompt: 'You are an expert at matching communication styles. The user gives you 2 examples of their commentary style. Analyse the style: vocabulary choices, sentence structure, number formatting, tone. Then write 3 new commentary examples in EXACTLY the same style for different data scenarios. Also write a "style guide" the user could include in all future prompts to always get their style.',
              expected_output: '3 commentary examples in user's style + extracted style guide for future prompts.'
            },
            {
              id: 'l04_02_03', title: 'Prompt Chaining — Multi-Step Financial Analysis',
              level: 'advanced', type: 'task',
              track: ['FP&A','Automation'], difficulty_score: 4,
              explanation: 'Prompt chaining breaks complex analysis into steps where each output feeds the next prompt. This produces more reliable results than one giant prompt and allows human checkpoints. For finance: Prompt 1 → data summary, Prompt 2 → variance analysis, Prompt 3 → root cause, Prompt 4 → recommendations, Prompt 5 → executive narrative.',
              example: 'Prompt chain for P&L analysis:
P1: "Summarise this P&L data in bullet points with numbers only."
P2: "Given this summary, identify the top 3 variances vs budget."
P3: "For these 3 variances, identify the most likely root causes using the waterfall method."
P4: "Recommend one specific corrective action for each root cause with an expected outcome."
P5: "Write a 3-sentence executive summary of all the above."',
              task: 'Build a 4-step prompt chain for analysing a monthly P&L. Test it and compare the quality of the chained result vs a single comprehensive prompt.',
              ai_prompt: 'You are a prompt engineering and financial analysis expert. The user has built a 4-step prompt chain for P&L analysis. Evaluate the chain: (1) Does each step build logically on the previous? (2) Are there redundant steps? (3) Where could AI hallucination enter and how to prevent it? (4) What human checkpoint should be added between which steps? Redesign the chain to be more reliable and suggest the exact quality check at each gate.',
              expected_output: 'Chain evaluation + redesigned chain + quality checks at each gate.'
            },
            {
              id: 'l04_02_04', title: 'Structured Output Prompting — JSON and Tables',
              level: 'advanced', type: 'task',
              track: ['Automation','FP&A'], difficulty_score: 4,
              explanation: 'When AI output needs to feed into another system or be consistently formatted, structured output prompting forces AI to respond in JSON, tables, or specific formats. For finance automation: AI generates analysis in JSON → Python parses → data enters database or report. No manual formatting needed.',
              example: 'Structured output prompt:
"Analyse this P&L and respond ONLY with valid JSON in this exact format:
{'headline_metric': 'EBITDA', 'actual': 11.2, 'budget': 13.5, 'variance_pct': -17.0, 'rag': 'RED', 'top_driver': 'COGS inflation', 'recommended_action': 'Review supplier contracts', 'confidence': 85}"
No other text. No explanation. Valid JSON only.',
              task: 'Write a prompt that forces AI to return P&L analysis as JSON with 8 specific fields. Test it and use the output in a simple Python script.',
              ai_prompt: 'You are an AI output specialist for finance automation. The user wants structured JSON output from P&L analysis. Review their prompt and: (1) Identify any ambiguities that could cause malformed JSON, (2) Add a validation instruction to prevent common JSON errors, (3) Show how to parse the output in Python with error handling, (4) Demonstrate the prompt working on sample data with actual JSON output. Make the prompt production-reliable.',
              expected_output: 'Validated JSON prompt + Python parsing code + sample JSON output.'
            },
            {
              id: 'l04_02_05', title: 'Role-Play Prompting — The McKinsey Framework',
              level: 'advanced', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 4,
              explanation: 'Role-play prompting assigns AI a specific expert persona to dramatically change the quality and style of output. "You are a McKinsey partner" produces fundamentally different analysis than "you are a financial analyst." The key: specify the persona's experience level, their communication style, and what frameworks they use.',
              example: 'Same question, different roles:
"You are a junior accountant" → produces cautious, detailed, process-focused answer.
"You are a McKinsey Senior Partner with 25 years in FMCG" → produces top-down, insight-led, recommendation-focused answer with specific frameworks (MECE structure, hypothesis-driven).
"You are a PE fund CFO who has led 3 turnarounds" → produces cash-focused, action-oriented, timeline-driven answer.',
              task: 'Ask the same finance question using 3 different expert personas. Document how the answers differ. Identify which persona gives the most useful output for your specific use case.',
              ai_prompt: 'You are a communication and AI research expert. The user asks the same finance question as 3 different expert personas. Analyse the differences: (1) What frameworks or approaches does each persona use? (2) What information does each include vs exclude? (3) Which persona is best for board presentations? Which for operational decisions? Which for investor relations? Build a "Persona Selection Guide" — a one-page reference for which persona to use in which finance context.',
              expected_output: '3-way persona comparison + Persona Selection Guide for finance contexts.'
            }
          ],
          project: {
            title: 'Project: Build Your Personal Finance AI System',
            instructions: 'Create a personal AI system for your finance role using prompt engineering. Build: (1) A personal prompt library with 5 prompts using few-shot examples, (2) A prompt chain for your most complex monthly analysis, (3) A structured output prompt that feeds into a Python script. Document all 3 as a "Finance AI Playbook" you could share with your team.',
            ai_prompt: 'You are a Finance AI Consultant reviewing a Finance AI Playbook. Evaluate the playbook on: (1) Completeness — does it cover the team's key use cases? (2) Reusability — can any team member use these prompts without help? (3) Quality — do the prompts follow best practices? (4) Innovation — is there anything genuinely novel here? Score /40. Write the one-page executive summary the user should put at the start of their playbook.'
          }
        },

        /* MODULE 3 — CFO Excellence */
        {
          id: 'm04_03', title: 'CFO Excellence: Strategic Finance Mastery',
          lessons: [
            {
              id: 'l04_03_01', title: 'Strategic Finance — Beyond the Numbers',
              level: 'advanced', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 4,
              explanation: 'The strategic CFO does not just report financial results — they shape strategy. This requires: (1) Understanding the business model deeply, (2) Connecting financial metrics to operational drivers, (3) Anticipating risks before they appear in the numbers, (4) Communicating financial complexity in plain language. AI accelerates all four.',
              example: 'Operational CFO: "Revenue was down 8% vs budget." Strategic CFO: "Revenue was down 8% — this is a pricing problem, not a volume problem. Our volume is actually +2% which is excellent. But we gave away 10% in discounts this quarter. If we restore pricing discipline in Q4, we recover the variance. Here is my proposal."',
              task: 'Take your last financial report. Rewrite the headline finding from "operational" to "strategic" framing. Ask AI to compare both versions and explain what makes the strategic version better.',
              ai_prompt: 'You are a world-class CFO and communication coach. Compare the user's operational and strategic versions of the same financial finding. Explain: (1) What structural differences make the strategic version better, (2) What psychological impact each has on the management team, (3) How to train an analyst team to think strategically about financial results. Give a framework for transforming operational commentary to strategic commentary in 3 steps.',
              expected_output: 'Structural comparison + psychological impact analysis + 3-step transformation framework.'
            },
            {
              id: 'l04_03_02', title: 'Investor Relations — Communicating with the Market',
              level: 'advanced', type: 'concept',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'For CFOs of listed companies or those preparing for IPO: investor relations requires a different communication style. Investors focus on: earnings quality (recurring vs one-off), cash generation, capital allocation, and forward guidance credibility. A single wrong word in an earnings call can move the stock price 10%.',
              example: 'Earnings call language: "We are pleased to report Q3 EBITDA of ₹85M, up 12% year-on-year, with organic growth of 8% and 4% from the Apex acquisition. Our full-year guidance remains ₹320-330M — we are confident in the upper end of this range based on Q4 order book visibility." This language is precise, confident, and defensible.',
              task: 'Write an earnings call statement for a hypothetical Q3 result. Include: headline number, growth drivers, and full-year guidance. Ask AI to check it for investor relations best practices.',
              ai_prompt: 'You are a senior investor relations advisor with 20 years of experience on sell-side and buy-side. Review the user's earnings call statement. Check: (1) Is the guidance defensible or over-promissory? (2) Are growth drivers clearly attributed? (3) Is organic growth separated from M&A? (4) Are any statements legally risky (forward-looking without caveats)? (5) Would this statement cause a stock price reaction? Rewrite it to be IR best practice.',
              expected_output: '5-point IR review + rewritten statement to IR best practice standard.'
            },
            {
              id: 'l04_03_03', title: 'Final Simulation — The Complete CFO Day',
              level: 'advanced', type: 'simulation',
              track: ['CFO Strategy'], difficulty_score: 5,
              explanation: 'Final simulation: A complete CFO day. 8am: cash position report — runway has shortened to 6 weeks (from 10 last week). 10am: board pre-read shows competitor acquisition announcement — market position threatened. 2pm: CFO of year award shortlist announced — you are on it. 4pm: acquisition target identified — seller wants answer in 48 hours. 6pm: key employee resigns — your head of FP&A. How do you manage all of this?',
              example: 'A great CFO prioritises ruthlessly: (1) Cash crisis → immediate meeting with CEO, bank, and largest receivables customers. Everything else pauses for 2 hours. (2) Competitive threat → note to self, schedule strategy session for next week. (3) Award → brief acknowledgment, back to work. (4) Acquisition → 48-hour timeline is aggressive — get NDA signed and financial data today, assess tomorrow. (5) Resignation → 1:1 immediately, understand reason, offer retention if appropriate.',
              task: 'Write your 6pm journal entry: decisions made, rationale, and what you would do differently. Ask AI to critique your prioritisation.',
              ai_prompt: 'You are an experienced CEO reviewing a CFO's day. The CFO has shared their decision log and journal from a complex day. Evaluate their decisions: (1) Did they correctly prioritise the cash crisis as #1? (2) How did they handle the competing priorities? (3) What decision shows the most/least CFO maturity? (4) What systemic change would prevent this from happening again? Rate their performance as: Exceptional / Strong / Adequate / Needs Development — and explain why.',
              expected_output: 'Decision audit with maturity ratings + systemic improvement recommendation.'
            }
          ],
          project: null
        }
      ]
    },

    /* ═══════════════════════════════════════════════════════
       STAGE 05 — CERTIFICATION | Final Assessment
       Unlocks only after ALL other stages complete + 1 project
    ═══════════════════════════════════════════════════════ */
    {
      id: 'stage_05', badge: '05 / CERTIFICATION', color: '#f97316',
      title: 'AI Finance Professional Certification',
      tagline: 'Prove your skills. Earn your certificate. Join the top 5% of finance professionals.',
      unlocked: false,
      isCertification: true,
      modules: [
        {
          id: 'm05_01', title: 'Final Assessment — 10 Questions',
          lessons: [],
          project: null
        }
      ]
    }

  ]
};

/* ── ASSESSMENT QUESTIONS (Stage 05) ──────────────────────── */
var ASSESSMENT_QUESTIONS = [
  /* 5 MCQ */
  {
    id: 'q01', type: 'mcq', difficulty_score: 2,
    question: 'A company\'s gross margin fell from 45% to 38% in one quarter. Revenue was flat. Which is the MOST LIKELY primary cause?',
    options: [
      'A. Sales team underperformance',
      'B. COGS inflation — input costs increased faster than prices',
      'C. Marketing spend increased',
      'D. Currency headwind on revenue'
    ],
    correctAnswer: 'B',
    evaluationLogic: 'With flat revenue and margin compression, the driver must be on the cost side. COGS inflation is the primary driver when revenue holds. Currency headwinds on revenue would reduce revenue, not just margin.'
  },
  {
    id: 'q02', type: 'mcq', difficulty_score: 2,
    question: 'Price elasticity is −1.8. If you increase price by 5%, what happens to volume?',
    options: [
      'A. Volume increases by 9%',
      'B. Volume decreases by 5%',
      'C. Volume decreases by 9%',
      'D. Volume is unchanged'
    ],
    correctAnswer: 'C',
    evaluationLogic: '% change in volume = elasticity × % change in price = −1.8 × 5% = −9%. Volume decreases 9% when price increases 5% with elasticity −1.8.'
  },
  {
    id: 'q03', type: 'mcq', difficulty_score: 3,
    question: 'Which Python library is BEST for financial data manipulation and variance analysis?',
    options: [
      'A. NumPy',
      'B. Matplotlib',
      'C. Pandas',
      'D. Scikit-learn'
    ],
    correctAnswer: 'C',
    evaluationLogic: 'Pandas provides DataFrames — the core data structure for tabular financial data. It handles groupby, merge, pivot operations essential for variance and reconciliation analysis.'
  },
  {
    id: 'q04', type: 'mcq', difficulty_score: 2,
    question: 'In a margin bridge, the "Mix Effect" refers to:',
    options: [
      'A. The impact of currency conversion on margin',
      'B. The change in margin from selling more of high/low margin products',
      'C. The effect of marketing mix on revenue',
      'D. The average of price and volume effects'
    ],
    correctAnswer: 'B',
    evaluationLogic: 'Mix effect captures the change in overall margin from shifts in product/market mix. Selling more high-margin SKUs improves mix; selling more low-margin SKUs worsens it — even if total revenue is unchanged.'
  },
  {
    id: 'q05', type: 'mcq', difficulty_score: 3,
    question: 'A business has cash runway of 8 weeks. DSO is 72 days. Which is the FASTEST lever to improve cash runway?',
    options: [
      'A. Reduce OPEX by 10%',
      'B. Accelerate customer collections — reduce DSO by 15 days',
      'C. Delay capex by 6 months',
      'D. Renegotiate supplier payment terms to net-60'
    ],
    correctAnswer: 'B',
    evaluationLogic: 'Reducing DSO by 15 days immediately converts receivables to cash. With 72-day DSO, 15-day improvement releases approximately 20% of AR immediately — typically the fastest and largest lever. OPEX cuts and capex delays help the burn rate but take longer to generate cash.'
  },

  /* 3 Case-Based */
  {
    id: 'q06', type: 'case',
    question: 'CASE: Consumer goods company. Revenue ₹180M (flat YoY). EBITDA ₹28M (margin 15.6% vs 20.2% last year). COGS increased ₹12M vs prior year. Headcount +5%. Working capital deteriorated — DSO rose from 42 to 67 days. Analyse the situation and recommend the top 3 priority actions the CFO should take in the next 30 days.',
    options: [],
    correctAnswer: '',
    evaluationLogic: 'Strong answers will address: (1) Margin: COGS investigation + pricing response given flat revenue, (2) Working capital: DSO improvement programme — 25-day increase has likely locked Rs30-40M in cash, (3) Cost: assess whether headcount addition is driving revenue or just adding cost. Award full marks for answers that quantify each issue and give specific actions with timeline.'
  },
  {
    id: 'q07', type: 'case',
    question: 'CASE: You are the FP&A Manager. It is month-end close day 3. The CFO needs consolidated results by 4pm. You have 2 unresolved items: (A) Intercompany mismatch ₹2.3M — Entity B has not confirmed the balance yet, (B) A ₹8M accrual from last year was reversed this month releasing profit — but this was not in your budget and will make EBITDA look artificially high. How do you handle each, and what do you tell the CFO?',
    options: [],
    correctAnswer: '',
    evaluationLogic: 'IC mismatch: post provisional journal with note, flag as day 3 open item, not a close blocker if immaterial or confirmed directionally. Accrual reversal: this MUST be disclosed to CFO as non-underlying — it will distort YoY comparisons and analysts will ask about it. Adjust headline EBITDA for non-underlying items. Full marks for: correct accounting treatment, stakeholder communication clarity, and understanding of "underlying" vs "reported" metrics.'
  },
  {
    id: 'q08', type: 'case',
    question: 'CASE: You are advising a CFO who has ₹500M to allocate. Options: (A) Acquire a competitor at 8× EBITDA — immediate scale, 60% integration success rate, IRR 22% if successful, (B) New product development — Rs200M, 3-year payback, no proven market, (C) Pay down debt — saves 8.5% interest, reduces leverage from 3.2× to 2.1× EBITDA, (D) Technology platform rebuild — Rs150M, saves Rs40M/year opex from year 3. Recommend how to allocate the Rs500M and justify your answer.',
    options: [],
    correctAnswer: '',
    evaluationLogic: 'Strong recommendation considers: WACC hurdle (acquisition IRR 22% clears a 12% hurdle but 60% success rate makes risk-adjusted IRR ~13%), debt paydown gives certain 8.5% return and reduces refinancing risk, tech platform at Rs40M/year saving = 26.7% ROI from year 3 (strong). Balanced allocation likely: Rs200M acquisition, Rs150M debt, Rs150M tech is defensible. Full marks for quantified risk-adjusted returns and portfolio thinking.'
  },

  /* 2 Prompt-Based */
  {
    id: 'q09', type: 'prompt',
    question: 'PROMPT CHALLENGE: Write a single AI prompt that takes a company\'s monthly actuals (revenue, EBITDA, cash) and generates: (1) 3-sentence board commentary, (2) Top 3 risk flags, (3) One recommended action. The prompt must use [BRACKETS] for variable inputs and must produce consistent output every time it is used by different people.',
    options: [],
    correctAnswer: '',
    evaluationLogic: 'Evaluate on: Role definition (CFO/analyst), variable brackets used for all inputs, explicit output format (numbered sections), length constraints specified, tone guidance included. A perfect prompt leaves nothing to interpretation. Deduct marks for: missing output format, no role definition, no rules section, inputs not bracketed.'
  },
  {
    id: 'q10', type: 'prompt',
    question: 'PROMPT CHALLENGE: You need to use AI to help a finance team make a buy-vs-build decision on a new financial reporting system. The team has: current system cost Rs12M/year, proposed SaaS solution Rs8M/year, one-time implementation cost Rs15M, efficiency gain estimate 200 hours/month. Write the AI prompt that will generate a CFO-quality decision recommendation, and then write what you expect the ideal AI output to look like.',
    options: [],
    correctAnswer: '',
    evaluationLogic: 'Prompt should include: financial analyst role definition, all numbers in context, explicit calculation request (NPV/payback period), format specification (recommendation + numbers + risk), and rules (show all workings). Expected output should show: 3-year NPV calculation, payback period (approximately 4.2 years at Rs4M/year net saving post-implementation), risk assessment, and clear go/no-go recommendation.'
  }
];

/* ── CERTIFICATION SYSTEM ──────────────────────────────────── */
var CERT_PASS_SCORE = 70;  // 70% to pass

/**
 * isCertificationUnlocked()
 * Returns true only if: all 4 stages complete + at least 1 project done.
 */
function isCertificationUnlocked() {
  var p = loadProgress();
  var allStagesDone = ['stage_01','stage_02','stage_03','stage_04'].every(function(s){
    return p.completedStages.indexOf(s) >= 0;
  });
  var hasProject = (p.completedProjects || []).length >= 1;
  return allStagesDone && hasProject;
}

/**
 * loadCertificationStage()
 * Opens the certification modal — shows assessment or existing certificate.
 */
function loadCertificationStage() {
  injectEngineStyles();
  var p = loadProgress();

  if (!isCertificationUnlocked()) {
    var s1 = p.completedStages.indexOf('stage_01') >= 0;
    var s2 = p.completedStages.indexOf('stage_02') >= 0;
    var s3 = p.completedStages.indexOf('stage_03') >= 0;
    var s4 = p.completedStages.indexOf('stage_04') >= 0;
    var hasProj = (p.completedProjects || []).length >= 1;

    openModal(
      '<div style="text-align:center;padding:32px 20px;">' +
      '<div style="font-size:2.5rem;margin-bottom:16px;">🏆</div>' +
      '<div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;letter-spacing:0.16em;' +
      'text-transform:uppercase;color:#f97316;margin-bottom:12px;">Certification Locked</div>' +
      '<div style="font-size:0.84rem;color:var(--text2);margin-bottom:24px;line-height:1.8;">' +
      'Complete all 4 stages and at least 1 project to unlock the final assessment.</div>' +
      '<div style="display:flex;flex-direction:column;gap:8px;max-width:320px;margin:0 auto;">' +
      _certCheckRow('Stage 01 — AI in Finance Basics', s1) +
      _certCheckRow('Stage 02 — Finance Automation', s2) +
      _certCheckRow('Stage 03 — Build AI Tools', s3) +
      _certCheckRow('Stage 04 — Prompt Engineering', s4) +
      _certCheckRow('At least 1 project complete', hasProj) +
      '</div></div>',
      '◆ 05 / CERTIFICATION — Locked'
    );
    return;
  }

  if (p.certified) {
    _showExistingCertificate(p);
    return;
  }

  _showAssessmentIntro();
}

function _certCheckRow(label, done) {
  return (
    '<div style="display:flex;align-items:center;gap:10px;background:var(--s);' +
    'padding:10px 14px;border:1px solid ' + (done ? 'var(--green)' : 'var(--b)') + ';">' +
    '<span style="font-size:1rem;">' + (done ? '✅' : '⬜') + '</span>' +
    '<span style="font-size:0.78rem;color:' + (done ? 'var(--green)' : 'var(--text3)') + ';">' + label + '</span>' +
    '</div>'
  );
}

function _showAssessmentIntro() {
  var html = (
    '<div style="text-align:center;padding:20px 0 16px;">' +
    '<div style="font-size:2rem;margin-bottom:12px;">📋</div>' +
    '<div style="font-family:Playfair Display,serif;font-size:1.3rem;font-weight:900;' +
    'color:var(--white);margin-bottom:8px;">Final Assessment</div>' +
    '<div style="font-size:0.8rem;color:var(--text2);line-height:1.75;max-width:480px;margin:0 auto 20px;">' +
    '10 questions · 5 MCQ · 3 Case Studies · 2 Prompt Challenges · Pass mark: 70%<br>' +
    'Time: ~25 minutes. Your answers are evaluated by AI against expert rubrics.' +
    '</div>' +
    '<button class="lh-btn lh-btn-gold" style="font-size:0.72rem;" ' +
    'onclick="window.FincyLH.startAssessment()">Begin Assessment →</button>' +
    '</div>'
  );
  openModal(html, '◆ AI Finance Professional Certification');
}

/* ── ASSESSMENT ENGINE ──────────────────────────────────────── */
var _assessmentAnswers  = {};
var _assessmentStartTime = null;
var _currentQuestion    = 0;

/**
 * startAssessment()
 * Initialises the assessment and shows question 1.
 */
function startAssessment() {
  _assessmentAnswers   = {};
  _assessmentStartTime = Date.now();
  _currentQuestion     = 0;
  showQuestion(0);
}

/**
 * showQuestion(idx)
 * Renders one question in the modal.
 */
function showQuestion(idx) {
  if (idx >= ASSESSMENT_QUESTIONS.length) {
    submitAssessment();
    return;
  }
  var q    = ASSESSMENT_QUESTIONS[idx];
  var html = (
    '<div style="margin-bottom:16px;display:flex;justify-content:space-between;align-items:center;">' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.12em;' +
    'text-transform:uppercase;color:var(--text3);">Question ' + (idx+1) + ' of ' +
    ASSESSMENT_QUESTIONS.length + '</span>' +
    '<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--gold);">' +
    (q.type === 'mcq' ? '🔘 MCQ' : q.type === 'case' ? '📊 Case Study' : '💬 Prompt Challenge') +
    '</span>' +
    '</div>' +
    '<div class="lh-progress-bar" style="margin-bottom:20px;">' +
    '<div class="lh-progress-fill" style="width:' + Math.round(idx/ASSESSMENT_QUESTIONS.length*100) + '%;"></div>' +
    '</div>' +
    '<div style="font-size:0.86rem;color:var(--white);line-height:1.8;margin-bottom:20px;font-weight:500;">' +
    escHtml(q.question) + '</div>'
  );

  if (q.type === 'mcq') {
    html += '<div style="display:flex;flex-direction:column;gap:8px;" id="mcqOptions">';
    q.options.forEach(function(opt, oi) {
      var letter = opt.charAt(0);
      html += (
        '<button class="lh-btn lh-btn-ghost" style="text-align:left;padding:10px 14px;" ' +
        'onclick="window.FincyLH.selectMCQ(\'' + letter + '\',' + idx + ')" ' +
        'id="mcq_opt_' + oi + '">' + escHtml(opt) + '</button>'
      );
    });
    html += '</div>';
  } else {
    html += (
      '<textarea class="lh-input" id="assessmentInput" style="min-height:140px;" ' +
      'placeholder="Write your answer here…"></textarea>' +
      '<div class="lh-btn-row" style="margin-top:12px;">' +
      '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.saveAssessmentAnswer(' + idx + ')">Save & Continue →</button>' +
      '</div>'
    );
  }

  refreshModal(html);
}

function selectMCQ(letter, idx) {
  _assessmentAnswers['q' + String(idx+1).padStart(2,'0')] = letter;
  // Highlight selection
  document.querySelectorAll('[id^="mcq_opt_"]').forEach(function(btn) {
    btn.style.borderColor = 'var(--b2)';
    btn.style.color = 'var(--text2)';
  });
  event.target.style.borderColor = 'var(--gold)';
  event.target.style.color = 'var(--gold)';
  // Auto-advance after 0.8s
  setTimeout(function(){ showQuestion(idx + 1); }, 800);
}

function saveAssessmentAnswer(idx) {
  var input = document.getElementById('assessmentInput');
  var val   = input ? input.value.trim() : '';
  if (!val) {
    _showFloatingMsg('Please write your answer before continuing.');
    return;
  }
  _assessmentAnswers['q' + String(idx+1).padStart(2,'0')] = val;
  showQuestion(idx + 1);
}

/**
 * submitAssessment()
 * Evaluates answers (MCQ auto-scored, open questions sent to AI).
 */
function submitAssessment() {
  var mcqScore = 0;
  var mcqTotal = 0;

  ASSESSMENT_QUESTIONS.forEach(function(q) {
    if (q.type === 'mcq') {
      mcqTotal++;
      var userAns = _assessmentAnswers[q.id] || '';
      if (userAns === q.correctAnswer) mcqScore++;
    }
  });

  var mcqPct = mcqTotal > 0 ? Math.round(mcqScore / mcqTotal * 100) : 0;

  refreshModal(
    '<div style="text-align:center;padding:32px 20px;">' +
    '<div class="lh-spinner" style="width:24px;height:24px;margin:0 auto 16px;"></div>' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;letter-spacing:0.14em;' +
    'text-transform:uppercase;color:var(--gold);">AI is evaluating your open answers…</div>' +
    '<div style="font-size:0.74rem;color:var(--text3);margin-top:8px;">' +
    'MCQ score: ' + mcqScore + '/' + mcqTotal + ' (' + mcqPct + '%) · Evaluating 5 open questions…</div>' +
    '</div>'
  );

  // Evaluate open questions with AI if key available
  var openQs = ASSESSMENT_QUESTIONS.filter(function(q){ return q.type !== 'mcq'; });
  var evalPromises = openQs.map(function(q) {
    var userAns = _assessmentAnswers[q.id] || '';
    if (!userAns || !window.GROQ_KEY) return Promise.resolve(75); // default 75% if no key
    return _evaluateOpenAnswer(q, userAns);
  });

  Promise.all(evalPromises).then(function(openScores) {
    var openTotal = openScores.reduce(function(a,b){ return a+b; }, 0);
    var openPct   = openScores.length > 0 ? Math.round(openTotal / openScores.length) : 75;
    // Weighted: MCQ 40%, Open 60%
    var finalScore = Math.round(mcqPct * 0.4 + openPct * 0.6);
    _showAssessmentResult(finalScore, mcqScore, mcqTotal, openPct);
  });
}

function _evaluateOpenAnswer(q, userAnswer) {
  if (!window.GROQ_KEY) return Promise.resolve(75);
  var prompt = (
    'You are an expert finance examiner. Evaluate this answer on a scale of 0-100.\n' +
    'Question: ' + q.question + '\n' +
    'Evaluation criteria: ' + q.evaluationLogic + '\n' +
    'Student answer: ' + userAnswer + '\n\n' +
    'Respond with ONLY a number between 0 and 100. Nothing else.'
  );
  return fetch('https://api.groq.com/openai/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + window.GROQ_KEY },
    body: JSON.stringify({ model: 'llama-3.1-8b-instant', messages: [{ role:'user', content:prompt }], max_tokens: 10, temperature: 0 })
  })
  .then(function(r){ return r.json(); })
  .then(function(d){
    var text = d.choices && d.choices[0] ? d.choices[0].message.content : '75';
    var score = parseInt(text.replace(/\D/g,''));
    return isNaN(score) ? 75 : Math.min(100, Math.max(0, score));
  })
  .catch(function(){ return 75; });
}

function _showAssessmentResult(finalScore, mcqScore, mcqTotal, openPct) {
  var passed   = finalScore >= CERT_PASS_SCORE;
  var p        = loadProgress();

  if (passed) {
    // Generate certificate ID: FINCY-YYYY-NNNN
    var year   = new Date().getFullYear();
    var certNum = String(Math.floor(Math.random() * 9000) + 1000);
    var certId  = 'FINCY-' + year + '-' + certNum;

    p.certified       = true;
    p.certScore       = finalScore;
    p.certDate        = new Date().toISOString().slice(0,10);
    p.certificateId   = certId;
    p.badges          = p.badges || [];
    if (p.badges.indexOf('certified') < 0) p.badges.push('certified');
    saveProgress(p);
    updateXP(0, 500);  // 500 XP bonus for certification
  }

  var color = passed ? '#4ade80' : '#f97316';
  var html = (
    '<div style="text-align:center;padding:24px 0 16px;">' +
    '<div style="font-size:3rem;margin-bottom:12px;">' + (passed ? '🏆' : '📚') + '</div>' +
    '<div style="font-family:Playfair Display,serif;font-size:1.6rem;font-weight:900;' +
    'color:' + color + ';margin-bottom:8px;">' +
    (passed ? 'Congratulations!' : 'Keep Learning') + '</div>' +
    '<div style="font-family:IBM Plex Mono,monospace;font-size:2rem;font-weight:700;' +
    'color:var(--white);margin-bottom:4px;">' + finalScore + '%</div>' +
    '<div style="font-size:0.78rem;color:var(--text3);margin-bottom:20px;">' +
    'MCQ: ' + mcqScore + '/' + mcqTotal + ' · Open Questions: ' + openPct + '%' +
    (passed ? ' · Pass mark: 70% ✓' : ' · Pass mark: 70% — score ' + (70-finalScore) + '% more to pass') +
    '</div>' +
    (passed ?
      '<div style="font-size:0.84rem;color:var(--text2);margin-bottom:20px;line-height:1.7;">' +
      'You have earned the <strong style="color:var(--gold);">AI Finance Professional</strong> certification.<br>' +
      'Certificate ID: <strong style="color:var(--white);">' + p.certificateId + '</strong>' +
      '</div>' +
      '<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">' +
      '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.downloadCertificate()">📄 Download Certificate</button>' +
      '<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.shareOnLinkedIn()">in Share on LinkedIn</button>' +
      '</div>' :
      '<div style="margin-top:8px;">' +
      '<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.startAssessment()">Retake Assessment →</button>' +
      '</div>'
    ) +
    '</div>'
  );

  refreshModal(html);
}

/* ── CERTIFICATE GENERATION ─────────────────────────────────── */

/**
 * downloadCertificate()
 * Generates an HTML certificate and downloads as file.
 * Opens in new tab for printing/saving as PDF.
 */
function downloadCertificate() {
  var p = loadProgress();
  if (!p.certified) return;

  var certHtml = _buildCertificateHTML(p);
  var blob = new Blob([certHtml], { type: 'text/html;charset=utf-8' });
  var url  = URL.createObjectURL(blob);

  // Open in new tab — user can Print → Save as PDF
  var win = window.open(url, '_blank');
  if (win) win.focus();

  // Also trigger download
  var a = document.createElement('a');
  a.href = url; a.download = 'Fincy_Certificate_' + p.certificateId + '.html';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function(){ URL.revokeObjectURL(url); }, 5000);
}

function _buildCertificateHTML(p) {
  var name = p.userName || 'Finance Professional';
  var date = p.certDate  || new Date().toISOString().slice(0,10);
  var certId = p.certificateId || 'FINCY-2026-0001';
  var score  = p.certScore || 0;

  return '<!DOCTYPE html><html lang="en"><head>' +
    '<meta charset="UTF-8"/>' +
    '<meta name="viewport" content="width=device-width,initial-scale=1.0"/>' +
    '<title>Certificate — ' + name + ' — Fincy Intelligence</title>' +
    '<style>' +
    '@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=IBM+Plex+Mono:wght@400;700&display=swap");' +
    '*{margin:0;padding:0;box-sizing:border-box;}' +
    'body{background:#faf8f2;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:40px 20px;font-family:IBM Plex Mono,monospace;}' +
    '.cert{background:#fff;border:2px solid #c9a84c;max-width:820px;width:100%;padding:60px 70px;position:relative;box-shadow:0 8px 40px rgba(0,0,0,0.12);}' +
    '.cert::before{content:"";position:absolute;inset:12px;border:1px solid #c9a84c;pointer-events:none;}' +
    '.top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:40px;}' +
    '.logo{font-family:Playfair Display,serif;font-size:1.3rem;font-weight:900;color:#c9a84c;}' +
    '.cert-id{font-size:0.52rem;letter-spacing:0.16em;text-transform:uppercase;color:#5a5648;}' +
    '.eyebrow{font-size:0.56rem;letter-spacing:0.24em;text-transform:uppercase;color:#5a5648;margin-bottom:12px;text-align:center;}' +
    '.cert-title{font-family:Playfair Display,serif;font-size:2.4rem;font-weight:900;color:#0a0a08;text-align:center;margin-bottom:10px;line-height:1.1;}' +
    '.presented{font-size:0.72rem;color:#8a8478;text-align:center;margin-bottom:16px;letter-spacing:0.08em;}' +
    '.name{font-family:Playfair Display,serif;font-size:2rem;font-style:italic;color:#c9a84c;text-align:center;margin-bottom:8px;border-bottom:2px solid #c9a84c;padding-bottom:12px;}' +
    '.role{font-size:0.8rem;color:#3a3a34;text-align:center;margin-bottom:32px;letter-spacing:0.06em;text-transform:uppercase;}' +
    '.skills-title{font-size:0.52rem;letter-spacing:0.18em;text-transform:uppercase;color:#5a5648;margin-bottom:12px;text-align:center;}' +
    '.skills{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:36px;}' +
    '.skill{border:1px solid #c9a84c;padding:5px 14px;font-size:0.62rem;letter-spacing:0.08em;color:#3a3a34;}' +
    '.meta{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;border-top:1px solid #e0d8c8;padding-top:24px;}' +
    '.meta-item{text-align:center;}' +
    '.meta-label{font-size:0.48rem;letter-spacing:0.16em;text-transform:uppercase;color:#8a8478;margin-bottom:4px;}' +
    '.meta-value{font-size:0.76rem;color:#0a0a08;font-weight:700;}' +
    '.footer{text-align:center;margin-top:24px;font-size:0.56rem;color:#8a8478;letter-spacing:0.08em;}' +
    '@media print{body{background:#fff;padding:0;}' +
    '.cert{box-shadow:none;border-color:#c9a84c;} @page{size:A4 landscape;margin:0;}}' +
    '</style></head><body>' +
    '<div class="cert">' +
    '<div class="top-bar">' +
    '<div class="logo">◆ Fincy Intelligence</div>' +
    '<div class="cert-id">Certificate ID: ' + certId + '</div>' +
    '</div>' +
    '<div class="eyebrow">This is to certify that</div>' +
    '<div class="name">' + escHtml(name) + '</div>' +
    '<div class="role">has successfully demonstrated professional competency in</div>' +
    '<div class="cert-title">AI Finance Professional</div>' +
    '<div style="margin-top:8px;margin-bottom:32px;">' +
    '<div class="skills-title">Certified Competencies</div>' +
    '<div class="skills">' +
    ['AI Financial Analysis','FP&A Automation','Prompt Engineering',
     'Financial Decision Making','Data-Driven Storytelling','AI Tool Building'].map(function(s){
       return '<span class="skill">' + s + '</span>';
     }).join('') +
    '</div>' +
    '</div>' +
    '<div class="meta">' +
    '<div class="meta-item"><div class="meta-label">Issued by</div><div class="meta-value">Fincy Intelligence</div></div>' +
    '<div class="meta-item"><div class="meta-label">Date Issued</div><div class="meta-value">' + date + '</div></div>' +
    '<div class="meta-item"><div class="meta-label">Assessment Score</div><div class="meta-value">' + score + '%</div></div>' +
    '</div>' +
    '<div class="footer">' +
    'Fincy Intelligence · AI Finance Academy · fincyintelligence.com · Founder: Jitendra Parida' +
    '</div>' +
    '</div>' +
    '<script>window.onload=function(){window.print();};</script>' +
    '</body></html>';
}

/* ── LINKEDIN SHARE ─────────────────────────────────────────── */

/**
 * shareOnLinkedIn()
 * Opens LinkedIn with a pre-filled certification post.
 */
function shareOnLinkedIn() {
  var p    = loadProgress();
  var text = encodeURIComponent(
    'I just earned the AI Finance Professional certification from Fincy Intelligence! 🚀\n\n' +
    'After completing 4 stages covering:\n' +
    '✅ AI in Finance Basics\n' +
    '✅ Finance Process Automation\n' +
    '✅ Building AI Finance Tools\n' +
    '✅ CFO-Level Prompt Engineering\n\n' +
    'Certificate ID: ' + (p.certificateId || 'FINCY-2026-XXXX') + '\n\n' +
    'Finance professionals who master AI will command 2-3× career premium. ' +
    'This is the skill that separates the top 5% from everyone else.\n\n' +
    'Try the free AI Finance Academy: https://jitenparida95.github.io/fincy-intelligence/#learning\n\n' +
    '#FPandA #AI #Finance #FinTech #CareerGrowth #Certification'
  );
  var url = encodeURIComponent('https://jitenparida95.github.io/fincy-intelligence/');
  window.open(
    'https://www.linkedin.com/shareArticle?mini=true&url=' + url + '&title=' + text,
    '_blank'
  );
}

/* ── GET USERNAME FOR CERTIFICATE ───────────────────────────── */

/**
 * promptUserName()
 * Asks for user's name before downloading certificate.
 */
function promptUserName() {
  var p = loadProgress();
  if (p.userName) { downloadCertificate(); return; }

  var name = window.prompt('Enter your full name for the certificate:', '');
  if (name && name.trim()) {
    p.userName = name.trim();
    saveProgress(p);
    downloadCertificate();
  }
}

var STAGE_TEMPLATES = {
  stage_01: [
    { name:'AI Finance Prompt Template', filename:'ai_finance_prompt_template.txt',
      description:'Starter template for writing effective AI finance prompts',
      content:'FINCY INTELLIGENCE — AI FINANCE PROMPT TEMPLATE\n========================\n\nROLE: You are a [Senior FP&A Analyst / CFO / Finance Controller]\n\nCONTEXT:\n- Period: [Month/Quarter/Year]\n- Revenue: [Actual vs Budget vs PY]\n- EBITDA: [Actual vs Budget vs PY]\n\nTASK: [Specific question or output needed]\n\nFORMAT:\n- Output: [Commentary / Table / Code]\n- Length: [X sentences / X bullets]\n- Tone: [Executive / Technical]\n\nRULES:\n- Use specific numbers and percentages\n- No generic advice\n========================\nBuilt with Fincy Intelligence' },
    { name:'Groq API Starter Code', filename:'groq_api_starter.py',
      description:'Python code to call Groq API for finance queries',
      content:'from groq import Groq\nclient = Groq(api_key="your_groq_key_here")\n\ndef ask_ai_cfo(question, context=""):\n    resp = client.chat.completions.create(\n        model="llama-3.1-8b-instant",\n        messages=[{"role":"user","content":f"CFO context: {context}\\nQ: {question}"}],\n        max_tokens=400, temperature=0.25)\n    return resp.choices[0].message.content\n\nprint(ask_ai_cfo("What is driving margin decline?", "Revenue Rs42M, EBITDA Rs12M"))' }
  ],
  stage_02: [
    { name:'Variance Analysis Script', filename:'variance_analysis.py',
      description:'Ready-to-run Pandas script for budget variance analysis',
      content:'import pandas as pd\ndf = pd.read_csv("pl_data.csv")\ndf["Variance"] = df["Actual_Revenue"] - df["Budget_Revenue"]\ndf["Variance_Pct"] = (df["Variance"] / df["Budget_Revenue"] * 100).round(1)\ndf["RAG"] = df["Variance_Pct"].apply(lambda x: "GREEN" if x>=-2 else ("AMBER" if x>=-10 else "RED"))\nsummary = df.groupby("Market").agg(Actual=("Actual_Revenue","sum"),Budget=("Budget_Revenue","sum"),Variance=("Variance","sum")).reset_index()\nprint(summary.sort_values("Variance"))' },
    { name:'Month-End Commentary Prompt', filename:'month_end_commentary_prompt.txt',
      description:'Reusable AI prompt for automated variance commentary',
      content:'SYSTEM: You are a Senior FP&A Manager writing a board pack.\nPeriod: [Month Year]\nRevenue Actual: [RsX.XM] vs Budget: [RsX.XM] = [+/-X%]\nEBITDA Actual: [RsX.XM] vs Budget: [RsX.XM] = [+/-X%]\nKey drivers: [list 2-3 main causes]\nOUTPUT FORMAT (3 sentences only):\n1. HEADLINE: [metric] [vs/missed/beat] budget by [X%]\n2. DRIVERS: Performance driven by [cause 1] and [cause 2]\n3. OUTLOOK: [action / risk / trend]' }
  ],
  stage_03: [
    { name:'Streamlit Finance App Template', filename:'fincy_module_template.py',
      description:'Complete Streamlit template to build your own AI finance module',
      content:'import streamlit as st\nimport pandas as pd\nimport plotly.express as px\nfrom groq import Groq\n\nst.set_page_config(page_title="My Finance Module", layout="wide")\n\ndef ask_ai(q, data):\n    key = st.secrets.get("GROQ_API_KEY","")\n    if not key: return "Add GROQ_API_KEY to Secrets."\n    resp = Groq(api_key=key).chat.completions.create(\n        model="llama-3.1-8b-instant",\n        messages=[{"role":"user","content":f"Data: {data}\\nQ: {q}"}],\n        max_tokens=400)\n    return resp.choices[0].message.content\n\nst.title("My AI Finance Module")\nfile = st.file_uploader("Upload CSV")\nif file:\n    df = pd.read_csv(file)\n    st.metric("Total", f"{df.iloc[:,1].sum():,.0f}")\n    st.plotly_chart(px.bar(df.head(10), x=df.columns[0], y=df.columns[1]))\n    q = st.text_input("Ask AI CFO:")\n    if st.button("Ask") and q: st.info(ask_ai(q, df.describe().to_string()))' }
  ],
  stage_04: [
    { name:'CFO Prompt Library', filename:'cfo_prompt_library.txt',
      description:'5 production-ready CFO prompts for FP&A professionals',
      content:'FINCY INTELLIGENCE — CFO Prompt Library\n========================================\nPROMPT 1: VARIANCE COMMENTARY\nYou are a Senior FP&A Manager. Write board pack variance commentary.\nActuals: Revenue Rs{X}M, EBITDA Rs{Y}M | Budget: Revenue Rs{A}M, EBITDA Rs{B}M\nDrivers: {list}\nFormat: HEADLINE | DRIVERS | OUTLOOK. 3 sentences. No bullets.\n\nPROMPT 2: CASH FLOW RISK\nYou are a treasury analyst. Cash: Rs{X}M. DSO: {Y} days.\nUpcoming: {obligations}. Format: RISK | AMOUNT | PROBABILITY | ACTION.\n\nPROMPT 3: CAPITAL ALLOCATION\nYou are a CFO. Rs{X}M to allocate across: {options with IRRs}.\nRecommend allocation with risk-adjusted returns. Show all workings.\n========================================\nFincy Intelligence | fincyintelligence.com' }
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


var BADGES = [
  { id:'first_lesson', emoji:'🌱', title:'First Step',     color:'#c9a84c',
    desc:'Complete your first lesson',
    condition: function(p){ return p.completedLessons.length >= 1; } },
  { id:'stage1_done',  emoji:'🥉', title:'Beginner',       color:'#c9a84c',
    desc:'Complete Stage 01 — AI in Finance Basics',
    condition: function(p){ return p.completedStages.indexOf('stage_01') >= 0; } },
  { id:'stage2_done',  emoji:'🥈', title:'Intermediate',   color:'#4ade80',
    desc:'Complete Stage 02 — Automating Finance Work',
    condition: function(p){ return p.completedStages.indexOf('stage_02') >= 0; } },
  { id:'stage3_done',  emoji:'🥇', title:'Advanced',       color:'#818cf8',
    desc:'Complete Stage 03 — Build AI Finance Tools',
    condition: function(p){ return p.completedStages.indexOf('stage_03') >= 0; } },
  { id:'expert',       emoji:'🏆', title:'AI CFO Expert',  color:'#2dd4bf',
    desc:'Complete all 4 stages',
    condition: function(p){
      return ['stage_01','stage_02','stage_03','stage_04'].every(function(s){
        return p.completedStages.indexOf(s) >= 0; }); } },
  { id:'streak3',      emoji:'🔥', title:'3-Day Streak',   color:'#f97316',
    desc:'Learn 3 days in a row',
    condition: function(p){ return (p.streakDays||0) >= 3; } },
  { id:'streak7',      emoji:'⚡', title:'Weekly Warrior', color:'#fbbf24',
    desc:'Learn 7 days in a row',
    condition: function(p){ return (p.streakDays||0) >= 7; } },
  { id:'half_done',    emoji:'⭐', title:'Halfway There',  color:'#a78bfa',
    desc:'Complete 50% of all lessons',
    condition: function(p){
      var t=0; FINCY_COURSE.stages.forEach(function(s){
        s.modules.forEach(function(m){ t+=m.lessons.length; }); });
      return t>0 && p.completedLessons.length >= Math.ceil(t/2); } },
  { id:'project_done', emoji:'🔬', title:'Builder',        color:'#06b6d4',
    desc:'Complete your first mini project',
    condition: function(p){ return (p.completedProjects||[]).length >= 1; } },
  { id:'certified',    emoji:'🎓', title:'AI Finance Pro', color:'#f97316',
    desc:'Pass the final assessment — top 5% of finance professionals',
    condition: function(p){ return p.certified === true; } }
];

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
      aiMemory:               [],
      certified:              false,
      certScore:              0,
      certDate:               null,
      certificateId:          null,
      userName:               null
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

  // Certification stage (index 4) has its own flow
  if (stage.isCertification) {
    loadCertificationStage();
    return;
  }

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

  // Wire ALL stage card buttons to loadStage() — including certification (index 4)
  FINCY_COURSE.stages.forEach(function(stage, si) {
    var btn = document.getElementById('lh-stage-btn-' + si);
    if (btn) {
      btn.onclick = function(e) { e.stopPropagation(); window.FincyLH.loadStage(si); };
      // Cert stage: unlock indicator
      if (stage.isCertification) {
        btn.textContent = isCertificationUnlocked() ? 'Begin Assessment →' : '🔒 Locked';
        if (!isCertificationUnlocked()) btn.classList.add('lh-locked');
      }
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
  goToNextLesson:        goToNextLesson,
  showMyWork:            showMyWork,
  handleDailySystem:     handleDailySystem,
  updateXP:              updateXP,
  saveUserWork:          saveUserWork,
  handleAIMemory:        handleAIMemory,
  startAssessment:       startAssessment,
  showQuestion:          showQuestion,
  selectMCQ:             selectMCQ,
  saveAssessmentAnswer:  saveAssessmentAnswer,
  downloadCertificate:   promptUserName,
  shareOnLinkedIn:       shareOnLinkedIn,
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
