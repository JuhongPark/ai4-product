# AI Systems Design and Management: An SDM Framework for AI-for-Product

> **Date:** 2026-04-21
> **Purpose:** Establish the top-layer framework for this repository — treating AI-for-product as a **systems engineering and management** problem, in the tradition of MIT SDM (System Design and Management). This frame sits above the lifecycle frame and the skill frame, providing the integrating lens.

---

## 1. Motivation: Why an SDM Frame is the Missing Layer

The repository's prior frames — **product lifecycle** (Discovery → Growth) and **skill domain** (Sales / Productization) — answer *which phase* and *whose work* AI touches. Neither answers the SDM-native questions:

| SDM question | Prior frames' answer | Required frame |
|---|---|---|
| How is the AI system *architected*? | Not explicitly | Architecture decomposition |
| Where are the *interfaces* and *boundaries*? | Implicit | Interface management (MCP, APIs, protocols) |
| What are the *feedback loops* and *emergent behaviors*? | Not modeled | System dynamics |
| How does the socio-technical *whole* achieve joint optimization? | Partial (cross-cutting) | Socio-technical systems theory |
| How does the system *evolve* across its lifecycle? | Not integrated | Lifecycle & evolution |
| What are the *failure modes* and *resilience* strategies? | Anecdotal | Risk & resilience engineering |
| Where is the *Pareto frontier* of architecture choices? | Not quantified | Tradespace exploration |
| What are the *decision rights* and *measurement architecture*? | Partial (governance) | Governance & measurement |

The SDM frame gives **vocabulary, methodology, and artifacts** to address each question rigorously — rather than as vendor-comparison or best-practice checklist.

---

## 2. The Three-Layer Architecture of This Repository

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3 (meta):  AI Systems Design & Management                │
│  ───────────────────────────────────────────────                │
│  Architecture · MBSE · System Dynamics · Socio-Technical ·      │
│  Lifecycle · Risk/Resilience · Tradespace · Governance          │
│  [research/ai-systems/]                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2 (cross-section):  Skill Domain                         │
│  ─────────────────────────────────────                          │
│  Sales Skills  ·  Productization Skills                         │
│  [research/sales-skills/  ·  research/productization-skills/]   │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1 (phases):  Product Lifecycle                           │
│  ─────────────────────────────                                  │
│  Discovery → Design → Development → Management → Growth         │
│  [research/01-discovery/ · 02-design/ · 03-development/ ...]    │
└─────────────────────────────────────────────────────────────────┘
```

Each layer answers a different question. An SDM thesis committee would expect the **Layer 3 analysis to frame** any specific Layer 1 or Layer 2 work.

---

## 3. Six SDM Sub-Disciplines Applied to AI Systems

| # | Sub-discipline | SDM canonical reference | Paper |
|---|---|---|---|
| 1 | **Architecture** (decomposition, interfaces, emergence) | Crawley, de Weck, Dori | [architecture](../research/ai-systems/papers/ai-system-architecture.md) |
| 2 | **MBSE methods** (SysML, OPM, DSM) | Dori (OPM), INCOSE, Eppinger (DSM) | [mbse-for-ai](../research/ai-systems/papers/mbse-for-ai.md) |
| 3 | **System dynamics** (CLDs, feedback loops) | Forrester, Sterman | [system-dynamics](../research/ai-systems/papers/system-dynamics-ai-adoption.md) |
| 4 | **Socio-technical systems** (joint optimization) | Trist (Tavistock), modern STS | [socio-technical](../research/ai-systems/papers/socio-technical-ai-systems.md) |
| 5 | **Lifecycle & operations** (MLOps→LLMOps→AgentOps) | de Weck (strategic engineering), industry | [lifecycle-ops](../research/ai-systems/papers/ai-system-lifecycle-ops.md) |
| 6 | **Risk & resilience** (STAMP/STPA, Safety-II) | Leveson (MIT), Hollnagel | [risk-resilience](../research/ai-systems/papers/ai-risk-resilience.md) |
| 7 | **Tradespace & real options** (Pareto choices, flexibility) | Ross, Hastings, de Weck | [tradespace-options](../research/ai-systems/papers/ai-tradespace-real-options.md) |
| 8 | **Governance & measurement** (RACI, observability) | Madnick/CAMS, enterprise arch. | [governance-measurement](../research/ai-systems/papers/ai-governance-measurement.md) |

---

## 4. The Relationship Between Layers

A concrete example: evaluating an AI coding assistant like Claude Code for productization.

### Layer 1 view (lifecycle)
"AI coding assistants accelerate the Development phase of the product lifecycle."
→ Limited. Tells you nothing about architecture or risk.

### Layer 2 view (skill)
"Claude Code is a productization-skill tool. Compared to Cursor and Copilot on SWE-bench, Claude Code Opus 4.7 scores 87.6%."
→ Better, but still a tool comparison.

### Layer 3 view (SDM)
"Claude Code is a **compound AI system** (Berkeley framing): LLM + tool orchestrator + MCP interface substrate + feedback-collected session context. Its architecture decouples *reasoning* (model) from *actuation* (tool calls via MCP). From an **STS joint optimization** perspective, its value depends on organizational practices: testing discipline, code review depth, training. From a **system dynamics** view, AI adoption creates a balancing loop — productivity rises but technical debt accumulates, potentially reversing gains (see 4x clone-rate data). From a **resilience engineering** view, the failure mode is **silent drift** — code looks reasonable but deviates from project conventions. The **tradespace** choice between Copilot, Cursor, and Claude Code is not about raw benchmark; it's about the architectural commitment — which interfaces (IDE integrations, MCP servers, review tooling) become dependencies."
→ SDM answer. Architectural, dynamic, multi-stakeholder.

---

## 5. Stakeholder Map for AI Systems in Product Organizations

Systems engineering insists on explicit stakeholder analysis. A generic AI product organization:

| Stakeholder | Primary interest | Interface to AI system |
|---|---|---|
| **End user / customer** | Value, privacy, reliability | Product UI / conversational interface |
| **Product team (PM)** | Fit, roadmap, quality | Feature prioritization, telemetry |
| **Engineering** | Maintainability, quality, velocity | Code, CI/CD, observability |
| **Data / ML team** | Model performance, data quality | Training pipelines, eval suites |
| **Security / compliance** | Risk, regulation, auditability | Logging, access controls |
| **Sales / CS** | Win/retain, enablement | CRM integrations, call intelligence |
| **Legal / procurement** | Contracts, liability, vendor risk | AI vendor agreements, IP clauses |
| **Executives / board** | Strategy, ROI, reputation | Dashboards, risk reporting |
| **External: regulators** | Compliance | Audit trails, disclosures |
| **External: vendors** | Integration, renewal | APIs, support SLAs |
| **External: investors** | Performance, defensibility | IR deck, financial model |

Joint optimization across this set is the **actual SDM problem**, not optimizing any single interface.

---

## 6. How This Framework Changes the Prior Work

Each paper in [research/sales-skills/](../research/sales-skills/) and [research/productization-skills/](../research/productization-skills/) is valid as a Layer 2 document but is incomplete without the Layer 3 view. The Layer 3 papers below provide the missing systems lens; cross-references from the skill papers point back to this framework.

### Concrete upgrades enabled by SDM lens

1. **Agentic AI SDR paper** ← gains architecture diagram (orchestrator → action tools → CRM), feedback loops (prospect fatigue balancing loop), resilience view (reversal cases like Klarna)
2. **AI coding assistants paper** ← gains compound AI framing, MCP as interface standard, tradespace Pareto between inline/agent/autonomous modes
3. **MLOps/LLMOps paper** ← reframed from tool list to lifecycle architecture with explicit drift, retrain, retirement phases
4. **DevSecOps paper** ← reframed from vulnerability list to STAMP hazard analysis on AI-generated-code attack surface
5. **All papers** ← gain stakeholder maps, explicit interfaces, and SDM vocabulary

---

## 7. Research Agenda — SDM Thesis-Scale Questions

1. **Reference architecture for compound AI product systems** — Can an INCOSE-style reference architecture be defined for AI-enabled SaaS products? What are the minimum coherent components?
2. **DSM analysis of AI product org structures** — Which organizational forms (centralized AI lab vs. federated model) minimize coupling cost for AI product teams?
3. **System dynamics of AI productivity paradox** — Build an explicit SD model for the METR 2025/2026 result: vendor self-reports, productivity, quality debt, attrition, retraining feedback loops.
4. **STAMP for AI-agent product failures** — Apply Leveson's STAMP to the Klarna customer-service reversal — what control loops failed?
5. **Tradespace of AI product architectures** — Pareto-map cost, latency, quality, privacy, and vendor lock-in across compound-AI system variants.
6. **STS joint optimization experiments** — Empirical studies on team composition + AI tool adoption, explicitly testing Tavistock-style joint optimization hypotheses.
7. **Real options for AI infrastructure investment** — Treat model-provider selection as a portfolio of options, quantify switching costs, and evaluate hedging strategies.
8. **Governance architecture across EU AI Act enforcement** — RACI for product orgs under August 2026 high-risk obligations.

Any of these could be a coherent SDM master's thesis.

---

## 8. Related Documents

- [Sales-Productization skill framework](sales-productization-framework.md) — Layer 2 frame
- [Full lifecycle survey](survey-report.md) — Layer 1 frame
- [research/ai-systems/](../research/ai-systems/) — Layer 3 papers

## 9. Summary

This framework makes the repository **SDM-coherent**: Layer 1 for discipline-traditional coverage, Layer 2 for organizational clarity, Layer 3 (this document) for systems-engineering depth. Only Layer 3 enables the questions that an SDM thesis committee would expect to see defended — and only by keeping all three layers does the research avoid becoming either ivory-tower theory or vendor-comparison journalism.
