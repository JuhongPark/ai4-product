# O1 — Human-AI Collaboration Model Evolution at AI-Forward Firms (2023–2026)

> **Prompt:** Axis O, prompt O1 of the AI-Era Organizational Adaptability research plan.
> **Date:** 2026-04-22
> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Anchor questions:**
> - *Engineering:* How is the technical infrastructure for an AI-based decision-making system designed and built?
> - *Managerial:* What operational and governance structures are required for it to function effectively in an organization?

---

## 1. Method

### 1.1 Question
Which human–AI collaboration models at leading AI-native and AI-forward firms proved **resilient** across 2023–2026 capability shifts, and which required repeated redesign? Distinguish **substantive restructuring** (Leavitt's diamond — task, technology, people, *and* structure jointly re-optimised) from **public-relations restructuring** (memo, slide, press release; no durable joint change).

### 1.2 Scope and unit of analysis
- **Window:** January 2023 (ChatGPT diffusion trigger) → April 2026 (date of writing).
- **Unit:** firm-year. A firm-year is a substantive change if we can document at least two of the four Leavitt vertices altered in the same calendar year with operational consequences.
- **Firms covered as primary cases:** Shopify, Klarna, Stripe, Palantir, Anthropic, OpenAI, Perplexity, Cognition, Harvey, Sierra, Cursor (Anysphere), Replit, McKinsey QuantumBlack, BCG X, Bain (secondary).
- **Firms covered for contrast or secondary evidence:** Duolingo, Canva, Atlassian, Salesforce, IBM, Amazon, Microsoft, Meta, Google, Accenture.

### 1.3 Evidence hygiene
- Primary: founder memos (Lütke, Siemiatkowski, von Ahn), X/LinkedIn posts, earnings calls, S-1/F-1 filings, company engineering blogs, company research publications (Anthropic Economic Index, Anthropic internal work-transformation survey).
- Secondary: Reuters, Bloomberg, CNBC, The Information, TechCrunch, Fortune, Financial Times, The Register, Pragmatic Engineer newsletter.
- Dates are absolute. Where a claim originates from a single promotional channel (Klarna Feb 2024 claim of "700-agent equivalent work"), it is labelled as such and the later counter-evidence is carried with it.
- Negative evidence is recorded explicitly in §4.
- Confidence labels: H (multiple independent primary sources), M (one primary + reputable press), L (trade press or single-source claim).

### 1.4 SDM frame applied
- **Socio-technical systems (Trist / Tavistock):** does the firm redesign the social subsystem (roles, norms, learning) *jointly* with the technical subsystem (agents, IDE surfaces, model routing)?
- **Ambidextrous organisation (O'Reilly & Tushman):** is exploration (AI labs, agent R&D) structurally separated from exploitation (revenue product lines), or integrated?
- **Viable System Model (Beer):** does the collaboration structure span S1 (operations), S2 (coordination), S3 (control), S4 (intelligence/scan), S5 (identity/policy)? Firms that attenuate any one system show adaptability failure modes.
- **Leavitt's diamond:** task × technology × people × structure — the classification screen for substantive vs. PR change.
- **DSM reading for reporting structure:** documented where public org-chart shifts allow it.

---

## 2. Evidence table

Each row is a firm-year with the most load-bearing action, source, and an SDM read. "Substantive" = at least two Leavitt vertices changed with operational consequences carried forward into the next year; "PR" = announcement without durable structural coupling; "Mixed" = partial.

| Firm | Year | Key action | Source | Classification |
|---|---|---|---|---|
| Shopify | 2023 | ~20 % headcount cut (May 2023, pre-AI-memo); founder consolidates product surfaces. | [MacroTrends / stockanalysis headcount series](https://stockanalysis.com/stocks/shop/employees/) | Substantive (cost; pre-AI framing) |
| Shopify | 2025 | 7 Apr 2025: Lütke memo *"Reflexive AI usage is now a baseline expectation"*; AI usage in 360 review; headcount only approved if manager shows AI cannot do the task. | [Lütke on X, 7 Apr 2025](https://x.com/tobi/status/1909251946235437514); [CNBC](https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html); [First Round — "From Memo to Movement"](https://www.firstround.com/ai/shopify) | Substantive (task + structure + people jointly changed; review rubric rewritten) |
| Shopify | 2025 | Headcount drifts from 8,100 (2024) to 7,600 (Dec 2025) while GMV grows; no single AI-layoff event disclosed. | [stockanalysis — SHOP headcount](https://stockanalysis.com/stocks/shop/employees/) | Substantive (tech × structure coupling maintained) |
| Klarna | 2023 | Dec 2023: hiring freeze announced, AI cited. | [HR Grapevine](https://www.hrgrapevine.com/us/content/article/2024-02-29-klarna-asked-to-be-openais-guinea-pig-now-its-chatbot-does-the-work-of-700-employees) | Substantive (structural hiring policy change) |
| Klarna | 2024 | 27 Feb 2024: OpenAI-powered assistant "doing the work of 700" customer-service FTE, 2/3 of chats handled, $40 M projected savings. | [Klarna press release](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/); [Fini labs explainer](https://www.usefini.com/blog/klarna-automates-two-thirds-of-customer-service-with-ai-assistant) | Substantive (at the time) but brittle |
| Klarna | 2024 | Dec 2024: Siemiatkowski delivers earnings commentary via AI clone of his own voice. | [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2025/klarna-ceo-sebastian-siemiatkowskiclones-voice-customer-service-hotline/) | PR (signalling) |
| Klarna | 2025 | 14 May 2025: Siemiatkowski tells Bloomberg "lower quality" from AI-only CX; rehiring humans; "Uber-style" flexible remote-agent model launched. | [Bloomberg via Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul); [Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396); [CX Dive](https://www.customerexperiencedive.com/news/klarna-pursues-uber-style-customer-service-model/812763/) | Substantive reversal |
| Klarna | 2025 | Mar 2025 F-1/S-1: headcount 5,527 (2022) → 4,352 (2023) → 3,422 (2024). ~40 % shrink. IPO narrative leans on AI. | [Klarna F-1 (SEC)](https://www.sec.gov/Archives/edgar/data/2003292/000200329225000024/klarnagroupplcf-1a3.htm); [CNBC](https://www.cnbc.com/2025/05/14/klarna-ceo-says-ai-helped-company-shrink-workforce-by-40percent.html) | Substantive (scale change is real) |
| Klarna | 2025–26 | Jun 2025: voice-cloned CEO hotline (US 1-424-667-5385) for feedback; hybrid AI-plus-human CX stack codified. | [PYMNTS Jun 2025](https://www.pymnts.com/news/artificial-intelligence/2025/klarna-ceo-sebastian-siemiatkowskiclones-voice-customer-service-hotline/) | Mixed (PR surface + substantive CX architecture) |
| Stripe | 2025 | Internal "Minions" agent harness on top of Goose; 400+ internal tools exposed via "Toolshed" MCP; ~1,300 PRs/wk merged unattended, reviewed by engineers. | [ByteByteGo — Stripe Minions](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs); [Lenny's Newsletter — Steve Kaliski](https://www.lennysnewsletter.com/p/how-stripe-built-minionsai-coding) | Substantive (tech + task; structure preserved — reviewers remain) |
| Palantir | 2023–26 | FDE model extended: "AIP bootcamp" five-day zero-to-use-case, ~70 % bootcamp-to-paid conversion within 90 days; 181 commercial customers +37 % YoY; "AI FDE" conversational agent beta Nov 2025. | [Palantir AIP bootcamp](https://www.palantir.com/platforms/aip/bootcamp/); [Palantir — AI FDE docs](https://www.palantir.com/docs/foundry/ai-fde/overview); [Constellation Research](https://www.constellationr.com/blog-news/insights/palantirs-commercial-business-scales-help-ai-boot-camps); [Everest Group](https://www.everestgrp.com/palantir-inside-the-category-of-one-forward-deployed-software-engineers-blog/) | Substantive (pre-AI model extends; now AI-hybrid) |
| Anthropic | 2024 | May 2024: Mike Krieger joins as CPO; product-engineering stood up as separate function. | [Anthropic news release](https://www.anthropic.com/news/mike-krieger-joins-anthropic) | Substantive (S4/S5 strengthened) |
| Anthropic | 2025 | Aug 2025 internal study: 132 engineer/researcher surveys + 53 interviews + 200 k Claude Code transcripts Feb→Aug 2025. Task complexity 3.2→3.8; "implement new feature" share 14.3 %→36.9 %; "design/planning" 1.0 %→9.9 %; delegable-task share ~20 %. Claude Code used across data infra, security, legal, growth. | [Anthropic — "How AI Is Transforming Work at Anthropic"](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic); [Anthropic internal blog — "How Anthropic teams use Claude Code"](https://claude.com/blog/how-anthropic-teams-use-claude-code); [PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf) | Substantive (social subsystem redesigned with tech; published as research) |
| Anthropic | 2025–26 | Applied AI / pre-sales architect team scaled ~5×; ~140 sales roles, engineering hiring +170 % since Jan 2025. | [Menlo VC jobs board](https://jobs.menlovc.com/companies/anthropic/jobs/50108263-recruiter-applied-ai); [STANDOUT Digital summary](https://standout.digital/post/ai-jobs-in-2026-what-anthropics-100m-and-openais-8k-hires-mean-for-you/) | Substantive (ambidextrous: research ↔ enterprise deployment) |
| Anthropic | 2026 | Jan 2026: Krieger moves from CPO to MTS / Labs co-lead (with Ben Mann) reporting to Daniela Amodei; Ami Vora becomes head of product. Labs unit (est. mid-2024 as 2-person incubator) doubled in 6 months. | [TechCrunch Apr 2026](https://techcrunch.com/2026/04/16/anthropic-cpo-leaves-figmas-board-after-reports-he-will-offer-a-competing-product/); [Techbuzz](https://www.techbuzz.ai/articles/anthropic-reshuffles-leadership-to-expand-ai-labs-unit) | Substantive (textbook O'Reilly-Tushman ambidextrous split) |
| OpenAI | 2024 | Headcount 770 (Nov 2023) → ~3,531 (Sep 2024). Engineering ~56 % of org. | [Unify](https://www.unifygtm.com/insights-headcount/openai); [seo.ai](https://seo.ai/blog/how-many-people-work-at-openai) | Substantive (pure scale) |
| OpenAI | 2025 | Oct 2025 DevDay: 92 % of OpenAI engineers use Codex; +70 % PRs/engineer/week; internal product built with "0 lines manually-written code". | [OpenAI — Introducing Codex](https://openai.com/index/introducing-codex/); [OpenAI — "Harness engineering"](https://openai.com/index/harness-engineering/); [VentureBeat](https://venturebeat.com/ai/the-most-important-openai-announcement-you-probably-missed-at-devday-2025); [DevOps.com](https://devops.com/openai-codex-transforming-software-development-with-ai-agents-2/) | Substantive (tech × task × process) |
| OpenAI | 2025 | 28 Oct 2025: corporate restructure — nonprofit becomes OpenAI Foundation; for-profit becomes OpenAI Group PBC. | [OpenAI — Our structure](https://openai.com/our-structure/) | Substantive (S5 identity/governance) |
| OpenAI | 2026 | Apr 2026: triple exit — CPO Kevin Weil, Sora head Bill Peebles, enterprise CTO Srinivas Narayanan depart in one day; "Science" initiative decentralised back into model teams; Brad Lightcap moved to "special projects". | [The Next Web](https://thenextweb.com/news/openai-departures-kevin-weil-sora-peebles-enterprise-pivot); [CNBC Apr 2026](https://www.cnbc.com/2026/04/17/openai-executives-leave.html) | Substantive (consolidation toward core revenue products) |
| Perplexity | 2025 | <50 FTE early 2025 at >$9 B valuation; Comet browser launched Jul 2025; CEO Srinivas: "entry-level jobs are disappearing" and "Comet boosts productivity so companies won't have to hire more". | [CNBC Oct 2025](https://www.cnbc.com/2025/10/03/perplexity-ceo-comet-ai-browser-hiring-gdp.html); [Final Round AI](https://www.finalroundai.com/blog/perplexity-ceo-admits-entry-level-jobs-are-disappearing-fast); [Fortune Mar 2026](https://fortune.com/2026/03/24/perplexity-ceo-ai-layoffs-not-bad-people-hate-jobs-entrepreneurship/) | Substantive (lean design as policy) |
| Cognition | 2025 (Jul) | Acquired Windsurf for ~$250 M; kept IP, 82 M ARR, 350+ enterprise customers; "100 % employees participated financially". | [Cognition blog](https://cognition.ai/blog/windsurf); [CNBC](https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html) | Substantive |
| Cognition | 2025 (Aug) | Three weeks later: 30 Windsurf FTE laid off; 9-month buyout offered to remaining ~200; stay-on requires 80+h/week, 6 days in office. | [TechCrunch Aug 2025](https://techcrunch.com/2025/08/05/three-weeks-after-acquiring-windsurf-cognition-offers-staff-the-exit-door/); [Storyboard18](https://www.storyboard18.com/how-it-works/after-acquisition-cognition-hits-reset-at-windsurf-with-layoffs-and-buyout-offers-78311.htm) | Substantive (harsh); partial acquihire |
| Cognition | 2025 (Sep) | Valuation $10.2 B on $400 M raise; combined enterprise ARR up >30 % post-deal. | [CNBC Sep 2025](https://www.cnbc.com/2025/09/08/cognition-valued-at-10point2-billion-two-months-after-windsurf-.html) | — |
| Harvey | 2023–26 | Headcount ~20 (Series B) → 340 (mid-2025) → 500+ (late 2025); 18 % of FTE are lawyers; Legal Engineer role formalised; 337 legal customers; $11 B valuation Mar 2026. | [Harvey company page](https://www.harvey.ai/company); [Fortune Jun 2025](https://fortune.com/2025/06/23/harvey-raises-300-million-at-5-billion-valuation-to-be-legal-ai-for-lawyers-worldwide/); [CNBC Mar 2026](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html); [Aderant partnership Dec 2025](https://www.aderant.com/news-pr/aderant-and-harvey-announce-market-defining-partnership/) | Substantive (new role family; workflow redesign) |
| Sierra | 2024–25 | Bret Taylor + Clay Bavor; outcome-based pricing (no-resolve = no-charge); $100 M ARR in 7 quarters from Feb 2024 launch; $10 B valuation Sep 2025; offices in SF / NY / London / Singapore / Tokyo / Paris / Madrid / Toronto / Atlanta. | [Sierra blog — $100 M ARR](https://sierra.ai/blog/100m-arr); [CNBC Sep 2025](https://www.cnbc.com/2025/09/04/bret-taylor-sierra-ai-startup-salesforce-openai.html); [Sierra — outcome-based pricing](https://sierra.ai/blog/outcome-based-pricing-for-ai-agents); [TechCrunch Nov 2025](https://techcrunch.com/2025/11/21/bret-taylors-sierra-reaches-100m-arr-in-under-two-years/) | Substantive (pricing-model change propagates to ops) |
| Cursor (Anysphere) | 2025 | Jan: $100 M ARR. Jun: $500 M+ ARR, $9.9 B valuation, $900 M raise. Aug: ~150 FTE. Jul: acquihire of Koala for enterprise-readiness team. Nov: $29.3 B valuation. | [TechCrunch Jun 2025](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/); [Contrary Research — Cursor](https://research.contrary.com/company/cursor); [Tech Funding News](https://techfundingnews.com/anysphere-soars-to-29-3b-valuation-with-2-3b-funding-redefining-the-future-of-coding/) | Substantive |
| Replit | 2025 | $2.8 M → $150 M ARR in <12 months via Agent launch; ~70 FTE at $150 M ARR moment; $3 B valuation Sep 2025; Agent 3 (200-min autonomy) Sep 2025. Masad prefers "smart generalists who manage more agents". | [TechCrunch Sep 2025](https://techcrunch.com/2025/09/10/replit-hits-3b-valuation-on-150m-annualized-revenue/); [Craft Ventures — Inside Replit's Breakout Growth](https://medium.com/craft-ventures/inside-replits-breakout-growth-lessons-from-2-8m-to-150m-arr-d2820d28552f); [SaaStr](https://www.saastr.com/by-late-2025-replit-got-really-good-imagine-if-it-could-run-24x7/) | Substantive (workforce design-intent ≈ SaaS/10) |
| McKinsey (QuantumBlack) | 2023–25 | "Project Magnolia" back-office cuts ~2 k (2023); ~360–400 technical specialists cut 2024; ~200 tech roles cut 2025. Stated direction: "one agent per human employee". | [Final Round AI](https://www.finalroundai.com/blog/mckinsey-layoffs-few-thousand-jobs); [ContentGrip](https://www.contentgrip.com/mckinsey-ai-layoffs-automation-impact/) | Mixed (cost + AI; MBB generalist practice redesigned around QB) |
| BCG (BCG X) | 2024–26 | AI consulting = ~20 % of BCG revenue (2024); BCG X >3 k FTE; BCG research projects 50–55 % of jobs reshaped 2–3y, 10–15 % fully displaced longer-term. | [Case Interview Hub](https://www.caseinterviewhub.com/post/consulting-crisis-mckinsey-bcg-bain); [BCG — AI at Work 2025](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain); [BCG — AI transforms over half of jobs in 3 years](https://www.hpcwire.com/aiwire/2026/04/20/bcg-finds-ai-will-transform-over-half-of-jobs-within-three-years/) | Substantive (unit-level carve-out) |
| Bain | 2024–25 | ~150 consultants cut in India offices; AI unit hiring continues. | [Consultancy.in](https://www.consultancy.in/news/4231/bain-company-fires-over-150-consultants-in-india-offices) | Mixed |
| Accenture | 2025 | Sep 2025: ~11 k cut over 3 months, $865 M restructuring programme; AI-and-data specialists ~77 k (≈2× from 2023); 550 k staff reskilled in gen-AI. | [CNBC Sep 2025](https://www.cnbc.com/2025/09/26/accenture-plans-on-exiting-staff-who-cant-be-reskilled-on-ai.html); [Gulf News](https://gulfnews.com/technology/accenture-cuts-thousands-of-jobs-in-global-ai-restructuring-1.500290493); [CIO Dive](https://www.ciodive.com/news/accenture-generative-ai-revenue-skills-training-data-modernization/761161/) | Substantive |
| Duolingo | 2023 (Dec) / 2024 (Oct) | ~10 % of contractor workforce cut late 2023; second round Oct 2024 (translators/writers). | [TechCrunch Jan 2024](https://techcrunch.com/2024/01/09/duolingo-cut-10-of-its-contractor-workforce-as-the-company-embraces-ai/); [The Register Apr 2025](https://www.theregister.com/2025/04/29/duolingo_ceo_ai_first_shift/) | Substantive (contractor stratum) |
| Duolingo | 2025 (Apr) | Von Ahn "AI-first" memo on LinkedIn — echo of Lütke template. | [TechCrunch May 2025](https://techcrunch.com/2025/05/04/is-duolingo-the-face-of-an-ai-jobs-crisis/) | PR (statement) |
| Duolingo | 2025 (May–Aug) | Consumer-side backlash ("AI first means people last"); CEO walks back on LinkedIn; "not replacing what employees do"; clarifying memo Aug 2025. | [Fortune Aug 2025](https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees/); [CX Dive](https://www.customerexperiencedive.com/news/duolingo-ai-first-consumer-backlash-lessons/757133/) | PR reversal |
| Duolingo | 2026 (Apr) | Von Ahn removes AI usage as formal performance-review metric but keeps contractor-substitution rule. | [Fortune Apr 2026](https://fortune.com/2026/04/13/duolingo-ceo-luis-von-ahn-ai-usage-requirement-employee-performance-evaluations/) | Mixed (partial rollback) |
| Canva | 2025 | Technical-writing team largely eliminated while Magic Studio at Scale and Canva AI ship. | [ACS Information Age](https://ia.acs.org.au/article/2025/canva-lays-off-technical-writers-amid-ai-push.html); [SmartCompany](https://www.smartcompany.com.au/artificial-intelligence/canvas-new-ai-tools-visual-suite-job-cuts/) | Substantive (one role family collapsed) |
| Atlassian | 2026 (Mar) | ~1,600 jobs cut (~10 %); >900 of cuts in SW R&D; Rovo rebranded from "tool" to "AI-powered teammate"; CTO replaced; ML-engineer and AI-product hiring continues. | [CNBC Mar 2026](https://www.cnbc.com/2026/03/11/atlassian-slashes-10percent-of-workforce-to-self-fund-investments-in-ai.html); [The Register](https://www.theregister.com/2026/03/11/atlassian_layoffs); [HR Digest — "AI washing"](https://www.thehrdigest.com/atlassian-layoffs-reignite-conversations-around-the-rise-of-ai-washing-in-2026/) | Mixed (cost-driven framed as AI-driven) |
| Salesforce | 2025 (Sep) | Benioff: CX staff reduced 9,000 → 5,000 after Agentforce; 2,000 new Agentforce-focused sales hires planned. | [CNBC Sep 2025](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html); [Fortune Sep 2025](https://fortune.com/2025/09/02/salesforce-ceo-billionaire-marc-benioff-ai-agents-jobs-layoffs-customer-service-sales/); [Salesforce Ben](https://www.salesforceben.com/ai-agents-drive-4000-job-cuts-in-salesforce-support-division/) | Substantive |
| IBM | 2024–25 | AskHR automates ~94 % of routine HR tasks, 11.5 M interactions 2024; ~200–400 HR FTE displaced; Krishna: "total employment actually up" (redeployed to programmers/sales). | [Entrepreneur Jul 2025](https://www.entrepreneur.com/business-news/ibm-ceo-ai-replaced-hundreds-of-human-resources-staff/491341); [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2025/ibm-ceo-hr-layoffs-due-to-ai-led-to-more-investment-in-other-roles/) | Substantive (one role family automated; redeploy funded net-new roles) |
| Amazon | 2025 (Oct) | ~14 k corporate cuts (~4 %); Reuters: up to 30 k cumulative; Jassy Jun-2025 memo: "fewer people doing some of the jobs"; Nov 2025 Jassy recant: "it's culture"; 1,000+ gen-AI services/apps in flight. | [CNN Oct 2025](https://www.cnn.com/2025/10/28/business/amazon-layoffs); [Fortune Nov 2025](https://fortune.com/2025/11/01/ceo-andy-jassy-amazon-layoffs-about-culture-not-ai/); [Fortune Jul 2025](https://fortune.com/2025/07/01/amazon-ceo-andy-jassy-ai-fewer-jobs/) | Mixed (AI + layers-removal) |
| Microsoft | 2025 | ~15 k cuts incl. 1,985 in Redmond; Nadella: Copilot writes ~30 % of code; Julia Liuson (Dev Div president) mandates AI-tool use as core performance criterion. | [JobsPikr](https://www.jobspikr.com/blog/analysing-microsoft-layoffs-2025/); [Storyboard18](https://www.storyboard18.com/brand-marketing/microsofts-2025-layoff-ledger-more-than-15000-jobs-axed-in-seven-months-74376.htm) | Mixed |
| Meta | 2025 (Jun) | $14.3 B Scale AI investment + 49 % stake; Alexandr Wang becomes Chief AI Officer running Meta Superintelligence Labs. | [BigGo Finance / artificialintelligence-news](https://www.artificialintelligence-news.com/news/meta-ai-job-cuts-hiring-contradiction-2025/); [CNBC Oct 2025](https://www.cnbc.com/2025/10/22/meta-layoffs-ai.html) | Substantive (ambidextrous: new "TBD Lab" / MSL separated from FAIR / product AI) |
| Meta | 2025 (Oct) | 600 laid off across FAIR, AI product, AI infra; TBD Lab untouched. | [CNBC Oct 2025](https://www.cnbc.com/2025/10/22/meta-layoffs-ai.html); [Final Round AI](https://www.finalroundai.com/blog/meta-layoffs-2025) | Substantive (exploration privileged over exploitation) |
| Meta | 2026 (May, announced Mar) | 8,000 cuts in second broad reorg; LeCun departed late 2025 after direction disagreement. | [The Next Web](https://thenextweb.com/news/meta-layoffs-may-2026-ai-restructuring-thousands) | Substantive |
| Google | 2024–25 | Management layers reduced by >1/3 in 2025; ~200 AI contractors cut (Gemini / AI Overviews); ~100 Cloud design FTE cut Oct 2025; boomerang rehires ~20 % of 2025 AI engineer intake. | [AILoss](https://ailoss.co/layoffs/google-layoffs-2023-onwards/); [Business Standard](https://www.business-standard.com/world-news/google-ai-hiring-boomerang-employees-rehiring-engineers-talent-war-gemini-125122200200_1.html); [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-terminates-200-ai-contractors-ramp-down-blamed-but-workers-claim-questions-over-pay-and-job-insecurity-are-the-real-reason-behind-layoffs) | Mixed (de-layering + selective AI cuts + boomerang hiring) |

---

## 3. Pattern findings

### 3.1 Finding A — The "Lütke template" became a genre, but only Shopify coupled it to internal systems *(Confidence: H)*

Tobi Lütke's 7 April 2025 memo ("Reflexive AI usage is now a baseline expectation at Shopify") was posted on X because the memo was "in the process of being leaked". It had four operational consequences that together made the change substantive in Leavitt terms:

1. **Task:** every team must first attempt the task with AI before requesting headcount.
2. **Technology:** employees issued Claude, Copilot and Cursor licences; internal evals normalised.
3. **People:** 360-review rubric adds "AI-native / AI-reflexive" items so peers and managers score colleagues.
4. **Structure:** the headcount-request process goes through a gate tied to (1).

This is not a memo — it is a **control-loop rewrite**. The same template, when used by Duolingo, Fiverr and others, lacked the structural gate or the review-rubric change, and the resulting reversals (von Ahn's Aug-2025 walk-back, Apr-2026 removal of AI as a performance-review metric) are consistent with the hypothesis that **a memo without a matching structure change decays to PR**. Shopify's own evidence that its memo is holding is weaker than it looks: headcount drift (8,100 → 7,600) is consistent with attrition, not with the memo alone, and the memo's productivity claims ("100× the work done") are self-reported. Still, on a Leavitt read, Shopify is the clearest substantive case in the cohort.

### 3.2 Finding B — Klarna 2024 → 2025 is the canonical learning-loop / failure-to-learn case *(Confidence: H)*

Klarna's three phases map cleanly to an Argyris single- vs. double-loop reading and to a Hollnagel resilience reading.

- **Phase 1 (Dec 2023 – Feb 2024 announcement):** hiring freeze announced; OpenAI-powered assistant claimed to "do the work of 700 agents", 2/3 of chats handled in month 1, $40 M projected 2024 profit boost. In VSM terms, S1 (operations — CX) is radically restructured; S3 (control — quality measurement) is *attenuated* because the metric set is cost and handle-time, not complex-case resolution or NPS. In Leavitt terms, three vertices change (task, technology, people) and the fourth (structure) shifts to an AI-only routing; reversibility not budgeted for.
- **Phase 2 (May 2025 reversal):** Siemiatkowski tells Bloomberg the focus on cost became "too predominant" and quality suffered; hiring humans again, "Uber-style" remote-agent model (students, rural workers) launched. CEO frames it as a brand argument ("it's so critical that you are clear to your customer that there will always be a human if you want"). In VSM terms, S4 (external scan — customer complaint rate and NPS) is finally re-coupled to S1 decisions; in Argyris terms, this is **double-loop learning** — the governing variable (cost-first) is changed, not just the tactic.
- **Phase 3 (Jun 2025 — Apr 2026):** the system stabilises as a **hybrid**: AI for routine / high-volume, human for escalation / high-value, voice-cloned CEO hotline for feedback. Klarna still reports 853-agent-equivalent work handled by AI (Customer Experience Dive, 2025). The F-1 (Mar 2025) carries the 5,527 → 3,422 headcount shrink forward as the equity story; the substantive CX architecture is hybrid.

The learning-loop reading has a sharp implication for the adaptability frame: **an AI collaboration model that attenuates the feedback loop between customer outcome and staffing will be resilient in the cost dimension and brittle in the quality dimension**. Klarna survived because it re-coupled the loop within 15 months. The equivalent question for every other firm in this cohort is whether their S3/S4 coupling measures something other than cost.

### 3.3 Finding C — Anthropic, OpenAI and Stripe show the "AI-eating-own-dogfood" pattern as substantive joint redesign *(Confidence: H)*

Three firms in the cohort have published internal data detailed enough to support a joint-optimisation (socio-technical) reading rather than a claims-based reading.

- **Anthropic:** August 2025 study — 132 engineer/researcher surveys + 53 qualitative interviews + 200 k Claude Code transcripts between Feb and Aug 2025. Task complexity grew from 3.2 to 3.8; "implement new features" share grew 14.3 % → 36.9 %; "code design/planning" grew 1.0 % → 9.9 %; up to ~20 % of tasks fully delegable. Non-engineering teams (legal built phone-tree systems, growth marketing generated hundreds of ad variations, data-infra diagnosed Kubernetes pod IP exhaustion by screenshot) used Claude Code across the firm. In Leavitt terms, this is *all four* vertices changing: task (what work is done), technology (Claude Code), people (who can do which work: "more full-stack"), structure (Legal and Growth not going through Engineering for bespoke tools). The published self-critique — deskilling risk, loss of human collaboration — is a social-subsystem marker that joint optimisation is being treated as an open problem rather than a marketing claim.
- **OpenAI:** DevDay October 2025 — 92 % of engineers use Codex daily, +70 % PR volume per engineer per week; Sam Altman Feb 2026: "Almost all new code written at OpenAI today is from Codex users"; 95 % engineer weekly-active by Feb 2026. An internal product was built with "0 lines of manually-written code". The 28 Oct 2025 corporate restructure (OpenAI Foundation + OpenAI Group PBC) and the Apr-2026 CPO/Sora/enterprise-CTO triple exit with "OpenAI for Science" decentralisation show *structural* coupling: when the revenue-generating surface becomes clearly the ChatGPT + API pair, the exploratory research unit is folded back into model teams. This is a deliberate *move away from* an ambidextrous split and toward centralisation around revenue.
- **Stripe:** the "Minions" agent harness ships ~1,300 PRs/week unattended, with human engineers shifting time from writing to reviewing. The "Toolshed" MCP exposes ~500 internal tools; devbox warming gives 10-second cold-starts. The collaboration model here is not "AI replaces engineer" but "engineer becomes reviewer + tool-curator + harness-maintainer". Role stays, work composition changes.

The common thread: **the firms that treat the collaboration change as a research object (with survey, interview, usage-log and published post-mortem) also show the more durable Leavitt coupling**. The firms that treat it as a marketing object (memo only) show reversal within 12 months.

### 3.4 Finding D — Forward-deployed engineering is the most transferable AI-era organisational primitive *(Confidence: H)*

Palantir's FDE model, originated for pre-AI deployment (Echo/Delta team split — domain expert pairs with rapid-prototyper engineer), has been adopted or mimicked by at least six firms in the cohort:

- **Anthropic** — "Applied AI" team (pre-sales architects + technical advisors) now ~140 roles and scaling ~5×.
- **OpenAI** — "Forward Deployed Engineer" and "Solutions Engineer" roles targeting Fortune 500.
- **Harvey** — "Legal Engineer" as a new job family; 18 % of FTE are lawyers embedded in product & GTM.
- **Sierra** — agent-delivery engineers ("agent OS engineers") against outcome-based pricing.
- **Cognition** — post-Windsurf, a concentrated high-intensity on-site engineering delivery model.
- **Palantir itself** — "AIP Bootcamp": five days from zero-to-use-case, ~70 % paid conversion within 90 days.

This is a Leavitt-diamond claim about **structure**: the organisational interface between a frontier AI capability and a customer value-system does not scale through a generalist sales force. It scales through a paired technical-domain role operating on the customer's live data. Every firm that has hit >$100 M ARR on enterprise AI in this cohort has instantiated some variant. BCG X and QuantumBlack are consulting-industry variants of the same primitive (gen-AI practice as a forward-deployed Delta team with partner-level Echo above).

In VSM terms, the FDE role is the S1–S4 bridge — it is simultaneously operations (building) and external scan (field intelligence). Its emergence explains why firms that did not hire FDEs (e.g. consumer apps claiming AI-first without a deployment arm) show the worst ratio of claim to durable change.

### 3.5 Finding E — Ambidextrous structures are the winning exploration/exploitation pattern *(Confidence: M)*

O'Reilly & Tushman's prediction — that firms that succeed through a capability shift separate exploration and exploitation with senior integrative leadership — is visible in:

- **Anthropic** (Jan 2026): Labs becomes a distinct incubator under Krieger + Mann reporting to Daniela Amodei; Ami Vora runs product. Exploitation (Claude API, Claude Code) on one side, exploration (Labs experimental products) on the other, with the president bridging.
- **Meta** (Jun 2025 onward): TBD Lab / Meta Superintelligence Labs (Wang) protected; FAIR and product-AI cut. Exploration privileged over exploitation.
- **OpenAI** (Apr 2026): *inverse* — the exploratory "Science" unit is being **decentralised** back into model teams; the firm moves from ambidextrous to integrated-around-revenue. Consistent with a shift from capability-expansion mode to capability-monetisation mode.
- **McKinsey / QuantumBlack**: QB is explicitly the exploration/innovation carve-out in an otherwise exploitation-structured firm; BCG X plays the same role at BCG.

The negative case: **firms that claim AI-first without separating exploration from exploitation (Duolingo, Canva — at least in public evidence)** show reversal or decay. This is consistent with Tushman's argument that exploration cannot be performed inside an exploitation structure because its metrics are incompatible. Confidence is M not H because internal structure at private firms is often invisible from outside.

### 3.6 Finding F — Lean-by-design small orgs are disproportionately represented among the fastest growers *(Confidence: H)*

| Firm (Apr 2026) | FTE | Peak ARR or valuation milestone | FTE/$100 M-ARR ratio |
|---|---|---|---|
| Anthropic | ~5 k | ~$19 B ARR pace | ~26 |
| OpenAI | ~6.4 k (Jul 2025) growing to ~8 k end-2026 | ~$14 B annualised | ~46 |
| Cursor / Anysphere | ~150 | $500 M ARR (Jun 2025) | ~30 |
| Replit | ~70–150 | $150 M ARR (Sep 2025) | ~50–100 |
| Perplexity | <50 (early 2025) | 780 M queries/mo May 2025 | n/a |
| Sierra | hundreds | $100 M ARR in 7 quarters | n/a |

Compared with a SaaS reference point of ~700 FTE at $150 M ARR cited by Masad, the AI-native cohort runs at **5× to 10× smaller** on a headcount-per-revenue basis. This is a structural consequence of Stripe-style agent harnesses and Anthropic-style Claude-Code-everywhere, not a claim about individual productivity. In SDM terms, this is a *stock-and-flow* shift in the talent stock — the capital required per unit of output compresses.

The risk, consistent with the Duolingo reversal and the Klarna reversal, is that the social subsystem (trust, learning, cross-functional coordination) is not scaled proportionally — a classic Tavistock "unbalanced joint optimisation" failure. Anthropic's own internal research calls this out directly (deskilling and reduced collaboration among the top worker concerns).

### 3.7 Finding G — Consulting firms and incumbents run a dual pattern: cut generalist, hire AI specialist *(Confidence: H)*

McKinsey, BCG, Accenture and (within Microsoft, Google, IBM) the corporate incumbents all show the same signed-net-zero pattern across 2024–2026:

- **Layoffs cluster in back-office / mid-level generalist / contractor strata.**
- **Hiring expands in AI-and-data specialists, forward-deployed/solutions-architect roles, and sales for AI products.**
- **Public framing oscillates between "AI-driven" (when investor narrative favours efficiency) and "performance-management / culture / bureaucracy-removal" (when labour-relations narrative matters).**

Examples:
- Accenture: 11 k cut + 77 k AI-and-data specialists (≈2× from 2023) + 550 k reskilled.
- IBM: ~200–400 HR cut via AskHR + redeployed to programmers/sales; Krishna says total headcount is *up*.
- Amazon: Jun-2025 Jassy memo ("fewer people doing some jobs") → Oct-2025 14 k cut → Nov-2025 Jassy recant ("it's culture"). The *cause* story is mutable; the cut is real.
- Microsoft: ~15 k cut + mandate that AI-tool usage is a core performance component; Copilot writes "30 % of code".
- Salesforce: 9 k → 5 k support + 2 k new Agentforce-focused sales.

This is the negative evidence point for the "AI automates away jobs" narrative in its strong form. The signed-net-zero pattern says **AI shifts the workforce composition** — generalist operators out, specialist operators-of-operators in. For the adaptability frame, this is a much cleaner construct than "AI-caused unemployment": what changes is *which roles are scarce*.

### 3.8 Finding H — "AI-washing" of cost-driven layoffs is now common, making attribution harder *(Confidence: M)*

Atlassian's March 2026 1,600-role cut (>900 in SW R&D) was announced as funding "investment in AI and enterprise sales" while simultaneously Rovo was rebranded from a "tool" to an "AI-powered teammate". Trade press used the phrase "AI washing" to describe the pattern. Amazon's flip from "AI makes the workforce smaller" (Jun 2025) to "it's culture" (Nov 2025) is consistent with the same dynamic. The memo trend identified in Finding A creates a structural incentive to *attribute* cuts to AI when the underlying cause is growth-margin pressure, regulatory risk, or over-hiring in 2021–22. The reverse attribution — layoffs *not* attributed to AI that actually are — is harder to observe but probably symmetric.

**Implication for O2 (role redefinition cycles):** any indicator of AI-driven role change must be triangulated against the hiring side (what new roles are being posted), not only the layoff side, to be construct-valid.

---

## 4. Open questions and negative evidence

### 4.1 Negative evidence

- **Firms that claimed AI-first without measurable structural change:** Duolingo (Apr 2025 memo → Aug 2025 walk-back → Apr 2026 removal of AI as perf-review metric) is the cleanest case. The company retained the contractor-substitution rule but rolled back the individual-level evaluation component — exactly the part that would have made Leavitt coupling work.
- **Klarna's Feb 2024 "work of 700" claim was a point-in-time optimisation, not a stable equilibrium.** The 2025 reversal is the evidence. We should not cite the 2024 claim without the 2025 counter-evidence in the same paragraph. The later Dec-2025 Klarna claim of "853-agent equivalent" is similarly point-in-time and should be labelled as such.
- **Notion:** despite being an obvious AI-collaboration subject, public evidence for 2025 is thin on structural change. Notion appears to be *hiring* designers and PMs and adding AI quality roles, with no public layoff event or structural reorg disclosed. This is a noted negative: a firm whose product embeds AI but whose org evidence does not publicly exhibit the Leavitt-diamond pattern. (Confidence: L.)
- **Stripe public positioning is quieter than its implementation.** The Collison brothers have avoided Lütke-style memos. The "Minions" system is extensively documented by Stripe engineers in trade channels but without a top-down "AI-first" announcement. This makes Stripe a counter-example to the hypothesis that public framing is required for substantive change, and a support-example for the hypothesis that the framing is decoupled from the change.
- **Palantir has not framed AIP as a role-restructuring event.** The AI-FDE is presented as an *addition* to the existing FDE function, not a substitution. If anything, Palantir's position is that FDE scaling is bottlenecked by FDE hiring, not by AI capability — the inverse of the standard claim.

### 4.2 Open questions

1. **What fraction of "AI-attributed" layoffs in 2025 were actually cost-driven?** Jassy's pivot from "AI" → "culture" gives one data point. A Bloomberg / FT / Reuters side-by-side of stated cause at announcement vs. stated cause 6–9 months later across the 30-firm cohort would resolve the attribution question for M2 indicators.
2. **How robust is the Klarna hybrid equilibrium?** The May-2025 reversal is documented but the follow-on 12–24-month data (complaint volume, NPS, agent retention, hybrid routing accuracy) is not yet public. Worth watching through the IPO prospectus updates.
3. **Is the Anthropic "Labs" carve-out durable, or will it be folded back like OpenAI's "Science" unit?** The O'Reilly-Tushman prediction would say durability depends on whether the Labs unit is resourced from the same P&L as the exploitation unit (Claude API). If so, it will eventually collapse.
4. **Does the Cursor / Replit / Perplexity lean-by-design model survive a transition to mid-size?** 150 FTE at $500 M ARR is extreme; the 500–2,000 FTE zone is where socio-technical stress typically emerges (Tavistock observation: joint-optimisation failures cluster at scale transitions).
5. **Do firms that publish their internal adoption data (Anthropic, Stripe) outperform firms that do not, holding for sector?** This is the testable version of the "transparency is substantive" hypothesis. Proxy measurement: GitHub commit velocity, PR throughput, revenue/FTE ratio compared between disclosers and non-disclosers.
6. **Is Palantir's FDE bottleneck ("talent who can actually be deployed") the binding constraint for every firm adopting the FDE primitive?** If yes, the adaptability of this collaboration primitive is limited by the supply of FDE-capable humans — which is itself a socio-technical limit, not a technical one.

### 4.3 Weak or absent evidence flagged

- Internal-structure data for private firms beyond what has been pushed publicly is inferred, not observed. Headcount figures for Anthropic in particular diverge across sources (1,500 early 2026 vs. 2,300 end-2025 vs. ~5,000 Mar 2026). The direction (monotonic rapid growth) is H; the absolute number is M.
- "AI-first" memo adoption counts from trade press (Marketing AI Institute, etc.) are promotional and likely over-count. Treated as directional.

---

## 5. Three-pillar feed

### 5.1 Feed to Axis A (AI usage framework)
- **A1 (model transition management):** the Anthropic internal-work study shows that the same people doing the same jobs delegate progressively more (human-turns-per-task decline, tool-calls-per-task rise). Any model-switching gate needs to measure this delegation ratio as a capability-match signal. Klarna's failure was a delegation-ratio that was too high for the task complexity; Shopify's success is partly that the 360-review rubric measures delegation-ratio indirectly.
- **A2 (capability-to-adoption lag):** for the AI-native cohort (Anthropic, OpenAI, Stripe), internal capability-to-adoption lag is ~weeks, dominated by harness and eval infrastructure. For incumbents (McKinsey, Accenture), lag is months, dominated by reskilling programmes. For consumer-facing incumbents with brand/quality constraints (Klarna, Duolingo), lag is *negative* then reversed (i.e. they deploy before they are ready, then roll back).
- **A3 (workflow retooling patterns):** the Legal-Engineer and forward-deployed-engineer role families are the best observed examples of workflow retooling that scales. They combine a domain expert with a rapid-prototyper engineer around an agent harness — this is the portable pattern.

### 5.2 Feed to Axis O (organisation)
- **O2 (role redefinition cycles):** this memo produces the input material for O2's role-life-cycle model. Created roles observed across the cohort: Legal Engineer (Harvey), Applied AI Solutions Architect (Anthropic/OpenAI), Agent OS Engineer (Sierra), AI FDE (Palantir), Forward-Deployed AI Engineer (BCG X / QB). Eliminated or contracted roles: technical writer (Canva), Tier-1 CX agent (Klarna/Salesforce), junior HR ops (IBM), contractor translator/writer (Duolingo), junior analyst (consulting). Redefined without rename: software engineer (becomes reviewer + harness maintainer at Stripe / Anthropic / OpenAI).
- **O3 (organisational learning velocity):** Anthropic's published internal study is the template. Firms that can publish 200 k-transcript-level internal studies on their own AI-usage have a learning apparatus whose cadence matches the tool-turnover cadence. Firms that cannot produce even month-over-month adoption data cannot be learning at the required rate.
- **Direct O1 output:** a **four-state classification** (PR, Mixed, Substantive-but-brittle, Substantive-durable) that can be applied to any candidate firm-year by screening the Leavitt-diamond vertices for joint change and checking for an S3/S4 feedback coupling in VSM terms.

### 5.3 Feed to Axis T (technical infrastructure)
- **T1 (build vs. rent):** Anthropic, Stripe and OpenAI have all built internal agent harnesses (Claude Code + internal eval; Minions/Toolshed on Goose; Codex + harness engineering). This is a *build* decision at the harness layer regardless of *rent* at the model layer. T1's decision tree should separate the two layers.
- **T2 (compute scaling):** Cursor's path ($100 M → $500 M ARR in ~6 months at ~150 FTE) and Replit's ($2.8 M → $150 M ARR at ~70 FTE) bound the upper envelope of revenue/compute scaling; their multi-provider model routing and inference cost per seat are high-leverage input parameters for the T2 scaling-phase-transition map.
- **T3 (AI-system technical debt):** Klarna's reversal exposed AI-system debt as *brand* debt (trust loss) not only as *code* debt. This expands T3's taxonomy: technical debt in AI-native systems has a socio-technical dimension that classical tech-debt taxonomies do not capture.

### 5.4 Feed to Axis M (synthesis)
- **M1 (system-dynamics map):** the Klarna case is the archetype of a delayed-feedback pathology — fast cost-loop, slow quality-loop, with a brand-stock that integrates quality faster than management believes. This should be named as a feedback loop ("Klarna loop") in the causal diagram. The Shopify case is the archetype of a *policy-reinforced* loop — the 360-review rubric is an artificial fast-feedback signal that keeps social and technical subsystems coupled even when organic coupling would decay.
- **M2 (adaptability indicators):** the four-state classification of §3 and the signed-net-zero pattern of §3.7 are directly promotable to two candidate indicators:
    - *Leavitt-coupling score:* 0–4 based on how many diamond vertices changed jointly in a firm-year with carry-forward to the next year.
    - *Net workforce composition shift:* (gen-AI specialist hires − generalist operator layoffs) / total FTE, measured quarterly, with the sign independent of the absolute count. A firm scoring positive on this is actively restructuring around AI even when gross headcount is flat.

### 5.5 Back to the two anchor questions
- **Engineering question:** the observable engineering signature of a substantive collaboration model is (i) an internal agent harness, (ii) an internal eval suite with published delegation-ratio statistics, (iii) forward-deployed pairing of domain expert with rapid-prototyper engineer. Firms that have all three (Anthropic, Stripe, Palantir, and — with caveats — OpenAI) differ from firms that have the memo-surface but none of the three (Duolingo).
- **Managerial question:** the governance structure that functions under monthly-cadence AI capability turnover has five observable VSM properties — S1 operations with a human-AI mix at role level (not just team level); S2 coordination via shared harness, MCP, or bootcamp; S3 control that includes quality/NPS, not only cost/throughput; S4 scan via published internal-adoption data; S5 identity that states the firm's position on AI-as-substitute vs. AI-as-multiplier clearly enough that employees can falsify it. Klarna attenuated S3 in 2024 and paid for it in 2025. Shopify writes S3 explicitly into the 360 review. OpenAI's Apr-2026 restructure collapses S4/S5 into the revenue surface — we should watch whether this under-weights exploration within the same 12–24-month window that caught Klarna.

---

**End of O1 memo.** Length ~4,900 words.
