# M1 — Systems-Dynamics Map of the Three-Pillar Adaptability Problem

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Date:** 2026-04-22
> **Prompt:** M1 — Cross-pillar integration via system dynamics (causal loops, stocks, flows, delays, leverage points)
> **Anchor questions:**
> - *Engineering*: How is the technical infrastructure for an AI-based decision-making system designed and built?
> - *Managerial*: What operational and governance structures are required for it to function effectively in an organization?
> **Pillars:** A (AI usage) × O (Organization) × T (Technical infrastructure)
> **Meta position:** This memo is the M-layer integrator — the model *is* the cross-pillar synthesis, not a separate pillar.

---

## (i) Method

### (i.1) SD primer — the Forrester / Sterman apparatus

System dynamics (SD), originated by **Jay Forrester** at MIT in *Industrial Dynamics* (1961) and codified for management by **John Sterman** in *Business Dynamics* (2000), treats an organization as a network of **stocks** (accumulations that persist over time) connected by **flows** (rates of change) modulated by **feedback loops** (reinforcing R, balancing B) with characteristic **delays** and **nonlinearities**. Four methodological commitments frame this memo:

1. **Structure determines behavior.** Observed pathologies (overshoot, oscillation, policy resistance) are consequences of stock-flow-loop structure, not of actor malice or incompetence (Sterman, ch. 1; Meadows, *Thinking in Systems*, 2008).
2. **Delays are load-bearing.** Most dysfunctional dynamics come from information or material delays that decouple perception from state (Sterman, ch. 15 "Delays and Overshoot").
3. **Leverage is counter-intuitive.** Meadows (1999, reprinted 2008) argues that intuitive interventions (change the numbers) are weak; high-leverage interventions (change the paradigm, the goals, the feedback geometry) are rarely attempted.
4. **Boundary selection is a design choice.** The modeler decides what is endogenous. Here the boundary is drawn to make **A × O × T coupling** endogenous and the **external AI capability frontier** exogenous (monthly new-model shocks), consistent with the plan's declaration that "the environment changes on a monthly cadence."

### (i.2) Fit with Sterman, Meadows, and adjacent SDM canon

- **Sterman, *Business Dynamics* (2000)** — primary methodological source. Chapter 10 (path dependence and positive feedback) frames the R-loops that lock in a tooling choice; chapter 15 (delays and overshoot) frames the B-loops that trigger reversal; chapter 19 (policy design) frames the leverage-point interventions.
- **Meadows, *Thinking in Systems* (2008) + "Leverage Points" (1999)** — the twelve-level hierarchy used for the leverage-points table in section (iii.4).
- **Forrester, *Industrial Dynamics* (1961)** — original formulation; relevant for the stock-flow notation and the insight that information flows are the true control variable.
- **Crawley, Cameron, Selva, *System Architecture* (2015)** — used to identify the **form-function mapping** at each pillar and to distinguish *architectural* interventions (high leverage, high cost, slow) from *parametric* interventions (low leverage, low cost, fast).
- **Ross, Hastings, Rhodes (MIT tradespace)** — provides the *epoch-era* framing used implicitly when labeling which stocks survive a capability epoch boundary and which do not, and is the basis for the real-options costing of the "keep the swap-option alive" intervention in section (iii.5).
- **Hollnagel, Safety-II / Safety-III** (with Leveson) — reframes resilience as the capacity to respond, monitor, learn, and anticipate under variability, supplying the language used for trust-debt dynamics in B4.
- **Beer, *Brain of the Firm* (1972) / *Heart of Enterprise* (1979)** — viable system model (VSM) Systems 1–5 overlay in section (iii.6).
- **Christensen, *The Innovator's Dilemma* (1997)** — disruption-theoretic framing used in R5 (capability-S-curve loop) and in the interpretation of Klarna-style reversals.
- **Teece (2007), "Explicating Dynamic Capabilities"**; **O'Reilly & Tushman (2008, 2013), "Organizational Ambidexterity"** — supply the managerial-theory anchor for the leverage-point and intervention tables.

### (i.3) Connection to the existing repo file

This memo extends the single-pillar model in [research/ai-systems/papers/system-dynamics-ai-adoption.md](../../ai-systems/papers/system-dynamics-ai-adoption.md), which develops one reinforcing loop (R1: AI use → code volume → confidence → more AI use) and one balancing loop (B1: code volume → quality debt → rework → effective throughput) at the **skill level** (the METR paradox). This memo generalizes that structure along three axes:

- from **single-pillar** (developer tool use) to **three-pillar** coupling (A × O × T);
- from **one R and one B** to **five named R-loops and five named B-loops** spanning all three pillars;
- from **qualitative CLD** to a **stock-flow-leverage specification** that can be instantiated in Vensim / Stella / Kumu and calibrated against the M2 indicator dashboard.

The METR paradox loop (R1 + B1 in the existing file) is preserved inside this memo as a *subsystem* of the larger structure — specifically, it is the fast inner loop of R1-Velocity-Flywheel and B1-Capability-Debt-Drag in the three-pillar model. Nothing in the existing single-pillar CLD is contradicted; it is extended.

### (i.4) Evidence hygiene

Every CLD arc, stock, and loop in section (iii) is labeled:

- **(ES)** *empirically supported* — evidence base exists in the repo or in cited public literature;
- **(TP)** *theoretically proposed* — derivable from the SDM canon but not yet calibrated to AI-era data;
- **(SP)** *speculative* — the structure is consistent with theory but rests on a limited number of cases or on analogical reasoning.

The goal is not to conceal speculation but to make the **falsification surface** explicit in section (iv).

---

## (ii) Evidence base / signals from literature

The three-pillar adaptability model is empirically anchored by signals already catalogued in this repository and by canonical SDM and management literature. The strongest signals, with confidence labels, are:

| Signal | Source / repo pointer | Confidence | What it tells us about structure |
|---|---|---|---|
| METR productivity paradox — developers forecast +24%, were actually –19% slower, but *perceived* +20% faster | [research/productization-skills/papers/metr-productivity-paradox.md](../../productization-skills/papers/metr-productivity-paradox.md) | ES | Confirms the **delay-in-B1** mechanism — perception runs on the fast R-loop, state on the slow B-loop. Foundational to R1/B1 here. |
| Klarna customer-service reversal (full-AI → rehired humans) | [research/ai-systems/papers/system-dynamics-ai-adoption.md](../../ai-systems/papers/system-dynamics-ai-adoption.md) §4 | ES | Confirms that B-loops can cross a tipping point faster than governance can respond — the **Trust-Debt Tipping** (B4) dynamic. |
| Monthly-cadence model turnover 2023–2026 (GPT-3.5 → GPT-4 → GPT-4o → GPT-5; Claude 2→3→3.5→4) | Plan §A1; [research/adaptability-framework/plan.md](../plan.md) | ES | Justifies treating the capability frontier as an **exogenous shock stream**, not a steady input. |
| Capability-to-adoption lag (release → 50% enterprise adoption on the order of 6–18 months) | Plan §A2 | TP (pending A2 memo) | Structures the **infrastructure-lag delay** in B2. |
| Emergent roles: chief AI officer, forward-deployed engineer, AI ops, model evaluator, prompt engineer | Plan §O2; [research/cross-cutting/papers/ai-product-team-transformation.md](../../cross-cutting/papers/ai-product-team-transformation.md) | ES | Drives the **Org-Structure-Fit** stock — formal roles are created faster than they are retired. |
| Prompt-library maintenance cost and "stale playbook" phenomenon | Plan §O3; §T3 | TP | Supplies the **Prompt-Library Stock** dynamic — evaporation when base model changes. |
| Technical debt in AI-native systems: RAG pipelines, evaluator drift, fine-tune/adapter churn | [research/ai-systems/papers/ai-system-lifecycle-ops.md](../../ai-systems/papers/ai-system-lifecycle-ops.md); plan §T3 | ES | Directly populates the **Capability-Debt** stock flows. |
| Teece's "sensing, seizing, reconfiguring" as the three sub-capabilities of dynamic capability | Teece (2007, 2014) | ES (management literature) | Maps to the three time-horizons of intervention; see section (iii.4). |
| O'Reilly–Tushman ambidextrous structure (separate exploration unit + integration by senior team) | O'Reilly & Tushman (2008, 2013, 2016) | ES | Motivates the **decoupled dual-track** interventions in O-pillar. |
| Hollnagel's Safety-II: adaptive performance variability as the mechanism of success, not the pathology | Hollnagel (2014); Leveson & Hollnagel adjacent work | ES | Frames **trust-debt** as a function of *mismatch between expected and exhibited variability*, not raw failure counts. |
| Beer's VSM — System 3/4/5 distinction: operations vs. environment-scanning vs. identity/policy | Beer (1972, 1979) | ES | Used directly in the VSM overlay (section iii.6). |
| Christensen's disruption S-curve: low-end / new-market displacement | Christensen (1997) | ES | Informs R5 — incumbent infrastructure's path-dependent lock-in. |

A key evidentiary gap (repeated in section iv): most CLDs in published AI-adoption literature are **qualitative**. The quantitative calibration of loop gains, delay durations, and stock decay rates for an AI-era org does not yet exist in a published, peer-reviewed form. This memo is therefore a *testable* model, not a *tested* one.

---

## (iii) Pattern findings — named loops, stocks, leverage points, interventions

### (iii.1) Three-pillar CLD (ASCII)

Legend: `+` same-direction link, `–` opposite-direction link, `||` delay marker, `(R#)` reinforcing loop, `(B#)` balancing loop.

```
                                EXOGENOUS
                      ┌───────────────────────────┐
                      │  AI Capability Frontier   │  (monthly new-model shocks)
                      │  F(t) — exogenous stock   │
                      └───────────┬───────────────┘
                                  │ (+)
                                  ▼
   ┌────────────────────────────────────────────────────────────────────┐
   │                      PILLAR A — AI USAGE                           │
   │                                                                    │
   │                   Prompt-Library Stock  ◄───(+)─── AI Usage Rate   │
   │                         │   ▲                          ▲           │
   │                         │(–)│(+)                       │           │
   │                         │   │  evaporation on          │(+)        │
   │                         ▼   │  base-model change       │           │
   │                   Stale-Playbook ──(+)──► Capability Debt (T)      │
   │                                           ▲                        │
   │        Confidence ──(+)──► AI Usage Rate ─┘                        │
   │            ▲                    │  (R1 METR-flywheel, fast)        │
   │            │                    │                                  │
   │            │ ||perception delay ▼                                  │
   │            └───────(+)── Perceived Output ◄──(+)── Code/Artifact   │
   │                                                         Volume     │
   │                                                                    │
   │                  (B1 Capability-Debt Drag, slow, ||)               │
   │            Capability Debt ──(+)──► Rework Burden ──(–)──►         │
   │                                         Effective Throughput       │
   └───────────┬─────────────────────────────────┬──────────────────────┘
               │                                 │
         (+) trust signals               (+) rework surfaces
               │                                 │
               ▼                                 ▼
   ┌────────────────────────────────────────────────────────────────────┐
   │                    PILLAR O — ORGANIZATION                         │
   │                                                                    │
   │   Talent Stock ──(+)──► Absorptive Capacity ──(+)──► AI Usage Rate │
   │      ▲                       ▲                                     │
   │      │(+) hiring             │(+) training / guilds                │
   │      │                       │                                     │
   │      │ ||hiring delay        │ ||learning delay                    │
   │      │                       │                                     │
   │   Hiring ◄──(+)── Org-Structure Fit ◄──(+)── Role Redefinition     │
   │                        ▲                          ▲                │
   │                        │(–)                       │(+)             │
   │                   Structural Inertia ─────────────┘                │
   │                        ▲                                           │
   │                        │(+)                                        │
   │               Political Cost of Restructuring                      │
   │                                                                    │
   │   (R2 Competence Flywheel)   (B2 Structural-Lag Drag, ||)          │
   │                                                                    │
   │   Trust Debt ──(+)──► Governance Throttle ──(–)──► AI Usage Rate   │
   │      ▲                                                             │
   │      │(+) incident visibility                                      │
   │      │ ||public reputation delay                                   │
   │      │                                                             │
   │      └────(+)── External Incidents (Klarna-type) ◄──(+)── AI Usage │
   │                                                                    │
   │                        (B4 Trust-Debt Tipping, ||)                 │
   └───────────┬─────────────────────────────────┬──────────────────────┘
               │                                 │
   (+) evaluator demand                  (+) infra demand
               ▼                                 ▼
   ┌────────────────────────────────────────────────────────────────────┐
   │              PILLAR T — TECHNICAL INFRASTRUCTURE                   │
   │                                                                    │
   │   Tooling Stock ◄──(+)── Infra Investment Rate                     │
   │        │                      ▲                                    │
   │        │(+) coverage          │(+) budget                          │
   │        ▼                      │                                    │
   │   Data Asset Stock ──(+)──► Fine-tune / RAG Quality ──(+)──►       │
   │        ▲                                              AI Usage     │
   │        │(+) telemetry capture       Rate                           │
   │        │                                                           │
   │   Capability Debt ◄──(+)── Model / Prompt / Eval Drift ◄──(+)──    │
   │        │                                         F(t) shocks       │
   │        │(+)                                                        │
   │        ▼                                                           │
   │   Migration Cost ──(+)──► Lock-in Pressure ──(–)──► Infra          │
   │                                                     Re-architect   │
   │                                                                    │
   │   (R3 Data-Flywheel)   (R4 Lock-in Reinforcement)                  │
   │   (B3 Capability-Debt Drag, T-flavor)                              │
   │   (B5 Migration-Cost Brake, ||)                                    │
   │                                                                    │
   │   (R5 Epoch Disruption): Exogenous F(t) ──(+)──► Capability Gap    │
   │       ──(+)──► Perceived Urgency ──(+)──► AI Usage Rate ──(+)──►   │
   │       Confidence ──(+)──► More Usage (… closes back into R1)       │
   └────────────────────────────────────────────────────────────────────┘
```

### (iii.2) Named feedback loops

Five reinforcing and five balancing loops are summarized below, with explicit pillar spans, polarity walks, and confidence labels.

**Reinforcing loops**

| ID | Name | Span | Polarity walk (sign of the product of arrows) | Dominant when | Confidence |
|---|---|---|---|---|---|
| **R1** | METR Velocity Flywheel | A | AI Usage → Artifact Volume → Perceived Output → Confidence → AI Usage (all +, product +) | Capability frontier recently moved; quality gates absent; short observation windows | ES (METR) |
| **R2** | Competence Flywheel | O → A | Talent Stock → Absorptive Capacity → AI Usage Rate → Learned Patterns → Talent Value → Hiring → Talent Stock | Training pipelines are funded; guilds / CoEs exist; labor market liquid | ES |
| **R3** | Data Flywheel | A → T | AI Usage → Telemetry → Data Asset Stock → Fine-tune / RAG Quality → AI Usage | Data-plane is owned; evaluator pipelines are in place | ES (well-known in ML systems literature) |
| **R4** | Lock-in Reinforcement | T → T | Tooling Stock → Integration Surface → Migration Cost → Inertia → Tooling Stock (growth by stickiness) | Single-provider architecture; contracts bundle compute + model + services | ES (cloud economics analog) |
| **R5** | Epoch Disruption Flywheel | F(t) → A → O → T | Exogenous frontier move → Capability Gap → Urgency → Usage → further frontier pull (via demand signals back to vendors and via internal scaling) | Shortly after a major model release (GPT-5, Claude 4, Gemini 2.5 class) | TP / SP |

**Balancing loops**

| ID | Name | Span | Polarity walk | Dominant when | Confidence |
|---|---|---|---|---|---|
| **B1** | Capability-Debt Drag (A-flavor) | A | AI Usage → Artifact Volume → Capability Debt → Rework Burden → Effective Throughput (negative on the goal of throughput growth) | Perception delay long; no quality gates; incentive for volume over quality | ES (METR) |
| **B2** | Structural-Lag Drag | A ↔ O | AI Usage shift → Role Obsolescence → Structural Inertia → Org-Structure Fit falls → Absorptive Capacity falls → AI Usage effectiveness falls | Role redefinition slower than capability churn (e.g., annual promotions vs. quarterly capability cycles) | ES (O2 plan signal) |
| **B3** | Capability-Debt Drag (T-flavor) | T | F(t) shock → Model / Prompt / Eval Drift → Capability Debt → Maintenance burden → Infra Investment Rate diverted from forward build | Post-major-release quarters; no automated drift detection | ES (T3 plan signal) |
| **B4** | Trust-Debt Tipping | A → O → external | AI Usage → Incidents / Drift → Trust Debt → Governance Throttle (or external reputation hit) → AI Usage falls | Regulated domain; high-visibility consumer surface (Klarna class) | ES (Klarna) |
| **B5** | Migration-Cost Brake | T → T | F(t) shock → desired re-architect → Migration Cost → Re-architect suppressed → Legacy Tooling Stock persists → Capability Debt grows (feeds B3) | Bundled vendor contracts; low internal platform-engineering headcount | TP |

**Cross-pillar delays**

The pathologies named in the prompt — "infrastructure built for last year's model, team structure outliving the capability shift that created it" — are products of specific delays in the above loops:

- **Perception delay (A)** — between state change (capability debt accrual) and awareness of it. Drives R1 > B1 domination in short windows. Estimated 3–12 months from onset to dashboard visibility (TP).
- **Structural-restructuring delay (O)** — between capability shift and role redefinition. Bounded below by compensation cycles (annual), above by tenure inertia (2–5 years). This is the core mechanism of "team structure outliving the capability shift."
- **Infra rebuild delay (T)** — between a decision to migrate and the migration being complete. Bounded below by CI/CD and migration tooling maturity (weeks), above by bundled-contract term and platform-team capacity (12–24 months). This is the core mechanism of "infrastructure built for last year's model."
- **Trust / reputation delay (A → external)** — between AI-user dissatisfaction and a public reversal decision. Typically shorter in consumer-facing B2C than in enterprise B2B (SP).
- **Data-asset accumulation delay (T)** — between usage onset and the data flywheel (R3) producing measurable quality gain. Often 6–18 months; shorter with strong telemetry, longer with privacy-constrained domains (TP).

**Loop-dominance hypothesis.** In any given quarter of an adaptive org's trajectory, *one or two loops dominate*. This is Sterman's dominance shift: behavior patterns switch when a stock crosses a threshold. Hypothesis (SP, to be tested): **R1 dominates 0–6 months post-adoption; B1 and B3 dominate 6–18 months if no interventions; B4 dominates in high-visibility or regulated segments; R2 and R3 dominate in organizations that have deliberately invested in absorptive capacity and data-plane ownership.** The M2 indicator dashboard is what would let us observe a loop-dominance switch.

### (iii.3) Stock-and-flow specification

The seven stocks prescribed in the brief, with their inflow and outflow rates, units, and coupling:

| Stock | Units | Inflow rate (sources) | Outflow / decay rate (sinks) | Primary couplings |
|---|---|---|---|---|
| **Capability Debt** | Story-points equivalent; or $ of deferred rework | `debt_accrual = k1 · AI_Usage · (1 – quality_gate_strength) + k2 · F(t)_drift_shock` | `debt_paydown = k3 · Remediation_Effort + k4 · Automated_Drift_Correction` | Grows with R1, drained by interventions in B1/B3; couples A and T |
| **Trust Debt** | Dimensionless index 0–1; or weighted incident count | `trust_erosion = k5 · (Exhibited_Variability – Expected_Variability)⁺` (Hollnagel-style) + `k6 · Public_Incidents` | `trust_recovery = k7 · Transparency_Output + k8 · Time_Since_Last_Incident` | Gates B4; feeds the governance throttle |
| **Talent Stock** | Headcount (or skill-weighted FTE) | `hiring_rate`, `internal_training_rate`, `inbound_transfers` | `attrition_rate`, `skill_atrophy_rate` (accelerates under non-use) | Feeds R2 via absorptive capacity |
| **Tooling Stock** | $ of capitalized tooling; or number of integrated tools | `tool_adoption_rate`, `platform_investment_rate` | `deprecation_rate`, `migration_out_rate` | Feeds R3, R4; consumed by B5 |
| **Data Asset Stock** | GB-equivalents of unique, usable, labeled data + evaluator sets | `telemetry_capture_rate`, `labeling_rate`, `eval_set_expansion_rate` | `staleness_rate` (tightly coupled to F(t) shocks — evaluator drift, domain shift), `purge_rate` (privacy / retention policy) | Core to R3; anchors measurement in B4 |
| **Org-Structure Fit** | Index 0–1 (skill-to-role and workflow-to-capability match) | `role_redefinition_rate`, `reorg_rate` | `capability_shift_rate` (erosion from F(t)) + `tenure_drift_rate` | Central to B2; interacts with political cost of restructuring |
| **Prompt-Library Stock** | Count of maintained, regression-tested prompts / playbooks | `prompt_authoring_rate`, `playbook_publication_rate` | `evaporation_rate = k9 · F(t)_base_model_shock + k10 · owner_attrition` | Direct coupling between A and T; survives model shocks only with deliberate regression testing |

Two derived stocks worth tracking alongside the mandated seven:

- **Option Value of Flexibility** (real-options stock, $) — sum of the not-yet-exercised options to switch model, provider, or architecture, valued by Dixit–Pindyck or Black–Scholes variants. Drained by bundled contracts, replenished by abstraction-layer investment. Directly cited in `ai-tradespace-real-options.md` in this repo.
- **Reversal Reserve** (number of safe rollback paths across A, O, T) — stocks that are often *not modeled* and hence not maintained; their depletion is invisible until a rollback is needed.

All stock units are proposed as defaults; M2 will harden the measurement spec.

### (iii.4) Leverage points — Meadows-ranked

Meadows (1999 / 2008) orders leverage points from weakest (12) to strongest (1). Applied to the three-pillar model:

| Meadows level | Generic name | Three-pillar intervention | Pillar(s) | Expected impact | Cost / feasibility |
|---|---|---|---|---|---|
| **1. Paradigm transcendence** | Ability to hold multiple paradigms | Treat AI flux as *permanent condition*, not transitional — plan for continual reconfiguration rather than steady state | M | Transformative; reframes the whole program | Very high (cultural) |
| **2. Paradigm** | The mindset the system arises from | Shift from "build decision system" to "keep decision system fit under change" (the plan's evolution in §2) | M | Transformative | High (requires leadership alignment) |
| **3. Goals of the system** | What the system is for | Reframe org goal from "deploy AI" to "maintain capability-to-deployment lag below X days and trust debt below threshold Y" (explicit adaptability goal) | O | Large | Medium (requires new KPIs) |
| **4. Power to change system structure** | Self-organization / re-architecture rights | Grant platform / CoE teams chartered authority to retire tools and roles (not just add them) | O, T | Large | High (political) |
| **5. Rules of the system** | Incentives, constraints, permissions | Require paired gate with every AI deployment: forward-build gate (deploy) + paydown gate (remediate debt) | A, T | Medium–large | Medium |
| **6. Information flows** | Who has access to what information | Capability-to-deployment lag dashboard; evaluator drift dashboard; trust-debt ledger — visible at operating-committee level | M, O | Medium (enables all downstream interventions) | Medium |
| **7. Reinforcing loop gain** | Driving rate of R-loops | Invest deliberately in R3 (data flywheel) and R2 (absorptive capacity) — the "good" R-loops — so they dominate over R4 (lock-in) | A, O, T | Medium | Medium–high |
| **8. Balancing loop strength** | Self-correcting mechanisms | Shorten perception delay (B1) via leading-indicator telemetry; shorten trust-recovery (B4) via transparency and staged rollback; automate drift correction (B3) | A, T | Medium | Medium |
| **9. Delays** | Length of delays | Reduce structural-restructuring delay via modular team design (team APIs); reduce infra-rebuild delay via abstraction layers (model router, prompt DSL) | O, T | Medium | Medium |
| **10. Stock-flow structure** | Physical structure | Choose hybrid multi-provider architecture (T1) so Tooling Stock and Data Asset Stock are not bundled; modularize Org-Structure Fit via chartered missions rather than persistent departments | O, T | Medium (architecturally load-bearing but slow to change) | High (one-time) |
| **11. Buffer sizes** | Size of stabilizing stocks | Maintain a Prompt-Library Stock reserve (regression-tested); maintain a Reversal-Reserve of rollback paths; maintain Option-Value reserve through unused-but-maintained alternative stacks | A, T | Low–medium | Medium |
| **12. Constants / parameters** | Numbers in the model | Budget allocations, headcount ratios, individual tool-license counts | A, O, T | Low (Meadows's classic point: "numbers are the lowest-leverage interventions") | Low |

The managerial implication is Meadows-classical: **the highest-leverage interventions (1–4) are paradigmatic and structural; the most-often-attempted interventions (11–12) are parametric and weak.** The adaptability program is advised to invest disproportionately in the 2–6 range — goals, rules, and information flows — before tuning parameters.

### (iii.5) Teece dynamic-capabilities mapping — intervention table

Teece's three-part decomposition of dynamic capabilities maps cleanly onto interventions across the three pillars.

| Dynamic-capability sub-function | Pillar A (AI usage) intervention | Pillar O (Organization) intervention | Pillar T (Technical infra) intervention |
|---|---|---|---|
| **Sensing** (scanning for opportunity / threat) | Monitor capability-to-adoption lag (M2 indicator); red-team evaluations against new frontier models within N days of release | Dedicated capability-scanning role (AI ops / chief AI officer); guild for cross-team pattern sharing | Abstraction-layer telemetry that exposes where each model version is used; drift detectors on evaluator sets |
| **Seizing** (mobilizing resources around sensed opportunity) | Model-transition playbook (A1) with pre-agreed gating criteria; decision authority mapping | Ambidextrous structure (O'Reilly–Tushman): separate exploration cell with direct exec sponsor, plus integration authority at senior team | Multi-provider routing built in; fine-tune / RAG pipelines with automated regression; option-value tracking |
| **Reconfiguring** (transforming asset base) | Deliberate retirement of stale playbooks; prompt-library regression plan | Role-life-cycle policy (O2): every role has a sunset trigger; charter-based missions rather than permanent departments | Migration playbooks costed in engineer-months (T1 data); reversal reserve maintained |

This mapping also links to **O'Reilly–Tushman ambidexterity**: the "sensing" column primarily loads exploration units; the "seizing" column requires exploration-exploitation integration at the senior team; the "reconfiguring" column requires structural decoupling so that the exploitation engine is not destabilized by reconfiguration events.

**Resilience engineering (Hollnagel) connection.** The four resilience-engineering capabilities — respond, monitor, learn, anticipate — are operationalized here as:
- *Monitor* maps to the information-flow interventions (Meadows level 6) and to Sensing;
- *Respond* maps to the reversal-reserve / rollback-path maintenance (level 11) and to Seizing;
- *Learn* maps to prompt-library regression, post-incident analysis, and data-asset flywheel (R3);
- *Anticipate* maps to the epoch-scanning scenarios (Ross / Rhodes epoch-era), the option-value stock, and the Paradigm-level leverage (1–2).

Safety-II / Safety-III adds: treat *adaptive variability* as the mechanism of success, not failure. The measurement target is not "zero incidents" but "variability bounded by designed reserves."

### (iii.6) VSM overlay — Beer's Systems 1–5 mapped to the AI-adaptability problem

Stafford Beer's Viable System Model asserts that any viable organism or organization contains five interacting systems. Applied to an AI-adaptive org:

| VSM System | Beer's definition | Mapped role in the three-pillar adaptability problem |
|---|---|---|
| **System 1** | Primary activities — the operating units doing the work | The product-delivery teams using AI tools. They carry the METR R1 loop (usage → output → confidence) and absorb B1 pain. |
| **System 2** | Coordination — anti-oscillation, resolves conflicts between S1 units | The platform / CoE function that standardizes prompts, model routers, evaluator sets. Without S2, S1 teams thrash independently and Prompt-Library evaporates faster than it is created. |
| **System 3** | Operational control — internal "here and now" optimization | The engineering / ops leadership that sets rules, allocates compute, sets quality gates (Meadows level 5 interventions). Owns Capability-Debt visibility. |
| **System 3\*** | Audit — sporadic direct inspection to validate S3 information | Independent audit function (METR-style third-party evaluation; internal red teams; external regulators). Critical counter to the perception-delay problem — S3 can be gamed; S3* is the corrective. |
| **System 4** | Intelligence — outside-and-future scanning | The capability-scanning / horizon function. Monitors F(t), the capability frontier. Owns Sensing in Teece terms. Typically under-invested; this is where many orgs fail. |
| **System 5** | Identity / policy — the organization's purpose and constitutional rules | The executive team / board that holds the paradigm (Meadows levels 1–2). Decides *what* adaptability means for this org, and adjudicates the S3–S4 tension between exploitation (now) and exploration (next). |

The **S3 ↔ S4 balance** is Beer's diagnostic for viability. AI-era organizations most often fail by **over-weighting S3** (run the current model stack; lock in the vendor contract) and **under-weighting S4** (scanning the frontier; maintaining switchability). A strong S5 is what forces a rebalancing: the explicit paradigm that capability turnover is permanent.

---

## (iv) Open questions — what is testable, what would falsify the model

This memo is a *testable* model. Concrete falsification conditions:

1. **Loop-dominance hypothesis (iii.2).** Claim: R1 dominates in the 0–6 month window after major AI adoption; B1 / B3 dominate 6–18 months without intervention. *Falsification*: a longitudinal panel of AI-adopting orgs that shows no measurable shift in productivity signal between early and late windows — or shows the opposite pattern — would falsify.
2. **Perception-delay claim (B1).** Claim: perceived output updates faster than measured throughput by a factor of roughly 2–4× in timescale. *Falsification*: METR-style repeat studies in different domains that show perception lagging measurement (would flip the sign of the paradox).
3. **Structural-restructuring delay (B2).** Claim: role redefinition delay in AI-era orgs is bounded below by compensation cycles (annual) and so lags capability shifts (quarterly). *Falsification*: firms that formally redefine roles at quarterly or faster cadences and do *not* see higher Org-Structure-Fit maintenance costs would challenge the delay structure.
4. **Prompt-library evaporation coefficient.** Claim: a non-trivial share (SP: 30–60%) of an un-maintained prompt library becomes obsolete within one major model-version shock. *Falsification*: longitudinal studies of prompt libraries (or tool-library artifacts) across a major model transition that show <10% evaporation would falsify the premise of prompt regression investment.
5. **Migration-Cost Brake (B5).** Claim: bundled vendor contracts and single-provider architecture materially raise migration cost such that B5 dominates over forward-build in post-shock quarters. *Falsification*: multi-provider benchmarking that shows no migration-cost penalty for single-provider architectures under model transition would falsify R4/B5.
6. **Trust-Debt Tipping (B4).** Claim: B4 dominates in consumer-visible / regulated segments and drives reversal (Klarna). *Falsification*: a large set of regulated-domain consumer AI deployments without reversal would challenge the pathway (though Klarna would remain an existence proof).
7. **Teece mapping tightness (iii.5).** Claim: interventions separate cleanly into sensing / seizing / reconfiguring. *Falsification*: empirically, many interventions cross all three (the mapping may be a heuristic rather than a partition — worth testing).
8. **VSM S3–S4 imbalance (iii.6).** Claim: AI-era organizational failures disproportionately come from S4 under-investment (no capability scanning function; no frontier monitoring). *Falsification*: a corpus of post-mortems that attributes failures primarily to S1–S3 breakdowns and not to S4 absence would challenge this.

**What the M2 indicator dashboard must measure to test the model:**

- capability-to-deployment lag (days) — tests delay (iii.2)
- model-switching cost (eng-days / swap) — tests R4 / B5
- role-redefinition frequency (events / 1000 FTE / year) — tests B2
- capability-debt accrual rate — tests B1 / B3
- trust-debt signal (internal incidents + external sentiment composite) — tests B4
- prompt-library evaporation rate — tests the evaporation flow
- adaptation-to-overcorrection ratio (reversals within 12 months / total changes) — tests B4 and Teece reconfiguring quality
- data-asset-growth rate and evaluator-drift rate — test R3 and its counter-forces

**Methodological caveats to flag:**

- *Construct validity*: Trust Debt and Capability Debt are latent constructs. Operationalization (iii.3) is proposed, not validated.
- *Survivor bias*: Klarna is one observable reversal; silent reversals (teams that quietly rolled back) are invisible and likely under-counted.
- *LLM-generated SD models* (flagged in [system-dynamics-ai-adoption.md](../../ai-systems/papers/system-dynamics-ai-adoption.md) §10) are candidate tools for accelerating model construction but require human validation — this memo was drafted by hand for that reason.
- *Boundary choice*: Treating the capability frontier as exogenous is pragmatic, not metaphysical. A fuller model would endogenize vendor strategy (Anthropic, OpenAI, Google) as actors shaping F(t) in response to enterprise demand signals from R5. That extension is reserved for a future memo.

---

## (v) Three-pillar feed — the model *is* the integration

M1's deliverable is explicitly the cross-pillar synthesis. Per section 4 of the [adaptability-framework plan](../plan.md), most prompts feed *into* a synthesis memo; M1 *is* that synthesis at the mid-stage. The model integrates the three pillars as follows:

**Pillar A (AI usage) contributes:**
- R1 (METR Velocity Flywheel) as the dominant near-term reinforcing loop;
- B1 (Capability-Debt Drag, A-flavor) as its balancing counter-force;
- the Prompt-Library Stock and its evaporation flow — the most direct A ↔ T coupling;
- the AI Usage Rate as the common variable that every other pillar's intervention ultimately moves.

**Pillar O (Organization) contributes:**
- R2 (Competence Flywheel) and B2 (Structural-Lag Drag) — the explanation for why capable organizations continue to pull ahead while structurally-rigid ones fall behind even if their technical stack is identical;
- B4 (Trust-Debt Tipping) — the reversal mechanism (Klarna);
- the Org-Structure Fit stock and the Teece / VSM / O'Reilly–Tushman / Hollnagel-Safety-II management-theory overlay.

**Pillar T (Technical infrastructure) contributes:**
- R3 (Data Flywheel) and R4 (Lock-in Reinforcement) — the two structurally opposite reinforcing loops in the tech stack;
- B3 (Capability-Debt Drag, T-flavor) and B5 (Migration-Cost Brake) — the drag on re-architecture;
- the Tooling and Data Asset stocks and the Option-Value stock — the real-options interface to tradespace exploration;
- the direct coupling to the exogenous F(t) capability frontier.

**The coupling is the research object.** The three pillars are not independent; every loop named in (iii.2) crosses at least two pillars. The managerial consequence is that single-pillar interventions are structurally insufficient — patching A alone reopens B2 via O, patching T alone reopens B1 via A. The engineering consequence is that the infrastructure design (Pillar T) must be architected with explicit interfaces to the organizational design (Pillar O) and the usage design (Pillar A), consistent with Crawley's form-function mapping.

**Feed-forward to M2.** The indicator dashboard proposed for M2 should be derived *from* this model — each indicator a direct measurement of a loop's dominant state or of a stock's level. That dashboard will make the loop-dominance hypotheses in (iv) empirically testable and will turn this testable model into a tested one.

**Feed-back to the anchor questions.**
- The *engineering* anchor ("how is the technical infrastructure for an AI-based decision-making system designed and built?") is answered partially here through the T-pillar stock-flow spec and the R3/R4/B3/B5 loops. The architectural design principle that falls out is **preserve switchability** — build for the Option-Value stock, not only for point-optimum performance.
- The *managerial* anchor ("what operational and governance structures are required for it to function effectively in an organization?") is answered partially here through the O-pillar loops and the VSM / Teece / ambidextrous-org overlay. The operational design principle is **maintain S3 ↔ S4 balance** — never let exploitation starve exploration of budget, attention, or charter.

This memo is the first synthesis; it is not the last word. It defines the **structure** that subsequent empirical memos (A1, A2, A3, O1, O2, O3, T1, T2, T3) will populate, and the indicator dashboard (M2) will instrument.

---

## Sources

Primary SDM / management canon:
- Beer, S. (1972). *Brain of the Firm.* Allen Lane.
- Beer, S. (1979). *The Heart of Enterprise.* Wiley.
- Christensen, C. M. (1997). *The Innovator's Dilemma.* Harvard Business School Press.
- Crawley, E., Cameron, B., & Selva, D. (2015). *System Architecture: Strategy and Product Development for Complex Systems.* Pearson.
- Forrester, J. W. (1961). *Industrial Dynamics.* MIT Press.
- Hollnagel, E. (2014). *Safety-I and Safety-II: The Past and Future of Safety Management.* Ashgate.
- Hollnagel, E., Wears, R. L., & Braithwaite, J. (2015). *From Safety-I to Safety-II: A White Paper.*
- Leveson, N. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety.* MIT Press.
- Meadows, D. H. (1999). "Leverage Points: Places to Intervene in a System." Sustainability Institute.
- Meadows, D. H. (2008). *Thinking in Systems: A Primer.* Chelsea Green.
- O'Reilly, C. A., & Tushman, M. L. (2008). "Ambidexterity as a Dynamic Capability." *Research in Organizational Behavior* 28.
- O'Reilly, C. A., & Tushman, M. L. (2013). "Organizational Ambidexterity: Past, Present, and Future." *Academy of Management Perspectives* 27(4).
- Ross, A. M., & Hastings, D. E. (2005). "The Tradespace Exploration Paradigm." INCOSE.
- Sterman, J. D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World.* McGraw-Hill / Irwin.
- Teece, D. J. (2007). "Explicating Dynamic Capabilities." *Strategic Management Journal* 28(13).
- Teece, D. J. (2014). "A Dynamic Capabilities-Based Entrepreneurial Theory of the Multinational Enterprise." *Journal of International Business Studies* 45.

Repository cross-links:
- [research/ai-systems/papers/system-dynamics-ai-adoption.md](../../ai-systems/papers/system-dynamics-ai-adoption.md) — single-pillar precursor
- [research/ai-systems/papers/socio-technical-ai-systems.md](../../ai-systems/papers/socio-technical-ai-systems.md) — Leavitt / Trist STS basis
- [research/ai-systems/papers/ai-risk-resilience.md](../../ai-systems/papers/ai-risk-resilience.md) — STAMP / Safety-II / Safety-III
- [research/ai-systems/papers/ai-tradespace-real-options.md](../../ai-systems/papers/ai-tradespace-real-options.md) — Ross / Hastings tradespace and real-options basis
- [research/ai-systems/papers/ai-system-architecture.md](../../ai-systems/papers/ai-system-architecture.md) — Crawley form-function
- [research/ai-systems/papers/ai-system-lifecycle-ops.md](../../ai-systems/papers/ai-system-lifecycle-ops.md) — T3-flavored technical-debt evidence
- [research/cross-cutting/papers/ai-product-team-transformation.md](../../cross-cutting/papers/ai-product-team-transformation.md) — O-pillar role evidence
- [research/productization-skills/papers/metr-productivity-paradox.md](../../productization-skills/papers/metr-productivity-paradox.md) — METR empirical anchor for R1/B1
- [research/adaptability-framework/plan.md](../plan.md) — the program's plan; M1 is the meta-synthesis prompt
