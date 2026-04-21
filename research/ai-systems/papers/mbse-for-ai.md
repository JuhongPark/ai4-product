# Model-Based Systems Engineering (MBSE) for AI: SysML, OPM, DSM

> **Date:** 2026-04-21
> **SDM lens:** MBSE methods (SysML v2, OPM/Dori, DSM/Eppinger); MIT-canonical formal methods applied to AI system design

---

## 1. Thesis

Narrative descriptions of AI systems ("orchestrator with tools") are insufficient for design, review, and evolution. SDM's tradition of **Model-Based Systems Engineering** — formal, executable, review-able models — is the appropriate rigor for AI systems that will persist and evolve over years. Three MIT-canonical methods apply directly:

- **SysML v2** (2025 release) — structural and behavioral modeling, now with AI-assisted authoring
- **OPM** (Dori, MIT/Technion; ISO 19450) — single-paradigm object + process modeling
- **DSM** (Eppinger, MIT) — dependency and coupling analysis

---

## 2. SysML v2 for AI Systems

The 2025 release of **SysML v2** is a significant advance in MBSE expressiveness and interoperability. Key for AI systems:

- **Improved precision** — stronger typing, more rigorous semantics
- **Expressiveness** — complex constraint modeling
- **Interoperability** — better integration with downstream tooling

### AI-assisted MBSE (2025+)
IBM's **Engineering AI Hub 1.1** adds an MBSE use-case discovery agent that interprets natural-language requirements and creates model elements in Rhapsody (SysML v1 & v2). Rosenberg, Weilkiens, Moberley published **"AI Assisted MBSE with SysML"** (2025).

**Caveat (Wiley INCOSE 2025)**: LLMs generate useful **skeleton** models, but complete AI-generated models contain critical errors. The pattern is **human-led, AI-augmented MBSE authoring** — exactly the selective-complementarity model from the Nature (2024) meta-analysis.

### What to model in an AI system with SysML
| Element | SysML construct | Example |
|---|---|---|
| Components | Block | `Orchestrator`, `LLMClient`, `ToolRegistry`, `MCPServer`, `VectorStore` |
| Interfaces | Interface + InterfaceDefinition | `MCP over JSON-RPC`, `REST to CRM` |
| State machines | StateMachine | Workflow graph nodes/edges |
| Parametric constraints | Constraint | Latency ≤ 300ms, cost/query ≤ $0.01 |
| Requirements | Requirement | Availability, privacy, explainability |
| Verification | Verification case | Eval suite, red-team scenarios |

---

## 3. Object-Process Methodology (OPM) for AI

Dov Dori's **OPM** (Springer 1999, revised editions; ISO/PAS 19450 in 2014) is especially well-suited to AI systems because of its **bimodal** representation:

- **OPD** (Object-Process Diagrams) — visual
- **OPL** (Object-Process Language) — natural-English sentences auto-generated from the diagram

OPM's **minimal ontology** — only Objects, Processes, and Relations — matches how AI system architects already think ("Agent [object] executes Plan [process] producing Result [object]").

### Why OPM is a fit for AI systems
1. **Executable** — OPCAT can animate the model, simulating behavior over time
2. **Single diagram for structure + behavior** — unlike SysML's multiple diagram types, OPM keeps both in one view, reducing consistency burden
3. **ISO standardized** (19450) — defensible in regulated contexts

### Minimal OPM-style textual model of an agentic AI system
Using OPL-like sentences (illustrative):

```
User sends Query to Orchestrator.
Orchestrator invokes Retrieval retrieving Context from VectorStore.
Orchestrator invokes Generation using Model with Context producing Draft.
Orchestrator invokes ToolCall through MCP interacting with EnterpriseSystem producing ToolResult.
Orchestrator invokes Refinement using Draft and ToolResult producing Response.
Response is returned to User.
ObservabilityPipeline consumes Query, Context, Draft, ToolResult, Response producing Trace.
```

This yields an executable, auditable system description usable by non-engineers.

---

## 4. Design Structure Matrix (DSM) for AI Systems

Eppinger's **DSM** (MIT Sloan, 1991 foundational paper; Sookocheff 2020s software applications) is the method for **coupling analysis**. For AI systems, DSM reveals:

- **Which components are tightly coupled** (and therefore must co-evolve)
- **Where cycles exist** (and therefore cannot be cleanly modularized)
- **Cluster structure** (natural sub-system boundaries)

### DSM for an AI product system

Illustrative DSM (rows and columns are components; cell value 1 = dependency):

| | UI | Orchestrator | Model | Retrieval | VectorStore | ToolRegistry | MCPSrv | CRM | Observability |
|---|---|---|---|---|---|---|---|---|---|
| **UI** | | 1 | | | | | | | 1 |
| **Orchestrator** | 1 | | 1 | 1 | | 1 | | | 1 |
| **Model** | | 1 | | | | | | | 1 |
| **Retrieval** | | 1 | | | 1 | | | | 1 |
| **VectorStore** | | | | 1 | | | | | 1 |
| **ToolRegistry** | | 1 | | | | | 1 | | 1 |
| **MCPSrv** | | | | | | 1 | | 1 | 1 |
| **CRM** | | | | | | | 1 | | 1 |
| **Observability** | | | | | | | | | |

Observations (typical for 2026 agentic systems):
- **Orchestrator is the hub** — high row + column weight; change-risk concentration
- **Observability is a sink** — depends on nothing, many depend on it; good
- **MCP decouples enterprise systems** — without MCP, every agent-to-enterprise link would be a direct DSM edge; with MCP, the coupling is one-to-many through a single substrate
- **Model is upstream** — only Orchestrator touches it; enabling model swapping

### DSM-based refactoring
When clusters are identified, the system can be refactored to **move coupling inside clusters** (reducing inter-cluster change propagation). Canonical Eppinger use case.

---

## 5. The Combined Methodology

| Phase | Method | Output |
|---|---|---|
| Conceive | OPM | High-level executable system description |
| Architect | SysML v2 | Block + interface + state-machine formal model |
| Analyze | DSM | Coupling clusters, refactoring targets |
| Verify | SysML Parametric | Constraint-satisfaction check |
| Evolve | All three | Changed models regenerate diagrams, language, coupling analysis |

The **combined use** — OPM for stakeholder-friendly concept, SysML for engineering rigor, DSM for coupling management — is the characteristic SDM approach.

---

## 6. Case Study: DSM-Analysis of Organizational Coupling in AI Product Teams

Beyond product DSM, **organizational DSM** (Sosa, Eppinger, Rowles 2004) models *team-to-team* dependencies. For AI product orgs:

- Where does **engineering** need to interact with **data science**?
- Where does **security** need visibility into **model development**?
- Where does **legal/compliance** gate **deployment**?

The **team-DSM vs. product-DSM misalignment** predicts integration friction. AI product orgs often exhibit:
- Product-DSM: Orchestrator is central, many dependencies
- Team-DSM: No single team owns orchestration
- → Chronic integration-rework cost at the orchestration layer

This is an **SDM-native research question** — one we flag under Section 8.

---

## 7. Stakeholders

| Stakeholder | MBSE usage |
|---|---|
| System architect | Primary author, maintains SysML/OPM models |
| PM | Reads OPD/OPL for stakeholder alignment |
| Engineering | Uses SysML for spec; DSM for module boundaries |
| Security | Uses SysML parametric constraints for threat modeling |
| Compliance | Uses OPM/SysML as audit artifacts |
| External reviewer (SDM committee) | Uses models to judge design rigor |

---

## 8. Research Gaps

1. **OPM for agentic systems** — No published OPM reference model for compound AI systems
2. **SysML v2 + AI-generated content** — How does auto-generated SysML degrade model integrity?
3. **DSM for AI product org design** — Which organizational structures minimize change propagation for AI products?
4. **Executable OPM simulation at scale** — Does OPCAT-style simulation scale to 20+ component AI systems?
5. **Formal verification of AI compound systems** — SysML + TLA+ or Alloy for non-trivial behavior verification

---

## 9. Sources

- Dori, D. (1995–present). Object-Process Methodology foundational papers. https://www.omgwiki.org/MBSE/doku.php?id=mbse:doriobjmethodology
- Dori, D. *Object-Process Methodology: A Holistic Systems Paradigm.* Springer. https://link.springer.com/book/10.1007/978-3-642-56209-9
- ISO/PAS 19450 (2014). OPM as international standard.
- INCOSE (2008). Recognition of OPM as one of six core MBSE methodologies.
- Eppinger, S. (MIT Sloan). DSM foundational work. https://dsmweb.org/
- MIT Sloan Executive Education. "The Design Structure Matrix: Helping to See Complexity." https://executive.mit.edu/the-design-structure-matrix.html
- Sookocheff, K. "Improving Software Architecture Using a Design Structure Matrix." https://sookocheff.com/post/dsm/improving-software-architecture-using-design-structure-matrix/
- Rosenberg, Weilkiens, Moberley (2025). *AI Assisted MBSE with SysML: An Integrated Systems/Software Approach.* https://mbse4u.com/books/ai-assisted-mbse-with-sysml/
- SysON (2025). "NextGen SysML Modeling Tool." https://mbse-syson.org/
- IBM (2025). "AI automations for Model Based Systems Engineering." https://www.ibm.com/new/announcements/new-ai-automations-for-model-based-systems-engineering
- Rafique et al. (2025). "Enhancing MBSE with LLMs." INCOSE International Symposium. https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/iis2.70067
- de Gruyter (2024). "AI-Augmented Model-Based Systems Engineering." https://www.degruyterbrill.com/document/doi/10.1515/zwf-2024-0123/html?lang=en
- Springer (2021). "Object-Process Methodology for Intelligent System Development." https://link.springer.com/chapter/10.1007/978-3-030-91581-0_3
