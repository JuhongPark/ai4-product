# The METR Productivity Paradox: Vendor Claims vs. Independent RCT

> **Date:** 2026-04-21
> **Scope:** METR randomized controlled trial (2025), follow-up study (2026), methodological analysis

---

## 1. Summary

The METR **randomized controlled trial** (July 2025) — the most widely-cited independent RCT on AI coding productivity — found that allowing AI tools increased task completion time by **19%** for experienced open-source developers. Developers predicted a **24% speedup** and, after the study, still believed AI **helped them by 20%** — despite actually experiencing a slowdown.

A **2026-02 follow-up** showed the signal flipping in the opposite direction (**-18% speedup** point estimate) once broader-pool recruiting was attempted, but researchers labeled the follow-up result unreliable due to selection bias.

**Net takeaway**: For experienced OSS developers in 2025 the measured result was -19%; the replication is inconclusive. The AI productivity question is **not settled** for experienced developers on their own codebases. This is the most important empirical counterweight to vendor productivity claims in the 2026 literature.

---

## 2. Study Design

| Parameter | Value |
|---|---|
| Developers | 16 experienced OSS contributors |
| Tasks | 246 tasks on their own repositories |
| Task length | ~2.0 hours each |
| AI tools allowed | Cursor Pro + Claude 3.5/3.7 Sonnet (developer's choice) |
| Control | No generative AI |
| Method | Randomized per task |

Published July 2025. https://arxiv.org/abs/2507.09089

---

## 3. Key Findings

### 3.1 The Objective Result
- **AI allowed: +19% time to complete** (slower)
- **AI disallowed: baseline**

### 3.2 The Belief Gap
- **Forecast (pre-study)**: AI would be **24% faster**
- **Actual**: AI was **19% slower**
- **Post-study belief**: AI was **20% faster** — developers continued to believe AI helped despite the measured slowdown

This is one of the sharpest objective/subjective gaps in SE productivity research.

---

## 4. 2026 Follow-Up: The Signal Flipped — But Unreliably

METR's 2026-02 update (https://metr.org/blog/2026-02-24-uplift-update/) reports that the late-2025 follow-up **partially contradicted** the 19% slowdown. Key details:

- Restarted August 2025 with broader pool and design changes
- Observed point estimates: **-18% speedup for original developers**, **-4% for new recruits** (sign flip vs 2025 RCT)
- **But researchers label these unreliable** due to selection effects:
  - 30–50% of developers chose not to submit some tasks because they didn't want to do them without AI
  - Hourly pay dropped from $150 to $50, biasing participation
  - AI-enthusiastic developers self-selected out of the no-AI arm
- Researchers note the true speedup "could be much higher" than measured
- Study redesign underway: shorter intensive experiments, observational GitHub data, fixed-task designs, developer-level randomization

**Interpretation**: Neither the original 19% slowdown nor the 18% speedup should be treated as a settled point estimate. The measurement problem is substantially harder than vendor studies imply, and **the true effect on experienced developers in late 2025 / 2026 remains empirically unresolved**.

---

## 5. Interpreting the Result

### 5.1 What the Study Is
- Rigorous RCT on a real task domain (OSS contribution)
- Experienced developers, own repositories — high ecological validity for *their* context

### 5.2 What the Study Is Not
- Does NOT claim AI slows all developers
- Does NOT generalize to novices, new codebases, greenfield projects
- Does NOT measure quality (did AI-assisted tasks produce better code?)

### 5.3 Mechanisms Hypothesized
- **Context-switching overhead** — prompt crafting, review loop breaks flow
- **Verification overhead** — developers review AI output carefully enough to exceed manual time
- **Inaccuracy correction** — AI output requires patching for the contributor's specific standards
- **Task selection mismatch** — experienced developers' OSS tasks may favor domain knowledge AI lacks

---

## 6. Contrast with Vendor Studies

| Study | Source | Claim | Population |
|---|---|---|---|
| METR (2025) | Independent RCT | **-19% (slower)** | 16 experienced OSS devs |
| GitHub Copilot | Vendor | +55% faster | Self-selected adopters |
| Cursor / UChicago | Vendor | +39% merged PRs | Self-selected adopters |

**Reconciliation**: All three are directionally correct for their populations. The METR finding does not invalidate vendor studies — it specifies **where vendor claims fail to generalize**: experienced developers on their own complex codebases may not gain from current AI tools.

---

## 7. Implications for Productization

1. **Tool evaluation should distinguish developer populations** — novice vs. expert, new vs. existing codebase
2. **Self-report is untrustworthy** — 24% forecast, 20% post-belief, -19% actual
3. **A/B testing inside a team** is necessary — not generic vendor claims
4. **The "AI productivity" question is not yet settled** — measurement, not consensus

---

## 8. Research Gaps

1. **Larger sample RCTs** — 16 developers cannot resolve heterogeneity
2. **Novice vs. expert RCTs** — METR's failure on experts doesn't predict novice impact
3. **Longitudinal learning curves** — Does the gap close after months of AI use?
4. **Task-type segmentation** — Which tasks robustly benefit, which don't
5. **Quality measurement** — Does AI-slower work produce better code?

---

## 9. Sources

- METR (2025). "Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity." https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- arXiv paper: https://arxiv.org/abs/2507.09089
- METR (2026). "Changing our Developer Productivity Experiment Design." https://metr.org/blog/2026-02-24-uplift-update/
- Simon Willison. "Measuring the Impact of Early-2025 AI on Developer Productivity." https://simonwillison.net/2025/Jul/12/ai-open-source-productivity/
- DX Newsletter. "METR's study on how AI affects developer productivity." https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity
- Let's Data Science. "AI Coding Tools Made Developers 19% Slower." https://letsdatascience.com/blog/developers-thought-ai-made-them-faster-the-data-said-otherwise
- Domenic Denicola. "My Participation in the METR AI Productivity Study." https://domenic.me/metr-ai-productivity/
- EA Forum. "Assessing heterogeneity in METR's late 2025 developer productivity experiment." https://forum.effectivealtruism.org/posts/jvrZ3gHYGj59Wa7z8/assessing-heterogeneity-in-metr-s-late-2025-developer
