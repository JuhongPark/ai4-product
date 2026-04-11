"""
P1: Selective Complementarity Dashboard
Classifies product tasks and recommends human-AI allocation.

Usage:
    pip install streamlit anthropic
    streamlit run app.py
"""

import json
import os
import csv
import datetime
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PHASES = [
    "Discovery",
    "Design",
    "Development",
    "Testing",
    "Launch",
    "Growth",
]

TASK_TYPES = {
    "execution": {
        "label": "Execution (clear input → output)",
        "allocation": "AI-led, human-reviewed",
        "rationale": "Clear specifications make AI efficient; human review catches edge cases.",
    },
    "creation": {
        "label": "Creation (aesthetic / creative judgment)",
        "allocation": "Human+AI collaboration",
        "rationale": "Nature meta-analysis (106 experiments): creation tasks show positive complementarity.",
    },
    "decision_data_rich": {
        "label": "Decision — data-rich pattern recognition",
        "allocation": "AI recommends, human decides",
        "rationale": "Stanford selective complementarity: AI recommends only when human is likely uncertain.",
    },
    "decision_uncertain": {
        "label": "Decision — uncertain / strategic",
        "allocation": "Human-led, AI-informed",
        "rationale": "Cooper AI-PRISM: ~80% of NPD investment decisions are inherently uncertain.",
    },
    "ethical_political": {
        "label": "Ethical / political / stakeholder judgment",
        "allocation": "Human only",
        "rationale": "AADM 'AI Absent' zone: value judgments require human accountability.",
    },
}

PHASE_DEFAULTS = {
    "Discovery": "decision_uncertain",
    "Design": "creation",
    "Development": "execution",
    "Testing": "execution",
    "Launch": "decision_uncertain",
    "Growth": "decision_data_rich",
}

LOG_PATH = Path(__file__).parent / "logs"

# ---------------------------------------------------------------------------
# Classification (rule-based fallback when no LLM API key)
# ---------------------------------------------------------------------------

KEYWORDS = {
    "execution": [
        "implement", "code", "build", "write tests", "deploy", "migrate",
        "refactor", "fix bug", "create endpoint", "set up", "configure",
        "automate", "script", "documentation", "generate report",
    ],
    "creation": [
        "design", "prototype", "wireframe", "brand", "visual", "layout",
        "illustration", "copy", "content", "creative", "look and feel",
        "color", "typography", "logo", "motion", "animation", "ideate",
    ],
    "decision_data_rich": [
        "analyze", "a/b test", "metrics", "dashboard", "segment",
        "funnel", "conversion", "retention", "cohort", "experiment",
        "personalize", "recommend", "prioritize backlog", "rank features",
    ],
    "decision_uncertain": [
        "strategy", "roadmap", "go/no-go", "pivot", "launch timing",
        "market entry", "positioning", "pricing", "vision", "bet",
        "investment", "kill", "sunset", "partner", "acquire",
    ],
    "ethical_political": [
        "ethics", "bias", "fairness", "privacy", "compliance",
        "regulation", "stakeholder", "legal", "trust", "safety",
        "governance", "responsible", "transparency", "consent",
    ],
}


def classify_task_rule_based(description: str) -> dict:
    """Classify a task using keyword matching."""
    desc_lower = description.lower()
    scores = {}
    for task_type, keywords in KEYWORDS.items():
        scores[task_type] = sum(1 for kw in keywords if kw in desc_lower)

    best = max(scores, key=scores.get)
    confidence = scores[best] / max(sum(scores.values()), 1)

    if scores[best] == 0:
        return {"type": "unknown", "confidence": 0.0}
    return {"type": best, "confidence": round(min(confidence, 1.0), 2)}


def classify_task_llm(description: str, phase: str) -> dict:
    """Classify a task using Anthropic Claude API."""
    try:
        import anthropic

        client = anthropic.Anthropic()
        prompt = f"""Classify this product task into exactly one of these types:
- execution: clear input→output (coding, testing, deployment, documentation)
- creation: aesthetic/creative judgment (design, copywriting, branding, ideation)
- decision_data_rich: data-driven pattern recognition (analytics, A/B testing, prioritization)
- decision_uncertain: uncertain/strategic judgment (go/kill, pivot, pricing, vision)
- ethical_political: ethics, compliance, stakeholder politics, governance

Task: "{description}"
Product phase: {phase}

Respond with JSON only: {{"type": "<type>", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}}"""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        return json.loads(message.content[0].text)
    except Exception:
        return classify_task_rule_based(description)


def classify_task(description: str, phase: str, use_llm: bool = False) -> dict:
    if use_llm and os.environ.get("ANTHROPIC_API_KEY"):
        return classify_task_llm(description, phase)
    result = classify_task_rule_based(description)
    if result["type"] == "unknown":
        result["type"] = PHASE_DEFAULTS.get(phase, "decision_uncertain")
        result["confidence"] = 0.3
        result["reasoning"] = f"Defaulted to phase typical task type for {phase}."
    return result


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


def log_classification(description, phase, result, recommendation):
    LOG_PATH.mkdir(exist_ok=True)
    log_file = LOG_PATH / "classifications.csv"
    write_header = not log_file.exists()
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow([
                "timestamp", "description", "phase",
                "task_type", "confidence", "allocation",
            ])
        writer.writerow([
            datetime.datetime.now().isoformat(),
            description, phase,
            result["type"], result.get("confidence", ""),
            recommendation["allocation"],
        ])


# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------


def main():
    st.set_page_config(page_title="Selective Complementarity Dashboard", layout="wide")
    st.title("Selective Complementarity Dashboard")
    st.caption(
        "Recommends human-AI allocation for product tasks based on the "
        "Selective Complementarity Framework (ai4-product, 2026)."
    )

    # Sidebar
    st.sidebar.header("Settings")
    phase = st.sidebar.selectbox("Product Phase", PHASES)
    use_llm = st.sidebar.checkbox(
        "Use LLM classification (requires ANTHROPIC_API_KEY)",
        value=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Phase Default Allocations")
    for p, t in PHASE_DEFAULTS.items():
        info = TASK_TYPES[t]
        st.sidebar.markdown(f"**{p}**: {info['allocation']}")

    # Main input
    description = st.text_area(
        "Describe the product task",
        placeholder="e.g., Design a new onboarding flow for mobile users",
        height=100,
    )

    if st.button("Classify & Recommend", type="primary") and description:
        result = classify_task(description, phase, use_llm)
        task_type = result["type"]
        info = TASK_TYPES.get(task_type, TASK_TYPES["decision_uncertain"])

        # Display results
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Classification")
            st.metric("Task Type", info["label"])
            st.metric("Confidence", f"{result.get('confidence', 0):.0%}")
            if "reasoning" in result:
                st.info(f"Reasoning: {result['reasoning']}")

        with col2:
            st.subheader("Recommendation")
            allocation = info["allocation"]

            color_map = {
                "AI-led, human-reviewed": "🟢",
                "Human+AI collaboration": "🔵",
                "AI recommends, human decides": "🟡",
                "Human-led, AI-informed": "🟠",
                "Human only": "🔴",
            }
            emoji = color_map.get(allocation, "⚪")
            st.markdown(f"## {emoji} {allocation}")
            st.markdown(f"**Rationale**: {info['rationale']}")

        # Log
        log_classification(description, phase, result, info)

        # Framework reference
        with st.expander("Framework Reference"):
            st.markdown("""
| Task Type | Allocation | Evidence |
|-----------|-----------|----------|
| Execution (clear I/O) | AI-led, human-reviewed | Devin: senior understanding, junior execution |
| Creation (aesthetic) | Human+AI collaboration | Nature: creation tasks show positive complementarity |
| Decision (data-rich) | AI recommends, human decides | Stanford: selective recommendation = best decisions |
| Decision (uncertain) | Human-led, AI-informed | Cooper: ~80% NPD decisions inherently uncertain |
| Ethical/political | Human only | AADM: value judgments need human accountability |
            """)

    # Batch mode
    st.markdown("---")
    with st.expander("Batch Classification (CSV)"):
        uploaded = st.file_uploader("Upload CSV with columns: description, phase", type="csv")
        if uploaded:
            import pandas as pd

            df = pd.read_csv(uploaded)
            results = []
            for _, row in df.iterrows():
                r = classify_task(row["description"], row["phase"], use_llm)
                info = TASK_TYPES.get(r["type"], TASK_TYPES["decision_uncertain"])
                results.append({
                    "description": row["description"],
                    "phase": row["phase"],
                    "task_type": info["label"],
                    "allocation": info["allocation"],
                    "confidence": r.get("confidence", 0),
                })
            result_df = pd.DataFrame(results)
            st.dataframe(result_df)
            st.download_button(
                "Download Results",
                result_df.to_csv(index=False),
                "complementarity_results.csv",
            )


if __name__ == "__main__":
    main()
