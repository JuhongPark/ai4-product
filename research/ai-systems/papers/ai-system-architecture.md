# AI System Architecture: Decomposition, Interfaces, and Emergence

> **Date:** 2026-04-21
> **SDM lens:** System architecture (Crawley, de Weck); compound-AI systems (Berkeley BAIR)

---

## 1. Thesis

Treating an AI-powered product as a **single model with an interface** is architecturally inadequate. Production AI systems in 2026 are **compound AI systems** — modular, extensible, multi-component assemblies. Architecture decisions at this level (how components decompose, which interfaces are stable, what is emergent) dominate the product's long-run cost, risk, and value delivery — far more than the choice of base model.

---

## 2. The Compound AI Systems Shift (Berkeley BAIR, Feb 2024)

Zaharia, Khattab, Chen, Davis, Miller, Potts, Zou, Carbin, Frankle, Rao, Ghodsi. **"The Shift from Models to Compound AI Systems."** Berkeley BAIR Blog, February 2024. https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/

**Core claim:** *"State-of-the-art AI results are increasingly obtained by compound systems with multiple components, not just monolithic models."*

**Definition:** A Compound AI System (CAIS) tackles tasks using **multiple interacting components** — including multiple calls to models, retrievers, or external tools.

**Implication for architecture:** Leading AI results are achieved through **clever engineering, not just scaling training**. The system architect's decisions become as consequential as the model builder's.

---

## 3. A Reference Architecture (Four Layers)

Consolidating from IEEE survey work (Chen et al., arxiv 2501.12904) and industry convergence:

```
┌───────────────────────────────────────────────────────────────┐
│ L4 Presentation                                               │
│    User interfaces, conversational surfaces, tool-invoked UIs │
├───────────────────────────────────────────────────────────────┤
│ L3 Application Logic                                          │
│    Business workflows, orchestration graphs (state machines), │
│    human-in-the-loop gates, feedback collection               │
├───────────────────────────────────────────────────────────────┤
│ L2 LLM Integration                                            │
│    Model routing, prompt management, tool calling,            │
│    retrieval (RAG), memory, guardrails, evaluation            │
├───────────────────────────────────────────────────────────────┤
│ L1 Data Management                                            │
│    Vector stores, document stores, telemetry,                 │
│    training & fine-tuning pipelines                           │
└───────────────────────────────────────────────────────────────┘
                        ↕ cross-layer
              Observability · Governance · Security
```

Each layer exposes **stable interfaces** to the next. Governance and observability cross-cut all layers.

---

## 4. Interfaces as Architectural Commitments

The 2026 architectural frontier is **interface standardization**. Three levels:

### 4.1 Intra-system interface: Tool invocation protocol
How the LLM calls tools. Historically model-specific function calling; by 2026, **MCP (Model Context Protocol)** is the dominant standard.

- **MCP origin**: Anthropic, November 2024
- **Stewardship**: Donated to Agentic AI Foundation (Linux Foundation) December 2025 with Block and OpenAI co-founding
- **Adoption**: 10,000+ active public MCP servers by 2026
- **Enterprise integration**: Gainsight MCP (April 2026), Carta Plugins for Claude
- **Technical**: Client-server, JSON-RPC, sub-50ms response time at 10k concurrent connections

**Architectural consequence:** MCP lets the *reasoning layer* (model) be swapped independently of the *action layer* (tools). This is the canonical **interface decoupling** move — making both sides substitutable.

### 4.2 Agent-to-agent interface
Multi-agent orchestration patterns emerging as standards (2026):

- **Sequential chain** — deterministic linear pipeline
- **Hierarchical orchestrator-sub** — most common production pattern (ref: Beam.ai 2026)
- **Explicit workflow graph** — state machine with nodes (tool/LLM calls) and edges (permitted transitions); **LangGraph** is representative

**Industry shift observed 2025→2026**: from *"open-ended multi-agent chat loops"* to *"explicit workflow graphs"* (i.e., flow engineering).

### 4.3 System-to-enterprise interface
- Traditional: REST/GraphQL APIs
- 2026: MCP as enterprise data substrate (Gainsight, Carta precedents)
- Emerging: agent-to-enterprise-agent protocols (e.g., Google's A2A)

---

## 5. Architectural Patterns for Production (2026)

From beam.ai and BAIR analyses, six production-validated multi-agent patterns:

| Pattern | When to use | Failure mode |
|---|---|---|
| **Single-agent with tools** | Well-scoped, deterministic task | Under-scaling on complex tasks |
| **Sequential pipeline** | Clear stages, predictable flow | Single-point failure cascades |
| **Hierarchical orchestrator** | Complex workflow with sub-tasks | Orchestrator becomes bottleneck/SPOF |
| **Parallel fan-out/fan-in** | Independent sub-tasks, aggregation | Coordination overhead, partial failures |
| **Explicit workflow graph** | Production workflows with checkpoints | Graph complexity rivals state-machine complexity |
| **Fully autonomous multi-agent chat** | Research/exploration only | Drift, loops, non-termination |

**Canonical finding (2026):** *"A weaker model with strong orchestration often outperforms a stronger model with poor orchestration."* Architecture compounds.

---

## 6. Emergence — The Architecturally Hard Part

Multi-agent systems exhibit **emergent behaviors** not predictable from components alone. Observed in 2026 production:

- **Convergent drift** — Multiple agents optimizing locally converge on globally suboptimal outcomes
- **Protocol degradation** — Tool-call accuracy degrades when multiple agents share state
- **Feedback amplification** — Minor prompt changes propagate into major output shifts after several hops
- **Adversarial collusion** (hypothetical, emerging concern) — Independent AI pricing agents tacitly coordinating (see Morgan Lewis 2026 on negotiation AI provisions)

Emergence is the **systems-engineering distinguishing concern**. Component-level review catches none of it; only whole-system monitoring and architectural constraints reduce it.

---

## 7. Architectural Tensions (Design Principles)

| Tension | Lean toward | When to reverse |
|---|---|---|
| Monolithic model ↔ Compound system | Compound | When latency/cost of compositions exceeds monolithic value |
| Free-form agent chat ↔ Explicit graph | Graph | Exploratory research only |
| Strong single interface ↔ Many weak ones | Strong (MCP) | Legacy systems with no migration budget |
| Synchronous ↔ Async | Async for reliability | Real-time user-facing flows |
| Human-out-of-loop ↔ HITL gate | HITL at high-stakes | Low-stakes autonomous ops |
| Vendor API ↔ Self-hosted model | Vendor for speed, self-host for IP control | Depends on data sensitivity & scale |

---

## 8. Stakeholders and Their Architectural Concerns

| Stakeholder | Primary concern | Architectural lever |
|---|---|---|
| End user | Reliability, privacy | HITL gates, data minimization |
| PM | Velocity | Orchestration simplicity |
| Engineering | Maintainability | Strong interfaces, testability |
| Security | Attack surface | Fewer trust boundaries, MCP access control |
| Legal/compliance | Auditability | Explicit logging at every layer |
| Finance | Cost | Model-routing, caching, latency SLA |
| Executive | Strategic option | Avoiding lock-in, swappability |

Joint optimization across this stakeholder set is the architect's job — not just technical correctness.

---

## 9. Research Gaps

1. **Reference architecture formalization** — No INCOSE-endorsed reference architecture for compound AI product systems exists yet
2. **Emergent-behavior detection** — No accepted methodology for predicting or monitoring emergent failure modes
3. **Interface versioning** — MCP versioning under active development; production migration patterns untested
4. **Architecture decay** — As models evolve faster than systems, architectures accumulate latent mismatches; rate unmeasured

---

## 10. Sources

- Zaharia et al. (2024). "The Shift from Models to Compound AI Systems." Berkeley BAIR. https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/
- Chen et al. (2025). "A Functional Software Reference Architecture for LLM-Integrated Systems." arXiv:2501.12904. https://arxiv.org/pdf/2501.12904
- "From Standalone LLMs to Integrated Intelligence: A Survey of Compound AI Systems" (2025). arXiv:2506.04565. https://arxiv.org/html/2506.04565v1
- "A Blueprint Architecture of Compound AI Systems for Enterprise" (2024). arXiv:2406.00584. https://arxiv.org/html/2406.00584v1
- "ALTO: An Efficient Network Orchestrator for Compound AI Systems" (2024). ACM SIGCOMM / arXiv:2403.04311. https://dl.acm.org/doi/10.1145/3642970.3655844
- SALLMA (2025). "Prototypical Software Architecture for LLM-Based Multi-Agent Systems." ICSE 2025 SATrends. https://conf.researchr.org/details/icse-2025/satrends-2025-papers/7/SALLMA-A-Prototypical-Software-Architecture-for-LLM-Based-Multi-Agent-Systems
- IEEE Access (2024). "A Review on Large Language Models." https://ieeexplore.ieee.org/document/10433480/
- "Software Architecture Meets LLMs" (2025). arXiv:2505.16697. https://arxiv.org/pdf/2505.16697
- Anthropic (Nov 2024). Model Context Protocol origin. https://modelcontextprotocol.io/specification/2025-11-25
- Beam.ai (2026). "6 Multi-Agent Orchestration Patterns for Production." https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- Exabeam. "Agentic AI Architecture: Types, Components, Best Practices." https://www.exabeam.com/explainers/agentic-ai/agentic-ai-architecture-types-components-best-practices/
- Kore.ai. "Agentic architecture: blueprint for enterprise AI." https://www.kore.ai/blog/agentic-architecture-blueprint-for-intelligent-enterprise
- arxiv (2026). "Agentic AI: Architectures, Taxonomies, and Evaluation." arXiv:2601.12560. https://arxiv.org/html/2601.12560v1
- Agentic AI Foundation / Linux Foundation MCP stewardship (December 2025).
