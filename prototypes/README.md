# Prototypes: AI-for-Product Toolkit

> Working prototypes to validate the three original frameworks from the ai4-product research.

## Overview

| Prototype | Validates | Type | Status |
|-----------|----------|------|--------|
| [P1: Complementarity Dashboard](p1-complementarity-dashboard/) | Selective Complementarity Framework | Streamlit app | Built |
| [P2: AADM Scoring Tool](p2-aadm-scoring/) | AI-Augmented Decision Matrix | Streamlit app | Built |
| [P3: Design Fiction Workshop Kit](p3-design-fiction-kit/) | Speculative methods for discovery | Workshop materials | Designed |
| [P4: Success Pattern Checklist](p4-success-checklist/) | Successful 5% patterns | Streamlit app | Built |

## Quick Start

```bash
# Install dependencies (shared across P1, P2, P4)
pip install streamlit pandas anthropic

# Run any prototype
cd p1-complementarity-dashboard && streamlit run app.py
cd p2-aadm-scoring && streamlit run app.py
cd p4-success-checklist && streamlit run app.py
```

## How They Connect

```
          P3: Design Fiction Workshop
          (discovers new requirements & risks)
                    ↓
    ┌───────────────┼───────────────┐
    ↓               ↓               ↓
P1: CompDash    P2: AADM        P4: Checklist
(task-level)    (decision-level) (org-level)
    ↓               ↓               ↓
    └───────────────┼───────────────┘
                    ↓
         Validated AI-for-Product Toolkit
```

## Research Plan

See [docs/prototyping-research-plan.md](../docs/prototyping-research-plan.md) for the full 9-month ADR validation plan.
