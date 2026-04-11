"""
P2: AI-Augmented Decision Matrix (AADM) v2 Scoring Tool
4-dimension model: D (Data), R (Reversibility), S (Subjectivity), C (Creativity)
With borderline detection.

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
# AADM v2 Engine
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
        "label": "AI Assists (Creative)",
        "emoji": "🟠",
        "description": "AI generates variations and options; human directs and curates.",
        "examples": "Design variations, copy alternatives, ideation, scenario generation",
    },
    "ai_absent": {
        "label": "AI Absent",
        "emoji": "🔴",
        "description": "Human leads entirely; AI has no meaningful role.",
        "examples": "Strategic vision, ethical boundaries, stakeholder negotiations",
    },
}


def score_to_role(d: int, r: int, s: int, c: int) -> dict:
    """Map D/R/S/C scores (1-5 each) to an AI role.

    C (Creativity) resolves the v1 conflict where low-D/low-S creative tasks
    were mapped to AI Absent instead of AI Assists. Nature meta-analysis shows
    creation is the one task type where Human+AI > either alone.
    """

    # --- AI Absent: low data + irreversible + NOT creative ---
    # Strategic/ethical judgment where AI has no role
    if d <= 2 and r <= 2 and c <= 2:
        return {"role": "ai_absent", "confidence": 0.9}

    if d <= 2 and s <= 2 and c <= 2:
        return {"role": "ai_absent", "confidence": 0.8}

    # --- AI Assists: creative tasks (high C) regardless of data/objectivity ---
    # Nature meta-analysis: creation tasks are where Human+AI excels
    if c >= 4:
        return {"role": "ai_assists", "confidence": 0.85}

    if c >= 3 and s <= 2:
        return {"role": "ai_assists", "confidence": 0.75}

    # --- AI Decides: high data + reversible + objective + not creative ---
    if d >= 4 and r >= 4 and s >= 4 and c <= 2:
        return {"role": "ai_decides", "confidence": 0.9}

    if d >= 4 and r >= 4 and s >= 4:
        return {"role": "ai_decides", "confidence": 0.8}

    # --- AI Recommends: high data + objective ---
    if d >= 4 and s >= 4:
        return {"role": "ai_recommends", "confidence": 0.85}

    if d >= 4 and s >= 3:
        return {"role": "ai_recommends", "confidence": 0.75}

    # --- AI Assists: moderate creativity ---
    if c >= 3:
        return {"role": "ai_assists", "confidence": 0.65}

    # --- AI Absent: low data + low reversibility (non-creative) ---
    if d <= 2 and r <= 2:
        return {"role": "ai_absent", "confidence": 0.7}

    # --- AI Informs: medium data + medium objectivity ---
    if d >= 3 and s >= 2:
        return {"role": "ai_informs", "confidence": 0.7}

    # Default
    return {"role": "ai_informs", "confidence": 0.5}


def detect_borderline(d: int, r: int, s: int, c: int) -> dict:
    """Check if ±1 on any dimension changes the role."""
    base_role = score_to_role(d, r, s, c)["role"]
    alternatives = set()

    for dim_name, dim_val, setter in [
        ("D", d, lambda v: (v, r, s, c)),
        ("R", r, lambda v: (d, v, s, c)),
        ("S", s, lambda v: (d, r, v, c)),
        ("C", c, lambda v: (d, r, s, v)),
    ]:
        for delta in [-1, 1]:
            new_val = dim_val + delta
            if 1 <= new_val <= 5:
                new_role = score_to_role(*setter(new_val))["role"]
                if new_role != base_role:
                    alternatives.add((dim_name, delta, new_role))

    return {
        "is_borderline": len(alternatives) > 0,
        "alternatives": [
            {"dimension": a[0], "change": f"{'+' if a[1] > 0 else ''}{a[1]}", "would_become": AI_ROLES[a[2]]["label"]}
            for a in sorted(alternatives)
        ],
    }


# ---------------------------------------------------------------------------
# Scenario Data (updated with C dimension)
# ---------------------------------------------------------------------------

SCENARIOS = [
    {"id": 1, "phase": "Discovery", "decision": "Which customer problem to pursue next?", "d": 2, "r": 1, "s": 2, "c": 1},
    {"id": 2, "phase": "Discovery", "decision": "Which customer segment shows highest potential?", "d": 4, "r": 3, "s": 4, "c": 1},
    {"id": 3, "phase": "Discovery", "decision": "Should we collect biometric data for personalization?", "d": 2, "r": 1, "s": 1, "c": 1},
    {"id": 4, "phase": "Design", "decision": "Which of 5 design directions to pursue?", "d": 2, "r": 3, "s": 1, "c": 5},
    {"id": 5, "phase": "Design", "decision": "Does checkout flow meet accessibility standards?", "d": 4, "r": 4, "s": 5, "c": 1},
    {"id": 6, "phase": "Design", "decision": "Which illustration style fits our brand better?", "d": 1, "r": 3, "s": 1, "c": 5},
    {"id": 7, "phase": "Development", "decision": "Microservices vs monolith for the new service?", "d": 3, "r": 1, "s": 3, "c": 1},
    {"id": 8, "phase": "Development", "decision": "Use AI-generated code or rewrite manually?", "d": 4, "r": 4, "s": 4, "c": 1},
    {"id": 9, "phase": "Development", "decision": "Build, buy, or partner for recommendation engine?", "d": 3, "r": 2, "s": 3, "c": 1},
    {"id": 10, "phase": "Testing", "decision": "Is test suite comprehensive enough to ship?", "d": 5, "r": 3, "s": 5, "c": 1},
    {"id": 11, "phase": "Testing", "decision": "Ship with 3 known bugs or delay 2 weeks?", "d": 4, "r": 2, "s": 3, "c": 1},
    {"id": 12, "phase": "Testing", "decision": "Should AI-generated tests replace manual test cases?", "d": 4, "r": 3, "s": 4, "c": 1},
    {"id": 13, "phase": "Launch", "decision": "Launch this quarter or wait for the next?", "d": 3, "r": 1, "s": 2, "c": 1},
    {"id": 14, "phase": "Launch", "decision": "Set price at $29/mo or $49/mo for enterprise?", "d": 4, "r": 3, "s": 3, "c": 1},
    {"id": 15, "phase": "Launch", "decision": "Soft launch in 2 markets or full global launch?", "d": 3, "r": 2, "s": 2, "c": 1},
    {"id": 16, "phase": "Growth", "decision": "Which of 4 experiment variants shows best conversion?", "d": 5, "r": 5, "s": 5, "c": 1},
    {"id": 17, "phase": "Growth", "decision": "Should we sunset the legacy product?", "d": 4, "r": 1, "s": 2, "c": 1},
    {"id": 18, "phase": "Growth", "decision": "Double down on feature A or pivot to feature B?", "d": 3, "r": 1, "s": 2, "c": 1},
    {"id": 19, "phase": "Growth", "decision": "Optimize recommendation for engagement or revenue?", "d": 4, "r": 3, "s": 3, "c": 1},
    {"id": 20, "phase": "Growth", "decision": "Is AI recommendation showing bias across demographics?", "d": 4, "r": 2, "s": 1, "c": 1},
    {"id": 21, "phase": "Discovery", "decision": "Validate product-market fit with synthetic user research?", "d": 3, "r": 3, "s": 3, "c": 2},
    {"id": 22, "phase": "Design", "decision": "Use generative AI for all marketing copy?", "d": 3, "r": 4, "s": 2, "c": 4},
    {"id": 23, "phase": "Development", "decision": "Accept AI-suggested architecture refactoring?", "d": 4, "r": 2, "s": 4, "c": 1},
    {"id": 24, "phase": "Testing", "decision": "Trust AI-generated load test results without manual verification?", "d": 5, "r": 3, "s": 4, "c": 1},
    {"id": 25, "phase": "Launch", "decision": "Let AI agent handle tier-1 support from day 1?", "d": 3, "r": 2, "s": 2, "c": 1},
    {"id": 26, "phase": "Discovery", "decision": "Use LLM to synthesize 500 interview transcripts?", "d": 4, "r": 4, "s": 3, "c": 2},
    {"id": 27, "phase": "Design", "decision": "Allow AI to auto-personalize UI per user segment?", "d": 4, "r": 4, "s": 3, "c": 3},
    {"id": 28, "phase": "Launch", "decision": "Respond to competitor's surprise product launch?", "d": 2, "r": 1, "s": 2, "c": 1},
    {"id": 29, "phase": "Growth", "decision": "Raise prices 20% based on value metric analysis?", "d": 4, "r": 2, "s": 3, "c": 1},
    {"id": 30, "phase": "Development", "decision": "Open-source the internal utility library?", "d": 2, "r": 1, "s": 2, "c": 1},
]

LOG_PATH = Path(__file__).parent / "logs"


def log_scoring(decision, d, r, s, c, result):
    LOG_PATH.mkdir(exist_ok=True)
    log_file = LOG_PATH / "aadm_v2_scores.csv"
    write_header = not log_file.exists()
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "decision", "D", "R", "S", "C", "role", "confidence", "borderline"])
        border = detect_borderline(d, r, s, c)
        writer.writerow([
            datetime.datetime.now().isoformat(),
            decision, d, r, s, c, result["role"], result["confidence"], border["is_borderline"],
        ])


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------


def main():
    st.set_page_config(page_title="AADM v2 Scoring Tool", layout="wide")
    st.title("AI-Augmented Decision Matrix (AADM) v2")
    st.caption(
        "Score product decisions on **four dimensions** to determine the appropriate AI role. "
        "v2 adds Creativity (C) to resolve the creation-task gap identified in simulation studies."
    )

    tab1, tab2 = st.tabs(["Score a Decision", "Scenario Library (30)"])

    with tab1:
        decision = st.text_area(
            "Describe the product decision",
            placeholder="e.g., Should we launch in Japan this quarter or wait for localization?",
        )

        st.markdown("### Score Four Dimensions")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("**D — Data Availability**")
            st.caption("How much structured data?")
            d = st.slider("D", 1, 5, 3, key="d",
                          help="1=Pure intuition → 5=Rich metrics")

        with col2:
            st.markdown("**R — Reversibility**")
            st.caption("How easily reversed?")
            r = st.slider("R", 1, 5, 3, key="r",
                          help="1=Irreversible → 5=Feature flag")

        with col3:
            st.markdown("**S — Objectivity**")
            st.caption("How objective vs subjective?")
            s = st.slider("S", 1, 5, 3, key="s",
                          help="1=Highly subjective → 5=Pass/fail")

        with col4:
            st.markdown("**C — Creativity**")
            st.caption("How much creative/generative value?")
            c = st.slider("C", 1, 5, 1, key="c",
                          help="1=No creative element → 5=Primarily creative")

        if st.button("Get AI Role Recommendation", type="primary") and (decision or True):
            result = score_to_role(d, r, s, c)
            role_info = AI_ROLES[result["role"]]
            border = detect_borderline(d, r, s, c)

            st.markdown("---")
            st.markdown(f"## {role_info['emoji']} {role_info['label']}")
            st.markdown(f"**{role_info['description']}**")
            st.markdown(f"Examples: {role_info['examples']}")
            st.metric("Confidence", f"{result['confidence']:.0%}")

            # Borderline warning
            if border["is_borderline"]:
                st.warning(
                    f"**Borderline case.** A ±1 change on some dimensions would change the recommendation:"
                )
                for alt in border["alternatives"]:
                    st.caption(f"  {alt['dimension']} {alt['change']} → {alt['would_become']}")

            # Profile
            st.markdown("### Decision Profile")
            pc1, pc2, pc3, pc4 = st.columns(4)
            pc1.metric("Data (D)", f"{d}/5")
            pc2.metric("Reversibility (R)", f"{r}/5")
            pc3.metric("Objectivity (S)", f"{s}/5")
            pc4.metric("Creativity (C)", f"{c}/5")

            if decision:
                log_scoring(decision, d, r, s, c, result)

    with tab2:
        st.markdown("### 30 Pre-Built Scenarios (with C dimension)")

        phase_filter = st.selectbox("Filter by phase", ["All"] + sorted(set(sc["phase"] for sc in SCENARIOS)))
        filtered = SCENARIOS if phase_filter == "All" else [sc for sc in SCENARIOS if sc["phase"] == phase_filter]

        for scenario in filtered:
            with st.expander(f"#{scenario['id']} [{scenario['phase']}] {scenario['decision']}"):
                c1, c2, c3, c4 = st.columns(4)
                sd = c1.slider("D", 1, 5, scenario["d"], key=f"sd_{scenario['id']}")
                sr = c2.slider("R", 1, 5, scenario["r"], key=f"sr_{scenario['id']}")
                ss = c3.slider("S", 1, 5, scenario["s"], key=f"ss_{scenario['id']}")
                sc_val = c4.slider("C", 1, 5, scenario["c"], key=f"sc_{scenario['id']}")

                result = score_to_role(sd, sr, ss, sc_val)
                role_info = AI_ROLES[result["role"]]
                border = detect_borderline(sd, sr, ss, sc_val)

                st.markdown(f"**{role_info['emoji']} {role_info['label']}** — {role_info['description']}")
                if border["is_borderline"]:
                    st.caption(f"⚠ Borderline: {len(border['alternatives'])} adjacent role(s)")

        if st.button("Export Scenarios as CSV"):
            import pandas as pd
            rows = []
            for sc in SCENARIOS:
                result = score_to_role(sc["d"], sc["r"], sc["s"], sc["c"])
                border = detect_borderline(sc["d"], sc["r"], sc["s"], sc["c"])
                rows.append({
                    "id": sc["id"], "phase": sc["phase"], "decision": sc["decision"],
                    "D": sc["d"], "R": sc["r"], "S": sc["s"], "C": sc["c"],
                    "role": AI_ROLES[result["role"]]["label"],
                    "borderline": border["is_borderline"],
                })
            df = pd.DataFrame(rows)
            st.download_button("Download", df.to_csv(index=False), "aadm_v2_scenarios.csv")


if __name__ == "__main__":
    main()
