# The Research-Market Gap: When "AI Everywhere" Contradicts the Evidence

> Every major tech company optimizes for more AI usage.
> The research says that's often the wrong move.
> This document maps the specific contradictions and their consequences.

---

## The Contradiction

| What the market does | What the research says |
|---------------------|----------------------|
| "Add AI to every feature" | Superficial AI features add complexity without value (ISACA 2025) |
| "AI Copilot for every task" | Automation bias: 47% of users accept incorrect AI outputs (ACM 2025) |
| "AI-generated code is faster" | 87% of Copilot PRs introduce vulnerabilities (Stanford/DryRun); code churn doubled vs pre-AI (GitClear) |
| "Human+AI is always better" | Nature meta-analysis: adding humans to AI decision tasks **hurts** performance |
| "Ship faster with AI" | Uplevel: developers with Copilot had **higher bug rate** with same throughput |
| "HITL solves safety" | Oversight fatigue: 200th approval gets fundamentally different attention than 1st (HackerNoon 2025) |
| "More AI agents = more productivity" | 40%+ of agentic AI projects will be canceled by 2027 (Gartner) |

---

## Five Specific Gaps

### Gap 1: The Automation Bias Problem

**Market assumption**: AI recommendations help humans make better decisions.
**Evidence**: The opposite often happens.

| Finding | Source |
|---------|--------|
| 47% of cybersecurity analysts exhibit automation bias with AI | ACM Digital Threats, 2025 |
| Radiologists' diagnoses worsened by false-positive AI suggestions | PubMed, 2024 |
| Users show "gulf of overreliance" — trusting AI even in high-error domains | CHI 2025 |
| Prolonged AI use correlates with **lower attentional resources and diminished confidence in independent decision-making** | PMC, 2025 |
| Agreement with incorrect AI is **the most consistent behavioral outcome** | Springer AI & Society, 2025 |

**Implication for product teams**: Putting AI recommendations in front of every decision doesn't help — it creates a new failure mode where humans stop thinking critically.

Source: https://dl.acm.org/doi/10.1145/3706598.3714103

### Gap 2: The Code Quality Paradox

**Market assumption**: AI coding tools make developers more productive AND produce better code.
**Evidence**: Faster yes, but quality is contested.

| Metric | AI Impact | Source |
|--------|-----------|--------|
| Development speed | +55% faster | Multiple studies |
| Code functionality | +53% more likely to pass tests | GitHub research |
| Bug rate | **Higher** with Copilot access | Uplevel Data Labs |
| Code churn | **Doubled** vs pre-AI baseline | GitClear 2025 |
| Code cloning | **4x increase** — "copy/paste" exceeds "moved" for first time | GitClear 2025 |
| Security vulnerabilities | **87% of Copilot PRs** introduce vulnerabilities | Stanford/DryRun |
| Delivery stability | **-7.2%** decrease | Industry reports |

**The paradox**: Code is written faster and passes more tests, but it's less maintainable, more duplicated, and more vulnerable. The speed gains create technical debt that isn't measured until later.

Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research

### Gap 3: The Oversight Fatigue Problem

**Market assumption**: Human-in-the-loop (HITL) ensures safety.
**Evidence**: HITL breaks down at scale.

HITL was designed for aviation/nuclear — **low-frequency decisions, high consequences, full context**. Agentic AI inverts all three:

| HITL Design Assumption | Agentic AI Reality |
|----------------------|-------------------|
| Low-frequency decisions | 100+ approvals per hour |
| High consequences per decision | Most are trivial, some are critical — you can't tell which |
| Full context available | Human "approves a conclusion, not a decision process" |

Three failure modes at scale:
1. **Automation bias**: Frictionless interfaces signal that scrutiny is unnecessary
2. **Alert saturation**: 82% of analysts worry about missing threats due to volume
3. **Context collapse**: Only 10/30 SOTA agents provide detailed reasoning traces

**Implication**: Simply adding "human review" doesn't make AI safe. The review degrades to rubber-stamping within hours.

Source: https://hackernoon.com/the-oversight-fatigue-problem-why-hitl-breaks-down-at-scale-and-what-comes-after

### Gap 4: The "AI Adoption J-Curve"

**Market assumption**: AI deployment immediately improves outcomes.
**Evidence**: There's a measurable performance dip first.

Research on US manufacturing firms found AI introduction frequently leads to a **temporary decline in performance** before improvements emerge. Causes:
- Misalignment between digital tools and legacy processes
- Inadequate data infrastructure investment
- Insufficient training
- Workflow redesign not done before AI introduction

**This maps exactly to our Success Pattern #1 (Process Readiness)**: The 95% that fail often fail because they add AI to unready processes, experience the J-curve dip, and abandon before the recovery.

### Gap 5: The Misalignment Problem in Product Design

**Market assumption**: AI can optimize product designs.
**Evidence**: AI optimizes for stated objectives, missing unstated ones.

From Göpfert et al. (2025, arXiv:2506.00047):
- **Design misalignment**: AI interprets objectives literally; latent requirements "that seem obvious to humans" are ignored
- **Narrow context**: AI designs without considering "complex societal, economic, and environmental interdependencies"
- **Excessive agency**: Autonomous systems may perform harmful actions through reward-hacking

**This is exactly what happened in our Design Fiction Scenario Card #1** (Brand Violation): AI redesigned the hero section, metrics looked good, but brand coherence was violated because it wasn't an explicit objective.

---

## The Root Cause: Misaligned Incentives

| Actor | Incentive | Result |
|-------|-----------|--------|
| **AI tool vendors** | Maximize usage/seats/API calls | Push AI into every workflow, never say "don't use AI" |
| **AI model providers** | Maximize API revenue | Make models seem capable of everything |
| **VCs** | Show hypergrowth | Fund "AI for X" regardless of evidence |
| **Enterprise buyers** | Fear of being left behind | Buy AI tools before understanding where they help |
| **Product teams** | Ship faster, look innovative | Use AI because everyone else does, not because evidence supports it |

**Nobody in this system has an incentive to say "stop using AI here."**

Except researchers. And the MIT/Nature/Stanford evidence is clear: **selective use outperforms universal use.**

---

## What "Selective Complementarity" Would Look Like in Practice

If the market adopted research findings, products would look different:

| Current Approach | Evidence-Based Approach |
|-----------------|----------------------|
| AI Copilot in every IDE | AI coding only for boilerplate/tests; human for architecture/design |
| AI suggests on every decision | AI suggests only when human is likely uncertain (Stanford) |
| AI reviews all PRs | AI reviews routine PRs; senior human reviews critical paths |
| AI writes all docs | AI drafts; human adds context and "why" (Knowledge Drain prevention) |
| AI handles all customer inquiries | AI handles routine; human handles complex/emotional (Klarna lesson) |
| AI scores every gate decision | AI provides data; human makes go/kill call (Cooper AI-PRISM) |

---

## Research Agenda: Studying the Gap

### Immediate Studies (feasible now)

1. **Automation Bias in Product Teams**: Do PMs show the same 47% automation bias with AI recommendations that cybersecurity analysts do? (replicate ACM study in product context)

2. **Code Quality Longitudinal Study**: Track a team's code quality metrics (churn, bugs, vulnerabilities) before and 6 months after AI coding tool adoption. Does the J-curve apply?

3. **Oversight Fatigue in AI-Assisted Reviews**: Give PM teams 50 AI recommendations per day for 2 weeks. Measure approval time and accuracy over time. When does rubber-stamping begin?

### Longer-Term Studies

4. **Selective vs Universal AI Adoption**: Compare teams using AI for everything vs teams using AI only where our framework recommends. Measure: shipping speed, quality, team satisfaction.

5. **"AI Abstinence" Experiments**: What happens when a team that's been using AI for 6 months stops using it for specific task types? Do they perform better or worse?

---

## Key Sources

1. "Automation Bias in AI-Decision Support." ACM, 2024. https://pubmed.ncbi.nlm.nih.gov/39234734/
2. "To Use or Not to Use: Overreliance on Generative AI." CHI 2025. https://dl.acm.org/doi/10.1145/3706598.3714103
3. "The Oversight Fatigue Problem." HackerNoon, 2025. https://hackernoon.com/the-oversight-fatigue-problem-why-hitl-breaks-down-at-scale-and-what-comes-after
4. GitClear (2025). "AI Code Quality: 4x Growth in Code Clones." https://www.gitclear.com/ai_assistant_code_quality_2025_research
5. Göpfert et al. (2025). "Risks of AI-driven product development." arXiv:2506.00047. https://arxiv.org/html/2506.00047v1
6. "Exploring automation bias in human-AI collaboration." Springer AI & Society, 2025. https://link.springer.com/article/10.1007/s00146-025-02422-7
7. "The Cognitive Cost of AI." PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12367725/
8. "Measuring and mitigating overreliance." arXiv, 2025. https://arxiv.org/html/2509.08010v1
