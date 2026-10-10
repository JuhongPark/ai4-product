# AI Systems Design & Management

> **Scope:** Treat AI-for-product as a **systems engineering & management** problem, applying MIT SDM-canonical frameworks (architecture, MBSE, system dynamics, socio-technical, lifecycle, risk/resilience, tradespace, governance).

> This is the Layer 3 meta-frame of the repository. See [docs/ai-systems-design-management-framework.md](../../docs/ai-systems-design-management-framework.md) for how this relates to Layer 1 (lifecycle) and Layer 2 (skill).

---

## Sub-disciplines

| # | Paper | SDM methods applied |
|---|---|---|
| 1 | [AI System Architecture](papers/ai-system-architecture.md) | Decomposition, interfaces, emergent behavior, compound AI systems |
| 2 | [MBSE for AI](papers/mbse-for-ai.md) | SysML, OPM (Dori), DSM (Eppinger), structured models for AI systems |
| 3 | [System Dynamics of AI Adoption](papers/system-dynamics-ai-adoption.md) | Causal loop diagrams, feedback loops, productivity-paradox SD model |
| 4 | [Socio-Technical AI Systems](papers/socio-technical-ai-systems.md) | Joint optimization (Trist), STS theory, Leavitt's diamond applied to AI |
| 5 | [AI System Lifecycle & Ops](papers/ai-system-lifecycle-ops.md) | Concept→retirement; MLOps→LLMOps→AgentOps architecture |
| 6 | [AI Risk & Resilience](papers/ai-risk-resilience.md) | STAMP/STPA (Leveson, MIT), Safety-II/III, resilience engineering (Hollnagel) |
| 7 | [AI Tradespace & Real Options](papers/ai-tradespace-real-options.md) | Pareto frontier, Ross/Hastings TSE paradigm, real-options for AI investment |
| 8 | [AI Governance & Measurement](papers/ai-governance-measurement.md) | RACI, decision rights, enterprise architecture for AI, LLM observability |

---

## Key SDM-canonical references applied

| Author / institution | Contribution | How used here |
|---|---|---|
| **Olivier de Weck** (MIT Aero/SDM) | Strategic engineering, lifecycle value, flexibility | Lifecycle, tradespace papers |
| **Dov Dori** (MIT) | Object-Process Methodology (OPM), ISO 19450 | MBSE paper |
| **Edward Crawley** (MIT) | System architecture textbook | Architecture paper |
| **Steven Eppinger** (MIT) | Design Structure Matrix (DSM) | MBSE paper |
| **Daniel Hastings** (MIT) | Tradespace exploration paradigm | Tradespace paper |
| **Adam Ross** (MIT) | Multi-attribute tradespace exploration (MATE) | Tradespace paper |
| **Nancy Leveson** (MIT) | STAMP, STPA, Safety-III | Risk/resilience paper |
| **Stuart Madnick** (MIT CAMS) | Cybersecurity governance, federated learning | Governance paper |
| **Donna Rhodes** (MIT) | Resilience engineering | Risk/resilience paper |
| **Jay Forrester / John Sterman** (MIT) | System dynamics, Business Dynamics | System dynamics paper |
| **Eric Trist / Tavistock** | Socio-technical systems | STS paper |
| **Erik Hollnagel** | Safety-II, resilience | Risk/resilience paper |
| **INCOSE** | SEBoK, SE body of knowledge, AI Systems WG | All papers |

---

## Thesis-scale research questions (embedded in papers)

1. Reference architecture for compound AI product systems (INCOSE-style)
2. DSM analysis of AI-product org structures
3. SD model of the METR productivity paradox
4. STAMP applied to Klarna-style customer-service reversals
5. Tradespace of compound-AI system variants
6. STS joint-optimization empirical experiments
7. Real options model for AI infrastructure investment
8. Governance architecture under EU AI Act August 2026 enforcement

Each is suitable as an SDM master's thesis scope.

## Related extension

[Organizational adaptability](../adaptability-framework/README.md) extends this meta-frame to repeated AI-driven change across AI usage, organizational structure, and technical infrastructure. It contains a research plan and eleven draft memos. Source audit and final synthesis remain pending.
