# AI System Lifecycle & Operations: From MLOps to LLMOps to AgentOps

> **Date:** 2026-04-21
> **SDM lens:** Lifecycle management (de Weck — "strategic engineering"); value-over-time; operations as integral part of design

---

## 1. Thesis

An AI system is not shipped when it first reaches production — it is shipped when the **operational discipline for its lifecycle** is in place. MIT's **strategic engineering** tradition (de Weck) insists lifecycle value is the objective; architecture and ops must be designed together. 2026's consolidation of **MLOps → LLMOps → AgentOps** represents the industry's alignment with this principle, though the maturity is uneven (MLOps market $4.38B, 39.8% CAGR).

---

## 2. Lifecycle Stages (SDM-canonical)

de Weck's Strategic Engineering framing: lifecycle stages as a **value-generating sequence with explicit flexibility points**. Applied to AI systems:

| Stage | Key decisions | Flexibility levers |
|---|---|---|
| **Concept** | Problem selection, architecture choice | Swap architectures before commitment |
| **Development** | Data strategy, model selection, pipeline design | Model-agnostic interfaces (MCP) |
| **Deployment** | Staging, canary, rollout | Gradual rollout, shadow mode |
| **Operation** | Monitoring, retraining, adaptation | Online eval, hotswap capability |
| **Evolution** | Model upgrades, feature additions | Versioned interfaces |
| **Retirement** | Graceful sunsetting | Data migration, user notice |

Each stage has **optionality value** — the right to defer, swap, or abandon. Real-options analysis (see [tradespace paper](ai-tradespace-real-options.md)) quantifies this.

---

## 3. Three Generations of Ops Discipline

### 3.1 MLOps (2015–2022 origin, mature 2026)
Born from DevOps for ML. Manages:
- Data versioning, feature stores
- Model training pipelines
- Model registry, versioning
- Deployment, canary, rollback
- Monitoring (accuracy, drift)
- Retraining triggers

Mature MLOps 2026 (Flexiana / Medium industry reports): continuous monitoring, auto-retraining on drift, consistent feature-store serving.

### 3.2 LLMOps (2023–2026)
Extends MLOps for generative AI. Additional concerns:
- **Prompt management** — versioning, A/B, safety
- **Cost & latency monitoring** — per-query economics matter
- **Output quality evaluation** — no single "accuracy" metric; complex eval suites
- **Guardrails** — content safety, hallucination checks
- **Retrieval augmentation** — vector store lifecycle
- **Prompt drift** — slow output change over time

LLM observability market: $2.69B (2026) → $9.26B (2030), 36.2% CAGR. Gartner: 60% of SWE teams will use LLM eval/observability by 2028 (from 18% in 2025).

### 3.3 AgentOps (2026 emerging)
AgentOps extends LLMOps for **multi-step, tool-using, autonomous** systems:
- **Workflow graph management** — state machine lifecycle
- **Multi-agent coordination monitoring**
- **Tool call auditing** — MCP traces, permission checks
- **Long-horizon memory management**
- **Reliability engineering** — retry, backoff, graceful degradation
- **Cost attribution across agents**
- **Emergent behavior detection**

Deloitte: 50% of enterprises using GenAI will deploy agents by 2027.

### 3.4 Lifecycle coverage matrix

| Concern | MLOps | LLMOps | AgentOps |
|---|---|---|---|
| Model versioning | ✓ | ✓ | ✓ |
| Data pipelines | ✓ | Partial | Limited |
| Prompt versioning | — | ✓ | ✓ |
| Cost monitoring per call | — | ✓ | ✓ |
| Output quality eval | ✓ (accuracy) | ✓ (multi-metric) | ✓ (workflow-level) |
| Tool call audit | — | Limited | ✓ |
| Multi-agent state | — | — | ✓ |
| Emergent behavior | — | — | Nascent |

AgentOps is **not MLOps + more** — it requires reasoning about **non-deterministic, stateful, multi-component** systems with dependencies the prior disciplines didn't model.

---

## 4. Model Drift — The Core Lifecycle Phenomenon

Production AI models degrade over time. Three drift classes:

| Type | Cause | Detection | Response |
|---|---|---|---|
| **Data drift** | Input distribution changes | Statistical monitoring on input features | Retrain on recent data |
| **Concept drift** | Target relationship changes | Performance monitoring on labeled data | Re-label + retrain |
| **Prompt drift** (LLM-specific) | Upstream model behavior changes (e.g., vendor updates base model) | Continuous eval on held-out set | Re-validate prompts; adjust |

Prompt drift is novel to LLM era — the **vendor can change the model without changing the version you call**, invalidating prompts. This is an interface-stability architectural concern, not just an ops one.

---

## 5. Retirement — The Often-Skipped Stage

de Weck's lifecycle framing specifically emphasizes **end-of-life design**. AI systems exhibit under-designed retirement:

- **Data migration**: model-generated artifacts (embeddings, summaries) may not be meaningfully portable
- **User expectations**: customers depend on specific AI behaviors; retiring features can trigger churn
- **Regulatory obligations**: retention periods for AI decisions continue post-retirement
- **Learnings capture**: if the AI system is retired, what is preserved? (Reinforcement learning trajectories, prompt libraries, eval suites)

Canonical SDM practice: design retirement during Concept stage, not at decommission.

---

## 6. Lifecycle Value Quantification (de Weck approach)

**Lifecycle cost (LCC)** = sum of cost across stages:
- Concept: architect time, initial data acquisition
- Development: engineering, infra, initial training
- Deployment: integration, testing, rollout
- Operation: inference compute, monitoring, on-call, retraining
- Evolution: major upgrades, re-architecture
- Retirement: decommission, data migration

**Lifecycle value** = expected benefit streams over the same stages.

**Key SDM insight (de Weck)**: lifecycle cost is **dominated by operation**, not concept or development. For AI systems this is amplified — per-query inference cost accumulates quickly at scale. Architecture decisions that trade concept/development cost for operational efficiency (caching, model routing, compression) dominate LCC.

### Illustrative LCC distribution for a mid-size AI product
| Stage | % of 5-year LCC |
|---|---|
| Concept + Development | 10–15% |
| Deployment | 5% |
| **Operation (including retraining)** | **60–75%** |
| Evolution | 10–15% |
| Retirement | 2–5% |

This distribution is **why LLMOps/AgentOps matters so much**: the operational stage is the biggest cost lever.

---

## 7. Flexibility as Designed-in Value (Strategic Engineering)

de Weck's strategic engineering research group explicitly builds **flexibility value** into architecture. Applied to AI:

| Flexibility | Architectural enabler | Value captured |
|---|---|---|
| Model swap | Strong model interface (MCP, standardized calls) | Ride commodity price declines |
| Vendor swap | Multi-vendor abstraction layer | Avoid lock-in, hedge pricing |
| Scaling (up/down) | Auto-scaling infra, batch modes | Match cost to demand |
| Feature deprecation | Versioned APIs, sunset process | Graceful evolution |
| Stake withdrawal | Separable data, portable outputs | Reduced retirement cost |

Each is a **real option** (see [tradespace paper](ai-tradespace-real-options.md)). An SDM architect budgets for flexibility explicitly.

---

## 8. Stakeholders Across the Lifecycle

| Stage | Primary stakeholder |
|---|---|
| Concept | PM, Architect, Executive |
| Development | Engineering, Data Science |
| Deployment | SRE, Security |
| Operation | Operators, End users, Support |
| Evolution | Product, R&D |
| Retirement | Legal, End users, Data governance |

The **same AI system** has **different decision-makers at different stages**. Governance (next paper) must track the handoff.

---

## 9. Research Gaps

1. **Retirement case studies** — Industry has few documented AI retirement playbooks
2. **Prompt drift measurement** — No standard methodology; vendors inconsistent about model-version disclosures
3. **LCC modeling for AI** — Frameworks exist conceptually; empirical data sparse
4. **Cross-stage handoff friction** — Unmeasured cost of miscommunication at stage transitions
5. **AgentOps maturity model** — No accepted maturity framework analogous to Flexiana's MLOps 4-stage model

---

## 10. Sources

- de Weck, O. MIT Strategic Engineering Research Group. http://strategic.mit.edu/deweck.php
- de Weck, O. Research profile. https://aeroastro.mit.edu/people/olivier-de-weck/
- de Weck, O. Google Scholar citations. https://scholar.google.com/citations?user=GFEciiAAAAAJ&hl=en
- TechTarget. "What is LLMOps? Lifecycle, benefits and challenges." https://www.techtarget.com/searchenterpriseai/definition/large-language-model-operations-LLMOps
- Flexiana (2026). "What Mature MLOps Really Looks Like in 2026." https://flexiana.com/news/ai/what-mature-mlops-really-looks-like-zin-2026-from-experiments-to-enterprise-scale-ai-systems
- Medium (tealamenta, Feb 2026). "MLOps in 2026: From MLflow to LLMOps." https://medium.com/codex/mlops-in-2026-from-mlflow-to-llmops-the-complete-guide-to-shipping-ai-in-production-0024955b70c4
- Medium (Sanjeeb Panda). "Complete MLOps/LLMOps Roadmap for 2026." https://medium.com/@sanjeebmeister/the-complete-mlops-llmops-roadmap-for-2026-building-production-grade-ai-systems-bdcca5ed2771
- Ideas2IT. "LLMOps vs MLOps: Key Differences." https://www.ideas2it.com/blogs/llmops-vs-mlops-key-differences-and-evolution
- Medium (AppVin). "LLMOps: Managing Lifecycles of AI Agents." https://medium.com/@appvintechnologies/llmops-managing-lifecycles-of-ai-agents-in-production-a7aed1d78ecb
- Flexiana (Mar 2026). "MLOps Maturity Model 2026." https://medium.com/@flexianadevgroup/mlops-maturity-model-2026-4-stages-to-resilient-risk-free-machine-learning-468c097dc25c
- Microsoft Foundry. "Observability in Generative AI." https://learn.microsoft.com/en-us/azure/foundry/concepts/observability
- Solulab. "AIOps, MLOps, and LLMOps." https://www.solulab.com/aiops-mlops-llmops-practical-comparison
