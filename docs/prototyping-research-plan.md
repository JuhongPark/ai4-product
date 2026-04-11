# Prototyping Research Plan: Validating AI-for-Product Frameworks

> Based on findings from the ai4-product research survey (2022-2026).
> Date: 2026-04-11

---

## Research Objective

Validate three original frameworks through prototype experiments:

1. **Selective Complementarity Framework** — When to use AI vs humans at each product lifecycle phase
2. **Successful 5% Patterns** — Can the 7 success patterns be codified into a repeatable methodology?
3. **AADM (AI-Augmented Decision Matrix)** — Does the D/R/S scoring model predict the right AI role?

---

## Methodology: Action Design Research (ADR)

ADR is chosen because it interweaves building, intervening, and evaluating concurrently — suited for AI artifacts where "design and deployment cannot be fixed from the outset" (EJIS, 2024).

### Four ADR Stages

```
Stage 1: Problem Formulation
  → Define research questions from our frameworks

Stage 2: Building, Intervention, Evaluation (BIE)
  → Build prototypes, deploy with real teams, evaluate concurrently

Stage 3: Reflection and Learning
  → Extract design principles from each cycle

Stage 4: Formalization of Learning
  → Generalize into validated frameworks
```

---

## Prototype 1: Selective Complementarity Dashboard

### Research Question
> When product teams can see a real-time recommendation of "AI-led / Human+AI / Human-led" for each task, do they make better allocation decisions?

### What to Build

An interactive dashboard that:
- Takes a product task description as input
- Classifies the task type (creation / decision / execution / verification)
- Recommends an allocation model based on our framework:

| Task Type | Recommendation |
|-----------|---------------|
| Clear input→output (code, test) | AI-led, human-reviewed |
| Creative/aesthetic (design, copy) | Human+AI collaboration |
| Data-rich pattern (analytics, A/B) | AI recommends, human decides |
| Uncertain/strategic (go/kill, pivot) | Human-led, AI-informed |
| Ethical/political (values, stakeholders) | Human only |

### Prototype Spec

```
Input:  Task description (text) + phase (discovery/design/dev/test/launch/growth)
Process: LLM classification → rule-based mapping → recommendation
Output: Recommended allocation + confidence score + rationale
```

### Technology
- LLM API (Claude/GPT) for task classification
- Simple web interface (React or Streamlit)
- Logging for evaluation data collection

### Evaluation Design

| Metric | Method |
|--------|--------|
| Classification accuracy | Expert panel rates 100 tasks; compare to model output |
| Adoption rate | Do teams follow the recommendation? Track over 4 weeks |
| Decision quality | Compare task outcomes (AI-led vs recommended allocation) |
| User satisfaction | Post-task survey (trust, usefulness, willingness to use again) |

### Timeline: 6 weeks

| Week | Activity |
|------|---------|
| 1-2 | Build prototype; curate 100 benchmark tasks |
| 3 | Expert panel validation of task classification |
| 4-5 | Deploy with 2-3 product teams; collect usage data |
| 6 | Analysis and design principle extraction |

---

## Prototype 2: AADM Scoring Tool

### Research Question
> Does scoring decisions on Data Availability (D), Reversibility (R), and Subjectivity (S) reliably predict the appropriate AI role?

### What to Build

A decision-support tool that:
- Presents a product decision point (e.g., "Should we launch this feature?")
- Prompts the user to score D, R, S (1-5 each)
- Maps the score to an AI role recommendation:

| Score Profile | AI Role |
|--------------|---------|
| High D, High R, High S | AI Decides (autonomous) |
| High D, Low R, High S | AI Recommends (human approves) |
| Medium all | AI Informs (human decides with data) |
| Low D, Any R, Low S | AI Assists (generates options) |
| Low D, Low R, Low S | AI Absent (human leads) |

- Compares to Cooper's AI-PRISM for gate decisions (where applicable)

### Prototype Spec

```
Input:  Decision description + D/R/S scores (slider 1-5)
Process: Scoring algorithm → role mapping → historical comparison
Output: Recommended AI role + similar past decisions + confidence level
```

### Evaluation Design

**Phase A — Inter-Rater Reliability (2 weeks)**
- 5 product managers score the same 30 decision scenarios
- Measure: Do different PMs arrive at the same D/R/S scores? (ICC, Cohen's kappa)
- Threshold: ICC > 0.7 for the framework to be considered reliable

**Phase B — Predictive Validity (4 weeks)**
- Teams use AADM for real decisions over 4 weeks
- Track: Did the recommended AI role lead to better outcomes?
- Compare: Decisions that followed AADM vs. those that diverged
- Metrics: Decision speed, outcome satisfaction, rework rate

**Phase C — Comparison to Expert Judgment (2 weeks)**
- 3 senior PMs and 2 AI researchers rate the same decisions without AADM
- Compare expert allocation to AADM recommendation
- Measure: Agreement rate, cases where AADM outperforms/underperforms

### Timeline: 8 weeks

| Week | Activity |
|------|---------|
| 1-2 | Build tool; curate 30 decision scenarios |
| 3-4 | Phase A: Inter-rater reliability study |
| 5-8 | Phase B: Field deployment with 3 product teams |
| 8 | Phase C: Expert comparison + analysis |

---

## Prototype 3: Design Fiction Workshop Series

### Research Question
> Can design fiction workshops reveal product requirements and risks that traditional methods (interviews, surveys, prototyping) miss?

### What to Build

Not software — a **workshop protocol** tested across multiple teams:

### Workshop Design: "A Day in the Life of an AI Product Team in 2028"

**Structure (3-hour session)**

```
Part 1: World-Building (45 min)
  - Facilitator presents a near-future scenario based on our research:
    "It's 2028. Your product team uses AI agents for 80% of execution.
     AADM scores determine which decisions AI handles autonomously.
     Last month, an AI agent shipped a feature that violated your
     brand guidelines. Your team's Selective Complementarity dashboard
     recommended 'Human+AI' but the PM overrode it to 'AI-led.'"
  - Participants extend the scenario: What happened next?

Part 2: Artifact Creation (60 min)
  - Teams create diegetic prototypes:
    Option A: A "retrospective report" from the fictional team
    Option B: An "incident post-mortem" for the brand violation
    Option C: A "policy document" defining when AI override is allowed
  - Materials: templates, AI-generated visuals, cards with scenario twists

Part 3: Critical Analysis (45 min)
  - Teams present artifacts to each other
  - Structured discussion:
    (1) What requirements did this reveal that we hadn't thought of?
    (2) What risks emerged that our current frameworks don't address?
    (3) What governance rules would have prevented the incident?

Part 4: Extraction (30 min)
  - Facilitator synthesizes: new requirements, new risks, new governance rules
  - Participants rate: "Would traditional methods have found this?" (1-5)
```

### Evaluation Design

| Metric | Method |
|--------|--------|
| Novel requirements discovered | Count requirements not found in prior interviews/surveys |
| Risk identification | Count risks not in current research-gaps.md |
| Participant-rated novelty | "Would traditional methods have found this?" (1-5 scale) |
| Actionability | Can discovered requirements be translated into prototype specs? |
| Cross-team consistency | Do different teams discover similar requirements/risks? |

### Run Plan: 3 workshops × 3 different team compositions

| Workshop | Participants | Focus |
|----------|-------------|-------|
| W1 | Product managers (5-7) | PM decision-making with AI |
| W2 | Designers (5-7) | AI in creative workflow |
| W3 | Mixed team (PM + designer + engineer, 6-8) | Cross-functional AI collaboration |

### Timeline: 6 weeks

| Week | Activity |
|------|---------|
| 1-2 | Design workshop protocol; prepare scenarios and materials |
| 3 | W1: PM workshop |
| 4 | W2: Designer workshop |
| 5 | W3: Mixed team workshop |
| 6 | Cross-workshop analysis; requirement/risk synthesis |

---

## Prototype 4: Success Pattern Checklist Validation

### Research Question
> Do teams that follow the 7 success patterns from the "Successful 5%" analysis achieve better AI adoption outcomes?

### What to Build

A **diagnostic checklist tool** based on the 7 patterns:

```
□ 1. Process readiness assessed before tool selection
□ 2. Line managers (not central AI lab) driving adoption
□ 3. Vendor solution evaluated before internal build
□ 4. Starting with back-office / internal operations
□ 5. One phase deeply before expanding (narrow and deep)
□ 6. Feedback loops and learning built in
□ 7. Human-in-the-loop designed, not bolted on
```

### Prototype Spec

```
Input:  Team self-assessment (7 questions, scored 1-5)
Process: Pattern matching → gap identification → recommendation
Output: Readiness score (0-35) + specific gaps + action items per gap
```

### Evaluation Design

**Retrospective Validation (4 weeks)**
- Survey 20+ teams that have attempted AI adoption (mix of success/failure)
- Each team scores themselves on the 7 patterns (retrospectively)
- Measure: Do higher-scoring teams correlate with successful adoption?
- Statistical test: Logistic regression (success/failure ~ pattern scores)

**Prospective Pilot (8 weeks)**
- 3 teams use the checklist before starting a new AI initiative
- Track: Do they follow the recommendations? What adjustments do they make?
- Compare outcomes to baseline (teams that didn't use the checklist)

### Timeline: 12 weeks total

| Week | Activity |
|------|---------|
| 1-2 | Build checklist tool; recruit 20+ teams for retrospective |
| 3-4 | Retrospective survey collection and analysis |
| 5 | Statistical validation; refine checklist based on findings |
| 6-12 | Prospective pilot with 3 new teams |
| 12 | Final analysis and pattern refinement |

---

## Integration: How the 4 Prototypes Connect

```
                    Prototype 3: Design Fiction
                    (discovers requirements and risks
                     that other methods miss)
                           ↓ feeds into
    ┌──────────────────────┼──────────────────────┐
    ↓                      ↓                      ↓
Prototype 1:          Prototype 2:          Prototype 4:
Selective             AADM Scoring          Success Pattern
Complementarity       Tool                  Checklist
Dashboard                                   
(task-level:          (decision-level:      (organization-level:
 which tasks?)         what AI role?)        are we ready?)
    ↓                      ↓                      ↓
    └──────────────────────┼──────────────────────┘
                           ↓
                  Validated Framework:
                  "AI-for-Product Toolkit"
```

### Data Flow Between Prototypes

- **P3 → P1**: Design fiction workshops reveal new task types to classify
- **P3 → P2**: Workshops reveal decision scenarios to score with AADM
- **P1 + P2 → P4**: Task/decision-level learnings inform organizational checklist
- **P4 → P1/P2**: Organizational readiness determines whether P1/P2 will work

---

## Overall Timeline

```
Month 1-2:  Build all prototypes in parallel
Month 2-3:  P1 (Complementarity Dashboard) + P3 W1 (PM Workshop)
Month 3-4:  P2 Phase A (Reliability) + P3 W2/W3 (Designer/Mixed)
Month 4-5:  P1 field test + P2 Phase B (Field deployment)
Month 5-6:  P4 retrospective survey + cross-prototype analysis
Month 6-8:  P4 prospective pilot
Month 8-9:  Integration, framework refinement, paper writing
```

## Expected Outputs

| Output | Target Venue | Timeline |
|--------|-------------|----------|
| AADM validation paper | CHI / CSCW 2027 | Month 8 |
| Design fiction methodology paper | DIS / C&C 2027 | Month 7 |
| Selective Complementarity empirical study | EJIS / Technovation | Month 9 |
| Success patterns validation | California Management Review | Month 9 |
| AI-for-Product Toolkit (open source) | GitHub + practitioner blog | Month 9 |

---

## Resource Requirements

| Resource | Purpose | Estimated |
|----------|---------|-----------|
| LLM API access | Task classification, AADM prototype | ~$500/month |
| Web development | Dashboard, scoring tool, checklist | 1 developer, 2 months |
| Workshop facilitation | 3 design fiction sessions | Facilitator + materials |
| Participant recruitment | 20+ teams for survey, 3 teams for pilot | University/industry network |
| Expert panel | 5 PMs + 2 AI researchers for AADM validation | Compensation/collaboration |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Low inter-rater reliability for AADM | Refine D/R/S definitions iteratively; add anchoring examples |
| Teams don't follow recommendations | Study divergence as data — "why did they override?" is valuable |
| Design fiction yields only obvious insights | Seed workshops with edge cases from Klarna, Devin failures |
| Small sample size | Focus on depth (rich qualitative data) over breadth |
| Framework too academic for practitioners | Co-design with practitioners from workshop 1 onward |

---

## Key References

1. "Design principles for AI-augmented decision making." EJIS, 2024. https://www.tandfonline.com/doi/full/10.1080/0960085X.2024.2330402
2. "Prototyping with Prompts." CHI 2025. https://dl.acm.org/doi/10.1145/3706598.3713166
3. "Human-AI collaboration by design." Design Society (Cambridge), 2024. https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/humanai-collaboration-by-design/45BC30ADFF2FE3B204D4A29DD67F6353
4. "AI and Agile: Research Roadmap from XP2025 Workshop." https://arxiv.org/html/2508.20563v1
5. "Towards a Science of Human-AI Decision Making." FAccT 2023. https://dl.acm.org/doi/fullHtml/10.1145/3593013.3594087
6. Sein et al. (2011). "Action Design Research." MIS Quarterly.
