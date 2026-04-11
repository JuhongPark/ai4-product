"""
Honest v2 Validation: What happens when C is scored imperfectly?

Instead of assigning "perfect" C values (circular), we simulate
realistic human scoring noise on the C dimension and measure how
much the consistency improvement survives.

Usage:
    python run_honest_v2_test.py
"""

import csv
import json
import random
from collections import Counter
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(exist_ok=True)


def score_to_role_v2(d, r, s, c):
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
    "ai_decides": "AI Decides", "ai_recommends": "AI Recommends",
    "ai_informs": "AI Informs", "ai_assists": "AI Assists", "ai_absent": "AI Absent",
}


def load_tasks():
    path = Path(__file__).parent.parent / "p1-complementarity-dashboard" / "benchmark_tasks.csv"
    tasks = []
    with open(path) as f:
        for row in csv.DictReader(f):
            tasks.append(row)
    return tasks


# "True" C values — what an ideal scorer would assign
TRUE_C = {
    "execution": 1,
    "creation": 5,
    "decision_data_rich": 1,
    "decision_uncertain": 1,
    "ethical_political": 1,
}

# D/R/S values (same for v1 and v2)
TYPE_DRS = {
    "execution": (4, 4, 5),
    "creation": (2, 3, 1),
    "decision_data_rich": (4, 3, 4),
    "decision_uncertain": (2, 2, 2),
    "ethical_political": (2, 1, 1),
}

COMPATIBLE_ROLES = {
    "AI-led, human-reviewed": ["ai_decides", "ai_recommends"],
    "Human+AI collaboration": ["ai_assists", "ai_informs"],
    "AI recommends, human decides": ["ai_recommends", "ai_informs"],
    "Human-led, AI-informed": ["ai_informs", "ai_absent"],
    "Human only": ["ai_absent"],
}


def run_test(noise_level, n_iterations=1000):
    """Test P1-P2 consistency with noisy C scores.

    noise_level: probability that C score shifts by ±1 or ±2
    - 0.0 = perfect scoring (circular test)
    - 0.3 = moderate noise (realistic human disagreement)
    - 0.5 = high noise (substantial disagreement)
    - 1.0 = random C (C dimension adds no signal)
    """
    random.seed(42)
    tasks = load_tasks()

    consistency_rates = []

    for _ in range(n_iterations):
        consistent = 0
        total = 0

        for task in tasks:
            p1_type = task["expected_type"]
            p1_alloc = task["expected_allocation"]
            compatible = COMPATIBLE_ROLES.get(p1_alloc, [])

            d, r, s = TYPE_DRS.get(p1_type, (3, 3, 3))
            true_c = TRUE_C.get(p1_type, 2)

            # Apply noise to C
            if random.random() < noise_level:
                noise = random.choice([-2, -1, 1, 2])
                c = max(1, min(5, true_c + noise))
            else:
                c = true_c

            role = score_to_role_v2(d, r, s, c)
            if role in compatible:
                consistent += 1
            total += 1

        consistency_rates.append(consistent / total)

    avg = sum(consistency_rates) / len(consistency_rates)
    low = sorted(consistency_rates)[int(0.05 * n_iterations)]
    high = sorted(consistency_rates)[int(0.95 * n_iterations)]

    return {"mean": round(avg, 3), "ci_low": round(low, 3), "ci_high": round(high, 3)}


def run_random_c_baseline(n_iterations=1000):
    """Baseline: What if C is completely random (uniform 1-5)?"""
    random.seed(42)
    tasks = load_tasks()
    rates = []

    for _ in range(n_iterations):
        consistent = 0
        total = 0
        for task in tasks:
            p1_type = task["expected_type"]
            p1_alloc = task["expected_allocation"]
            compatible = COMPATIBLE_ROLES.get(p1_alloc, [])

            d, r, s = TYPE_DRS.get(p1_type, (3, 3, 3))
            c = random.randint(1, 5)  # completely random

            role = score_to_role_v2(d, r, s, c)
            if role in compatible:
                consistent += 1
            total += 1
        rates.append(consistent / total)

    avg = sum(rates) / len(rates)
    return round(avg, 3)


def main():
    print("=" * 60)
    print("HONEST v2 VALIDATION: Noisy C Scores")
    print("=" * 60)

    # v1 baseline (no C dimension)
    tasks = load_tasks()
    v1_consistent = 0
    for task in tasks:
        p1_type = task["expected_type"]
        p1_alloc = task["expected_allocation"]
        compatible = COMPATIBLE_ROLES.get(p1_alloc, [])
        d, r, s = TYPE_DRS.get(p1_type, (3, 3, 3))
        role = score_to_role_v1(d, r, s)
        if role in compatible:
            v1_consistent += 1
    v1_rate = v1_consistent / len(tasks)

    print(f"\n## Baselines")
    print(f"  v1 (D/R/S only):    {v1_rate:.1%}")

    random_baseline = run_random_c_baseline()
    print(f"  v2 + random C:      {random_baseline:.1%}")

    print(f"\n## v2 Consistency Under Different C Noise Levels")
    print(f"  (1000 iterations each, 90% confidence interval)")
    print(f"  {'Noise':>8} {'Mean':>8} {'90% CI':>16} {'vs v1':>10}")
    print(f"  {'-'*46}")

    results = {}
    for noise in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0]:
        r = run_test(noise)
        delta = r["mean"] - v1_rate
        results[str(noise)] = r
        ci_str = f"[{r['ci_low']:.1%}, {r['ci_high']:.1%}]"
        print(f"  {noise:>7.0%} {r['mean']:>7.1%} {ci_str:>16} {delta:>+9.1%}")

    print(f"\n## Interpretation")
    print(f"  - At 0% noise (circular test):  {results['0.0']['mean']:.1%} ← this was our invalid claim")
    print(f"  - At 30% noise (realistic):     {results['0.3']['mean']:.1%} ← likely real-world performance")
    print(f"  - At 50% noise (high):          {results['0.5']['mean']:.1%} ← pessimistic estimate")
    print(f"  - At 100% noise (random C):     {results['1.0']['mean']:.1%} ← C adds no signal")
    print(f"  - v1 baseline:                  {v1_rate:.1%}")

    improvement_at_30 = results["0.3"]["mean"] - v1_rate
    improvement_at_50 = results["0.5"]["mean"] - v1_rate
    print(f"\n## Honest Improvement Estimate")
    print(f"  Realistic (30% noise): {improvement_at_30:+.1%} over v1")
    print(f"  Pessimistic (50% noise): {improvement_at_50:+.1%} over v1")

    degrades = results["1.0"]["mean"] < v1_rate
    print(f"\n## Does random C degrade v2 below v1?")
    print(f"  Random C consistency: {results['1.0']['mean']:.1%} vs v1: {v1_rate:.1%}")
    print(f"  {'YES — random C hurts' if degrades else 'NO — v2 is at least as good as v1 even with random C'}")

    report = {
        "v1_baseline": round(v1_rate, 3),
        "random_c_baseline": random_baseline,
        "noise_levels": results,
        "honest_improvement_30_noise": round(improvement_at_30, 3),
        "honest_improvement_50_noise": round(improvement_at_50, 3),
        "random_c_degrades": degrades,
    }
    with open(OUTPUT_DIR / "honest_v2_validation.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"\nReport saved to {OUTPUT_DIR / 'honest_v2_validation.json'}")


if __name__ == "__main__":
    main()
