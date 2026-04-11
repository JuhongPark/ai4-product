"""
AADM v2 Simulation Studies: Re-run S1 and S6 with 4-dimension (D/R/S/C) model.
Compare against v1 results to measure improvement.

Usage:
    python run_v2_studies.py
"""

import json
from collections import Counter, defaultdict
from pathlib import Path
import csv

OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(exist_ok=True)


def score_to_role_v2(d, r, s, c):
    """AADM v2: 4-dimension scoring with Creativity."""
    if d <= 2 and r <= 2 and c <= 2:
        return "ai_absent"
    if d <= 2 and s <= 2 and c <= 2:
        return "ai_absent"
    if c >= 4:
        return "ai_assists"
    if c >= 3 and s <= 2:
        return "ai_assists"
    if d >= 4 and r >= 4 and s >= 4 and c <= 2:
        return "ai_decides"
    if d >= 4 and r >= 4 and s >= 4:
        return "ai_decides"
    if d >= 4 and s >= 4:
        return "ai_recommends"
    if d >= 4 and s >= 3:
        return "ai_recommends"
    if c >= 3:
        return "ai_assists"
    if d <= 2 and r <= 2:
        return "ai_absent"
    if d >= 3 and s >= 2:
        return "ai_informs"
    return "ai_informs"


def score_to_role_v1(d, r, s):
    """AADM v1: 3-dimension scoring (for comparison)."""
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


ROLE_LABELS = {
    "ai_decides": "AI Decides",
    "ai_recommends": "AI Recommends",
    "ai_informs": "AI Informs",
    "ai_assists": "AI Assists",
    "ai_absent": "AI Absent",
}


# ============================================================
# Study 1 v2: Boundary Mapping (5^4 = 625 combinations)
# ============================================================

def study_1_v2():
    print("\n" + "=" * 60)
    print("STUDY 1 v2: AADM Boundary Mapping (625 combinations)")
    print("=" * 60)

    role_counts = Counter()
    grid = {}

    for d in range(1, 6):
        for r in range(1, 6):
            for s in range(1, 6):
                for c in range(1, 6):
                    role = score_to_role_v2(d, r, s, c)
                    grid[(d, r, s, c)] = role
                    role_counts[role] += 1

    # Boundary detection
    boundary_count = 0
    for d in range(1, 6):
        for r in range(1, 6):
            for s in range(1, 6):
                for c in range(1, 6):
                    base = grid[(d, r, s, c)]
                    is_boundary = False
                    for dd, dr, ds, dc in [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]:
                        nd, nr, ns, nc = d+dd, r+dr, s+ds, c+dc
                        if 1 <= nd <= 5 and 1 <= nr <= 5 and 1 <= ns <= 5 and 1 <= nc <= 5:
                            if grid[(nd, nr, ns, nc)] != base:
                                is_boundary = True
                                break
                    if is_boundary:
                        boundary_count += 1

    total = 625
    print(f"\n## Role Volume (out of {total})")
    for role in ["ai_decides", "ai_recommends", "ai_informs", "ai_assists", "ai_absent"]:
        count = role_counts[role]
        pct = count / total
        bar = "█" * int(pct * 40)
        print(f"  {ROLE_LABELS[role]:<16} {count:>4} ({pct:>5.1%}) {bar}")

    boundary_pct = boundary_count / total
    print(f"\n## Boundary Points: {boundary_count}/{total} ({boundary_pct:.0%})")
    print(f"   v1 was: 92/125 (74%)")
    print(f"   Change: {boundary_pct:.0%} vs 74% ({'improved' if boundary_pct < 0.74 else 'similar or worse'})")

    # Dimension influence at midpoint
    dim_influence = {}
    for dim_name, dim_idx in [("D", 0), ("R", 1), ("S", 2), ("C", 3)]:
        transitions = 0
        for val in range(1, 5):
            coords1 = [3, 3, 3, 2]  # midpoint with C=2 (non-creative default)
            coords2 = [3, 3, 3, 2]
            coords1[dim_idx] = val
            coords2[dim_idx] = val + 1
            if grid[tuple(coords1)] != grid[tuple(coords2)]:
                transitions += 1
        dim_influence[dim_name] = transitions

    print(f"\n## Dimension Influence (at midpoint, C=2)")
    for dim, trans in sorted(dim_influence.items(), key=lambda x: -x[1]):
        print(f"  {dim}: {trans} transitions")

    report = {
        "version": "v2",
        "total_combinations": total,
        "role_volume": dict(role_counts),
        "boundary_count": boundary_count,
        "boundary_fraction": round(boundary_pct, 3),
        "v1_boundary_fraction": 0.736,
        "dimension_influence": dim_influence,
    }
    with open(OUTPUT_DIR / "s1_v2_boundary_mapping.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


# ============================================================
# Study 6 v2: Cross-Prototype Consistency (with C dimension)
# ============================================================

def study_6_v2():
    print("\n" + "=" * 60)
    print("STUDY 6 v2: Cross-Prototype Consistency (D/R/S/C)")
    print("=" * 60)

    benchmark_path = Path(__file__).parent.parent / "p1-complementarity-dashboard" / "benchmark_tasks.csv"
    tasks = []
    with open(benchmark_path) as f:
        for row in csv.DictReader(f):
            tasks.append(row)

    allocation_to_role = {
        "AI-led, human-reviewed": ["ai_decides", "ai_recommends"],
        "Human+AI collaboration": ["ai_assists", "ai_informs"],
        "AI recommends, human decides": ["ai_recommends", "ai_informs"],
        "Human-led, AI-informed": ["ai_informs", "ai_absent"],
        "Human only": ["ai_absent"],
    }

    # v2: add C dimension based on task type
    type_to_drsc = {
        "execution": (4, 4, 5, 1),      # not creative
        "creation": (2, 3, 1, 5),        # HIGHLY creative — this is the key fix
        "decision_data_rich": (4, 3, 4, 1),
        "decision_uncertain": (2, 2, 2, 1),
        "ethical_political": (2, 1, 1, 1),
    }

    # Also run v1 for comparison
    type_to_drs_v1 = {
        "execution": (4, 4, 5),
        "creation": (2, 3, 1),
        "decision_data_rich": (4, 3, 4),
        "decision_uncertain": (2, 2, 2),
        "ethical_political": (2, 1, 1),
    }

    v1_consistent = 0
    v2_consistent = 0
    v2_fixes = []
    v2_regressions = []

    for task in tasks:
        p1_type = task["expected_type"]
        p1_alloc = task["expected_allocation"]
        compatible = allocation_to_role.get(p1_alloc, [])

        # v1
        d1, r1, s1 = type_to_drs_v1.get(p1_type, (3, 3, 3))
        v1_role = score_to_role_v1(d1, r1, s1)
        if v1_role in compatible:
            v1_consistent += 1

        # v2
        d2, r2, s2, c2 = type_to_drsc.get(p1_type, (3, 3, 3, 2))
        v2_role = score_to_role_v2(d2, r2, s2, c2)
        if v2_role in compatible:
            v2_consistent += 1

        # Track fixes and regressions
        v1_ok = v1_role in compatible
        v2_ok = v2_role in compatible
        if not v1_ok and v2_ok:
            v2_fixes.append({"desc": task["description"][:60], "v1": v1_role, "v2": v2_role, "expected": compatible})
        if v1_ok and not v2_ok:
            v2_regressions.append({"desc": task["description"][:60], "v1": v1_role, "v2": v2_role, "expected": compatible})

    total = len(tasks)
    v1_rate = v1_consistent / total
    v2_rate = v2_consistent / total

    print(f"\n## Consistency Comparison")
    print(f"  v1 (D/R/S):   {v1_rate:.1%} ({v1_consistent}/{total})")
    print(f"  v2 (D/R/S/C): {v2_rate:.1%} ({v2_consistent}/{total})")
    print(f"  Improvement:   {v2_rate - v1_rate:+.1%}")

    print(f"\n## Fixes (v1 wrong → v2 correct): {len(v2_fixes)}")
    for fix in v2_fixes[:5]:
        print(f"  '{fix['desc']}...' : {ROLE_LABELS[fix['v1']]} → {ROLE_LABELS[fix['v2']]}")

    print(f"\n## Regressions (v1 correct → v2 wrong): {len(v2_regressions)}")
    for reg in v2_regressions[:5]:
        print(f"  '{reg['desc']}...' : {ROLE_LABELS[reg['v1']]} → {ROLE_LABELS[reg['v2']]}")

    report = {
        "v1_consistency": round(v1_rate, 3),
        "v2_consistency": round(v2_rate, 3),
        "improvement": round(v2_rate - v1_rate, 3),
        "fixes": len(v2_fixes),
        "regressions": len(v2_regressions),
        "fix_samples": v2_fixes[:10],
        "regression_samples": v2_regressions[:10],
    }
    with open(OUTPUT_DIR / "s6_v2_cross_prototype.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


if __name__ == "__main__":
    print("AADM v2 SIMULATION STUDIES")
    print("=" * 60)
    s1 = study_1_v2()
    s6 = study_6_v2()

    print("\n" + "=" * 60)
    print("v2 STUDIES COMPLETE")
    print("=" * 60)
