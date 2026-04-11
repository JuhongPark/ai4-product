"""
P4: Success Pattern Checklist — AI Adoption Readiness Diagnostic
Based on the 7 patterns from Stanford Playbook (51 cases) + MIT NANDA.

Usage:
    pip install streamlit pandas
    streamlit run app.py
"""

import csv
import datetime
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# The 7 Success Patterns
# ---------------------------------------------------------------------------

PATTERNS = [
    {
        "id": 1,
        "name": "Process Readiness",
        "question": "Have you assessed whether your current workflows are well-defined and functioning before adding AI?",
        "description": "AI magnifies whatever it touches — including broken processes (Gartner 2026). The 5% that succeed have functioning processes before AI.",
        "low_guidance": "Map your current workflow end-to-end. Fix bottlenecks and ambiguities before adding AI. If the process is broken, AI will accelerate the breakage.",
        "high_guidance": "Your process is ready. Focus on identifying the highest-value insertion points for AI within the workflow.",
        "source": "Stanford Playbook: 'The difference was never the AI model. It was always the organization.'",
    },
    {
        "id": 2,
        "name": "Line Manager Ownership",
        "question": "Are line managers (not a central AI lab or innovation team) driving AI adoption in your team?",
        "description": "MIT NANDA: Centralized AI labs lead in pilot count but lag in production conversion. Line managers who understand daily workflows drive successful adoption.",
        "low_guidance": "Identify 2-3 team leads who are already experimenting with AI tools ('prosumers'). Empower them to lead adoption in their domain rather than waiting for a top-down mandate.",
        "high_guidance": "Good. Ensure these line managers have budget authority and executive air-cover to experiment and fail safely.",
        "source": "MIT NANDA: 'Key factors for success include empowering line managers, not just central AI labs.'",
    },
    {
        "id": 3,
        "name": "Buy Before Build",
        "question": "Have you evaluated specialized vendor solutions before deciding to build AI tools internally?",
        "description": "MIT data: vendor-led solutions succeed 67% of the time vs. 33% for internal builds. Vendors bring domain expertise, multi-client learning, and built-in feedback loops.",
        "low_guidance": "Before building, survey the vendor landscape. Request demos from 3+ specialized vendors. Internal build should be a conscious decision, not the default.",
        "high_guidance": "You've evaluated the market. If building internally, ensure you have a clear competitive reason (proprietary data, regulatory need, core differentiator).",
        "source": "MIT NANDA: 'Purchased solutions delivered more reliable results.' (67% vs 33%)",
    },
    {
        "id": 4,
        "name": "Back-Office First",
        "question": "Are you starting AI adoption with internal/back-office operations before customer-facing features?",
        "description": "MIT: Highest ROI is in back-office — document automation, HR, internal support ($2-10M/year savings). Most companies over-invest in sales/marketing AI first.",
        "low_guidance": "Identify internal tasks your team does repeatedly: documentation, test writing, data analysis, meeting summaries. Start there. Build confidence before touching customer experiences.",
        "high_guidance": "Smart sequencing. Use internal AI successes to build organizational confidence and learning before scaling to customer-facing applications.",
        "source": "MIT NANDA: 'Back-office functions deliver higher returns through cost reduction and efficiency gains.'",
    },
    {
        "id": 5,
        "name": "Narrow and Deep",
        "question": "Are you focusing AI on one phase/function deeply before expanding to others?",
        "description": "Stanford: Deployment efficiency improved 3x when teams focused (from 16:1 to 5:1 experiment-to-production ratio). Broad-and-shallow creates 'science projects' with no impact.",
        "low_guidance": "Pick ONE phase of your product lifecycle where AI can have the highest impact. Go deep: integrate, measure, iterate. Resist the urge to add AI everywhere at once.",
        "high_guidance": "Depth-first approach is working. Document your learnings before expanding to the next phase — what worked, what didn't, what would you do differently.",
        "source": "Stanford Playbook: Deployment efficiency improved 3x with focused approach.",
    },
    {
        "id": 6,
        "name": "Learning Systems",
        "question": "Does your AI tooling retain feedback, adapt to context, and improve over time?",
        "description": "MIT: 'Most GenAI systems do not retain feedback, adapt to context, or improve over time.' This is the #1 technical differentiator between the 5% and the 95%.",
        "low_guidance": "Demand learning capability from your tools/vendors. Set up feedback loops: track which AI outputs are accepted/rejected, use this to improve over time. Static AI = failed AI.",
        "high_guidance": "You have learning systems. Ensure feedback loops are measured and reported — how much has the system improved over the last month/quarter?",
        "source": "MIT NANDA: 'The core barrier is learning rather than infrastructure, regulation, or talent.'",
    },
    {
        "id": 7,
        "name": "Human-in-the-Loop by Design",
        "question": "Have you designed explicit human review/override points into your AI workflows (not added them as an afterthought)?",
        "description": "McKinsey: 65% of AI high performers have defined HITL processes vs. only 23% of others. Klarna's failure came from removing human oversight entirely.",
        "low_guidance": "For each AI-powered workflow, define: (1) When must a human review? (2) How does a human override? (3) Where does human feedback go? Design these before deployment.",
        "high_guidance": "HITL is designed in. Ensure override data is captured and analyzed — every human override is a signal about where your AI needs improvement.",
        "source": "McKinsey: '65% of high performers have defined HITL processes vs. 23% of others.'",
    },
]

READINESS_LEVELS = [
    (0, 14, "Not Ready", "🔴", "Significant gaps in AI adoption readiness. Focus on foundational patterns (1, 2, 4) before investing in AI tools."),
    (15, 21, "Partially Ready", "🟡", "Some foundations in place but critical gaps remain. Address low-scoring patterns before scaling AI."),
    (22, 28, "Ready", "🟢", "Strong foundation for AI adoption. Focus on depth (Pattern 5) and learning (Pattern 6) to maximize value."),
    (29, 35, "Highly Ready", "🔵", "Excellent readiness. You're positioned to be in the successful 5%. Focus on continuous improvement and knowledge sharing."),
]

LOG_PATH = Path(__file__).parent / "logs"


def get_readiness_level(score):
    for low, high, label, emoji, description in READINESS_LEVELS:
        if low <= score <= high:
            return {"label": label, "emoji": emoji, "description": description}
    return {"label": "Unknown", "emoji": "⚪", "description": ""}


def log_assessment(scores, total, level):
    LOG_PATH.mkdir(exist_ok=True)
    log_file = LOG_PATH / "assessments.csv"
    write_header = not log_file.exists()
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "total_score", "level"] + [f"p{p['id']}" for p in PATTERNS])
        writer.writerow([datetime.datetime.now().isoformat(), total, level] + scores)


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------


def main():
    st.set_page_config(page_title="AI Adoption Readiness", layout="wide")
    st.title("AI Adoption Readiness Diagnostic")
    st.caption(
        "Based on 7 success patterns from Stanford Enterprise AI Playbook (51 cases) "
        "and MIT NANDA GenAI Divide report. Assess your team's readiness for AI adoption."
    )

    st.markdown("### Rate each pattern for your team (1 = Not at all, 5 = Fully in place)")

    scores = []
    for pattern in PATTERNS:
        st.markdown(f"---")
        st.markdown(f"#### Pattern {pattern['id']}: {pattern['name']}")
        st.markdown(f"*{pattern['description']}*")
        score = st.slider(
            pattern["question"],
            1, 5, 3,
            key=f"pattern_{pattern['id']}",
        )
        scores.append(score)

    st.markdown("---")

    if st.button("Get Readiness Assessment", type="primary"):
        total = sum(scores)
        level = get_readiness_level(total)

        # Overall score
        st.markdown(f"## {level['emoji']} Readiness: {level['label']} ({total}/35)")
        st.markdown(f"**{level['description']}**")

        # Per-pattern analysis
        st.markdown("### Pattern-by-Pattern Analysis")

        gaps = []
        strengths = []
        for pattern, score in zip(PATTERNS, scores):
            if score <= 2:
                gaps.append((pattern, score))
            elif score >= 4:
                strengths.append((pattern, score))

        if gaps:
            st.markdown("#### 🔴 Critical Gaps (address first)")
            for pattern, score in gaps:
                with st.expander(f"Pattern {pattern['id']}: {pattern['name']} — Score: {score}/5"):
                    st.warning(pattern["low_guidance"])
                    st.caption(pattern["source"])

        if strengths:
            st.markdown("#### 🟢 Strengths (maintain and leverage)")
            for pattern, score in strengths:
                with st.expander(f"Pattern {pattern['id']}: {pattern['name']} — Score: {score}/5"):
                    st.success(pattern["high_guidance"])

        # Action plan
        st.markdown("### Recommended Action Plan")
        sorted_patterns = sorted(zip(PATTERNS, scores), key=lambda x: x[1])
        for i, (pattern, score) in enumerate(sorted_patterns[:3], 1):
            guidance = pattern["low_guidance"] if score <= 3 else pattern["high_guidance"]
            st.markdown(f"**Priority {i}**: {pattern['name']} (current: {score}/5)")
            st.markdown(f"> {guidance}")

        # Visualization
        st.markdown("### Score Profile")
        import pandas as pd
        chart_data = pd.DataFrame({
            "Pattern": [f"P{p['id']}: {p['name']}" for p in PATTERNS],
            "Score": scores,
        })
        st.bar_chart(chart_data.set_index("Pattern"))

        # Log
        log_assessment(scores, total, level["label"])

    # Research context
    with st.expander("About This Tool"):
        st.markdown("""
### Research Basis

These 7 patterns are synthesized from:

1. **Stanford Digital Economy Lab (2026)**: "Enterprise AI Playbook: Lessons from 51 Successful Deployments"
   — Pereira, Graylin & Brynjolfsson

2. **MIT Project NANDA (2025)**: "The GenAI Divide: State of AI in Business 2025"
   — 150 leader interviews, 350-employee survey, 300 public AI deployments

3. **McKinsey State of AI (2025)**: High-performer vs. low-performer analysis

4. **Gartner (2025)**: "Over 40% of Agentic AI Projects Will Be Canceled by 2027"

### Validation Status

This tool is part of an ongoing validation study (P4 in the prototyping research plan).
It requires empirical validation through:
- Retrospective survey of 20+ teams (do higher scores correlate with success?)
- Prospective pilot with 3 teams (does using the checklist improve outcomes?)
        """)


if __name__ == "__main__":
    main()
