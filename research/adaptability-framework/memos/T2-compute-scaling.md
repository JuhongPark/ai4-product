# T2 — Compute Scaling Under 10×/18-Month Demand Growth (2023–2026)

> **Track:** Adaptability Framework — Axis T (Technical Infrastructure)
> **Anchor questions fed:** engineering (primary) + managerial (secondary)
> **Date:** 2026-04-22
> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)

---

## i. Method

**Question.** How did non-frontier organizations (application-layer firms and mid-sized AI products) adapt their inference infrastructure to demand that grew by roughly 10× every 18 months across 2023–2026? What architectural decisions compounded (kept paying off across model generations, price cuts, and incidents), and which required full rewrite when QPS crossed an order-of-magnitude threshold?

**Scope.**
- *Inclusion*: firms that (a) operate an inference workload they do not train the foundation model for, and (b) published either engineering-blog detail, press-release scale signals, or were described in independent secondary coverage with absolute dates; plus (c) the inference-optimized providers and custom silicon they depend on.
- *Exclusion*: frontier training infrastructure at OpenAI / Anthropic / Google / xAI themselves (covered in T1 build-vs-rent). Inference at these labs is included only as context (provider-side behaviour that application firms routed around).

**Sources.** See appendix. Emphasis on primary engineering blogs (Character.AI, Harvey, Anthropic postmortem) and independent benchmark sources (Artificial Analysis, Epoch AI, SemiAnalysis InferenceMAX, a16z LLMflation).

**Evidence hygiene.** All dates are absolute (YYYY-MM or YYYY-MM-DD). Claims are labelled **[observed]**, **[inferred]**, or **[speculative]**. Negative evidence (data searched for but not found publicly) is recorded in §iv. Confidence labels (high / medium / low) are attached to pattern claims in §iii.

**SDM lens.**
- *Architecture decomposition*: five layers — compute (GPU / LPU / TPU / custom ASIC), serving (runtime + batching), caching (KV, semantic, inter-turn), routing (provider, model, region, priority), application (prompt, agent control).
- *Tradespace*: four-axis vector (cost, latency, throughput, quality); the Pareto frontier moved dramatically 2023 → 2026.
- *Resilience (Hollnagel)*: multi-provider routing as a Safety-II mechanism — degrade gracefully rather than fail binary.
- *Queueing theory*: at >1k QPS with heterogeneous request sizes, M/M/1 intuition breaks; batching is a throughput-latency tradeoff governed by a scheduler.

---

## ii. Evidence table

Scale tier shorthand: **T0** <100 QPS; **T1** 100–1k QPS; **T2** 1k–10k QPS; **T3** 10k+ QPS.

### (a) Mid-size AI product companies scaling inference

| Firm | Scale signal (date) | Architectural response | Cost / latency impact | Source |
|---|---|---|---|---|
| **Character.AI** | >20,000 QPS in prompt serving by 2024-06 (~20% of Google Search volume) [observed] | Custom serving stack; KV cache reduced >20× via Multi-Query Attention + cross-layer KV sharing; int8 quantization of weights, activations, and KV cache trained natively in int8 to avoid train/serve mismatch; inter-turn KV cache on host memory for long dialogues (avg 180 messages) | Serving cost reduced 33× since late 2022; 95% inter-turn cache hit rate; estimated >13.5× cheaper than commercial APIs at equivalent volume | Character.AI research blog 2024-06; Part Deux 2025-08 |
| **Cursor** | ~400M AI requests/day reported 2025 [observed]; editor latency SLO ~<200 ms first-token [inferred from product behaviour] | Custom serving with Fireworks AI partnership; speculative edits using existing source code as draft tokens; custom fine-tuned 70B model served at ~1,000 tok/s (reported ~13× speedup over naive serving); context engine retrieves ~13k tokens from million-line codebases | Editing latency low enough to feel like autocomplete; cost per suggestion unpublished but clearly sub-cent to sustain free tier | Fireworks partnership announcement; Cursor engineering writeups (secondary reporting) |
| **Notion** | Not disclosed in QPS; Q&A and embeddings workload migrated 2024-05 to serverless [observed] | Multi-provider strategy (OpenAI, Anthropic, Fireworks, Baseten, Google); fine-tuned specialized small models for high-volume tasks (auto-fill, summarization); serverless embedding pipeline | Embedding cost down ~50% vs. peak dedicated-pod cost; latency halved on auto-fill via specialized model | Notion–Braintrust case 2025; ZenML LLMOps DB |
| **Harvey** | Millions of daily LLM requests; billions of prompt tokens + hundreds of millions of output tokens/day [observed]; "bursty" load pattern | Centralized Python library abstracting all model I/O; in-house OpenAI-compatible proxy service; parallel deployments per model family with weighted selection on (health, capacity, region); layered fallbacks; periodic SLI (latency + success) driving deployment weights | Enables cross-provider failover without changing application code; resilience mechanism is declared, incidents not quantified in public | Harvey "Resilient AI Infrastructure" engineering blog (2024–2025) |
| **Klarna** | 2.3M conversations in first month of deployment (2024-02 to 2024-03) [observed]; equivalent to 700 FTEs of handling capacity | OpenAI GPT-based AI assistant fronting support; application layer built in-house; handles two-thirds of chats | ~$40M estimated profit improvement (2024); resolution time 11 min → 2 min; but by 2025 CEO Siemiatkowski admitted cost-driven model selection produced "lower quality" — company began rehiring human agents | OpenAI case study (Klarna); PromptLayer case 2025; Klarna press 2024-02 |
| **Perplexity** | Sonar Pro launched 2025-03-07 at $3 / $15 per M tokens input/output [observed]; consumer Pro plan $20/mo | Retrieval + generation coupled; Sonar model (API product) billed includes search "tax"; later (2026) stopped billing citation tokens to lower effective cost | Pricing stable since launch despite underlying cost declines — indicating Perplexity absorbed declines as margin rather than passing them through [inferred] | Perplexity API docs; pricing pages |
| **Hebbia** | 30% of top 50 asset managers by AUM as clients [observed]; no public QPS | Matrix decomposition architecture (ISD: Inference, Search, Decomposition); retains full documents rather than RAG snippets; multi-step agent plans | Longer completion times traded for higher task success in complex analyst workflows; multi-model orchestration (not named) [inferred] | Hebbia Inquirer profile; Cuckoo AI deep dive 2025-06 |
| **Sierra** | Reached $100M ARR in ~7 quarters (launch 2024-02 → 2025-Q3) [observed]; no public QPS | Multi-agent architecture per customer deployment; custom per-client voice agents; unclear public detail on routing | Scale implies multi-provider orchestration [inferred]; negative evidence on architectural detail | Sierra "Year Two in Review" blog; CNBC 2024-10 |
| **Glean** | Enterprise knowledge graph spanning customer SaaS corpora | Not publicly detailed at QPS level; depends on embedding + reranking pipeline | Vertical defensibility cited as moat; not cost frontier | Sequoia 2025-11 analysis (secondary) |
| **Duolingo** | Birdbrain processes 1.25B daily exercises [observed]; 148 new AI-generated courses in 1 year (doubled library) | GPT-4 roleplay features; in-house Birdbrain system; two-hour weekly AI-learning blocks for engineers | No public inference-cost figures; "AI-first" declaration 2025 | Duolingo blog; company press 2024–2025 |
| **Intercom** | Fin AI agent handles support; no public QPS | Multi-model strategy; Fin 3 launched on Anthropic + OpenAI mix [inferred from product changelog] | Per-resolution pricing model (outcome-based) | Secondary reporting; not deeply documented publicly |
| **Canva** | Generative AI features (Magic Studio) shipping to ~200M MAU-scale base | Multi-modal (image, video, text) with underlying providers and Canva-trained models | No inference-cost detail published | Secondary reporting |
| **Replit** | Replit Agent launched 2024-09; code-indexing over 300M+ repos [observed] | Strong task-priors to reduce inference work; relies on Anthropic Claude for agent reasoning | Cost per session material — tiered pricing reflects it | Replit engineering blog "How Replit makes sense of code at scale" |
| **Linear** | AI features (autofill, smart routing) on small-model spine | Fine-tuned small models for structured mutation tasks [inferred from product behaviour]; minimal frontier-model dependence | Cost absorbed into per-seat pricing | Negative evidence: no detailed engineering post found publicly |

### (b) Inference-optimized providers and hardware

| Provider / HW | Milestone (date) | Capability | Market role |
|---|---|---|---|
| **Groq (LPU)** | Llama 2 70B at 241 tok/s (2024-02); Llama 3 70B at 284 tok/s and 8B at 877 tok/s (2024-04); Llama 3.3 70B at 276 tok/s, with speculative decoding at 1,665 tok/s on Nov 2024; "artificial analysis" benchmarks repeatedly topped by Groq [observed] | LPU deterministic architecture; SRAM-heavy design | Latency-frontier provider; pricing competitive on Llama family |
| **Cerebras (WSE-3)** | Launched inference 2024-08 at 450 tok/s on Llama 3.1 70B; 969 tok/s on Llama 3.1 405B (2024-11); 2,100 tok/s on Llama 3.3 70B (2025-H2) — 3× improvement [observed] | Wafer-scale engine; 7,000× memory bandwidth vs H100 | Latency frontier for open-weight models |
| **AWS Trainium2 / Inferentia2** | Project Rainier with Anthropic; Anthropic expected to run on >1M Trainium2 chips by end-2025 [observed] | Claimed up to 50% lower training cost, up to 40% lower cost/inference vs GPU | Captive silicon for Anthropic + broader Bedrock customers |
| **Google TPU v5e → v6 (Trillium)** | v5e at $1.20/chip-hour; Trillium at $1.375/hour on-demand, $0.55 with commitment; Trillium gives ~2× inference throughput vs v5e on Llama2-70B and ~1.8× perf/$ [observed] | TPU v6 GA 2024-Q4; v7 announced 2026-04 | Google-captive + Google Cloud customers; Anthropic also on TPU |
| **Fireworks** | $315M annualized revenue 2026-02 (+416% YoY) [observed]; 10T tokens/day by 2025-10; powered Cursor's 1,000 tok/s Llama 3 70B | Serverless + dedicated + per-GPU-second; fine-tune + RL-fine-tune offerings | Application-tier partner of choice for open-weight fine-tunes |
| **Together** | $305M Series B 2025-02; ~$150M ARR [observed] | Serverless + dedicated; dedicated-endpoint break-even cited at ~130k tok/min | Similar positioning to Fireworks; strong open-weight catalogue |
| **Baseten** | $300M Series E at $5B valuation 2026-02 [observed] | Enterprise inference engine focus; custom and proprietary models; VPC deployment | Enterprise serving, often for fine-tuned in-house models |
| **Modal** | Series B $87M at $1.1B valuation 2025-09 [observed]; GPU snapshotting alpha 2025 | Arbitrary Python; sub-second cold starts by late 2025 | Platform for custom inference + non-LLM ML |
| **Lepton / Replicate / RunPod** | Three distinct models: Lepton (platform), Replicate (model marketplace + serverless), RunPod (raw GPU) | Sub-second cold start by end-2025 on leading platforms | "Long tail" serving + prototyping + batch |

### (c) Token-price & latency frontier — the Pareto frontier moved

Values below are canonical public list prices per 1M tokens (input/output), with 72-hour rolling tok/s from Artificial Analysis where cited. Dates rounded to release month.

| Date | Frontier model | Input / Output ($/1M) | Speed (tok/s) | Frontier-equivalent floor (GPT-4-class task) |
|---|---|---|---|---|
| 2022-11 | GPT-3.5 Turbo | $2 / $2 (legacy)* | ~50 | $20 / 1M tokens |
| 2023-03 | GPT-4 (8k) | $30 / $60 | ~20 | GPT-4 only |
| 2023-11 | GPT-4 Turbo | $10 / $30 | ~30 | GPT-4 Turbo only |
| 2024-05 | GPT-4o | $5 / $15 | ~80 | GPT-4o |
| 2024-06 | Claude 3.5 Sonnet | $3 / $15 | ~80 | Claude 3.5 Sonnet |
| 2024-07 | **GPT-4o-mini** | **$0.15 / $0.60** | ~110 | Floor drops to sub-$1 / 1M tokens for GPT-4-class |
| 2024-09 | o1-preview | $15 / $60 | reasoning | Reasoning premium emerges |
| 2024-12 | o3 (announced) | $10 / $40 | reasoning | Reasoning frontier |
| 2025-01 | **DeepSeek V3/R1** | $0.55 / $2.19 (R1) | ~60 | ~27× cheaper than o1 at similar task performance; triggers 18% NVDA drop 2025-01-27 |
| 2025-03 | Gemini 2.5 Flash | $0.30 / $2.50 | ~150 | Low-cost capable floor below $1 / 1M |
| 2025-06 | **o3 repriced** | $2 / $8 (-80% cut) | reasoning | Reasoning cost falls 5× in ~6 months |
| 2025-09 | Claude Opus 4.x | $15 / $75 | ~50 | Frontier Opus tier |
| 2026 | Gemini 2.5 Pro | $1.25 / $10 | ~120 | Undercuts GPT-5-class |
| 2026 | Claude Opus 4.7 | $5 / $25 | ~60 | Opus frontier cut 67% from 4.1 to 4.7 |
| 2026 | GPT-5.4 | $2.50 / $15 | ~90 | GPT-4-level tasks now at $0.40 / 1M tokens blended |

*Sources: OpenAI / Anthropic / Google pricing pages retrieved via Internet Archive; Epoch AI; a16z LLMflation; Artificial Analysis leaderboards.*

**Headline frontier-shift claims** (all [observed]):
- a16z (Appenzeller, 2024-11): GPT-4-equivalent inference cost fell from ~$20 per 1M tokens (late 2022) to ~$0.40 (late 2024) — 10× / year, which extrapolates to ~1,000× over three years.
- Epoch AI: post-2024-01, per-benchmark task price declines accelerated from median ~50×/yr to ~200×/yr; highest observed decline 900×/yr on selected benchmarks.
- DeepSeek V3/R1 (2025-01): forced the whole market's reasoning-tier floor down ~20–50× within six months; OpenAI's o3 cut 80% in 2025-06 directly attributable [inferred].

### (d) Multi-provider routing and fallback under incident / price-shock conditions

| Incident / event | Date | Description | Routing response pattern |
|---|---|---|---|
| **Anthropic 1M-context routing bug** | 2025-08-05 → 2025-09-18 | Sonnet 4 requests misrouted to 1M-ctx servers; initial 0.8% impact escalated to 16% at peak (2025-08-31) because a load-balancing change sent short-context requests to the wrong pool; "sticky" routing compounded; bug fix deployed 2025-09-04, rolled to Vertex 2025-09-16, Bedrock 2025-09-18 | Teams with health-based weighted routing (e.g., Harvey pattern) shed traffic off Anthropic direct API toward Bedrock / Vertex or alternative providers |
| **Anthropic TPU quantization / token-sampling bug** | 2025-08-25 → 2025-08-26 | Misconfiguration on Claude API TPU servers produced rare tokens (Thai / Chinese characters in English outputs); approx. 30% of Claude Code users saw at least one degraded response | Enterprise consumers of Claude Code shifted to other coding tools temporarily; Anthropic published postmortem 2025-09-17 |
| **Anthropic weekly rate-limit tightening** | 2025-07 → 2025-08 | Anthropic introduced weekly limits on Pro/Max; Opus 4 subject to distinct cap; peak-hour tightening 2026-03 | OpenRouter :nitro and :floor routes; developers fan out to OpenAI / Google; Claude Code usage caps discussed in Anthropic community 2026-03 |
| **Azure OpenAI GPT-5.2 outage** | 2026-03-09 → 2026-03-10 | Configuration update incompatible with production engine; HTTP 400 + HTTP 429 errors; secondary telemetry bug concentrated traffic to limited regions, producing knock-on 429s during rollback | Multi-provider gateways (OpenRouter, LiteLLM) routed around Azure; customers with only Azure endpoints saw hours of degradation |
| **Azure datacenter power outage → ChatGPT down** | 2024-12 | Azure DC power failure knocked ChatGPT offline for hours | Consumer product; API path had partial mitigation via other regions |
| **DeepSeek price shock** | 2025-01-20 → 2025-01-27 | DeepSeek R1 launched; within a week became #1 iOS app in the US; Nvidia share price down 18% 2025-01-27 | Consumer apps (Perplexity among them [inferred from pattern]) evaluated DeepSeek routing; OpenAI cut o3 price 80% in 2025-06; OpenRouter added DeepSeek routes within hours |
| **GPT-4o-mini price shock** | 2024-07-18 | $0.15 / $0.60 per 1M tokens — 60% below GPT-3.5 Turbo; GPT-4-class intelligence at GPT-3.5 cost | Downstream firms (Notion, Intercom) moved high-volume tasks off GPT-3.5 within ~30 days [inferred]; internal routing rules updated to prefer mini on short completions |
| **o3 price drop** | 2025-06 | OpenAI cut o3 API 80% | Enterprises who had held off reasoning adoption on cost grounds flipped evaluator agents and code-review pipelines to o3 |
| **Azure PTU / reservation economics** | 2024–2026 | Azure introduced hourly PTU billing + reservations; up to 64% discount monthly, 70% yearly | Enterprises with consistent >130k tok/min volume moved to PTU; bursty workloads stayed on pay-per-token or mixed |
| **Martian router** | From 2023-11 | Dynamic LLM router; Accenture investment 2024-09; claims up to 98% cost savings | Pattern of "spend-optimal routing" became a category alongside OpenRouter's uptime/price approach |

---

## iii. Pattern findings (with confidence labels)

### Scaling-phase transition map (primary artifact)

```
  QPS     |  Architecture (compute → serving → caching → routing → app)        | What breaks when you cross the boundary
 --------- +-------------------------------------------------------------------- +-----------------------------------------------
  <100     |  Direct provider API calls (OpenAI / Anthropic / Bedrock)           |  Nothing — but you have no telemetry to see
 (T0)      |  Single model, single provider                                      |  breakage coming.
           |  Naive prompt templates; no caching                                 |
           |  Thin wrapper client                                                |
 --------- +-------------------------------------------------------------------- +-----------------------------------------------
  100–1k   |  Same compute plane, but now behind a rate-limited SDK              |  First rate-limit (429) events hit; naive retry
 (T1)      |  A **queue** in front of the client (Redis / SQS); async workers    |  amplifies the incident (retry storms);
           |  Prompt-level + response-level **cache** (LRU / Redis) keyed on     |  providers' hidden back-pressure surprises you.
           |   canonicalized prompts                                             |  p99 latency explodes before average does.
           |  **Central client library** with uniform telemetry                  |  Without caching, unit economics go negative on
           |  Begin *one secondary provider* for disaster fallback               |  "ask the same question twice" traffic.
 --------- +-------------------------------------------------------------------- +-----------------------------------------------
  1k–10k   |  **Dedicated / provisioned endpoints** for hot paths                |  Serverless API rate-limits become binding;
 (T2)      |   (Azure PTU, Anthropic Bedrock provisioned, Fireworks dedicated)   |  cold-start variance kills latency SLO.
           |  **Batching** (continuous batching via vLLM / TGI / TensorRT-LLM);  |  Static batching can't handle variable output
           |   dynamic admission control; SLO-aware schedulers                   |  lengths — GPUs sit idle mid-batch.
           |  **Multi-model routing**: frontier for hard tasks, distilled/small  |  A single-provider outage now = company outage;
           |   for high-volume; reasoning only when justified                    |  public incident for your own customers.
           |  **Multi-provider routing** with health-weighted selection          |  Prompt versioning matters: silent regressions
           |   (Harvey pattern)                                                  |  on provider updates hit your users first.
           |  Semantic / KV-reuse caching (Anthropic prompt caching, in-house    |
           |   inter-turn caching for chat products)                             |
 --------- +-------------------------------------------------------------------- +-----------------------------------------------
  10k+     |  **Custom serving** on owned fleet (Character.AI pattern) or        |  Provider APIs cannot be operated inside a
 (T3)      |   contracted dedicated inference (Cerebras / Groq / Fireworks)      |  consumer-latency budget at your scale —
           |  **Model distillation / specialization** — you no longer call a     |  you bought a model, not an API.
           |   frontier model for >50% of traffic                                |  Memory bandwidth is the true constraint;
           |  **KV-cache engineering**: multi-query / grouped-query attention,   |  treat it as architecture, not optimization.
           |   cross-layer KV sharing, int8 / fp8 KV cache, inter-turn KV        |  Training / serving code-path drift becomes an
           |   reuse on host memory                                              |  existential risk — quantize from training time.
           |  **Regional / multi-cloud** deployment for survivability and        |  Regulatory + sovereignty constraints force
           |   latency                                                           |  routing rules that can't be centralized.
           |  Custom scheduler, p99-aware admission                              |  Fallback to a public API is no longer a plan;
           |  Continuous-learning draft-model loops (online speculative          |  provider cannot absorb your burst.
           |   decoding)                                                         |
```

**How to read the map.** The rightmost column is the load-bearing part — it names what *breaks at the next order of magnitude*. Each row is a boundary event, not a menu of options. Firms that cross a boundary without adopting the listed architecture accrue what T3 calls "inference-serving tech debt" (see that memo).

### Price-latency frontier movement (second primary artifact)

Movement of the (cost, latency, quality) Pareto frontier, interpreted as capability accessible at ≤$1 per 1M output tokens and ≤50 tok/s latency budget:

| Year-end | What was on the Pareto frontier at ≤$1 / 1M tokens & usable latency | What was frontier-only (no cheap substitute) |
|---|---|---|
| 2023 | Nothing at <$1 / 1M tokens with GPT-4 quality. GPT-3.5 at ~$2/$2 was the floor. | GPT-4 ($30/$60). Claude 2 at similar tier. |
| 2024 | GPT-4o-mini ($0.15/$0.60), Claude 3 Haiku ($0.25/$1.25), Gemini 1.5 Flash (~$0.35/$1.05). GPT-4-class tasks for first time <$1. | o1-preview reasoning ($15/$60). Long-context 1M+. Multimodal video. |
| 2025 | GPT-4o-mini, Gemini 2.5 Flash, DeepSeek V3/R1 (~$0.55/$2.19 even for reasoning), Claude Haiku 4.5. Reasoning tier falls below $3/M output. | Pure frontier (GPT-5-class, Opus 4.x) still at $15+/75. Computer-use agents. |
| 2026-04 | Gemini 2.0 Flash ($0.10/$0.40), Claude Haiku 4.5, Mistral Nemo ($0.02/M blended). Reasoning at ~$2/$8 for o3-repriced. | Max-effort Opus 4.7 ($5/$25), GPT-5.4 Pro ($30/$180). Gap "cheap↔premium" now ~1,000× (Nemo vs o1-pro blended). |

Interpretation: the **floor** moved ~50× down per year; the **ceiling** moved down ~3–5× per year. The spread widened. Application teams that anchored architecture on "frontier or nothing" in 2023 over-paid by 10–100× through 2025; teams that anchored on "cheap or nothing" missed the reasoning tier's separate frontier. **Two frontiers now coexist** (capable-and-cheap for volume; frontier-and-costly for hard tasks), and routing is the mechanism that reconciles them.

### Pattern P1 — Multi-provider routing is Safety-II resilience, not cost arbitrage

**Claim.** The dominant purpose of multi-provider routing at T1–T2 is *graceful degradation under provider incidents and model-quality regressions*, not cost optimization.

**Evidence.** Harvey's engineering blog explicitly frames its proxy + weighted routing in resilience terms (health SLIs drive selection, not price). The Anthropic August–September 2025 routing-bug postmortem shows that a single-provider enterprise would have had 16% of Claude Sonnet 4 traffic degraded at the worst hour with no architectural escape hatch — the customers who stayed functional had already built cross-provider paths. Azure's March 2026 GPT-5.2 outage and the December 2024 datacenter power loss reinforced the same lesson. **Confidence: high.**

**SDM framing.** This is a direct instantiation of Hollnagel's Safety-II: systems that succeed under varying conditions are those that adjust performance before failure is binary. The routing layer is the "performance adjustment" mechanism. Rhodes' "system resilience" likewise reframes resilience as capacity-for-adjustment, not redundancy — and weighted-health routing is adjustment, not backup.

### Pattern P2 — Caching is the throughput multiplier; unit economics inverts without it

**Claim.** At >1k QPS, caches turn negative unit economics positive. Character.AI's 95% inter-turn cache rate is the reason their cost fell 33× — not any single model improvement.

**Evidence.** Character.AI 2024-06 post: KV cache on host memory + multi-query attention + int8. Anthropic launched prompt caching in 2024-Q3 specifically so downstream customers could survive the surge from agentic workloads (agents repeatedly send overlapping context). OpenAI and Google followed with implicit prompt caching. DeepSeek's MLA is a fundamentally *cache-reduction* architecture: ~93.3% less KV per query. **Confidence: high.**

**SDM framing.** This is a classic queueing result: in an M/G/1 system with cacheable work, effective arrival rate is λ(1−h) where h is the hit rate. h=0.95 is a 20× reduction in effective load — more than any realistic GPU uplift per year. Compute matters; cache matters more.

### Pattern P3 — Batching is the throughput-latency tradeoff at 1k–10k QPS

**Claim.** At T2 scale, continuous batching (vLLM / TGI / TensorRT-LLM) is the difference between GPU utilization of ~30% and ~80%, which is the difference between the workload being economic and being unaffordable. Static batching is *actively worse than naive serial* past a certain batch-size / variance threshold.

**Evidence.** vLLM public claims of ~24× throughput over HuggingFace Transformers. SemiAnalysis InferenceMAX documents how Blackwell + vLLM + continuous batching gives ~4× throughput at similar latency versus Hopper on the same models. Anyscale's original continuous-batching post showed 23× throughput and 50% p50 latency reduction. **Confidence: high.**

**SDM framing.** Batching is the scheduler in a classic server-system problem. The "control variable" is batch-size; the "disturbance" is heterogeneity in output length. Continuous batching replaces global batch boundaries with iteration-level scheduling — formally, it converts a batch-closed system into an open queueing network, which fundamentally changes the throughput-latency tradeoff curve.

### Pattern P4 — Distillation + custom serving are the only T3 paths

**Claim.** At >10k QPS with cost-per-token targets below frontier list prices, the only two architectures that survive are (a) own-fleet custom serving with a distilled / specialized model, or (b) contracted dedicated inference with a distilled / specialized model. Naive API-on-frontier does not cost in.

**Evidence.** Character.AI's 33× cost reduction was not a provider change — it was model-co-design with serving. Cursor's 1,000 tok/s on Fireworks' custom 70B is the same pattern via partnership rather than in-house. Notion openly states it is fine-tuning open-weight models to reduce frontier-pricing dependence. Klarna's partial rollback to human agents (2025) is the negative evidence for (c) "stay on frontier API at all costs" — it was unaffordable at target quality. **Confidence: high.**

**SDM framing.** This is Christensen-style disruption inside the inference layer: the "too-good-for-the-job" frontier model loses volume to the "just-right" distilled model wherever task complexity permits. The architecture implication is a *bimodal stack*: routing-layer decisions on "is this task hard enough to need the frontier?" become the commercial lever.

### Pattern P5 — What compounds vs. what requires rewrite

| Decision | Compounds? | Why |
|---|---|---|
| Centralized client library / proxy (all model calls through one choke point) | **Compounds** | Gives observability, unified retry/backoff, prompt-version logging, provider swap without app change. Harvey is exhibit A. |
| Prompt → response cache keyed on canonicalized prompt | **Compounds** | Survives any model swap; value grows as traffic grows. |
| Multi-provider routing with health SLI | **Compounds** | Each added provider widens the safety envelope; rules layer lives on top of model generations. |
| Provider-specific SDK wiring throughout the app | **Rewrite** | Broke at Claude 3 → Sonnet transition (different tool-use schema); breaks again at every major provider update. |
| Hard-coded model name in prompt templates | **Rewrite** | Broke at GPT-4 Turbo deprecation; at Claude 3.5 → 4 transition; at o1 → o3 reasoning-output shape change. |
| Single-region dedicated endpoint | **Rewrite at T3** | Compounds until the capacity cap is hit, then requires full regional rewrite under SLO pressure. |
| KV cache / batching assumptions tuned to one model architecture | **Rewrite** | GQA vs MQA vs MLA differences break throughput assumptions; DeepSeek V3 → MLA breaks vLLM paging heuristics until patched. |
| Fine-tuned small model on top of a frozen base | **Rewrite on base change** | New base = redo fine-tune. But the *data + evaluator + serving* around it compound. |
| Provisioned throughput (PTU) sized for last quarter's load | **Partial rewrite** | Capacity plan itself is continuously renegotiated; PTU contract structure is stable. |

**Confidence: medium–high.** The classification depends on team maturity and how much abstraction was built up front. A firm that builds the proxy + routing abstractions at T1 compounds; a firm that "just calls the API" will still have that as a rewrite when it crosses T2.

### Pattern P6 — The DeepSeek price shock forced global re-architecture inside 6 months

**Claim.** The January 2025 DeepSeek V3/R1 release was the single most consequential incident of the period for routing architecture, because it moved the *reasoning* tier's floor 20–50× in two weeks. Every serious router (OpenRouter, Martian, LiteLLM, in-house Harvey-style) added DeepSeek as a first-class route within days. OpenAI cut o3 80% by June 2025 — a directly attributable competitive response.

**Evidence.** Nvidia's -18% drop on 2025-01-27 is the public-market tell. OpenAI's own o3 cut date (June 2025) and magnitude (80%) align with a competitive repricing. Epoch AI's price-trend acceleration (50×/yr → 200×/yr median post-2024-01) absorbs the DeepSeek shock as an inflection. **Confidence: high.**

**SDM framing.** This is a coupled-system shock on the price axis of the tradespace. Price-axis shocks have historically been absorbed by quality-axis positioning ("you get what you pay for"); DeepSeek's contribution was to land near the top-right of the reasoning frontier at a fraction of the price — which collapses the Pareto set by ~1.5 decades on one axis without surrendering the other.

---

## iv. Open questions / negative evidence

- **Missing QPS data.** Public QPS figures exist for Character.AI (>20k), Cursor (~400M requests/day), Duolingo's Birdbrain (1.25B daily exercises) and Klarna (2.3M conversations/month). We could **not find public QPS** for Notion, Linear, Intercom, Canva, Glean, Sierra, Hebbia, or Harvey. Scale signals are indirect (client count, ARR, token volume). Any scaling-phase claim for these firms is an inference from scale-adjacent signals, not a measurement.
- **Missing routing-cost savings.** Harvey, Notion, and Sierra all imply multi-provider routing, but do **not** publish cost reductions attributable to routing alone (distinct from caching, distillation, and price declines). Martian's "up to 98%" claim is vendor-supplied, not independently audited.
- **Missing post-incident change logs.** Anthropic's August 2025 postmortem is unusually detailed; Azure's March 2026 GPT-5.2 outage is described; but we could **not find public postmortems** from application-layer firms describing how their routing layer actually performed during the incidents. Harvey's blog describes the design; it does not narrate the incident behaviour.
- **Character.AI post-Google.** After Google's 2024 licensing deal with Character.AI and the departure of key founders, the subsequent evolution of Character.AI's bespoke serving stack is not public. The 2025-08 "Part Deux" post fills part of the gap but does not describe organizational continuity.
- **"GPT-4o-mini shock" absorption.** While the price was obvious (2024-07-18), the downstream *architectural* response inside Notion, Intercom, etc., is inferred from product changes and scattered interviews — not directly narrated in an engineering blog.
- **Regional routing vs. sovereignty.** Several firms (Harvey, Glean, Sierra) have EU customers subject to data-residency rules, which presumably constrains their routing layer. Public detail on how routing rules encode sovereignty is thin. Treat this as a significant T3 unknown.
- **Queueing-model validation.** The claim that M/G/1 intuition with h=0.95 cache hit implies 20× effective load reduction is theoretically correct but **not validated against any firm's published data**. No firm publishes cache-hit elasticities with enough granularity to fit a curve.
- **Inference-compute growth rate.** The "10× every 18 months" figure from the prompt is consistent with a16z's LLMflation chart (10× per year on cost decline ~= 10× per 18 months on demand growth if quality-adjusted) but is itself an estimate. A precise per-firm compute-growth rate was not publicly available for most subjects.

---

## v. Three-pillar feed

### Feed to Axis A (AI usage)

- The **two-frontier structure** (cheap-and-capable vs. frontier-and-costly) means "choose the model" is no longer a one-off decision — it becomes a *per-request* policy encoded in the routing layer. A1 (model transition management) should treat transitions as multi-model blends, not single-model swaps.
- **Price shocks re-enter the model-selection decision without warning**. DeepSeek's January 2025 shock means every model-selection policy has a <90-day half-life against a new entrant. A1's decision tree needs a "price-shock trigger" branch.
- The **reasoning-tier sub-frontier** moved independently of the base-model frontier. A2 capability-adoption lag curves should measure reasoning-tier adoption separately.

### Feed to Axis O (organization)

- The **centralized client library / proxy** (Harvey pattern) is not just a technical artifact — it *implies an organizational unit* whose job is to own model-I/O abstractions across products. At firm sizes where that unit does not exist, infrastructure brittleness is predictable. O2 (role redefinition) should track this as a recurring 2024–2026 role creation.
- **Multi-provider routing requires provider-contract management** as an ongoing capability: PTU reservations, dedicated endpoints, Bedrock vs. Vertex allocation. This is a blend of procurement, FinOps, and reliability engineering — a genuine new role at mid-size AI firms.
- **Klarna's rollback from AI-only to human-hybrid** (2025) is the single most important organizational case in this memo: demand-driven cost optimization produced quality regression, which required hiring back. The lesson for O3 (organizational learning) is that *infrastructure choices and workforce choices are coupled* — you cannot cost-optimize the model and keep the humans the same.

### Feed to Axis T

- **Compounding vs. rewrite** is the most actionable categorization (P5). Any T1 decision framework (build vs. rent) should explicitly score on this axis: a "rent" decision that forces you to rewrite your routing layer at T3 is more expensive than a "build" decision that compounds.
- **Batching and caching** belong in T3 (technical debt) as *engineered dependencies*: they are not bolt-on optimizations, they are structural assumptions. When an upstream provider changes its KV cache semantics (e.g., the MLA transition), the downstream batching regime must change with it.
- **Regional / sovereignty routing** is a T2 sub-problem that becomes a T3 constraint. The earlier it is admitted into the architecture, the less rewrite it costs.

### Feed to M (cross-pillar)

- For the M1 systems-dynamics map: **caching-rate** and **routing-provider-count** are two stocks that compound, while **frontier-model-spend** is a flow that drains unless those stocks grow. The balancing loop "price shock → routing adds provider → cache warms → cost falls" has a ~90-day delay observed across DeepSeek (2025-01), o3 cut (2025-06) — that delay itself is the variable of interest.
- For M2 indicators: two concrete measurable indicators emerge from this memo — (1) *incident-aware route-miss rate* (% of traffic that hit a provider within 5 minutes of that provider's incident start), and (2) *price-shock absorption lag* (days between a ≥3× price drop and that price being reflected in ≥50% of affected routes). Both should be added to the M2 dashboard.

---

## Appendix: Sources cited

Primary engineering / research: Character.AI "Optimizing AI Inference at Character.AI" (2024-06) and "Part Deux" (2025-08); Harvey AI "Resilient AI Infrastructure"; Anthropic "A postmortem of three recent issues" (2025-09-17); a16z "Welcome to LLMflation" (Appenzeller, 2024-11); Epoch AI "LLM inference prices have fallen rapidly but unequally across tasks"; SemiAnalysis InferenceMAX and "Groq Inference Tokenomics"; Anyscale continuous-batching post; vLLM engineering blog; OpenRouter routing and fallback docs; Microsoft Foundry PTU docs; Klarna press (2024-02) + OpenAI case study; Cerebras and Groq press releases (2024–2025); Google Cloud Trillium GA; Fireworks/Together/Baseten/Modal announcements.

Secondary: Artificial Analysis and llm-stats leaderboards; Notion–Braintrust case + ZenML LLMOps DB; Cursor writeups (Data Science Collective); Sequoia 2025-11 app-layer analysis; OpenAI/Anthropic/Google pricing via Internet Archive; TechCrunch/VentureBeat/The Register incident coverage; Martian/Accenture press (2024-09).
