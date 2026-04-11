# Empirical Simulation Study Plan

> Rigorous simulation methods to validate prototypes before human participant studies.
> Each study has explicit hypotheses, methods, analyses, and validity threats.
> Date: 2026-04-11

---

## Methodological Rationale

Three simulation approaches, each with known strengths and limitations:

| Method | Strength | Limitation | Mitigation |
|--------|----------|-----------|------------|
| **Monte Carlo Analysis** | Systematic, exhaustive, reproducible | No human judgment involved | Used for structural analysis, not behavioral claims |
| **LLM-Simulated Personas** | Scalable, persona-conditioned | Captures trends but not effect magnitudes (NN/g 2025) | Use for hypothesis generation, not final validation |
| **Case-Based Bootstrapping** | Grounded in real outcomes | Small sample (n=6) | Bootstrap 1,000x; report confidence intervals |

**Key principle**: These simulations generate **hypotheses and structural insights**, not final conclusions. Human participant studies remain necessary for validation. Each study explicitly marks what it can and cannot claim.

---

## Study 1: AADM Boundary Mapping (Monte Carlo)

### Hypothesis
> H1: The AADM scoring model produces a stable, interpretable mapping from D/R/S scores to AI roles, with identifiable "decision boundaries" where small score changes cause role transitions.

### Method

**Full combinatorial analysis**: Score all 125 possible D/R/S combinations (5³).

```python
# Pseudocode
for d in range(1, 6):
    for r in range(1, 6):
        for s in range(1, 6):
            role = score_to_role(d, r, s)
            record(d, r, s, role)
```

**Analyses**:
1. **Role volume**: How much of the 5³ space does each role occupy?
2. **Boundary map**: Which D/R/S combinations are exactly on a boundary (±1 changes role)?
3. **Dimension influence**: Hold two dimensions constant, vary the third — which dimension changes the role most often?
4. **Cluster analysis**: Are roles contiguous in D/R/S space or fragmented?

### Expected Outputs
- 3D heatmap of AI roles across D/R/S space
- Boundary surface visualization
- Dimension influence ranking (S > D > R expected)
- "Ambiguity zones" where role assignment is unstable

### What This Can Claim
- Structural properties of the scoring algorithm
- Which score regions need clearer anchoring for human raters

### What This Cannot Claim
- Whether humans agree with these role assignments
- Whether following recommendations improves outcomes

---

## Study 2: Simulated Inter-Rater Reliability (LLM Personas)

### Hypothesis
> H2: LLM personas conditioned on different PM experience profiles will produce D/R/S scores with moderate agreement (simulated ICC 0.5-0.7), and disagreement will be highest on the S dimension.

### Method

**5 LLM Personas** (based on real PM archetypes from our research):

| Persona | Profile | Expected Bias |
|---------|---------|---------------|
| **Alex** | Senior PM, 10yr experience, data-driven, ex-Google | Higher D scores (trusts data more) |
| **Sam** | Junior PM, 2yr experience, design background | Lower S scores (sees more subjectivity) |
| **Jordan** | Engineering manager turned PM, systems thinker | Higher R scores (thinks in reversibility) |
| **Morgan** | Product strategist, MBA, McKinsey background | Lower R scores (sees bigger stakes) |
| **Riley** | UX researcher turned PM, user-centered | Lower D scores (skeptical of quantitative data alone) |

**Procedure**:
Each persona scores all 30 AADM scenarios. LLM prompt:

```
You are [Persona name], a product manager with [profile details].
You tend to [expected bias].

Score this product decision on three dimensions (1-5):
- D (Data Availability): 1=pure intuition → 5=rich metrics
- R (Reversibility): 1=irreversible → 5=easily reversed  
- S (Subjectivity): 1=highly subjective → 5=highly objective

Decision: "[scenario text]"
Context: [phase]

Respond with JSON: {"D": X, "R": X, "S": X, "reasoning": "..."}
```

**Analyses**:
1. **ICC(2,1)** per dimension across 5 personas × 30 scenarios
2. **Krippendorff's alpha** for ordinal data
3. **Per-scenario disagreement**: Which scenarios produce most variance?
4. **Per-dimension disagreement**: D vs R vs S
5. **Persona clustering**: Do personas with similar backgrounds agree more?
6. **Role agreement**: Even when D/R/S differ, do personas land on the same role?

### Validity Considerations

| Threat | Mitigation |
|--------|-----------|
| LLM personas may be more consistent than real humans | Report as upper bound; real ICC likely lower |
| LLM may not capture true PM reasoning diversity | Use diverse persona descriptions; compare to NN/g synthetic research parity scores (85-92%) |
| Central tendency bias in LLMs | Explicitly instruct personas to use full 1-5 range |
| LLM cannot disagree in truly surprising ways | Note this limitation; human study still needed |

### What This Can Claim
- Which scenarios are structurally ambiguous (high variance even for simulated raters)
- Which dimension is most subjective (likely S, ironically)
- Hypothesis about expected ICC range for human study

### What This Cannot Claim
- Actual inter-rater reliability of human PMs
- Whether persona biases reflect real PM biases

---

## Study 3: Classifier Cross-Validation (Leave-Phase-Out)

### Hypothesis
> H3: The rule-based classifier's accuracy drops significantly when tested on held-out phases, indicating phase-specific keyword patterns that don't generalize.

### Method

**Leave-one-phase-out cross-validation**:
- Train keyword weights on 5 phases, test on the 6th
- Repeat for each phase
- Compare to full-dataset accuracy (67.3%)

**Confusion matrix analysis**:
- For each held-out phase, generate confusion matrix
- Identify systematic misclassification patterns
- Quantify per-phase generalization gap

**Keyword coverage analysis**:
- For each phase, what percentage of benchmark tasks contain at least one keyword for the correct type?
- Identify "keyword deserts" — tasks with zero keyword matches

### Expected Outputs
- Per-phase generalization accuracy
- Keyword coverage rates per phase × type
- Recommended keyword expansions for low-coverage areas
- Estimated LLM improvement potential (keyword-missed tasks)

---

## Study 4: P4 Pattern Scoring Bootstrap Analysis

### Hypothesis
> H4: The monotonic relationship between total pattern score and AI adoption success is robust to perturbation of individual pattern scores within ±1.

### Method

**Bootstrap with perturbation** (1,000 iterations):

```
For each iteration:
  For each of 6 cases:
    For each of 7 patterns:
      Perturb score by uniform random ±1 (clamped to 1-5)
    Compute total score
  Check: Is the rank order of cases preserved?
  Check: Is Klarna still in "Not Ready" zone?
  Check: Is PostNL still in "Highly Ready" zone?
```

**Sensitivity analysis per pattern**:
- Remove each pattern one at a time
- Recompute total scores and rank order
- Which pattern removal most disrupts the correct ranking?

**Threshold sensitivity**:
- Vary the readiness level boundaries (e.g., Not Ready: 0-14 → 0-12 or 0-16)
- At what thresholds does misclassification occur?

### Expected Outputs
- Rank preservation rate across 1,000 bootstrap iterations
- Pattern importance ranking (by rank disruption when removed)
- Robust threshold ranges for each readiness level
- Confidence intervals for each case's readiness classification

### What This Can Claim
- Whether the scoring model is robust to scoring noise
- Which patterns contribute most to discriminative power
- Safe threshold ranges for readiness levels

### What This Cannot Claim
- Whether the 7 patterns are the right patterns (content validity)
- Whether the patterns generalize beyond these 6 cases

---

## Study 5: Synthetic Workshop Simulation (LLM Roleplay)

### Hypothesis
> H5: LLM-simulated workshop participants, conditioned on PM/Designer/Engineer personas, will discover at least 60% of the predicted requirements (R1-R8) and generate novel insights not in our predictions.

### Method

**Simulate P3 Workshop Protocol**:

Three simulated sessions with LLM personas:

| Session | Personas (3 per session) | Scenario Card |
|---------|------------------------|---------------|
| S1: PM Workshop | Senior PM, Junior PM, Product Strategist | Card 4: Strategy Drift |
| S2: Designer Workshop | UX Designer, Visual Designer, Design Lead | Card 1: Brand Violation |
| S3: Mixed Workshop | PM + Designer + Engineer | Card 7: Governance Vacuum |

**Per session, simulate the 4-part protocol**:

Part 1: Present scenario, ask personas to extend it (what happened next?)
Part 2: Ask each persona to create an artifact using one template
Part 3: Cross-examine artifacts — what requirements/risks emerge?
Part 4: Rate each discovery on "Would traditional methods find this?"

**Analyses**:
1. **Recall vs predictions**: How many of R1-R8 and K1-K6 were discovered?
2. **Novel discoveries**: Insights not in our prediction list (true exploratory value)
3. **Role differences**: Do PM/Designer/Engineer personas discover different things?
4. **Novelty ratings**: Simulated "Would traditional methods find this?" scores
5. **Artifact quality**: Are the generated post-mortems/policies actionable?

### Validity Considerations

| Threat | Mitigation |
|--------|-----------|
| LLMs may reproduce our own framework thinking | Use personas with no knowledge of our frameworks |
| LLMs may not generate truly surprising insights | Explicitly prompt for contrarian/unexpected perspectives |
| Single LLM may produce homogeneous responses | Use different temperature settings; compare across sessions |
| Workshop dynamics (negotiation, conflict) can't be simulated | Note this as fundamental limitation; mark insights as "solo reasoning, not group dynamics" |

### What This Can Claim
- Lower-bound estimate of workshop discovery potential
- Whether scenario cards surface the intended framework gaps
- Whether role-specific perspectives lead to different discoveries

### What This Cannot Claim
- What real humans would discover (group dynamics, emotion, surprise)
- Whether the method is "better" than traditional methods
- Novelty ratings (LLMs can't assess their own novelty vs human methods)

---

## Study 6: Integrated Cross-Prototype Stress Test

### Hypothesis
> H6: When a task is classified by P1 and the resulting decision is scored by P2, the combined recommendation is consistent and the tools don't produce contradictory guidance.

### Method

**Pipeline test** (100 benchmark tasks):
```
For each task:
  1. P1 classifies task → type + allocation
  2. Construct a decision scenario: "Should we follow P1's allocation?"
  3. Score that meta-decision in P2 (estimate D/R/S)
  4. Check: Does P2's role recommendation align with P1's allocation?
  5. Run P4 checklist on a hypothetical team following P1+P2
  6. Check: Would P4 flag any pattern violations?
```

**Contradiction analysis**:
- Cases where P1 says "AI-led" but P2 says "AI Absent" for the meta-decision
- Cases where P1 says "Human only" but P4's back-office pattern suggests AI
- Quantify consistency rate across the full pipeline

---

## Implementation Plan

### Phase 1: Automated Studies (can run now)

| Study | Compute | Time | Dependencies |
|-------|---------|------|-------------|
| **S1: AADM Boundary Mapping** | Python script | 1 hour | None |
| **S3: Leave-Phase-Out CV** | Python script | 1 hour | P1 evaluate.py |
| **S4: Bootstrap Analysis** | Python script | 1 hour | P4 case data |
| **S6: Cross-Prototype Stress Test** | Python script | 2 hours | P1 + P2 |

### Phase 2: LLM Simulation Studies (requires API)

| Study | Compute | Time | Dependencies |
|-------|---------|------|-------------|
| **S2: Simulated Inter-Rater** | LLM API (~150 calls) | 3 hours | ANTHROPIC_API_KEY |
| **S5: Synthetic Workshop** | LLM API (~50 calls) | 4 hours | ANTHROPIC_API_KEY |

### Phase 3: Analysis and Reporting

| Activity | Time |
|----------|------|
| Generate visualizations (heatmaps, confusion matrices) | 2 hours |
| Write integrated findings report | 3 hours |
| Identify modifications to prototypes based on findings | 2 hours |
| Update prototyping-research-plan.md with simulation results | 1 hour |

---

## Success Criteria

| Study | Minimum Threshold | Stretch Goal |
|-------|------------------|-------------|
| S1 | All 5 roles occupied; boundaries interpretable | Clean contiguous role regions |
| S2 | Simulated ICC > 0.5 on D and R dimensions | ICC > 0.7 on all dimensions |
| S3 | Cross-validation accuracy > 50% | > 60% (near full-data performance) |
| S4 | Rank preservation > 80% across 1,000 bootstraps | > 95% |
| S5 | > 60% of R1-R8 discovered; ≥ 2 novel insights | > 80% recall + > 5 novel insights |
| S6 | > 80% consistency across P1-P2 pipeline | > 90% |

---

## Reporting Standard

Each study report will include:
1. **Hypothesis** (stated before analysis)
2. **Method** (reproducible)
3. **Results** (quantitative)
4. **Validity threats** (what this can and cannot claim)
5. **Implications for human study design** (what to test next with real participants)
6. **Prototype modifications** (what to fix based on findings)

---

## Key References

1. NN/g (2025). "Evaluating AI-Simulated Behavior: Digital Twins and Synthetic Users." https://www.nngroup.com/articles/ai-simulations-studies/
2. "Whose Personae? Synthetic Persona Experiments in LLM Research." AAAI AIES, 2025. https://ojs.aaai.org/index.php/AIES/article/download/36553/38691/40628
3. "Simulacrum of Stories: LLMs as Qualitative Research Participants." CHI 2025. https://dl.acm.org/doi/full/10.1145/3706598.3713220
4. "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies." 2025. https://arxiv.org/html/2601.17087v1
5. "Human Subjects Research in the Age of Generative AI." CHI 2025 Extended Abstracts. https://dl.acm.org/doi/10.1145/3706599.3716299
6. "LLM Personas as a Substitute for Field Experiments." 2025. https://arxiv.org/html/2512.21080v1
