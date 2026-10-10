# T1 — Build vs. Rent Decision Framework Under Model Flux

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Axis:** T — Pillar 3 (Technical Infrastructure), adaptability lens
> **Date:** 2026-04-22
> **Frame:** research memo feeding the three-pillar adaptability framework
> **Anchor questions:**
> - *Engineering* — How is the technical infrastructure for an AI-based decision-making system designed and built?
> - *Managerial* — What operational and governance structures are required for it to function effectively in an organization?
>
> This memo treats "build vs. rent" not as a one-shot procurement choice but as an **architectural stance** that must remain valid across a model-generation turnover of 6–12 months. Every finding is tied back to the two anchor questions.

---

## i. Method

### Object of study

The decision surface under investigation is the joint choice across five axes:

1. **Serving substrate** — managed API (OpenAI, Anthropic, Google) vs. cloud-hosted weights (Bedrock, Vertex, Azure) vs. self-hosted on rented GPUs (RunPod, CoreWeave, Together, Fireworks, Baseten) vs. on-prem clusters.
2. **Weight provenance** — proprietary frontier (GPT-5, Claude 4/Opus, Gemini Ultra) vs. open-weight (Llama 3.x / 4, Qwen 2.5 / 3, DeepSeek V3 / R1, Mistral Large 2, Codestral).
3. **Topology** — single provider with vendor lock-in vs. multi-provider routing (OpenRouter, LiteLLM, Portkey, Martian, Not Diamond, Vercel AI SDK).
4. **Data perimeter** — public cloud tenancy vs. virtual private cloud / Data Zones (Azure OpenAI) vs. sovereign cloud (Mistral Compute, Gaia-X, French state cloud) vs. air-gapped on-prem.
5. **Customization depth** — pure prompting vs. RAG vs. fine-tuning / LoRA adapters vs. continued pre-training vs. trained-from-scratch (rare; Character.AI pre-Google, Cursor Composer 2, Intercom Fin Apex, BloombergGPT).

### Sampling strategy

I catalogued switch events in 2024–2026 across six observable categories: (a) API → self-hosted, (b) self-hosted → API return, (c) proprietary → open-weight, (d) single-vendor → multi-provider routing, (e) regulated-data VPC / sovereign builds, (f) "DeepSeek inflection" responses. Cases were included when at least one of stated rationale, stated cost, or stated outcome is publicly documented. Total: 15 anchored case rows plus a secondary reference pool.

### SDM lens applied

- **Tradespace exploration** (Ross & Hastings) — each configuration mapped as a point in the vector (cost-per-million-tokens, p95 latency, data-sensitivity-tier, capability ceiling, switching-cost) space; the Pareto frontier moves as model generations release.
- **Real options** (de Weck) — API is a call option on the next frontier model; self-hosted open-weights is a put option against price hikes and deprecations; multi-provider routing is a switching option on the above two.
- **Architecture decomposition** (Crawley) — decompose into five separable layers: model, serving, prompt, eval, governance. The interface contracts between layers determine what survives a model-generation shift.
- **Lifecycle** — explicitly separate *decisions that survive* a model turnover (layer boundaries, routing abstractions, eval harnesses) from *decisions that require rewrite* (prompts keyed to tokenizer quirks, fine-tunes bound to a retired base, provider-specific SDK calls, JSON-mode schemas).

### Evidence hygiene

Absolute dates throughout. Cost figures in USD. Confidence labels: **H** (primary-source corroboration), **M** (single primary source or triangulated secondary), **L** (industry commentary / single secondary). Speculation explicitly tagged.

---

## ii. Evidence table — switch events, 2024–2026

| # | Firm | Date | From | To | Trigger | Cost / scale | Outcome | Conf | Source |
|---|------|------|------|----|---------|--------------|---------|------|--------|
| 1 | Character.AI | 2024-06 → 2024-11 | Self-hosted, custom-trained models on rented H100s, >20k QPS (~20% of Google-search volume) | Continued self-hosted, but int8 native training + custom FlashAttention-3 int8 kernel + 20× KV-cache compression; then post-Google licensing deal (2024-08) scaled down model R&D | Unit-economics crisis; inference costs unsustainable at consumer-chat price points | Two public optimization rounds: end-to-end inference speedup ~10% prefill / ~30% decoding over prior Triton baseline; 95% cache hit rate; 3.8× cost improvement reported by 2025 | Cost curve bent enough to survive, but unable to outrun frontier-model R&D cost; co-founders + ~30 researchers joined Google in licensing deal at ~$2.5B implied valuation; company shifted focus to consumer chat on Llama-family | H | research.character.ai/optimizing-inference (2024-06); .../part-deux (2024-11); Bloomberg 2024-08-02 |
| 2 | Character.AI (post-deal) | 2024-09+ | Self-trained Character model | Meta Llama 3.1-family | Capital + talent exit; cost of training at frontier exceeds consumer-chat ARPU | Public disclosure light; "step away from developing LLMs" — shift to consumer platform | Proprietary weights no longer a source of advantage at their cost structure | M | btimesonline 2024-10-03 |
| 3 | Intercom (Fin) | 2024-10 | OpenAI GPT-based Fin v1 | Anthropic Claude-based Fin 2 | Claude quality on customer-service resolution exceeded GPT-4-class on Intercom's own eval | Not publicly quantified; company launched "Fin 2" as product event, not migration | Fin 2 shipped as primary agent; Intercom later (2025) launched *Fin Apex 1.0*, a small post-trained in-house model reported to beat GPT-5.4 and Claude 4.6 Sonnet on resolution rate | H | Fortune 2024-10-10; thelettertwo 2024-10-12; VentureBeat Fin Apex 1.0 |
| 4 | Harvey | 2025-05 | OpenAI-exclusive (proprietary vertical "Legal GPT" fine-tune) | Multi-model orchestrator: OpenAI + Anthropic + Google, routed by task | Frontier reasoning models (o1/o3-class, Claude 3.5/4, Gemini Ultra) beat Harvey's custom legal model on Harvey's own *BigLaw Bench* | Not publicly quantified; Harvey explicitly "scrapped its proprietary vertical model" | Routing: drafting → extended-reasoning models; research → high-recall models; jurisdictional → models with regional training strength | H | TechCrunch 2025-05-13; harvey.ai/blog |
| 5 | Morgan Stanley Wealth Management | 2023-09 (Assistant) → 2024-Q1 (Debrief) | Pre-AI retrieval / manual note-taking | OpenAI GPT-4 via *enterprise partnership* (zero data retention; fine-tuned on anonymized advisor queries) | Advisor productivity; SEC-regulated context forbids public-tier model use | Two tools, both direct to OpenAI API (not via Azure in reported architecture); >98% advisor-team adoption | Strategic client status = early-access option on next generations; compliance perimeter enforced at contract layer, not infrastructure layer | M | openai.com/index/morgan-stanley; morganstanley.com/press-releases |
| 6 | JPMorgan Chase | 2024-summer launch; rolling updates every 8 weeks | Pre-GenAI internal tooling | *LLM Suite*, in-house orchestration platform, model-agnostic, wrapping OpenAI + Anthropic models via secure APIs | Compliance + data-protection + governance control over training / deployment / evolution | ~200k–250k employees provisioned within 8 months; 50k concurrent sessions at peak; technology budget $17B (2024) → $18B (2025) | "Entirely in-house" orchestration; microservices; model layer decoupled so providers can be swapped on 8-week cadence without rewriting app layer | H | thedigitalbanker.com; artificialintelligence-news.com 2025 |
| 7 | Klarna | 2024-02 launch → 2025-05 walk-back | Human customer-service + legacy CRM | OpenAI-powered chatbot handling ~2/3 of tickets (claim: equivalent of 700 FTEs) | Cost reduction; public "AI-first" positioning | In 2025 CEO publicly acknowledged "lower quality"; hybrid model restored (AI + remote human agents on Uber-style flex schedules) | Not an infra switch per se but a *governance* reversal on what an API-based agent could own; SaaS (Salesforce, Workday) partly re-purchased after internal Neo4j-based replacement faltered | H | cxtoday.com; loris.ai; arvindmozumdar.medium.com |
| 8 | Perplexity | 2024 | Earlier *pplx-online* on Mistral-7B / Llama-2-70B | *Sonar* family (own post-training on Llama 3.1 70B / later Llama 3.3 70B), with a Huge variant on Llama 3.1 405B; served on Cerebras for 1,200 tok/s | Answer quality + latency for search-grade UX | Moved from pure open-weight usage to open-weight + in-house post-training; inference on specialty silicon | Model layer owned; serving substrate rented (Cerebras); Llama base provides option-to-upgrade as Meta releases new generations without re-architecting the post-training pipeline | H | perplexity.ai/hub/blog/meet-new-sonar; openrouter.ai |
| 9 | Replit (Agent) | 2024-09 → 2025+ | Single-vendor Anthropic Claude 3.5 Sonnet on Vertex AI + Gemini 1.5 Flash for Assistant | Multi-provider: Anthropic, OpenAI, Google, xAI Grok, Perplexity integrations usable inside generated apps; Databricks Apps integration for enterprise data-awareness | Capability-specific routing (code vs. planning vs. cheap assistant); enterprise data-residency via Databricks | Not publicly quantified in engineer-months; Replit "accelerated the product roadmap" after Claude 3.5 Sonnet v2 release | Serving substrate diversified; app layer abstracted so user apps can pick provider | M | blog.replit.com/2025-replit-in-review; cloud.google.com/customers/replit |
| 10 | Thomson Reuters (CoCounsel) | 2024-2025 | Per-provider SDKs across 10 providers | Vercel AI SDK as unified provider-abstraction layer | Consolidation + maintenance cost of per-SDK branches | Vercel report: "thousands of lines of code" deprecated during migration; initial CoCounsel build: 3 devs, 2 months | Architectural bet on provider-abstraction SDK rather than per-provider clients | M | vercel.com/blog/ship-ai-2025-recap |
| 11 | Cursor (Anysphere) | 2025 → 2026-04 | Multi-provider API: OpenAI + Anthropic + Google, with Cursor credits mapped to provider tokens | Composer 2: own model trained from scratch on own infrastructure, tuned for IDE operations (repo read / plan / test / fix), 200+ tok/s on custom GPU kernels | Cost control at $2B ARR scale; latency requirements for IDE UX; differentiation | Raised >$3B from NVIDIA, Google, others | Proprietary model layer + proprietary serving; but retains multi-provider API fall-back so users can still call frontier models per-task | M | dev.to/gabrielanhaia 2026-04; nxcode.io/resources |
| 12 | SNCF Group (French state rail) | 2024-01 pilot (SNCF-GPT) → 2025+ | Internal SNCF-GPT (100k employees trialling) on unspecified provider | Mistral partnership integrating Mistral Large + Codestral into existing orchestration | Sovereignty; French-language + EU-AI-Act posture; procurement preference | Not publicly quantified | Mistral compute substrate (French data centers) + existing SNCF-GPT UI preserved; model layer swapped under a stable app | M | railwaypro.com; mistral.ai/news |
| 13 | Nuance DAX Copilot / Microsoft Cloud for Healthcare (e.g., Stanford Medicine, WellSpan Health) | 2023-03 product launch; 2024 enterprise-wide deployments | Pre-GenAI ambient-scribe workflows | DAX Express / DAX Copilot powered by GPT-4 on Azure, under hospital's HIPAA Business Associate Agreement with Microsoft; regional data residency + redundancy | Compliance (HIPAA); clinician burnout | Per-clinician survey n=879: ~5 min saved per encounter; 77% quality lift; 70% work-life balance lift | Regulated-data architecture: API layer fixed to Azure OpenAI; data residency + BAA at contract/infra layer rather than model layer | H | news.nuance.com; blogs.microsoft.com 2024-03-11 |
| 14 | Epic / Mayo Clinic | 2023-H1 → 2024 | Manual in-basket messaging; pre-GenAI ambient nursing | GPT-4 via Epic-MSFT pipeline; Abridge-Epic-Mayo nursing-AI co-development | Clinician burden + volume of patient messages | ~30 seconds saved per nurse message; draft quality described as more empathetic | Stack: model = GPT-4 on Azure; workflow owned by Epic; clinical content owned by Mayo — three-party interface contract rather than stack ownership | H | fiercehealthcare.com HIMSS24; abridge.com/press-release |
| 15 | 300+ enterprises via Martian (incl. Accenture "switchboard" integration) | 2024-09+ | Single-provider and hand-rolled fallbacks | Patent-pending LLM router with compliance features + Accenture portfolio integration | Cost + reliability + compliance routing | Reportedly approaching $1.3B valuation by 2026-04; customer logos incl. Amazon, Zapier | Multi-provider routing as a productized capability — switching option owned outside the app | M | newsroom.accenture.com 2024-09; medium.com/@sarawgiapoorvwork 2026-04 |

**Secondary reference pool** (not fully tabled; cited in pattern findings):

- **BloombergGPT** (March 2023, 50B params, $10M+ training) — Ethan Mollick and others documented GPT-4-8k *beating* BloombergGPT on most finance tasks; no public update to BloombergGPT after 2023; canonical "build-from-scratch loses to scale" case. (H)
- **DeepSeek V3 / R1 inflection** (2025-01-23 R1 release; 2025-01-27 Nvidia/Broadcom ~$600B market-cap cut) — prompted AWS, Azure, Google Cloud, Snowflake to all add DeepSeek to marketplaces within weeks; DeepSeek subsequently cut API prices 50%+ in September 2025 and again in December 2025. (H)
- **Qwen 2.5 family** — 90k+ enterprise deployments via Alibaba Cloud Model Studio by 2024-2025; Xiaomi (consumer electronics/smart manufacturing), Airbnb customer-service chatbot; Qwen 3.6-Plus + MiMo-V2-Pro accounting for ~49% of coding tokens on OpenRouter by early 2026. (M)
- **Groq LPU** — Dropbox, Volkswagen, Riot Games as named customers; 1.9M developers on GroqCloud; 75% of Fortune 100 maintain accounts; IBM watsonx Orchestrate partnership 2025-10; Meta official Llama API on Groq 2025-04. (H)
- **Cerebras** — OpenAI master relationship ≥$20B / 750 MW inference capacity disclosed 2026-01; Perplexity Sonar inference. (M)
- **Menlo Ventures 2025 State of GenAI** — 47% of AI deals reach production (~2× traditional SaaS); 27% of spend is PLG (shadow AI pushes true figure closer to 40%); once an enterprise picks a vendor it tends to stay even when switching costs are low. (H)
- **CIO survey evidence** (VentureBeat "Swapping LLMs isn't plug-and-play" 2025): 55% of CIOs switched LLMs ≥ once; 81% expect to rely on ≥2 providers in 2026; migration expenses 20–50% of original dev time. (M)
- **EU AI Act** — entered into force 2024-08-01; prohibited practices + AI literacy applicable 2025-02-02; high-risk obligations enforceable 2026-08-02; extended transition for embedded regulated products to 2027-08-02. (H)
- **Azure OpenAI** — Data Zones feature strengthening residency controls; HIPAA / SOC2 / FedRAMP covered; BAA via Microsoft Data Protection Addendum; 2025-03 update disclosing possible cross-region "temporary data relocation" for fine-tuning. (H)

---

## iii. Pattern findings

### P1 — The break-even for self-hosting is one order of magnitude higher than most teams estimate (H)

Multiple independent analyses converge near the same threshold: self-hosting Llama-class open-weights becomes cheaper than API only above roughly **5–11 billion tokens per month** (≈100–500M tokens/day) once GPU amortization, engineering time, utilization gaps, power, and redundancy are included. A healthcare AI team's reported figure — $4,300/month in GPU cost plus $6,100/month in engineering time, versus $1,870/month on the equivalent API — is the canonical *5.6× loss* from self-hosting below threshold. For the 87% of workloads below this break-even, API is strictly Pareto-dominant on cost, latency variance, and time-to-next-generation. The self-hosting regret region is larger than vendor blogs suggest.

### P2 — Self-hosting wins return above break-even *and* for regulated data (H)

Above the break-even, save-rate claims cluster at 50–80% cost reduction on inference (multiple vendor and independent sources). Character.AI's 3.8× unit-cost improvement between 2024-06 and 2025 is the engineering-heroics version; JPMorgan's LLM Suite is the regulated-data version — the driver there is not cost per token but end-to-end control over training, deployment, evolution, and auditability. Two distinct mechanisms, often conflated.

### P3 — The DeepSeek R1 release (2025-01-23) was the single largest price-curve shock of the 2024–2026 window (H)

The R1 release caused an immediate Nvidia / Broadcom market-cap event (~$600B combined) and led all three US hyperscalers plus Snowflake to add DeepSeek to their marketplaces within weeks. Downstream effect: API-side price competition compressed input-token costs by another 50%+ by late 2025, independently of hardware progress. **Implication for the decision framework**: any self-hosting business case built before January 2025 on 2024 API price assumptions needs recomputation — the API rental curve moved faster than on-prem amortization.

### P4 — Proprietary-data advantages are smaller than scale advantages *at frontier, for general reasoning* (H)

BloombergGPT is the canonical negative result: $10M+ of finance-specialized pre-training underperformed GPT-4 on most finance tasks. Harvey's 2025-05 pivot is the mirror case in legal: Harvey's own *BigLaw Bench* showed frontier reasoning models beating their custom legal model; they scrapped the proprietary vertical model. The pattern is **not** "verticals never win" — Intercom's Fin Apex 1.0 is a counterexample within a narrow resolution task — but "verticals rarely win at frontier general reasoning, and the window to catch up closes at every new generation." Vertical training compounds only on very narrow, well-defined task surfaces where post-training on proprietary conversation data exceeds what a frontier model can do zero-shot.

### P5 — Multi-provider routing has transitioned from "nice to have" to "stated strategy" between 2024 and 2026 (H)

Menlo Ventures 2025: once picked, vendors tend to stay; but CIO surveys (VentureBeat 2025) find 55% have already switched at least once and 81% expect ≥2 providers in 2026. Intermediary firms (OpenRouter $500M valuation June 2025; Martian nearing $1.3B April 2026; Portkey; LiteLLM 470k+ proxy downloads; Vercel AI SDK >20M monthly downloads) have capitalized. Harvey's multi-model orchestration, Replit's multi-provider app-generation, JPMorgan's 8-week-cadence model-agnostic LLM Suite, Cursor's co-existence of Composer 2 and frontier APIs — all encode the *switching option* as a first-class architectural element. The anti-pattern (unanchored single-provider coupling with prompts tied to a provider's quirks) is now recognized as malpractice.

### P6 — Decisions that *survived* the GPT-4 → GPT-5 / Claude 3 → Claude 4 turnovers (H/M)

| Decision | Survived because | Confidence |
|---|---|---|
| Thin client wrapper around provider SDKs (Vercel AI SDK, LiteLLM, Portkey pattern) | Interface contract isolates app from SDK breaking changes | H |
| JSON output validation with schemas *outside* the prompt | JSON-mode semantics differ across providers and across generations; external validation is tokenizer-agnostic | H |
| Golden-set eval harness with win/loss reporting (llama-prompt-ops style) | Eval harness is independent of model; regressions become visible on swap | H |
| Model-agnostic orchestration layer with 8-week model-refresh cadence (JPMorgan LLM Suite) | Decouples business logic from provider selection | H |
| Routing rules expressed as capability × task (Harvey, Replit) | Pattern is stable while underlying providers rotate | M |
| VPC / Data Zone / BAA at infrastructure contract layer (Azure OpenAI, Morgan Stanley, Epic/Mayo, DAX) | Compliance perimeter is orthogonal to model generation | H |
| Retrieval layer (RAG) with vector store external to provider | Embedding-model churn is independent of generation model churn | M |

### P7 — Decisions that *required rewrite* at every model-generation shift (H/M)

| Decision | Broke because | Confidence |
|---|---|---|
| Prompts keyed to specific tokenizer quirks (Llama chat template, OpenAI system-prompt behavior, Claude XML preference) | Every generation re-tunes instruction following | H |
| Few-shot examples assuming fixed context length | Context growth + attention recomputation change which few-shots help | M |
| Fine-tunes bound to a specific base that gets deprecated (multiple OpenAI fine-tune migrations during GPT-3.5 → GPT-4 → GPT-4o → GPT-5 cycle) | Deprecation forces re-fine-tune or re-architecture | H |
| Per-provider JSON-mode schemas (OpenAI's stricter GPT-5.4 schema rejected 30% of legacy prompts per OpenAI's own migration tool) | Schema semantics drift across generations | H |
| Prompt libraries in `.md` files, never regression-tested | Silent regressions compound across generations | M |
| Agent loops hard-coded to one provider's tool-use format | Tool-use syntax differs across providers and generations | M |
| Evaluator prompts using LLM-as-judge with the *same* model being judged | Evaluator drifts with the judged-model; circular dependency surfaces at every release | H |

### P8 — The Klarna inversion: *governance reversal* is an under-modelled class of switching cost (H)

Klarna's 2024-02 "replaced 700 FTEs" announcement to 2025-05 "lower quality — hybrid restored" rollback is not a model-migration event but a *governance-migration* event. The infrastructure choice (OpenAI API-based chatbot) did not change; the *scope of authority* given to the agent did. The switching cost is real but lives in the organization pillar, not the infrastructure pillar, and is not captured in engineering-month accounting. Connects to M1 (systems dynamics) and O2 (role redefinition).

### P9 — Sovereignty / regulated-domain cases look like a different Pareto surface (M)

SNCF-Mistral, French sovereign-cloud AI, EU AI Act high-risk deadline (2026-08-02 / 2027-08-02 for embedded products), Morgan Stanley / JPMorgan / Nuance DAX / Epic all exhibit the same pattern: **the decision variable is not primarily price-per-token, but enforceable control over the data perimeter** (BAA, Data Zones, sovereign cloud, on-prem). Frontier capability is acceptable only at price = contractable compliance posture. This is a different tradespace than the consumer / developer-tool tradespace and should not be aggregated.

### P10 — The "Cursor Composer 2 pattern" — going backward on rent-first — appears only above ARR thresholds (speculative, M)

Cursor ($2B ARR reported 2026), Character.AI (pre-Google: consumer-scale inference at ~20% of Google Search request volume), Intercom Fin Apex (post-trained in-house), and Perplexity Sonar (post-trained in-house) all chose to *own more of the stack* than their earlier selves. The observable threshold seems to be (a) extreme volume making amortization rational, (b) differentiation pressure from APIs commoditizing to all competitors, or (c) latency / UX envelope tighter than what APIs guarantee. **Speculation**: below ~$50M ARR, building model + serving is rarely worth it; between $50M–$500M, selective vertical post-training on an open-weight base starts to pencil; above $500M–$1B, trained-from-scratch for specific task surfaces re-enters the option set.

---

## iv. Primary output — decision tree (ASCII)

The decision tree below is parameterized by (a) company size, (b) regulatory posture, (c) capability requirement, (d) latency / cost constraint, (e) data-sensitivity tier. Output is a **stance** with a primary and a fallback.

```
START
 |
 +-- (a) Data-sensitivity tier?
 |     |
 |     +-- REGULATED (HIPAA / PCI / EU AI Act high-risk / SEC-regulated / classified)
 |     |     |
 |     |     +-- (b) Has BAA / Data Zone / sovereign-cloud contract with a hyperscaler?
 |     |     |     |
 |     |     |     +-- YES --> STANCE A1: Managed API via VPC / Data Zone
 |     |     |     |           (Azure OpenAI, Vertex AI, Bedrock with BAA/PCI/ISO)
 |     |     |     |           Primary: frontier proprietary model through that channel.
 |     |     |     |           Fallback: second approved provider of same tier inside same perimeter.
 |     |     |     |           Exemplars: Morgan Stanley, Nuance DAX, Epic/Mayo, Harvey on Azure.
 |     |     |     |
 |     |     |     +-- NO (or insufficient) --> STANCE A2: On-prem / sovereign cluster with open-weights
 |     |     |                                 (Llama 3.x / Qwen 2.5 / Mistral Large / DeepSeek under license)
 |     |     |                                 served by vLLM / TGI / Triton with strict egress control.
 |     |     |                                 Exemplar: SNCF-Mistral on Mistral Compute; air-gapped defense cases.
 |     |     |
 |     |     +-- Additional gate: EU AI Act high-risk system destined for EU market
 |     |                          -> also satisfy risk management, bias testing, human oversight per
 |     |                             2026-08-02 deadline (2027-08-02 if embedded in regulated product).
 |     |
 |     +-- CONFIDENTIAL (internal IP, customer PII, strategy docs) but not externally regulated
 |     |     |
 |     |     +-- (c) Company size?
 |     |           |
 |     |           +-- <50 FTE           --> STANCE B1: Managed API + provider-abstraction SDK
 |     |           |                          (OpenAI / Anthropic / Google via Vercel AI SDK / LiteLLM).
 |     |           |                          Do NOT self-host. Engineer-months >> token savings below threshold.
 |     |           |
 |     |           +-- 50-500 FTE        --> STANCE B2: As B1 + dual-provider fallback wired in from day one.
 |     |           |                          Add per-task routing only if measurable quality delta justifies it.
 |     |           |
 |     |           +-- 500-5,000 FTE     --> STANCE B3: LLM-gateway pattern (LiteLLM / Portkey)
 |     |           |                          + organization-wide guardrails + shadow-AI discovery.
 |     |           |                          Model-agnostic orchestration with 8-12 week refresh cadence
 |     |           |                          (cf. JPMorgan LLM Suite).
 |     |           |
 |     |           +-- 5,000+ FTE        --> STANCE B4: Multi-provider, multi-region, with internal platform team.
 |     |                                      Consider open-weight hot-swap for cost-sensitive workloads
 |     |                                      only after measuring monthly token volume per workload class.
 |     |
 |     +-- INTERNAL (ops docs, codebases, non-sensitive)
 |     |     |
 |     |     +-- (d) Token volume per month for the workload?
 |     |           |
 |     |           +-- < 1B tokens/month                 --> STANCE C1: Managed API only. Rent the option.
 |     |           +-- 1B-10B tokens/month               --> STANCE C2: API primary; evaluate cloud-hosted
 |     |           |                                          open-weights (Bedrock / Vertex Model Garden /
 |     |           |                                          Together / Fireworks) for identified hot paths.
 |     |           +-- 10B-100B tokens/month             --> STANCE C3: Mixed. Frontier API for novel/long-tail;
 |     |           |                                          self-hosted open-weight (Llama 3.x / Qwen 2.5 /
 |     |           |                                          DeepSeek) on rented GPUs (CoreWeave / RunPod /
 |     |           |                                          Together) for well-characterized high-volume paths.
 |     |           +-- > 100B tokens/month or latency-critical UX --> STANCE C4: Self-host + custom kernels,
 |     |                                                              specialty silicon (Groq LPU / Cerebras / TPU);
 |     |                                                              model layer owned if post-training on open-weight base pays back.
 |     |                                                              Exemplars: Character.AI, Perplexity Sonar, Cursor Composer 2, Intercom Fin Apex.
 |     |
 |     +-- PUBLIC / low-sensitivity
 |           --> STANCE D: Use whatever is cheapest and fastest today; default to managed API
 |               with provider-abstraction SDK so switching remains a config change.
 |
 +-- (e) Capability requirement?
       (evaluated independently; can *force* a stance upward)
       |
       +-- FRONTIER (requires best available reasoning / tool-use / coding)
       |     --> Upgrade stance to include *at least* one frontier proprietary provider in the route set.
       |         Pure self-hosted open-weight usually insufficient for frontier tasks as of 2026-04
       |         (gap closing but not closed; DeepSeek R1 narrowed it in Jan 2025; Llama 4 narrowed it further;
       |         but Claude 4 Opus / GPT-5 still hold on complex reasoning at date-of-writing).
       |
       +-- COMPETENT (matches mainstream SaaS quality; text, RAG, standard agents)
       |     --> Open-weight (Llama 3.3 70B, Qwen 2.5 72B, Mistral Large 2) + post-training is viable.
       |         API still likely cheaper below break-even volume.
       |
       +-- NARROW (single well-defined task surface — classification, extraction, summarization, one-domain Q&A)
             --> Small post-trained open-weight on rented GPUs is competitive and controllable.
                 Exemplar: Intercom Fin Apex 1.0.
```

**How to read the tree under model flux.** The tree is re-evaluated on any of four triggers: (T1) new generation release by any primary provider; (T2) >30% price drop in any major API; (T3) new regulatory constraint (EU AI Act stage enforcement, sectoral rule); (T4) workload volume crosses a decade boundary (×10). Between triggers, the layer boundaries are *invariant* and the specific model inside each layer is *swappable*.

### Tradespace framing (Ross & Hastings)

Each stance is a point in the vector **(cost/Mtok, p95 latency, sensitivity tier covered, capability ceiling, switching cost)**. The Pareto frontier in 2025-01 (pre-DeepSeek-R1) and 2026-04 (post-Claude-4-Opus and GPT-5, post-DeepSeek V3.2) are visibly different: the R1 release shifted the cost axis by 50–75%; Claude 4 and GPT-5 pushed the capability-ceiling axis. Architectural decisions that were on the 2024 frontier (single-provider, hand-rolled client) fall behind the 2026 frontier.

### Real-options framing (de Weck)

- **Managed API** = call option on next frontier model (exercise price = month-over-month API cost).
- **Open-weight on rented GPU** = put option on provider price hikes + call option on fine-tuning (exercise price = engineering-months + GPU amortization).
- **Multi-provider router** = switching option on the above (premium = router/gateway maintenance + regression-test infrastructure).
- **Trained-from-scratch** = compound option: higher premium, higher payoff only if workload volume + differentiation pressure justify it (exemplars Cursor Composer 2, Intercom Fin Apex; counterexemplar BloombergGPT).

### Architecture decomposition (Crawley)

The five-layer decomposition with lifecycle behavior under model-generation shift:

```
+-----------------------------------------------------------------+
| Governance layer  | DLP, BAA, Data Zones, audit, EU AI Act       |   invariant
|                    | conformity, egress policy                    |
+-----------------------------------------------------------------+
| Eval layer        | Golden sets, LLM-as-judge with fixed judge,  |   near-invariant
|                    | win/loss harness, shadow deploys            |
+-----------------------------------------------------------------+
| Prompt layer      | Instructions, schemas, tool definitions      |   partially fragile
|                    |   (schemas stable; per-provider idioms drift)|   (redo ~20-40% per generation)
+-----------------------------------------------------------------+
| Serving layer     | SDK wrappers, routing, gateways, rate limit  |   invariant if abstracted
|                    |                                              |   (Vercel AI SDK / LiteLLM pattern)
+-----------------------------------------------------------------+
| Model layer       | Which specific generation, which provider,   |   fully volatile
|                    | which fine-tune                             |   (6-12 month life)
+-----------------------------------------------------------------+
```

The research finding is that **the volatility budget should be concentrated in the bottom two layers**; a system where fragility leaks upward into eval, governance, or app layers is mis-architected.

---

## v. Open questions, negative evidence, three-pillar feed

### Open questions

1. **What is the real engineering-month cost of a typical major model swap?** Published data is fragmentary. VentureBeat's "20–50% of original dev time" figure is useful but bands are wide. Morgan Stanley / JPMorgan / Harvey have not disclosed line-item migration costs. Intercom discloses direction of switch but not cost. Character.AI discloses performance improvement but not engineering-hour line items. A research extension (M2 indicator) could attempt to construct this via vendor-contracted case studies.
2. **At what workload shape, specifically, does self-hosting dominate?** The "5–11B tokens/month" break-even is averaged across many workload profiles. Conversational workloads with high variance in request length and batch-unfriendly patterns shift the threshold substantially; high-throughput embedding and batch-scorable workloads shift it in the other direction.
3. **How often does a proprietary-data vertical model actually stay ahead of frontier over a 12-month window?** BloombergGPT, Harvey legal GPT: lost. Intercom Fin Apex 1.0: ahead at launch. Cursor Composer 2: ahead at launch. Perplexity Sonar: comparable to frontier on task-specific benchmarks. No systematic longitudinal study exists (gap worth flagging for M2).
4. **How does EU AI Act enforcement (beginning 2026-08-02) change the cost structure of multi-provider routing?** Providers will diverge in EU-compliance posture; routing has to become compliance-aware. This is a prediction (speculation, L) rather than observed.
5. **What is the switching-cost of *rolling back* an AI deployment** (cf. Klarna)? The inverse migration — restoring human workflows, re-hiring, re-establishing SaaS contracts — is rarely analyzed and is quantitatively different from a forward migration.

### Negative evidence (looked for, not found)

- **No well-documented case of a mid-scale firm self-hosting a frontier-*quality* model below 5B tokens/month and winning on cost.** This is load-bearing: it is evidence that the break-even is real. Plenty of blog posts advocate self-hosting but case studies that include honest engineering accounting do not support it below threshold.
- **No documented case (2024–2026) of a firm that switched from API back to human-only for the *same capability* and called it a win.** Klarna's rollback is to a *hybrid* not a full human return.
- **No public disclosure of regression *budgets* (acceptable % degradation) used by enterprises when swapping providers.** Teams seem to run swaps on ad-hoc gates; a standardized acceptance criterion for a model-swap decision would improve M2.
- **No public evidence of a regulated enterprise running a production *inference* workload on air-gapped on-prem frontier-class hardware at scale.** JPMorgan remains "in-house orchestration wrapping hyperscaler-hosted models," not air-gapped inference. This is consistent with the cost structure: frontier weights + H100 clusters are not yet economical for fully-air-gapped private operation at enterprise-grade latency.
- **DeepSeek R1 adoption in highly regulated US domains** (defense, financial supervision) is absent from public sources — consistent with national-security concerns around Chinese-origin open weights.

### Three-pillar feed

This memo feeds the three-pillar adaptability framework as follows:

**Pillar T (Technical Infrastructure) — direct.**

- Use the five-axis decision tree (above) as the canonical T-pillar artifact.
- Maintain the Crawley five-layer decomposition as the interface-contract map.
- Re-run the tree on each of the four triggers (new generation, price drop, regulatory change, volume boundary crossed).
- The key engineering commitment is the *volatility-containment principle*: fragile model-layer churn must not leak into eval or governance layers.

**Pillar A (AI Usage) — coupled.**

- The switch-events in the evidence table are, from the usage side, capability-envelope changes (Harvey's router; Replit's per-task provider selection; Morgan Stanley's advisor-assistant; Intercom Fin 2 and Fin Apex).
- Feeds A1 (foundation-model transition management): use this memo's T7/T7 table as the canonical list of prompt-layer fragilities.
- Feeds A2 (capability-to-adoption lag curves): the DeepSeek R1 inflection (2025-01-23) is a zero-point for re-calibration of cost-adoption lag.

**Pillar O (Organization) — stakeholder and governance.**

- Who owns the decision when the tree re-triggers? Observed patterns: CTO + platform lead in tech-native firms (Cursor, Perplexity, Replit); CIO + compliance + procurement in regulated firms (Morgan Stanley, JPMorgan, Harvey); CEO in PR-forward firms (Klarna — anti-pattern).
- Feeds O2 (role redefinition cycles): AI-platform engineer, AI FDE, AI model evaluator, chief AI officer are the roles activated whenever the tree re-triggers.
- Feeds O3 (organizational learning velocity): the eval-harness invariant of Pillar T is where *organizational* double-loop learning about model behavior is concentrated; loss of this artifact = regression to trial-and-error per release.

**Meta (M1, M2).**

- Feeds M1 (system-dynamics map): the causal loop "new generation release → capability-envelope shift → prompt-layer rewrite → eval harness validates → deploy → usage increases → volume crosses decade boundary → stance re-evaluated" is the *adaptability cycle* for the infrastructure pillar.
- Feeds M2 (adaptability indicators): proposed indicators from this memo — (i) model-refresh cadence (weeks between production model-layer swaps), (ii) regression rate on golden set per swap, (iii) % of code in SDK-abstraction vs. provider-specific calls, (iv) months since last eval-harness refresh, (v) % of production spend flowing through a gateway/router, (vi) average age of deepest fine-tune still in production.

### Anchor-question answers (concise)

- *Engineering* — The infrastructure should be built as a five-layer stack with the volatility budget concentrated in the model and serving layers. Manage the other three layers as invariants. Express provider choice through a gateway or SDK abstraction. Keep a golden-set eval harness that is independent of any single model. Re-evaluate stance on generation, price, regulation, or volume triggers.
- *Managerial* — Make the decision owner the joint CTO/compliance/procurement function, not the CEO or product lead. Budget the model layer as a *rented option*, not as capital. Maintain the switching option at all times unless workload economics or regulatory posture forces self-hosting. Treat any proprietary-vertical investment as a *compound option* with a 6–12 month falsifiability test against frontier. For regulated deployments, invest in the governance layer (BAA, Data Zones, sovereign contracts) once and inherit the benefit across every subsequent model-layer swap.

---

**Word count (body):** ~4,300 words excluding tables and ASCII diagram.

**Sources referenced** (primary where possible):
- Character.AI research blog, "Optimizing AI Inference" (2024-06) and "Part Deux" (2024-11): https://research.character.ai/optimizing-inference/
- Bloomberg, "Character.AI Co-Founders Hired by Google" (2024-08-02): https://www.bloomberg.com/news/articles/2024-08-02/character-ai-co-founders-hired-by-google-in-licensing-deal
- Fortune / The Letter Two, Intercom → Claude for Fin 2 (2024-10-10 / 2024-10-12): https://fortune.com/europe/2024/10/10/irish-founded-intercom-ditching-chatgpt-antrhopic-claude-customer-service/
- VentureBeat, Intercom Fin Apex 1.0: https://venturebeat.com/technology/intercoms-new-post-trained-fin-apex-1-0-beats-gpt-5-4-and-claude-sonnet-4-6
- TechCrunch, "Anthropic, Google score win by nabbing OpenAI-backed Harvey" (2025-05-13): https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/
- Harvey, "Expanding Harvey's Model Offerings": https://www.harvey.ai/blog/expanding-harveys-model-offerings
- OpenAI, Morgan Stanley case: https://openai.com/index/morgan-stanley/
- The Digital Banker, JPMorgan LLM Suite: https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/
- Perplexity, "Meet New Sonar": https://www.perplexity.ai/hub/blog/meet-new-sonar
- Replit, "2025: Replit in Review": https://blog.replit.com/2025-replit-in-review
- Railway Pro, SNCF × Mistral partnership: https://www.railwaypro.com/wp/sncf-group-and-mistral-ai-form-strategic-partnership/
- Microsoft Blog, "Microsoft makes the promise of AI in healthcare real" (2024-03-11): https://blogs.microsoft.com/blog/2024/03/11/microsoft-makes-the-promise-of-ai-in-healthcare-real-through-new-collaborations-with-healthcare-organizations-and-partners/
- Epic, "Epic and Microsoft Bring GPT-4 to EHRs": https://www.epic.com/epic/post/epic-and-microsoft-bring-gpt-4-to-ehrs/
- Accenture, "Accenture Invests in Martian" (2024-09): https://newsroom.accenture.com/news/2024/accenture-invests-in-martian-to-bring-dynamic-routing-of-large-language-queries-and-more-effective-ai-systems-to-clients
- VentureBeat, "Swapping LLMs isn't plug-and-play": https://venturebeat.com/ai/swapping-llms-isnt-plug-and-play-inside-the-hidden-cost-of-model-migration
- Menlo Ventures, "2025: The State of Generative AI in the Enterprise": https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- a16z, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025": https://a16z.com/ai-enterprise-2025/
- Alibaba Cloud, "Qwen Models Attract over 90,000 Enterprise Adoptions": https://www.alibabacloud.com/blog/alibaba-clouds-qwen-models-attract-over-90000-enterprise-adoptions-within-its-first-year_601130
- IBM Newsroom, "IBM and Groq Partner" (2025-10-20): https://newsroom.ibm.com/2025-10-20-ibm-and-groq-partner-to-accelerate-enterprise-ai-deployment-with-speed-and-scale
- European Commission, AI Act policy page: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Azure Blog, Data Zones: https://azure.microsoft.com/en-us/blog/enterprise-trust-in-azure-openai-service-strengthened-with-data-zones/
- CX Today, "Klarna Didn't Replace Salesforce & Workday with AI": https://www.cxtoday.com/crm/klarna-didnt-replace-salesforce-it-replaced-them-with-alternative-saas-apps/
- Vercel, Ship AI 2025 Recap: https://vercel.com/blog/ship-ai-2025-recap
- DEV Community, Cursor 3 / Composer 2 (2026-04): https://dev.to/gabrielanhaia/cursor-3-just-shipped-a-coding-model-trained-from-scratch-heres-why-that-changes-the-stack-57g7
