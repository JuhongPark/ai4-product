# P1: Selective Complementarity Dashboard

Classifies product tasks and recommends human-AI allocation based on the Selective Complementarity Framework.

## Quick Start

```bash
pip install streamlit anthropic pandas
streamlit run app.py
```

For LLM-powered classification (optional):
```bash
export ANTHROPIC_API_KEY=your_key_here
streamlit run app.py
```

Without an API key, the tool falls back to keyword-based classification.

## How It Works

1. User describes a product task and selects the lifecycle phase
2. Task is classified into one of 5 types (execution, creation, data-rich decision, uncertain decision, ethical/political)
3. Classification maps to an allocation recommendation:

| Task Type | Allocation |
|-----------|-----------|
| Execution (clear I/O) | AI-led, human-reviewed |
| Creation (aesthetic) | Human+AI collaboration |
| Decision (data-rich) | AI recommends, human decides |
| Decision (uncertain) | Human-led, AI-informed |
| Ethical/political | Human only |

## Benchmark Data

`benchmark_tasks.csv` contains 100 pre-classified tasks across all 6 lifecycle phases for evaluation.

## Evaluation

Classifications are logged to `logs/classifications.csv` for later analysis of accuracy, adoption rates, and decision outcomes.
