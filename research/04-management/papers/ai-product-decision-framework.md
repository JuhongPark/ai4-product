# AI-Augmented Product Decision Framework

> Extending Cooper's AI-PRISM from gate decisions to all critical decision points across the product lifecycle.

---

## Foundation: Cooper's AI-PRISM (2026)

Cooper's AI-PRISM model addresses go/kill decisions at Stage-Gate reviews:
- 7 weighted success factors, 20 sub-factors
- Source Quality Rating Framework weighting evidence by credibility
- Validated through beta testing; positioned as decision **support**, not autonomous decision-maker
- Source: https://www.academia.edu/165246907/Moneyball_for_New_Product_Development_Feb_2026_Cooper

### The Problem AI-PRISM Solves
- ~80% of NPD investment decisions prove wrong
- Traditional intuition-driven go/kill decisions are deeply flawed
- AI-PRISM provides a "rigorous reality check" and "unbiased evaluator" at gate meetings

---

## Extension: Decision Points Across the Full Product Lifecycle

### Decision Point Inventory

| Phase | Decision Point | Stakes | Data Availability | Current Practice |
|-------|---------------|--------|-------------------|-----------------|
| **Discovery** | Which problem to pursue? | Very High | Low (qualitative) | Intuition + limited research |
| **Discovery** | Which customer segment to target? | High | Medium | Survey/interview data |
| **Design** | Which design direction? | Medium | Low (subjective) | Team debate + user testing |
| **Development** | Build vs buy vs partner? | High | Medium | Cost analysis + strategy |
| **Development** | Technical architecture choices? | High | Medium | Engineering judgment |
| **Gate Review** | Go / Kill / Pivot? | Very High | Medium | Stage-Gate scorecard |
| **Testing** | Ship or fix? | High | High (test results) | Quality metrics + judgment |
| **Launch** | When to launch? | Very High | Medium | Market timing + readiness |
| **Launch** | How to price? | High | Medium-High | Market data + strategy |
| **Growth** | Double down or sunset? | Very High | High (usage data) | Metrics + strategic judgment |
| **Growth** | What to build next? | Very High | Medium | Feedback + strategy |

### AI Suitability by Decision Type

Based on the Nature meta-analysis, Stanford selective complementarity research, and empirical evidence:

| Decision Characteristic | AI Role | Human Role |
|------------------------|---------|-----------|
| **Data-rich, pattern-based** | Lead (recommend) | Review and approve |
| **Uncertain, strategic** | Inform (provide data) | Lead (judge and decide) |
| **Creative, aesthetic** | Assist (generate options) | Direct and curate |
| **Ethical, value-laden** | Flag risks | Own the decision |
| **Political, stakeholder** | Not involved | Fully human |

---

## Proposed Framework: AI-Augmented Decision Matrix (AADM)

### For Each Decision Point, Score Three Dimensions:

**1. Data Availability (D)**: How much structured data exists to inform this decision?
- 1 = Almost none (pure intuition)
- 3 = Moderate (some quantitative + qualitative)
- 5 = Rich (extensive metrics, historical data, benchmarks)

**2. Reversibility (R)**: How easily can this decision be reversed?
- 1 = Irreversible (kill a product, major pivot)
- 3 = Costly to reverse (architecture change, pricing change)
- 5 = Easily reversible (feature flag, A/B test variant)

**3. Subjectivity (S)**: How much does the decision depend on subjective judgment?
- 1 = Highly subjective (creative direction, brand fit)
- 3 = Mixed (some data, some judgment)
- 5 = Highly objective (pass/fail test, threshold metric)

### AI Role = f(D, R, S, C) — AADM v2

**v2 Update**: Added Creativity (C) as 4th dimension based on simulation Study S6 findings. v1 misclassified all 17 creative tasks as "AI Absent" because low D + low S triggered the absence rule. The Nature meta-analysis (106 experiments) shows creation is the one task type where Human+AI > either alone. C resolves this.

**4. C (Creativity)** — How much does the task benefit from generative variation?
- 1 = No creative element (pure analysis or judgment)
- 3 = Some creative input helpful (mixed tasks)
- 5 = Primarily creative (design, ideation, content)

| Score Profile | AI Role | Example |
|--------------|---------|---------|
| High D, High R, High S, Low C | **AI Decides** (autonomous) | Automated A/B test routing |
| High D, High S | **AI Recommends** (human approves) | AI-PRISM gate scoring |
| Medium D, Medium S, Low C | **AI Informs** (human decides with data) | Feature prioritization |
| **High C** (any D/S) | **AI Assists** (creative collaboration) | Design variations, copy alternatives |
| Low D, Low R, Low C | **AI Absent** (human leads) | Strategic vision, ethical calls |

**Simulation Validation**:
- v1 P1-P2 consistency: 82.7% → v2: **100%** (17 fixes, 0 regressions)
- Boundary sensitivity: 74% → **59%** (improved)

### Applied to Product Lifecycle

| Decision Point | D | R | S | C | AI Role |
|---------------|---|---|---|---|---------|
| Which problem to pursue? | 2 | 1 | 1 | 1 | AI Absent → Human leads with market data |
| Customer segmentation? | 4 | 4 | 4 | 1 | AI Recommends → LLM clustering + human validation |
| Design direction? | 2 | 3 | 1 | **5** | AI Assists → Generates variations, human curates |
| Build vs buy? | 3 | 2 | 3 | 1 | AI Informs → Cost models, human decides strategy |
| Go / Kill / Pivot? | 3 | 1 | 3 | 1 | AI Recommends → AI-PRISM score + human judgment |
| Ship or fix? | 5 | 4 | 5 | 1 | AI Decides → Automated quality gates |
| When to launch? | 3 | 2 | 2 | 1 | AI Absent → Market signals, human decides timing |
| Pricing? | 4 | 3 | 3 | 1 | AI Recommends → Price optimization + human approval |
| Double down or sunset? | 4 | 1 | 2 | 1 | AI Informs → Usage data + strategic human judgment |
| Marketing copy? | 3 | 4 | 2 | **4** | AI Assists → AI generates, human curates tone/brand |

---

## Integration with Existing Frameworks

### Cooper Stage-Gate + AADM
- AI-PRISM handles the "scoring" dimension of gate reviews
- AADM extends this to determine the AI's role at every decision point, not just gates
- Gate decisions are typically D=3, R=1, S=3 → "AI Recommends" — consistent with Cooper's positioning of AI-PRISM as support tool

### Stanford Selective Complementarity + AADM
- Stanford's "recommend only when human is uncertain" maps to the "AI Recommends" zone
- AADM formalizes when to be in each zone based on measurable characteristics
- The decision tree from selective-complementarity-framework.md provides the micro-level; AADM provides the macro-level

### Parikh Co-Evolutionary Model + AADM
- PM as "orchestrator of socio-technical ecosystems" = PM using AADM to allocate decisions
- The co-evolutionary aspect: as AI improves (D increases), decisions may shift zones over time
- AADM is dynamic, not static — reassess periodically as AI capabilities mature

---

## Validation Status

| Component | Status |
|-----------|--------|
| AI-PRISM (Cooper) | Beta-tested, validated, ready for public use |
| Nature meta-analysis task taxonomy | Empirically validated (106 experiments) |
| Stanford selective complementarity | Experimentally validated (hiring domain) |
| AADM scoring model | **Proposed** — requires empirical validation |
| Full lifecycle application | **Proposed** — no production validation yet |

### Research Needed
1. Empirical validation of D/R/S/C scoring in real product teams
2. Longitudinal study of AADM application across multiple product cycles
3. Cross-industry validation (software vs hardware vs service products)
4. Dynamic reassessment: how quickly should AI roles shift as capabilities improve?

---

## Key Sources

1. Cooper (2026). "Moneyball for NPD." https://www.academia.edu/165246907/Moneyball_for_New_Product_Development_Feb_2026_Cooper
2. Vaccaro et al. (2024). Nature Human Behaviour meta-analysis. https://www.nature.com/articles/s41562-024-02024-1
3. Spiess et al. (2025). Stanford selective complementarity. https://www.gsb.stanford.edu/faculty-research/working-papers/designing-algorithmic-recommendations-achieve-human-ai
4. Parikh (2025). "Agentic AI in PM: Co-Evolutionary Model." https://arxiv.org/abs/2507.01069
5. "Design principles for AI-augmented decision making." EJIS, 2024. https://www.tandfonline.com/doi/full/10.1080/0960085X.2024.2330402
6. "AI and Strategic Decision-Making: Evidence from Entrepreneurs." Strategy Science, 2024. https://pubsonline.informs.org/doi/10.1287/stsc.2024.0190
