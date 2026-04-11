# P2: AI-Augmented Decision Matrix (AADM) v2 Scoring Tool

Scores product decisions on **four dimensions** — D (Data), R (Reversibility), S (Objectivity), C (Creativity) — to recommend the appropriate AI role.

## v2 Changelog

- **Added Creativity (C) dimension** — resolves the v1 conflict where creative tasks were misclassified as AI Absent
- **Borderline detection** — warns when ±1 on any dimension would change the recommendation
- **Simulation-validated**: P1-P2 consistency improved from 82.7% to **100%** with 0 regressions

## Quick Start

```bash
pip install streamlit pandas
streamlit run app.py
```

## How It Works

Score each decision on four 1-5 dimensions:

- **D (Data Availability)**: 1 = pure intuition → 5 = rich metrics
- **R (Reversibility)**: 1 = irreversible → 5 = easily reversed
- **S (Objectivity)**: 1 = highly subjective → 5 = highly objective
- **C (Creativity)**: 1 = no creative element → 5 = primarily creative

The tool maps scores to one of 5 AI roles:

| Score Profile | AI Role |
|--------------|---------|
| High D, High R, High S, Low C | AI Decides (autonomous) |
| High D, High S | AI Recommends (human approves) |
| Medium D, Medium S, Low C | AI Informs (human decides with data) |
| **High C** (any D/S) | **AI Assists (creative collaboration)** |
| Low D, Low R, Low C | AI Absent (human leads) |

## Why 4 Dimensions?

Simulation Study S6 found that v1 (D/R/S only) produced 17 inconsistencies — all on creative tasks. Creative tasks are low-data (D=2) and low-objectivity (S=1), which v1 mapped to "AI Absent." But the Nature meta-analysis (106 experiments) shows creation is the one task type where Human+AI > either alone. C resolves this by distinguishing "low data because strategic" from "low data because creative."

## Scenario Library

30 pre-built decision scenarios with D/R/S/C scores. Use for inter-rater reliability studies.

## Evaluation Data

Scoring sessions are logged to `logs/aadm_v2_scores.csv` including borderline status.
