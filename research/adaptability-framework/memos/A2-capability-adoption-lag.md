# A2 — Capability-to-Adoption Lag Curves

> **Status:** research_memo (draft; source audit pending)
> **Date compiled:** 2026-04-22
> **Research prompt:** A2 (Axis A, Pillar 1 — AI Usage Framework)
> **Parent plan:** [Research plan](../plan.md)
> **Evidence window:** 2022 Q4 – 2026 Q1
> **SDM lens:** each capability treated as a **release** moving through a lifecycle (experimentation → pilot → production → commoditization); enterprise adoption gated by **balancing loops** (compliance, integration surface, change management, ROI visibility).

---

## i. Method

### Research object

The unit of analysis is a **capability wave** — not a model version, not a vendor, not a product. A capability wave is a discrete AI primitive that became exercisable in production at a specific moment. The waves examined in this memo, drawn from the anchor list in the parent plan:

1. Function calling / tool use (OpenAI June 2023; Anthropic follow-on 2024)
2. Vision / multimodal input (GPT-4V September 2023; Claude 3 March 2024; Gemini 1.5)
3. Long context (Claude 100k May 2023; GPT-4 Turbo 128k November 2023; Gemini 1.5 Pro 1M February 2024)
4. Reasoning / inference-time scaling (o1-preview September 2024; o1 December 2024; o3 December 2024; DeepSeek R1 January 2025; Claude 3.7 Sonnet extended thinking February 2025)
5. Agents (AutoGPT March 2023; Claude computer use October 2024; OpenAI Operator January 2025; ChatGPT agent mid-2025)
6. Computer use (Claude October 2024; Operator January 2025)
7. Multimodal generation (GPT-4o audio May 2024; Sora December 2024; Veo 2 December 2024)

### Three lag measurements per wave

Following the prompt:
- **(a) Release → first public enterprise production deploy.** The first named, non-demo enterprise whose workload ran the capability in production, confirmed by vendor case-study page, press release, or press coverage dated within weeks of release.
- **(b) Release → 50% enterprise adoption.** The month in which roughly half of enterprise survey respondents (Menlo Ventures, Ramp AI Index, a16z CIO panel, Stack Overflow Dev Survey, S&P 451, IDC) reported either testing or production use of the capability.
- **(c) Release → commoditization.** The month at which either (i) price per million tokens / per call collapsed by ≥50% under new entrants, or (ii) open-weight models (Llama, Qwen, DeepSeek, Mistral) reached rough parity on the specific capability.

### Sourcing

- Primary: vendor release notes, model cards, system cards, Anthropic and OpenAI engineering blogs, Google DeepMind release posts, Meta Llama release notes, DeepSeek paper / model card.
- Enterprise adoption: Menlo Ventures *State of Generative AI in the Enterprise* (2023, 2024, 2025), a16z *Enterprise AI* panel (2024, 2025) and *How 100 Enterprise CIOs are Building and Buying Gen AI in 2025*, Ramp AI Index (monthly), Stack Overflow Developer Survey (2024, 2025), KPMG AI Pulse (Q1 2026), Deloitte *State of AI in the Enterprise* (2026), PwC Agentic AI tracker, IDC / AWS agent adoption study (Nov 2025).
- Financial / press: TechCrunch, Bloomberg, CNBC, InfoQ.

### Confidence labels

Each claim in Section iii carries one of:
- **[High]** — multiple independent surveys or vendor disclosures converge within ±10%.
- **[Medium]** — one reliable survey plus triangulating evidence.
- **[Low]** — single-source or inferred.
- **[Speculation]** — forward extrapolation, labeled as such.
- **[Negative evidence]** — absence noted explicitly.

### What this memo does not do

It does not measure revenue, seat count, or deployment depth. A capability is counted as "in production" once someone ships it; it is counted as 50% adopted when survey panels say half their peers are running it. Depth-of-use is a separate research object (see companion prompt A3).

---

## ii. Evidence Table — capability-adoption velocity chart

Lag is measured in months from **initial public release** to the target milestone. "~" marks interpolated months where surveys did not fall on the exact anniversary. "n/a" marks negative evidence (see Section iv). Bold is the capability; italics are the specific release.

| Capability wave | Release (month, year) | First public enterprise production deploy | ~50% enterprise adoption | Commoditization (price collapse or open-weight parity) | Lag first deploy (mo) | Lag 50% (mo) | Lag commoditization (mo) |
|---|---|---|---|---|---|---|---|
| **Function calling** — *OpenAI function calling API* | Jun 2023 | Jul 2023 (Stripe, Instacart, Snap public references within days of release) | ~Q2 2024 (~12 mo; Menlo 2024 report shows broad integration in enterprise RAG and agent stacks) | Jul 2024 (Llama 3.1 tool-use parity; Groq Llama-3-Groq-Tool-Use model release) | ~1 | ~12 | ~13 |
| **Tool use** — *Anthropic Claude 3 tool use* | Apr 2024 (beta; GA May 2024) | May 2024 (multiple SaaS vendors via Bedrock and Vertex) | ~Q4 2024 (~7 mo; Menlo 2024 shows Anthropic doubling share to 24%, partly tool-use driven) | Q3 2024 (parity with Llama 3.1, Mistral Large 2) | ~1 | ~7 | ~5 |
| **Vision — image input** — *GPT-4V* | Sep 2023 (ChatGPT), Nov 2023 (API) | Oct 2023 (Be My Eyes consumer-industrial hybrid; Morgan Stanley pilots) | ~Q3 2024 (~11 mo; a16z and Menlo 2024 report vision broadly tested but production concentrated in document extraction and accessibility) | Mar 2024 (Claude 3 vision parity; Gemini 1.5 Pro vision); open weights via Llava, Qwen-VL reach parity ~Q3 2024 | ~1 | ~11 | ~6 |
| **Vision — Claude 3 multimodal** | Mar 2024 | Mar 2024 (multiple legal-tech and finance pilots — Harvey, Hebbia references in Anthropic customer pages within weeks) | ~Q4 2024 (~7 mo) | Q3 2024 (open-weight parity on common tasks) | ~0 | ~7 | ~5 |
| **Long context — 100k** — *Claude 2 / Claude-Instant 100k* | May 2023 | Jun 2023 (Anthropic case studies: Notion, Quora Poe, DuckDuckGo integrations within weeks) | ~Q4 2023 (~6 mo; rapid uptake as the first clear differentiator vs. GPT-4 8k/32k) | Nov 2023 (GPT-4 Turbo 128k); Feb 2024 (Gemini 1.5 1M leapfrog); open weights reach 128k with Llama 3.1 (Jul 2024) | ~1 | ~6 | ~6 |
| **Long context — 128k** — *GPT-4 Turbo* | Nov 2023 | Nov 2023 (Microsoft Copilot stack, Morgan Stanley, Klarna within the same quarter) | Q2 2024 (~6 mo; became default developer assumption by Menlo 2024) | Feb 2024 (Gemini 1.5 1M free tier); Jul 2024 (Llama 3.1 128k open weight) | ~0 | ~6 | ~3 |
| **Long context — 1M+** — *Gemini 1.5 Pro 1M* | Feb 2024 (private preview); Apr 2024 (developer waitlist); May 2024 (GA) | Apr 2024 (Goldman, Citi code-migration pilots reported in Google Cloud Next 2024 keynotes) | Still <50% of production workloads as of Q1 2026 — long context remains expensive per call; most enterprises cap at 128k-200k | Gemini 2 Flash Feb 2025 dropped price ~10x; open-weight 1M via Qwen, Llama 4 remains partial | ~2 | **n/a by Apr 2026** | ~12 |
| **Reasoning (inference-time scaling)** — *OpenAI o1-preview* | Sep 2024 | Sep 2024 (ChatGPT Enterprise/Edu within same week; code-gen startups Cursor and Cognition within days) | ~Q3 2025 (~12 mo; a16z 2025 reports 54% of enterprise respondents said reasoning models accelerated adoption) | Jan 2025 (DeepSeek R1 open-weight parity, ~27x cheaper); Feb 2025 (Claude 3.7 extended thinking) | ~0 | ~12 | ~4 |
| **Reasoning (production)** — *OpenAI o1* | Dec 2024 | Dec 2024 (Enterprise API GA within weeks; financial services and life sciences quant workloads) | ~Q4 2025 (~11 mo) | Jan 2025 (DeepSeek R1) | ~0 | ~11 | ~1 |
| **Reasoning — Claude 3.7 extended thinking** | Feb 2025 | Feb 2025 (coding assistants — Cursor, Replit, Sourcegraph within days) | Q3 2025 (~6 mo) | Already commoditized by DeepSeek R1 (Jan 2025) at launch | ~0 | ~6 | **~0 (arrived into already-commoditized space)** |
| **Reasoning — OpenAI o3** | Dec 2024 (announced), Apr 2025 (GA) | Apr 2025 (research partners used pre-GA; production after GA) | Q4 2025 / Q1 2026 (~9-12 mo post-announce, ~6-9 mo post-GA) | Apr 2025 (o3-mini price comparable to DeepSeek; DeepSeek V3 / R1-Next pushing further) | ~4 from announce, ~0 from GA | ~9-12 | ~4 |
| **Agents — autonomous-loop scaffolds** — *AutoGPT* | Mar 2023 | Apr 2023 (small startups; no fortune-500 production deploy documented in 2023) | **n/a** — 2023 agent loops never reached 50% enterprise adoption in that form; the category re-formed around "agentic workflows" by 2025 | Immediate — open-source from day one; commoditization was not a pricing collapse but an engineering reset | ~1 | **n/a (shape-shifted)** | ~0 |
| **Agents — enterprise agent platforms** (Crew, LangGraph, Agent SDK, Claude agents SDK, OpenAI Agents API) | Mid-2024 onward (LangGraph Feb 2024; OpenAI Assistants API Nov 2023 GA for assistants, evolving into Agents SDK Mar 2025) | Q2 2024 (financial services, legal AI — Harvey, Hebbia, Sierra) | Q4 2025 (~18 mo from first SDK; Menlo 2025 reports only 16% of deployments are "true agents"; G2 survey Aug 2025 reports 57% have *some* agent in production) | Partially commoditized by mid-2025 via LangGraph, CrewAI, open-weight Llama agents | ~2 | ~18 (but with heavy caveat on definition) | ~12 |
| **Computer use** — *Claude Computer Use* | Oct 2024 (beta) | Oct 2024 (small-scale RPA replacement pilots at InfoSys, select BPOs — reported in Anthropic customer posts) | **n/a by Apr 2026** — surveys through Q1 2026 do not report >50% production adoption; computer-use remains mostly pilot | Jan 2025 (Operator); open-source browser-use / Anthropic-computer-use-demo proliferation Q1 2025; full parity still developing | ~0 | **Negative evidence — not reached by Apr 2026** | ~3-6 |
| **Computer use — OpenAI Operator** | Jan 2025 (Pro tier US only); Feb 2025 wider | Feb 2025 (consumer rollout; enterprise adoption via API later in 2025) | **n/a by Apr 2026** | Operator itself deprecated Aug 2025 and folded into ChatGPT agent; DeepSeek and Qwen-based browser agents commoditize in H2 2025 | ~1 | **Negative evidence** | ~7 |
| **Multimodal generation — audio** — *GPT-4o voice* | May 2024 (announce); Jul 2024 (Advanced Voice alpha); Sep 2024 (wider) | Jul 2024 (consumer first; Duolingo, Khan Academy enterprise education pilots) | ~Q3 2025 (~15 mo; most adoption is consumer; enterprise voice-agent usage still <50%) | Sep 2024 (Gemini Live); Q4 2024 open-weight alternatives (Whisper v3 + open TTS) approach parity in specific sub-tasks, not full conversational duplex | ~2 | ~15 | ~5-7 |
| **Multimodal generation — image** — *DALL-E 3* | Oct 2023 | Oct 2023 (marketing / creative agencies same quarter) | ~Q3 2024 (~11 mo; a16z and Menlo 2024 report image gen as a top horizontal use case — marketing, product design) | Stable Diffusion XL (Jul 2023 — pre-date), Flux.1 (Aug 2024) open-weight parity; Ideogram, Midjourney commoditize pricing | ~0 | ~11 | ~10 |
| **Multimodal generation — video** — *Sora* | Feb 2024 (research preview); Dec 2024 (public) | Dec 2024 (agency, marketing, film preproduction) | **n/a by Apr 2026** — video generation <50% of enterprise AI workloads; still concentrated in creative / media sectors | Veo 2 (Dec 2024) open alternatives (Hunyuan, Wan 2.1) reach parity for short clips by mid-2025; Sora 2 Sep 2025 extends the frontier | ~0 | **Negative evidence** | ~6-9 |
| **Multimodal generation — video** — *Google Veo 2* | Dec 2024 | Jan 2025 (advertising, product marketing within first quarter) | **n/a by Apr 2026** | Hunyuan Video (Dec 2024), Wan 2.1 (Feb 2025) open weights push pricing pressure | ~1 | **Negative evidence** | ~2-3 |

### Headline pattern

Reading the table by row, three distinct curves emerge:

- **Developer-primitive curves** (function calling, tool use, long context, vision): lag to first production deploy is measured in **days to weeks**; lag to 50% enterprise adoption is measured in **6–12 months**; commoditization arrives in **3–10 months**, typically ahead of or overlapping with 50% adoption. These are the waves whose integration surface is a JSON schema.
- **Reasoning curves** (o1, o3, extended thinking, R1): first-deploy lag approaches zero (days). 50% adoption lag is **~6–12 months**, a full order of magnitude faster than classical enterprise software because the capability is consumed through the same API surface developers already use. Commoditization is violently fast — DeepSeek R1 collapsed reasoning pricing within ~4 months of o1 release.
- **Agent / computer-use / video curves**: first-deploy lag is **days**, but 50% adoption lag has **not been reached by April 2026**. These are the waves whose integration surface is a workflow — or a screen — not an API. The balancing loops dominate: compliance, change management, and ROI proof-points starve the reinforcing deployment loop.

---

## iii. Pattern findings with confidence labels

### Finding 1 — Lag compression over time **[High]**

The time from release to first public enterprise production deploy collapsed from measurable months in 2022 to **same-week / same-day** by 2024–2025 for API-native capabilities. Reference points:

- GitHub Copilot (2021 preview, 2022 GA): months between GA and large-enterprise production.
- OpenAI function calling (Jun 2023): Stripe, Instacart, Snap references within the same news cycle.
- Claude 3 (Mar 2024): enterprise customer quotes embedded in the launch post itself.
- OpenAI o1-preview (Sep 2024): ChatGPT Enterprise access "next week" per OpenAI's own release note; Cursor integrated the model in days.

**Why** (SDM interpretation): the capability-release interface standardized on OpenAI-compatible JSON over HTTPS. That uniform interface collapsed integration cost for any capability that could be cast as a request/response — which is **all of** function calling, long context, vision input, and reasoning. Interface standardization is the reinforcing loop enabling the compression.

### Finding 2 — 50% adoption lag has two regimes **[High]**

- **API-surface regime (function calling, long context, vision, reasoning):** 6–12 months from release to ~50% of enterprise respondents reporting testing or production use.
- **Workflow-surface regime (agents, computer use, video generation):** 18+ months and still counting; some have not crossed 50%.

The Menlo Ventures 2025 report finding that "only 16% of enterprise deployments qualify as true agents — most are fixed-sequence workflows" is the canonical data point. Even when 57% of G2 respondents self-report agents in production (August 2025), drilling into deployment shape reveals that most are orchestrated LLM calls, not autonomous loops.

**Why**: the integration surface is the determinant. An API-surface capability plugs into an existing application; a workflow-surface capability demands rewiring SOPs, access controls, audit trails, and human-AI handoff design — the classic change-management balancing loop.

### Finding 3 — Commoditization runs ahead of 50% adoption for reasoning **[High]**

This is the most striking inversion in the data:

- **o1-preview** released Sep 12, 2024.
- **DeepSeek R1** released Jan 20, 2025 — open weights, benchmark parity, ~27x cheaper inference, MIT license.
- **50% enterprise reasoning adoption** arrived around Q3-Q4 2025.

So commoditization preceded majority adoption by roughly half a year. This reverses the classical enterprise software pattern where a proprietary incumbent enjoys a multi-year monopoly window. For enterprises that instrumented careful model-abstraction layers (see also research prompt A1), the value of switching *at commoditization* exceeded the value of deploying *at release*. The rational strategy is no longer "buy the best model"; it is "buy the abstraction and swap the model."

### Finding 4 — Accelerators **[Medium-High]**

Identifiable reinforcing loops that shortened adoption lag:

- **Interface uniformity.** OpenAI-compatible chat-completions API became the de facto standard; most new capabilities ride it.
- **SDK and framework availability at release.** LangChain, LlamaIndex, the OpenAI Agents SDK (Mar 2025), and Anthropic's Claude Agent SDK launched in parallel with the capability, not months later.
- **Cloud marketplace presence.** AWS Bedrock (Apr 2023), Azure AI Foundry, Vertex AI each released frontier models in weeks — unlocking procurement through existing cloud contracts.
- **Pricing fall during 2023–2025.** GPT-4 input token price fell roughly 30x from launch through GPT-4o and GPT-5 cycles; Gemini 2 Flash, Haiku 3.5, and DeepSeek V3 compressed per-token costs further. Lower price expands the ROI-positive workload set.
- **Open-weight existence proof.** Once Llama, DeepSeek, Qwen replicate a capability, budget-constrained teams can run a PoC without procurement approval, expanding the top of the funnel.
- **Capability arriving inside existing workflows.** Copilot in Microsoft 365, Duet in Google Workspace, Einstein in Salesforce — a16z 2025 notes the "battle for adoption happening inside existing tools rather than through new platforms," collapsing the integration lag to near-zero because the end-user surface is unchanged.

### Finding 5 — Decelerators (balancing loops) **[Medium-High]**

Four balancing loops systematically compete with the reinforcing deployment loop:

1. **Compliance and data-governance loop.** GDPR, HIPAA, SOC 2, FINRA obligations require data-residency, audit trails, model explainability, and human-in-the-loop sign-off. Each new capability must re-clear these gates. Computer use and agents trigger stronger variants because the capability *acts* — an action in production creates liability the way a read-only completion does not.
2. **Integration-surface / workflow loop.** Tools that live inside an IDE or an API (function calling, long context, vision input) integrate fast; tools that replace a business process (agents, computer use) require SOP rewriting, RACI updates, and org-chart changes.
3. **Change-management loop.** Stack Overflow 2025 reports developer trust in AI tools *declining* even as usage rises. KPMG Q1 2026 AI Pulse reports 54% actively deploying agents — up from 11% two years earlier, but with <20% reporting "meaningful production outcomes." Human trust moves on a different (slower) time constant than model capability.
4. **ROI visibility loop.** Enterprises re-qualify spend when benefits are unclear. Ramp AI Index shows monthly business AI spend grew 4x Feb 2025 to Feb 2026, but adoption rate *flatlined at 45%* in November 2025 — indicating that existing adopters spend more while marginal new adopters slow down. Until ROI is provable, the marginal enterprise holds.

These four balancing loops are why the **API-surface regime** and **workflow-surface regime** diverge so sharply (Finding 2). Loops 1 and 2 dominate the workflow-surface regime; loops 3 and 4 dominate the slope of any given wave after early adopters have bought in.

### Finding 6 — The capability-velocity curve is not monotonic — it re-starts per wave **[Medium]**

Each new wave resets the clock. An enterprise that reached "adopted" status on function calling does not automatically reach it on agents; in fact, the organizations furthest along on function calling (heavy RAG stacks, deep API integration) are sometimes *slower* on agents because their existing architecture assumes tight human-in-the-loop review. **Adaptability is wave-independent** — an organization's *capacity to adopt* does not straightforwardly accumulate from wave to wave, since each wave taxes different organizational subsystems.

This is the central finding that feeds the **adaptability meta-frame** of the larger research program.

### Finding 7 — Classical enterprise software lag comparison **[Medium]**

Historical reference for calibration: the "cross the chasm" adoption lag for enterprise SaaS (2000s) was commonly cited at 4–7 years from launch to 50% F500 adoption. For mobile (iOS developer API 2008 to 50% enterprise MDM adoption): ~5 years. For cloud (AWS EC2 2006 to 50% enterprise workload adoption): ~8–10 years.

AI capabilities are compressing this by **a factor of roughly 5–10x** for API-surface waves, and by **roughly 2–3x** for workflow-surface waves. The Menlo Ventures 2025 report frame this as "the fastest category expansion in enterprise software history" — $37B enterprise AI spend in 2025, tripled year-on-year.

---

## iv. Open questions and negative evidence

### Explicit negative evidence

- **Computer use 50% adoption.** No reliable enterprise survey reports ≥50% production adoption of computer-use agents by Apr 2026. Menlo Ventures 2025 (Dec 2025) and KPMG Q1 2026 both characterize computer use and general-purpose agent operation as pilot-phase. The category may be re-forming faster than surveys can measure it.
- **Video generation enterprise adoption.** Sora and Veo 2 are widely consumer-tested but enterprise production adoption outside marketing and media verticals is low. No horizontal enterprise survey reports ≥50% adoption.
- **1M-token context adoption.** Despite Gemini 1.5 launching Feb 2024, most production workloads still cap context at 128k-200k. The cost-per-call is the dominant balancing loop; 1M contexts are reserved for narrow use cases (codebase analysis, legal mega-contracts).
- **AutoGPT-style autonomous agents (2023 variant).** That specific pattern did not reach 50% enterprise adoption. The agent category *reformed* into workflow-oriented agent platforms in 2024–2025, so the original release's adoption curve is interrupted rather than completed.

### Open questions (not yet resolvable from public evidence)

1. **Depth-of-use vs. breadth-of-use.** Surveys count "in production" at the yes/no level. The data does not distinguish an enterprise running agent-X on one internal helpdesk from one running it across 2000 customer-facing workflows. Ramp's finding that median AI-spending companies dedicate ~15% of software budget to AI hints at depth, but survey panels remain yes/no.
2. **Substitution vs. net-new workloads.** How much 2025 AI spend displaces existing SaaS versus creates net-new use cases? a16z and Menlo hint at substitution (Klarna's 1,200-SaaS consolidation) but no systematic measurement exists.
3. **The "reasoning-model reinforcement" question.** a16z 2025 claims 54% of enterprise respondents attribute faster adoption to reasoning models. Does this represent a genuine capability threshold crossing, or survey-respondent rationalization of adoption they would have done anyway? Untestable from public data.
4. **The 2025 agent definitional split.** "Agent" in G2 (57% in production) vs. Menlo Ventures (16% are "true agents") differ by ~4x. Which definition should A2 use? This memo reports both and flags the definitional hazard.
5. **Capability-wave overlap.** When reasoning and agents release within months of each other, enterprise adoption surveys do not separate them cleanly. The tabled lag numbers therefore carry cross-wave interference.
6. **Geographic variance.** Most surveys are US-centric. European enterprise adoption is widely reported as 6–12 months slower because of GDPR, EU AI Act, and data-residency requirements. Asian enterprise adoption varies dramatically by country. This memo's lag numbers are US-skewed.
7. **Post-commoditization stickiness.** Once a capability is commoditized (e.g., reasoning via DeepSeek R1), does enterprise share follow cost-down or inertia? a16z's May-to-Nov 2025 data showing Anthropic +25% share suggests capability / quality still matters beyond price.

### Evidence that contradicts clean lag compression

- Ramp AI Index (Nov 2025): adoption flatlined at 45% of businesses. Implies the marginal curve has slowed materially, even as the absolute installed base rose. The average **depth** of adoption rose (4x spend growth) while the **breadth** of adoption plateaued.
- Stack Overflow 2025 developer survey: trust in AI tools at an "all-time low" despite usage rising. The absolute usage number is not the only signal; sentiment diverges.
- Deloitte 2026 *State of AI in the Enterprise*: significant share of enterprises report ROI below expectations. Several of the 2024-era agent projects are in post-implementation retrospective phase.

---

## v. Three-pillar feed

This section translates A2 findings into specific inputs for the three pillars of the adaptability framework (the parent plan's core decomposition).

### Pillar A — AI Usage Framework

- **The adaptability design target is the model-abstraction layer.** Because commoditization can precede 50% adoption (Finding 3), the instrument that maximizes optionality is a thin, versioned abstraction over model-calling — provider, model, tool-schema, and reasoning-budget as separable configuration. This is more important than picking the "best" model at any point.
- **Capability-wave watch process.** The team must run a standing capability-release radar on at least: (i) release announcements, (ii) open-weight parity events, (iii) price events. The cadence is monthly, matching the observed capability turnover rate named in the parent plan.
- **Workflow-surface capabilities need a different playbook than API-surface capabilities.** The 18-month-plus 50% adoption lag for agents and computer use (Finding 2) means attempts to adopt workflow-surface capabilities with API-surface playbooks fail. Expect multi-quarter pilots, SOP rewriting, and explicit change-management tracks.

### Pillar O — Organization

- **Adoption is a decision role, not a tech role.** The balancing loops (Finding 5) are human: compliance, change management, ROI. The adaptability organization needs a named owner for each — not centralized in a "Chief AI Officer" but distributed into the functional areas the loops live in (General Counsel, Head of Ops, CFO, CTO).
- **The capability-turnover cadence exceeds typical annual planning rhythms.** Monthly capability radar implies monthly replan checkpoints at the capability/portfolio level, with quarterly or semiannual major bets. Annual planning alone cannot keep pace.
- **"AI adoption" is not monotonic (Finding 6).** Organizations can be early on wave *n* and late on wave *n+1*. Promotion criteria and team scorecards should not reward "once-adopted" status; they should reward repeat capability-uptake velocity.
- **Definitional hygiene matters internally too.** The 16% vs. 57% agent-adoption definitional gap will replicate inside any organization's internal reporting. Leaders should specify what counts as "agent in production" before asking the org to report.

### Pillar T — Technical infrastructure

- **Model-abstraction and model-swap tooling pays more than compute optimization.** Given that reasoning commoditized in ~4 months, infrastructure bets on a specific frontier model have short half-lives. Portable eval harnesses, provider-agnostic tool-schema, and hot-swap deployment are the higher-leverage investments.
- **Inference-cost curves reshape build-vs-buy.** The 27x cost collapse on reasoning (DeepSeek) plus ~10x on Gemini 2 Flash widens the set of workloads where self-hosting open weights on fine-tuned infrastructure makes sense, but *only* if the organization has the MLOps maturity to operate it. Otherwise cloud-API remains optimal.
- **Compliance must be designed into the substrate, not bolted on per capability.** Because each new capability re-triggers the compliance loop (Finding 5, loop 1), a reusable compliance substrate — data-residency-aware routing, standardized audit logging, standardized red-team harness — amortizes the balancing-loop cost across waves.
- **Long-context and 1M-token remain expensive.** Infrastructure should default to 128k–200k context with explicit, cost-approved escalation paths to 1M. Treat 1M context as a reviewable scarce resource, not a default primitive.

### Meta / adaptability

- **A2 is the clearest empirical support for the parent plan's central claim** that monthly-scale AI capability turnover is the design target. The data shows first-deploy lags of days, commoditization lags of months, and adoption-lag regimes that diverge by 3–5x based on integration surface. An organization optimized for the 1-wave-per-3-years cadence of SaaS adoption will mis-design its three pillars.
- **The capability-velocity chart (Section ii) should be kept live.** It is a monthly-updated artifact, not a static memo. The lag numbers move with each new release, each new open-weight parity event, each new price event.
- **The lag-curve shape itself is the governance object.** A team whose first-deploy lag is 3 months when industry peers run at 1 month has an adaptability deficit that is *diagnosable and actionable*. Making the curve visible to leadership turns adaptability from a slogan into a measurement.

---

### Appendix — Source-source mapping (non-exhaustive)

Primary release sources:
- OpenAI function calling: `openai.com/index/function-calling-and-other-api-updates/` (Jun 13, 2023).
- GPT-4V: `openai.com/index/gpt-4v-system-card/` (Sep 25, 2023); API Nov 6, 2023.
- GPT-4 Turbo 128k: OpenAI DevDay (Nov 6, 2023).
- GPT-4o: `openai.com/index/hello-gpt-4o/` (May 13, 2024).
- OpenAI o1-preview: `openai.com/index/introducing-openai-o1-preview/` (Sep 12, 2024).
- OpenAI o3: announced Dec 20, 2024; GA Apr 2025.
- OpenAI Operator: `openai.com/index/introducing-operator/` (Jan 23, 2025); deprecated Aug 31, 2025.
- Sora: Dec 9, 2024 (public).
- Claude 100k: `anthropic.com/news/100k-context-windows` (May 11, 2023).
- Claude 3 family (incl. vision): `anthropic.com/news/claude-3-family` (Mar 4, 2024).
- Claude computer use: Anthropic release (Oct 22, 2024).
- Claude 3.7 Sonnet (extended thinking): `anthropic.com/news/claude-3-7-sonnet` (Feb 24, 2025).
- Gemini 1.5 Pro 1M: Google blog (Feb 15, 2024).
- Veo 2: Google DeepMind (Dec 16, 2024).
- DeepSeek R1: DeepSeek API docs (Jan 20, 2025).
- AutoGPT: GitHub Significant-Gravitas/AutoGPT (Mar 30, 2023).

Enterprise adoption surveys:
- Menlo Ventures, *2024 State of Generative AI in the Enterprise* (Nov 20, 2024): 600 IT decision-makers; $2.3B → $13.8B spend; Anthropic 12% → 24%; RAG 31% → 51%.
- Menlo Ventures, *2025 State of Generative AI in the Enterprise* (Dec 2025): $37B enterprise AI investment (tripled YoY); 47% of AI deals reach production; only 16% of deployments qualify as "true agents"; coding/dev-tools $7.3B; healthcare $3.5B; copilots $8.4B.
- a16z, *How 100 Enterprise CIOs are Building and Buying Gen AI in 2025*: 54% say reasoning models accelerated adoption; 81% use 3+ model families; Anthropic +25% share May–Nov 2025.
- Ramp AI Index (monthly through 2025): adoption crossed 50% Mar 2025; flatlined at 45% Nov 2025; 4x monthly spend growth Feb 2025 – Feb 2026; median AI-spending company allocates ~15% of software budget to AI.
- Stack Overflow Developer Survey 2024 / 2025: 76% → 84% AI-tool usage; trust falling; 62% actively use AI tools (2024).
- KPMG Q1 2026 AI Pulse: 54% actively deploying agents vs. 11% two years earlier, 33% mid-2024.
- G2 (Aug 2025): 57% of companies have agents in production, 22% pilot, 21% pre-pilot.
- PwC Agentic AI: 79% of organizations have implemented agents at some level.
- IDC / AWS agent adoption study (Nov 2025): projects scaling hurdles through 2027.
- Deloitte *State of AI in the Enterprise* 2026.

---

*End of A2 memo. Word count ~3,850.*
