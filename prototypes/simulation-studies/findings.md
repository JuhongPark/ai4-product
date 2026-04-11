# Simulation Study Findings

> Results from 4 automated studies (S1, S3, S4, S6) and implications for framework refinement.
> Date: 2026-04-11

---

## Study 1: AADM Boundary Mapping

### Key Results

| Role | Volume (of 125) | Share |
|------|-----------------|-------|
| AI Decides | 8 | 6.4% |
| AI Recommends | 22 | 17.6% |
| AI Informs | 33 | 26.4% |
| AI Assists | 30 | 24.0% |
| AI Absent | 32 | 25.6% |

- **74% of all D/R/S combinations are on a boundary** — a ±1 change would switch the role
- Role distribution is reasonably balanced (no single role dominates)
- AI Decides is appropriately rare (6.4%) — only high D + high R + high S

### Implications

1. **High boundary density (74%) is a critical finding.** It means the scoring system is sensitive to input. This is both a feature (discriminates well) and a risk (small disagreements in scoring → different recommendations).
2. **Inter-rater reliability study is absolutely essential** — if raters disagree by even ±1 on any dimension, 74% of the time the recommendation could change.
3. **Consider**: Move to continuous (0-10) scoring to reduce boundary jumps, or add "confidence zones" where the tool says "this is a borderline case, consider both roles."

---

## Study 3: Leave-Phase-Out Cross-Validation

### Key Results

| Phase | Accuracy | Keyword Coverage |
|-------|----------|-----------------|
| Design | 81.2% | 81% |
| Development | 83.3% | 72% |
| Growth | 70.6% | 82% |
| Testing | 78.6% | 21% |
| Discovery | 56.2% | 50% |
| Launch | 35.3% | 29% |

- **Average CV accuracy: 67.5%** — virtually identical to full-data (67.3%)
- **Generalization gap: -0.2%** — essentially zero
- **But**: Launch (35%) and Discovery (56%) are significantly weak

### Implications

1. **Zero generalization gap is surprising and good** — the classifier doesn't overfit to any phase. Keywords are generalizable across contexts.
2. **Launch phase failure (35%, 29% keyword coverage) is structural**, not a generalization issue. Launch tasks use strategic language ("decide," "market," "timing") that overlaps with "decision_uncertain" but not distinctively.
3. **Testing has only 21% keyword coverage but 78.6% accuracy** — the phase default ("execution") is doing the heavy lifting. This means Testing tasks are predictably typed even without keywords.
4. **Practical fix**: For Launch phase, either (a) add phase-specific keywords, (b) use LLM classification, or (c) default to "Human-led, AI-informed" for Launch (which would be correct ~60% of the time).

---

## Study 4: Bootstrap Perturbation Analysis

### Key Results

| Metric | Value | Assessment |
|--------|-------|-----------|
| Rank preservation | **47.0%** | LOW — rank is unstable under ±1 perturbation |
| Klarna stays "Not Ready" | **46.8%** | LOW — classification unstable |
| PostNL stays "Highly Ready" | **89.8%** | HIGH — top case is robust |

- **No individual pattern removal changes the rank order** — all 7 patterns are stable
- The instability comes from **accumulation of small perturbations** across multiple patterns

### Implications

1. **47% rank preservation is concerning.** It means that if raters disagree by ±1 on a few patterns, the rank ordering of cases changes more than half the time.
2. **However**: PostNL (89.8% "Highly Ready") and the gap between top and bottom cases is robust. The instability is mainly in the **middle of the distribution** (Devin, EY.ai, OpenTable — all within a few points of each other).
3. **Klarna at 46.8% "Not Ready"** means it sometimes gets pushed to "Partially Ready" with +1 perturbations. This suggests the Not Ready threshold (0-14) should potentially be raised to 0-16 for more robustness.
4. **All patterns contribute equally** — no single pattern is more important than others for maintaining rank order. The checklist is well-balanced but needs wider scoring ranges to be discriminating.

### Recommended Fix
- Consider **weighted patterns** — if HITL, Narrow/Deep, and Back-Office are most predictive (from case analysis), weight them higher (e.g., 1.5x)
- Alternatively, use 1-7 or 1-10 scale instead of 1-5 to increase spread

---

## Study 6: Cross-Prototype Consistency

### Key Results

| Metric | Value |
|--------|-------|
| P1-P2 consistency rate | **82.7%** (81/98) |
| Inconsistencies | 17 tasks |
| Pattern of inconsistency | All 17 are "creation" tasks mapped to D=2, R=3, S=1 |

- P1 says "Human+AI collaboration" for creation tasks
- P2 maps D=2, S=1 to "AI Absent" (because D≤2 and S≤2 triggers Absent rule)
- **This is a systematic clash between the two tools**

### Root Cause

The disagreement reveals a real conceptual tension:
- **P1 (Selective Complementarity)**: Creation tasks benefit from Human+AI collaboration (Nature meta-analysis evidence)
- **P2 (AADM)**: Low Data + Low Subjectivity = AI Absent (the rule prioritizes human judgment when data and objectivity are low)

The issue: **creativity is low-data and low-objectivity (correctly scored) but high-value for AI collaboration (correctly identified by P1)**. AADM's D/R/S model can't distinguish "low data because it doesn't exist" from "low data because the task is creative."

### Recommended Fix

Add a 4th dimension to AADM: **C (Creativity)** — how much does the task benefit from generative variation?

| Profile | AI Role |
|---------|---------|
| Low D, Low S, **High C** | AI Assists (generate variations) |
| Low D, Low S, **Low C** | AI Absent (pure human judgment) |

This would resolve the P1-P2 conflict and better model the Nature meta-analysis finding that creation is the one task type where Human+AI consistently outperforms.

---

## Cross-Study Synthesis

### Framework Modifications Needed

| Priority | Modification | Source Study | Impact |
|----------|-------------|-------------|--------|
| **1** | Add Creativity (C) dimension to AADM | S6 | Resolves P1-P2 conflict for creation tasks |
| **2** | Add "borderline" indicator when near role boundary | S1 | Addresses 74% boundary density |
| **3** | Raise Not Ready threshold or weight predictive patterns | S4 | Improves discrimination in middle of distribution |
| **4** | Add phase-specific keywords or LLM fallback for Launch | S3 | Fixes worst-performing phase (35%) |
| **5** | Consider continuous (1-10) scoring for AADM | S1 + S4 | Reduces boundary effects and perturbation sensitivity |

### What Simulations Validated

- AADM role distribution is balanced and covers all 5 roles appropriately (S1)
- P1 classifier generalizes well across phases (zero overfit) (S3)
- P4 checklist is robust at extremes (PostNL: 89.8% stable) (S4)
- P1-P2 pipeline is 82.7% consistent — usable but needs improvement (S6)

### What Simulations Revealed Needs Fixing

- AADM is too sensitive to ±1 scoring changes (S1: 74% boundary density)
- P4 rank order is unstable in the middle of the distribution (S4: 47% rank preservation)
- P1-P2 clash on creative tasks reveals a missing dimension (S6: all 17 inconsistencies are creation)
- P1 Launch phase needs dedicated attention (S3: 35% accuracy, 29% keyword coverage)
