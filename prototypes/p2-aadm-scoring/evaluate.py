"""
P2 Evaluation: Analyze 30 scenario scoring distribution, role coverage,
boundary sensitivity, and edge cases.

Usage:
    python evaluate.py
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Inline AADM engine (avoid streamlit dependency)
# ---------------------------------------------------------------------------

AI_ROLES = {
    "ai_decides": "AI Decides",
    "ai_recommends": "AI Recommends",
    "ai_informs": "AI Informs",
    "ai_assists": "AI Assists",
    "ai_absent": "AI Absent",
}


def score_to_role(d, r, s):
    if d <= 2 and r <= 2:
        return {"role": "ai_absent", "confidence": 0.85}
    if d <= 2 and s <= 2:
        return {"role": "ai_absent", "confidence": 0.75}
    if d >= 4 and r >= 4 and s >= 4:
        return {"role": "ai_decides", "confidence": 0.9}
    if d >= 4 and s >= 4:
        return {"role": "ai_recommends", "confidence": 0.85}
    if d >= 4 and s >= 3:
        return {"role": "ai_recommends", "confidence": 0.75}
    if s <= 2:
        return {"role": "ai_assists", "confidence": 0.7}
    if d >= 3 and s >= 2:
        return {"role": "ai_informs", "confidence": 0.7}
    return {"role": "ai_informs", "confidence": 0.5}


SCENARIOS = [
    {"id": 1, "phase": "Discovery", "decision": "Which customer problem to pursue next?", "d": 2, "r": 1, "s": 2},
    {"id": 2, "phase": "Discovery", "decision": "Which customer segment shows highest potential?", "d": 4, "r": 3, "s": 4},
    {"id": 3, "phase": "Discovery", "decision": "Should we collect biometric data for personalization?", "d": 2, "r": 1, "s": 1},
    {"id": 4, "phase": "Design", "decision": "Which of 5 design directions to pursue?", "d": 2, "r": 3, "s": 1},
    {"id": 5, "phase": "Design", "decision": "Does checkout flow meet accessibility standards?", "d": 4, "r": 4, "s": 5},
    {"id": 6, "phase": "Design", "decision": "Which illustration style fits our brand better?", "d": 1, "r": 3, "s": 1},
    {"id": 7, "phase": "Development", "decision": "Microservices vs monolith for the new service?", "d": 3, "r": 1, "s": 3},
    {"id": 8, "phase": "Development", "decision": "Use AI-generated code or rewrite manually?", "d": 4, "r": 4, "s": 4},
    {"id": 9, "phase": "Development", "decision": "Build, buy, or partner for recommendation engine?", "d": 3, "r": 2, "s": 3},
    {"id": 10, "phase": "Testing", "decision": "Is test suite comprehensive enough to ship?", "d": 5, "r": 3, "s": 5},
    {"id": 11, "phase": "Testing", "decision": "Ship with 3 known bugs or delay 2 weeks?", "d": 4, "r": 2, "s": 3},
    {"id": 12, "phase": "Testing", "decision": "Should AI-generated tests replace manual test cases?", "d": 4, "r": 3, "s": 4},
    {"id": 13, "phase": "Launch", "decision": "Launch this quarter or wait for the next?", "d": 3, "r": 1, "s": 2},
    {"id": 14, "phase": "Launch", "decision": "Set price at $29/mo or $49/mo for enterprise?", "d": 4, "r": 3, "s": 3},
    {"id": 15, "phase": "Launch", "decision": "Soft launch in 2 markets or full global launch?", "d": 3, "r": 2, "s": 2},
    {"id": 16, "phase": "Growth", "decision": "Which of 4 experiment variants shows best conversion?", "d": 5, "r": 5, "s": 5},
    {"id": 17, "phase": "Growth", "decision": "Should we sunset the legacy product?", "d": 4, "r": 1, "s": 2},
    {"id": 18, "phase": "Growth", "decision": "Double down on feature A or pivot to feature B?", "d": 3, "r": 1, "s": 2},
    {"id": 19, "phase": "Growth", "decision": "Optimize recommendation for engagement or revenue?", "d": 4, "r": 3, "s": 3},
    {"id": 20, "phase": "Growth", "decision": "Is AI recommendation showing bias across demographics?", "d": 4, "r": 2, "s": 1},
    {"id": 21, "phase": "Discovery", "decision": "Validate product-market fit with synthetic user research?", "d": 3, "r": 3, "s": 3},
    {"id": 22, "phase": "Design", "decision": "Use generative AI for all marketing copy?", "d": 3, "r": 4, "s": 2},
    {"id": 23, "phase": "Development", "decision": "Accept AI-suggested architecture refactoring?", "d": 4, "r": 2, "s": 4},
    {"id": 24, "phase": "Testing", "decision": "Trust AI-generated load test results without manual verification?", "d": 5, "r": 3, "s": 4},
    {"id": 25, "phase": "Launch", "decision": "Let AI agent handle tier-1 support from day 1?", "d": 3, "r": 2, "s": 2},
    {"id": 26, "phase": "Discovery", "decision": "Use LLM to synthesize 500 interview transcripts?", "d": 4, "r": 4, "s": 3},
    {"id": 27, "phase": "Design", "decision": "Allow AI to auto-personalize UI per user segment?", "d": 4, "r": 4, "s": 3},
    {"id": 28, "phase": "Launch", "decision": "Respond to competitor's surprise product launch?", "d": 2, "r": 1, "s": 2},
    {"id": 29, "phase": "Growth", "decision": "Raise prices 20% based on value metric analysis?", "d": 4, "r": 2, "s": 3},
    {"id": 30, "phase": "Development", "decision": "Open-source the internal utility library?", "d": 2, "r": 1, "s": 2},
]


def evaluate():
    print("=" * 70)
    print("P2 EVALUATION REPORT: AADM Scoring Analysis on 30 Scenarios")
    print("=" * 70)

    # 1. Role distribution
    role_counts = Counter()
    phase_roles = defaultdict(Counter)
    results = []

    for s in SCENARIOS:
        result = score_to_role(s["d"], s["r"], s["s"])
        role = result["role"]
        role_counts[role] += 1
        phase_roles[s["phase"]][role] += 1
        results.append({**s, "role": role, "confidence": result["confidence"]})

    print(f"\n## Role Distribution (n=30)")
    print(f"{'Role':<20} {'Count':>5} {'Pct':>6}")
    print("-" * 32)
    for role in ["ai_decides", "ai_recommends", "ai_informs", "ai_assists", "ai_absent"]:
        count = role_counts[role]
        print(f"{AI_ROLES[role]:<20} {count:>5} {count / 30:>5.0%}")

    # 2. Per-phase distribution
    print(f"\n## Per-Phase Role Distribution")
    phases = ["Discovery", "Design", "Development", "Testing", "Launch", "Growth"]
    header = f"{'Phase':<14}" + "".join(f"{AI_ROLES[r]:>16}" for r in ["ai_decides", "ai_recommends", "ai_informs", "ai_assists", "ai_absent"])
    print(header)
    print("-" * 94)
    for phase in phases:
        row = f"{phase:<14}"
        for role in ["ai_decides", "ai_recommends", "ai_informs", "ai_assists", "ai_absent"]:
            row += f"{phase_roles[phase][role]:>16}"
        print(row)

    # 3. Boundary sensitivity
    print(f"\n## Boundary Sensitivity Analysis")
    print("Testing how ±1 on each dimension changes the role...")
    sensitive_cases = []
    for s in SCENARIOS:
        base_role = score_to_role(s["d"], s["r"], s["s"])["role"]
        for dim, key in [("D", "d"), ("R", "r"), ("S", "s")]:
            for delta in [-1, 1]:
                new_val = s[key] + delta
                if 1 <= new_val <= 5:
                    new_scores = {"d": s["d"], "r": s["r"], "s": s["s"]}
                    new_scores[key] = new_val
                    new_role = score_to_role(new_scores["d"], new_scores["r"], new_scores["s"])["role"]
                    if new_role != base_role:
                        sensitive_cases.append({
                            "id": s["id"],
                            "decision": s["decision"][:50],
                            "change": f"{dim} {s[key]}→{new_val}",
                            "from": AI_ROLES[base_role],
                            "to": AI_ROLES[new_role],
                        })

    print(f"\nFound {len(sensitive_cases)} boundary-sensitive changes:")
    print(f"{'ID':>3} {'Decision':<50} {'Change':<10} {'From':<16} {'To':<16}")
    print("-" * 96)
    for c in sensitive_cases[:15]:
        print(f"{c['id']:>3} {c['decision']:<50} {c['change']:<10} {c['from']:<16} {c['to']:<16}")
    if len(sensitive_cases) > 15:
        print(f"... and {len(sensitive_cases) - 15} more")

    # 4. Confidence distribution
    print(f"\n## Confidence Distribution")
    confs = [r["confidence"] for r in results]
    conf_buckets = Counter()
    for c in confs:
        if c >= 0.85:
            conf_buckets["High (≥0.85)"] += 1
        elif c >= 0.7:
            conf_buckets["Medium (0.7-0.84)"] += 1
        else:
            conf_buckets["Low (<0.7)"] += 1

    for bucket in ["High (≥0.85)", "Medium (0.7-0.84)", "Low (<0.7)"]:
        print(f"  {bucket}: {conf_buckets[bucket]} scenarios")

    # 5. Face validity check
    print(f"\n## Face Validity Spot Check")
    spot_checks = [
        (16, "A/B test variant selection", "ai_decides", "Data-rich + reversible + objective → autonomous"),
        (1, "Which problem to pursue", "ai_absent", "Low data + irreversible + subjective → human only"),
        (4, "Design direction choice", "ai_assists", "Low objectivity → AI generates, human curates"),
        (14, "Enterprise pricing", "ai_recommends", "Good data + moderate reversibility → AI recommends"),
        (20, "AI bias assessment", "ai_assists", "Low subjectivity (ethical) despite high data → human judgment needed"),
    ]
    all_pass = True
    for sid, desc, expected, rationale in spot_checks:
        actual = next(r for r in results if r["id"] == sid)
        status = "PASS" if actual["role"] == expected else "FAIL"
        if status == "FAIL":
            all_pass = False
        print(f"  [{status}] #{sid} {desc}")
        print(f"         Expected: {AI_ROLES[expected]}, Got: {AI_ROLES[actual['role']]}")
        print(f"         Rationale: {rationale}")

    # Save report
    report = {
        "role_distribution": dict(role_counts),
        "phase_roles": {p: dict(c) for p, c in phase_roles.items()},
        "boundary_sensitive_count": len(sensitive_cases),
        "boundary_cases": sensitive_cases,
        "confidence_distribution": dict(conf_buckets),
        "face_validity_pass": all_pass,
        "results": results,
    }

    report_path = Path(__file__).parent / "evaluation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nFull report saved to: {report_path}")

    return report


if __name__ == "__main__":
    evaluate()
