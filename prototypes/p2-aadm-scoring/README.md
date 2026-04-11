# P2: AI-Augmented Decision Matrix (AADM) Scoring Tool

Scores product decisions on Data Availability (D), Reversibility (R), and Subjectivity (S) to recommend the appropriate AI role.

## Quick Start

```bash
pip install streamlit pandas
streamlit run app.py
```

## How It Works

Score each decision on three 1-5 dimensions:

- **D (Data Availability)**: 1 = pure intuition → 5 = rich metrics
- **R (Reversibility)**: 1 = irreversible → 5 = easily reversed
- **S (Subjectivity)**: 1 = highly subjective → 5 = highly objective

The tool maps scores to one of 5 AI roles:

| Score Profile | AI Role |
|--------------|---------|
| High D, High R, High S | AI Decides (autonomous) |
| High D, any R, High S | AI Recommends (human approves) |
| Medium D, Medium S | AI Informs (human decides with data) |
| Any D, Low S | AI Assists (generates options) |
| Low D, Low R, Low S | AI Absent (human leads) |

## Scenario Library

30 pre-built decision scenarios across all 6 lifecycle phases, with suggested D/R/S scores. Use for inter-rater reliability studies.

## Evaluation Data

Scoring sessions are logged to `logs/aadm_scores.csv`.
