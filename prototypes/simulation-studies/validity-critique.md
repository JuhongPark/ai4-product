# Validity Critique: AADM v2 Simulation Results

> Self-audit identifying methodological flaws in the v2 evaluation.
> Date: 2026-04-11

---

## The Problem: Circular Validation in Study S6 v2

### What We Claimed
P1-P2 consistency improved from 82.7% to 100% with the addition of the C (Creativity) dimension.

### What Actually Happened

```
P1 classified task as "creation"
  → S6 test code assigned C=5 (because we KNOW it's a creation task)
    → AADM v2 returns "AI Assists" (because C≥4 triggers this rule)
      → P1's "Human+AI collaboration" is compatible with "AI Assists"
        → 100% consistency
```

**This is circular.** We used the P1 classification (the thing we're testing consistency against) to derive the C score (the input to P2). The "consistency" is a tautology — it's logically guaranteed to be 100% because the answer is encoded in the input.

### Why This Is Wrong

In real use, a human PM would score C independently. They might score a task as:
- "Design onboarding flow" → C=5 (obviously creative) — easy case
- "Write microcopy for error states" → C=3? C=4? (debatable)
- "Define brand voice guidelines" → C=4? C=2? (is this creative or strategic?)

The test assumed perfect C scoring. Real humans will disagree on C, especially for ambiguous tasks.

---

## What IS Valid in the v2 Results

| Claim | Status | Reasoning |
|-------|--------|-----------|
| C dimension resolves the conceptual conflict between P1 and P2 | **VALID** | The logic is sound: low D + low S can be either strategic (C=1) or creative (C=5), and these need different AI roles |
| 100% P1-P2 consistency | **INVALID** | Circular — C was derived from the thing being tested |
| Boundary sensitivity improved (74% → 59%) | **PARTIALLY VALID** | The 625-space mapping is structurally correct, but 59% may be misleadingly low because C adds a dimension that spreads points out |
| Face validity (4/5 spot checks pass) | **VALID** | Spot checks used independent reasoning, not circular assignment |
| Nature meta-analysis supports C dimension | **VALID** | Creation is empirically the one task type where Human+AI > either alone |

---

## Honest Assessment of What We Know and Don't Know

### We Know (Structurally Valid)
1. v1 has a real conflict: creation tasks get misclassified as AI Absent
2. A Creativity dimension is the correct conceptual fix (Nature evidence)
3. The v2 scoring logic produces correct results when C is scored correctly

### We Don't Know (Requires Empirical Testing)
1. **Can humans reliably score C?** (inter-rater reliability for C)
2. **Does C add signal or just noise?** (incremental validity over D/R/S)
3. **Is C independent of D and S?** (discriminant validity — C might correlate strongly with low S)
4. **Does 4 dimensions overwhelm users?** (cognitive load vs 3 dimensions)

---

## Proper Validation Design

### Test 1: C Independence Check

**Question**: Is C just a proxy for "low S"?

**Method**: Score 100 tasks on all 4 dimensions. Compute:
- Correlation between C and (5-S) — if r > 0.8, C is redundant
- Cases where C and S are independent (e.g., high C + high S: "optimize the AI-generated design system" is both creative and objective)

**Threshold**: If C correlates with (5-S) at r > 0.7, the dimension may not add genuine information.

### Test 2: C Inter-Rater Reliability

**Question**: Do different PMs agree on C scores?

**Method**: 5 PMs independently score C for 30 scenarios. Compute ICC(2,1).

**Threshold**: ICC > 0.6 for C to be usable. If ICC < 0.5, the dimension is too subjective to be reliable.

### Test 3: Incremental Validity

**Question**: Does adding C actually improve role accuracy over D/R/S alone?

**Method**: 
- Expert panel assigns "correct" AI role for 30 scenarios
- Compare: D/R/S agreement with expert vs D/R/S/C agreement with expert
- Statistical test: McNemar's test for paired proportions

**Threshold**: Statistically significant improvement (p < 0.05) on at least the creative-task subset.

### Test 4: Non-Circular P1-P2 Consistency

**Question**: When C is scored by humans (not derived from P1), what is the real consistency rate?

**Method**:
- P1 classifies 100 tasks (task type + allocation)
- Independently, 3 PMs score D/R/S/C for the same 100 tasks
- P2 computes role from the PM-scored D/R/S/C
- Measure: P1-P2 consistency using human-scored C

**Expected**: Real consistency will be somewhere between v1 (82.7%) and our circular v2 (100%). If it's above 90%, the C dimension genuinely helps.

---

## Revised Claims

### What We Can Honestly Say Now

> "AADM v2 adds a Creativity (C) dimension that **conceptually resolves** the creation-task conflict identified in v1. The Nature meta-analysis provides empirical justification for distinguishing creative from non-creative tasks. Structural analysis shows the scoring logic produces correct results when C is scored correctly. **However, the 100% consistency claim is methodologically circular and requires independent validation with human-scored C values.** The actual improvement over v1 is an open empirical question."

### What We Incorrectly Claimed

> ~~"P1-P2 consistency improved from 82.7% to 100% with 0 regressions."~~

This should be: "P1-P2 consistency improved from 82.7% to 100% **under the assumption of perfect C scoring**, which is unrealistic. Real improvement requires empirical measurement."
