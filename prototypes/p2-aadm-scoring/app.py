"""
P2: AI-Augmented Decision Matrix (AADM) Scoring Tool
Scores product decisions on D/R/S dimensions and recommends AI role.

Usage:
    pip install streamlit pandas
    streamlit run app.py
"""

import csv
import datetime
import json
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# AADM Engine
# ---------------------------------------------------------------------------

AI_ROLES = {
    "ai_decides": {
        "label": "AI Decides",
        "emoji": "🟢",
        "description": "AI acts autonomously; human monitors outcomes.",
        "examples": "Automated A/B test routing, feature flag rollout, anomaly alerts",
    },
    "ai_recommends": {
        "label": "AI Recommends",
        "emoji": "🔵",
        "description": "AI provides scored recommendation; human approves or overrides.",
        "examples": "AI-PRISM gate scoring, backlog prioritization, pricing suggestions",
    },
    "ai_informs": {
        "label": "AI Informs",
        "emoji": "🟡",
        "description": "AI provides data and analysis; human synthesizes and decides.",
        "examples": "Market analysis, competitive intelligence, user segmentation",
    },
    "ai_assists": {
        "label": "AI Assists",
        "emoji": "🟠",
        "description": "AI generates options or variations; human directs and curates.",
        "examples": "Design variations, copy alternatives, scenario generation",
    },
    "ai_absent": {
        "label": "AI Absent",
        "emoji": "🔴",
        "description": "Human leads entirely; AI has no meaningful role.",
        "examples": "Strategic vision, ethical boundaries, stakeholder negotiations",
    },
}


def score_to_role(d: int, r: int, s: int) -> dict:
    """Map D/R/S scores (1-5 each) to an AI role."""

    # High data + high reversibility + high objectivity → AI Decides
    if d >= 4 and r >= 4 and s >= 4:
        return {"role": "ai_decides", "confidence": 0.9}

    # High data + low reversibility + high objectivity → AI Recommends
    if d >= 4 and s >= 4:
        return {"role": "ai_recommends", "confidence": 0.85}

    # High data + any reversibility + medium objectivity → AI Recommends
    if d >= 4 and s >= 3:
        return {"role": "ai_recommends", "confidence": 0.75}

    # Medium data + medium all → AI Informs
    if d >= 3 and s >= 2:
        return {"role": "ai_informs", "confidence": 0.7}

    # Low subjectivity (creative) + any data → AI Assists
    if s <= 2 and d >= 2:
        return {"role": "ai_assists", "confidence": 0.7}

    # Low subjectivity + low data → AI Assists (generate options)
    if s <= 2:
        return {"role": "ai_assists", "confidence": 0.6}

    # Low data + low reversibility + low objectivity → AI Absent
    if d <= 2 and r <= 2 and s <= 2:
        return {"role": "ai_absent", "confidence": 0.85}

    # Low data + low reversibility → AI Absent
    if d <= 2 and r <= 2:
        return {"role": "ai_absent", "confidence": 0.7}

    # Default: AI Informs
    return {"role": "ai_informs", "confidence": 0.5}


# ---------------------------------------------------------------------------
# Scenario Data
# ---------------------------------------------------------------------------

SCENARIOS = [
    {"id": 1, "phase": "Discovery", "decision": "Which customer problem to pursue next?", "suggested_d": 2, "suggested_r": 1, "suggested_s": 2},
    {"id": 2, "phase": "Discovery", "decision": "Which customer segment shows highest potential based on survey data?", "suggested_d": 4, "suggested_r": 3, "suggested_s": 4},
    {"id": 3, "phase": "Discovery", "decision": "Should we collect biometric data for personalization?", "suggested_d": 2, "suggested_r": 1, "suggested_s": 1},
    {"id": 4, "phase": "Design", "decision": "Which of 5 design directions to pursue?", "suggested_d": 2, "suggested_r": 3, "suggested_s": 1},
    {"id": 5, "phase": "Design", "decision": "Does the new checkout flow meet accessibility standards?", "suggested_d": 4, "suggested_r": 4, "suggested_s": 5},
    {"id": 6, "phase": "Design", "decision": "Which illustration style fits our brand better?", "suggested_d": 1, "suggested_r": 3, "suggested_s": 1},
    {"id": 7, "phase": "Development", "decision": "Microservices vs monolith for the new service?", "suggested_d": 3, "suggested_r": 1, "suggested_s": 3},
    {"id": 8, "phase": "Development", "decision": "Should we use the AI-generated code or rewrite manually?", "suggested_d": 4, "suggested_r": 4, "suggested_s": 4},
    {"id": 9, "phase": "Development", "decision": "Build, buy, or partner for recommendation engine?", "suggested_d": 3, "suggested_r": 2, "suggested_s": 3},
    {"id": 10, "phase": "Testing", "decision": "Is the test suite comprehensive enough to ship?", "suggested_d": 5, "suggested_r": 3, "suggested_s": 5},
    {"id": 11, "phase": "Testing", "decision": "Ship with 3 known bugs or delay launch 2 weeks?", "suggested_d": 4, "suggested_r": 2, "suggested_s": 3},
    {"id": 12, "phase": "Testing", "decision": "Should AI-generated tests replace manual test cases?", "suggested_d": 4, "suggested_r": 3, "suggested_s": 4},
    {"id": 13, "phase": "Launch", "decision": "Launch this quarter or wait for the next?", "suggested_d": 3, "suggested_r": 1, "suggested_s": 2},
    {"id": 14, "phase": "Launch", "decision": "Set price at $29/mo or $49/mo for enterprise?", "suggested_d": 4, "suggested_r": 3, "suggested_s": 3},
    {"id": 15, "phase": "Launch", "decision": "Soft launch in 2 markets or full global launch?", "suggested_d": 3, "suggested_r": 2, "suggested_s": 2},
    {"id": 16, "phase": "Growth", "decision": "Which of 4 experiment variants shows best conversion?", "suggested_d": 5, "suggested_r": 5, "suggested_s": 5},
    {"id": 17, "phase": "Growth", "decision": "Should we sunset the legacy product?", "suggested_d": 4, "suggested_r": 1, "suggested_s": 2},
    {"id": 18, "phase": "Growth", "decision": "Double down on feature A or pivot to feature B?", "suggested_d": 3, "suggested_r": 1, "suggested_s": 2},
    {"id": 19, "phase": "Growth", "decision": "Optimize recommendation algorithm for engagement or revenue?", "suggested_d": 4, "suggested_r": 3, "suggested_s": 3},
    {"id": 20, "phase": "Growth", "decision": "Is the AI recommendation showing bias across demographics?", "suggested_d": 4, "suggested_r": 2, "suggested_s": 1},
    {"id": 21, "phase": "Discovery", "decision": "Validate product-market fit with synthetic user research?", "suggested_d": 3, "suggested_r": 3, "suggested_s": 3},
    {"id": 22, "phase": "Design", "decision": "Use generative AI for all marketing copy?", "suggested_d": 3, "suggested_r": 4, "suggested_s": 2},
    {"id": 23, "phase": "Development", "decision": "Accept AI-suggested architecture refactoring?", "suggested_d": 4, "suggested_r": 2, "suggested_s": 4},
    {"id": 24, "phase": "Testing", "decision": "Trust AI-generated load test results without manual verification?", "suggested_d": 5, "suggested_r": 3, "suggested_s": 4},
    {"id": 25, "phase": "Launch", "decision": "Let AI agent handle tier-1 customer support from day 1?", "suggested_d": 3, "suggested_r": 2, "suggested_s": 2},
    {"id": 26, "phase": "Discovery", "decision": "Use LLM to synthesize 500 interview transcripts?", "suggested_d": 4, "suggested_r": 4, "suggested_s": 3},
    {"id": 27, "phase": "Design", "decision": "Allow AI to auto-personalize UI per user segment?", "suggested_d": 4, "suggested_r": 4, "suggested_s": 3},
    {"id": 28, "phase": "Launch", "decision": "Respond to competitor's surprise product launch?", "suggested_d": 2, "suggested_r": 1, "suggested_s": 2},
    {"id": 29, "phase": "Growth", "decision": "Raise prices 20% based on value metric analysis?", "suggested_d": 4, "suggested_r": 2, "suggested_s": 3},
    {"id": 30, "phase": "Development", "decision": "Open-source the internal utility library?", "suggested_d": 2, "suggested_r": 1, "suggested_s": 2},
]

LOG_PATH = Path(__file__).parent / "logs"


def log_scoring(decision, d, r, s, result):
    LOG_PATH.mkdir(exist_ok=True)
    log_file = LOG_PATH / "aadm_scores.csv"
    write_header = not log_file.exists()
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "decision", "D", "R", "S", "role", "confidence"])
        writer.writerow([
            datetime.datetime.now().isoformat(),
            decision, d, r, s, result["role"], result["confidence"],
        ])


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------


def main():
    st.set_page_config(page_title="AADM Scoring Tool", layout="wide")
    st.title("AI-Augmented Decision Matrix (AADM)")
    st.caption(
        "Score product decisions on three dimensions to determine the appropriate AI role. "
        "Based on the AADM framework (ai4-product, 2026)."
    )

    tab1, tab2 = st.tabs(["Score a Decision", "Scenario Library (30)"])

    # --- Tab 1: Interactive scoring ---
    with tab1:
        decision = st.text_area(
            "Describe the product decision",
            placeholder="e.g., Should we launch in Japan this quarter or wait for localization?",
        )

        st.markdown("### Score Three Dimensions")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**D — Data Availability**")
            st.caption("How much structured data informs this decision?")
            d = st.slider("D score", 1, 5, 3, key="d",
                          help="1=Almost none (pure intuition) → 5=Rich (extensive metrics)")

        with col2:
            st.markdown("**R — Reversibility**")
            st.caption("How easily can this decision be reversed?")
            r = st.slider("R score", 1, 5, 3, key="r",
                          help="1=Irreversible (kill product) → 5=Easily reversible (feature flag)")

        with col3:
            st.markdown("**S — Subjectivity**")
            st.caption("How objective vs. subjective is this decision?")
            s = st.slider("S score", 1, 5, 3, key="s",
                          help="1=Highly subjective (creative direction) → 5=Highly objective (pass/fail)")

        if st.button("Get AI Role Recommendation", type="primary"):
            result = score_to_role(d, r, s)
            role_info = AI_ROLES[result["role"]]

            st.markdown("---")
            st.markdown(f"## {role_info['emoji']} {role_info['label']}")
            st.markdown(f"**{role_info['description']}**")
            st.markdown(f"Examples: {role_info['examples']}")
            st.metric("Confidence", f"{result['confidence']:.0%}")

            # Visual position
            st.markdown("### Decision Profile")
            profile_col1, profile_col2, profile_col3 = st.columns(3)
            profile_col1.metric("Data (D)", f"{d}/5", help="Higher = more data available")
            profile_col2.metric("Reversibility (R)", f"{r}/5", help="Higher = easier to undo")
            profile_col3.metric("Subjectivity (S)", f"{s}/5", help="Higher = more objective")

            if decision:
                log_scoring(decision, d, r, s, result)

    # --- Tab 2: Scenario library ---
    with tab2:
        st.markdown("### 30 Pre-Built Decision Scenarios")
        st.caption("Use these for inter-rater reliability studies (Phase A of evaluation plan).")

        phase_filter = st.selectbox("Filter by phase", ["All"] + sorted(set(s["phase"] for s in SCENARIOS)))

        filtered = SCENARIOS if phase_filter == "All" else [s for s in SCENARIOS if s["phase"] == phase_filter]

        for scenario in filtered:
            with st.expander(f"#{scenario['id']} [{scenario['phase']}] {scenario['decision']}"):
                sc1, sc2, sc3 = st.columns(3)
                sd = sc1.slider("D", 1, 5, scenario["suggested_d"], key=f"sd_{scenario['id']}")
                sr = sc2.slider("R", 1, 5, scenario["suggested_r"], key=f"sr_{scenario['id']}")
                ss = sc3.slider("S", 1, 5, scenario["suggested_s"], key=f"ss_{scenario['id']}")

                result = score_to_role(sd, sr, ss)
                role_info = AI_ROLES[result["role"]]
                st.markdown(f"**{role_info['emoji']} {role_info['label']}** — {role_info['description']}")

                # Show suggested vs user scores
                if (sd, sr, ss) != (scenario["suggested_d"], scenario["suggested_r"], scenario["suggested_s"]):
                    suggested_result = score_to_role(
                        scenario["suggested_d"], scenario["suggested_r"], scenario["suggested_s"]
                    )
                    suggested_info = AI_ROLES[suggested_result["role"]]
                    st.caption(
                        f"Suggested scores: D={scenario['suggested_d']}, "
                        f"R={scenario['suggested_r']}, S={scenario['suggested_s']} "
                        f"→ {suggested_info['label']}"
                    )

        # Export for reliability study
        if st.button("Export Scenarios as CSV"):
            rows = []
            for s in SCENARIOS:
                result = score_to_role(s["suggested_d"], s["suggested_r"], s["suggested_s"])
                rows.append({
                    "id": s["id"], "phase": s["phase"], "decision": s["decision"],
                    "suggested_D": s["suggested_d"], "suggested_R": s["suggested_r"],
                    "suggested_S": s["suggested_s"], "suggested_role": AI_ROLES[result["role"]]["label"],
                })
            import pandas as pd
            df = pd.DataFrame(rows)
            st.download_button("Download", df.to_csv(index=False), "aadm_scenarios.csv")


if __name__ == "__main__":
    main()
