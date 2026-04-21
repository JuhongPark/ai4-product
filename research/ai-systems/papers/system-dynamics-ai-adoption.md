# System Dynamics of AI Adoption: Causal Loops and the Productivity Paradox

> **Date:** 2026-04-21
> **SDM lens:** System dynamics (Forrester, Sterman — MIT Sloan); causal loop diagrams (CLDs); simulation modeling

---

## 1. Thesis

The empirical record on AI productivity (see [metr-productivity-paradox.md](../../productization-skills/papers/metr-productivity-paradox.md)) is a **paradox at the individual level but not at the system level**. Applying Jay Forrester's **system dynamics** method — **causal loop diagrams** (CLDs) and **stock-and-flow simulation** — makes the paradox tractable: the reinforcing and balancing loops are identifiable, and the non-intuitive dynamics (initial gain → later backfire) are predictable.

---

## 2. Method Primer

**System dynamics** (SD) was developed by **Jay Forrester** at MIT in the 1950s and elaborated by **John Sterman** (MIT Sloan) in *Business Dynamics* (2000). Core constructs:

- **Stocks** — accumulations (e.g., codebase size, bug count, team skill)
- **Flows** — rates of change (e.g., code commits per day, bug introduction rate)
- **Causal loops** — reinforcing (R) or balancing (B) feedback structures
- **Delays** — time lags that produce overshoot/oscillation
- **Nonlinearities** — tipping points where behavior reverses

SD's strength vs. traditional analysis: **it makes dynamics visible**. Static comparisons (AI = X% faster) hide the trajectory.

---

## 3. CLD: AI Productivity Paradox for Software Development

```
                   (+)
    AI Tool Use ─────────► Code Volume
       ▲    │                    │
       │    │                    ▼
       │    │            Quality Debt (bugs, clones, drift)
       │    │                    │
       │    │            (delay)  │
       │    │                    ▼
       │   (R1)          Rework Burden
       │                          │
       │                          ▼
       │                   Effective Throughput
       │                          │
       └──── Confidence ◄─────────┘
                 (perception
                  outpaces reality)
```

### Loop identification

- **R1 (Reinforcing, fast)**: AI use → more code → appears productive → more confidence → more AI use
- **B1 (Balancing, slow)**: More code → quality debt accumulates → rework burden rises → effective throughput falls
- **Perception gap**: Confidence updates fast, rework cost updates slowly (delay)

The **METR paradox** (24% forecast, 19% actual slower, 20% perceived) **falls out naturally** from this structure: the fast R1 loop dominates perception; the slow B1 loop dominates actual throughput; developers perceive via R1, the measurement catches B1.

### Analogous loops in other skill domains

Applying the same structure elsewhere (see [research/sales-skills/](../../sales-skills/)):

| Domain | R1 (fast gain) | B1 (slow backfire) | Delay driver |
|---|---|---|---|
| AI SDR | AI outreach → more touches | Prospect fatigue → reply rates drop | Aggregate market response time |
| AI pricing | Personalized prices → revenue lift | Fairness perception → customer backlash | Media/regulator cycle |
| AI IR | AI-personalized investor contact → engagement | Reg FD risk → compliance event | Enforcement cycle |
| AI vibe coding | Fast prototype shipping → growth | Hidden security debt → breach | Attacker discovery time |

The pattern is **general**: fast reinforcing gains, delayed balancing backfires. SDM's value is recognizing the pattern and **designing the architecture to dampen B1** (e.g., embedded quality gates, fairness monitoring, compliance automation).

---

## 4. Bass Diffusion for AI Adoption

**Bass diffusion model** (1969, formalized within SD) decomposes adoption into:

- **External influence** (advertising, announcements) → **Innovators**
- **Internal influence** (word-of-mouth) → **Imitators**

For 2025–2026 AI tool adoption (Copilot, Claude Code, v0, Cursor), the observed trajectory fits Bass well:
- Early innovators (2023): 20–30% of developers
- Imitator phase (2024–2025): 45 → 72% daily AI tool usage (accelerating)
- Saturation phase (2026+): approaching 80–90% usage

### Counter-adoption: reversal cases
Klarna's 2024–2025 reversal (full AI customer service → rehired humans) is a **counter-flow** — rarely modeled in Bass but critical for system dynamics. SDM analysis would model:

- Stock: Customers satisfied vs. dissatisfied
- Flow: Satisfaction-to-dissatisfaction flow accelerated by AI poor handling
- Delay: Customer perception-to-public-reputation delay
- Tipping: When dissatisfaction flow exceeds satisfaction flow → reversal decision

Klarna is not a story of bad technology; it is a **system-dynamics story of tipping-point misjudgment**.

---

## 5. LLM-Assisted SD Modeling (2024–2025)

Recent SD research explores LLMs for model construction:

- Hosseinichimeh et al. (2024). "From text to map: a system dynamics bot for constructing causal loop diagrams." *System Dynamics Review.* https://onlinelibrary.wiley.com/doi/full/10.1002/sdr.1782
- arXiv:2402.11400 "A System Dynamics Bot for Constructing CLDs." https://arxiv.org/pdf/2402.11400
- System Dynamics Society 2025 Conference: "Integrating AI Techniques into SD." https://proceedings.systemdynamics.org/2025/papers/O1111.pdf

This is the symbol of co-evolution: **AI is both** a subject of SD analysis and a tool for accelerating SD modeling.

---

## 6. Canonical MIT Reference: Sterman's *Business Dynamics*

Sterman, J. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World.* McGraw-Hill / Irwin. Classroom-used at MIT Sloan; definitive reference for SD methodology.

Applicable chapters for AI systems:
- Ch. 10 — "Path Dependence and Positive Feedback" — for AI adoption dynamics
- Ch. 15 — "Delays and Overshoot" — for METR-style perception/reality gap
- Ch. 19 — "Policy Design and Evaluation" — for governance architecture

---

## 7. From CLD to Policy Design

SD's normative contribution: once loops are mapped, you can **design counter-measures**:

| System behavior | Counter-measure (policy design) |
|---|---|
| R1 dominates perception | Explicit B1-tracking metrics (technical debt dashboards) |
| Delay in B1 | Early-warning leading indicators (code clone rate, security scan frequency) |
| Tipping-point risk | Shadow-mode deployment (see [AI SRE paper](../../productization-skills/papers/ai-sre-incident-response.md)) |
| Asymmetric information | Third-party audit / independent measurement (METR as exemplar) |

This maps directly onto the **successful-5% patterns** (repo's [successful-5-percent-patterns.md](../../cross-cutting/papers/successful-5-percent-patterns.md)) — the 7 patterns are themselves SD policies.

---

## 8. Thesis-Scale Research Question

**Build an executable Vensim/Stella model of the AI developer productivity paradox**, calibrate to METR 2025 + 2026 data + vendor-reported data, and test whether policies (e.g., mandatory code review gates, static analysis thresholds) dampen the paradox.

Deliverable: An SDM thesis centered on SD modeling of AI productivity in engineering orgs — with explicit validation against METR panel data.

---

## 9. Stakeholders

| Stakeholder | CLD concern |
|---|---|
| Executives | R1/B1 misread → strategic error |
| Engineering leads | Delay in B1 → under-investment in debt paydown |
| Data teams | Measurement architecture for leading indicators |
| Risk / compliance | Tipping-point monitoring for reversal trigger |
| Investors | External-signal noise (hype-cycle B2/R2 loops) |

---

## 10. Research Gaps

1. **Empirical calibration** — Most published CLDs are qualitative; quantitative calibration to real AI data is rare
2. **LLM-generated SD models** — Validity not established; generated models need human validation
3. **AI-adoption Bass parameters** — Innovation coefficient *p* and imitation coefficient *q* for AI tools not systematically estimated
4. **Reversal-case taxonomy** — Klarna is one case; systematic collection of AI adoption reversals underexplored

---

## 11. Sources

- Forrester, J. (1961). *Industrial Dynamics.* MIT Press.
- Sterman, J. (2000). *Business Dynamics.* https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/SystemDynamics.JohnSterman2001.pdf
- Kirkwood (1998). "System Dynamics Methods: A Quick Introduction." https://nutritionmodels.com/papers/Kirkwood1998.pdf
- Hosseinichimeh et al. (2024). *System Dynamics Review.* https://onlinelibrary.wiley.com/doi/full/10.1002/sdr.1782
- arXiv:2402.11400 (2024). "A System Dynamics Bot for Constructing CLDs." https://arxiv.org/pdf/2402.11400
- System Dynamics 2025 proceedings. "Integrating AI into SD." https://proceedings.systemdynamics.org/2025/papers/O1111.pdf
- Springer (2020). "System Dynamics Approach for Adoption of AI in Finance." https://link.springer.com/chapter/10.1007/978-981-15-8025-3_54
- Sustainability Methods. "System Thinking & Causal Loop Diagrams." https://sustainabilitymethods.org/index.php/System_Thinking_&_Causal_Loop_Diagrams
