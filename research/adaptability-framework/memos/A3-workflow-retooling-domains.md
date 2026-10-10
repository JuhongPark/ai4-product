# A3 — Workflow retooling patterns across knowledge-work domains

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Prompt:** A3 (Axis A, Pillar 1 — AI Usage Framework, adaptability lens)
> **Date:** 2026-04-22
> **Window:** 2023-01 through 2026-04
> **Relation to anchor questions:** Workflow redesign is where the engineering pillar (how AI is built into the flow) meets the managerial pillar (who owns the work, at what cadence, under what governance). Domain retooling velocity is a leading indicator of three-pillar coupling.

---

## (i) Method

**Research object.** The *daily workflow of a knowledge worker* — the ordered sequence of sub-tasks performed on a standard unit of work (contract review, patient encounter, research note, pull request, client deck). The question: how was that artifact rebuilt between 2023-01 and 2026-04 as foundation-model capability shifted across six generations (GPT-3.5 → 4 → 4o → o-series → 5; Claude 2 → 3 → 3.5 → 4 → 4.7).

**Unit of analysis.** (domain, company, year, workflow change) — each row in section (ii) is one identifiable workflow delta with a date, a named deploying organisation, and a description of what changed.

**Evidence sources.** Vendor case studies (OpenAI, Anthropic, Microsoft, Epic, Harvey), partner press (A&O Shearman, Paul Weiss, Kaiser, Morgan Stanley, JPMorgan, Goldman Sachs), engineering blogs (Anthropic, Shopify, Stripe), practitioner surveys (Thomson Reuters *Future of Professionals Report* 2024, 2025; Deloitte *State of GenAI in the Enterprise*), field experiments (Dell'Acqua et al. 2023 BCG-Harvard; METR 2025–2026), and regulator filings (FTC *DoNotPay* 2024–2025; Rule 11 sanction orders in the Charlotin hallucination database).

**Frames applied.**
- *Socio-technical systems* (Trist, Emery) — score each change on whether it redesigned the technical **and** social subsystems jointly, or only one side.
- *Lifecycle redesign* — treat workflow change as a lifecycle event (concept, deployment, steady state, obsolescence), not a one-shot migration.
- *Ambidextrous organisation* (O'Reilly & Tushman) — exploitation of the legacy flow and exploration of the AI-augmented flow usually proceed in parallel; track where that parallelism was preserved vs. collapsed.
- *Retooling velocity* — the primary quantitative metric: **substantive workflow redesigns per domain per year**. Secondary: capability-to-retooling lag and redesign cost in engineering-months or disclosed dollars.

**Substance vs. cosmetics.** Following Trist, a *substantive* retooling ("re-plumbed") shows at least two of: (1) sub-task sequence changes; (2) authoring locus moves; (3) downstream artifacts change shape; (4) role allocation across humans changes. A sidebar chatbot that the worker does not structurally depend on is scored *cosmetic* ("renamed").

**Big-bang vs. continuous.** *Big-bang* flips a full user population to the new workflow inside a single quarter with a hard cutover. *Continuous* introduces the new tool alongside legacy practice and diffuses by opt-in over multiple quarters. Hybrids are labeled.

**Confidence labels.** **Strong** = multiple primary sources + quantitative outcome data; **moderate** = one primary source + consistent secondary coverage; **weak** = single vendor-authored or self-reported source.

**Scope guardrails.** No "best practice" claims without a mechanism argument. Regulated vs. unregulated patterns held separate. Vendor time-savings numbers reported as *self-reported* unless an external RCT or independent measurement is cited.

---

## (ii) Evidence table — row per (domain, company, year, workflow change)

All dates are absolute. "Self-reported" marks vendor or partner claims without independent verification.

| # | Domain | Organization | Date | Workflow change | Mode | Substance | Source class |
|---|--------|--------------|------|-----------------|------|-----------|--------------|
| L1 | Legal | Allen & Overy + Harvey + Microsoft | 2023-11 (launch) → 2024-01 (external launch via ContractMatrix) | First-draft and clause-review authoring moved from associate-led Word markup to Harvey/GPT-4 Word-add-in draft + lawyer edit; rolled out to 3,500+ A&O lawyers internally before external release. Self-reported ~7 hours saved per contract negotiation. | Continuous (internal pilot, then opt-in rollout, then client product) | Re-plumbed (sequence, locus, role allocation all changed) | Firm + vendor PR |
| L2 | Legal | PwC + Harvey + OpenAI | 2023-03 (alliance) → 2023-04 (rollout to ~4,000 PwC lawyers in 100+ countries) | Regulatory-compliance Q&A, due-diligence extraction, and contract triage moved from junior-associate manual review to Harvey-first workflow with human QA; initial 12-month contract. | Big-bang at the population level (4,000 lawyers in weeks) with opt-in usage inside | Re-plumbed | Firm + vendor PR |
| L3 | Legal | Paul Weiss + Harvey | 2023-01 (testing) → 2024-06-11 (Workflow Builder launch) | Firm became lead design partner for Harvey *Workflow Builder*; turned repeatable diligence tasks into parameterised templates that embed firm precedent and guardrails. | Continuous (18-month co-design) | Re-plumbed (authoring locus shifted; templates become the unit of practice) | Firm + vendor PR |
| L4 | Legal | Harvey (platform) | 2025-03 (Agents) → 2026-03 (platform scale) | Harvey moved from single-turn Q&A to agentic multi-step workflows; by 2026-Q1 the platform hosted >25,000 custom agents across >1,300 organizations and >100,000 lawyers; firm raised at $11B valuation 2026-03. | Continuous at the ecosystem level | Re-plumbed (introduces agent orchestration above the workflow layer) | Vendor PR + press |
| L5 | Legal | A&O Shearman + Harvey | 2025-04 | First publicly disclosed profit-share arrangement with a legal-AI vendor — a *business-model* change that follows the workflow change. | Continuous | Re-plumbed (governance + commercial model) | Artificial Lawyer |
| L6 | Legal | Evisort + Workday | 2024 (acquisition) | Standalone contract-intelligence CLM absorbed into an enterprise suite; CLM function rebranded Workday Contract Intelligence. | Big-bang in org terms | Mixed: technically re-plumbed, but for many customers the daily legal-ops workflow changed only at the edges. | M&A / vendor |
| L7 | Legal | DoNotPay | 2024-09 FTC complaint → 2025-02 final order | "AI lawyer" consumer product found to not meet professional-lawyer standard; $193,000 fine, remedial notice to past subscribers. *Negative evidence* — an entire market segment (B2C AI legal help) retraced in 2024–2025. | Big-bang reversal | Re-plumbed in reverse | FTC primary |
| L8 | Legal | US federal courts (all firms) | 2023-06 (*Mata v. Avianca*) → 2025-08 (three sanctions in two weeks) | *Negative evidence* — hallucinated citations produced by AI tools generated an expanding docket of Rule 11 sanctions, pushing firms to impose human-verification checklists on top of AI drafting; >300 logged hallucination incidents by 2025. Workflow change: mandatory citation-verification step re-added. | Continuous (and reactive) | Re-plumbed (explicit new review gate) | Court filings + Charlotin database |
| M1 | Medical | Nuance / Microsoft + Epic (DAX Copilot) | 2024-01-18 (GA embedded in Epic) → 2024-Q3 (150+ health systems committed) | Clinical documentation moved from post-visit typing to ambient capture + draft note in Haiku mobile app; self-reported 70% reduction in burnout, 50% reduction in documentation time, ~7 min saved per encounter. | Big-bang at the vendor level (Epic-native GA); continuous at the clinician level (voluntary opt-in by encounter) | Re-plumbed | Nuance + Epic PR |
| M2 | Medical | Kaiser Permanente + Abridge | 2024-08 announcement (40 hospitals, 600+ offices, ~24,000 physicians across 8 states + DC) | Largest single-health-system ambient-AI rollout to that date; Kaiser described it as "the largest implementation to date of ambient listening technology." | Big-bang at the system level | Re-plumbed | Kaiser + Abridge PR |
| M3 | Medical | UPMC + Abridge | 2025 | Enterprise-wide rollout to 12,000 clinicians. | Big-bang | Re-plumbed | Abridge PR |
| M4 | Medical | Emory Healthcare + Abridge (Inside for Emergency Medicine) | 2025-01 | Emergency-medicine ambient documentation with Epic ASAP integration; first clinical adoption of an ED-specific ambient product. | Continuous (domain extension) | Re-plumbed | Abridge PR |
| M5 | Medical | Epic (platform) | 2024-Q1 → 2025-08 UGM | Epic launched *Art* (clinician-facing), *Emmie* (patient-facing), *Penny* (revenue cycle). CEO Faulkner disclosed 160–200 AI projects; MyChart In-Basket ART generated >1M drafts monthly across 150+ orgs. | Continuous at the platform level | Re-plumbed (sustained platform-level flow redesign) | Epic + Microsoft |
| M6 | Medical | OpenEvidence | 2024-07 (≈358k physician consultations / month) → 2025-07 (≈8.5M / month; 40% of US physicians registered; 65k new clinicians/month) | Evidence-retrieval step moved from UpToDate-style manual lookup to LLM-over-peer-reviewed-literature; July 2025 *DeepConsult* adds reasoning-agent flow for multi-paper synthesis. | Continuous (bottom-up physician adoption) | Re-plumbed | Company + PubMed |
| M7 | Medical | Ambience Healthcare | 2024 (Epic Toolbox) → 2025-Q4 ($243M Series C, $1.25B valuation) | Specialty-aware ambient scribing embedded in Haiku/Hyperspace; competes with DAX and Abridge on specialty coverage and coding depth. | Continuous | Re-plumbed | Company + Epic PR |
| M8 | Medical | Suki AI | 2025 (3× usage growth, 400+ organizations, Epic Toolbox, Suki INSIDE, ICD-10/CPT auto-coding) | Documentation + coding compressed into single AI step; self-reported 48% reduction in amended encounters. | Continuous | Re-plumbed | Suki year-in-review |
| M9 | Medical | Aidoc — Advocate Health | 2024-10 (22 sites, Wisconsin + North Carolina) | aiOS platform triages acute findings on CT/MRI/X-ray; vendor-neutral EHR/PACS integration. | Continuous (site-by-site) | Re-plumbed (workflow adds algorithmic triage step upstream of radiologist worklist) | Advocate PR |
| M10 | Medical | Aidoc — WellSpan Health | 2025 (nine hospitals, 250+ care locations, >200k cases, >10k critical findings surfaced in 12 months) | Full enterprise scaling across all hospitals after pilot. | Big-bang at expansion | Re-plumbed | WellSpan PR |
| M11 | Medical | Radiology field (negative evidence) | 2024–2025 systematic reviews | *Negative evidence* — 41% of radiologists say available AI tools don't address real-world needs; 63% concerned about bias; PACS lacks correction tooling; "meaningful integration remains limited" in UK NHS despite majority-of-departments uptake. | — | *Cosmetic* in many sites (pilot without workflow re-plumbing) | Mayo Clinic Proceedings: Digital Health; *Lancet eClinicalMedicine* scoping review |
| M12 | Medical | Mount Sinai | 2024 | NutriScan AI malnutrition risk scoring deployed across 5 additional hospitals; Hearst Health Prize 2024. | Continuous | Re-plumbed (adds a new triage step upstream of dietitian consult) | Mount Sinai PR |
| M13 | Medical | Cleveland Clinic | 2024–2025 | NLP chart abstraction in oncology; AKASA revenue-cycle automation; Ambience + Bayesian + IBM partnerships; new CAIO appointed. | Continuous | Re-plumbed | Cleveland Clinic PR |
| F1 | Finance | Morgan Stanley (Wealth Mgmt) + OpenAI — *AI @ Morgan Stanley Assistant* | 2023-09 launch → by 2025 at 98% advisor-team active use | Research-retrieval moved from manual search across 350k+ documents (30+ minutes per query) to seconds-scale chatbot lookup. | Continuous | Re-plumbed | Morgan Stanley press + OpenAI case study |
| F2 | Finance | Morgan Stanley — *Debrief* | 2024-03 pilot → 2024-06 firmwide → 2025 at 98% advisor adoption | Meeting-note-taking, CRM logging, email drafting moved from human post-meeting activity to AI-listener + advisor edit; self-reported ~30 min saved per meeting, up to 15 hours/week per advisor. | Continuous | Re-plumbed | Morgan Stanley |
| F3 | Finance | Morgan Stanley — *AskResearchGPT* | 2024 | Institutional Securities equity-research lookup moved to GPT-4-powered synthesis of proprietary research corpus. | Continuous | Re-plumbed | Morgan Stanley |
| F4 | Finance | JPMorgan — *LLM Suite* | 2024 launch → 2024-08 200k users in 8 months → 2026 ~230k employees globally; *Innovation of the Year* (American Banker) 2025 | Enterprise-wide general-purpose LLM for drafting, summarization, analysis; horizontal rollout, not workflow-specific. | Big-bang at the population level | Mixed — horizontal usage without re-plumbing specific desks leaves many workflows *renamed* rather than *re-plumbed* | JPMorgan press |
| F5 | Finance | Goldman Sachs — *GS AI Assistant* + Devin | 2025 Q2 firmwide GS AI Assistant after 10k-employee pilot → 2025-07-11 Devin pilot alongside ~12,000 human engineers, projected 3–4× productivity | Coding workflow moving to AI-agent drafting with human supervision for legacy modernisation. | Continuous (hybrid-workforce framing) | Re-plumbed (on the coding track); Assistant is mixed | CNBC, IBM Think |
| F6 | Finance | Bloomberg — BloombergGPT + Terminal | 2023-03 model release → 2024-01-22 AI-powered earnings-call summaries GA on Terminal → 2024-07 mobile/Vision Pro → 2026 expanded Terminal AI tool | Analyst-read-the-transcript workflow replaced by AI summary; 400 Bloomberg Intelligence analysts trained the model. | Continuous | Re-plumbed | Bloomberg press + Institutional Investor |
| F7 | Finance | Hebbia | 2024 Series B ($130M, $700M valuation) → 2025 billion-page processing; BlackRock, Carlyle, Centerview among users; used by 40% of largest asset managers by AUM | Due-diligence, CIM, IC-memo production moved from analyst-heavy multi-day cycle to agent-first draft with minutes-scale turnaround; self-reported 30–40 hrs saved per deal (banking), 20–30 hrs per deal (PE). | Continuous (firm by firm) | Re-plumbed | Company + OpenAI case study |
| F8 | Finance | Bridgewater — AIA Labs | 2023 *Artificial Investment Associate* → 2024 ~$2B fund run by ML with OpenAI / Anthropic / Perplexity models | Fundamental-systematic research workflow encoded inside a reasoning-engine product; human investment associates reoriented to design and QA. | Big-bang for the new fund; continuous for the rest of the firm | Re-plumbed | Bloomberg + Bridgewater |
| F9 | Finance | BlackRock Aladdin, S&P, Moody's (assumed based on industry patterning) | 2024–2025 | *Lower-confidence* row: each added LLM-based features atop existing platforms, but publicly disclosed workflow changes remain thin; treated as renaming-dominant unless better evidence lands. | — | Likely *cosmetic*–mixed | Weak — note uncertainty |
| F10 | Finance | Klarna | 2024-02 announcement of AI handling ~700 FTE-equivalent customer-service work → 2025 reversal; CEO Siemiatkowski: "We went too far." | *Negative evidence* — a big-bang replacement reversed to a blended Uber-style human+AI model after complaint and satisfaction metrics deteriorated. | Big-bang → reversal | Re-plumbed twice | CEO on record, multiple outlets |
| S1 | Software | Shopify + GitHub Copilot | 2022-01 early access → 2023–2024 cultural core → 2025-03 ~1M lines of code written with Copilot in aggregate → 2025-04 *Reflexive AI Usage* memo by CEO Lütke | Pair-programming moved to AI-first drafting; *pre-hire* justification now requires the team to demonstrate why AI cannot do the job. | Big-bang (cultural mandate) after years of continuous build-up | Re-plumbed (including hiring policy) | GitHub discussion + Shopify memo leaked and confirmed |
| S2 | Software | GitHub Copilot (platform) | 2024–2025 | 15M total users by early 2025; 20M by 2025-07; 1.3M paid subs; 90% of Fortune 100; self-reported 55% task-completion speedup; PR time 9.6 → 2.4 days in vendor data. | Continuous at the platform level | Re-plumbed across the user base | GitHub + Microsoft |
| S3 | Software | Cursor | 2024–2025 | By 2025-Q2 >half of Fortune 500 had developers on Cursor; $1B ARR in 2025; adopted across Stripe, Shopify, Uber, Spotify, OpenAI, Nvidia; Patrick Collison (Stripe) publicly reported R&D spend up but headcount ratio down. | Continuous at the platform level | Re-plumbed (IDE, not sidebar; workflow is AI-first) | Cursor + Stripe on record |
| S4 | Software | Cognition Devin + Goldman Sachs, Infosys, Visma | 2024-Q4 launch → 2025-06 ~$73M ARR → 2025-07 Goldman Sachs pilot → 2025 Infosys global deployment | Legacy-code migration moved from engineering-month human work to agent-hours; self-reported 10–14× speed-up for migration tasks; 2× faster, 2× less resource, 67% merged-PR rate at Anthropic-adjacent benchmarks. | Continuous at customer level; big-bang at Infosys | Re-plumbed | Cognition reports + Microsoft customer story + IBM Think |
| S5 | Software | Anthropic — Claude Code internal usage | 2025-02–2025-08 | Anthropic surveyed 132 engineers / researchers; transcripts using Claude to implement new features grew 14.3% → 36.9%; planning-and-design transcripts 1.0% → 9.9%; majority of Anthropic code now written by Claude Code. | Continuous | Re-plumbed (TDD, architecture-first, orchestration of multiple agents) | Anthropic internal study |
| S6 | Software | Anthropic Economic Index | 2025-11 → 2026-02 | Coding migrated from Claude.ai to first-party API; ~79% of business interactions on API automation-dominant; coding remains the single largest usage category (~35% of Claude.ai traffic). | — | Ecosystem-level re-plumbing of where coding work happens | Anthropic Economic Index |
| S7 | Software | METR field study of experienced OSS developers | 2025-07 (v1 report, 16 devs, 246 tasks, -19% speed) → 2026-02 (v2, 57 devs, 800+ tasks, -4% with CI [-15%, +9%]) | *Negative evidence early, regression later* — AI tooling *slowed* experienced OSS developers on mature projects in v1; v2 sample correction substantially attenuated the finding. Perception gap persisted: devs *thought* they were 20% faster. | — | Workflow-level: re-plumbing without productivity gain in the short run | Primary RCT |
| C1 | Consulting | McKinsey — *Lilli* | 2023-07 firmwide launch → 2024 | 72% active users; 500k+ prompts/month; ~17 uses/week per consultant; self-reported ~30% time savings on search/synthesis; ~50,000 labour hours/month recovered; auto-generated decks/proposals ≈1/3 of all usage, 90–120 min saved per invocation. | Continuous (but firmwide) | Re-plumbed | McKinsey Tech & AI |
| C2 | Consulting | BCG — *GENE* | 2024-09 public launch; GPT-4o-based; wide-context architecture instead of RAG | Story-line brainstorming, podcast co-hosting, interview preparation compressed into a single chatbot flow. | Continuous | Mixed — some workflows re-plumbed, some *renamed* | BCG press |
| C3 | Consulting | BCG — internal AI agent buildout | 2023-09 Anthropic alliance → 2024-09 >6,000 AI agents built by BCG staff | Individual consultants build task-scoped agents; re-plumbing is decentralised. | Continuous | Re-plumbed at agent level, mixed at workflow level | BCG |
| C4 | Consulting | BCG-HBS *Jagged Frontier* field experiment | 2023-09 publication | 758 BCG consultants; inside-the-frontier tasks: +12.2% completed, -25.1% time, +40% quality; outside-the-frontier tasks: ~23% worse for AI-assisted workers who did not critique; "cyborg" vs "centaur" archetypes emerge. | Not a deployment — an RCT inside the firm | — | *Nature Human Behaviour* working paper |
| C5 | Consulting | Bain + OpenAI | 2022 (quiet collab) → 2023 public alliance → 2024-10 *OpenAI Center of Excellence* | Client-delivery workflow explicitly co-produces deliverables with OpenAI engineers (e.g., Coca-Cola, Amgen, retail shelf-planning). | Continuous | Re-plumbed (delivery org co-staffed) | Bain press |
| C6 | Consulting | OpenAI Frontier Alliances | 2026-02-23 | Formal alliance with McKinsey, BCG, Accenture, Capgemini; split of mandate between strategy/operating model (MBB) and integration/lifecycle (SI). | Big-bang (alliance form) | Workflow implications emerging | OpenAI press |
| C7 | Consulting | Deloitte *AI Factory* + Zora AI | 2024–2025 | Invoice processing, trend analysis automated via agentic tooling; *State of GenAI in Enterprise* 2026 reports 70% of enterprises expect "AI factory" scaling by 2028; budget 3–4× growth expected. | Continuous | Re-plumbed on operations; mixed on audit | Deloitte reports |
| C8 | Consulting | Accenture GenAI | 2023–2026 | Internal GenAI studio + Frontier-Alliance integration work; large-scale training programs. | Continuous | Mixed | Accenture + press |
| C9 | Consulting | Big-Four audit platforms | 2024–2025 | EY *EY.ai* + *EYQ* (80,000 tax pros, 3M+ compliance cases/yr); PwC *Aura* + *GL.ai*; KPMG *Ignite* (announced $2B over 5 yrs, $12B revenue target); Deloitte *Omnia* + Zora. | Continuous | Re-plumbed (anomaly detection, document extraction), mixed on sign-off (regulatory hold) | Consultancy.uk + firm press |

---

## (iii) Pattern findings

### Cross-domain patterns (transferable)

**P1. Re-plumbing travels through the application layer; it stalls at the sign-off layer. [strong]**
In every domain, the top of the workflow — retrieval, drafting, summarisation, note generation, extraction — moved to AI-first cadence inside eighteen months of GPT-4 GA (2023-03). The bottom — the adjudicated sign-off step where a licensed professional puts their name to the artifact — moved slower or not at all. Evidence: Harvey drafts, signing partner verifies (L1–L5); DAX/Abridge/Ambience draft, attending physician signs (M1–M8); Morgan Stanley *Debrief* drafts, advisor sends (F2); Epic Art drafts, clinician finalises (M5); Big-Four audit platforms flag, audit partner signs (C9). Mechanism: liability and regulatory gates are *epistemic bottlenecks* compressed into human professional-standing roles. Structurally predicted by the Dell'Acqua "jagged frontier" finding (C4).

**P2. Continuous integration dominates inside regulated domains; big-bang shows up most often at the *population* level of an unregulated vendor deployment. [strong]**
Medical (M1–M13), legal (L1–L5), finance (F1–F8) all follow pilot → refine → scale inside each organisation. Big-bang occurs *across the population* (PwC flipping 4,000 lawyers in weeks; Kaiser rolling Abridge to 24,000 physicians across 8 states; JPMorgan 200k users in 8 months) *but inside each workflow* individual workers opt in encounter-by-encounter. True inside-workflow big-bang appears only outside regulated domains: Shopify's April-2025 *Reflexive AI Usage* memo (S1); Klarna's 2024 customer-service replacement (F10), later reversed. Regulated-domain organisations *do not* do inside-workflow big-bangs.

**P3. AI champions + centre-of-excellence + vendor partnership is the dominant operating model; pure internal builds remain rare. [strong]**
Across all 47 rows, the modal model is (a) named executive champion + (b) cross-functional AI CoE + (c) primary external vendor: Paul Weiss + Harvey (L3); Bain + OpenAI CoE (C5); Kaiser + Abridge (M2); Morgan Stanley + OpenAI (F1); BCG + Anthropic (C3). Pure internal builds (Bridgewater AIA (F8), BloombergGPT (F6), Epic platform AI (M5)) are the exception and occur where the firm already has platform ownership or scientific-staff depth. Managerial implication: the CoE-plus-vendor template is the *steady state* for regulated knowledge work, not a transition.

**P4. Retooling velocity clusters by domain in a clear rank order. [moderate]**
Crude 2023-01 → 2026-04 counts of substantive workflow redesigns per thousand professionals per year:

| Domain | Retooling velocity | Evidence |
|---|---|---|
| Software engineering | **very high** (multiple IDE-scale redesigns in 36 months; Copilot → Cursor → Devin) | S1–S7 |
| Consulting / knowledge services | **high** (Lilli, GENE, Bain-OpenAI, 6,000+ BCG agents) | C1–C9 |
| Finance | **medium-high** on client-facing tier; **medium** on trading/risk | F1–F10 |
| Legal | **medium** (blocked at sign-off; accelerating 2025–2026 via agents) | L1–L8 |
| Medical | **medium-low** overall, **high** in ambient documentation specifically | M1–M13 |

Ordering maps onto (a) where liability sits relative to the workflow, (b) whether the upstream interface is text-native. Software and consulting have soft sign-off gates (PR review, partner review) and text-native artifacts — both favour fast retooling. Medical and legal have hard liability gates — retooling accumulates upstream of the gate but not at it.

**P5. Retooling velocity is sold as a productivity claim but measured as an adoption claim. [strong]**
Publicly disclosed numbers split into (a) self-reported time savings (7 hrs/contract at A&O; 15 hrs/week at Morgan Stanley; ~30% at McKinsey; 70% burnout reduction at Nuance) and (b) adoption rates (98% at Morgan Stanley, 72% at McKinsey, 90% of Fortune 100 on Copilot). External measurement is sparse: BCG-HBS (C4, +12.2% tasks, -25.1% time, -23% outside-frontier) and METR (S7, -19% v1, -4% v2) are the main RCT-grade points. For M2: current industry reporting treats adoption and productivity as interchangeable; they are not.

**P6. Re-plumbing vs. renaming is most cleanly observed by authoring locus. [moderate]**
Mechanical test: *who presses the button that produces the first draft of the day's unit of work?* If the worker, it's a sidebar; if the AI, it's re-plumbed. Medical ambient docs (M1–M8), Morgan Stanley Debrief (F2), Harvey Workflow Builder (L3), and agent-based coding (S4) pass. Horizontal assistants (JPMorgan LLM Suite F4, much of GENE C2) remain *renamed* in many users' flows.

### Domain-locked patterns

**P7. Legal — citation-verification is a new mandatory sub-task, not a cosmetic checklist. [strong]**
Following *Mata v. Avianca* (2023-06) and the expanding sanction docket (L8), virtually every major firm inserted an explicit human-verification step for AI-generated citations. Structurally a *new* sub-task, forced by Rule 11 and state-bar rules. Contrast: clinicians also verify AI documentation, but the verification is subsumed in the existing sign-off step — no new step is added.

**P8. Medical — EHR integration is the choke point; EHR vendors become workflow-design oligopolists. [strong]**
Abridge, Nuance DAX, Ambience, and Suki all compete on depth of Epic (and, to a lesser extent, Oracle) integration (M1–M8). Epic's platform-layer moves (M5) shape the space in which all ambient-scribe vendors operate. Not seen in legal (Harvey is document-platform-agnostic), finance (Hebbia is multi-tenant), or software (Cursor is IDE-level). Implication: medical retooling velocity is upper-bounded by the EHR vendor's release cadence.

**P9. Finance — horizontal general-purpose assistants dominate; workflow-specific re-plumbing is concentrated in wealth management and research. [moderate]**
JPMorgan *LLM Suite* (F4) and industry counterparts read as horizontal LLM rollouts. Genuine re-plumbing is most advanced in (a) wealth-advisor note generation (F1, F2), (b) research-analyst synthesis (F3, F6), (c) investment-banker deliverable production (F7). Trading-desk and risk-management workflows, tightly coupled to existing quant models, re-plumb more slowly.

**P10. Software — the IDE is the workflow edit surface; once the IDE becomes AI-native, retooling velocity in the domain detaches from the rest of the organisation. [strong]**
Cursor's 2024–2025 rise (S3): an AI-native IDE sweeps through an engineering org independent of any firmwide AI programme. Stripe's Patrick Collison on record: R&D spend up, headcount ratio down — the *economics* of the role changed, not just the tool. Anthropic's internal study (S5) shows the next phase: engineers orchestrating multiple agents in parallel. Not observed in any other domain here.

**P11. Consulting — the firm's proprietary corpus becomes the most valuable single input to the rebuilt workflow. [moderate]**
Lilli (C1) pulls from 100,000+ documents across 40+ sources. GENE (C2) embeds proprietary research via wide context instead of RAG. Bain's OpenAI CoE (C5) and BCG's 6,000+ agents (C3) are infrastructure on top of an existing corpus. Workflow redesign as a *corpus-mobilisation event* — domain-locked because consulting firms have uniquely large internal-knowledge-to-deliverable ratios.

**P12. Regulated domains have a different adaptability envelope. [strong]**
Three strands converge: (a) retooling-velocity ranking (P4) puts medicine and law below software and consulting; (b) sign-off-gate stickiness (P1) is severe in medicine and law; (c) big-bang is absent inside regulated workflows (P2). The *envelope* — changes a domain can absorb per quarter — is narrower for medicine and law by roughly the time-constant of their liability systems. Not a maturity gap to close; a design constraint the three-pillar redesign has to work from. For the engineering anchor: regulated-domain infrastructure and governance must assume retooling velocity is bounded by the sign-off system, not the capability curve of the model.

---

## (iv) Open questions / negative evidence

**Q1. Rework cost is poorly measured.** Almost no firm publishes engineering-months or FTE-weeks taken to unwind a retooling. Klarna (F10) is the cleanest public reversal; DoNotPay (L7) the cleanest regulator-forced one. Everything else is announced without public correction. *Reversal rate* — a leading indicator for M2's "adaptation-to-overcorrection ratio" — is near-unmeasurable from public data.

**Q2. The "renamed vs. re-plumbed" ratio is not systematically tracked.** Horizontal rollouts (F4, C2, parts of C9) claim population coverage but publish no telemetry on whether daily task sequences changed. The right instrument is behavioural telemetry from the work surface (IDE, EHR, CRM, draft-authoring platform) — which Anthropic does internally (S5) and Shopify reportedly does for Copilot. Elsewhere the data is missing.

**Q3. Where are the middle-market cases?** Evidence concentrates on the largest firms (AmLaw 100, 20+ hospital systems, global banks, MBB). Middle-market firms (50–500 professionals) are under-represented; the adaptability envelope (P12) likely behaves differently there because CoE-plus-vendor is hard to sustain below a certain headcount.

**Q4. Negative evidence is uneven across domains.** Legal: loud (sanctions, DoNotPay, hallucination docket). Medical: quieter but present (PACS gaps, radiology trust deficit). Finance: Klarna is the main reversal; other failures mostly undisclosed. Software: METR is the unusual piece of negative evidence; most other reporting is vendor-flavoured. Consulting: negative evidence almost entirely inside the BCG-HBS jagged-frontier finding (C4). Loud negative evidence yields faster guardrails (legal added citation-verification within months); quiet negative evidence accumulates latent risk.

**Q5. Cross-domain learning is almost nonexistent in public evidence.** Harvey learns from Harvey customers; Abridge from Abridge customers. Cross-domain playbooks — e.g., the citation-verification-step pattern adapted to medical discharge summaries — are not visible. Unclear whether absence is real or reporting-driven.

**Q6. OpenAI *Frontier Alliances* (2026-02-23, C6) is too recent to score.** The split (MBB = strategy/operating model; SI = integration/lifecycle) will reshape consulting retooling in 2026–2027. Re-score in the A3 update in twelve months.

**Q7. Role redefinition is coupled to workflow retooling but scoped to O2.** Paul Weiss's "AI Director," Harvey's "Workflow Builder designer" role, Goldman's "Devin supervisor," Kaiser's clinical-AI champions — all belong in O2 but feed back into A3's velocity estimate.

---

## (v) Three-pillar feed

### A (AI usage)

- **Substance test** for workflow claims: authoring-locus shift + task-sequence change + role-allocation change — use to de-inflate vendor time-savings claims.
- **Retooling-velocity ranking** by domain (P4) inverts into a decision input for A1: in high-velocity domains the test-validation pipeline has to be continuously rebuilt.
- **Sign-off-gate model** (P1) defines where A1's swap-or-stay decision must hold invariant: the model under the gate must pass the gate's professional-liability test, not only the capability test.

### O (organisation)

- Confirmation that the **AI-champion + CoE + vendor** template is the steady state (P3); O2's role-lifecycle model should encode it as persistent structure, not a transition state.
- A **regulated-domain adaptability envelope** (P12) bounds O3's learning-velocity expectations for medical / legal / finance orgs.
- **Big-bang is a cultural tool, not an operational one** (P2): inside-workflow big-bang is rare but deployed for signalling (Shopify memo; JPMorgan LLM Suite; Kaiser-Abridge). O1 can interpret these as CEO-level ambidexterity signals.

### T (technical infrastructure)

- **Choke-point map**: EHR vendor (medical), document platform + agent orchestrator (legal), research-data provider + CRM (finance), IDE + agent runtime (software), proprietary-corpus indexer (consulting). T1's build-vs-rent framework should be instantiated per choke-point.
- **Platform-lock hypothesis**: Epic's 160–200 AI projects make it a workflow-design oligopolist for medicine (P8). T1 should model platform-decoupling cost as a first-class variable.
- **Agent-layer inflection signal**: Harvey Agents (L4), Devin (S4), Epic agentic AI (M5), BCG's 6,000+ agents (C3) — 2025–2026 is when agent orchestration moves from demo into production. T3 should add *agent-orchestration debt* as a category (ownership, versioning, retirement).

### M (meta) — feeds for synthesis

- **M1 loop seed.** A reinforcing loop between *retooling velocity* and *sign-off-gate pressure*: more upstream AI adoption → sign-off becomes the bottleneck → liability compresses into it → gate gets more cautious → next-iteration velocity dampens.
- **M2 indicator seeds.** (a) *re-plumb ratio* = re-plumbed / total rows per domain per year; (b) *reversal rate* = documented reversals / total rollouts; (c) *adoption-productivity divergence* = self-reported adoption minus externally-measured productivity delta — exploitable because both numbers are routinely reported.

---

*End of A3.*
