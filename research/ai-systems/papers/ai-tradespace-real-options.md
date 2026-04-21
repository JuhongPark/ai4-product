# AI Tradespace Exploration and Real Options

> **Date:** 2026-04-21
> **SDM lens:** Tradespace Exploration (Ross & Hastings MIT); real options valuation (Myers, Dixit-Pindyck); MIT Strategic Engineering (de Weck)

---

## 1. Thesis

AI architecture decisions are typically made by **point-comparison** ("Tool A vs. Tool B on benchmark X"). SDM's **Tradespace Exploration (TSE)** — developed at MIT by Ross and Hastings — treats the full design-space as a first-class object, enumerating architectures and revealing the **Pareto frontier** where no architecture dominates another. Combined with **real options valuation**, which prices the flexibility to switch architectures later, TSE gives product organizations a defensible way to make AI architecture decisions under uncertainty.

---

## 2. Tradespace Exploration: The MIT-Canonical Method

**Adam Ross** and **Daniel Hastings** formalized multi-attribute TSE at MIT. Foundational paper: Ross & Hastings, INCOSE 2005. https://web.mit.edu/adamross/www/Ross_INCOSE05.pdf

### Method
1. **Enumerate** candidate architectures spanning design decisions (model choice, orchestration pattern, hosting, memory, etc.)
2. **Evaluate** each against multiple attributes — cost, latency, quality, privacy, vendor lock-in, maintainability
3. **Visualize** as a tradespace — typically 2D projections of high-dimensional Pareto frontier
4. **Identify** non-dominated architectures — no other architecture is better in *all* dimensions
5. **Select** among Pareto-optimal candidates based on stakeholder preferences

Canonical visualization: scatter plot of cost (x-axis) vs. utility (y-axis); the upper-envelope is the Pareto frontier.

---

## 3. A Tradespace for a Compound AI System

Design decisions (architectural):

| Decision | Options |
|---|---|
| Base model | GPT-5.4 · Claude Opus 4.7 · Gemini 3.1 Pro · Self-hosted Llama 4 · Korean sovereign (HyperCLOVA X, EXAONE) |
| Orchestration | Single call · Sequential chain · Orchestrator-sub · Workflow graph · Multi-agent chat |
| Memory | None · Session · Long-term vector · Hybrid |
| Retrieval | None · Keyword · Dense vector · Hybrid |
| Tool interface | Model-specific function calling · MCP · Custom REST |
| Hosting | Vendor API · Hybrid · Self-hosted |
| Safety | Post-hoc filter · Inline guardrail · Multi-stage |
| Observability | Minimal · Standard LLMOps · Full AgentOps |

Combinatorial space (illustrative): 5 × 5 × 4 × 4 × 3 × 3 × 3 × 3 ≈ 32,400 architectures.

### Evaluation attributes (multi-attribute)
- Cost per query ($)
- Latency p95 (ms)
- Quality (task-specific eval score, 0–1)
- Privacy (ordinal: data-leaves-premises, region-locked, etc.)
- Vendor lock-in (ordinal: replaceability)
- Maintainability (FTE-equivalent)
- Flexibility option value (see §5)

### Pareto frontier in 2D projection (cost vs. quality)
Rough qualitative pattern (illustrative, based on 2026 benchmark literature):

```
Quality
 ↑
 │                                  ● Claude Opus 4.7 + MCP + workflow-graph
 │                              ● GPT-5.4 + sequential
 │                           ● Gemini 3.1 Pro + sequential  ← Pareto
 │                        ● Claude Opus 4.6 + chain         frontier
 │                   ● Self-hosted Llama 4 + hybrid            
 │               ● Smaller vendor model + basic
 │          ●
 │       ● Cheap base + minimal
 │    ●
 └────────────────────────────────────────→  Cost per query
```

Non-Pareto architectures (dominated — lower quality at higher cost) are identified and excluded from consideration.

---

## 4. The Tradespace Tells You What "Best" Means

Different stakeholders have different utility functions:
- **Cost-sensitive operation**: maximize utility at lowest cost → bottom-left of Pareto frontier
- **Quality-first enterprise**: maximize quality regardless → upper-right
- **Privacy-constrained (healthcare, finance)**: remove all non-privacy-safe architectures from tradespace first
- **Flexibility-first (startups)**: maximize option value (§5) over point utility

The **same tradespace answers multiple stakeholder questions** — this is the SDM virtue over point decisions.

---

## 5. Real Options for AI Investment

Real options theory (Myers 1977; Dixit & Pindyck 1994) prices **flexibility**. Applied to AI investments, flexibility is architectural:

### Types of real options relevant to AI systems

| Option | Instance in AI architecture |
|---|---|
| **Option to switch** | MCP interface → swap LLM vendor |
| **Option to abandon** | Pilot deployment → cancel without full rollout cost |
| **Option to expand** | Initial narrow use case → broaden with same architecture |
| **Option to defer** | Choose modular architecture → wait to decide agents vs. humans |
| **Option to stage** | Sequential rollout, each stage gated on success |

### Real-options framing vs. NPV

Traditional NPV asks: *does the AI investment produce positive NPV at the required IRR?*

Real options asks: *what is the value of the flexibility built into this architecture, given future uncertainty?*

For AI, where **model quality improves 10–50% per year**, flexibility to swap models is worth **substantial option value** — possibly exceeding the base NPV. McKinsey's *"The real power of real options"* makes this case generically; applied to AI it is decisive.

### Worked example (illustrative)

Architecture A: Custom vendor-API calls directly embedded in code.
Architecture B: Same functionality behind MCP abstraction.

Architecture B costs 15% more up-front. But:
- A year later, a cheaper/better model emerges (say, 50% better per $)
- Architecture A: rewrite required. Cost: 80% of original engineering.
- Architecture B: swap MCP server binding. Cost: ~5% of engineering.

Option value of Architecture B's flexibility dominates the 15% upfront premium over any 2+ year horizon. This is exactly the pattern that **interface standardization** (MCP) captures.

---

## 6. Build vs. Buy as Real Options Question

Industry framing ("Build vs. Buy") is actually three options:

| Option | Cost profile | Option value |
|---|---|---|
| **Build** | High capex, low opex | Customization; IP retention; but no optionality to switch |
| **Buy (vendor)** | Low capex, high opex | Fast start; but lock-in risk |
| **Build on top of vendor (hybrid)** | Medium capex, medium opex | Flexibility to substitute layer-by-layer |

2026 empirical pattern: Stanford Enterprise AI Playbook finds **vendor-led (Buy) succeeds 67% vs. internal Build at 33%** — but this doesn't invalidate Build; it reframes: *the organizations choosing Build likely had justifications (IP, regulatory) that make partial-hybrid the SDM-rigorous choice*.

### Layered decision (Cabin co, 2026)
> *"The real question is: at which layer of the AI stack do you need proprietary capability, and where is a commodity solution good enough? The integration layer — how your AI system connects to your internal data, your existing workflows, and your downstream systems — is almost always a build."*

This is TSE plus real options: **decompose the stack → evaluate each layer in its own tradespace → retain flexibility at each layer**.

---

## 7. AI in Tradespace Tooling (2025+)

Recent research: **AI is being applied to TSE itself** — transformer models generating near-Pareto-optimal architecture candidates (arXiv:2510.03544 for aerospace rendezvous). This is the co-evolution pattern: AI systems **as subject** and **as tool** for SDM methodology.

For product orgs: AI-assisted TSE could surface Pareto-optimal compound AI architectures faster than manual enumeration — but the selection still requires human stakeholder-preference judgment.

---

## 8. Thesis-Scale Research Direction

Build a **public tradespace tool for compound AI system design**:
- Input: stakeholder preference weights, cost/latency/quality benchmarks per architecture
- Process: Pareto frontier computation; flexibility-value estimation (option pricing)
- Output: recommended architectures with sensitivity analysis

This is an SDM-thesis-scope project combining Ross & Hastings TSE, de Weck strategic engineering, and 2026-era AI architecture choices.

---

## 9. Stakeholders

| Stakeholder | Tradespace concern |
|---|---|
| CTO / Architect | Full Pareto frontier analysis |
| CFO | Cost axis dominance |
| CISO | Privacy + lock-in exclusion criteria |
| CPO | Quality + user-perceived attributes |
| Board | Flexibility value under uncertainty |
| Regulator | Compliance axis (EU AI Act eligibility) |

---

## 10. Research Gaps

1. **Public benchmarks for compound-AI architectures** — No accepted way to compare multi-attribute performance across reference architectures
2. **Option-pricing models for AI-specific flexibility** — Traditional Black-Scholes assumptions poor fit for AI-tech curves
3. **Tradespace visualization at scale** — 30k+ candidate architectures exceed typical TSE tool capacity
4. **Stakeholder preference elicitation** — No standard methodology for weighting attributes in AI product orgs
5. **Empirical validation** — Do organizations using TSE + real options for AI decisions actually outperform point-decisions? Unmeasured

---

## 11. Sources

- Ross, A. & Hastings, D. (2005). "The Tradespace Exploration Paradigm." INCOSE International Symposium. https://web.mit.edu/adamross/www/Ross_INCOSE05.pdf
- Ross, A. et al. (2004). "Multi-Attribute Tradespace Exploration as Front End for Effective Space System Design." *Journal of Spacecraft and Rockets.* https://arc.aiaa.org/doi/10.2514/1.9204
- MIT OCW. "Fundamentals of Systems Engineering — Concept Selection and Tradespace Exploration." https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-842-fundamentals-of-systems-engineering-fall-2015/class-videos/session-5-concept-selection-and-tradespace-exploration/
- ResearchGate. "Technology Decisions Under Architectural Uncertainty: Informing Investment Decisions Through Tradespace Exploration." https://www.researchgate.net/publication/262998745_Technology_Decisions_Under_Architectural_Uncertainty_Informing_Investment_Decisions_Through_Tradespace_Exploration
- NASA SBIR 2022-I. "Architecture Decision Modeling & Automated Tradespace Formulation." https://sbir.nasa.gov/SBIR/abstracts/22/sbir/phase1/SBIR-22-1-S17.02-1504.html
- de Weck, O. MIT Strategic Engineering Research Group. http://strategic.mit.edu/deweck.php
- arXiv:2510.03544 (2025). "Agile Tradespace Exploration for Space Rendezvous via Transformers." https://arxiv.org/html/2510.03544
- Systems Engineering Trends. "Tradespace Exploration: Making informed decisions." https://www.se-trends.de/en/tradespace-exploration/
- McKinsey. "The real power of real options." https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-real-power-of-real-options
- ScienceDirect. "Real Options Analysis overview." https://www.sciencedirect.com/topics/economics-econometrics-and-finance/real-options-analysis
- TechTarget. "Build vs. buy AI: A CIO's decision matrix." https://www.techtarget.com/searchcio/feature/Build-vs-buy-AI-A-CIOs-decision-matrix
- Cabin (2026). "Build vs Buy AI." https://cabinco.com/build-vs-buy-ai/
- HP. "Enterprise AI Services: Build vs. Buy Framework." https://www.hp.com/us-en/shop/tech-takes/enterprise-ai-services-build-vs-buy
- Planisware. "Top AI-Powered Strategic Portfolio Management Platforms 2026." https://planisware.com/resources/strategic-planning-alignment/what-top-6-ai-strategic-portfolio-management-platforms
- WEF (2025). "AI redefining investment strategy." https://www.weforum.org/stories/2025/02/ai-redefine-investment-strategy-generate-value-financial-firms/
