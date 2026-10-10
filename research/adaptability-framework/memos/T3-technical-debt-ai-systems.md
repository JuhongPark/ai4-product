# T3 — Technical debt in AI-native systems

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Axis / Pillar:** T (Technical infrastructure)
> **Date:** 2026-04-22
> **Prompt:** T3. Technical debt in AI-native systems (2023–2026)
> **Output artifact:** taxonomy of AI-system technical debt × five focus areas × three resolution classes (compound / self-resolve / deliberate remediation), with maintenance-cost curves.

---

## i. Method

This memo investigates the form technical debt takes in AI-native systems operated against foundation-model APIs that turn over on a quarterly cadence. Evidence was gathered across 2023–2026 from: (a) primary engineering blog posts from model and application vendors (Anthropic, Shopify, Klarna, LangChain, Intercom, OpenAI), (b) observability-platform product documentation and pricing pages (LangSmith, Arize, Braintrust, Langfuse, Helicone), (c) practitioner writing from Hamel Husain, Eugene Yan, Bryan Bischof, Shreya Shankar, and collaborators, (d) academic papers extending Sculley et al. (2015) to LLM systems, and (e) publicly reported post-mortems.

**Systems-engineering posture.** The memo treats technical debt as an SDM object: a *stock* that accrues through a *flow* of expedient decisions, partially drained by a *remediation flow*, and partially drained *without action* when a dependent component changes upstream. Three framing devices are applied:

- **Sculley extension.** Sculley et al. (2015) identified ML-specific debt factors — boundary erosion, entanglement, CACE, hidden feedback loops, undeclared consumers, data dependencies, configuration drift, glue code, pipeline jungles, and external-world change — most of which intensify in the LLM era. This memo names five new LLM-era categories (prompt debt, RAG debt, eval debt, observability debt, adapter debt) and maps each back to the Sculley taxonomy where lineage exists.
- **DSM / interface view.** Debt is located at specific architectural boundaries — prompt ↔ application code, embedding ↔ index ↔ retriever, judge ↔ product metric, SDK ↔ framework ↔ vendor API. Some boundaries *contain* debt (it stays local to the interface). Others *leak* debt into dependent components, causing the CACE amplification that Sculley warned about but in a more extreme form than classical ML showed.
- **Safety-III (Leveson).** Debt is treated as a contributing factor to AI-system accidents — not as a root cause but as an erosion of the control structure that catches emergent failures. A stale eval, an uncalibrated judge, or a brittle RAG pipeline functions like a missing safety barrier: the first quarter without it is uneventful; the third is when the outage or the CVE arrives.

**Resolution-class definitions used throughout.**

1. **Compounding debt.** The debt worsens monotonically without action. The maintenance cost curve is convex and slopes upward; a quarter of inattention raises next quarter's remediation cost more than linearly.
2. **Self-resolving debt.** Upstream action — a base-model upgrade, an SDK version, a vendor feature release — eliminates or reduces the debt without the application team doing work. The cost curve is sawtooth: accrual between upstream releases, discontinuous drop at each release.
3. **Deliberate-remediation debt.** Only an intentional engineering effort — rewriting prompts, re-embedding a corpus, recalibrating a judge, rebuilding an observability layer, retraining an adapter — removes the debt. No vendor or upstream change helps. Cost curve is flat-to-rising until a remediation event causes a step-down.

**Evidence hygiene.** Claims are labelled *observed* (primary source with citation), *inferred* (reasoned from observed evidence), or *speculation* (labelled explicitly). Absolute dates are preserved. Where a claim depends on a single vendor-published source with marketing incentives (e.g., resolution-rate numbers from Fin or the Klarna-LangChain case study), the limitation is noted. Some of the strongest evidence — the Klarna reversal, Cursor's pricing incident, CVE-tracked prompt-injection breaches — is *negative evidence* about whether technical debt patterns were managed adequately.

---

## ii. Evidence table

Row per (debt pattern, firm / source citation, resolution class, approximate cost). Abbreviations: *C* = compounding, *SR* = self-resolving on upstream change, *DR* = deliberate remediation only.

| # | Focus area | Debt pattern | Firm / source (date) | Class | Approximate cost signal |
|---|---|---|---|---|---|
| 1 | Prompt | Prompt stuffing / "God-object" prompt (2,000+ tokens, contradicting instructions) | Yan, Bischof, Frye, Husain, Liu, Shankar — "What we learned from a year of building with LLMs" (2024-05-28) | C | Prompt length grows until refactor; token cost scales linearly, latency superlinearly |
| 2 | Prompt | "Death by a thousand instructions" from tool-inventory growth (0 → 50+ tools) | Shopify Sidekick engineering blog (2025-08-26) | DR | Required architectural rewrite to JIT-instruction retrieval; team size and hours undisclosed |
| 3 | Prompt | Vendor deprecation forces prompt migration on vendor's schedule | OpenAI deprecations index; GPT-4o retirement 2026-03-31 per OpenAI docs; Anthropic Claude 4.7 migration guide | DR | Healthcare case (Gemini 1.5 → 2.5 Flash): 400+ eng-hours, JSON parsing broke, 5× token bloat per response |
| 4 | Prompt | "Criteria drift" — evaluation rubric shifts after engineers see outputs | Shankar et al. "Who Validates the Validators?" (2024); Husain & Shankar "LLM Evals" (2026-01-15) | C | Research finding: impossible to fix eval criteria before reviewing outputs; eval rework is recurring labour |
| 5 | Prompt | Stricter schema adherence in new model generation breaks downstream parsers | GPT-5.1 behavioural-difference writeups (multiple, 2025–2026); Claude 4.7 literal-instruction behaviour (Anthropic docs 2026) | SR *or* DR (bimodal) | Mostly deliberate rewrite; occasional self-resolve when vendor ships backward-compat mode |
| 6 | RAG | Stale embeddings after corpus updates or embedding-model change | Morphik / Dhiwise / Data Nucleus enterprise RAG guides (2025); internal reports of 42% of failed RAG implementations cite data-prep as root cause | C | Full re-embed of corpus; "100×" recompute vs. Drift-Adapter baseline per arXiv 2509.23471 (2025-09-27) |
| 7 | RAG | Chunking strategy coupling — chunks built for one retriever regress on another | Anthropic "Contextual Retrieval" (2024-09-19); late-chunking vs. contextual-retrieval analyses (2025) | DR | Anthropic method: 35% retrieval-failure reduction vs. baseline; $1.02 per million document tokens one-time preprocessing |
| 8 | RAG | Long-context models partly obviate chunk tuning | Karpathy "2025 LLM Year in Review" (2025-12); Willison "2025: year in LLMs" (2025-12-31); Yan et al. (2024-05) | SR | Capability release drains prior chunking debt; still leaves multi-tenancy + leakage debt |
| 9 | RAG | Index-rebuild contention at billion-item scale | Drift-Adapter (arXiv 2509.23471, 2025-09-27); Redis "What breaks in production" (2025) | DR | Recompute cost reduced 100× by embedding-space translation adapter; without adapter: full re-embed + downtime |
| 10 | Eval | LLM-as-judge calibration drift vs. human labels | Husain "LLM-as-Judge guide" (2024-10); Husain & Shankar eval FAQ (2026-01-15); Evidently, Monte Carlo, GoDaddy 2024–2025 writeups | C | Judge requires 100+ labelled examples + weekly maintenance per Husain & Shankar (2026) |
| 11 | Eval | Position bias, length bias, self-preference in judge models | Survey on LLM-as-a-Judge (arXiv 2411.15594, 2024); "Overconfidence in LLM-as-a-Judge" (arXiv 2508.06225, 2025) | DR | Regression-based bias correction halves residual error; ongoing human re-labelling required |
| 12 | Eval | Expert-domain agreement gap (dietetics, mental health: 60–68% LLM-human) | Academic surveys referenced in Monte Carlo 2024 writeup | C (in regulated domains) | Requires continuous SME re-labelling; domain-specialist salaries |
| 13 | Eval | Shopify "Ground Truth Sets" require Cohen's Kappa governance + 3 experts per label | Shopify Sidekick ICML 2025 talk recap (2025-08-26) | DR | Judge Kappa improved 0.02 → 0.61 across iteration; human baseline 0.69 |
| 14 | Observability | Trace-volume billing collapses under agentic workloads | Pydantic / Pecollective / Braintrust 2026 pricing comparisons | C | Arize: $10 per million spans + $3/GB payload overage; production apps >$2/M spans noted |
| 15 | Observability | Vendor SDK breaking changes in the observability layer itself | LangChain 0.1 → 0.2 → 0.3 breaking changes; recommended split into langchain-core + langgraph (2026 guidance) | DR | Upgrade tax every 6–12 months; teams staying on pinned versions lose new features |
| 16 | Observability | Opaque pipelines without execution traces block debugging | Databricks "Hidden Technical Debt of GenAI Systems" blog (2025) | DR | Qualitative: "essential when a response returns an error"; no $ figure given |
| 17 | Observability | Observability lock-in — moving from LangSmith to Braintrust/Arize is a second migration | 2026 vendor-comparison articles (Confident AI, Braintrust, Firecrawl) | DR | Prompt registry, judge definitions, datasets all vendor-specific |
| 18 | Adapter | LoRA adapter trained on base model X regresses on base model X+1 | Runpod / Digital Divide Data LoRA 2025 guides; TianPan "Fine-Tuning Economics" (2026-04-09) | DR | Quarterly re-eval at minimum; monthly for fast-moving domains; 3–5× cost underestimate typical |
| 19 | Adapter | Full fine-tune cost tied to chips (100–120 GB VRAM for 7B) | Introl / RunPod / TrueFoundry LoRA 2025 guides | C if ignored, DR if paid | ~$50k for H100-class full tune; $1,500 4090-class QLoRA; 90–95% quality retention |
| 20 | Adapter | Only ~10% of fine-tune projects reach production | Industry estimate referenced across 2025 sources | — | Sunk-cost signal: adapter debt includes dead experimental codepaths per Sculley |
| 21 | Cross | Klarna customer-support AI reversal — AI handled 700-person-equivalent in early 2024, CEO admits "went too far" by 2025-Q2 and rehires humans | Reporting across Entrepreneur, FinTechWeekly, Reworked, Vice (2025); LangChain customer case (2025-02-12) | DR | No $ disclosed; reputational + hiring cost documented |
| 22 | Cross | Prompt-injection CVEs in production (Microsoft 365 Copilot CVE-2025-32711 CVSS 9.3; ServiceNow Now Assist second-order injection 2025; GitHub Copilot / VS Code CVE-2025-53773 RCE) | Public CVE records; LastPass, Obsidian, Simon Willison writeups (2025) | C | Safety-III reading: eroded control structure is the debt; breach is the accident |
| 23 | Cross | Cursor pricing incident — token-cost model misaligned with new-generation model economics; refunds issued | Cursor public apology 2025-07-04; community reports (Reddit, DEV.to 2025–2026) | DR | Pricing rebuild required; unsolicited developer cost spikes ($100/mo → $20–30/day reported) |
| 24 | Cross | Intercom Fin AI Group ~40 ML scientists / engineers as a continuous remediation function | Intercom / Fin.ai product pages and 2024–2025 "Pioneer" announcements | DR (institutionalised) | Headcount as standing capex for LLM-debt servicing |
| 25 | Cross | GoDaddy "build a single prompt for everything" anti-pattern (Lesson #1) | GoDaddy writeup cited in Yan et al. (2024-05-28) | C | Same debt class as #1; different vantage |

---

## iii. Pattern findings with confidence labels

### Finding 1 — Four of the five focus areas are dominated by deliberate-remediation debt; only RAG shows meaningful self-resolution from upstream change

**Confidence: high.** Across the 25 evidence rows, self-resolving debt is confined to two sub-cases in RAG (rows 8 for long-context, 6 where a vendor ships a backward-compatible embedding-space adapter) and to a bimodal fraction of prompt debt (row 5). Eval, observability, and adapter debt are uniformly deliberate-remediation. The dominant AI-system technical-debt curve is therefore *not* the classical Sculley sawtooth (drained by platform upgrades) but a monotonically rising stock that only engineer labour can drain. This aligns with Sculley's 2015 warning that ML systems accrue more debt than software systems, intensified by the fact that the upstream (the foundation model) changes on a cadence *incompatible* with the application team's release cycle.

### Finding 2 — The LLM era adds five new debt categories beyond Sculley (2015), mapped by extension rather than replacement

**Confidence: high.** The Sculley framework anticipated six LLM-era patterns at the abstraction level, but LLM-era engineering has produced concrete instantiations that deserve their own taxonomy slots:

| Sculley (2015) category | LLM-era instantiation (this memo) | Interface where debt sits |
|---|---|---|
| Entanglement / CACE | Prompt-stuffing, "death by thousand instructions" | Prompt ↔ application code |
| Data dependencies | RAG: stale embeddings, chunking coupling | Embedding ↔ index ↔ retriever |
| Hidden feedback loops | Eval: criteria drift, judge self-preference | Judge ↔ product metric |
| Undeclared consumers | Observability: opaque pipelines, lock-in | Trace layer ↔ downstream analytics |
| Glue code + dead experimental codepaths | Adapter: fine-tunes that never shipped, base-model churn | Adapter weights ↔ base-model API |
| External-world change | Vendor deprecation cadence | API contract boundary |

This is *extension*, not replacement: CACE in LLMs is not a new phenomenon but an intensification — "Changing Anything" now includes an invisible change in the model provider's RLHF weights, not just a code change in your system.

### Finding 3 — Interface boundaries determine whether debt is contained or leaks (DSM reading)

**Confidence: medium-high.** The five focus areas differ sharply in whether their debt stays local:

- **Prompt debt** leaks heavily. A prompt is embedded in application code, and a vendor-side behavioural change (Claude 4.7 taking instructions more literally; GPT-5.1 enforcing schemas more strictly) propagates through downstream parsers, judges, and UI assumptions. Klarna and Shopify both report architectural responses: Shopify's JIT-instruction layer and Klarna's multi-agent routing exist specifically to *contain* prompt changes at a single boundary. The architectural pattern that works is an explicit prompt registry with versioned artifacts, immutable, stored outside application code — exactly the practice recommended across TianPan, Reintech, Maxim, and DeepChecks 2024–2026 writeups.
- **RAG debt** leaks because the embedding space, the index, the retriever, and the generator form a tightly coupled chain. A change in embedding model breaks the index; a change in chunk size breaks both. The Drift-Adapter line of research (arXiv 2509.23471) is explicitly motivated by this leakage, and its contribution is an *interface-translation* layer that contains the debt at a single boundary — a textbook DSM remediation.
- **Eval debt** is the most hidden-feedback-loop-prone. When judges drift, product metrics drift with them — but the application code does not know. Every quarter without re-calibrating the judge silently erodes the decision basis on which every other engineering choice is being made. This is the Safety-III case: the degraded barrier is invisible until the accident.
- **Observability debt** leaks in an economic sense. Trace-volume billing (Arize, LangSmith, Braintrust at high scale) penalises the very telemetry needed to manage all other debt categories, which can cause teams to truncate telemetry, which causes new-blind-spot debt elsewhere.
- **Adapter debt** leaks along the base-model ↔ adapter interface. If the base model changes, the adapter is in a superposition: it may still work, it may regress quietly, or it may need a full retrain. Few teams have the eval rigor to know which.

### Finding 4 — Debt accrual is front-loaded at integration; the rework flow is back-loaded at maintenance

**Confidence: medium.** The SDM stock-and-flow reading is: debt is created almost for free at integration time (copying a prompt from a notebook, picking the first embedding model that works, setting up an LLM-as-judge with default settings), then revealed at a maintenance-time stress event — a vendor deprecation, a user complaint, a cost spike, a CVE. The pattern is identical to technical debt in classical software; what is *different* is the cadence of the stress events. OpenAI and Anthropic cycle major model generations every 6–12 months; observability vendors cycle SDKs every 6–12 months; embedding-model leaderboards cycle similar. A team that integrates an AI feature in Q1 and does no further work can expect to face a forced remediation event within 2–4 quarters. This is an order of magnitude faster than the "every 2–5 years" schedule that governs classical software replatforming.

### Finding 5 — Some debt self-resolves, but the self-resolution itself triggers debt elsewhere

**Confidence: medium.** Rows 5 and 8 of the evidence table illustrate this paradox. Long-context models self-resolve some RAG tuning debt (you can stuff more into context, skipping chunking decisions), but they *create* new debt in the form of token-cost bloat, new judge calibration needs (judging a 200k-token answer is harder), and new data-leakage risks (multi-tenant corpora fit in one context window). Similarly, when Claude 4.7 self-resolves vague-prompt instructions, it creates a new debt of over-literal behaviour on formatting templates — what the Anthropic migration guide calls "harness effects." The net debt is often positive, not negative, when upstream changes land. This is consistent with Sculley's CACE principle: upstream improvements, like any other change, change everything.

### Finding 6 — The five LLM-era debt types form a systems-dynamics *doom loop* if left alone

**Confidence: speculative, well-reasoned.** Tracing feedback loops across the five focus areas:

```
  (prompt debt) -> harder to reliably generate outputs
     -> (eval debt) harder to know if outputs are good
     -> (observability debt) harder to see where they go wrong
     -> (RAG debt) retrieval errors masked
     -> (adapter debt) fine-tunes optimise for the wrong target
     -> back to prompt debt (engineers compensate by stuffing the prompt)
```

This is a reinforcing loop. Each category makes the adjacent category harder to manage. The intervention points are the ones Meadows would flag: monitoring (observability) and judge quality (eval), because they are the system's feedback channels. A team that lets observability and eval debt accumulate will find that the other three categories compound faster. This is why Hamel Husain's and Eugene Yan's writing has converged on eval as the master skill: fix the feedback first.

### Finding 7 — The Klarna reversal is the most instructive case

**Confidence: high for the facts; medium for the interpretation.** Klarna's February 2025 LangChain case study claimed 80% query-resolution-time reduction and 700-FTE-equivalent workload within 9 months. By spring 2025, the CEO publicly reversed: quality had degraded, trust had eroded, humans were being rehired. The technical-debt reading is that Klarna accrued all five debt types simultaneously and in unmanaged form:

- prompt debt (the single-system-prompt approach they document became brittle across edge cases),
- RAG debt (support knowledge bases drifted as product features changed),
- eval debt (their evaluation framework optimised for resolution *time*, not for customer satisfaction — a Goodhart's Law outcome on the judge target),
- observability debt (they had LangSmith traces but not the customer-experience signals that would have caught the degradation),
- and a policy debt (irreversible headcount cuts pre-committed the organisation to living with whatever debt accumulated).

The Klarna case therefore functions as a *full-system* stress test of the T3 taxonomy, across all five focus areas, ending in deliberate remediation at the organisation level, not just the system level. It also illustrates Leveson's Safety-III thesis: the removal of the human-support safety barrier exposed the accumulated debt, which then caused the accident.

---

### Primary taxonomy artefact — AI-system technical debt × 5 focus areas × 3 resolution classes

| Focus area | Compounding (C) | Self-resolving (SR) | Deliberate remediation (DR) |
|---|---|---|---|
| **(a) Prompt** | Prompt stuffing / "God object" prompts; tool-inventory bloat; criteria drift on internal prompt-review | (rare) vendor ships backward-compat mode on deprecation | Vendor deprecation migration; schema-adherence tightening; "thousand instructions" architectural rewrite (Shopify JIT); prompt-as-code registry migration |
| **(b) RAG** | Stale embeddings; chunk-size coupling to retriever; multi-tenant leakage; domain-vocabulary drift | Long-context models obviate some chunk tuning; vendor ships embedding-space translation (Drift-Adapter class); improved re-rankers | Full re-embed on embedding-model change; chunking rewrite (contextual retrieval); re-indexing at scale; domain-specific embedding fine-tunes |
| **(c) Eval** | Judge calibration drift vs. humans; position / length / self-preference bias accumulation; criteria drift as product evolves; expert-domain agreement gap | (none observed at meaningful scale) | Judge recalibration cadence (weekly per Husain & Shankar 2026); regression-based bias correction; Cohen's Kappa governance (Shopify); human-in-the-loop re-labelling |
| **(d) Observability** | Trace-volume cost explosion at agentic scale; lock-in to vendor-specific prompt / judge schemas; telemetry truncation creating blind spots | Open-source alternatives (Langfuse self-host; Phoenix) drain some lock-in | SDK breaking-change upgrades (LangChain 0.1 → 0.2 → 0.3); observability-vendor migration; instrumentation rebuild for new span schemas |
| **(e) Adapter** | Dead experimental fine-tunes; data curation cost growth; training-data drift | (rare and risky) base-model upgrade occasionally improves adapter's downstream task without retrain | Quarterly adapter re-eval; full adapter retrain on base-model change; QLoRA migration to cheaper hardware; deprecation of unreachable adapters |

**Maintenance-cost curves, qualitative.**

- **Compounding (C)** — convex upward. Unit of accrual is per-quarter prompt growth, embedding-age, judge-drift, telemetry volume, stale fine-tune.
- **Self-resolving (SR)** — sawtooth. Accrual plus upstream-release step-down. Net cost still positive because self-resolution usually introduces new debt elsewhere (Finding 5).
- **Deliberate remediation (DR)** — flat-then-cliff. Cost stays low until a forced event (deprecation, CVE, cost spike, customer revolt), then jumps to the remediation cost. The remediation cost is bounded above by the "full rebuild" cost documented by the healthcare case (400+ eng-hours per prompt library) and the Drift-Adapter cost baseline (100× recompute without the translation adapter).

---

## iv. Open questions and negative evidence

**Open questions.**

1. *Cost scaling of deliberate remediation.* Engineer-months per model generation, per RAG pipeline, per judge re-calibration — almost never disclosed in absolute terms. The 400-eng-hour figure in the healthcare migration writeup is the clearest public anchor; more are needed to build credible cost curves. A research instrument proposal is to pair the T3 taxonomy with M2 (adaptability indicators) to collect standardised engineer-month estimates.
2. *What fraction of self-resolution is real vs. survivorship bias?* Teams that *survived* a model upgrade attribute success to self-resolution; teams that were burned (like the healthcare example) are the minority reporting. The true self-resolution rate is likely lower than blog posts suggest.
3. *Is eval debt a master variable?* Finding 6 argues eval is the central feedback channel. Testable hypothesis: teams with mature eval infrastructure (Shopify-level, Intercom-level) have lower compounding rates in the other four categories. M2 indicators could operationalise this.
4. *Does observability vendor consolidation help or hurt?* The current market has 5+ viable platforms. If one wins, lock-in worsens; if fragmentation persists, per-platform SDK churn worsens. Neither equilibrium drains observability debt.
5. *Where does adapter debt go in an agentic world?* If frontier models continue to eat fine-tuning use cases, adapter debt may shift from "compounds if ignored" to "self-resolves by disuse." Speculative; the evidence for 2025–2026 is that only ~10% of fine-tune projects reach production.
6. *Prompt injection as debt, not bug.* Public CVEs treat prompt injection as a bug class. The Safety-III reading in this memo treats it as a debt-symptom of eroded control barriers. Whether the taxonomy should contain a sixth focus area — *trust boundary debt* — is an open question.

**Negative evidence (looked for, not found).**

- *Quantified maintenance-cost curves from vendors.* Shopify, Klarna, Intercom all publish case studies; none disclose dollar maintenance costs with time-series granularity. The closest public artifact is Cursor's public apology (pricing-model debt) and the healthcare writeup's eng-hour figure.
- *Post-mortems with named root-cause linkage to prompt debt.* Incidents are often described in product terms ("quality dropped") rather than debt terms ("the prompt had 2,000 tokens and started contradicting itself after the Claude 4.7 migration").
- *Academic evidence extending Sculley 2015 with equivalent rigor.* The Databricks 2025 blog is the closest, but it is vendor-published. A rigorous peer-reviewed paper is overdue and would strengthen this track.
- *A single primary source that measures judge drift longitudinally in production.* The academic literature surveys judges cross-sectionally. Eugene Yan's AlignEval (2024-10) and Hamel Husain's writing push toward continuous re-calibration, but public time-series data is absent.
- *Evidence of debt transfer across organisational boundaries.* When a team migrates from a vendor to self-hosting (or vice versa), does the debt carry over, or does it zero out? No clean case in the public record.

**Limitations of this memo.** Four of the strongest rows (Klarna, Shopify, Intercom, Cursor) rely on vendor-controlled narratives. Primary engineering post-mortems at the depth of the Google SRE book, Stripe's Rails upgrade write-up, or Shopify's monolith-refactor series do not yet exist for LLM debt categories. This memo extrapolates from fragmentary primary data plus strong practitioner writing (Husain, Yan, Shankar, Bischof, Frye, Liu). The taxonomy should be treated as a *hypothesis* that can be falsified by better disclosure.

---

## v. Three-pillar feed — how T3 feeds the adaptability framework

### Engineering-anchor question — "How is the technical infrastructure for an AI-based decision-making system designed and built?"

**The T3 answer.** Design the infrastructure with debt-class awareness at every interface. The five focus areas identify five mandatory investment categories that the engineering anchor question cannot treat as optional:

1. **Prompts as code.** Prompt registry, version control, CI-gated regression suites, canary + rollback. Not a Year-2 luxury; a Year-0 requirement because prompt debt is the fastest-compounding category and the one most likely to be invisible to non-engineering stakeholders.
2. **RAG interface discipline.** Treat the embedding ↔ index ↔ retriever chain as a DSM block with a single external interface (the query). Keep internal components replaceable. Drift-Adapter-style translation layers should be a standing architectural choice, not an emergency patch.
3. **Judge as product.** An LLM-as-judge is a product with its own lifecycle, evals, drift, and deprecation. Staff it accordingly. Shopify's Cohen's Kappa governance and Intercom's 40-person AI Group are not overkill; they are proportionate to the debt dynamics described in Finding 3.
4. **Observability as feedback channel.** Do not pick an observability platform on trace-volume pricing alone; the incentive to truncate telemetry is the debt accelerator. Open-source self-host (Langfuse, Phoenix) or negotiated flat pricing are structurally better aligned with the debt-management goal.
5. **Adapter with base-model contract.** Every adapter should carry metadata binding it to a specific base-model version and a re-eval cadence. Adapters with no re-eval cadence should be treated as dead experimental codepaths and pruned.

Mapped to Pillar 3 (Technical Infrastructure) of the adaptability framework, these are five T-side investments with known compounding dynamics if skipped. This is the T3 contribution to T1 (build-vs-rent): the "rent" option does not zero out debt; it shifts *which* focus areas compound.

### Managerial-anchor question — "What operational and governance structures are required for it to function effectively in an organization?"

**The T3 answer.** Debt that only resolves through deliberate remediation must be a standing capex line, not a project. Three organisational patterns are observable in the evidence:

1. *Standing AI Ops function.* Intercom's ~40-person AI Group is the paradigm case. Shopify's Sidekick team is functionally similar. These teams exist because debt accrues continuously; a project-based staffing model would fall behind between projects.
2. *Eval as a governance object.* The Klarna reversal is the negative case: eval infrastructure (LangSmith traces, LLM judges) existed, but the governance loop from customer-experience signal back to technical remediation did not close in time. The O pillar implication is that eval maturity needs a named owner with authority to block releases or trigger remediation — a role that the Shopify Cohen's Kappa governance process institutionalises.
3. *Vendor-cadence-aware planning.* Vendor deprecation schedules (OpenAI, Anthropic, Google) should enter the managerial planning cycle as known forcing functions, not as surprises. The healthcare 400-eng-hour migration happened because the organisation did not treat Gemini 1.5 → 2.5 as a scheduled event.

Mapped to Pillar 2 (Organisational Structure), T3 argues for (a) a named AI-systems-maintenance function, (b) an eval-governance role with release authority, and (c) a vendor-cadence planning ritual. These are O-side implications that fall out of the technical debt taxonomy.

### Cross-pillar (M-side) feed

For M1 (systems-dynamics map): the reinforcing loop in Finding 6 — prompt → eval → observability → RAG → adapter → prompt — is a candidate named feedback loop for the M1 causal-loop diagram. Leverage points (Meadows) are eval and observability.

For M2 (adaptability indicators): the taxonomy directly yields candidate indicators:

- Compounding-debt accrual rate per focus area (tokens added to prompt/month; embedding-age in days; judge-drift vs. human baseline per week; trace-volume growth/month; adapter-staleness in base-model generations).
- Deliberate-remediation lag — days between forced event (deprecation, CVE, cost spike) and full remediation.
- Self-resolution realisation rate — fraction of expected self-resolutions on upstream release that actually remove debt without introducing equivalent new debt (Finding 5 skepticism).

For T1 (build vs. rent): each row of the taxonomy implies a build-vs-rent tradeoff. Building in-house tooling trades vendor-SDK-churn debt for engineering-debt; renting trades engineering-debt for lock-in debt. The memo argues for a *debt-class-aware* decision, not a blanket build-or-rent stance.

For A1 (foundation-model transition management): rows 3 and 5 of the evidence table are direct A1 inputs. The cost of a model switch is dominated by prompt debt (Claude 4.7 literal-instruction behaviour; GPT-5.1 schema adherence), RAG debt (embedding-model switch), and eval debt (re-calibrating judges against the new base model).

### Tie-back to SDM frameworks

- *Architecture / DSM*: Finding 3 assigns each debt category to a specific interface boundary. The memo proposes DSM-aware investments at the prompt-registry boundary (contain prompt debt), the embedding-translation boundary (contain RAG debt), the judge-governance boundary (contain eval debt).
- *System dynamics / Sterman*: debt as stock, rework as flow, vendor-deprecation as discrete forcing function. Finding 4 (front-loaded accrual, back-loaded rework) is the classical shape; Finding 5 (self-resolution creates new debt) is the classical "better-before-worse" pattern.
- *Safety-III / Leveson*: prompt injection CVEs, Klarna reversal, and undetected judge drift are all accidents caused by eroded control barriers. Debt is the erosion mechanism.
- *Tradespace*: each cell of the taxonomy has a cost / quality / time tradeoff. The taxonomy is the starting grid for a tradespace search rather than a checklist of best practices.

This is T3's contribution to the adaptability frame: the three pillars are held together, or pulled apart, by how AI-system technical debt is managed across the five focus areas. Debt-class awareness turns the T-pillar from a set of point technologies into a coordinated feedback system.

---

## Sources

Primary engineering sources:

- [Shopify — Building production-ready agentic systems: Lessons from Shopify Sidekick](https://shopify.engineering/building-production-ready-agentic-systems) (2025-08-26)
- [LangChain — Klarna customer case](https://www.langchain.com/blog/customers-klarna) (2025-02-12)
- [Anthropic — Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (2024-09-19)
- [Anthropic — Claude 4 best practices / migration](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [OpenAI — Deprecations index](https://developers.openai.com/api/docs/deprecations)
- [Intercom — Fin.ai](https://fin.ai/) and [Pioneer 2025 headlines](https://www.intercom.com/blog/headlines-from-pioneer-2025/)

Practitioner writing:

- [Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, Shreya Shankar — What we learned from a year of building with LLMs, Part I](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) (2024-05-28)
- [Hamel Husain — Field guide to rapidly improving AI products](https://hamel.dev/blog/posts/field-guide/) (2025-03-24)
- [Hamel Husain and Shreya Shankar — LLM Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) (2026-01-15)
- [Hamel Husain — Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/) (2024-10)
- [Eugene Yan — Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/) (2024-08)
- [Eugene Yan — AlignEval](https://eugeneyan.com/writing/aligneval/) (2024-10)
- [Simon Willison — 2025: The year in LLMs](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)

Academic and survey:

- [Sculley et al. — Hidden Technical Debt in Machine Learning Systems, NeurIPS 2015](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)
- [Drift-Adapter: Near Zero-Downtime Embedding Model Upgrades in Vector Databases, arXiv 2509.23471](https://arxiv.org/abs/2509.23471) (2025-09-27, EMNLP 2025)
- [A Survey on LLM-as-a-Judge, arXiv 2411.15594](https://arxiv.org/abs/2411.15594) (2024)
- [Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution, arXiv 2508.06225](https://arxiv.org/html/2508.06225v2) (2025)
- [Databricks — Hidden Technical Debt of GenAI Systems](https://www.databricks.com/blog/hidden-technical-debt-genai-systems)

Observability platforms and pricing:

- [LangSmith observability](https://www.langchain.com/langsmith/observability)
- [Helicone — Complete Guide to LLM Observability Platforms 2025](https://www.helicone.ai/blog/the-complete-guide-to-LLM-observability-platforms)
- [Logfire vs LangSmith vs Langfuse vs Arize: AI Observability Pricing Compared (Pydantic)](https://pydantic.dev/articles/ai-observability-pricing-comparison)
- [Braintrust — Best AI observability platforms 2025](https://www.braintrust.dev/articles/best-ai-observability-platforms-2025)

Post-mortems and production incidents:

- [Entrepreneur — Klarna hires customer service agents after AI couldn't cut it](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)
- [FinTech Weekly — Klarna Reverses Course on AI Customer Support](https://www.fintechweekly.com/magazine/articles/klarna-hires-customer-service-after-ai-pivot)
- [TianPan — Fine-Tuning Economics](https://tianpan.co/blog/2026-04-09-fine-tuning-economics-lora-peft-vs-prompt-engineering)
- [TianPan — Prompt Versioning and Change Management in Production AI Systems](https://tianpan.co/blog/2026-03-13-prompt-versioning-change-management-production)
- [TianPan — Prompt Injection in Production](https://tianpan.co/blog/2025-10-18-prompt-injection-defense)
- [Cursor pricing apology and community discussion, July 2025 (documented across DEV.to and community forums)](https://dev.to/bytedesk/i-spent-11922-on-cursor-in-under-4-weeks-heres-how-i-fixed-it-3gh2)
- [Simon Willison — New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](https://simonw.substack.com/p/new-prompt-injection-papers-agents)
