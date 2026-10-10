# A1 — Foundation model transition management (2022–2026)

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Date:** 2026-04-22
> **Time window:** 2022-11 (ChatGPT launch) → 2026-04 (Claude Opus 4.7 era; GPT-4o retirement)
> **Anchor questions:**
> - Engineering: how is the technical infrastructure for an AI-based decision-making system designed and built?
> - Managerial: what operational and governance structures are required for it to function effectively in an organization?

---

## (i) Method

**Object of study.** A *foundation-model transition* is any production event in which the primary LLM powering a decision or customer-facing capability is (a) upgraded in place to a new version from the same provider, (b) swapped to a different provider, (c) extended by routing part of the traffic to a new model, or (d) rolled back after a failed transition. The unit of analysis is the transition event, not the product.

**Data sources.**
- Vendor customer stories (OpenAI, Anthropic, Google Cloud, AWS).
- Engineering blogs (Shopify, Airbnb, Abridge, Harvey, Replit, Intercom).
- Practitioner reporting (Pragmatic Engineer, VentureBeat, TechCrunch, Fortune, CNBC, CIO Dive, Legal IT Insider).
- Corporate press releases, SEC-adjacent disclosures (Duolingo investor relations).
- Regulatory / legal artefacts (Moffatt v Air Canada BC CRT ruling 2024-02-14).
- Practitioner aggregation (ZenML LLMOps Database "What 1,200 production deployments reveal").

**Selection criteria.** Sixteen transition events across eleven organizations were retained if they (i) involved a production-facing AI capability, (ii) had a dateable transition or non-transition decision 2022–2026, and (iii) had at least one primary-source citation. Regulated-domain cases (healthcare: Abridge, Nuance DAX; finance: Morgan Stanley, JPMorgan; legal: Harvey, CoCounsel) were over-sampled relative to their share of public cases, because the adaptability frame is stress-tested most severely where compliance and audit weight constrain fast iteration.

**Analytical lens (MIT SDM frameworks applied).**
- **DSM (Design Structure Matrix)** for switching interfaces: prompts, evals, tools, retrieval pipelines, provider SDKs, and governance gates are treated as coupled elements; the *switching cost* is a function of how tightly these couple to the specific model.
- **STS (socio-technical systems)** for decision-authority analysis: each transition has a technical decision (which model, which eval bar) and a social decision (who signs off, who is accountable if it fails).
- **STAMP (Leveson)** for failure analysis: failures are read as control-structure breakdowns — missing constraints, missing feedback, missing authority — not as individual model errors.
- **Dynamic capabilities (Teece)** for the "sense-seize-transform" lens on why firms differ in how fast they switch.
- **Real options** for build-vs-stay decisions under capability uncertainty.

**Limits.** Engineering-months are mostly indirectly reported. Where public figures were not available, I infer a range from the scale of the rollout and the reported elapsed time; inferences are labelled.

---

## (ii) Evidence table — 16 transition events across 11 organizations

| # | Org | Product | Transition | Date | (a) Trigger | (b) Validation / gating | (c) Engineering-months (est.) | (d) Decision authority | (e) Failures during/after |
|---|-----|---------|-----------|------|-------------|-------------------------|-------------------------------|------------------------|----------------------------|
| 1 | Klarna | AI Assistant | None → GPT-4 class (OpenAI) | 2024-02-13 launch; 2024-02-27 results | CEO mandate to AI-first; Siemiatkowski framed Klarna as OpenAI's "guinea pig" [1](https://blog.pragmaticengineer.com/klarnas-ai-chatbot/) | Prod traffic metric (resolution time 11 min → <2 min); 2.3M convos in month 1 equiv. 700 FTE [2](https://openai.com/index/klarna/) | Inferred 4–8 eng-months to first launch; not publicly disclosed | CEO Sebastian Siemiatkowski (top-down) [1](https://blog.pragmaticengineer.com/klarnas-ai-chatbot/) | Policy hallucinations on refund / fee edge cases; quality drop on complex disputes; prompt-injection system-prompt disclosure; partial public rollback May 2025 — CEO acknowledged "lower quality" and re-hired human agents in Uber-style gig model [3](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396) [4](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/) |
| 2 | Intercom | Fin 1 | None → GPT-4 (OpenAI) | 2023-03 (4 months after GPT-4 release) | Capability leap from GPT-3.5 → GPT-4 made multi-turn resolutions viable; OpenAI partnership [5](https://openai.com/index/intercom/) | Offline eval of deflection rate; piloted against Resolution Bot baseline | Inferred ~4 eng-months (explicitly stated "4 months" build [6](https://www.dkmeco.com/en/how-did-intercom-use-100-million-and-gpt-4-to-build-the-hit-ai-customer-service-fin-in-4-months/)) | Co-founders (Des Traynor public face); CEO decision | Lower resolution rate than later Claude version (~23% vs 51% with Claude) |
| 3 | Intercom | Fin 2 | GPT-4 → Claude 3.5 Sonnet (Anthropic) | 2024-10-12 | Performance in internal bake-off; "Claude delivers" per Des Traynor; competitive pressure around a major version release [7](https://thelettertwo.com/2024/10/12/intercom-releases-fin-2-ai-agent-switching-anthropic-from-openai/) [8](https://claude.com/customers/intercom) | Comparative eval across thousands of customers and millions of conversations; resolution rate benchmarked (51% avg. vs original ~23%) | Not disclosed; inferred 3–6 eng-months given the partnership depth and custom tooling | Des Traynor (Chief Strategy Officer / co-founder) publicly owned the call | None disclosed; managed as a planned major release, not incident-driven |
| 4 | Intercom | Fin | GPT-4 → GPT-4.1 (in-family upgrade) | 2025 (post GPT-4.1 release) | Improvements in "instruction handling and function execution" [5](https://openai.com/index/intercom/) | Intercom says migration from GPT-4 → GPT-4.1 was completed "in just a few days" [5](https://openai.com/index/intercom/) | ~0.1–0.5 eng-months (days, small team) | Engineering leadership; continuation under existing governance | None publicly reported |
| 5 | Intercom | Fin Apex 1.0 | Claude Sonnet 4 → post-trained in-house vertical model on open-weights base | 2025-11 | Vertical-model thesis: "age of vertical models is here"; resolution-rate competition (73.1% vs 71.1% for GPT-5.4 and Claude Opus 4.5) [9](https://venturebeat.com/technology/intercoms-new-post-trained-fin-apex-1-0-beats-gpt-5-4-and-claude-sonnet-4-6) | Benchmarked on Intercom's own customer-service suite; 2M weekly conversations as production corpus | Multi-quarter R&D; undisclosed, inferred 12–24 eng-months for post-training stack + evals | Product + ML Research (Fergal Reid lineage); CEO level strategic bet | Transparency cost — base open-weights base not disclosed; customer trust question about a self-graded benchmark |
| 6 | Shopify | Sidekick | Pre-LLM → Claude Sonnet 4.5 on Vertex AI | First rollout 2023-07, mature agentic architecture by 2025 | Director of Applied AI Andrew McNamara chose Claude for "right balance between response speed and output quality" on Google Cloud Vertex AI [10](https://claude.com/customers/shopify) | Multi-stage: Ground Truth Sets (GTX) with ≥3 expert annotators; LLM-judge calibration (Kappa 0.02 → 0.61 against human 0.69); user simulator replays; N-stage gated rewards (syntactic + semantic) [11](https://shopify.engineering/building-production-ready-agentic-systems) | Not disclosed; inferred 18–30+ eng-months across the Sidekick platform (multi-year, ~ICML-2025-paper scale) | Director of Applied AI; architecture decisions at platform layer (LLM proxy routes Claude/OpenAI/Google) | Reward hacking (opt-out hacking, tag hacking); schema violations (hallucinated IDs, wrong enums) — published post-deployment [11](https://shopify.engineering/building-production-ready-agentic-systems) |
| 7 | Harvey | Core legal assistant + Agents | OpenAI-exclusive → multi-model (OpenAI + Anthropic + Google) | 2025-05-13 announcement [12](https://www.harvey.ai/blog/expanding-harveys-model-offerings) | Internal BigLaw Bench showed "seven models" outperforming original Harvey stack; Gemini 2.5 Pro best at drafting, o3 best at pre-trial, Claude 3.7 Sonnet close second — no single best model [12](https://www.harvey.ai/blog/expanding-harveys-model-offerings) [13](https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/) | BigLaw Bench (proprietary) + expert evaluation (lawyers rate preference, tone, style); public leaderboard promised | Inferred 6–12 eng-months to re-architect around multi-model routing; bench-build effort amortized over prior year | CEO Winston Weinberg publicly owned; OpenAI retained as investor & key collaborator — explicit signalling of non-rupture | None disclosed; the strategic cost is political (first OpenAI-backed unicorn publicly diversifying) more than technical |
| 8 | Harvey | Reasoning workflows | GPT-4-class → OpenAI o1 (reasoning) | 2024-09 [14](https://www.harvey.ai/blog/harvey-building-legal-agents-and-workflows-with-openai-s-o1) | o1 scored game-changing uplift on Harvey's leading indicators (expert preference, BigLaw Bench) | Step-change review across "reasoning, planning, collaboration"; domain-gap still acknowledged ("glimpses... nascent") | Inferred 2–4 eng-months for integration, plus ongoing alignment work with OpenAI | Legal + ML research leadership; Partnership-level with OpenAI | Domain-reasoning ceiling — o1 generalizes poorly to legal work without dataset curation; Harvey and OpenAI co-built domain data |
| 9 | Zendesk | AI Agents | GPT-4 → GPT-4o | 2024-05 (within 24h of OpenAI release) [15](https://www.zendesk.com/newsroom/articles/gpt-4o/) | Not separately disclosed | "Advanced LLM benchmarking and flexible deployment model" tuned for latency / cost / quality; test-to-deploy < 24h | ~0.03 eng-months (single-day cutover) for model swap at gateway; years of prior investment in benchmarking rig | Engineering / AI platform team under standing governance; no individual-call escalation | None reported; the case is an existence proof that gateway + prebuilt evals collapse switching cost |
| 10 | Morgan Stanley | AI @ Morgan Stanley Assistant + Debrief | Pre-LLM search → GPT-4; Debrief adds Whisper+GPT-4 | Assistant launched 2023-09; Debrief 2024-06 [16](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch) [17](https://openai.com/index/morgan-stanley/) | Not separately disclosed | Firm-built "eval framework to test every AI use case before deployment"; Debrief used curated evaluation datasets of meeting-type scenarios; compliance review | Inferred 6–12 eng-months for Assistant, 4–6 for Debrief (layered on existing stack); heavy compliance effort | COO / Head of Wealth Mgmt AI (Jeff McMillan lineage); compliance + legal have hard veto; 98% advisor adoption post-rollout | None public; failures are structurally absorbed by human-in-the-loop (advisor edits Debrief outputs) |
| 11 | JPMorgan | LLM Suite | External API forbidden → in-house LLM Suite (multi-provider behind a gated wrapper) | 2024-07 broad rollout (200k+ employees by 2025) [18](https://dataconomy.com/2024/07/31/jpmorgan-financial-ai-llm-suite/) | External ChatGPT / Gemini banned internally for data privacy; need to federate multiple providers behind compliance wrapper [19](https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/) | Cross-functional governance board (model vetting, data access, audit logging); 7 specialized LLMs fine-tuned on internal data | Multi-hundred eng-month program (inferred; entirely in-house build, governance board, 200k-seat deployment) | Cross-functional board — CTO, Risk, Compliance, Legal all in the loop; no single product owner | None disclosed; the design preempts most runtime failures by constraining inputs and logging outputs |
| 12 | Morgan Stanley | AskResearchGPT (research) | GPT-4 research-restricted | Announced 2024-07 (research-specific) | Internal eval of GPT-4-based retrieval over Morgan Stanley Research corpus | Eval framework reused from Assistant programme | Inferred 3–6 eng-months on top of existing platform | Morgan Stanley Research leadership; compliance gate | None public |
| 13 | Duolingo | Duolingo Max | GPT-3.5 (beta) → GPT-4 | Announced 2023-03-14 (GPT-4 launch day) [20](https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4/) | Internal testing showed GPT-4 materially better at Role Play dialogue & explanation features; paid tier economics gated cost | A/B in beta; subscription-tier product gating (only paying users) absorbed cost risk; Max = ~5% of subscribers | Inferred 3–6 eng-months for the Max feature suite | CPO / CEO-level product call; OpenAI partnership front and centre | None publicly reported at transition; ongoing capacity / cost concerns handled at infra layer |
| 14 | Khan Academy | Khanmigo | Early-access GPT-4 → GPT-4o multimodal (tutoring demo) | 2023-03 (GPT-4 launch) → 2024-05 (GPT-4o demo with Sal Khan) | Multimodal voice/video enables spoken tutoring | Pilot-mode with teachers / donors; expanded to 700k users by 2024–25 after Microsoft free-for-educators deal 2024-08 | Inferred 6–12 eng-months initial; GPT-4o retrofit ~2–4 eng-months | Sal Khan / CEO-level; non-profit board | No public failure post-transition; accuracy concerns on math tutoring acknowledged generally |
| 15 | Abridge | Ambient clinical documentation | Multi-specialty models, continuous silent transitions | Ongoing; specialty updates publicly referenced 2025-12 [21](https://www.abridge.com/blog/clinical-ai-specialty-models) | Data-gated, not date-gated: Alpha → Beta → staged GA → 100% GA, graduated when specialty beats baseline on live A/B (ratings, edit-frequency) | Three-layer validation: (1) automated LLM "Judge" layer (non-inferiority, misattribution rate); (2) clinician reviewers; (3) third-party audit; live clinical head-to-head blinded trials before GA; dashboarded real-world monitoring | Continuous R&D load; a model update is shipped "quietly" without clinician-side config change — so runtime switching cost approaches zero for the user | Distributed — Product, Clinical, and AI/ML each have a gate; Success Directors hold real-world review authority; no single CTO call | None disclosed; validation layer is explicitly designed to *prevent* failures reaching deployment; the remaining failure surface is drift between specialty baselines |
| 16 | CoCounsel (Casetext → Thomson Reuters) | Legal assistant | Proprietary pre-LLM → GPT-4 (2023-03) → multi-model Anthropic + OpenAI + Google (2024–2026) | 2023-03-01 launch; 2023-08 acquired by Thomson Reuters for $650M; multi-model by 2026 [22](https://www.lawnext.com/2026/02/three-years-after-launching-as-first-ai-legal-assistant-cocounsel-reaches-1-million-users-and-thomson-reuters-teases-whats-ahead.html) | First-mover timing on GPT-4; later, acquired firm (Westlaw) provided 175-year editorial corpus + 4,500 SMEs for validation | Expert-validated legal corpus + retrieval grounding; model ensemble for task specialization | Inferred 12–30 eng-months cumulative; + proprietary LLM for legal / tax / compliance teased for 2026 | CEO / Westlaw leadership post-acquisition; compliance + editorial gates | None disclosed; the acquired editorial gate substantially reduces the hallucination attack surface |

### Non-transitions and rollbacks (negative evidence)

| Org | Transition not taken | Stated rationale | Date |
|-----|---------------------|------------------|------|
| Nuance DAX Copilot / Microsoft | Not yet migrated to non-OpenAI models publicly; stays on GPT-4 class via Azure OpenAI | Workflow integration + Epic EHR integration + regulatory certifications (SOC 1/2/3, HITRUST, HIPAA) [23](https://news.nuance.com/2023-03-20-Nuance-and-Microsoft-Announce-the-First-Fully-AI-Automated-Clinical-Documentation-Application-for-Healthcare) | Launched 2023-03-20 |
| Bloomberg (BloombergGPT) | Publicly unclear — no announced replacement or deprecation, but GPT-4 outperformed BloombergGPT on finance tasks per Queen's University research | "ROI uncertain" around proprietary finance LLM vs frontier general models | 2023-03 launch; public silence after 2023 |
| Klarna | Rollback from full AI to hybrid | "Lower quality" on complex disputes; fintech compliance cost of wrong answers about money | 2025-05 CEO public reversal |
| Character.AI | Not transitioned to frontier frontier models | Consumer-scale economics favor open-weights / in-house efficiency (inferred) | Ongoing |
| JPMorgan | External ChatGPT/Gemini banned for employees | Data privacy + regulatory posture | 2024- |

---

## (iii) Pattern findings

### Pattern 1 — Two archetypes: the "gateway" and the "vertical" (confidence: strong)

**Observed.** Zendesk deployed GPT-4o within 24 hours of release; Intercom moved GPT-4 → GPT-4.1 "in a few days"; Shopify built an internal LLM proxy routing across Claude/OpenAI/Google [10](https://claude.com/customers/shopify); Salesforce Einstein exposes BYOM across OpenAI, Anthropic, Cohere, AWS, Google [24](https://developer.salesforce.com/docs/einstein/genai/guide/supported-models.html). At the other pole, Intercom Fin Apex 1.0 post-trained an in-house vertical model on open-weights; Glean moved from proprietary frontier models to in-house for reliability, cost, privacy; Decagon runs >80% of traffic on models it trained itself.

**Inferred.** Two architectural archetypes crystallized by 2025. The *gateway archetype* minimizes switching cost by treating the model as an interchangeable capability behind a stable interface (proxy + evals + guardrails). The *vertical archetype* minimizes *quality* risk and inference cost by owning the post-training. The two are not mutually exclusive — Shopify has both — but the organizational commitments are different: the gateway needs platform engineering and evals; the vertical needs ML research + post-training + data labeling.

### Pattern 2 — Validation pipeline design dominates switching cost, not the swap itself (confidence: strong)

**Observed.** Zendesk: "evaluation, testing, and deployment of new models in under 24 hours" once the bench was built. Intercom: GPT-4 → GPT-4.1 "in a few days." Abridge: shipped "quietly" with clinicians seeing no config change. Shopify: Kappa 0.02 → 0.61 on judge calibration took the paper-worthy effort. Morgan Stanley: the "eval framework to test every AI use case before deployment" was the enduring artefact, not any specific model integration.

**Inferred (DSM view).** If evals + prompts + retrieval + tool-use are *tightly coupled* to a specific model, each transition costs 2–6 eng-months and introduces silent regressions (format drift, JSON whitespace drift, verbosity-token inflation — see VentureBeat 2025 [25](https://venturebeat.com/ai/swapping-llms-isnt-plug-and-play-inside-the-hidden-cost-of-model-migration)). If they are *loosely coupled* behind a gateway with a reusable eval suite, each transition costs 0.03–0.5 eng-months. The DSM-level architectural prior — "what couples to the model, what couples to the interface" — sets the per-transition cost envelope for years.

### Pattern 3 — Decision authority patterns cluster by regulated vs non-regulated (confidence: strong)

**Observed.**
- Non-regulated SaaS / consumer: CEO or single product leader owns the call publicly (Klarna Siemiatkowski, Intercom Traynor, Duolingo / Khan-level CEO, Shopify McNamara as Director of Applied AI).
- Regulated: cross-functional governance board with compliance + legal + risk veto (JPMorgan LLM Suite; Morgan Stanley Assistant / Debrief; Abridge's three-layer validation; Nuance DAX's Azure-OpenAI + HIPAA/SOC certifications).

**Inferred (STS view).** In regulated domains, the decision authority is *distributed* over a control structure because the cost of an uncaught failure is regulatory (fines, licensure, malpractice). In non-regulated domains, the authority is *centralized* because the cost of an uncaught failure is reputational and reversible. This maps cleanly onto STS: the socio-technical system's formal constraints (regulation, liability) shape who can authorize a capability change; technical constraints (evals, tests) are necessary but not sufficient.

### Pattern 4 — Failures follow three recurrent modes (confidence: moderate, STAMP lens)

**Observed failure classes.**
1. *Policy-surface hallucination under edge cases*: Air Canada Moffatt v 2024-02-14 BC CRT (chatbot fabricated bereavement-fare policy; airline held liable) [26](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416); Klarna 2025-05 rollback on complex disputes; Chevy-of-Watsonville $1-Tahoe 2023-12 prompt-injection.
2. *Reward hacking / schema violation post-deployment*: Shopify Sidekick ICML 2025 paper documents opt-out hacking, tag hacking, hallucinated IDs, wrong enum values [11](https://shopify.engineering/building-production-ready-agentic-systems).
3. *Silent format/behavior drift across model versions*: format drift (trailing period), JSON whitespace drift, Anthropic-tokenizer verbosity inflation, 30% performance drop when reasoning traces dropped (Cursor / Codex evidence in ZenML survey) [27](https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025).

**Inferred (STAMP view).** Each failure mode is a control-structure gap: (1) missing policy-surface constraints — no grounding or citation layer; (2) missing post-deployment feedback — agents optimized without adversarial / integrity checks; (3) missing behavioral regression tests — evals defined at semantic level but not at format level. The pattern: *production safety requires constraints and feedback at three layers simultaneously: policy, agent integrity, behavioral invariants*. Failures happen when one of the three is assumed to be covered by another.

### Pattern 5 — The "capability gap" is the transition trigger more than price (confidence: moderate)

**Observed.** Harvey added Anthropic + Google in May 2025 because BigLaw Bench showed task-specific superiority (Gemini 2.5 Pro for drafting, o3 for pre-trial). Intercom switched to Claude 3.5 Sonnet because it "delivered." Replit chose Claude 3.5 Sonnet for code gen. Duolingo moved GPT-3.5 → GPT-4 for dialog fluency. The publicly stated trigger in 8 of 16 events is *quality on the target task*, in 3 of 16 *regulatory/privacy posture*, in 3 of 16 *capability class (reasoning, multimodality)*; *price* appears only as a secondary constraint.

**Inferred.** For mission-critical production decisions in this window, quality > capability class > price. Price matters mostly via model-within-family choices (Sonnet vs Opus) and infra (Vertex / Bedrock / Azure) not via provider swaps. Implication: the *trigger* for an A1 swap is almost always a benchmark signal, not a cost signal, *unless* the company is at the vertical archetype where unit economics drive post-training.

### Pattern 6 — Regulated / healthcare cases systematically avoid the "swap" language; they run *continuous silent transitions* (confidence: moderate)

**Observed.** Abridge describes updates as "shipped quietly" and graduates models by data-threshold, not date [21](https://www.abridge.com/blog/clinical-ai-specialty-models). Nuance DAX has stayed with Azure OpenAI publicly for 3+ years. JPMorgan abstracts providers behind LLM Suite. Morgan Stanley wraps models in an eval framework applied per use case.

**Inferred.** In regulated domains, the transition is reframed as a *staged model release inside a stable clinician- or advisor-facing product*, not as a "model swap." The transition's visibility is contained to internal governance. This is consistent with resilience-engineering (Hollnagel): the *performance variability* of a new model is absorbed by a validation buffer before it reaches the user. For the adaptability frame, this suggests that *regulated organizations don't adapt slower — they adapt through a different surface*, namely the internal release pipeline rather than the product-facing vendor banner.

### Pattern 7 — The observable product-facing vendor brand has decoupled from the actual model mix (confidence: moderate)

**Observed.** Perplexity routes across Claude, GPT, Gemini, Llama, Mistral behind a meta-router [28](https://www.perplexity.ai/hub/blog/inside-the-rise-of-enterprise-ai-model-switching). Glean Model Hub curates OpenAI, Anthropic, Google, Amazon, Meta models under admin policy. CoCounsel is multi-model. Sierra is "model-agnostic" from day one.

**Inferred.** By 2025–2026 the observable product brand and the underlying foundation model have decoupled for most of the enterprise AI surface. The user-visible decision is "which agent/product," not "which model." Meaning: A1 decisions are increasingly *invisible* from the outside, and the adaptability metric cannot rely on press releases. Proxies needed: model-hub release notes, pricing pages, eval blog posts, deprecation schedules.

---

## (iv) Open questions, negative evidence, speculation

**Looked for but not found.**
- Engineering-month cost of the Klarna AI rollback (human rehiring) — disclosed only as high-level reversal.
- Harvey's cost to build BigLaw Bench and the multi-model router — blog gives architecture description, no eng-months.
- JPMorgan's eng-month total for LLM Suite — implied multi-hundred, not public.
- Public Abridge failure post-mortem — framework documented; specific regressions not.
- Replit Agent pre- and post-Claude eng-months — partnership story; cost silent.
- Specific transition timing for Nuance DAX Copilot (upgrades vs GPT-5-class migration) — not public.
- Bloomberg BloombergGPT current status (active, maintained, or quietly deprecated) — confirmed *absence* of public update post-2023.

**Speculations (labelled).**
- *Speculation.* The "gateway" vs "vertical" split is a 2024–2025 transient. By 2027, regulated verticals (legal, healthcare, finance) will consolidate on *hybrid* — gateway for breadth, vertical for cash-cow workflows — and the A1 decision will migrate from "which model" to "which workflow on which archetype."
- *Speculation.* The public Klarna reversal is likely a sentinel, not an outlier. Customer-service AI with no grounding/citation will face further rollbacks as regulators (EU AI Act liability) and courts (Moffatt v Air Canada) harden liability lines. The companies quiet about failures in the evidence table are not failure-free; they are coverage-poor.
- *Speculation.* The true cost of model transition is dominated by prompt and retrieval-pipeline rewrites, not provider SDK swaps; this is why gateway-first firms can do Zendesk-style 24-hour cutovers while prompt-bound firms have multi-month migrations. The measurable correlate of adaptability is eval-suite maturity.

**Gaps worth filling in later memos.**
- M1/M2: dollarize the eng-month cost across the 15 events as a stock-flow exercise.
- T1 (build vs rent): the gateway vs vertical archetype is a T1 restatement.
- O2 (role redefinition): who sits on the governance board for A1 decisions, and is that role new?
- T3 (technical debt): format-drift, JSON-whitespace drift, evaluator drift across model versions are the debt vectors.

---

## (v) Three-pillar feed

**Pillar 1 — AI usage framework (anchor-managerial).** A1 is now a *routine* decision, not a once-a-year event. The managerial question "what operational and governance structures are required for it to function effectively in an organization" resolves, for this sub-capability, into: *institute a pre-wired control structure that can receive a new model, test it against a durable eval suite, and promote it through a staged release with distributed sign-offs proportional to regulatory exposure.* The specific A1-unit of that structure is a **model transition runbook** with: (a) trigger ladder (benchmark uplift ≥ X, regulatory exposure tier, competitive move, price collapse), (b) pre-declared evals and release-gate thresholds, (c) named decision authority per tier, (d) rollback plan. The Abridge three-layer validation and Shopify judge-calibration pipeline are concrete existence proofs.

**Pillar 2 — Organizational structure.** The decision authority finding maps into the broader adaptability framing: AI-forward regulated firms institutionalize the transition through a *governance board*, an *eval platform team*, and a *clinician/advisor feedback channel*. AI-forward non-regulated firms institutionalize it through a *CEO-level or product-leader bet* plus a *platform team* behind an LLM gateway. The *role-life-cycle* angle (O2) sits on this memo's backbone: "AI ops / model evaluator" is a durable role in both archetypes; "prompt engineer" is transient and absorbed into the eval-platform team; "Chief AI Officer" is largely a regulated-industry signal.

**Pillar 3 — Technical infrastructure (anchor-engineering).** The engineering anchor question "how is the technical infrastructure for an AI-based decision-making system designed and built" resolves for A1 into a small number of load-bearing interfaces:
1. *LLM gateway / proxy* with provider abstraction (Shopify, Salesforce, Perplexity, Glean, JPMorgan LLM Suite) — makes provider swap one-day instead of multi-month.
2. *Prompt library with versioning* + *reusable eval suite* bound to the interface, not the model — the Abridge / Morgan Stanley / Zendesk pattern.
3. *Tool schema + retrieval pipeline* with explicit contract (N-stage gating at Shopify) — lets reward-hacking and schema-violation classes of failure be caught before GA.
4. *Monitoring and drift detection* for format and behavioral regression — the layer 2025's silent failures most often punctured.

**Cross-pillar (meta).** The three pillars *must* move together for adaptability. Organizations that rewired Pillar 3 (gateway + evals) without rewiring Pillar 2 (governance board) either produced headline failures (Klarna 2025 rollback) or absorbed silent regressions (Cursor 30% drop on Codex traces). Organizations that rewired Pillar 2 without Pillar 3 either over-gated innovation (some banks) or re-introduced manual transition cost each quarter. The A1 case evidence suggests a specific architecture for the M1 causal-loop: **"evals-as-infrastructure" is the reinforcing loop; "compliance-veto" is the balancing loop; the delay between capability release and validated production deploy is the adaptability lag and the candidate M2 measurable.**

---

## Decision framework — when to swap vs when to stay

The framework below is calibrated to (i) application criticality, (ii) regulatory posture, (iii) capability gap between incumbent and candidate model. It is designed to be read top-down and to fail safely (default = stay, unless all gates are cleared).

### Decision tree (ASCII)

```
                       [ A1 decision: swap primary LLM or stay? ]
                                           |
                       +-------------------+-------------------+
                       |                                       |
         Q1: Is the app regulated or                 Q1: Non-regulated
         subject to hard liability                    (consumer SaaS,
         (health/finance/legal,                       internal tools,
         or EU AI Act high-risk)?                     non-advice CS)
                       |                                       |
                       |                                       |
                   YES |                                       | NO
                       v                                       v
     Q2: Is there a pre-declared                  Q2': Is the app mission-critical
     eval suite + governance board                 (revenue-path, brand-facing)?
     that has approved this category
     of change before?                                  |          |
              |            |                         YES|          |NO
           NO |            | YES                        v          v
              v            v                     Go to Q3     Q7: Fast-follow OK
     STAY (build the gate  Q3: Does candidate              only behind an LLM
     first; a model is     model show                      gateway + eval
     not the gating item)  benchmark uplift                suite; else STAY
                           >= X% on the 3 key
                           task evals (not demo)?

                           |          |
                        NO |          | YES
                           v          v
                        STAY       Q4: Can the transition be
                        (capability staged (alpha -> beta ->
                        gap not      cohorts -> GA) with
                        material)    rollback?
                                        |          |
                                     NO |          | YES
                                        v          v
                                     STAY       Q5: Does the candidate model
                                     (staged     require prompt / retrieval
                                     release is  rewrite > 2 eng-weeks?
                                     the default             |          |
                                     release mode         YES|          |NO
                                     for regulated)          v          v
                                                         Q6: Is the   SWAP, STAGED
                                                         cost (eng-   (gateway route
                                                         months +     incremental
                                                         drift risk)  traffic, eval
                                                         < expected   gated)
                                                         quality
                                                         uplift
                                                         over 6 mo?
                                                           |     |
                                                         NO|     |YES
                                                           v     v
                                                         STAY   SWAP, STAGED
                                                         (wait  with remediation
                                                         for    tickets in-sprint
                                                         next   pre-cutover
                                                         model)

At Q7 (non-mission-critical):
       IF LLM gateway + eval suite exist -> SWAP in-day (Zendesk / Intercom GPT-4.1 pattern)
       IF not                              -> STAY; the precondition is the gateway, not the model
```

### Calibration table — decision gate thresholds

| Axis | "Stay" zone | "Stage" zone | "Swap" zone |
|------|-------------|--------------|-------------|
| Application criticality | Customer-facing in regulated domain (health/finance/legal) w/o validated gate | Revenue-path SaaS w/ partial guardrails | Internal productivity; low-liability |
| Regulatory posture | Hard liability (HIPAA, FINRA, EU AI Act high-risk) without eval board approval | Soft liability (privacy, IP) with governance in place | No liability lock-in |
| Capability gap | < ~3% on 3 key internal evals (signal within noise) | 3–10% uplift on ≥ 2 of 3 key evals | ≥ 10% uplift on mission-critical task eval with no regression in other two |
| Switching cost (eng-months) | > 6 eng-months, or no rollback path | 1–6 eng-months with rollback | < 1 eng-month behind existing gateway |
| Failure blast radius | End-users can be harmed directly; no human checkpoint | Harm filtered by human edits (advisor, clinician, lawyer) | Internal users only |
| Decision authority | Cross-functional board with compliance veto | Governance board + product leader co-sign | Product / engineering leader single call |

### Practical read-out

- *Zendesk / Intercom-minor-upgrade* → swap in-day; the precondition was the gateway + bench.
- *Harvey multi-model 2025-05* → stage; the capability-gap data justified it and the eval bench controlled the exposure.
- *Abridge specialty models* → continuous silent-stage; data-gated, not date-gated.
- *Klarna late-2024 onwards* → should have been "stay" (policy-surface liability, no grounding/citation infrastructure); the 2025 rollback is exactly the counterfactual.
- *Air Canada 2024-02* → counter-example reading: the absence of a policy-constraint layer turned any model into a liability generator; the decision tree would have blocked at Q2 (regulated-adjacent, no gate) → STAY.

---

## Sources

[1] Pragmatic Engineer — Klarna's AI chatbot analysis, 2024-02-29: https://blog.pragmaticengineer.com/klarnas-ai-chatbot/
[2] OpenAI — Klarna customer story: https://openai.com/index/klarna/
[3] Entrepreneur — Klarna CEO reverses course, 2025: https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
[4] Fortune — Klarna flips from AI-first to hiring people, 2025-05-09: https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
[5] OpenAI — Intercom customer story: https://openai.com/index/intercom/
[6] DKM — How Intercom used $100M + GPT-4 to build Fin in 4 months: https://www.dkmeco.com/en/how-did-intercom-use-100-million-and-gpt-4-to-build-the-hit-ai-customer-service-fin-in-4-months/
[7] The Letter Two — Intercom releases Fin 2, switching Anthropic from OpenAI, 2024-10-12: https://thelettertwo.com/2024/10/12/intercom-releases-fin-2-ai-agent-switching-anthropic-from-openai/
[8] Anthropic — Intercom customer story: https://claude.com/customers/intercom
[9] VentureBeat — Intercom Fin Apex 1.0 beats GPT-5.4 and Claude Sonnet 4.6: https://venturebeat.com/technology/intercoms-new-post-trained-fin-apex-1-0-beats-gpt-5-4-and-claude-sonnet-4-6
[10] Anthropic — Shopify customer story: https://claude.com/customers/shopify
[11] Shopify Engineering — Building production-ready agentic systems (Sidekick, ICML 2025), 2025-08-26: https://shopify.engineering/building-production-ready-agentic-systems
[12] Harvey blog — Expanding Harvey's model offerings, 2025-05-13: https://www.harvey.ai/blog/expanding-harveys-model-offerings
[13] TechCrunch — Anthropic, Google score win by nabbing OpenAI-backed Harvey, 2025-05-13: https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/
[14] Harvey blog — Building legal agents and workflows with OpenAI's o1, 2024-09: https://www.harvey.ai/blog/harvey-building-legal-agents-and-workflows-with-openai-s-o1
[15] Zendesk — Rolling out GPT-4o, 2024-05: https://www.zendesk.com/newsroom/articles/gpt-4o/
[16] Morgan Stanley — Launch of AI @ Morgan Stanley Debrief, 2024-06: https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch
[17] OpenAI — Morgan Stanley customer story: https://openai.com/index/morgan-stanley/
[18] Dataconomy — JPMorgan introduces its own LLM Suite, 2024-07-31: https://dataconomy.com/2024/07/31/jpmorgan-financial-ai-llm-suite/
[19] The Digital Banker — JPMorgan Chase LLM Suite drives AI transformation: https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/
[20] TechCrunch — Duolingo launches subscription tier with GPT-4 tutor, 2023-03-14: https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4/
[21] Abridge — Innovation at the speed of trust: continuous improvement in clinical AI, 2025-12: https://www.abridge.com/blog/clinical-ai-specialty-models
[22] LawSites — Three years after launching, CoCounsel reaches 1M users, 2026-02-24: https://www.lawnext.com/2026/02/three-years-after-launching-as-first-ai-legal-assistant-cocounsel-reaches-1-million-users-and-thomson-reuters-teases-whats-ahead.html
[23] Nuance news — Nuance and Microsoft announce first fully AI-automated clinical documentation, 2023-03-20: https://news.nuance.com/2023-03-20-Nuance-and-Microsoft-Announce-the-First-Fully-AI-Automated-Clinical-Documentation-Application-for-Healthcare
[24] Salesforce Developers — Supported models in Agentforce: https://developer.salesforce.com/docs/einstein/genai/guide/supported-models.html
[25] VentureBeat — Swapping LLMs isn't plug-and-play: hidden cost of model migration: https://venturebeat.com/ai/swapping-llms-isnt-plug-and-play-inside-the-hidden-cost-of-model-migration
[26] CBC — Air Canada held liable for chatbot's bad advice on bereavement rates, 2024-02: https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416
[27] ZenML LLMOps — What 1,200 production deployments reveal about LLMOps in 2025: https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025
[28] Perplexity hub — Inside the rise of enterprise AI model-switching: https://www.perplexity.ai/hub/blog/inside-the-rise-of-enterprise-ai-model-switching
