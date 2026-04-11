# P3 Pre-Analysis: Scenario Cards vs Framework Gap Mapping

> Analyzing which framework gaps each scenario card is designed to expose,
> and predicting what requirements/risks workshops should discover.

---

## Scenario-Framework Matrix

| Card | Scenario | SC Framework Gap | AADM Gap | Success Pattern Gap | Predicted Discovery |
|------|----------|-----------------|----------|--------------------|--------------------|
| **1** | Brand violation (AI redesigns hero) | Misclassified creation as execution | S score missed aesthetic dimension | #7 HITL wasn't designed for creative review | **Req**: Creative tasks need mandatory human review even when metrics look good |
| **2** | Biased pricing | Ethical dimension invisible to data-rich classification | S=5 was wrong — ethical tasks can look objective | #6 Learning system didn't learn fairness constraints | **Risk**: AADM can't detect ethical issues in "objective" metrics |
| **3** | Silent failure (circular testing) | AI testing AI = no complementarity | D=5 was illusory — data quality wasn't validated | #5 Deep but in wrong direction — testing itself | **Req**: Independent validation layer; AI cannot validate its own output |
| **4** | Strategy drift | Per-task optimization ≠ portfolio strategy | AADM is per-decision, no portfolio view | #5 Narrow-deep became narrow-stuck | **Risk**: Task-level tools can't prevent strategic drift; need portfolio-level oversight |
| **5** | Knowledge drain | Efficiency gains mask knowledge loss | Not captured by D/R/S at all | #6 System learned tasks, forgot context | **Risk**: Rigobon cognitive atrophy — AI efficiency → organizational amnesia |
| **6** | Customer empathy gap | AI scales data but not empathy | D score high but data is filtered | #4 Back-office success doesn't transfer to front-office understanding | **Req**: Mandatory unfiltered human-customer contact quota |
| **7** | Governance vacuum (agents coordinating) | Multi-agent bypasses human-in-loop | No AADM score calculated = ungoverned decision | #7 HITL designed for single agent, not multi-agent | **Risk**: Multi-agent coordination creates emergent decisions no human approved |
| **8** | Trust collapse | Binary trust (all or nothing) after failures | Confidence scores didn't prevent over-reliance | #7 HITL degraded over time as trust grew | **Req**: Trust calibration mechanism — graduated, not binary |

---

## Gap Coverage Analysis

### Gaps Each Scenario Exposes

| Framework | # of Scenarios That Expose a Gap | Coverage |
|-----------|--------------------------------|----------|
| Selective Complementarity | 7/8 | 87.5% |
| AADM Scoring | 6/8 | 75.0% |
| Success Patterns | 7/8 | 87.5% |

### Gaps NOT Covered by Any Scenario

| Gap | Why Missing | Proposed Addition |
|-----|-----------|------------------|
| Cross-cultural differences in AI trust | All scenarios assume Western context | Add twist: "Your Japan team rejects AI recommendations that the US team accepts" |
| Regulatory compliance failure | Partially covered by Twist B | Could be a full scenario: AI ships feature that violates new regulation |
| Vendor lock-in / API dependency | Covered by Twist D | Consider promoting to full scenario given Chiang's relevance |

---

## Predicted Workshop Outcomes

### Requirements We Expect to Discover (Hypotheses)

| # | Predicted Requirement | Source Scenario | Novelty (vs current frameworks) |
|---|----------------------|----------------|-------------------------------|
| R1 | Creative output needs human review regardless of metric performance | Card 1 | HIGH — current framework allows AI-led for "execution" |
| R2 | Ethical audit layer independent of AADM scoring | Card 2 | HIGH — AADM has no ethical override |
| R3 | AI cannot validate its own output; need external validation | Card 3 | HIGH — not addressed in any current framework |
| R4 | Portfolio-level strategic oversight beyond per-task allocation | Card 4 | HIGH — completely missing from current frameworks |
| R5 | Organizational knowledge preservation policy | Card 5 | MEDIUM — Rigobon warned but no mechanism proposed |
| R6 | Minimum direct human-customer contact quota | Card 6 | HIGH — counter-intuitive in an "AI scales everything" world |
| R7 | Multi-agent governance protocol (no agent-to-agent unsupervised decisions) | Card 7 | HIGH — current HITL assumes single agent |
| R8 | Graduated trust calibration (not binary) | Card 8 | MEDIUM — trust literature exists but not operationalized |

### Risks We Expect to Discover

| # | Predicted Risk | Source | Novelty |
|---|---------------|--------|---------|
| K1 | Metric optimization can violate unstated human values (brand, fairness) | Cards 1, 2 | HIGH |
| K2 | AI self-validation creates invisible blind spots | Card 3 | HIGH |
| K3 | Per-task efficiency can mask strategic bankruptcy | Card 4 | HIGH |
| K4 | Organizational knowledge atrophies without explicit preservation | Card 5 | MEDIUM |
| K5 | Multi-agent systems create emergent ungoverned decisions | Card 7 | HIGH |
| K6 | Trust is fragile — one failure cascade can undo months of gains | Card 8 | MEDIUM |

---

## Evaluation Benchmark

After running workshops, compare actual discoveries against these predictions:
- **Recall**: How many of R1-R8 and K1-K6 did participants actually discover?
- **Precision**: What did participants discover that we DIDN'T predict? (novelty beyond predictions)
- **Novelty confirmation**: Do participants rate these as "Would traditional methods have found this?" ≥ 4/5?

This pre-analysis serves as the evaluation baseline — if workshops discover exactly what we predicted, the method is confirmatory. If they discover things we didn't predict, the method has genuine exploratory power.
