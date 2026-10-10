# M2 — Measurable Indicators of AI-Era Organizational Adaptability

> **Status:** research_memo (draft; source audit pending)
> **Date:** 2026-04-22
> **Scope:** Design a 5-7 indicator dashboard that operationally measures AI-era organizational adaptability, with reference ranges for small / mid / large organizations, explicit gaming-resistance analysis, and construct-validity notes rooted in the measurement literature.
> **Time window:** 2023-01-01 to 2026-04-22; forward reference ranges are labelled.
> **Upstream anchor:** [Research plan](../plan.md), M2 prompt in Axis M.
> **Sibling memo:** [M1 systems-dynamics map](M1-systems-dynamics-map.md). These memos were drafted independently. Indicator definitions and loop mappings still need alignment.

---

## (i) Method — what constitutes a valid adaptability indicator

### 1. The measurement problem, reframed from SDM

The three-pillar adaptability frame (AI usage × Organization × Technical infrastructure) is a **cybernetic object**: a control system that senses capability change, reconfigures internal state, and re-deploys. **Beer/Ashby's law of requisite variety** states that a regulator's variety must match the system it regulates. The measurement apparatus must span as many qualitatively distinct failure modes as the adaptation system itself can exhibit. A single KPI cannot cover A, O and T without collapsing their couplings into noise.

Four measurement-literature anchors discipline the indicator design:

1. **Kaplan & Norton (1992, 1996) — Balanced Scorecard (BSC).** "What you measure is what you get." BSC's contribution is not the four perspectives per se but the **compositional rule**: measures must cross-validate each other through a cause-and-effect logic. Each indicator must participate in a hypothesised causal chain across A, O and T, not stand alone.

2. **Campbell's law (Campbell 1976).** "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures." Implication: **any indicator in executive compensation or board reporting will be gamed**. The design task is to make the gaming observable and expensive.

3. **Goodhart's law (Goodhart 1975; Strathern 1997).** "When a measure becomes a target, it ceases to be a good measure." In 2024-2025 this played out on LMSYS Chatbot Arena, where Meta, OpenAI, Google and Amazon privately tested many model versions and published only best scores, collapsing the leaderboard's information value (collinear.ai 2024). Metrics that are *optimisable at the surface* (seat count, prompts per employee, % of employees using AI) will be gamed within one or two quarters of becoming a board metric.

4. **Construct validity (Messick 1995).** A score is valid only to the extent that its interpretation is defensible. Messick's six facets — content, substantive, structural, generalisability, external, consequential — apply directly: a "capability-to-deployment lag" score means what the dashboard claims only if what counts as "production integration" is defined, if the underlying process is observed rather than self-reported, and if the measurement does not itself degrade the thing measured (the consequential facet is Campbell/Goodhart in academic dress).

### 2. Design constraints for the adaptability dashboard

From the anchors above and the SDM lens declared in plan.md §2:

- **Pillar-spanning.** The set must place at least one sensor on each pillar (A, O, T) and at least one meta-sensor (M) on the cross-pillar coupling.
- **Variety-matched (Beer).** Indicators must distinguish the adaptability failure modes proposed in M1: overshoot reversal (Klarna-type), infrastructure rot (last year's stack), capability-shock lag (organisation too slow for model release), overcorrection churn (re-orgs that themselves get reversed). These mappings still need alignment with M1.
- **Gaming-resistant as a set.** No single metric survives Goodhart on its own; the defence is **pairing** — each surface metric paired with a counter-metric that goes the wrong way under the most obvious gaming strategy (duperrin.com 2025; kpitree.co 2025). Example: if "capability-to-deployment lag" is gamed by declaring trivial integrations as "production", the paired metric "revenue share from AI capabilities released < 6 months ago" goes down because the trivial integrations produce no revenue.
- **Construct-valid.** Each indicator has (a) an explicit formula, (b) a rule for what counts in numerator and denominator, (c) a data source path, (d) a labelled source of measurement error.
- **SD-model coupled.** Each indicator corresponds to a stock (level), a flow (rate) or a loop (ratio) variable — so the dashboard can be read as a calibration instrument for the M1 SD model, not merely a management scorecard.

### 3. Evidence hygiene rules followed in this memo

- Absolute dates, primary sources where possible, labelled speculation.
- "Benchmark" values from 2023-2026 cases are classified as one of: **disclosed** (company or regulator filing), **reported** (vendor survey, consulting report), **estimated** (analyst back-of-envelope), or **speculative** (this author's inference from adjacent data).
- Industry survey aggregates (Menlo, Ramp, McKinsey, BCG, Deloitte, Productiv/Zylo) are treated as **reported** not **disclosed** — they have non-trivial selection bias and self-reporting error, and they only give population-level priors, not firm-level benchmarks.

---

## (ii) Evidence table — candidate indicators with construct-validity notes

Each row distills what is observable, where the evidence currently sits, and what the construct can and cannot support.

### Candidate C1 — Capability-to-deployment lag (CDL)

- **Definition.** `CDL = t_prod - t_release`, where `t_release` is the public release date of a new AI capability (e.g., a major model version, a new modality, a tool-use capability) and `t_prod` is the date a specific production workflow of the focal organisation routes real user traffic through that capability.
- **Unit.** Days.
- **Data-source feasibility.** Internal: high (release/merge metadata, LaunchDarkly/feature-flag logs). External: low — organisations rarely announce integration dates with precision; engineering blogs and changelog posts are the main signal. The measurement is feasible internally but hard to benchmark cross-firm.
- **Benchmark evidence, 2023-2026.**
  - *Short-tail pole, AI-native product firms.* Cursor and other AI-powered IDEs integrated newly-released models within **48-72 hours** through Q4 2025 (vertu.com / llm-stats 2026); Perplexity integrated DeepSeek R1 on public servers within approximately two weeks of the January 2025 launch (Perplexity official X post, 29 Jan 2025). **Reported / disclosed.**
  - *Long-tail pole, regulated Fortune 500.* 42% of companies abandon most AI initiatives before reaching production, up from 17% a year earlier (sderosiaux 2025 citing MIT NANDA). 95% pilot failure rate. "Leading enterprises achieve time-to-production under 90 days; most do not." **Reported.**
  - *JPMorgan LLM Suite updates its underlying models "every 8 weeks"* (CNBC 30 Sep 2025 reporting on JPMorgan's LLM Suite). This is a firm-level benchmark for the **inverse**: how fast a large regulated enterprise can absorb each model rotation once the platform is in place — approximately 56 days. **Disclosed-through-press.**
- **Construct validity.** Moderate. The formula presumes a canonical "capability", which is unstable — each quarter introduces a new capability category (reasoning, computer-use, sub-agent tool orchestration). Operationally, the unit of analysis must be fixed per dashboard period (e.g., "new frontier reasoning model" Q1 2026 = GPT-5.2 / Claude Opus 4.5 / Gemini 3). Cross-firm comparison requires holding the capability constant.
- **Known gaming risks.** (a) Declaring a shadow-deploy (<1% traffic) as "production" to shorten the lag. (b) Choosing capabilities the firm was already well-placed for while ignoring those it lags on. (c) Selective reporting — publishing CDL only for fast integrations.

### Candidate C2 — Model-switching cost (MSC)

- **Definition.** `MSC = engineer_days` spent per major model swap, counted from decision-to-switch through production cutover and 30-day post-cutover stabilisation. Decompose into `MSC_eval + MSC_prompt + MSC_adapter + MSC_observability + MSC_customer_communication`.
- **Unit.** Engineer-days per swap (or FTE-months).
- **Data-source feasibility.** Internal only. Cross-firm: only through case studies and engineering blogs; no standardised disclosure exists.
- **Benchmark evidence.**
  - *AI-native firms:* switching between comparable frontier models in 2025 reported as "days to low weeks" in engineering blogs (Cursor, Perplexity, various agent startups). **Reported.**
  - *Mid-size AI product companies:* 1-4 engineer-weeks is a commonly cited figure in LangSmith / Braintrust / Arize case studies when a standard eval harness and observability substrate already exist; 2-6 engineer-months when the switch crosses vendor boundaries and requires prompt rework. **Estimated.**
  - *Fortune 500 with fine-tunes/adapters in production:* 6-18 engineer-months due to re-tuning, compliance re-attestation, and SRE risk review. **Speculative from adjacent data.**
- **Construct validity.** High when the eval harness and observability substrate are present (the measurement denominator is clean). Low when they are not — the MSC then includes the one-time cost of *building* the switching infrastructure, which inflates the number artificially and penalises firms at exactly the moment they are making the right investment.
- **Known gaming risks.** (a) Booking the observability/eval investment to a separate project so MSC looks low. (b) Defining "switch" so narrowly (swap `model=X` for `model=Y` and declare done) that the quality cost is externalised to customers. Counter-metric: 30-day post-switch quality regression.

### Candidate C3 — Role redefinition frequency (RRF)

- **Definition.** `RRF = formal_role_changes_per_year / (FTE / 1000)`, where a formal role change is a material change in job title, scope-of-responsibility statement, reporting line, or compensation band, documented in HRIS. Exclude pure rebranding (title change with identical scope).
- **Unit.** Changes per 1000 FTE per year.
- **Data-source feasibility.** Internal: high through HRIS. External: low — LinkedIn title changes are a proxy but conflate real restructuring with branding inflation.
- **Benchmark evidence.**
  - *Chief AI Officer prevalence:* roughly tripled over 2020-2025 on LinkedIn; projected ≥40% of Fortune 500 to hold the role by 2026 (LinkedIn 2025; pixiebrix reports 2025). **Reported.**
  - *LinkedIn Jobs on the Rise:* 70% of the fastest-growing roles were new to the list; 70% of skills used in most jobs will change by 2030 per LinkedIn workforce research. **Reported.**
  - *Klarna:* restructured to replace ~700 roles with AI in 2023-2024, then re-hired human customer-service agents from spring 2025 — a **reversed** structural change (mlq.ai 2025; tech.co 2025). The reversal is itself a data point for indicator C7 below. **Reported.**
- **Construct validity.** Mixed. RRF as defined captures both genuine adaptation and churn from bad restructuring. Must be paired with the adaptation-to-overcorrection ratio (C7) to distinguish sense-making from thrash. Rebranding inflation is a known confound; the "material change" filter is essential.
- **Known gaming risks.** (a) Title inflation — renaming Analyst to AI Analyst and counting it. (b) Rapid re-org cycles as a performative signal. Counter-metric: reversal rate (C7) and span-of-control stability.

### Candidate C4 — Technical-debt accrual rate in AI subsystems (AI-TDR)

- **Definition.** Composite of (a) **story-point accrual rate** — backlog growth of AI-specific maintenance tickets per sprint minus burn-down, (b) **eval-drift rate** — delta in continuous eval score per week against a frozen held-out eval suite, (c) **prompt/clone ratio** — % of prompt templates with substantial duplication. Standardised as a single 0-1 composite with documented weights.
- **Unit.** 0-1 composite; report sub-metrics alongside.
- **Data-source feasibility.** Internal via Jira / Linear / LangSmith / Arize / custom eval harness. External: almost none; the most-cited public evidence is aggregate (GitClear 2025, Stanford/DryRun).
- **Benchmark evidence.**
  - *GitClear 2025 "AI Assistant Code Quality":* code churn roughly doubled vs. pre-AI baseline; "copy/paste" exceeded "moved" for the first time, with a ~4× increase in clones. **Reported.**
  - *Stanford/DryRun (via multiple 2024-2025 summaries):* 87% of Copilot-authored PRs introduced at least one vulnerability category. **Reported.**
  - *Anthropic / LangChain / Braintrust engineering content 2025:* "silent regressions" when teams ship without complete re-evaluation — treated in the field as the dominant AI-systems technical-debt pattern. **Reported.**
- **Construct validity.** High within a firm over time; low across firms (different definitions of "AI ticket", different eval suites). This is an **internal management** indicator primarily, with cross-firm comparison only in category terms (debt high / medium / low).
- **Known gaming risks.** (a) Burning down backlog by ticket closure without remediation. (b) Rewriting the eval suite to match current behaviour (erasing drift by moving the goal posts — a direct Goodhart instance). (c) Excluding "AI" from the ticket label to keep the denominator small. Counter-metric: external incident rate (C5 below) and a quarterly independent eval.

### Candidate C5 — Fresh-AI revenue share (FAR)

- **Definition.** `FAR = revenue_from_AI_features_released_in_last_6_months / total_revenue` in the same period. Operationally: revenue attributable via pricing, monetised SKUs, or attribution to AI-routed traffic to capabilities that did not exist 6 months prior.
- **Unit.** Percentage.
- **Data-source feasibility.** Internal: medium (requires clean attribution). External: low — most firms do not disclose, and definitions vary. Microsoft is the exception, disclosing AI revenue trajectory (datacenterdynamics 2024; news.microsoft.com 2025-07-30): Microsoft AI business reached ~$13B annualised run rate at Q2 FY26, up 175% YoY. Vendors now selling $19B of AI applications in enterprise (Menlo 2025 report). **Disclosed / reported.**
- **Benchmark evidence.**
  - *Enterprise AI market:* $37B enterprise AI investment in 2025, triple 2024 (Menlo Ventures 2025, press release 2025-12-09). **Reported / disclosed.**
  - *Stripe top-100 AI companies:* 11.5-month median from launch to $1M ARR, ~4 months ahead of the fastest SaaS cohort; 55 countries covered in year 1 vs. 25 for SaaS (Stripe "Indexing the AI Economy", 2025-2026). **Disclosed-through-press.**
  - *Cross-firm FAR for non-AI-native firms:* almost no disclosure. Fortune 500 earnings-call hits on "AI revenue" are rising but rarely quantified. **Negative evidence.**
- **Construct validity.** Moderate. Captures adaptation *output* better than any other candidate — the firm is demonstrably turning capability change into revenue. But attribution is fragile: the counterfactual ("would the customer have paid without AI?") is usually not testable.
- **Known gaming risks.** (a) Attribution inflation — routing existing revenue through an AI-labelled SKU. (b) Re-launching existing features with an "AI" badge and resetting the 6-month clock. Counter-metric: net-new customer share within FAR, and retention of AI-SKU customers at month 12.

### Candidate C6 — Time-to-workflow-redesign after capability shock (TWR)

- **Definition.** `TWR = t_redesign_live - t_capability_shock`, where `t_capability_shock` is the publication date of a capability release that, on the SD model (M1), crosses a threshold that makes the prior workflow dominated (cost-parity or quality-parity with a substantially different workflow), and `t_redesign_live` is when the redesigned workflow is the default for the target user population (≥50% of the relevant workload).
- **Unit.** Days.
- **Data-source feasibility.** Internal: high with workflow-level instrumentation. External: low — only visible in case-study reporting.
- **Benchmark evidence.**
  - *PepsiCo PepGenX:* NPD cycle compressed from 6-9 months to 6 weeks over 2022-2025 after generative AI was integrated into formulation workflows (AI Magazine; cited in repo `ai-adoption-timing.md`). **Reported.**
  - *Mondelez:* 3-year → <12-month development cycles; 80% time reduction over 2020-2025 (Chief AI Officer Blog; repo source). **Reported.**
  - *Klarna reversal:* capability-shock redesign went the other way — ~12-18 months from "AI handles 75% of chats" (Feb 2024) to re-hiring humans into a hybrid workflow (spring 2025). **Reported.**
- **Construct validity.** High *when the threshold is pre-specified*; low otherwise, because organisations rationalise post-hoc which capability "triggered" the redesign. Requires the SD model (M1) to name the thresholds in advance.
- **Known gaming risks.** (a) Declaring a micro-redesign as "live" to shorten TWR. (b) Under-scoping the user population to hit ≥50% quickly. Counter-metric: quality and throughput of the redesigned workflow at 90 days.

### Candidate C7 — Adaptation-to-overcorrection ratio (AOR)

- **Definition.** `AOR = structural_changes_reversed_within_12_months / total_structural_changes` in a rolling 24-month window. "Structural change" includes: formal re-org, vendor swap in AI stack, major policy (AI usage policy, data governance regime), and AI-driven role consolidation. "Reversed" = returning to within 20% of the pre-change state on the relevant dimension.
- **Unit.** Ratio, 0-1.
- **Data-source feasibility.** Internal: medium (requires a maintained change log). External: only the most visible reversals are documented.
- **Benchmark evidence.**
  - *Klarna:* 2023-2024 AI-replacement → 2025 partial reversal. **Reported.**
  - *Microsoft Recall:* May 2024 default-on launch → June 2024 opt-in reversal → delayed launch, all within ~30 days (CNBC 2024). **Reported.**
  - *Google AI Overviews:* May 2024 launch at 84% SERP presence → reduced to 15% by mid-2024 after "glue pizza" class errors (BrightEdge; Washington Post 2024). **Reported.**
  - *Industry aggregate:* 42% of companies abandon most AI initiatives before production; 40% of agentic AI projects expected to be cancelled by 2027 (Gartner 2025). These are project-level, not pure "reversals", but they populate the denominator. **Reported.**
- **Construct validity.** High as a trailing leading indicator of governance quality — high AOR signals reactive rather than anticipatory adaptation. Low when the change-log is ad-hoc; the indicator *is* the change-log discipline.
- **Known gaming risks.** (a) Never formally declaring changes so nothing can be reversed. (b) Re-categorising reversals as "further evolution" to avoid the reversal count. Counter-metric: changes per year (pair with C3) — if RRF → 0 while AOR → 0, the organisation is simply inert.

### Candidates considered and dropped or merged

- **"% employees using AI / seat count" — dropped.** Menlo 2025 reports ~78% enterprise adoption; Ramp March 2026 puts business adoption at 50.4%. Saturating, prone to vanity inflation, and cannot distinguish productive use from shadow use (67% of employees use unsanctioned AI per Productiv/Zylo 2026). Retained as context, not scored.
- **"Time-to-first-AI-pilot" — dropped.** Saturated post-2025; no remaining discriminatory power.
- **"Compute cost per revenue dollar" — merged into C5** as an efficiency sub-metric.
- **"Eval-drift rate" — merged into C4** as a sub-metric of AI-TDR.

---

## (iii) Pattern findings

### F1. The dashboard shape that survives Goodhart is not a scorecard, it is a paired-control instrument

Seven candidates reduce to seven through merging, but the discriminating structure is the **pairing**. Each indicator has a partner that goes the wrong way under its most obvious gaming strategy:

| Primary | Paired counter-metric | Gaming strategy the pair defeats |
|---|---|---|
| C1 CDL | C5 FAR (same capability window) | "Trivial shadow-deploy" — produces no revenue, so the pair does not improve together. |
| C2 MSC | C4 AI-TDR 30-day post-switch delta | "Swap and ship without eval" — inflates tech-debt visibly. |
| C3 RRF | C7 AOR | "Re-org theatre" — reversals become visible. |
| C4 AI-TDR | External incident rate + quarterly independent eval | "Move the goal posts on evals" — independent eval catches the delta. |
| C5 FAR | Retention of fresh-AI customers at month 12 | "AI-badge revenue" — churns out at month 6-12. |
| C6 TWR | Quality / throughput of redesigned workflow at 90 days | "Micro-redesign claim" — no throughput delta. |
| C7 AOR | C3 RRF | "Never formally change" — RRF → 0, flags inertia. |

The paired design is the **variety-match** (Beer) the individual metrics cannot achieve on their own.

### F2. Three indicators carry cross-pillar load; the other four are single-pillar sensors

- **Cross-pillar (M-sensor):** C1 CDL (A×T — capability routing into prod), C6 TWR (A×O — capability routing into workflow), C7 AOR (O×M — governance loop quality).
- **Single-pillar with cross-pillar tributaries:** C2 MSC (T, with A input), C3 RRF (O), C4 AI-TDR (T, with A input), C5 FAR (A output, gated by O and T).

A minimal dashboard must keep at least one of the cross-pillar indicators and at least one on each single pillar. The recommended **5-indicator minimum core** is **{C1, C2, C3, C4, C5}** — one cross-pillar (C1), one T (C2 and C4), one O (C3), one A output (C5). The **7-indicator full dashboard** adds C6 (cross-pillar A×O) and C7 (governance loop, M-sensor).

### F3. Indicators align to SD stocks, flows, and loops

Forward-linking to M1's expected variables:

| Indicator | SD role | SD variable it calibrates |
|---|---|---|
| C1 CDL | Delay (in days) | Delay on the capability-ingestion edge from A-pillar to T-pillar |
| C2 MSC | Inverse flow rate | T-pillar architectural churn rate; high MSC = low churn capacity |
| C3 RRF | Flow rate | O-pillar role-change flow into/out of the role stock |
| C4 AI-TDR | Stock + slow-leak rate | T-pillar debt stock (the B1 loop in system-dynamics-ai-adoption.md §3) |
| C5 FAR | Flow rate | Revenue flow from the fresh-capability stock; proxy for R1 reinforcement |
| C6 TWR | Delay (in days) | Delay on the capability-ingestion edge from A-pillar to O-pillar |
| C7 AOR | Loop-gain ratio | Gain of the overcorrection balancing loop vs. the adaptation reinforcing loop |

Once M1 exists, this mapping lets the dashboard double as a **calibration suite** for the SD simulation: each indicator's time series provides a data-point for one structural parameter of the model. This is the BSC "cause-and-effect across perspectives" discipline applied to an SD substrate.

### F4. Benchmarks exist only for the tails; the middle is statistical dark matter

Two poles are well-documented: the AI-native short tail (48-72 hours integration at Cursor; 1-2 weeks at Perplexity; Stripe top-100 AI ventures monetising in ~11.5 months) and the aggregate long tail (42% abandon pre-production; 95% pilot failure rate; 40% agentic-project cancellation expected by 2027). The **middle** — mid-market AI product companies and Fortune 500 with substantive deployments — is poorly measured publicly. Reference ranges for mid- and large-org tiers in the dashboard below are constructed from adjacent data and labelled `Estimated` or `Speculative`.

### F5. Campbell's law operates most strongly on the easiest-to-aggregate metric

C5 FAR is the most likely board metric because it is monetary and legible. It is therefore the most likely to be gamed. The counter-metric discipline (retention of fresh-AI customers, net-new customer share within FAR) must be **pre-committed** — not added after gaming is observed — or the indicator will degrade in the same way the LMSYS Chatbot Arena did in 2024-2025.

### F6. The 2023-2026 record shows more overcorrection than under-adaptation

Across the documented cases (Klarna AI-to-human reversal; Microsoft Recall launch-to-delay; Google AI Overviews 84% → 15% SERP share; Humane AI Pin $230M loss followed by HP acquisition; Rabbit R1 critical failure; 42% abandon-rate pre-production), the dominant failure mode is not "waiting too long" but "deploying too structurally, too fast, on inadequate evidence." This promotes C7 AOR to first-class status: the adaptability question is not just "can you move fast" but "can you move fast without thrashing." In the three-pillar frame this is the meta-stability constraint on A-O coupling.

---

## (iv) Open questions and negative evidence

### Open questions

1. **CDL unit-of-analysis instability.** What counts as "a capability" in a world where capabilities arrive faster than categories stabilise? Candidate answer: define a rolling-quarter capability taxonomy (e.g., MLCommons / Epoch / ARC-AGI v2 / Stanford HELM) and report CDL per current taxonomy row. Needs work.

2. **Cross-firm comparability of MSC and AI-TDR.** Both indicators are internally consistent but not standardised. A consortium benchmark (the AI-era equivalent of DORA metrics for DevOps) does not yet exist at the time of writing. **Negative evidence:** searches for a "DORA-for-AI" standard returned vendor whitepapers (Arize, LangSmith) and consultant frameworks (Drata, Tredence) but no multi-firm publicly-benchmarked dataset.

3. **Attribution validity of FAR.** The counterfactual ("what would revenue have been without this AI capability?") is almost never empirically available. Alternative framings: feature-level A/B attribution, AI-SKU gross margin, retention on AI-only customer cohorts. Each has its own gaming surface.

4. **Threshold specification for TWR.** Without pre-specified thresholds, "capability shock" is defined after the fact by whichever capability release was followed by the redesign. M1 SD model must name thresholds prospectively for TWR to be valid.

5. **The small-organisation tier is thinly populated in the evidence base.** Stripe's AI-startup data is informative for *AI-native* small firms but not for traditional small businesses adopting AI. Ramp's 50.4% adoption figure for small US businesses (Ramp AI Index, March 2026) gives a population rate but no firm-level benchmark for the dashboard indicators.

### Negative evidence — what was looked for and not found

- **No firm-level public disclosure of MSC.** Companies do not publish engineer-days per model switch. The closest public artefact is engineering blog posts with directional language ("took us a quarter", "couple of sprints") — not numeric disclosure.
- **No cross-firm RRF benchmark.** LinkedIn data on title changes is aggregate; ADP, Mercer and Willis Towers Watson publish workforce analytics but do not break out AI-driven role-change rates in public summaries.
- **No standard AI technical-debt disclosure format.** Unlike SOC 2 or CMMI, there is no common reporting standard. The AI observability market ($2.69B 2026 → $9.26B 2030 projection per `ai-governance-measurement.md`) is growing into this gap but has not produced an industry-wide metric standard.
- **No public reversal counter (AOR equivalent).** Reversals are narratively famous (Klarna, Microsoft Recall, Google AI Overviews) but no trade publication aggregates them numerically.

These gaps define the measurement research agenda for the Pillar-M thesis track.

---

## (v) Three-pillar feed — which indicator senses which pillar

| Indicator | Pillar sensor | Proposed loop mapping (M1 alignment pending) | What the indicator *does* in the three-pillar frame |
|---|---|---|---|
| C1 CDL | A ↔ T | Capability-ingestion delay (A → T edge) | Measures whether the technical substrate routes new capability into production fast enough to keep up with the external clock set by A. |
| C2 MSC | T (with A input) | T-pillar architectural churn resistance | Measures whether the technical infrastructure is built for swap (low MSC) or built-in to a specific vendor generation (high MSC). |
| C3 RRF | O | O-pillar role-change flow | Measures whether the organisation is structurally moving people/roles at the pace the external capability clock demands. |
| C4 AI-TDR | T (with A input) | B1 balancing loop gain (per SD paper §3) | Measures the slow-burn cost of the fast-gain R1 loop — if AI-TDR is rising, R1 is outrunning the org's ability to absorb the debt B1 is accumulating. |
| C5 FAR | A output (gated by O and T) | R1 reinforcing loop output | Measures whether the adaptation is producing revenue, not just activity. Without FAR, the dashboard cannot distinguish real adaptation from theatre. |
| C6 TWR | A ↔ O | Workflow-redesign delay (A → O edge) | Pairs with C1 on the organisational side: the analogous delay, but on workflows rather than infrastructure. |
| C7 AOR | O ↔ M | Overcorrection balancing loop gain | Measures whether the adaptation system is oscillating or converging — the meta-stability sensor for the whole three-pillar controller. |

**Coverage check.** The 7-indicator dashboard places at least one primary sensor on each of A, O, T, and on two M-couplings (A×T, A×O). The governance meta-loop is covered by C7. No pillar is dark. Per BSC cause-and-effect logic, the dashboard tells a causal story: fresh capability enters via C1, infrastructure absorbs it (C2, C4), organisation re-forms around it (C3, C6), revenue follows (C5), and C7 gates the whole thing against thrash.

---

## Dashboard specification (primary output artifact)

**Cadence legend.** W = weekly, M = monthly, Q = quarterly, H = half-yearly. All indicators reported with a 13-period rolling history.

**Scale tiers.** Small = <200 FTE; Mid = 200-5,000 FTE; Large = >5,000 FTE. Ranges are labelled `Estimated` (from adjacent data), `Reported` (from the evidence base) or `Speculative` (extrapolation where direct data is absent).

| # | Indicator | Formula | Unit | Sensor (A/O/T/M) | Data source | Cadence | Small org ref | Mid org ref | Large org ref | Gaming risk | Countermeasure |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Capability-to-deployment lag (CDL)** | `t_prod − t_release` for the defined capability list of the current quarter | days | A↔T (M) | Feature-flag logs, deploy metadata, changelogs | W | 2-14 (Reported: Cursor, Perplexity class) | 14-90 (Estimated) | 56-180 (Reported: JPMorgan 8-week cycle; 90+ days for most Fortune 500) | Shadow-deploy declared as prod; selective reporting on easy capabilities | Pair with C5 FAR on the same capability; require ≥1% traffic through the capability for CDL to count |
| 2 | **Model-switching cost (MSC)** | Engineer-days from switch decision to 30-day post-cutover stabilisation, decomposed by sub-cost | engineer-days | T | Jira / Linear exports, CI/eval logs | Q or per-event | 5-20 (Estimated) | 20-120 (Estimated) | 120-500 (Speculative; some regulated firms 500+) | Booking eval/observability investment off-book; over-narrow "switch" definition | Pair with AI-TDR 30-day delta; independent technical audit once per year |
| 3 | **Role redefinition frequency (RRF)** | `material_role_changes / (FTE/1000) / year`; material = ≥1 of {title + scope, reporting line, comp band} with documented scope change | changes / 1000 FTE / year | O | HRIS change log | Q | 5-40 (Estimated; young firms re-org continuously) | 15-60 (Estimated) | 10-40 (Estimated; Fortune 500 restructure is lumpy but lower per-FTE) | Title inflation; re-org theatre | Pair with C7 AOR; exclude pure rebranding via scope-change filter |
| 4 | **AI technical-debt accrual rate (AI-TDR)** | Composite of {backlog growth of AI tickets, weekly eval-drift, prompt-clone %} standardised to 0-1 with documented weights | 0-1 composite | T | Jira / Linear, LangSmith / Arize, static code analysis | M | 0.1-0.4 (Estimated) | 0.2-0.5 (Reported: GitClear-level clone/churn doubling) | 0.3-0.6 (Speculative; legacy estates carry higher baseline) | Ticket re-labelling; eval-suite revision to hide drift | External independent eval quarterly; lock-version eval-suite baseline |
| 5 | **Fresh-AI revenue share (FAR)** | `revenue_from_AI_features_released_<6_months_ago / total_revenue` | % | A (output), gated by O and T | Product analytics, finance attribution | Q | 10-40% (Reported: Stripe top-100 AI-native) | 2-15% (Estimated) | 0.5-5% (Reported: Microsoft ~$13B AI run rate is a small but fast-growing share; most Fortune 500 <1%) | AI-badge re-labelling; attribution inflation | Report month-12 retention of fresh-AI customers alongside FAR; disclose the attribution rule |
| 6 | **Time-to-workflow-redesign (TWR)** | `t_redesign_live(≥50% of target pop) − t_capability_shock` using pre-specified thresholds | days | A↔O (M) | Workflow instrumentation, product analytics | Q | 14-90 (Reported: AI-native) | 60-270 (Reported: PepsiCo PepGenX 2022-2025; Mondelez 2020-2025 category of cycle change) | 180-720 (Reported: consulting data; "change at speed of org, not tech", Deloitte 2026) | Under-scoping target population to hit 50% quickly | Require 90-day throughput and quality delta as co-condition |
| 7 | **Adaptation-to-overcorrection ratio (AOR)** | `structural_changes_reversed_within_12_months / total_structural_changes` over rolling 24 months | 0-1 ratio | O↔M | Change log, re-org / policy audit trail | H | 0.10-0.40 (Speculative; young firms iterate fast) | 0.10-0.25 (Speculative) | 0.05-0.20 (Reported: visible reversals — Klarna, Recall, Overviews — are a small fraction of total structural changes in large firms) | Never formally declaring changes; re-categorising reversals as "further evolution" | Pair with C3 RRF; external disclosure of reversal events with root-cause class |

**Read-out rule.** The dashboard is read as a set, not individually. A high CDL with a low FAR is the *infrastructure rot* pattern. A low CDL with a high AOR is the *thrash* pattern. A low RRF with a high AI-TDR is the *silent rot* pattern. A high FAR with a high AOR is the *growth built on over-promises* pattern (Klarna 2024 state). Etc. Management action is triggered by pattern, not by a single threshold — this is the BSC cause-and-effect discipline and the Beer variety-matching principle in one frame.

---

## Three-pillar closing note

This memo operationalises the two anchor questions from plan.md §1 into observable form:

- **Engineering anchor** ("how is the technical infrastructure designed and built"): sensed by C1, C2 and C4.
- **Managerial anchor** ("what operational and governance structures are required for it to function effectively"): sensed by C3, C6 and C7.
- **Coupling between the two** is read off as the pattern across the whole dashboard, not as any single metric.

The dashboard is deliberately thin (5-7 indicators) and paired (each primary has a counter-metric). It is designed as a **sensing instrument for the M1 SD model** once that model exists — and as a fallback, it stands on its own as a Kaplan-Norton-style balanced scorecard specifically engineered for AI-era three-pillar coupling.

---

## Sources

### Measurement literature
- Kaplan, R. S., & Norton, D. P. (1992). "The Balanced Scorecard—Measures that Drive Performance." *Harvard Business Review*. https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2
- Kaplan, R. S., & Norton, D. P. (2007). "Using the Balanced Scorecard as a Strategic Management System." *Harvard Business Review*. https://hbr.org/2007/07/using-the-balanced-scorecard-as-a-strategic-management-system
- Kaplan, R. S., & Norton, D. P. *Conceptual Foundations of the Balanced Scorecard*. Harvard Business School Working Paper 10-074. https://www.hbs.edu/ris/Publication%20Files/10-074_0bf3c151-f82b-4592-b885-cdde7f5d97a6.pdf
- Goodhart, C. (1975). Re-stated in Strathern, M. (1997). "Improving ratings: audit in the British University system." *European Review* 5(3): 305-321.
- Campbell, D. T. (1976). "Assessing the Impact of Planned Social Change." *Evaluation and Program Planning*.
- Messick, S. (1995). "Validity of Psychological Assessment." *American Psychologist* 50(9): 741-749.
- Sterman, J. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World.* McGraw-Hill / Irwin.
- Ashby, W. R. (1956). *An Introduction to Cybernetics.* — law of requisite variety.
- Beer, S. (1972). *Brain of the Firm.* — viable system model, cybernetic measurement.
- Duperrin, B. (2025-08-07). "Do you know Goodhart's law on KPIs and measurement?" https://www.duperrin.com/english/2025/08/07/goodhart-law-kpi/
- KPI Tree (2025). "Goodhart's Law and metric design." https://kpitree.co/guides/frameworks/goodharts-law
- Collinear.ai blog (2024). "Gaming the System: Goodhart's Law Exemplified in AI Leaderboard Controversy." https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy
- Practical DevSecOps (2025). "Goodhart's Law in AI." https://www.practical-devsecops.com/glossary/goodharts-law/

### Enterprise AI adoption benchmarks
- Menlo Ventures (2025-12-09). "2025: The State of Generative AI in the Enterprise." https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- Menlo Ventures (2025-12-09). Press release: "Enterprise Investment Hit $37B in 2025, Tripling in One Year." https://www.globenewswire.com/news-release/2025/12/09/3202258/0/en/Menlo-Ventures-2025-State-of-Generative-AI-Report-Enterprise-Investment-Hit-37B-in-2025-Tripling-in-One-Year.html
- Menlo Ventures 2025 PDF (direct). https://menlovc.com/wp-content/uploads/2025/12/menlo_ventures_enterprise_ai_report-2025-123125.pdf
- Ramp (2026). "Ramp AI Index." https://ramp.com/data/ai-index
- Ramp (2026-03). "Ramp AI Index March 2026 update." https://ramp.com/leading-indicators/ai-index-march-2026
- Ramp (2026-04). "Ramp AI Index April 2026 update." https://ramp.com/leading-indicators/april-2026-ai-index
- Ramp (2026). "Introducing our Spring 2026 Business Spending Report." https://ramp.com/reports/2026-spring-spending-benchmarks
- Stripe (2025). "Indexing the AI Economy." https://stripe.com/guides/indexing-the-ai-economy
- Stripe. "Inside the growth of the top AI companies on Stripe." https://stripe.com/blog/inside-the-growth-of-the-top-ai-companies-on-stripe
- McKinsey (2025). "The State of AI." https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- BCG (2025). "Are You Generating Value from AI? The Widening Gap." https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap
- Deloitte (2026). "State of AI in the Enterprise — 2026 AI report." https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html
- Gartner (2025-06-25). "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027." https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- Productiv / UC Today (2026). "What Do the Best AI Productivity Reports Reveal in 2026?" https://www.uctoday.com/productivity-automation/ai-productivity-reports-2026/
- Zylo (2026). "2026 SaaS Management Index: How AI Is Reshaping SaaS Costs." https://zylo.com/reports/2026-saas-management-index/

### Case-study benchmarks (2023-2026)
- CNBC (2025-09-30). "JPMorgan Chase: fully AI-connected megabank." https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html
- Perplexity (2025-01-29). X post announcing DeepSeek R1 integration. https://x.com/perplexity_ai/status/1883913343854923989
- Vertu (2025). "AI model race timeline: Grok 4.1, Gemini 3, Claude Opus 4.5, GPT-5.2." https://vertu.com/lifestyle/the-ai-model-race-reaches-singularity-speed/
- LLM Stats (2026-04). "AI Updates Today — April 2026." https://llm-stats.com/llm-updates
- Sderosiaux, S. (2025-12). "What Changed in Q4 2025 and Why Enterprises are afraid of 2026-2027." https://sderosiaux.medium.com/what-changed-in-q4-2025-and-why-enterprises-are-afraid-of-2026-2027-ccd4e632baae
- MLQ (2025). "Klarna CEO admits AI job cuts went too far." https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/
- Tech.co (2025). "Klarna Reverses AI Customer Service Replacement." https://tech.co/news/klarna-reverses-ai-overhaul
- CNBC (2024-06-14). "Microsoft to delay launch of AI Recall tool due to security concerns." https://www.cnbc.com/2024/06/14/microsoft-to-delay-launch-of-ai-recall-tool-due-to-security-concerns.html
- Washington Post (2024-05-24). "Google's AI search feature was mocked for telling users to eat rocks and make pizza with glue." https://www.washingtonpost.com/technology/2024/05/24/google-ai-overviews-wrong/
- TechCrunch (2025-02-18). "Humane's AI Pin is dead as HP buys startup's assets for $116M." https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m/
- GitClear (2025). "AI Assistant Code Quality Research." https://www.gitclear.com/ai_assistant_code_quality_2025_research
- AI Magazine. "How PepsiCo's AI strategy is dominating consumer goods." https://aimagazine.com/articles/how-pepsicos-ai-strategy-is-dominating-consumer-goods
- Chief AI Officer Blog. "Mondelez AI recipe development 80% faster." https://chiefaiofficer.com/blog/mondelez-ai-recipe-development-80-percent-faster/
- MIT Sloan Management Review. "How Procter & Gamble uses AI to unlock new insights from data." https://sloanreview.mit.edu/article/how-procter-gamble-uses-ai-to-unlock-new-insights-from-data/

### Role redefinition and organisational data
- LinkedIn (2025). "Rise in number of chief AI officers." https://www.linkedin.com/news/story/rise-in-number-of-chief-ai-officers-5981036/
- LinkedIn News (2025). "LinkedIn Welcomes Deepak Agarwal as New Chief AI Officer." https://news.linkedin.com/2025/linkedin-welcomes-deepak-agarwal-as-new-chief-ai-officer
- PixieBrix (2025). "Top Chief AI Officers of 2025." https://www.pixiebrix.com/reports/top-ai-officers-of-2025
- InformationWeek (2025). "How Will the Role of Chief AI Officer Evolve in 2025?" https://www.informationweek.com/machine-learning-ai/how-will-the-role-of-chief-ai-officer-evolve-in-2025-

### AI technical debt and eval drift
- Anthropic. "Demystifying evals for AI agents." https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Braintrust. "What is LLM evaluation? A practical guide to evals, metrics, and regression testing." https://www.braintrust.dev/articles/llm-evaluation-guide
- LangChain. "LLM Evals: Production Monitoring to Regression Tests." https://www.langchain.com/articles/llm-evals
- arXiv (2024). "Evaluation-Driven Development and Operations of LLM Agents." https://arxiv.org/html/2411.13768v3
- arXiv (2025). "Evaluation and Benchmarking of LLM Agents: A Survey." https://arxiv.org/html/2507.21504v1

### AI revenue disclosure
- Microsoft (2026-01). "FY26 Q2 Press Release / Webcast." https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/press-release-webcast
- Microsoft Source (2025-07-30). "Microsoft Cloud and AI strength fuels fourth quarter results." https://news.microsoft.com/source/2025/07/30/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results/
- Data Center Dynamics. "Microsoft on track for $10bn in annual revenue from AI inference." https://www.datacenterdynamics.com/en/news/microsoft-on-track-for-10bn-in-annual-revenue-from-ai-inference/

### Internal repo cross-references
- `research/adaptability-framework/plan.md` — M2 prompt source; three-pillar anchor questions.
- `research/ai-systems/papers/ai-governance-measurement.md` — observability as measurement architecture; layered L1-L5 sensor frame.
- `research/ai-systems/papers/system-dynamics-ai-adoption.md` — R1/B1 loop structure that C4 AI-TDR and C5 FAR calibrate.
- `research/cross-cutting/papers/ai-adoption-timing.md` — canonical case studies (Mondelez, JPMorgan, P&G, PepsiCo, Adobe, Salesforce, Klarna, Humane, Rabbit, Google Overviews).
- `research/cross-cutting/papers/research-market-gap-analysis.md` — market-research contradictions informing gaming-risk analysis.
- `research/productization-skills/papers/metr-productivity-paradox.md` — objective-vs-perceived gap informing C4 construct validity.
