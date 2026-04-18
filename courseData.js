'use strict';

var FINCY_COURSE={stages:[{id:"stage_01",badge:"01 / BEGINNER",color:"#c9a84c",title:"AI in Finance Basics",tagline:"Understand what AI is and why it changes everything for finance professionals.",unlocked:true,modules:[{id:"m01_01",title:"AI in Finance Fundamentals",lessons:[{id:"l01_01_01",title:"LLMs Explained in Finance Terms",level:"beginner",type:"concept",track:["FP&A", "CFO Strategy"],difficulty_score:1,explanation:"A Large Language Model like Llama or GPT is trained on billions of documents and generates structured answers. Ask \"Why is EBITDA declining?\" and get a CFO-level response in seconds.",example:"You upload a P&L CSV and ask: Which market has the worst margin trend? The LLM replies: Germany \u2014 EBITDA margin fell from 18% to 11% in Q3, driven by COGS inflation and flat volume.",task:"Write one finance question you wish your team could answer faster. Click Ask AI to see how an LLM responds.",ai_prompt:"You are a senior FP&A analyst. Answer the user finance question in 3-4 sentences as an AI CFO \u2014 direct, with numbers, no fluff.",expected_output:"A concise CFO-style answer with specific reasoning."},{id:"l01_01_02",title:"AI Agents vs LLMs",level:"beginner",type:"concept",track:["Automation"],difficulty_score:1,explanation:"An LLM answers questions. An AI Agent takes actions. The Data Analysis Agent reads your CSV, runs statistics, builds charts, and writes commentary in one click.",example:"LLM: Your DSO is high. Agent: reads AR data, calculates DSO, flags customers over 60 days, generates collections list, saves CSV. One click.",task:"Name one finance task taking 2+ hours. Ask AI how an agent could automate it end to end.",ai_prompt:"You are an AI automation expert for Finance teams. Explain step by step how an AI agent could automate the task. Name specific tools: Python, Pandas, Groq.",expected_output:"Step-by-step automation plan with specific tools named."},{id:"l01_01_03",title:"5 Finance Tasks AI Does Better Than Excel",level:"beginner",type:"concept",track:["FP&A", "Automation"],difficulty_score:1,explanation:"Excel is a calculator. AI is a reasoning engine. Top 5 tasks AI beats Excel: variance commentary, anomaly detection, scenario modelling, reconciliation, and forecasting.",example:"Team using Excel for month-end commentary: 3 hours per analyst times 4 analysts = 12 hours. Same team using Fincy AI: 4 minutes total. Same quality.",task:"Ask AI which of these 5 tasks would save you the most time. Request a specific estimate in hours per month.",ai_prompt:"You are a senior FP&A advisor. Calculate which AI tasks would save the user the most time. Give specific hour estimates per month for each task based on their role.",expected_output:"Ranked list of 5 tasks with specific hours saved per month."},{id:"l01_01_04",title:"Write Your First AI Finance Prompt",level:"beginner",type:"task",track:["FP&A", "CFO Strategy"],difficulty_score:2,explanation:"A great finance prompt has 4 parts: Role, Context, Task, and Format. Missing any part drops quality by 50%.",example:"You are a CFO advising a CEO. EBITDA margin is 12% vs 18% budget. Revenue grew 8% YoY but COGS rose 15%. Write a 2-paragraph board commentary. No bullet points. Executive tone.",task:"Write a prompt for a real finance task using all 4 parts. Ask AI to evaluate it and score it.",ai_prompt:"You are a prompt engineering coach for CFOs. Score the user finance prompt: Role (0-25), Context (0-25), Format (0-25), Rules (0-25) = total /100. Then rewrite it to score 90+.",expected_output:"Score /100 with improvement explanation, then the improved prompt."},{id:"l01_01_05",title:"Case Study \u2014 AI Saves 40 Hours Per Month",level:"beginner",type:"case_study",track:["FP&A"],difficulty_score:2,explanation:"Real case: An FP&A team spent 40 hours every month-end on variance commentary and reporting. After implementing AI tools this dropped to 4 hours. The 36 hours freed were reinvested into strategic analysis.",example:"Workflow: Upload ERP data, AI runs variance analysis, AI writes commentary, human reviews, board pack done. Total AI time: 12 minutes. Human review: 48 minutes. Previous total: 40 hours.",task:"Calculate the value of your own time saved. If you earn Rs15L/year and AI saves 20 hours/month, what is the annual value? Ask AI to help build the business case.",ai_prompt:"You are a CFO helping build a business case for AI tools. Calculate: annual cost of current manual time, ROI of AI tools at Rs5000/month, productivity gain percentage. Give a 3-sentence manager pitch.",expected_output:"Business case with Rs figures, ROI percentage, and a 3-sentence manager pitch."},{id:"l01_01_07",title:"Finance AI Skill 06",level:"beginner",type:"task",track:["FP&A"],difficulty_score:2,explanation:"Stage 1 lesson 6: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_01_08",title:"Finance AI Skill 07",level:"beginner",type:"case_study",track:["CFO Strategy"],difficulty_score:2,explanation:"Stage 1 lesson 7: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_01_09",title:"Finance AI Skill 08",level:"beginner",type:"challenge",track:["FP&A"],difficulty_score:3,explanation:"Stage 1 lesson 8: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_01_10",title:"Finance AI Skill 09",level:"beginner",type:"simulation",track:["CFO Strategy"],difficulty_score:3,explanation:"Stage 1 lesson 9: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_01",title:"Finance AI Skill 10",level:"beginner",type:"concept",track:["FP&A"],difficulty_score:3,explanation:"Stage 1 lesson 10: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Map Your AI Opportunity",instructions:"Create an AI Opportunity Map for your finance role. List top 5 most time-consuming tasks and describe how AI could automate each one.",ai_prompt:"You are a senior AI strategy consultant. Review the user AI Opportunity Map. For each task: validate time estimate, recommend specific AI approach, score automation potential 1-5."}},{id:"m01_02",title:"Practical AI Skills for Finance",lessons:[{id:"l01_02_02",title:"Finance AI Skill 11",level:"beginner",type:"task",track:["CFO Strategy"],difficulty_score:3,explanation:"Stage 1 lesson 11: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_03",title:"Finance AI Skill 12",level:"beginner",type:"case_study",track:["FP&A"],difficulty_score:4,explanation:"Stage 1 lesson 12: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_04",title:"Finance AI Skill 13",level:"beginner",type:"challenge",track:["CFO Strategy"],difficulty_score:4,explanation:"Stage 1 lesson 13: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_05",title:"Finance AI Skill 14",level:"beginner",type:"simulation",track:["FP&A"],difficulty_score:4,explanation:"Stage 1 lesson 14: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_06",title:"Finance AI Skill 15",level:"beginner",type:"concept",track:["CFO Strategy"],difficulty_score:4,explanation:"Stage 1 lesson 15: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_07",title:"Finance AI Skill 16",level:"beginner",type:"task",track:["FP&A"],difficulty_score:5,explanation:"Stage 1 lesson 16: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_08",title:"Finance AI Skill 17",level:"beginner",type:"case_study",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 1 lesson 17: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_09",title:"Finance AI Skill 18",level:"beginner",type:"challenge",track:["FP&A"],difficulty_score:5,explanation:"Stage 1 lesson 18: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_02_10",title:"Finance AI Skill 19",level:"beginner",type:"simulation",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 1 lesson 19: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l01_03_01",title:"Finance AI Skill 20",level:"beginner",type:"concept",track:["FP&A"],difficulty_score:5,explanation:"Stage 1 lesson 20: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Your First AI Finance Prompt",instructions:"Build and test an AI prompt for a real finance task from your job. Document the prompt, the output, and the time saved.",ai_prompt:"You are a finance AI mentor. Review the user first AI finance prompt. Score it on practicality (1-5), accuracy (1-5), and business impact (1-5). Total /15."}}]},{id:"stage_02",badge:"02 / INTERMEDIATE",color:"#4ade80",title:"Automating Finance Work",tagline:"Eliminate manual work. Build automation that runs every month-end in seconds.",unlocked:false,modules:[{id:"m02_01",title:"Python for Finance",lessons:[{id:"l02_01_01",title:"Pandas for FP&A",level:"intermediate",type:"concept",track:["Automation", "FP&A"],difficulty_score:2,explanation:"Pandas is Excel but 100x faster and scriptable. Read a CSV, filter by market, group by brand, calculate variance in 5 lines. Once scripted it runs every month in 2 seconds instead of 2 hours.",example:"import pandas as pd; df = pd.read_csv(\"pl.csv\"); df[\"Var\"] = df[\"Actual\"] - df[\"Budget\"]; print(df.groupby(\"Market\")[\"Var\"].sum().sort_values())",task:"Ask AI to write a Pandas script calculating budget variance by market from a CSV with Market, Brand, Actual_Revenue, Budget_Revenue columns.",ai_prompt:"You are a Python/Pandas expert for finance. Write a complete runnable script: reads CSV with Market, Brand, Actual_Revenue, Budget_Revenue; calculates Variance and Variance%; groups by Market; sorts by worst performers; prints clean table with comments.",expected_output:"Complete runnable script with comments on every step."},{id:"l02_01_02",title:"Automating Monthly Close Commentary",level:"intermediate",type:"task",track:["FP&A", "Automation"],difficulty_score:2,explanation:"The most time-consuming FP&A task is writing variance commentary. AI does it in seconds. Typically saves 2 hours per person per close cycle.",example:"Prompt result: EBITDA missed by Rs2.3M (-8%). Revenue was in line but COGS spiked due to freight (+12% YoY) and promo overspend (+15% vs plan). Three-sentence board pack. Executive tone.",task:"Write a commentary prompt for your P&L. Include revenue, margin, and 2 key drivers. Ask AI to generate board-ready commentary.",ai_prompt:"You are a Senior FP&A Manager. Write exactly 3 sentences: (1) Headline vs budget with numbers. (2) Two specific driver explanations with figures. (3) Outlook and corrective action. CFO language. No bullets.",expected_output:"3 sentences of board-ready variance commentary."},{id:"l02_01_03",title:"Margin Bridge Analysis",level:"intermediate",type:"concept",track:["FP&A", "CFO Strategy"],difficulty_score:3,explanation:"A margin bridge decomposes gross margin change into Volume, Price, Mix, and Cost effects. CFOs use it to identify which lever to pull: price increase, cost reduction, or volume push.",example:"Margin change -3.2pp breakdown: Volume +1.1pp, Price -2.0pp, Mix +0.3pp, Cost -2.6pp. Total: -3.2pp. Largest driver is Cost at -2.6pp \u2014 vendor renegotiation is priority action.",task:"Build a margin bridge: prior year margin 54%, current 49%, Revenue +6%, COGS +14%, volume +4%. Ask AI to identify the largest driver and recommend one corrective action.",ai_prompt:"You are a CFO and financial modelling expert. Build a margin bridge table showing each effect in pp. Identify the largest driver. Give one specific corrective recommendation with expected margin recovery timeline.",expected_output:"Margin bridge table in pp + largest driver + recommendation with timeline."},{id:"l02_01_04",title:"Scenario Modelling \u2014 3-Case Framework",level:"intermediate",type:"task",track:["FP&A", "CFO Strategy"],difficulty_score:3,explanation:"Every board needs 3 scenarios: Base, Bull, Bear. Effective modelling identifies key assumptions for each case and quantifies the range of outcomes.",example:"Base: Revenue Rs42.8M, EBITDA 28.3%. Bull: volume +15%, margin 30.1%. Bear: volume -10%, margin 24.8%. Trigger events defined for each scenario.",task:"Define your base case with 3 financial metrics. Ask AI to build Bull and Bear scenarios with specific assumptions and financial outcomes.",ai_prompt:"You are a financial planning expert. Build Bull and Bear scenarios from the user base case. Present as a clean 3-column table with Trigger Events row at the bottom.",expected_output:"3-column scenario table with trigger events row."},{id:"l02_01_05",title:"ERP vs Bank Reconciliation Automation",level:"intermediate",type:"concept",track:["Accounting", "Automation"],difficulty_score:2,explanation:"Reconciliation matches two datasets and finds differences. Using a composite key (prefix + date + amount) catches breaks that single-key matching misses. Pandas makes this a 10-line script.",example:"merged = pd.merge(erp, bank, on=[\"prefix\",\"date\",\"amount\"], how=\"outer\", indicator=True). Three outcomes: both matched, only in ERP, only in bank.",task:"Ask AI to write a Python reconciliation script: loads 2 CSVs, merges on an ID column, classifies each row as Matched, Amount Break, Missing in A, or Missing in B, exports an exceptions report.",ai_prompt:"You are a Python expert teaching reconciliation automation. Write complete Python: load 2 CSVs, merge on ID column, classify rows into 4 categories, export exceptions as CSV. Include comments and error handling.",expected_output:"Complete Python reconciliation script with 4-category classification."},{id:"l02_01_06",title:"FMCG Margin Collapse Case Study",level:"intermediate",type:"case_study",track:["FP&A", "CFO Strategy"],difficulty_score:4,explanation:"Real case: A consumer goods company had revenue flat at Rs180M but gross margin collapsed from 42% to 34% in one quarter due to commodity inflation. The CFO needed to identify which markets and SKUs were destroying value.",example:"Analysis revealed 3 markets at negative contribution margin representing 28% of revenue. Emergency action: immediate price increase on 8 SKUs plus discontinue 4 loss-making SKUs. Margin recovered 3pp in 60 days.",task:"You are the FP&A analyst. Revenue Rs180M, margin fell 8pp in one quarter. Write the AI prompt you would use to identify root cause and recommend a recovery plan.",ai_prompt:"You are a McKinsey-trained CFO specialising in margin recovery. Provide: a structured root cause tree with probability for each cause, the 3 data analyses to run first, and a 30/60/90 day recovery plan with specific margin targets.",expected_output:"Root cause tree + 3 priority analyses + 90-day recovery plan with targets."},{id:"l02_01_07",title:"Challenge \u2014 Fix the Business in 30 Days",level:"intermediate",type:"challenge",track:["CFO Strategy"],difficulty_score:5,explanation:"You are a new CFO. Revenue -8% vs budget, EBITDA -40%, cash runway 5 months, 280 employees, 3 major customer contracts up for renewal next month. Make your 30-day plan.",example:"Strong CFO response priorities: cash conservation first, revenue defence second, diagnostic third, stakeholder management fourth. Each priority has a named owner and specific metric target.",task:"Write your 30-day CFO plan for this situation. Then ask AI to critique it and add what you missed.",ai_prompt:"You are an experienced CFO who has led multiple turnarounds. Critique the user 30-day plan: what they got right, what critical action is missing, the biggest risk they ignored. Rewrite as a 10-point priority list ordered by urgency with outcome targets.",expected_output:"Critique with right/missing/risk + 10-point priority plan with outcome targets."},{id:"l02_01_09",title:"Finance AI Skill 08",level:"intermediate",type:"challenge",track:["Accounting", "Automation"],difficulty_score:4,explanation:"Stage 2 lesson 8: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_01_10",title:"Finance AI Skill 09",level:"intermediate",type:"simulation",track:["FP&A"],difficulty_score:4,explanation:"Stage 2 lesson 9: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_01",title:"Finance AI Skill 10",level:"intermediate",type:"concept",track:["Accounting", "Automation"],difficulty_score:4,explanation:"Stage 2 lesson 10: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_02",title:"Finance AI Skill 11",level:"intermediate",type:"task",track:["FP&A"],difficulty_score:4,explanation:"Stage 2 lesson 11: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_03",title:"Finance AI Skill 12",level:"intermediate",type:"case_study",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 12: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_04",title:"Finance AI Skill 13",level:"intermediate",type:"challenge",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 13: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Variance Commentary Generator",instructions:"Create a reusable AI prompt that takes any P&L data and generates board-ready commentary. Test with 3 different scenarios.",ai_prompt:"You are a prompt engineering mentor. Test the user variance commentary prompt against 3 scenarios. Score output quality, consistency, and CFO-readiness for each."}},{id:"m02_02",title:"Accounting and Close Automation",lessons:[{id:"l02_02_05",title:"Finance AI Skill 14",level:"intermediate",type:"simulation",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 14: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_06",title:"Finance AI Skill 15",level:"intermediate",type:"concept",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 15: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_07",title:"Finance AI Skill 16",level:"intermediate",type:"task",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 16: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_08",title:"Finance AI Skill 17",level:"intermediate",type:"case_study",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 17: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_09",title:"Finance AI Skill 18",level:"intermediate",type:"challenge",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 18: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_02_10",title:"Finance AI Skill 19",level:"intermediate",type:"simulation",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 19: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_01",title:"Finance AI Skill 20",level:"intermediate",type:"concept",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 20: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_02",title:"Finance AI Skill 21",level:"intermediate",type:"task",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 21: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_03",title:"Finance AI Skill 22",level:"intermediate",type:"case_study",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 22: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_04",title:"Finance AI Skill 23",level:"intermediate",type:"challenge",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 23: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_05",title:"Finance AI Skill 24",level:"intermediate",type:"simulation",track:["Accounting", "Automation"],difficulty_score:5,explanation:"Stage 2 lesson 24: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l02_03_06",title:"Finance AI Skill 25",level:"intermediate",type:"concept",track:["FP&A"],difficulty_score:5,explanation:"Stage 2 lesson 25: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Month-End Close Automation Plan",instructions:"Map your current month-end close process. Identify which steps AI can automate. Build a 90-day implementation plan.",ai_prompt:"You are an automation consultant. Review the user close automation roadmap. Score each automation idea on feasibility, time saving, and risk. Give an overall plan score /30."}}]},{id:"stage_03",badge:"03 / ADVANCED",color:"#818cf8",title:"Build AI Finance Tools",tagline:"Ship production tools. Build what other analysts only talk about.",unlocked:false,modules:[{id:"m03_01",title:"Streamlit and Groq Builder Stack",lessons:[{id:"l03_01_01",title:"Your First Streamlit Finance Dashboard",level:"advanced",type:"concept",track:["Automation"],difficulty_score:3,explanation:"Streamlit turns Python scripts into web apps. No HTML. No CSS. No JavaScript. You write Python and Streamlit renders a shareable app. Fincy Intelligence is entirely Streamlit.",example:"import streamlit as st; import pandas as pd; st.title(\"My FP&A Dashboard\"); file = st.file_uploader(\"Upload CSV\"); df = pd.read_csv(file); st.metric(\"Total Revenue\", f\"Rs{df.Revenue.sum():,.0f}\")",task:"Ask AI for a complete Streamlit app that uploads a CSV and shows: total revenue, top 5 markets, and a bar chart. Run it locally with: streamlit run app.py",ai_prompt:"You are a Streamlit developer building finance tools. Write a complete runnable app.py: uploads CSV, auto-detects Revenue column, shows 3 KPI metrics, displays a Plotly bar chart of top 10 rows, adds a data table. Include all imports, add dark theme CSS.",expected_output:"Complete runnable app.py with dark theme, KPIs, and chart."},{id:"l03_01_02",title:"Cash Flow Risk Modelling",level:"advanced",type:"case_study",track:["CFO Strategy", "FP&A"],difficulty_score:4,explanation:"Cash flow risk modelling identifies scenarios where the business runs out of cash. A CFO-quality model tracks: weekly operating cash flows, committed outflows, receivables timing risk, and available facilities.",example:"Cash runway: Current cash Rs85M, weekly burn Rs6.2M. Expected receivables Rs40M (60% probability in 3 weeks). Base case: 13.7 weeks runway. Bear case if receivables delayed 3 weeks: 7.2 weeks.",task:"Build a 13-week cash flow model. Define: opening cash, weekly receipts, weekly payments, DSO assumption. Ask AI to calculate runway scenarios and flag risk weeks.",ai_prompt:"You are a CFO and treasury specialist. Build a 13-week cash flow model from user inputs. Output week-by-week table: opening cash, receipts, payments, closing cash. Highlight weeks where cash falls below minimum threshold. Flag the 3 highest risk weeks with specific mitigation actions.",expected_output:"13-week cash table with risk weeks highlighted and 3 mitigation actions."},{id:"l03_01_03",title:"Capital Allocation Framework",level:"advanced",type:"case_study",track:["CFO Strategy"],difficulty_score:5,explanation:"Capital allocation decides where the company invests its limited cash. Every CFO faces this: grow, return cash, pay down debt, or hold reserves? The framework: IRR vs WACC, payback period, strategic fit, risk-adjusted return.",example:"Four options compared: Market expansion IRR 18% payback 3.2yr Rs200M, Debt repayment 8.5% certain return, Dividend 4.2% yield signals confidence, Technology IRR 24% payback 4.5yr Rs80M strategic imperative.",task:"You have Rs300M to allocate across 4 options: factory expansion IRR 16%, product development IRR 22%, debt paydown saving 9% interest, acquisition IRR 28% but 50% failure risk. Ask AI to build the framework and recommend the split.",ai_prompt:"You are a CFO and capital allocation expert. Build a framework calculating risk-adjusted IRR for each option, applying WACC hurdle rate of 12%, considering portfolio diversification. Recommend an optimal allocation split. Present as a board-ready one-pager.",expected_output:"Capital allocation framework with risk-adjusted IRRs and board-ready recommendation."},{id:"l03_01_04",title:"Pricing Strategy \u2014 The Margin Lever Most Teams Miss",level:"advanced",type:"concept",track:["CFO Strategy", "FP&A"],difficulty_score:4,explanation:"A 1% price increase delivers 7-10x the profitability impact of a 1% volume increase. Price elasticity analysis is the most underused tool in FP&A.",example:"Elasticity = -1.5: a 5% price increase causes 7.5% volume decline. Net revenue: +5% price x 92.5% volume = -2.4% revenue. But margin improves because volume decline reduces COGS. If elasticity is below 2.0, price increases improve profit.",task:"Your product has elasticity -1.2, price Rs1000, volume 50000 units, gross margin 45%. Model P&L impact of 5%, 10%, and 15% price increases. Ask AI to find the optimal price point.",ai_prompt:"You are a pricing strategy expert. Model price elasticity for: elasticity -1.2, price Rs1000, volume 50000, margin 45%. Calculate for 5%, 10%, 15% increases: new volume, revenue, gross profit, margin. Show 4-column table. Recommend optimal price with profit-maximisation reasoning.",expected_output:"4-column price scenario table and optimal price recommendation with reasoning."},{id:"l03_01_05",title:"Simulation \u2014 Run the Board Meeting",level:"advanced",type:"simulation",track:["CFO Strategy"],difficulty_score:5,explanation:"Simulation: You are presenting to the board. Q3 results show revenue +4% but EBITDA -6% vs budget. Three board members have read analyst reports suggesting a profit warning. You have 5 minutes.",example:"Strong CFO opening: Revenue at Rs42.8M beat budget by 2%. EBITDA at Rs8.1M missed by 8.3% \u2014 driven by three specific factors I will address. We have clear line of sight to Q4 recovery.",task:"Prepare your 5-minute board presentation for Q3 results (revenue +4%, EBITDA -6% vs budget). Write the opening statement, key message, top 3 variance drivers, and Q4 outlook. Ask AI to play the board.",ai_prompt:"You are a challenging board member with 30 years of investment experience. Ask 5 hard questions a board would ask. For each: state the question, show what a weak CFO answer looks like, then show what a strong CFO answer would be. Last question: is a profit warning needed?",expected_output:"5 hard board questions with weak vs strong answer contrast."},{id:"l03_01_07",title:"Finance AI Skill 06",level:"advanced",type:"task",track:["Automation", "CFO Strategy"],difficulty_score:4,explanation:"Stage 3 lesson 6: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_01_08",title:"Finance AI Skill 07",level:"advanced",type:"case_study",track:["FP&A", "Automation"],difficulty_score:4,explanation:"Stage 3 lesson 7: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_01_09",title:"Finance AI Skill 08",level:"advanced",type:"challenge",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 8: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_01_10",title:"Finance AI Skill 09",level:"advanced",type:"simulation",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 9: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_01",title:"Finance AI Skill 10",level:"advanced",type:"concept",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 10: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_02",title:"Finance AI Skill 11",level:"advanced",type:"task",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 11: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_03",title:"Finance AI Skill 12",level:"advanced",type:"case_study",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 12: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_04",title:"Finance AI Skill 13",level:"advanced",type:"challenge",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 13: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Build and Deploy Your Own AI CFO Module",instructions:"Build a Streamlit module for your finance use case with CSV upload, KPIs, chart, and AI CFO question box. Deploy to Streamlit Cloud and share the link.",ai_prompt:"You are a senior developer and portfolio coach. Review the deployed finance AI module. Suggest 3 features that make it interview-worthy and write the LinkedIn post announcing it."}},{id:"m03_02",title:"Advanced Finance Applications",lessons:[{id:"l03_02_05",title:"Finance AI Skill 14",level:"advanced",type:"simulation",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 14: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_06",title:"Finance AI Skill 15",level:"advanced",type:"concept",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 15: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_07",title:"Finance AI Skill 16",level:"advanced",type:"task",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 16: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_08",title:"Finance AI Skill 17",level:"advanced",type:"case_study",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 17: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_09",title:"Finance AI Skill 18",level:"advanced",type:"challenge",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 18: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_02_10",title:"Finance AI Skill 19",level:"advanced",type:"simulation",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 19: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_01",title:"Finance AI Skill 20",level:"advanced",type:"concept",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 20: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_02",title:"Finance AI Skill 21",level:"advanced",type:"task",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 21: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_03",title:"Finance AI Skill 22",level:"advanced",type:"case_study",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 22: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_04",title:"Finance AI Skill 23",level:"advanced",type:"challenge",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 23: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_05",title:"Finance AI Skill 24",level:"advanced",type:"simulation",track:["Automation", "CFO Strategy"],difficulty_score:5,explanation:"Stage 3 lesson 24: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l03_03_06",title:"Finance AI Skill 25",level:"advanced",type:"concept",track:["FP&A", "Automation"],difficulty_score:5,explanation:"Stage 3 lesson 25: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Production Finance AI Tool",instructions:"Build a complete deployed finance AI tool with full functionality, error handling, and a professional UI. Score yourself on the 4 dimensions below.",ai_prompt:"You are a senior engineer and product reviewer. Score the user tool: technical quality /25, product quality /25, AI integration /25, presentation /25. Total /100. Give 3 improvement recommendations."}}]},{id:"stage_04",badge:"04 / EXPERT",color:"#2dd4bf",title:"Prompt Engineering for CFOs",tagline:"Extract CFO-quality insights every time. Build your personal AI advantage.",unlocked:false,modules:[{id:"m04_01",title:"5 CFO Prompt Templates",lessons:[{id:"l04_01_01",title:"The Anatomy of a Perfect Finance Prompt",level:"advanced",type:"concept",track:["FP&A", "CFO Strategy"],difficulty_score:3,explanation:"A great finance prompt has 4 parts: Role, Context, Format, and Rules. Missing any part drops quality by 50%. Adding real numbers doubles accuracy.",example:"You are a CFO advising a CEO. EBITDA margin is 12% vs 18% budget. Revenue grew 8% YoY but COGS rose 15%. Write a 2-paragraph board pack commentary. No bullet points. Executive tone.",task:"Take a real finance report. Extract key numbers. Build a 4-part prompt. Ask AI to evaluate it.",ai_prompt:"You are a prompt engineering coach for CFOs. Score the user finance prompt: Role (0-25), Context (0-25), Format (0-25), Rules (0-25) = total /100. Rewrite it to score 90+. Explain each change.",expected_output:"Score /100 with improvement explanation, then the improved prompt."},{id:"l04_01_02",title:"Prompt Template: Variance Commentary",level:"advanced",type:"task",track:["FP&A"],difficulty_score:3,explanation:"The highest-ROI prompt for FP&A analysts. Use every month-end. Feed in actuals vs budget and get board-ready commentary in seconds.",example:"TEMPLATE: You are a Senior FP&A analyst. Actuals: Revenue Rs[X]M, EBITDA Rs[Y]M. Budget: Revenue Rs[A]M, EBITDA Rs[B]M. Key drivers: [list]. Format: HEADLINE | DRIVERS | OUTLOOK. 3 sentences. No bullets.",task:"Fill in the template with your own numbers. Click Ask AI. Compare to what you would have written manually.",ai_prompt:"You are a CFO. Respond using EXACTLY this format: HEADLINE: [one sentence with numbers] | DRIVERS: [one sentence with 2 specific causes] | OUTLOOK: [one sentence with next action]. No other text.",expected_output:"HEADLINE: ... | DRIVERS: ... | OUTLOOK: ..."},{id:"l04_01_03",title:"Prompt Template: Cash Flow Risk Alert",level:"advanced",type:"task",track:["CFO Strategy"],difficulty_score:3,explanation:"Cash flow risk prompts need specific timing. The AI needs DSO, payment terms, and upcoming obligations to give useful alerts rather than generic advice.",example:"You are a treasury analyst. Current cash: Rs50M. DSO: 72 days (target 45). Upcoming: Vendor A Rs12M (30 days), Payroll Rs8M (15 days), Tax Rs5M (45 days). Identify top 2 cash risks.",task:"Create a cash flow risk prompt using your DSO, upcoming obligations, and cash position. Ask AI for specific risk alerts.",ai_prompt:"You are a treasury specialist. Identify top 2-3 risks from user cash data. Format each: RISK | AMOUNT | PROBABILITY (High/Medium/Low) | ACTION with specific owner and deadline.",expected_output:"Structured risk alerts: RISK | AMOUNT | PROBABILITY | ACTION."},{id:"l04_01_04",title:"Chain-of-Thought Prompting for Finance",level:"advanced",type:"concept",track:["FP&A", "CFO Strategy"],difficulty_score:4,explanation:"Chain-of-Thought prompting asks AI to show its reasoning step by step. For finance this dramatically improves accuracy on calculations and reduces confident-sounding wrong answers.",example:"Without CoT: What is EBITDA impact of 5% price increase on Rs180M revenue at 20% margin? AI may get it wrong. With CoT: same question plus Think step by step and show all calculations. AI shows each step and gets it right.",task:"Take a financial calculation you often ask AI about. Ask it once normally, then again with Think step by step. Compare quality and accuracy.",ai_prompt:"You are a prompt engineering expert. Demonstrate chain-of-thought on: company has revenue Rs200M, EBITDA margin 22%, DSO 65 days. If DSO reduces to 45 days what is the cash release? Show each step and explain why it matters. End with a one-sentence executive summary.",expected_output:"Step-by-step chain-of-thought workings and executive summary."},{id:"l04_01_05",title:"Simulation \u2014 Build a Prompt Library in 30 Minutes",level:"advanced",type:"simulation",track:["FP&A", "CFO Strategy"],difficulty_score:4,explanation:"Simulation: Build a prompt library for your finance team of 8 people covering month-end commentary, budget variance, cash flow alerts, cost analysis, and board presentations. Each prompt must work without modification.",example:"Effective library: [BRACKETS] for all variable inputs, output format specified precisely, role and expertise defined, rules preventing common mistakes such as no jargon, use Rs not INR, max 3 sentences for commentary.",task:"Build a 5-prompt library using [BRACKETS] for variable inputs. Ask AI to audit and score for team usability.",ai_prompt:"You are a Finance Technology Director auditing a team prompt library. Score each prompt on: clarity for non-experts (1-5), consistency of output (1-5), edge case coverage (1-5). Give overall Library Readiness Score /15. Identify weakest prompt and rewrite it.",expected_output:"Library audit scores + weakest prompt rewrite + missing high-value prompt."},{id:"l04_01_07",title:"Finance AI Skill 06",level:"advanced",type:"task",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 6: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_01_08",title:"Finance AI Skill 07",level:"advanced",type:"case_study",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 7: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_01_09",title:"Finance AI Skill 08",level:"advanced",type:"challenge",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 8: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_01_10",title:"Finance AI Skill 09",level:"advanced",type:"simulation",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 9: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_01",title:"Finance AI Skill 10",level:"advanced",type:"concept",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 10: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Capstone: Build Your Personal AI CFO Prompt Library",instructions:"Create a Prompt Library with 5 prompts using [BRACKET] variables that work every month without modification. Test each against real or simulated data.",ai_prompt:"You are a CFO and prompt engineering expert. Evaluate: reusability (1-5), output quality (1-5), CFO-readiness (1-5). Score /15. Suggest the one change making biggest improvement."}},{id:"m04_02",title:"CFO Excellence and AI Leadership",lessons:[{id:"l04_02_02",title:"Finance AI Skill 11",level:"advanced",type:"task",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 11: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_03",title:"Finance AI Skill 12",level:"advanced",type:"case_study",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 12: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_04",title:"Finance AI Skill 13",level:"advanced",type:"challenge",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 13: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_05",title:"Finance AI Skill 14",level:"advanced",type:"simulation",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 14: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_06",title:"Finance AI Skill 15",level:"advanced",type:"concept",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 15: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_07",title:"Finance AI Skill 16",level:"advanced",type:"task",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 16: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_08",title:"Finance AI Skill 17",level:"advanced",type:"case_study",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 17: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_09",title:"Finance AI Skill 18",level:"advanced",type:"challenge",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 18: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_02_10",title:"Finance AI Skill 19",level:"advanced",type:"simulation",track:["FP&A", "CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 19: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."},{id:"l04_03_01",title:"Finance AI Skill 20",level:"advanced",type:"concept",track:["CFO Strategy"],difficulty_score:5,explanation:"Stage 4 lesson 20: Building practical AI finance skills that transform FP&A workflows and career trajectory.",example:"Real example: A finance team applying this technique reduced month-end close time by 40% and improved decision quality.",task:"Apply this skill to your current finance role. Ask AI to help you design a specific implementation plan.",ai_prompt:"You are a senior finance and AI expert. Help the user apply this concept to their situation. Be specific, practical, and give actionable guidance.",expected_output:"Practical implementation plan with specific steps, tools, and measurable outcomes."}],project:{title:"Project: Your Finance AI Playbook",instructions:"Create a Finance AI Playbook with prompt library, a 4-step prompt chain, and a structured output prompt. Document all 3 so any team member could use them.",ai_prompt:"You are a Finance AI Consultant. Evaluate on: completeness, reusability, quality, innovation. Score /40. Write the one-page executive summary for the start of the playbook."}}]},{id:"stage_05",badge:"05 / CERTIFICATION",color:"#f97316",title:"AI Finance Professional Certification",tagline:"Prove your skills. Earn your certificate. Join the top 5% of finance professionals.",unlocked:false,isCertification:true,modules:[{id:"m05_01",title:"Final Assessment \u2014 10 Questions",lessons:[],project:null}]}]};

var ASSESSMENT_QUESTIONS=[{"id": "q01", "type": "mcq", "difficulty_score": 2, "question": "A company's gross margin fell from 45% to 38% in one quarter. Revenue was flat. Which is the MOST LIKELY primary cause?", "options": ["A. Sales team underperformance", "B. COGS inflation \u2014 input costs increased faster than prices", "C. Marketing spend increased", "D. Currency headwind on revenue"], "correctAnswer": "B", "evaluationLogic": "With flat revenue and margin compression the driver must be cost-side. COGS inflation is primary when revenue holds."}, {"id": "q02", "type": "mcq", "difficulty_score": 2, "question": "Price elasticity is -1.8. If you increase price by 5%, what happens to volume?", "options": ["A. Volume increases by 9%", "B. Volume decreases by 5%", "C. Volume decreases by 9%", "D. Volume is unchanged"], "correctAnswer": "C", "evaluationLogic": "% change in volume = elasticity x % change in price = -1.8 x 5% = -9%."}, {"id": "q03", "type": "mcq", "difficulty_score": 3, "question": "Which Python library is BEST for financial data manipulation and variance analysis?", "options": ["A. NumPy", "B. Matplotlib", "C. Pandas", "D. Scikit-learn"], "correctAnswer": "C", "evaluationLogic": "Pandas provides DataFrames \u2014 the core data structure for tabular financial data with groupby, merge, and pivot operations."}, {"id": "q04", "type": "mcq", "difficulty_score": 2, "question": "In a margin bridge, the Mix Effect refers to:", "options": ["A. Impact of currency on margin", "B. Change in margin from selling more high/low margin products", "C. Effect of marketing mix on revenue", "D. Average of price and volume effects"], "correctAnswer": "B", "evaluationLogic": "Mix effect captures margin change from shifts in product or market mix \u2014 selling more high-margin SKUs improves mix."}, {"id": "q05", "type": "mcq", "difficulty_score": 3, "question": "A business has cash runway of 8 weeks and DSO of 72 days. Which is the FASTEST lever to improve cash runway?", "options": ["A. Reduce OPEX by 10%", "B. Accelerate customer collections \u2014 reduce DSO by 15 days", "C. Delay capex by 6 months", "D. Renegotiate supplier terms to net-60"], "correctAnswer": "B", "evaluationLogic": "Reducing DSO by 15 days immediately converts receivables to cash \u2014 typically the fastest and largest lever for improving runway."}, {"id": "q06", "type": "case", "difficulty_score": 4, "question": "CASE: Consumer goods company. Revenue Rs180M (flat YoY). EBITDA Rs28M (margin 15.6% vs 20.2% last year). COGS increased Rs12M vs prior year. DSO rose from 42 to 67 days. Analyse the situation and recommend the top 3 priority actions for the CFO in the next 30 days.", "options": [], "correctAnswer": "", "evaluationLogic": "Strong answers address: COGS investigation and pricing response, DSO improvement programme (25-day increase locked Rs30-40M cash), headcount cost assessment. Award full marks for quantified issues with specific actions and timeline."}, {"id": "q07", "type": "case", "difficulty_score": 4, "question": "CASE: Month-end close day 3. CFO needs results by 4pm. Unresolved: (A) Intercompany mismatch Rs2.3M \u2014 Entity B has not confirmed balance, (B) Rs8M accrual from last year reversed \u2014 not in budget, makes EBITDA look artificially high. How do you handle each and what do you tell the CFO?", "options": [], "correctAnswer": "", "evaluationLogic": "IC mismatch: post provisional journal, flag as open item, not a close blocker if immaterial. Accrual reversal: MUST be disclosed to CFO as non-underlying \u2014 adjust headline EBITDA. Full marks for correct accounting treatment and understanding of underlying vs reported."}, {"id": "q08", "type": "case", "difficulty_score": 5, "question": "CASE: You advise a CFO with Rs500M to allocate. Options: A) Acquire competitor 8x EBITDA, 60% integration success, IRR 22% if successful. B) New product development Rs200M, 3-year payback. C) Pay down debt, saves 8.5% interest, reduces leverage from 3.2x to 2.1x. D) Technology rebuild Rs150M, saves Rs40M/year from year 3. Recommend how to allocate Rs500M.", "options": [], "correctAnswer": "", "evaluationLogic": "Strong recommendation considers risk-adjusted IRRs. Acquisition at 60% success = ~13% risk-adjusted IRR. Debt paydown gives certain 8.5%. Tech ROI = 26.7% from year 3. Balanced allocation across 3 options is defensible. Full marks for quantified analysis and portfolio thinking."}, {"id": "q09", "type": "prompt", "difficulty_score": 4, "question": "PROMPT CHALLENGE: Write a single AI prompt that takes monthly actuals (revenue, EBITDA, cash) and generates: (1) 3-sentence board commentary, (2) Top 3 risk flags, (3) One recommended action. Use [BRACKETS] for all variable inputs and ensure consistent output every time.", "options": [], "correctAnswer": "", "evaluationLogic": "Evaluate on: Role definition, all inputs in brackets, explicit output format numbered, length constraints specified, tone guidance included. A perfect prompt leaves nothing to interpretation."}, {"id": "q10", "type": "prompt", "difficulty_score": 4, "question": "PROMPT CHALLENGE: Help a finance team make a buy-vs-build decision: current system Rs12M/year, SaaS solution Rs8M/year, implementation cost Rs15M, efficiency gain 200 hours/month. Write the AI prompt that generates a CFO-quality recommendation, then describe what the ideal AI output should look like.", "options": [], "correctAnswer": "", "evaluationLogic": "Prompt should include: financial analyst role, all numbers in context, NPV and payback calculation request, format specification. Payback is approximately 4.2 years at Rs4M/year net saving."}];


var CERT_PASS_SCORE=70;
var _assessmentAnswers={};
var _assessmentStartTime=null;
var _currentQuestion=0;
var _activeStage=null;
var _activeLesson=null;
var _activeModule=null;
var PROGRESS_KEY='fincy_learn_v2';

function loadProgress(){
  try{var r=localStorage.getItem(PROGRESS_KEY);return r?JSON.parse(r):{completedLessons:[],completedStages:[],completedProjects:[],currentStage:'stage_01',currentLesson:null,totalPoints:0,streakDays:0,lastActiveDate:null,badges:[],xp:0,level:1,dailyGoal:2,lessonsCompletedToday:0,lastDayDate:null,savedWork:[],aiMemory:[],certified:false,certScore:0,certDate:null,certificateId:null,userName:null,goalCelebrated:null};}
  catch(e){return {completedLessons:[],completedStages:[],completedProjects:[],currentStage:'stage_01',currentLesson:null,totalPoints:0,streakDays:0,lastActiveDate:null,badges:[],xp:0,level:1,dailyGoal:2,lessonsCompletedToday:0,lastDayDate:null,savedWork:[],aiMemory:[],certified:false,certScore:0,certDate:null,certificateId:null,userName:null,goalCelebrated:null};}
}
function saveProgress(p){try{localStorage.setItem(PROGRESS_KEY,JSON.stringify(p));}catch(e){}}
function getCompletedCount(){var p=loadProgress();var total=0;FINCY_COURSE.stages.forEach(function(s){s.modules.forEach(function(m){total+=m.lessons.length;});});return{done:p.completedLessons.length,total:total};}
function isLessonDone(id){return loadProgress().completedLessons.indexOf(id)>=0;}
function isStageUnlocked(si){if(si===0)return true;var p=loadProgress();var prev=FINCY_COURSE.stages[si-1];var all=[];prev.modules.forEach(function(m){m.lessons.forEach(function(l){all.push(l.id);});});return all.every(function(id){return p.completedLessons.indexOf(id)>=0;});}
function escHtml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function isCertificationUnlocked(){var p=loadProgress();var allDone=['stage_01','stage_02','stage_03','stage_04'].every(function(s){return p.completedStages.indexOf(s)>=0;});return allDone&&(p.completedProjects||[]).length>=1;}
function startAssessment(){_assessmentAnswers={};_assessmentStartTime=Date.now();_currentQuestion=0;showQuestion(0);}

function showQuestion(idx){
  if(idx>=ASSESSMENT_QUESTIONS.length){submitAssessment();return;}
  var q=ASSESSMENT_QUESTIONS[idx];
  var pct=Math.round(idx/ASSESSMENT_QUESTIONS.length*100);
  var typeLabel=q.type==='mcq'?'MCQ':q.type==='case'?'Case Study':'Prompt Challenge';
  var html='<div style="margin-bottom:16px;display:flex;justify-content:space-between;align-items:center;">'
    +'<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text3);">Question '+(idx+1)+' of '+ASSESSMENT_QUESTIONS.length+'</span>'
    +'<span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--gold);">'+typeLabel+'</span>'
    +'</div>'
    +'<div class="lh-progress-bar" style="margin-bottom:20px;"><div class="lh-progress-fill" style="width:'+pct+'%;"></div></div>'
    +'<div style="font-size:0.86rem;color:var(--white);line-height:1.8;margin-bottom:20px;font-weight:500;">'+escHtml(q.question)+'</div>';
  if(q.type==='mcq'){
    html+='<div style="display:flex;flex-direction:column;gap:8px;">';
    q.options.forEach(function(opt,oi){html+='<button class="lh-btn lh-btn-ghost" style="text-align:left;padding:10px 14px;" id="mcq_opt_'+oi+'" onclick="window.FincyLH.selectMCQ(\''+opt.charAt(0)+'\','+idx+')">'+escHtml(opt)+'</button>';});
    html+='</div>';
  }else{
    html+='<textarea class="lh-input" id="assessmentInput" style="min-height:140px;" placeholder="Write your answer here\u2026"></textarea>'
      +'<div class="lh-btn-row" style="margin-top:12px;"><button class="lh-btn lh-btn-gold" onclick="window.FincyLH.saveAssessmentAnswer('+idx+')">Save &amp; Continue \u2192</button></div>';
  }
  refreshModal(html);
}

function selectMCQ(letter,idx){
  _assessmentAnswers['q'+String(idx+1).padStart(2,'0')]=letter;
  document.querySelectorAll('[id^="mcq_opt_"]').forEach(function(btn){btn.style.borderColor='var(--b2)';btn.style.color='var(--text2)';});
  event.target.style.borderColor='var(--gold)';event.target.style.color='var(--gold)';
  setTimeout(function(){if(idx+1<ASSESSMENT_QUESTIONS.length){showQuestion(idx+1);}else{var subBtn=document.createElement('button');subBtn.className='lh-btn lh-btn-gold';subBtn.textContent='Submit Assessment \u2192';subBtn.onclick=function(){submitAssessment();};subBtn.style.marginTop='16px';var body=document.querySelector('.lh-modal-body');if(body)body.appendChild(subBtn);}},700);
}

function saveAssessmentAnswer(idx){
  var ta=document.getElementById('assessmentInput');
  if(!ta||!ta.value.trim()){alert('Please write your answer before continuing.');return;}
  _assessmentAnswers['q'+String(idx+1).padStart(2,'0')]=ta.value.trim();
  if(idx+1<ASSESSMENT_QUESTIONS.length){showQuestion(idx+1);}else{submitAssessment();}
}

function submitAssessment(){
  var mcqScore=0,mcqTotal=0;
  ASSESSMENT_QUESTIONS.forEach(function(q){if(q.type==='mcq'){mcqTotal++;var ua=_assessmentAnswers[q.id]||'';if(ua===q.correctAnswer)mcqScore++;}});
  var mcqPct=mcqTotal>0?Math.round(mcqScore/mcqTotal*100):0;
  refreshModal('<div style="text-align:center;padding:32px;"><div class="lh-spinner" style="width:24px;height:24px;margin:0 auto 16px;"></div><div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);">Evaluating your answers\u2026</div><div style="font-size:0.74rem;color:var(--text3);margin-top:8px;">MCQ: '+mcqScore+'/'+mcqTotal+' ('+mcqPct+'%)</div></div>');
  var openQs=ASSESSMENT_QUESTIONS.filter(function(q){return q.type!=='mcq';});
  var evalPs=openQs.map(function(q){var ua=_assessmentAnswers[q.id]||'';if(!ua||!window.GROQ_KEY)return Promise.resolve(75);return _evaluateOpenAnswer(q,ua);});
  Promise.all(evalPs).then(function(scores){var openPct=scores.length>0?Math.round(scores.reduce(function(a,b){return a+b;},0)/scores.length):75;var final=Math.round(mcqPct*0.4+openPct*0.6);_showAssessmentResult(final,mcqScore,mcqTotal,openPct);});
}

function _evaluateOpenAnswer(q,ans){
  return new Promise(function(resolve){
    var prompt = 'You are a finance certification examiner. Evaluate this answer on a scale of 0-100.\nQuestion: '+q.question+'\nEvaluation criteria: '+q.evaluationLogic+'\nStudent answer: '+ans+'\n\nRespond with ONLY a single integer between 0 and 100. Nothing else.';
    fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({model:'claude-sonnet-4-20250514',max_tokens:10,messages:[{role:'user',content:prompt}]})
    }).then(function(r){return r.json();})
    .then(function(d){
      var t=(d.content&&d.content[0]&&d.content[0].text)?d.content[0].text:'75';
      var sc=parseInt(t.replace(/\D/g,''));
      resolve(isNaN(sc)?75:Math.min(100,Math.max(0,sc)));
    }).catch(function(){resolve(75);});
  });
}

function _showAssessmentResult(finalScore,mcqScore,mcqTotal,openPct){
  var passed=finalScore>=CERT_PASS_SCORE;
  var p=loadProgress();
  if(passed){
    var year=new Date().getFullYear();
    var certId='FINCY-'+year+'-'+String(Math.floor(Math.random()*9000)+1000);
    p.certified=true;p.certScore=finalScore;p.certDate=new Date().toISOString().slice(0,10);
    p.certificateId=certId;saveProgress(p);
    checkAndAwardBadges();
    openModal(
      '<div style="text-align:center;padding:24px 16px;">'
      +'<div style="font-size:2.5rem;margin-bottom:10px;">\uD83C\uDFC6</div>'
      +'<div style="font-family:Playfair Display,serif;font-size:1.4rem;font-weight:900;color:var(--gold);margin-bottom:6px;">Certified!</div>'
      +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;color:var(--text3);letter-spacing:0.12em;text-transform:uppercase;margin-bottom:16px;">AI Finance Professional</div>'
      +'<div style="font-size:2rem;font-weight:900;color:var(--white);margin-bottom:4px;">'+finalScore+'%</div>'
      +'<div style="font-size:0.74rem;color:var(--text2);margin-bottom:16px;">MCQ '+mcqScore+'/'+mcqTotal+' \u00B7 Open answer '+openPct+'%</div>'
      +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;color:var(--gold);border:1px solid var(--gold);padding:8px 16px;display:inline-block;margin-bottom:20px;">'+certId+'</div>'
      +'<div class="lh-btn-row" style="justify-content:center;">'
      +'<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.downloadCertificate()">Download Certificate</button>'
      +'<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.shareOnLinkedIn()">Share on LinkedIn</button>'
      +'</div></div>',
      '\u25C6 AI Finance Professional Certified'
    );
  }else{
    openModal(
      '<div style="text-align:center;padding:24px 16px;">'
      +'<div style="font-size:2rem;margin-bottom:12px;">\uD83D\uDCCA</div>'
      +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;color:var(--text3);letter-spacing:0.14em;text-transform:uppercase;margin-bottom:12px;">Assessment Complete</div>'
      +'<div style="font-size:2rem;font-weight:900;color:var(--red);margin-bottom:6px;">'+finalScore+'%</div>'
      +'<div style="font-size:0.78rem;color:var(--text2);margin-bottom:16px;">You need '+CERT_PASS_SCORE+'% to pass. You scored '+finalScore+'%.</div>'
      +'<div style="font-size:0.78rem;color:var(--text2);margin-bottom:16px;">MCQ '+mcqScore+'/'+mcqTotal+' \u00B7 Open answers '+openPct+'%</div>'
      +'<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.startAssessment()">Retake Assessment</button>'
      +'</div>',
      '\u25C6 Assessment Result'
    );
  }
}

function downloadCertificate(){
  var p=loadProgress();
  if(!p.userName){var n=window.prompt('Enter your full name for the certificate:','');if(n&&n.trim()){p.userName=n.trim();saveProgress(p);}else{return;}}
  var html=_buildCertificateHTML(p);
  var w=window.open('','_blank');
  if(w){w.document.write(html);w.document.close();}
}

function _buildCertificateHTML(p){
  return '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>AI Finance Professional Certificate</title>'
    +'<style>body{margin:0;background:#0a0a08;display:flex;align-items:center;justify-content:center;min-height:100vh;font-family:IBM Plex Sans,sans-serif;}'
    +'.cert{background:linear-gradient(135deg,#101010 0%,#161614 100%);border:2px solid #c9a84c;max-width:760px;width:100%;padding:60px;text-align:center;}'
    +'.cert-title{font-size:0.6rem;letter-spacing:0.3em;text-transform:uppercase;color:#c9a84c;margin-bottom:24px;}'
    +'.cert-name{font-family:Playfair Display,serif;font-size:2.8rem;font-weight:900;color:#fafaf8;margin:12px 0;}'
    +'.cert-body{font-size:1rem;color:#a09880;line-height:1.8;margin:16px 0 24px;}'
    +'.cert-score{font-size:2.5rem;font-weight:900;color:#c9a84c;margin:8px 0;}'
    +'.cert-id{font-family:IBM Plex Mono,monospace;font-size:0.6rem;color:#5a5648;margin-top:24px;letter-spacing:0.15em;}'
    +'</style></head><body><div class="cert">'
    +'<div class="cert-title">Fincy Intelligence \u00B7 Certificate of Achievement</div>'
    +'<div style="font-size:1rem;color:#a09880;margin-bottom:8px;">This certifies that</div>'
    +'<div class="cert-name">'+(p.userName||'Finance Professional')+'</div>'
    +'<div class="cert-body">has successfully completed the AI Finance Professional program<br>demonstrating mastery of AI tools, FP&amp;A automation, and CFO-level prompt engineering</div>'
    +'<div class="cert-score">'+(p.certScore||0)+'%</div>'
    +'<div style="font-size:0.74rem;color:#5a5648;">Assessment Score</div>'
    +'<div class="cert-id">'+(p.certificateId||'FINCY-2026-XXXX')+' \u00B7 '+(p.certDate||new Date().toISOString().slice(0,10))+' \u00B7 fincyintelligence.com</div>'
    +'</div></body></html>';
}

function shareOnLinkedIn(){
  var p=loadProgress();
  var text='I just earned the AI Finance Professional certification from Fincy Intelligence! Certificate: '+(p.certificateId||'FINCY-2026-XXXX')+'. Skills: AI Financial Analysis, FP&A Automation, Prompt Engineering. Free academy: https://jitenparida95.github.io/fincy-intelligence/#learning #FPandA #AI #Finance';
  var url=encodeURIComponent('https://jitenparida95.github.io/fincy-intelligence/');
  window.open('https://www.linkedin.com/shareArticle?mini=true&url='+url+'&title='+encodeURIComponent('AI Finance Professional Certification'),'_blank');
  if(navigator.clipboard)navigator.clipboard.writeText(text);
}

var BADGES=[
  {id:'first_lesson',emoji:'\uD83C\uDF31',title:'First Step',color:'#c9a84c',desc:'Completed your first lesson'},
  {id:'stage1_done',emoji:'\uD83E\uDD49',title:'Stage 1 Complete',color:'#c9a84c',desc:'Finished AI in Finance Basics'},
  {id:'stage2_done',emoji:'\uD83E\uDD48',title:'Stage 2 Complete',color:'#4ade80',desc:'Finished Automating Finance Work'},
  {id:'stage3_done',emoji:'\uD83E\uDD47',title:'Stage 3 Complete',color:'#818cf8',desc:'Finished Build AI Finance Tools'},
  {id:'expert',emoji:'\uD83C\uDFC6',title:'Expert',color:'#2dd4bf',desc:'Finished all 4 stages'},
  {id:'streak3',emoji:'\uD83D\uDD25',title:'3-Day Streak',color:'#f97316',desc:'Learned 3 days in a row'},
  {id:'streak7',emoji:'\u26A1',title:'7-Day Streak',color:'#fbbf24',desc:'Learned 7 days in a row'},
  {id:'half_done',emoji:'\u2B50',title:'Halfway There',color:'#a78bfa',desc:'Completed 45 lessons'},
  {id:'project_done',emoji:'\uD83D\uDD2C',title:'Project Builder',color:'#34d399',desc:'Completed a project'},
  {id:'certified',emoji:'\uD83C\uDF93',title:'AI Finance Professional',color:'#f97316',desc:'Earned the certification'}
];

function checkAndAwardBadges(){
  var p=loadProgress();p.badges=p.badges||[];
  var done=p.completedLessons.length;
  var awards=[];
  var add=function(id){if(p.badges.indexOf(id)<0){p.badges.push(id);awards.push(id);}};
  if(done>=1)add('first_lesson');
  if(p.completedStages.indexOf('stage_01')>=0)add('stage1_done');
  if(p.completedStages.indexOf('stage_02')>=0)add('stage2_done');
  if(p.completedStages.indexOf('stage_03')>=0)add('stage3_done');
  if(['stage_01','stage_02','stage_03','stage_04'].every(function(s){return p.completedStages.indexOf(s)>=0;}))add('expert');
  if((p.streakDays||0)>=3)add('streak3');
  if((p.streakDays||0)>=7)add('streak7');
  if(done>=45)add('half_done');
  if((p.completedProjects||[]).length>=1)add('project_done');
  if(p.certified)add('certified');
  saveProgress(p);
  awards.forEach(function(id){var b=BADGES.find(function(x){return x.id===id;});if(b)showBadgeToast(b);});
}

function showBadgeToast(badge){
  var el=document.createElement('div');
  el.className='lh-badge-toast';
  el.style.cssText='position:fixed;top:80px;right:24px;z-index:10001;background:#101010;border:1px solid '+badge.color+';padding:14px 18px;display:flex;align-items:center;gap:12px;min-width:220px;';
  el.innerHTML='<span style="font-size:1.4rem;">'+badge.emoji+'</span><div><div style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;text-transform:uppercase;letter-spacing:0.1em;color:'+badge.color+';">Badge Unlocked</div><div style="font-size:0.82rem;color:var(--white);font-weight:700;">'+badge.title+'</div></div>';
  document.body.appendChild(el);setTimeout(function(){el.remove();},4000);
}

function getBadgePanel(){
  var p=loadProgress();p.badges=p.badges||[];
  var html='<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px;">';
  BADGES.forEach(function(b){var earned=p.badges.indexOf(b.id)>=0;html+='<div style="background:var(--s);border:1px solid '+(earned?b.color:'var(--b)')+';padding:14px;text-align:center;opacity:'+(earned?1:0.35)+'"><div style="font-size:1.6rem;">'+b.emoji+'</div><div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;text-transform:uppercase;color:'+(earned?b.color:'var(--text3)')+';margin:6px 0 4px;">'+b.title+'</div><div style="font-size:0.68rem;color:var(--text3);">'+b.desc+'</div></div>';});
  html+='</div>';return html;
}

function openModal(html,title){
  closeModal();
  var ov=document.createElement('div');ov.className='lh-modal-overlay';ov.id='lhEngineModal';
  ov.innerHTML='<div class="lh-modal"><div class="lh-modal-hdr"><span class="lh-modal-title">'+(title||'')+'</span><button class="lh-close" onclick="window.FincyLH.closeModal()">\u2715</button></div><div class="lh-modal-body" id="lhModalBody">'+html+'</div></div>';
  document.body.appendChild(ov);ov.addEventListener('click',function(e){if(e.target===ov)closeModal();});
}
function closeModal(){var m=document.getElementById('lhEngineModal');if(m)m.remove();}
function refreshModal(html){var b=document.getElementById('lhModalBody');if(b)b.innerHTML=html;}

function injectEngineStyles(){
  if(document.getElementById('lh-engine-styles'))return;
  var s=document.createElement('style');s.id='lh-engine-styles';
  s.textContent=[
    '.lh-modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:800;display:flex;align-items:center;justify-content:center;padding:20px;animation:lhFadeIn 0.2s ease;}',
    '@keyframes lhFadeIn{from{opacity:0}to{opacity:1}}',
    '.lh-modal{background:#101010;border:1px solid #2e2e28;max-width:760px;width:100%;max-height:88vh;overflow-y:auto;position:relative;}',
    '.lh-modal-hdr{background:#0f0f0c;border-bottom:1px solid #1e1e18;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:2;}',
    '.lh-modal-title{font-family:IBM Plex Mono,monospace;font-size:0.56rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);}',
    '.lh-close{background:none;border:none;color:var(--text3);cursor:pointer;font-size:1.1rem;padding:0 4px;}',
    '.lh-close:hover{color:var(--white);}',
    '.lh-modal-body{padding:24px 28px;}',
    '.lh-lesson-nav{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px;}',
    '.lh-lesson-btn{background:var(--s);border:1px solid var(--b);color:var(--text2);font-family:IBM Plex Mono,monospace;font-size:0.58rem;letter-spacing:0.06em;text-transform:uppercase;padding:7px 12px;cursor:pointer;transition:all 0.2s;}',
    '.lh-lesson-btn.done{border-color:var(--green);color:var(--green);}',
    '.lh-lesson-btn.active{background:var(--gold);color:var(--bg);border-color:var(--gold);}',
    '.lh-lesson-btn:hover:not(.active){border-color:var(--gold);color:var(--gold);}',
    '.lh-section{margin-bottom:20px;}',
    '.lh-section-label{font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold);margin-bottom:8px;}',
    '.lh-section-body{font-size:0.82rem;color:var(--text2);line-height:1.85;font-weight:300;}',
    '.lh-code{background:var(--bg);border:1px solid var(--b);border-left:3px solid var(--gold);padding:14px 16px;font-family:IBM Plex Mono,monospace;font-size:0.72rem;color:var(--text);line-height:1.7;white-space:pre-wrap;margin:8px 0;}',
    '.lh-input{width:100%;background:var(--bg);border:1px solid var(--b);color:var(--text);font-family:IBM Plex Mono,monospace;font-size:0.76rem;padding:10px 14px;resize:vertical;min-height:80px;box-sizing:border-box;outline:none;transition:border-color 0.2s;}',
    '.lh-input:focus{border-color:var(--gold);}',
    '.lh-btn{font-family:IBM Plex Mono,monospace;font-size:0.62rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;padding:10px 20px;cursor:pointer;border:none;transition:all 0.2s;}',
    '.lh-btn-gold{background:var(--gold);color:var(--bg);}',
    '.lh-btn-gold:hover{background:var(--gold2);}',
    '.lh-btn-ghost{background:transparent;border:1px solid var(--b2);color:var(--text2);}',
    '.lh-btn-ghost:hover{border-color:var(--gold);color:var(--gold);}',
    '.lh-btn-green{background:#4ade80;color:#0a0a08;}',
    '.lh-btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}',
    '.lh-ai-box{background:var(--s);border:1px solid var(--b);border-left:3px solid var(--gold);padding:16px 18px;font-size:0.8rem;color:var(--text2);line-height:1.85;min-height:60px;margin-top:8px;white-space:pre-wrap;}',
    '.lh-progress-bar{background:var(--b);height:6px;margin:8px 0;}',
    '.lh-progress-fill{height:100%;transition:width 0.4s ease;background:var(--gold);}',
    '.lh-spinner{display:inline-block;width:14px;height:14px;border:2px solid var(--b2);border-top-color:var(--gold);border-radius:50%;animation:lhSpin 0.8s linear infinite;vertical-align:middle;margin-right:6px;}',
    '@keyframes lhSpin{to{transform:rotate(360deg)}}',
    '.lh-locked{opacity:0.4;cursor:not-allowed;pointer-events:none;}',
    '.lh-badge-toast{animation:lhSlideIn 0.3s ease;}',
    '@keyframes lhSlideIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}',
    '@keyframes lhFI{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}'
  ].join('');
  document.head.appendChild(s);
}

function loadStage(si){
  try{
    injectEngineStyles();
    var stage=FINCY_COURSE.stages[si];
    if(!stage){console.warn('No stage at index',si);return;}
    if(stage.isCertification){loadCertificationStage();return;}
    if(!isStageUnlocked(si)){
      openModal('<div style="text-align:center;padding:32px;"><div style="font-size:2rem;margin-bottom:12px;">\uD83D\uDD12</div><div style="font-size:0.84rem;color:var(--text2);">Complete all lessons in Stage '+si+' to unlock this stage.</div></div>','Stage Locked');
      return;
    }
    _activeStage=si;
    var count=getCompletedCount();
    var pct=count.total>0?Math.round(count.done/count.total*100):0;
    var html='<div style="margin-bottom:20px;"><div style="font-size:0.76rem;color:var(--text3);margin-bottom:6px;">Overall progress: '+count.done+'/'+count.total+' lessons ('+pct+'%)</div><div class="lh-progress-bar"><div class="lh-progress-fill" style="width:'+pct+'%;"></div></div></div>';
    html+='<div class="lh-module-list">';
    stage.modules.forEach(function(m,mi){
      var mDone=0,mTotal=0;
      m.lessons.forEach(function(l){mTotal++;if(isLessonDone(l.id))mDone++;});
      html+='<div class="lh-module-card" onclick="window.FincyLH.loadModule('+si+','+mi+')" style="cursor:pointer;">'
        +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;text-transform:uppercase;color:var(--text3);margin-bottom:6px;">Module '+(mi+1)+'</div>'
        +'<div style="font-size:0.9rem;font-weight:700;color:var(--white);margin-bottom:8px;">'+escHtml(m.title)+'</div>'
        +'<div style="font-size:0.72rem;color:var(--text3);margin-bottom:8px;">'+mDone+'/'+mTotal+' lessons</div>'
        +'<div class="lh-progress-bar" style="height:3px;"><div class="lh-progress-fill" style="width:'+(mTotal>0?Math.round(mDone/mTotal*100):0)+'%;"></div></div>'
        +'</div>';
    });
    html+='</div>';
    openModal(html,'\u25C6 '+stage.badge+' \u2014 '+stage.title);
  }catch(e){console.error('loadStage error:',e);}
}

function loadCertificationStage(){
  injectEngineStyles();
  var p=loadProgress();
  var unlocked=isCertificationUnlocked();
  if(p.certified){
    openModal('<div style="text-align:center;padding:24px;">'
      +'<div style="font-size:2rem;margin-bottom:10px;">\uD83C\uDFC6</div>'
      +'<div style="font-family:Playfair Display,serif;font-size:1.3rem;color:var(--gold);margin-bottom:8px;">Certified!</div>'
      +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.56rem;color:var(--text3);margin-bottom:16px;">'+p.certificateId+'</div>'
      +'<div style="font-size:0.84rem;color:var(--text2);margin-bottom:20px;">Score: '+p.certScore+'% \u00B7 '+p.certDate+'</div>'
      +'<div class="lh-btn-row" style="justify-content:center;">'
      +'<button class="lh-btn lh-btn-gold" onclick="window.FincyLH.downloadCertificate()">Download Certificate</button>'
      +'<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.shareOnLinkedIn()">Share on LinkedIn</button>'
      +'</div></div>','\u25C6 Your Certificate');
    return;
  }
  if(!unlocked){
    openModal('<div style="text-align:center;padding:32px;">'
      +'<div style="font-size:2rem;margin-bottom:12px;">\uD83D\uDD12</div>'
      +'<div style="font-size:0.9rem;color:var(--white);font-weight:700;margin-bottom:8px;">Certification Locked</div>'
      +'<div style="font-size:0.78rem;color:var(--text2);line-height:1.8;">Complete all lessons in Stages 1\u20134 and finish at least one project to unlock the certification assessment.</div>'
      +'</div>','\u25C6 Certification Locked');
    return;
  }
  openModal('<div style="padding:8px 0;">'
    +'<div style="font-size:0.84rem;color:var(--text2);line-height:1.8;margin-bottom:20px;">Final assessment: 10 questions (5 MCQ + 3 case study + 2 prompt challenge). Pass at 70% to earn your AI Finance Professional certificate.</div>'
    +'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px;">'
    +'<div style="background:var(--s);border:1px solid var(--b);padding:14px;text-align:center;"><div style="font-size:1.3rem;margin-bottom:4px;">\uD83D\uDCCA</div><div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;color:var(--gold);">MCQ</div><div style="font-size:0.72rem;color:var(--text2);">5 questions</div></div>'
    +'<div style="background:var(--s);border:1px solid var(--b);padding:14px;text-align:center;"><div style="font-size:1.3rem;margin-bottom:4px;">\uD83D\uDCBC</div><div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;color:var(--gold);">Case Study</div><div style="font-size:0.72rem;color:var(--text2);">3 questions</div></div>'
    +'<div style="background:var(--s);border:1px solid var(--b);padding:14px;text-align:center;"><div style="font-size:1.3rem;margin-bottom:4px;">\uD83D\uDCA1</div><div style="font-family:IBM Plex Mono,monospace;font-size:0.5rem;color:var(--gold);">Prompt Challenge</div><div style="font-size:0.72rem;color:var(--text2);">2 questions</div></div>'
    +'</div>'
    +'<div class="lh-btn-row"><button class="lh-btn lh-btn-gold" onclick="window.FincyLH.startAssessment()">Begin Assessment \u2192</button></div>'
    +'</div>','\u25C6 AI Finance Professional Certification');
}

function loadModule(si,mi){
  var stage=FINCY_COURSE.stages[si];
  if(!stage)return;
  var mod=stage.modules[mi];
  if(!mod)return;
  _activeStage=si;_activeModule=mi;
  var html='<button class="lh-btn lh-btn-ghost" style="margin-bottom:16px;padding:6px 12px;font-size:0.54rem;" onclick="window.FincyLH.loadStage('+si+')">\u2190 Back to Stage</button>';
  html+='<div class="lh-lesson-nav">';
  mod.lessons.forEach(function(l,li){var done=isLessonDone(l.id);html+='<button class="lh-lesson-btn'+(done?' done':'')+'" onclick="window.FincyLH.loadLesson('+si+','+mi+','+li+')">'+escHtml(l.title.slice(0,28))+'</button>';});
  html+='</div>';
  if(mod.project){html+='<div style="background:var(--s);border:1px solid var(--b);border-left:3px solid var(--green);padding:14px 18px;margin-top:16px;cursor:pointer;" onclick="window.FincyLH.loadProject('+si+','+mi+')">'+'<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;text-transform:uppercase;color:var(--green);margin-bottom:4px;">Module Project</div>'+'<div style="font-size:0.82rem;color:var(--white);">'+escHtml(mod.project.title)+'</div></div>';}
  openModal(html,'\u25C6 '+escHtml(mod.title));
}

function loadLesson(si,mi,li){
  var stage=FINCY_COURSE.stages[si];if(!stage)return;
  var mod=stage.modules[mi];if(!mod)return;
  var l=mod.lessons[li];if(!l)return;
  _activeStage=si;_activeModule=mi;_activeLesson=l;
  var done=isLessonDone(l.id);
  var html='<button class="lh-btn lh-btn-ghost" style="margin-bottom:16px;padding:6px 12px;font-size:0.54rem;" onclick="window.FincyLH.loadModule('+si+','+mi+')">\u2190 Back</button>';
  html+='<div style="margin-bottom:6px;font-family:IBM Plex Mono,monospace;font-size:0.5rem;text-transform:uppercase;color:var(--text3);">'+l.level+' \u00B7 '+l.type+' \u00B7 Difficulty '+l.difficulty_score+'/5</div>';
  html+='<div style="font-family:Playfair Display,serif;font-size:1.2rem;font-weight:900;color:var(--white);margin-bottom:16px;">'+escHtml(l.title)+'</div>';
  html+='<div class="lh-section"><div class="lh-section-label">Concept</div><div class="lh-section-body">'+escHtml(l.explanation)+'</div></div>';
  html+='<div class="lh-section"><div class="lh-section-label">Example</div><div class="lh-code">'+escHtml(l.example)+'</div></div>';
  html+='<div class="lh-section"><div class="lh-section-label">Your Task</div><div class="lh-section-body">'+escHtml(l.task)+'</div></div>';
  html+='<div class="lh-section"><div class="lh-section-label">Ask AI CFO</div><textarea class="lh-input" id="lhTaskInput" placeholder="Type your question or answer here\u2026"></textarea><div id="lhAIOutput" class="lh-ai-box" style="display:none;"></div>';
  html+='<div class="lh-btn-row"><button class="lh-btn lh-btn-gold" onclick="window.FincyLH.handleAIRequest()">Ask AI CFO \u2192</button>';
  if(!done){html+='<button class="lh-btn lh-btn-green" onclick="window.FincyLH.markComplete()">Mark Complete \u2713</button>';}
  else{html+='<span style="display:inline-flex;align-items:center;gap:6px;border:1px solid var(--green);color:var(--green);font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.1em;text-transform:uppercase;padding:4px 10px;">\u2713 Complete</span>';}
  html+='<button class="lh-btn lh-btn-ghost" onclick="window.FincyLH.goToNextLesson('+si+','+mi+','+li+')">Next \u2192</button></div></div>';
  openModal(html,'\u25C6 '+escHtml(l.title));
}

function loadProject(si,mi){
  var stage=FINCY_COURSE.stages[si];if(!stage)return;
  var mod=stage.modules[mi];if(!mod||!mod.project)return;
  var proj=mod.project;
  var html='<div style="font-family:Playfair Display,serif;font-size:1.1rem;font-weight:900;color:var(--white);margin-bottom:14px;">'+escHtml(proj.title)+'</div>';
  html+='<div class="lh-section"><div class="lh-section-label">Instructions</div><div class="lh-section-body">'+escHtml(proj.instructions)+'</div></div>';
  html+='<div class="lh-section"><div class="lh-section-label">AI Prompt to Use</div><div class="lh-code">'+escHtml(proj.ai_prompt)+'</div></div>';
  html+='<div class="lh-btn-row"><button class="lh-btn lh-btn-gold" onclick="window.FincyLH.useExample()">Use This Prompt \u2192</button><button class="lh-btn lh-btn-green" onclick="window.FincyLH.markProjectComplete('+si+','+mi+')">Mark Project Complete \u2713</button></div>';
  openModal(html,'\u25C6 Module Project');
}

function useExample(){
  var pf=document.getElementById('lhTaskInput');
  if(pf&&_activeLesson){pf.value=_activeLesson.ai_prompt||_activeLesson.task||'';}
}

function formatAIResponse(text) {
  /* Parse structured CFO response into styled sections */
  var sections = [
    {key:'ANSWER:',       icon:'💡', label:'Answer',         color:'var(--white)'},
    {key:'FINANCE INSIGHT:',icon:'📊',label:'Finance Insight',color:'var(--gold)'},
    {key:'ACTION:',       icon:'⚡', label:'Action',         color:'var(--green)'},
    {key:'NEXT LESSON:',  icon:'📚', label:'Next Lesson',    color:'#818cf8'},
    {key:'ASK NEXT:',     icon:'🎯', label:'Ask Next',       color:'#2dd4bf'}
  ];
  var html = '';
  var remaining = text;
  sections.forEach(function(sec, idx) {
    var startIdx = remaining.indexOf(sec.key);
    if (startIdx < 0) return;
    var endIdx = remaining.length;
    /* Find where next section starts */
    for (var j = idx+1; j < sections.length; j++) {
      var ni = remaining.indexOf(sections[j].key);
      if (ni > startIdx) { endIdx = ni; break; }
    }
    var content = remaining.slice(startIdx + sec.key.length, endIdx).trim();
    html += '<div style="margin-bottom:12px;padding:10px 14px;background:var(--s);border-left:3px solid '+sec.color+';">'
      + '<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;letter-spacing:0.12em;text-transform:uppercase;color:'+sec.color+';margin-bottom:6px;">'+sec.icon+' '+sec.label+'</div>'
      + '<div style="font-size:0.8rem;color:var(--text2);line-height:1.8;">'+escHtml(content)+'</div>'
      + '</div>';
  });
  /* If parsing found nothing, show raw text */
  if (!html) {
    html = '<div style="font-size:0.8rem;color:var(--text2);line-height:1.8;white-space:pre-wrap;">'+escHtml(text)+'</div>';
  }
  return html;
}

function callAnthropicAI(systemPrompt, userText, onSuccess, onError) {
  /* Direct Anthropic API call — no external key required */
  fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 700,
      system: systemPrompt,
      messages: [{ role: 'user', content: userText }]
    })
  })
  .then(function(r) {
    if (r.status === 429) { onError('Rate limit reached — please wait 30 seconds and try again.'); return null; }
    if (!r.ok) { onError('AI service error (' + r.status + '). Please try again.'); return null; }
    return r.json();
  })
  .then(function(d) {
    if (!d) return;
    var text = (d.content && d.content[0] && d.content[0].text) ? d.content[0].text : '';
    if (!text) { onError('No response received. Please try again.'); return; }
    onSuccess(text);
  })
  .catch(function(e) {
    onError('Connection error. Check your internet and try again.');
    console.error('callAnthropicAI:', e);
  });
}

function handleAIRequest(){
  var input=document.getElementById('lhTaskInput');
  var output=document.getElementById('lhAIOutput');
  try{
    if(!_activeLesson){
      if(output){output.innerHTML='<span style="color:#fbbf24;">Please start a lesson first.</span>';output.style.display='block';}
      return;
    }
    if(!input||!output)return;
    var userText=(input.value||'').trim();
    if(!userText){
      output.innerHTML='<span style="color:#fbbf24;">Please type a question or answer first.</span>';
      output.style.display='block';
      return;
    }
    /* Loading state */
    output.innerHTML='<span class="lh-spinner"></span> AI CFO thinking\u2026';
    output.style.display='block';

    var stage=typeof _activeStage==='number'?FINCY_COURSE.stages[_activeStage]:null;
    var sysPrompt='You are Fincy AI CFO — a world-class senior financial advisor, FP&A expert, and AI finance mentor. '
      +'You combine McKinsey analytical precision with FTSE CFO strategic thinking. '
      +'Stage context: '+(stage?stage.title:'Finance')+' | Lesson: '+(_activeLesson.title||'Finance')+' | Level: '+(_activeLesson.level||'intermediate')+'.'
      +'\n\nLesson AI Prompt: '+(_activeLesson.ai_prompt||'')
      +'\n\nALWAYS respond in this EXACT format (each section on its own line):'
      +'\nANSWER: [Direct, specific answer with real numbers from the user input]'
      +'\nFINANCE INSIGHT: [The underlying principle — why this matters for their career]'
      +'\nACTION: [One measurable step to take TODAY — specific, with a target]'
      +'\nNEXT LESSON: [One topic from the '+(_activeLesson.track||['FP&A']).join('+')+' track to study next]'
      +'\nASK NEXT: [One harder follow-up question to push their thinking further]'
      +'\n\nRULES: No generic advice. Reference exact numbers from user input. Be direct and CFO-level.';

    var askBtn = document.querySelector('.lh-btn-gold[onclick*="handleAIRequest"]');
    if(askBtn){askBtn.disabled=true;askBtn.textContent='Thinking\u2026';}

    callAnthropicAI(sysPrompt, userText,
      function(text) {
        output.innerHTML = formatAIResponse(text);
        output.style.display='block';
        saveUserWork(userText, text);
        _storeAIMemory(userText, text);
        var inp2=document.getElementById('lhTaskInput');if(inp2)inp2.value='';
        if(askBtn){askBtn.disabled=false;askBtn.textContent='Ask AI CFO \u2192';}
      },
      function(errMsg) {
        output.innerHTML='<div style="color:var(--red);font-size:0.8rem;">\u26a0\ufe0f '+escHtml(errMsg)+'</div>';
        output.style.display='block';
        if(askBtn){askBtn.disabled=false;askBtn.textContent='Ask AI CFO \u2192';}
      }
    );
  }catch(e){
    if(output){output.innerHTML='<span style="color:var(--red);">Unexpected error — please refresh the page.</span>';output.style.display='block';}
    console.error('handleAIRequest sync:',e);
  }
}

function markComplete(){
  if(!_activeLesson)return;
  var p=loadProgress();
  if(p.completedLessons.indexOf(_activeLesson.id)<0){
    p.completedLessons.push(_activeLesson.id);
    p.lessonsCompletedToday=(p.lessonsCompletedToday||0)+1;
    updateXP(20,0);
    var stage=FINCY_COURSE.stages[_activeStage];
    if(stage){var allDone=true;stage.modules.forEach(function(m){m.lessons.forEach(function(l){if(p.completedLessons.indexOf(l.id)<0)allDone=false;});});if(allDone&&p.completedStages.indexOf(stage.id)<0){p.completedStages.push(stage.id);}}
    saveProgress(p);checkAndAwardBadges();
    var btn=document.querySelector('.lh-btn-green');
    if(btn){btn.textContent='\u2713 Done!';btn.disabled=true;btn.style.opacity='0.6';}
  }
}

function markProjectComplete(si,mi){
  var p=loadProgress();p.completedProjects=p.completedProjects||[];
  var pid='proj_'+si+'_'+mi;
  if(p.completedProjects.indexOf(pid)<0){p.completedProjects.push(pid);saveProgress(p);checkAndAwardBadges();updateXP(50,0);_showFloatingMsg('Project complete! +50 XP!');}
}

function goToNextLesson(si,mi,li){
  var stage=FINCY_COURSE.stages[si];var mod=stage.modules[mi];
  if(li<mod.lessons.length-1){loadLesson(si,mi,li+1);}
  else if(mi<stage.modules.length-1){loadModule(si,mi+1);}
  else if(si<FINCY_COURSE.stages.length-2){loadStage(si+1);}
  else{closeModal();}
}

function handleAIMemory(sysPrompt,userText){
  var p=loadProgress();var memory=p.aiMemory||[];
  var msgs=[{role:'system',content:sysPrompt}];
  memory.slice(-2).forEach(function(t){if(t.user)msgs.push({role:'user',content:t.user});if(t.ai)msgs.push({role:'assistant',content:t.ai});});
  msgs.push({role:'user',content:userText});return msgs;
}

function _storeAIMemory(userText,aiResponse){
  var p=loadProgress();p.aiMemory=p.aiMemory||[];
  p.aiMemory.push({lessonId:_activeLesson?_activeLesson.id:'',user:userText,ai:aiResponse.slice(0,400)});
  if(p.aiMemory.length>3)p.aiMemory=p.aiMemory.slice(-3);saveProgress(p);
}

function saveUserWork(userInput,aiOutput){
  if(!userInput||!aiOutput)return;
  var p=loadProgress();p.savedWork=p.savedWork||[];
  p.savedWork.unshift({lessonId:_activeLesson?_activeLesson.id:'',lessonTitle:_activeLesson?_activeLesson.title:'Lesson',userInput:userInput,aiOutput:aiOutput,timestamp:new Date().toISOString()});
  if(p.savedWork.length>30)p.savedWork=p.savedWork.slice(0,30);saveProgress(p);
}

function showMyWork(){
  var p=loadProgress();var works=p.savedWork||[];
  if(!works.length){openModal('<div style="text-align:center;padding:32px;color:var(--text3);">No saved work yet. Complete a lesson and ask AI.</div>','\u25C6 My AI Work');return;}
  var html='<div style="display:flex;flex-direction:column;gap:12px;">';
  works.slice(0,20).forEach(function(w,i){
    html+='<div style="background:var(--s);border:1px solid var(--b);border-left:3px solid var(--gold);padding:14px 16px;">'
      +'<div style="font-family:IBM Plex Mono,monospace;font-size:0.48rem;color:var(--gold);margin-bottom:6px;">'+escHtml(w.lessonTitle||'')+'</div>'
      +'<div style="font-size:0.72rem;color:var(--text3);margin-bottom:4px;font-style:italic;">'+escHtml((w.userInput||'').slice(0,120))+'</div>'
      +'<div style="font-size:0.76rem;color:var(--text2);line-height:1.7;margin-bottom:8px;">'+escHtml((w.aiOutput||'').slice(0,250))+'</div></div>';
  });
  html+='</div>';
  openModal(html,'\u25C6 My AI Work ('+works.length+')');
}

function updateXP(xp){
  if(!xp)return;
  var p=loadProgress();p.xp=(p.xp||0)+xp;p.level=Math.floor(p.xp/100)+1;saveProgress(p);
  var el=document.getElementById('lhXPLabel');if(el)el.textContent=p.xp+' XP';
  var lel=document.getElementById('lhLevelBadge');if(lel)lel.textContent='Lv.'+p.level;
}

function updateStreak(){
  var p=loadProgress();var today=new Date().toISOString().slice(0,10);
  if(p.lastActiveDate===today){return p.streakDays||0;}
  var yesterday=new Date();yesterday.setDate(yesterday.getDate()-1);var yStr=yesterday.toISOString().slice(0,10);
  if(p.lastActiveDate===yStr){p.streakDays=(p.streakDays||0)+1;}else{p.streakDays=1;}
  p.lastActiveDate=today;saveProgress(p);return p.streakDays;
}

function getStreakDisplay(){var p=loadProgress();var days=p.streakDays||0;return{days:days,emoji:days>=7?'\u26A1':days>=3?'\uD83D\uDD25':'\uD83D\uDCA7'};}

function handleDailySystem(){
  var p=loadProgress();var today=new Date().toISOString().slice(0,10);
  if(p.lastDayDate!==today){p.lessonsCompletedToday=0;p.lastDayDate=today;saveProgress(p);}
}

function _showFloatingMsg(msg){
  var el=document.createElement('div');
  el.style.cssText='position:fixed;bottom:140px;right:24px;z-index:10000;background:#101010;border:1px solid var(--gold);padding:12px 18px;max-width:280px;font-size:0.78rem;color:var(--text2);animation:lhSlideIn 0.3s ease;';
  el.textContent=msg;document.body.appendChild(el);setTimeout(function(){el.remove();},4000);
}

function _buildStreakBadgeRowHtml(){
  var p=loadProgress();var s=getStreakDisplay();p.badges=p.badges||[];
  var xp=p.xp||0;var level=Math.floor(xp/100)+1;
  return '<div style="display:flex;align-items:center;gap:8px;font-family:IBM Plex Mono,monospace;font-size:0.52rem;text-transform:uppercase;letter-spacing:0.08em;">'
    +'<span style="color:var(--gold);" id="lhLevelBadge">Lv.'+level+'</span>'
    +'<span style="color:var(--text3);">|</span>'
    +'<span style="color:var(--text2);" id="lhXPLabel">'+xp+' XP</span>'
    +'<span style="color:var(--text3);">|</span>'
    +'<span id="streakEmoji">'+s.emoji+'</span>'
    +'<span style="color:var(--text2);" id="streakLabel">'+s.days+' day streak</span>'
    +'<span style="color:var(--text3);">|</span>'
    +'<span style="cursor:pointer;color:var(--gold);text-decoration:underline;" onclick="window.FincyLH.showBadges()">Badges ('+p.badges.length+'/'+BADGES.length+')</span>'
    +'<span style="cursor:pointer;color:var(--text2);text-decoration:underline;" onclick="window.FincyLH.showMyWork();" id="workCount">My Work ('+((p.savedWork||[]).length)+')</span>'
    +'</div>';
}

function updateProgressBars(){
  FINCY_COURSE.stages.forEach(function(stage,si){
    var done=0,total=0;
    stage.modules.forEach(function(m){m.lessons.forEach(function(l){total++;if(isLessonDone(l.id))done++;});});
    var pct=total>0?Math.round(done/total*100):0;
    var barEl=document.getElementById('lh-stage-bar-'+si);if(barEl)barEl.style.width=pct+'%';
    var progEl=document.getElementById('lh-stage-prog-'+si);
    if(progEl){
      if(stage.isCertification){var p=loadProgress();progEl.textContent=p.certified?'Certified \u2713 \u00B7 '+(p.certScore||0)+'%':(isCertificationUnlocked()?'Ready to assess':'Complete stages 1\u20134 first');}
      else{progEl.textContent=done+'/'+total+' lessons';}
    }
    var btn=document.getElementById('lh-stage-btn-'+si);
    if(btn){
      if(stage.isCertification){var p2=loadProgress();btn.textContent=p2.certified?'\uD83C\uDFC6 View Certificate':(isCertificationUnlocked()?'Begin Assessment \u2192':'\uD83D\uDD12 Locked \u2014 Complete All Stages');btn.classList.toggle('lh-locked',!isCertificationUnlocked()&&!p2.certified);}
      else if(!isStageUnlocked(si)){btn.classList.add('lh-locked');btn.textContent='\uD83D\uDD12 Locked';}
      else{btn.classList.remove('lh-locked');btn.textContent=done===total&&total>0?'\u2713 Review':'Start Stage '+String(si+1).padStart(2,'0')+' \u2192';}
    }
  });
}

function updateStreakDisplay(){var s=getStreakDisplay();var p=loadProgress();var xp=p.xp||0;var level=Math.floor(xp/100)+1;var el=document.getElementById('lhLevelBadge');if(el)el.textContent='Lv.'+level;var xpEl=document.getElementById('lhXPLabel');if(xpEl)xpEl.textContent=xp+' XP';var sEl=document.getElementById('streakEmoji');if(sEl)sEl.textContent=s.emoji;var slEl=document.getElementById('streakLabel');if(slEl)slEl.textContent=s.days+' day streak';var dlEl=document.getElementById('dailyGoalLabel');if(dlEl)dlEl.textContent=(p.lessonsCompletedToday||0)+'/'+(p.dailyGoal||2)+' today';}

function downloadTemplate(stageId,idx){_showFloatingMsg('Templates coming soon in the next update!');}
function getTemplatePanel(){return '<div style="padding:8px 0;color:var(--text2);">Templates download from the module project sections.</div>';}
function getResumePanel(){var p=loadProgress();return '<div style="padding:8px 0;font-size:0.78rem;color:var(--text2);">Complete stages to unlock resume bullets and LinkedIn templates.</div>';}
function getSharePanel(){return '<div class="lh-btn-row"><button class="lh-btn lh-btn-gold" onclick="window.FincyLH.shareOnLinkedIn()">Share on LinkedIn</button></div>';}

function resetProgress(){if(confirm('Reset ALL progress? This cannot be undone.')){localStorage.removeItem(PROGRESS_KEY);location.reload();}}
function copyText(elemId){var el=document.getElementById(elemId);if(!el)return;if(navigator.clipboard){navigator.clipboard.writeText(el.innerText||el.textContent).then(function(){_showFloatingMsg('Copied!');});}}

function initLearningHub(){
  injectEngineStyles();
  handleDailySystem();
  updateStreak();
  updateProgressBars();

  var lhSec=document.getElementById('learning');
  if(lhSec){
    var existing=document.getElementById('lhOverallBar');
    if(!existing){
      var count=getCompletedCount();var pct=count.total>0?Math.round(count.done/count.total*100):0;
      var barEl=document.createElement('div');barEl.id='lhOverallBar';barEl.style.cssText='margin:16px 0 0;padding:0 0 8px;';
      barEl.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;"><span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text3);">Overall Progress</span><span style="font-family:IBM Plex Mono,monospace;font-size:0.52rem;color:var(--gold);" id="lhOverallLabel">'+count.done+'/'+count.total+' lessons ('+pct+'%)</span></div><div class="lh-progress-bar"><div class="lh-progress-fill" id="lhOverallProgress" style="width:'+pct+'%;"></div></div>';
      var banner=lhSec.querySelector('[style*="818cf8"]');
      if(banner&&banner.parentNode){banner.parentNode.insertBefore(barEl,banner.nextSibling);}else{lhSec.insertBefore(barEl,lhSec.firstChild.nextSibling);}
    }
    var sRow=document.getElementById('lhStreakBadgeRow');
    if(!sRow){sRow=document.createElement('div');sRow.id='lhStreakBadgeRow';sRow.style.cssText='display:flex;align-items:center;gap:14px;margin-bottom:16px;flex-wrap:wrap;';sRow.innerHTML=_buildStreakBadgeRowHtml();var ob=document.getElementById('lhOverallBar');if(ob&&ob.parentNode){ob.parentNode.insertBefore(sRow,ob.nextSibling);}}
  }

  FINCY_COURSE.stages.forEach(function(stage,si){
    var btn=document.getElementById('lh-stage-btn-'+si);
    if(btn){btn.onclick=function(e){e.stopPropagation();window.FincyLH.loadStage(si);};}
  });

  /* Drain queued clicks */
  var q=window._FLH_QUEUE||[];
  if(q.length&&window.FincyLH){q.forEach(function(call){var fn=call[0];if(typeof window.FincyLH[fn]==='function'){try{window.FincyLH[fn].apply(window.FincyLH,call.slice(1));}catch(e){console.warn('Replay:',e);}}});window._FLH_QUEUE=[];}
}

window.FincyLH={
  loadStage:loadStage,loadModule:loadModule,loadLesson:loadLesson,
  handleAIRequest:handleAIRequest,markComplete:markComplete,markProjectComplete:markProjectComplete,
  loadProject:loadProject,useExample:useExample,closeModal:closeModal,
  downloadTemplate:downloadTemplate,showBadges:function(){openModal(getBadgePanel(),'\u25C6 Your Badges');},
  copyText:copyText,goToNextLesson:goToNextLesson,showMyWork:showMyWork,
  handleDailySystem:handleDailySystem,updateXP:updateXP,saveUserWork:saveUserWork,
  handleAIMemory:handleAIMemory,startAssessment:startAssessment,showQuestion:showQuestion,
  selectMCQ:selectMCQ,saveAssessmentAnswer:saveAssessmentAnswer,submitAssessment:submitAssessment,
  downloadCertificate:downloadCertificate,shareOnLinkedIn:shareOnLinkedIn,
  resetProgress:resetProgress,getSharePanel:getSharePanel,getResumePanel:getResumePanel,
  getTemplatePanel:getTemplatePanel
};

if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',initLearningHub);}else{initLearningHub();}
