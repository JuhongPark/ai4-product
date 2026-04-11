# Prototype Evaluation Report (Pre-Participant Phase)

> Results from automated testing and case simulation before deploying to human participants.
> Date: 2026-04-11

---

## P1: Selective Complementarity Dashboard

### Rule-Based Classifier Performance (100 benchmark tasks)

| Metric | Value |
|--------|-------|
| **Overall accuracy** | **67.3%** (66/98) |
| Best type: Execution | 77.4% F1 |
| Best type: Decision (data-rich) | 77.4% F1 |
| Worst type: Ethical/political | 26.7% F1 (precision 100%, recall 15%) |
| Best phase: Development | 83.3% |
| Worst phase: Launch | 35.3% |

### Key Findings

1. **Execution and data-rich decisions** are well-classified by keyword matching (F1 > 77%)
2. **Ethical/political tasks** are almost invisible to keyword matching — only 2/13 detected. These tasks often use neutral language ("evaluate," "assess") that overlaps with other types
3. **Launch phase** is hardest — mixed task types and strategic language confuse the classifier
4. **LLM classification would likely improve accuracy significantly**, especially for ethical and strategic tasks where context understanding matters

### Implications for Research

- Rule-based classifier is a usable MVP for demonstration and data collection
- LLM classification is essential for production-quality tool
- Ethical/political detection needs dedicated mechanism (possibly separate classifier or keyword expansion)
- Phase-specific tuning would help (Launch phase needs different keywords)

---

## P2: AADM Scoring Tool

### 30 Scenario Analysis (after scoring logic fix)

| Metric | Value |
|--------|-------|
| **Role distribution** | Decides: 10%, Recommends: 37%, Informs: 10%, Assists: 23%, Absent: 20% |
| **All 5 roles covered** | Yes (after fix — initial version had 0% Absent) |
| **Face validity** | 4/5 spot checks passed |
| **Boundary sensitivity** | 50 cases where ±1 on any dimension changes the role |
| **Confidence** | 40% high (≥0.85), 60% medium (0.7-0.84), 0% low |

### Key Findings

1. **AI Recommends is the most common role (37%)** — makes sense given that most product decisions have moderate data and moderate objectivity
2. **Rule ordering matters critically** — AI Absent rules must be checked before AI Assists to avoid misclassification of strategic decisions as "generate options" tasks
3. **50 boundary-sensitive cases across 30 scenarios** = high sensitivity to scoring. A ±1 change on any dimension frequently changes the recommendation
4. **S (Subjectivity) is the most influential dimension** — it differentiates between "AI Assists" (creative) and "AI Informs/Recommends" (analytical)

### Implications for Research

- High boundary sensitivity means **inter-rater reliability study is critical** — if PMs disagree by ±1 on D/R/S, they'll get different recommendations
- Need anchoring examples for each score level to improve reliability
- Consider continuous (not discrete) scoring to reduce boundary effects
- Separate "ethical override" flag may be needed instead of encoding ethics into S dimension

---

## P3: Design Fiction Workshop Kit

### Scenario-Framework Coverage Analysis

| Framework | Scenarios Exposing a Gap | Coverage |
|-----------|------------------------|----------|
| Selective Complementarity | 7/8 | 87.5% |
| AADM Scoring | 6/8 | 75.0% |
| Success Patterns | 7/8 | 87.5% |

### Predicted Discoveries (8 requirements, 6 risks)

High-novelty predictions (things current frameworks miss):
- **R1**: Creative tasks need human review even when metrics look good
- **R3**: AI cannot validate its own output (circular testing blind spot)
- **R4**: Portfolio-level strategic oversight missing from per-task tools
- **R6**: Minimum direct human-customer contact quota needed
- **R7**: Multi-agent governance protocol for unsupervised agent-to-agent decisions

### Evaluation Benchmark Established

After running workshops, we can measure:
- **Recall**: How many of R1-R8 did participants discover?
- **Precision**: What did participants discover beyond our predictions?
- **Novelty confirmation**: Participant ratings on "Would traditional methods find this?"

---

## P4: Success Pattern Checklist

### Case Simulation Results (6 real-world cases)

| Case | Outcome | Score | Level | Prediction Correct? |
|------|---------|-------|-------|-------------------|
| PostNL | SUCCESS | 32/35 | Highly Ready | YES |
| PepsiCo | SUCCESS | 31/35 | Highly Ready | YES |
| OpenTable | SUCCESS | 27/35 | Ready | YES |
| Klarna | FAILURE | 14/35 | Not Ready | YES |
| Devin | PARTIAL | 19/35 | Partially Ready | YES |
| EY.ai PDLC | TBD | 24/35 | Ready (borderline) | TBD |

### Key Finding: Perfect Monotonic Correlation

**Higher pattern scores correlate perfectly with outcomes across all 5 scored cases.** This is the strongest pre-validation signal possible without a formal study.

### Most Predictive Patterns

1. **#7 HITL by Design** — strongest differentiator (Klarna: 1, PostNL: 4)
2. **#5 Narrow and Deep** — all successes ≥ 4, all failures ≤ 2
3. **#4 Back-Office First** — Klarna went customer-facing first (score: 1) and failed

### EY.ai PDLC Prediction

Score of 24 (Ready but borderline) with low scores on #4 (Back-Office First: 3) and #5 (Narrow and Deep: 2). **Prediction: will succeed in narrow domains (legacy modernization) but struggle with full end-to-end claims.**

---

## Cross-Prototype Insights

### Issue 1: The Ethics Gap

All prototypes struggle with ethical/political dimensions:
- P1: 15% recall on ethical tasks
- P2: AADM S dimension doesn't capture ethics well
- P3: Scenario Card 2 (biased pricing) specifically designed to expose this
- **Recommendation**: Add dedicated ethical override flag across all tools

### Issue 2: Portfolio vs Task-Level Blindness

Current tools optimize per-task or per-decision, but:
- P3 Scenario Card 4 (strategy drift) shows this can lead to strategic bankruptcy
- P4: No pattern explicitly addresses portfolio coherence
- **Recommendation**: Add "strategic alignment" as a meta-check above individual tool recommendations

### Issue 3: Multi-Agent Governance

- P2: AADM assumes single decision-maker; multi-agent coordination is ungoverned
- P3 Scenario Card 7 directly addresses this
- P4 Pattern #7 (HITL) designed for single agent, not multi-agent mesh
- **Recommendation**: Extend all frameworks for multi-agent scenarios

---

## Next Steps (Require Human Participants)

| Priority | Activity | Participants Needed | Duration |
|----------|---------|-------------------|----------|
| 1 | P2 inter-rater reliability study | 5 PMs scoring 30 scenarios | 2 weeks |
| 2 | P3 Workshop 1 (PM-only) | 5-7 PMs | 3 hours |
| 3 | P1 field test with LLM classifier | 2-3 product teams | 4 weeks |
| 4 | P3 Workshops 2 & 3 | 5-7 designers; 6-8 mixed | 3 hours each |
| 5 | P4 retrospective survey | 20+ teams | 2 weeks |
| 6 | P4 prospective pilot | 3 new teams | 8 weeks |
