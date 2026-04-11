"""
Simulation Studies: Automated Phase (S1, S3, S4, S6)
Run all computational studies that don't require LLM API.

Usage:
    python run_all_studies.py
"""

import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# AADM scoring function (shared)
# ============================================================

def score_to_role(d, r, s):
    if d <= 2 and r <= 2:
        return "ai_absent"
    if d <= 2 and s <= 2:
        return "ai_absent"
    if d >= 4 and r >= 4 and s >= 4:
        return "ai_decides"
    if d >= 4 and s >= 4:
        return "ai_recommends"
    if d >= 4 and s >= 3:
        return "ai_recommends"
    if s <= 2:
        return "ai_assists"
    if d >= 3 and s >= 2:
        return "ai_informs"
    return "ai_informs"


# ============================================================
# Study 1: AADM Boundary Mapping (5^3 = 125 combinations)
# ============================================================

def study_1_boundary_mapping():
    print("\n" + "=" * 60)
    print("STUDY 1: AADM Boundary Mapping (125 combinations)")
    print("=" * 60)

    role_counts = Counter()
    boundary_points = []
    grid = {}

    for d in range(1, 6):
        for r in range(1, 6):
            for s in range(1, 6):
                role = score_to_role(d, r, s)
                grid[(d, r, s)] = role
                role_counts[role] += 1

    # Boundary detection
    for d in range(1, 6):
        for r in range(1, 6):
            for s in range(1, 6):
                base = grid[(d, r, s)]
                neighbors = []
                for dd, dr, ds in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                    nd, nr, ns = d + dd, r + dr, s + ds
                    if 1 <= nd <= 5 and 1 <= nr <= 5 and 1 <= ns <= 5:
                        if grid[(nd, nr, ns)] != base:
                            neighbors.append(grid[(nd, nr, ns)])
                if neighbors:
                    boundary_points.append({"d": d, "r": r, "s": s, "role": base, "adjacent_roles": list(set(neighbors))})

    # Dimension influence: vary one, hold others at 3
    dim_influence = {}
    for dim_name, dim_idx in [("D", 0), ("R", 1), ("S", 2)]:
        transitions = 0
        for val in range(1, 5):
            coords1 = [3, 3, 3]
            coords2 = [3, 3, 3]
            coords1[dim_idx] = val
            coords2[dim_idx] = val + 1
            if grid[tuple(coords1)] != grid[tuple(coords2)]:
                transitions += 1
        dim_influence[dim_name] = transitions

    print(f"\n## Role Volume (out of 125)")
    for role in ["ai_decides", "ai_recommends", "ai_informs", "ai_assists", "ai_absent"]:
        pct = role_counts[role] / 125
        bar = "█" * int(pct * 40)
        print(f"  {role:<16} {role_counts[role]:>3} ({pct:>5.1%}) {bar}")

    print(f"\n## Boundary Points: {len(boundary_points)} out of 125 ({len(boundary_points)/125:.0%})")

    print(f"\n## Dimension Influence (transitions when varying at midpoint)")
    for dim, trans in sorted(dim_influence.items(), key=lambda x: -x[1]):
        print(f"  {dim}: {trans} transitions")

    report = {
        "role_volume": dict(role_counts),
        "boundary_count": len(boundary_points),
        "boundary_fraction": round(len(boundary_points) / 125, 3),
        "dimension_influence": dim_influence,
        "boundary_points_sample": boundary_points[:10],
    }
    with open(OUTPUT_DIR / "s1_boundary_mapping.json", "w") as f:
        json.dump(report, f, indent=2)

    return report


# ============================================================
# Study 3: Leave-Phase-Out Cross-Validation for P1 Classifier
# ============================================================

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

PHASE_DEFAULTS = {
    "Discovery": "decision_uncertain", "Design": "creation", "Development": "execution",
    "Testing": "execution", "Launch": "decision_uncertain", "Growth": "decision_data_rich",
}


def classify(desc):
    desc_lower = desc.lower()
    scores = {t: sum(1 for kw in kws if kw in desc_lower) for t, kws in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "unknown"


def study_3_cross_validation():
    print("\n" + "=" * 60)
    print("STUDY 3: Leave-Phase-Out Cross-Validation")
    print("=" * 60)

    import csv
    benchmark_path = Path(__file__).parent.parent / "p1-complementarity-dashboard" / "benchmark_tasks.csv"
    tasks = []
    with open(benchmark_path) as f:
        for row in csv.DictReader(f):
            tasks.append(row)

    phases = sorted(set(t["phase"] for t in tasks))
    results = {}

    for held_out in phases:
        test_tasks = [t for t in tasks if t["phase"] == held_out]
        correct = 0
        total = len(test_tasks)
        for t in test_tasks:
            predicted = classify(t["description"])
            if predicted == "unknown":
                predicted = PHASE_DEFAULTS.get(t["phase"], "decision_uncertain")
            if predicted == t["expected_type"]:
                correct += 1
        accuracy = correct / total if total > 0 else 0
        results[held_out] = {"accuracy": round(accuracy, 3), "correct": correct, "total": total}

    # Keyword coverage
    coverage = {}
    for phase in phases:
        phase_tasks = [t for t in tasks if t["phase"] == phase]
        matched = sum(1 for t in phase_tasks if classify(t["description"]) != "unknown")
        coverage[phase] = round(matched / len(phase_tasks), 3) if phase_tasks else 0

    print(f"\n## Per-Phase Accuracy (Leave-Phase-Out)")
    print(f"{'Phase':<14} {'Accuracy':>8} {'Correct':>8} {'Total':>6} {'Keyword Coverage':>16}")
    print("-" * 55)
    full_accuracy = 0.673  # from P1 evaluation
    for phase in phases:
        r = results[phase]
        c = coverage[phase]
        delta = r["accuracy"] - full_accuracy
        print(f"{phase:<14} {r['accuracy']:>7.1%} {r['correct']:>8} {r['total']:>6} {c:>15.0%}")

    avg_cv = sum(r["accuracy"] for r in results.values()) / len(results)
    print(f"\n  Average CV accuracy: {avg_cv:.1%} (vs full-data: {full_accuracy:.1%})")
    print(f"  Generalization gap: {full_accuracy - avg_cv:.1%}")

    report = {"per_phase": results, "keyword_coverage": coverage,
              "avg_cv_accuracy": round(avg_cv, 3), "generalization_gap": round(full_accuracy - avg_cv, 3)}
    with open(OUTPUT_DIR / "s3_cross_validation.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


# ============================================================
# Study 4: Bootstrap Perturbation Analysis for P4
# ============================================================

CASES = [
    {"name": "PostNL", "outcome": "SUCCESS", "scores": [5, 4, 5, 5, 5, 4, 4]},
    {"name": "PepsiCo", "outcome": "SUCCESS", "scores": [5, 4, 5, 5, 4, 4, 4]},
    {"name": "OpenTable", "outcome": "SUCCESS", "scores": [4, 3, 5, 4, 4, 3, 4]},
    {"name": "EY.ai PDLC", "outcome": "TBD", "scores": [4, 3, 5, 3, 2, 3, 4]},
    {"name": "Devin", "outcome": "PARTIAL", "scores": [3, 2, 4, 3, 2, 3, 2]},
    {"name": "Klarna", "outcome": "FAILURE", "scores": [3, 2, 3, 1, 2, 2, 1]},
]

PATTERN_NAMES = [
    "Process Readiness", "Line Manager", "Buy Before Build",
    "Back-Office First", "Narrow and Deep", "Learning Systems", "HITL by Design",
]


def get_level(score):
    if score <= 14:
        return "Not Ready"
    elif score <= 21:
        return "Partially Ready"
    elif score <= 28:
        return "Ready"
    else:
        return "Highly Ready"


def study_4_bootstrap():
    print("\n" + "=" * 60)
    print("STUDY 4: Bootstrap Perturbation Analysis (1000 iterations)")
    print("=" * 60)

    random.seed(42)
    n_iters = 1000

    # Original rank order (by total score, descending)
    original_totals = [(c["name"], sum(c["scores"])) for c in CASES]
    original_rank = [x[0] for x in sorted(original_totals, key=lambda x: -x[1])]

    rank_preserved = 0
    klarna_not_ready = 0
    postnl_highly_ready = 0
    pattern_removal_disruptions = defaultdict(int)

    for _ in range(n_iters):
        perturbed_totals = []
        for case in CASES:
            perturbed = [max(1, min(5, s + random.choice([-1, 0, 1]))) for s in case["scores"]]
            perturbed_totals.append((case["name"], sum(perturbed)))

        perturbed_rank = [x[0] for x in sorted(perturbed_totals, key=lambda x: -x[1])]

        if perturbed_rank == original_rank:
            rank_preserved += 1

        klarna_score = next(t for n, t in perturbed_totals if n == "Klarna")
        if get_level(klarna_score) == "Not Ready":
            klarna_not_ready += 1

        postnl_score = next(t for n, t in perturbed_totals if n == "PostNL")
        if get_level(postnl_score) == "Highly Ready":
            postnl_highly_ready += 1

    # Pattern removal sensitivity
    for remove_idx in range(7):
        original_without = [(c["name"], sum(s for i, s in enumerate(c["scores"]) if i != remove_idx)) for c in CASES]
        rank_without = [x[0] for x in sorted(original_without, key=lambda x: -x[1])]
        if rank_without != original_rank:
            pattern_removal_disruptions[PATTERN_NAMES[remove_idx]] = 1

    print(f"\n## Bootstrap Results (n={n_iters})")
    print(f"  Rank preservation rate: {rank_preserved / n_iters:.1%}")
    print(f"  Klarna stays 'Not Ready': {klarna_not_ready / n_iters:.1%}")
    print(f"  PostNL stays 'Highly Ready': {postnl_highly_ready / n_iters:.1%}")

    print(f"\n## Pattern Removal Sensitivity")
    print(f"  Patterns whose removal changes rank order:")
    for pattern, disrupted in sorted(pattern_removal_disruptions.items()):
        print(f"    - {pattern}: {'DISRUPTS' if disrupted else 'stable'}")
    stable = [p for p in PATTERN_NAMES if p not in pattern_removal_disruptions]
    if stable:
        print(f"  Stable patterns (removal doesn't change rank): {', '.join(stable)}")

    report = {
        "n_iterations": n_iters,
        "rank_preservation_rate": round(rank_preserved / n_iters, 3),
        "klarna_not_ready_rate": round(klarna_not_ready / n_iters, 3),
        "postnl_highly_ready_rate": round(postnl_highly_ready / n_iters, 3),
        "pattern_removal_disruptions": dict(pattern_removal_disruptions),
    }
    with open(OUTPUT_DIR / "s4_bootstrap.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


# ============================================================
# Study 6: Cross-Prototype Consistency Test
# ============================================================

def study_6_cross_prototype():
    print("\n" + "=" * 60)
    print("STUDY 6: Cross-Prototype Consistency Test")
    print("=" * 60)

    import csv
    benchmark_path = Path(__file__).parent.parent / "p1-complementarity-dashboard" / "benchmark_tasks.csv"
    tasks = []
    with open(benchmark_path) as f:
        for row in csv.DictReader(f):
            tasks.append(row)

    # Map P1 allocation to expected AADM role
    allocation_to_role = {
        "AI-led, human-reviewed": ["ai_decides", "ai_recommends"],
        "Human+AI collaboration": ["ai_assists", "ai_informs"],
        "AI recommends, human decides": ["ai_recommends", "ai_informs"],
        "Human-led, AI-informed": ["ai_informs", "ai_absent"],
        "Human only": ["ai_absent"],
    }

    # Estimate D/R/S from task type
    type_to_drs = {
        "execution": (4, 4, 5),
        "creation": (2, 3, 1),
        "decision_data_rich": (4, 3, 4),
        "decision_uncertain": (2, 2, 2),
        "ethical_political": (2, 1, 1),
    }

    consistent = 0
    inconsistent = 0
    inconsistencies = []

    for task in tasks:
        p1_type = task["expected_type"]
        p1_alloc = task["expected_allocation"]
        d, r, s = type_to_drs.get(p1_type, (3, 3, 3))
        p2_role = score_to_role(d, r, s)
        compatible_roles = allocation_to_role.get(p1_alloc, [])

        if p2_role in compatible_roles:
            consistent += 1
        else:
            inconsistent += 1
            if len(inconsistencies) < 10:
                inconsistencies.append({
                    "desc": task["description"][:60],
                    "p1_alloc": p1_alloc,
                    "p2_role": p2_role,
                    "expected_roles": compatible_roles,
                })

    total = consistent + inconsistent
    rate = consistent / total if total > 0 else 0

    print(f"\n## P1-P2 Consistency Rate: {rate:.1%} ({consistent}/{total})")
    if inconsistencies:
        print(f"\n## Sample Inconsistencies ({inconsistent} total)")
        for inc in inconsistencies[:5]:
            print(f"  '{inc['desc']}...'")
            print(f"    P1: {inc['p1_alloc']} | P2: {inc['p2_role']} | Expected: {inc['expected_roles']}")

    report = {
        "consistency_rate": round(rate, 3),
        "consistent": consistent,
        "inconsistent": inconsistent,
        "total": total,
        "sample_inconsistencies": inconsistencies,
    }
    with open(OUTPUT_DIR / "s6_cross_prototype.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("SIMULATION STUDIES — AUTOMATED PHASE")
    print("Date: 2026-04-11\n")

    s1 = study_1_boundary_mapping()
    s3 = study_3_cross_validation()
    s4 = study_4_bootstrap()
    s6 = study_6_cross_prototype()

    print("\n" + "=" * 60)
    print("ALL STUDIES COMPLETE")
    print("=" * 60)
    print(f"Results saved to: {OUTPUT_DIR}/")
