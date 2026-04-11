"""
P2 Evaluation v2: Analyze 30 scenarios with D/R/S/C model.

Usage:
    python evaluate.py
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

AI_ROLES = {
    "ai_decides": "AI Decides", "ai_recommends": "AI Recommends",
    "ai_informs": "AI Informs", "ai_assists": "AI Assists", "ai_absent": "AI Absent",
}


def score_to_role(d, r, s, c):
    if d <= 2 and r <= 2 and c <= 2:
        return {"role": "ai_absent", "confidence": 0.9}
    if d <= 2 and s <= 2 and c <= 2:
        return {"role": "ai_absent", "confidence": 0.8}
    if c >= 4:
        return {"role": "ai_assists", "confidence": 0.85}
    if c >= 3 and s <= 2:
        return {"role": "ai_assists", "confidence": 0.75}
    if d >= 4 and r >= 4 and s >= 4 and c <= 2:
        return {"role": "ai_decides", "confidence": 0.9}
    if d >= 4 and r >= 4 and s >= 4:
        return {"role": "ai_decides", "confidence": 0.8}
    if d >= 4 and s >= 4:
        return {"role": "ai_recommends", "confidence": 0.85}
    if d >= 4 and s >= 3:
        return {"role": "ai_recommends", "confidence": 0.75}
    if c >= 3:
        return {"role": "ai_assists", "confidence": 0.65}
    if d <= 2 and r <= 2:
        return {"role": "ai_absent", "confidence": 0.7}
    if d >= 3 and s >= 2:
        return {"role": "ai_informs", "confidence": 0.7}
    return {"role": "ai_informs", "confidence": 0.5}


SCENARIOS = [
    {"id": 1, "phase": "Discovery", "decision": "Which customer problem to pursue next?", "d": 2, "r": 1, "s": 2, "c": 1},
    {"id": 2, "phase": "Discovery", "decision": "Which customer segment shows highest potential?", "d": 4, "r": 3, "s": 4, "c": 1},
    {"id": 3, "phase": "Discovery", "decision": "Should we collect biometric data?", "d": 2, "r": 1, "s": 1, "c": 1},
    {"id": 4, "phase": "Design", "decision": "Which of 5 design directions to pursue?", "d": 2, "r": 3, "s": 1, "c": 5},
    {"id": 5, "phase": "Design", "decision": "Does checkout flow meet accessibility standards?", "d": 4, "r": 4, "s": 5, "c": 1},
    {"id": 6, "phase": "Design", "decision": "Which illustration style fits our brand?", "d": 1, "r": 3, "s": 1, "c": 5},
    {"id": 16, "phase": "Growth", "decision": "Which of 4 experiment variants shows best conversion?", "d": 5, "r": 5, "s": 5, "c": 1},
    {"id": 20, "phase": "Growth", "decision": "Is AI recommendation showing bias?", "d": 4, "r": 2, "s": 1, "c": 1},
]

SPOT_CHECKS = [
    (16, "A/B test variant selection", "ai_decides", "High D+R+S, Low C → autonomous"),
    (1, "Which problem to pursue", "ai_absent", "Low D+R+C → human only"),
    (4, "Design direction choice", "ai_assists", "High C → creative collaboration"),
    (6, "Illustration style", "ai_assists", "High C → creative collaboration"),
    (20, "AI bias assessment", "ai_assists", "Low S but C=1 → needs special handling"),
]


def evaluate():
    print("=" * 60)
    print("P2 EVALUATION v2: AADM with D/R/S/C (4 dimensions)")
    print("=" * 60)

    print(f"\n## Face Validity Spot Check")
    all_pass = True
    for sid, desc, expected, rationale in SPOT_CHECKS:
        sc = next((s for s in SCENARIOS if s["id"] == sid), None)
        if sc is None:
            print(f"  [SKIP] #{sid} — not in subset")
            continue
        result = score_to_role(sc["d"], sc["r"], sc["s"], sc["c"])
        status = "PASS" if result["role"] == expected else "FAIL"
        if status == "FAIL":
            all_pass = False
        print(f"  [{status}] #{sid} {desc}")
        print(f"         D={sc['d']} R={sc['r']} S={sc['s']} C={sc['c']}")
        print(f"         Expected: {AI_ROLES[expected]}, Got: {AI_ROLES[result['role']]}")
        print(f"         {rationale}")

    print(f"\n## Overall: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
    print(f"\n## Key v2 Fix Verified:")
    print(f"  Design direction (D=2,R=3,S=1,C=5): {AI_ROLES[score_to_role(2,3,1,5)['role']]} (was AI Absent in v1)")
    print(f"  Illustration style (D=1,R=3,S=1,C=5): {AI_ROLES[score_to_role(1,3,1,5)['role']]} (was AI Absent in v1)")


if __name__ == "__main__":
    evaluate()
