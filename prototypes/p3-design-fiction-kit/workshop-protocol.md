# P3: Design Fiction Workshop Protocol

## "A Day in the Life of an AI Product Team in 2028"

> 3-hour participatory design fiction workshop to discover requirements and risks that traditional methods miss.

---

## Overview

| Item | Detail |
|------|--------|
| Duration | 3 hours |
| Participants | 5-8 per session |
| Sessions | 3 (PM-only, Designer-only, Mixed team) |
| Materials | Scenario cards, artifact templates, evaluation forms |
| Facilitator | 1 lead + 1 note-taker |

---

## Pre-Workshop Preparation

### Facilitator Checklist
- [ ] Print scenario cards (see `scenario-cards.md`)
- [ ] Print artifact templates (see `artifact-templates.md`)
- [ ] Prepare twist cards (see scenario cards, twist section)
- [ ] Set up recording (video + audio, with consent)
- [ ] Prepare wall space or digital whiteboard (Miro/FigJam)
- [ ] Print evaluation forms (see `evaluation-form.md`)
- [ ] Brief note-taker on what to capture

### Participant Pre-Read (Send 2 Days Before)
> "Imagine it's 2028. Your product team uses AI agents for about 80% of execution tasks — coding, testing, documentation, data analysis. A 'Complementarity Dashboard' recommends whether each task should be AI-led, human+AI, or human-led. An 'AADM Score' determines how much autonomy the AI gets for each decision. This has been working well for 6 months. Then something goes wrong."

---

## Workshop Flow

### Part 1: World-Building (45 min)

**1a. Facilitator Presents the Scenario (10 min)**

Read aloud:

> "It's March 2028. You're on a product team at [fictional company name]. For the past 6 months, you've been using three AI tools:
>
> 1. **CompDash** — tells you whether each task should be AI-led, human+AI, or human-led
> 2. **AADM Scorer** — scores each decision and recommends how much AI autonomy to give it
> 3. **AgentFleet** — a set of AI agents that handle execution: code, tests, docs, analytics
>
> Results have been strong: 40% faster shipping, 60% less documentation time, consistently better A/B test analysis.
>
> Last Tuesday, something happened."

**1b. Draw a Scenario Card (5 min)**

Each sub-team (2-3 people) draws one scenario card from the deck. The card describes what went wrong. (See `scenario-cards.md`)

**1c. Extend the Scenario (30 min)**

Teams answer these questions on sticky notes / whiteboard:
1. What happened immediately after the incident?
2. Who was affected? (users, team members, executives, partners)
3. What did the team's AI tools do / not do?
4. What did the humans do / not do?
5. How was it eventually resolved?

Facilitator circulates, asks probing questions:
- "What would CompDash have recommended for this task?"
- "What AADM score would this decision have gotten?"
- "Would any of the 7 success patterns have prevented this?"

---

### Part 2: Artifact Creation (60 min)

**Each team creates ONE diegetic artifact from 2028:**

Option A: **Incident Post-Mortem**
- "5 Whys" analysis of the incident
- Root cause: human, AI, or system-level?
- Action items and policy changes

Option B: **Team Retrospective Notes**
- What went well in the human-AI collaboration?
- What didn't work?
- What should we change in CompDash/AADM settings?

Option C: **Policy Document**
- "AI Override Policy v2.0" — when is a human allowed to override AI recommendations?
- "Escalation Protocol" — when must AI defer to human?
- Updated AADM scoring guidelines based on the incident

Option D: **News Article / Blog Post**
- External perspective: "How [Company] Handled Its AI Product Failure"
- Public reaction, customer impact, industry implications

**Materials provided:**
- Artifact templates (see `artifact-templates.md`)
- Scenario twist cards (drawn at 30-min mark to add complications)

---

### Part 3: Critical Analysis (45 min)

**3a. Presentations (25 min)**
Each team presents their artifact (5-7 min each).

**3b. Structured Discussion (20 min)**
Facilitator leads discussion using these prompts:

1. **Requirements Discovery**: "What requirements did this workshop reveal that we hadn't considered before?"
2. **Risk Discovery**: "What risks emerged that our current frameworks don't address?"
3. **Governance Rules**: "What governance rules would have prevented or mitigated the incident?"
4. **Framework Gaps**: "Where did CompDash / AADM / Success Patterns fail in this scenario?"
5. **Human Judgment Points**: "At which moment was human judgment most critical?"

Each insight is captured on a card categorized as:
- 🟢 NEW REQUIREMENT
- 🔴 NEW RISK
- 🟡 GOVERNANCE RULE
- 🔵 FRAMEWORK GAP

---

### Part 4: Extraction & Evaluation (30 min)

**4a. Synthesis (15 min)**
Facilitator clusters all cards and summarizes:
- Top 3 new requirements
- Top 3 new risks
- Top 3 governance rules
- Framework modifications needed

**4b. Individual Evaluation (15 min)**
Each participant fills out `evaluation-form.md`:
- Rate each discovered insight: "Would traditional methods have found this?" (1-5)
- Rate overall workshop: engagement, realism, usefulness (1-5)
- Open-ended: "What was the most surprising thing you learned?"

---

## Post-Workshop

### Data Collection
- Collect all artifacts (photos / digital files)
- Collect all evaluation forms
- Transcribe key discussion points from recording
- Compile card clusters (requirements, risks, governance, gaps)

### Analysis
1. Count unique requirements/risks per workshop
2. Compare across W1 (PM), W2 (Designer), W3 (Mixed)
3. Calculate novelty scores from evaluation forms
4. Map discovered insights back to research-gaps.md
5. Identify insights that appear in 2+ workshops (cross-validated)

### Reporting
- Insight catalog: all discovered requirements, risks, governance rules
- Novelty analysis: % of insights rated 4-5 on "would traditional methods have found this?"
- Framework modification proposals based on workshop findings
