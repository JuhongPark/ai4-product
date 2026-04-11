# P4: AI Adoption Readiness Diagnostic

Assesses team readiness for AI adoption based on the 7 success patterns from Stanford Playbook (51 cases) and MIT NANDA.

## Quick Start

```bash
pip install streamlit pandas
streamlit run app.py
```

## The 7 Patterns

| # | Pattern | Source |
|---|---------|--------|
| 1 | Process Readiness | Stanford: "The difference was never the AI model" |
| 2 | Line Manager Ownership | MIT: Decentralized > centralized adoption |
| 3 | Buy Before Build | MIT: 67% vendor success vs 33% internal |
| 4 | Back-Office First | MIT: Highest ROI in document automation, HR, support |
| 5 | Narrow and Deep | Stanford: 3x efficiency improvement with focus |
| 6 | Learning Systems | MIT: #1 technical differentiator |
| 7 | Human-in-the-Loop by Design | McKinsey: 65% of high performers have defined HITL |

## Readiness Levels

| Score | Level | Implication |
|-------|-------|-------------|
| 0-14 | Not Ready | Fix foundations before AI investment |
| 15-21 | Partially Ready | Address critical gaps |
| 22-28 | Ready | Go deep on one phase |
| 29-35 | Highly Ready | Positioned for the successful 5% |

## Evaluation Data

Assessments are logged to `logs/assessments.csv` for retrospective analysis.
