# O3 — Organizational Learning Velocity Under Tool Flux

> **Status:** research_memo (draft; source audit pending)
> **Research plan:** [Research plan](../plan.md)
> **Axis:** O (Organization) — Pillar 2
> **Date:** 2026-04-22
> **Anchor questions**
> - *Engineering*: what artifact and process infrastructure must be built so that knowledge survives quarterly tool turnover?
> - *Managerial*: what governance and role structures keep an organization's learning velocity faster than its tool-flux velocity?

---

## 1. Method

**Scope.** Which knowledge-management and internal-learning systems survive when AI tools turn over every three months. Window 2023-01-01 through 2026-04-22. Primary public-source evidence, labelled by confidence. Negative evidence (what failed) is load-bearing.

**Why velocity, not adoption.** Adoption statistics (McKinsey 2025: 88% of organizations report regular AI use in at least one function; BCG AI at Work 2025: ~75% weekly usage among leaders, ~50% among frontline; DX Q1 2026: 93% developer adoption) measure the **stock** of AI usage. The research prompt asks about the **flow** — how fast an organization can re-internalize a changed tool and re-stabilize its practice. The unit of analysis is therefore *(learning mechanism × tool-change event × survival outcome)*, not *(firm × adoption %)*.

**Tool-flux operationalization.** A tool-change event is any of: (i) a foundation-model generation shift (GPT-4 → GPT-4o → GPT-5; Claude 3 → 3.5 → 4), (ii) a coding-agent UX shift (Copilot Chat → Copilot Agent; Cursor 1/2 → Cursor 3 with demoted IDE; Claude Code launch; Replit Agent; Windsurf), (iii) an enterprise platform change (Atlassian Rovo launch 2024; Gemini Enterprise late-2025 launch; M365 Copilot auto-install October 2025), (iv) a prompting-paradigm shift (few-shot → function calling → skills / MCP → "context engineering" summer 2025). On the 2023–2026 window these events are at ~quarterly cadence for any given team.

**Evidence sources.** Engineering blogs (Shopify, Stripe, Anthropic, GitLab, Atlassian), academic field experiments (Wharton/HBS "Navigating the Jagged Frontier" 2023; Mollick "Cybernetic Teammate" P&G 2025; Brynjolfsson-Li-Raymond MIT Sloan on contact-center GenAI), practitioner writing (Hamel Husain, Eugene Yan, Will Kelly, ALM on "prompt library burnout"), vendor reports (McKinsey State of AI March 2025 and November 2025, BCG AI at Work 2025 and 2026, Stanford HAI AI Index 2025, DX Q4-2025 and Q1-2026), and negative-evidence cases (Klarna AI reversal 2024–2026, Gartner finding only 5–6% of enterprises move past pilot).

**Out of scope.** Full-text review of proprietary internal wikis; firm-level financial attribution. Where only public references exist (e.g., Shopify's internal prompt library mentioned in Bessemer's Atlas article), that fact is noted and treated as medium confidence.

**Lenses applied.** Senge's five disciplines (shared vision, mental models, team learning, personal mastery, systems thinking); Cohen & Levinthal (1990) absorptive capacity = prior knowledge × diversity × integration mechanisms; Argyris & Schön single- vs double-loop learning; March (1991) exploration-exploitation; Nonaka (1994) SECI spiral (socialization → externalization → combination → internalization).

---

## 2. Evidence table

Rows are *(learning mechanism × firm × tool-change event × survival outcome)*. Confidence: **H** = primary source direct, **M** = secondary source or inferred from public artefact, **L** = practitioner claim without corroboration.

| # | Mechanism | Firm / source | Tool-change event | Survival outcome | Conf. |
|---|-----------|---------------|-------------------|------------------|-------|
| 1 | `CLAUDE.md` in-repo context file | Anthropic internal; Claude Code defaults | Claude 3 → 3.5 → 4; Skills release Oct-2025 | **Survives.** File persists across model versions; new models re-read it. Becomes canonical onboarding doc. | H |
| 2 | "Team OS" repo (root + nested `claude.md`, playbooks, queries, schemas, launch gate) — DoorDash PM Hannah Stulberg, ~1,500 hrs usage | DoorDash (public talk 2026) | Claude Code Skills, MCP, Rovo | **Survives** by being a **codebase**, not a prompt list. 30-day setup; queries and schemas re-used even when model swaps. | M |
| 3 | Roast open-sourced YAML + markdown workflow framework | Shopify Augmented Engineering DX | GPT-4 → Claude family; agent UX shifts | **Survives**: declarative workflow spec decouples intent from model. ~500 DAU, open-sourced May-2025. | H |
| 4 | Internal "prompt library" (flat list) at Shopify | Shopify (via Bessemer Atlas) | Context-engineering shift summer 2025 | Mixed. Library plus *leader modelling in demos* succeeds; library alone hits "prompt library burnout" reported elsewhere. | M |
| 5 | Centralized flat prompt libraries at large enterprises (generic) | Will Kelly / ALM Corp analysis 2025 | Any model version bump | **Breaks.** Staleness ≥60% → users work around it; ≥80% → stop adding; ≥90% → dead. Canonical pattern. | M |
| 6 | Evaluator harness (LLM-as-judge + human labels) with CI gating | Braintrust pattern; Hamel Husain course; Eugene Yan writing | Model swap, prompt edit | **Survives and strengthens.** When evals block merge, prompt changes are test-driven. Translates fast artefact change into slow durable metric improvement. | H |
| 7 | Prompt versioning in Langfuse / Braintrust / LangSmith | Cross-vendor | Model swap | **Survives** where adopted; creates rollback path. Adoption is still minority in typical enterprises. | H |
| 8 | Runbooks + markdown troubleshooting guides ingested by Claude | Anthropic Security Engineering | Claude model change | **Survives**: plain-text knowledge remains the canonical medium; Claude re-reads it. | H |
| 9 | "Minions" blueprint system (workflows as code interweaving agent skills and deterministic routines) | Stripe Developer Productivity AI | Coding-agent generation change | **Survives**: 1,300 PRs/week; blueprints persist across underlying model updates because they separate orchestration from generation. | H |
| 10 | Atlassian shared **skills registry** (first-party + third-party + custom) | Atlassian (Rovo, 2024+) | Agent Skills open standard Oct-2025 | **Survives**: registry abstraction outlives any specific agent; Agent Skills standard also spans VS Code, Copilot CLI, coding agent. | M |
| 11 | Weekly demos / AMAs / "show me how you used AI" rituals | Shopify (First Round), generic Slack/Notion posts | Any tool change | **Survives** because socialization (Nonaka S) is tool-invariant; the ritual binds to role, not tool. | M |
| 12 | Guilds / communities of practice for AI users | Management 3.0 / GitHub CoP / generic | Any tool change | **Survives** where given real time budget. Spotify-style guild model pre-dates AI and is directly reusable. | M |
| 13 | Klarna customer-service AI replacing 700 agents, minimal human-in-loop learning structure | Klarna (reversed 2025–2026) | Quality / edge-case failures | **Breaks.** Learning loop absent; tacit CS knowledge disintermediated and lost; rehiring. Canonical 2026 cautionary case. | H |
| 14 | Microsoft Copilot enterprise rollouts without training | Gartner 2025 survey; Xenoss 2026 summary | M365 Copilot auto-install Oct-2025 | **Stalls.** Only ~5–6% past pilot; penetration ~3% of seats despite licence; learning curve cited as top blocker. | H |
| 15 | Role-based capability training (≥5 hours + coaching) | BCG AI at Work 2025 | Cross-tool | **Works.** Regular usage sharply higher above 5h + in-person coaching threshold. Only ~33% of employees say they have been properly trained. | H |
| 16 | 70/20/10 resource split (people/process, tech/data, algorithms) | BCG "value in AI" 2024–2025 | Cross-tool | **Works.** Leaders (~5%) deliver ~4× TSR of laggards; upskilling is the largest single lever. | H |
| 17 | New-hire AI-assisted ramp (time-to-10th-PR) | DX Q4-2025 and Q1-2026 reports | AI coding agents | 33 days in Q1-2026, down from 39 days (Q4-2025), down from ~66 days pre-AI. **Works**, when the codebase has `CLAUDE.md`-style context. | H |
| 18 | Novice engineers delegating to AI without structured practice | Anthropic RCT (2026, via third-party summary) | Any coding agent | **Breaks.** 17% lower retention-quiz scores; debugging skills specifically atrophy. Skill-atrophy effect documented. | M |
| 19 | Wharton/BCG "jagged frontier" 758-worker RCT | HBS/Wharton/MIT Sloan/Warwick/BCG (Dell'Acqua et al. 2023) | GPT-4 capability boundary | Tasks inside frontier: +25% speed, +40% quality; **outside: -23%** — over-reliance when boundary is misread. Absorptive capacity at the discipline level predicts response. | H |
| 20 | Lab-Crowd-Leadership model (identify 2% power users, CEO sponsorship, cash/promotion incentives for sharing) | Mollick (Cybernetic Teammate; Insight partners interview) | Cross-tool | **Works** as absorptive-capacity accelerant. High-performer firms in McKinsey 2025 are 3× more likely to report strong senior role-modelling. | H |
| 21 | Slack-channel AI Q&A bots (Salesforce ~70,000 employees late-2024) | Salesforce | Slack AI features 2024–2026 | Mixed. 40% reduction in repeated Slack questions reported within 90 days of structured feedback loops (Gartner 2024). Survival depends on on-going evaluator feedback. | M |
| 22 | Shared skills/catalog governance (trust registries) | Agent Skills Catalog; tech-leads-club registry; Atlassian TWG CLI | Agent Skills standardization Oct-2025 | **Survives** because the standard is agent-agnostic (Cursor, Copilot, Claude Code, Antigravity all read it). | M |
| 23 | Palantir Learn role-based bootcamps ("Foundry & AIP Aware") | Palantir | AIP product evolution | **Survives** as a structural asset — bootcamp curricula and certifications decouple learning from any one model version. | M |
| 24 | GitLab Handbook-first culture applied to AI Usage Principles and AI feature development playbook | GitLab (docs.gitlab.com, handbook.gitlab.com) | GitLab Duo, model changes | **Survives**: handbook is version-controlled text; new AI sections added rather than rewritten. A direct inheritance from an all-remote documentation culture. | H |

Confidence ladder observation: mechanisms that **externalize knowledge into version-controlled text** (rows 1, 2, 3, 8, 9, 24) are the highest-confidence survivors; mechanisms that **depend on a central curator** (row 5) are the highest-confidence failures.

---

## 3. Pattern findings

### 3.1 Five theoretical lenses mapped to concrete AI-era mechanisms

| Lens | AI-era mechanism that realizes it | Failure mode if absent |
|---|---|---|
| **Senge — shared mental models** | `CLAUDE.md` / team-OS root file; handbook-first docs (GitLab). Converts individual working theories into shared text that humans *and* AI agents read. | Tacit, tool-specific folklore that re-resets every tool change. |
| **Senge — team learning** | Weekly demos, AMAs, guild channels, paired use with senior engineer. | Silent power users; 2% of staff build leverage, 98% stall at "silicon ceiling" (BCG AI at Work 2025). |
| **Senge — personal mastery** | Role-based capability training ≥5 h, in-person coaching, certification bootcamps (Palantir Learn, Google Skills). | "Proper training" covers only ~33% of employees (BCG 2025). |
| **Senge — systems thinking** | Evaluator-driven development (Hamel / Eugene Yan), CI-gated prompt merges (Braintrust), prompt versioning (Langfuse). | Teams "tweak and hope"; silent regressions after model swap. |
| **Cohen & Levinthal — absorptive capacity = prior knowledge × diversity × integration** | Prior knowledge: written runbooks, APIs, schemas. Diversity: cross-functional guilds; 2%-power-user cohorts (Mollick). Integration: skills registry + MCP servers binding AI to existing workflows. | Dell'Acqua et al. 2023: discipline-level absorptive capacity predicts whether GPT-4 helps or hurts — below a threshold, adoption produces the *-23% outside-the-frontier* regression. |
| **Argyris — single-loop / double-loop** | Single-loop = prompt edit, eval re-run, ship. Double-loop = re-evaluation of which tasks belong to AI at all (Klarna reversal is forced double-loop after single-loop failure; Shopify "prove AI can't do it before hiring" memo is intentional double-loop). | Enterprises stuck at pilot (Gartner: 94–95%) are stuck in single-loop: tuning an approach that a double-loop review would scrap. |
| **March — exploration / exploitation** | Exploration: lab / crowd / 2% power users. Exploitation: version-controlled playbooks, skills registries, blueprints. Needs *both*. | Pure exploration = abandoned experiments. Pure exploitation = stale library. The "prompt library burnout" pattern is exploitation without exploration channel. |
| **Nonaka — SECI spiral** | **S**ocialization: AMAs, demos, pair work. **E**xternalization: `CLAUDE.md`, playbooks, runbooks, skills. **C**ombination: skills registries, eval suites, Roast/Minions-style composed workflows. **I**nternalization: hands-on practice under coaching (the 5-h threshold in BCG 2025). | If E is missing, tacit knowledge dies when the power user leaves or tools change. If C is missing, knowledge accumulates locally but never becomes organizational. GenAI-SECI and HAC-SECI research (2025) argues AI agents act as an additional agent layer in the spiral. |

**Headline (high confidence):** survival under tool flux tracks with how completely an organization executes the **externalization** and **combination** steps of Nonaka's SECI spiral in *version-controlled, agent-readable* form.

### 3.2 The fast loop and the slow loop (system dynamics)

Two coupled loops, different time constants:

- **Fast loop — AI use to artefact.** Practitioner opens an agent, drafts a workflow, saves a prompt/skill. Time constant: minutes to days. Reinforcing loop R1: "more usage → more artefacts → more visible leverage → more usage." This is what BCG's 70/20/10 and Shopify's weekly-demo ritual accelerate. This is also what "prompt library burnout" chokes when artefacts outpace maintenance capacity.
- **Slow loop — artefact to durable learning.** Artefacts are externalized into `CLAUDE.md`, skills, evaluators, handbook sections; combined and certified via training, bootcamps, guilds; internalized into role descriptions and onboarding. Time constant: weeks to months. Balancing loop B1: "artefacts grow → maintenance cost grows → staleness grows → usage drops → artefact growth slows." Balancing loop B2: "evaluator coverage grows → regression detection grows → double-loop reviews triggered → scope of AI use re-drawn."

The slow loop is what keeps the fast loop productive. **If the fast loop runs without the slow loop, the organization accumulates artefacts faster than it can integrate them, and staleness kills usage** — the Confluence/SharePoint failure mode re-enacted at prompt scale (ALM Corp / Will Kelly). **If the slow loop runs without the fast loop, the organization has beautiful documentation of AI practices that no one uses.**

Leverage points in Meadows's sense:
- Highest: mental model shift — "prompt library" (artefact-centric) → **skill / blueprint / evaluator** (process-centric). Observed in Stripe Minions (blueprints), Shopify Roast (workflows), Anthropic/Atlassian (skills).
- High: feedback delay reduction — CI-gated evals (Braintrust) collapse the detection delay on regressions; skills registries collapse the discovery delay on reusable knowledge.
- Medium: stock buffers — Palantir Learn, Google Skills, BCG 5-h training threshold increase *personal-mastery* stock faster than tools can drain it.
- Low: parameter tweaks — renaming "prompt engineer" to "context engineer" (summer 2025) is parameter-level and produces no durable change on its own.

### 3.3 Tooling-invariant structures — the "ilities" of learning

Borrowing MBSE *ilities* (modularity, evolvability, scalability, portability, observability), the structures that repeatedly survive are:

- **Modularity** — knowledge unit is a *skill* or *playbook* with a contract (inputs, outputs, evaluator), not a paragraph in a wiki. Agent Skills standard (Anthropic Oct-2025, GitHub Copilot, Cursor, Atlassian TWG CLI) is modularity at the ecosystem level.
- **Evolvability** — text artefacts in git; prompts and skills versioned (Langfuse, Braintrust, LangSmith). New model version prompts a diff review, not a rewrite.
- **Scalability** — the same artefact serves one team and then 100 teams (Roast: 500 DAU; Minions: 1,300 PRs/wk). Central curator models do not scale; federated ownership with registry discovery does.
- **Portability** — handbook-first + plain markdown (GitLab, Anthropic CLAUDE.md) is portable across models and across agents.
- **Observability** — evaluator suites and production traces (Eugene Yan, Hamel Husain) make regressions legible. Without observability, tool-change events become silent quality shocks (Klarna).

**Headline (high confidence):** the *format* of the learning artefact determines survival more than the *content*. Markdown in git + an executable evaluator survives. A Notion page curated by one person does not.

### 3.4 What breaks (negative evidence, high confidence)

1. **Central-curator prompt libraries.** Above stated staleness thresholds (60 / 80 / 90%) the library is already dead. A single "prompt engineer" or ops team cannot maintain institutional knowledge across dozens of departments and hundreds of workflows.
2. **Tool-branded training divorced from role.** Microsoft Copilot enterprise stalls (~5–6% past pilot, penetration ~3%) are partly a training-curriculum problem: generic "use Copilot" classes do not change role-level workflows.
3. **Replacement without learning loop.** Klarna (2024 → 2026 reversal) substituted AI for ~700 CS agents without a structured feedback loop that captured the tacit edge-case knowledge; CSAT dropped on complex interactions; rehiring underway.
4. **Delegation without practice.** Anthropic RCT (2026): novices delegating code to AI show -17% retention and debug-skill atrophy. Addy Osmani and others document the same pattern. Threatens the slow loop by hollowing out personal-mastery stock.
5. **Adoption-before-evaluators.** Organizations that deploy prompts without `evals` cannot detect regressions when a model swaps under them. "An LLM-as-Judge won't save the product — fixing your process will" (Eugene Yan) — evaluators are necessary but not sufficient; the surrounding process must also be tight.
6. **PR-restructuring instead of structural restructuring.** BCG AI at Work 2025: 75% of leaders claim weekly AI use vs 50% of frontline — claimed transformation is top-heavy. O1-type public re-orgs that don't alter workflows produce no EBIT lift (McKinsey Nov-2025: "workflow redesign is the biggest single lever").
7. **Artefacts produced by the fast loop without the slow loop.** A Slack channel full of clever prompts with no exporter to a shared registry loses 60–80% of them to channel scrollback within weeks.

### 3.5 What survives (positive pattern, high confidence)

Cross-case, these coexist in every survivor:

1. A **root context file** in the project/team repo (`CLAUDE.md` + nested) that any new agent reads automatically.
2. A **modular skill or playbook format** (Skills, Roast workflows, Minions blueprints) with an evaluator attached.
3. A **version-controlled registry** (internal or federated; Atlassian skills, Agent Skills Catalog) with discovery and trust metadata.
4. An **evaluator culture** (Hamel / Eugene Yan / Braintrust / LangSmith) treating prompt changes as code changes that go through CI.
5. **Role-based training ≥5 h with coaching** (BCG threshold) rather than tool-branded webinars.
6. **Leadership role-modelling + incentives for sharing** (Mollick Leadership-Lab-Crowd; Shopify memo; McKinsey 2025 high-performer 3× role-modelling).
7. **Guilds / AMAs / weekly demos** — Nonaka-socialization ritual, tool-invariant.
8. **Double-loop triggers** — explicit review of whether AI should be doing a task at all (Klarna hindsight; Shopify "prove AI can't" memo; "jagged frontier" task triage).

### 3.6 Maturity model — the primary artefact

A five-level maturity model for AI-era organizational learning, in Crawley/Rhodes MBSE style (capability statements, evaluation criteria, typical artefacts, transition trigger to next level).

**Level 1 — Static documentation.**
- *Capability:* Practitioners read a wiki page or PDF about "how to use AI."
- *Artefacts:* Notion pages, SharePoint, onboarding slide deck.
- *Dynamics:* Single-loop. Fast loop local to individuals; no slow loop. External to agents (no `CLAUDE.md`).
- *Failure mode:* staleness within one model generation; "silicon ceiling" at ~50% usage, ~33% properly trained (BCG 2025).
- *Transition trigger to L2:* leadership commits to an internal prompt/skill library.

**Level 2 — Prompt library with version tracking.**
- *Capability:* Centralized library of prompts / templates; owned team maintains it; versions tracked in a tool (Langfuse/Braintrust/LangSmith or home-grown).
- *Artefacts:* library UI, prompt files, tag taxonomy.
- *Dynamics:* Fast loop produces artefacts; slow loop still manual and curator-dependent.
- *Failure mode:* prompt library burnout (≥60% staleness); curator bottleneck at ~hundreds of prompts; survives the *first* model change but not the *fourth*.
- *Transition trigger to L3:* curator realizes they cannot maintain coverage; failures become visible via missed regressions.

**Level 3 — Living playbook with evaluators.**
- *Capability:* Artefacts (playbooks, skills, runbooks) live in version control next to code; every major artefact carries an evaluator; CI gates merge; onboarding reads the same files AI agents read.
- *Artefacts:* `CLAUDE.md` + nested; skills directory (`.github/skills/` or equivalent); eval suites; CI pipelines; prompt and eval diffs in PRs.
- *Dynamics:* Fast and slow loops both present and coupled; B2 (regression detection) active; R1 (usage-leverage) reinforcing without triggering the staleness failure.
- *Failure mode:* coverage unequal across teams; two-speed org — Stripe Minions-grade in one team, L1 documentation across the hall.
- *Transition trigger to L4:* leadership wants organizational, not team-level, consistency; duplicated work across teams becomes expensive.

**Level 4 — Continuous-learning feedback loop with shared registry and governance.**
- *Capability:* Federated ownership model where every team contributes skills / blueprints / evaluators to a shared registry with trust metadata; agents across vendors (Claude Code, Copilot, Cursor, Rovo, Antigravity) read the same skill definitions. Role-based training pipeline feeds registry usage. Double-loop triggers are scheduled (not reactive).
- *Artefacts:* internal skills registry, Agent-Skills-standard adoption, training cadence calendar, guild / CoP structure with time budget, dashboards for staleness, evaluator coverage, and capability-to-deployment lag.
- *Dynamics:* explicit management of exploration (labs, 2%-crowd) and exploitation (registry, playbooks) budgets; SECI complete (S via guilds, E via skills, C via registry + evals, I via training-and-coaching threshold).
- *Failure mode:* governance overhead; registry becomes a gatekeeper bottleneck if not federated; risk of "certified skills" calcifying when model capability jumps.
- *Transition trigger to L5:* organization can measure *itself* learning — that is, the registry + evaluators + dashboards produce second-order observations that feed strategy.

**Level 5 — Integrated human-and-AI learning with governance and measurement.**
- *Capability:* Learning velocity is itself a measured, budgeted capability, aligned with an adaptability thesis (e.g. from M1 causal-loop map / M2 indicator dashboard). Role definitions, promotions, compensation, and budget decisions reference learning-velocity indicators (capability-to-deployment lag, model-swap cost, role-redefinition cadence, staleness ratio). AI agents participate in the SECI spiral as reliable, versioned agent-layer contributors (HAC-SECI). Double-loop review is institutional, triggered by both eval drift and strategy review.
- *Artefacts:* executive dashboard (O3 indicators + M2 adaptability indicators); HR policy tied to training hours + coaching; promotion criteria referencing capability-to-deployment lag; board-level reporting on AI-capability-from-releases-<6-months-old revenue share.
- *Dynamics:* two coupled loops plus a meta-loop that re-budgets between them by strategic review cadence. Hollnagel-style resilience: graceful degradation under tool-generation shock; rapid re-configuration when the frontier moves.
- *Observed instances (2026-04):* none fully. Closest partial instances: Anthropic internal (strong on L3–L4 patterns, visible artefacts); Stripe (L3–L4 in developer productivity domain specifically via Minions); Shopify (L3 patterns plus leadership ritual); Palantir (L3–L4 in enterprise-delivery via Learn + AIP). This is therefore a *target* level rather than a *documented* level — speculative for L5, labelled as such.

**Self-assessment questions per level.**
- L1 → L2: "Do we have a single maintained place where a new hire finds our current AI prompts and skills?"
- L2 → L3: "When the model changes under us, do we detect regressions automatically, or do users report them?"
- L3 → L4: "Can a team in another part of the org discover and safely reuse a skill we built?"
- L4 → L5: "Can we report learning velocity as a number, and does it influence resource allocation?"

---

## 4. Open questions and negative evidence

**Open questions.**
1. What is the empirical decay rate of a "Level 2" prompt library — is the 60/80/90 staleness ladder (ALM Corp / Kelly) a distribution or a threshold phenomenon? A longitudinal study on a real library would resolve whether decay is linear-in-time or driven by discrete tool-change events.
2. Does the 5-hour training threshold (BCG AI at Work 2025) generalize across frontline vs knowledge-worker roles, or is it specific to knowledge-worker pilots?
3. The HAC-SECI / GRAI / GenAI-SECI extensions to Nonaka (2025 academic literature) are proposed models; they are not yet empirically calibrated against a firm's tool-change history. Which of the three actually predicts survival?
4. Anthropic's RCT on novice skill atrophy (2026) is a strong signal but is not replicated; how does deskilling interact with double-loop learning in practice? Does evaluator culture (Level 3) protect against skill atrophy by keeping humans in the judging loop?
5. What is the relationship between role redefinition cadence (O2) and learning velocity? Hypothesis: firms that redefine roles too often destroy personal-mastery stock; firms that redefine too rarely leave absorptive-capacity on the table.
6. Klarna's reversal is about *customer-service tacit knowledge lost*; what is the parallel risk for engineering teams that aggressively delegate to coding agents? Is there a "tacit debugging knowledge" stock that is currently being drained?

**Negative evidence explicitly looked for and not found.**
- **Public longitudinal data on prompt-library staleness at a named firm.** The 60/80/90 heuristic is published by practitioners but not corroborated by a named firm's internal audit. Medium-term research gap.
- **Measured onboarding velocity for *AI tool usage* itself** (distinct from onboarding to a codebase). DX Q1-2026 measures time-to-10th-PR, which bundles tool ramp-up and codebase ramp-up; the disentanglement has not been published.
- **Survival rates for AMAs and guilds over multi-year periods.** Anecdotally strong; quantitatively thin.
- **Failure cases of skills registries.** Registries are new (Agent Skills standard Oct-2025); not enough time has passed for mature failure data. Expect "skills registry burnout" analogue to emerge by 2027 in slow organizations.
- **Direct evidence of "double-loop learning frequency" as a measurable construct.** Argyris framed it conceptually; operationalization for AI-era firms is an open construct-validity problem that feeds M2.

---

## 5. Three-pillar feed

How O3 findings feed the **AI usage × Organization × Technical infrastructure** adaptability frame, linked to the anchor questions.

**To Pillar 1 — AI usage.** Organizational learning velocity is the limiting resource on how fast an organization can *use* a new AI capability. The A2 capability-to-adoption lag curve has a *lower bound* set by the slow loop's time constant. A Level-2 org cannot usefully adopt capabilities that change every quarter — it will accumulate staleness faster than it can internalize. A Level-3+ org (evals + playbooks) can track the A2 frontier within a few weeks, because its fast and slow loops run concurrently. Therefore A1 (model transition management) and A3 (workflow retooling) patterns are downstream of this memo's maturity level.

**To Pillar 2 — Organization (self-reinforcement).** O1 (human-AI collaboration) and O2 (role redefinition) co-depend with O3. Roles created in O2 (model evaluator, AI ops, forward-deployed engineer, prompt/context engineer, agent orchestrator) are *containers* for the SECI spiral: without them, externalization and combination happen by accident. The O1 collaboration model determines whether the 2% power users (Mollick) spread or hoard. A learning-velocity investment strengthens O1 and O2 outcomes; an O1/O2 restructuring without O3 investment produces hollow public re-orgs.

**To Pillar 3 — Technical infrastructure.** T1 (build vs rent), T2 (compute scaling), T3 (technical debt) each require the organizational substrate described here. In particular:
- T3 prompts-as-code, evaluator drift, RAG pipeline maintenance — these are simultaneously *technical-debt* problems and *organizational-learning* problems. An evaluator suite with no team that reads its results is noise.
- T1 multi-provider routing decisions depend on whether the org can re-read and re-certify its skills across providers (Agent Skills standard is the key interface here — the tech infrastructure is ready, and the organizational learning maturity determines whether the option is actually exercisable).

**To the two anchor questions.**
- *Engineering* ("how is the decision-making infrastructure built?"): build it with the **SECI-complete, modular, evolvable, observable** properties named in §3.3. The concrete artefact set is `CLAUDE.md` + skills + evaluators + registry, in version control, with CI gates.
- *Managerial* ("what operational and governance structures are required?"): at minimum, Level 3 maturity — role-based ≥5 h training, guilds with time budgets, evaluator culture, federated skill ownership. Level 4 when scale demands registry governance. Level 5 when learning velocity becomes a reporting and budgeting category in its own right.

**Feeds to M1 (system dynamics map):** supplies the fast loop / slow loop pair and balancing loops B1 (staleness) and B2 (regression detection) as candidate causal-loop-diagram components.

**Feeds to M2 (adaptability indicators):** four candidate measurable indicators from this memo:
- *Staleness ratio* of the skill/playbook registry (fraction of artefacts not invoked in last N days relative to rolling average).
- *Evaluator coverage* of deployed AI-dependent workflows (fraction of prompts with a passing CI-gated eval).
- *Onboarding velocity* specifically to AI-tool usage (time-to-first-productive-skill-invocation by a new hire).
- *Double-loop frequency* — count of scheduled reviews that revise the scope of AI use (distinct from single-loop prompt edits).

---

## References (primary and public)

- Anthropic. "How Anthropic teams use Claude Code" (2025). <https://claude.com/blog/how-anthropic-teams-use-claude-code>
- Anthropic. "Effective context engineering for AI agents" (2025).
- Anthropic. "Equipping agents for the real world with Agent Skills" (Oct-2025).
- Bessemer Venture Partners — Atlas: "Inside Shopify's AI-first engineering playbook" (2025). <https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook>
- Shopify Engineering. "Introducing Roast: Structured AI workflows made easy" (2025). <https://shopify.engineering/introducing-roast>
- First Round Review. "From Memo to Movement: Shopify's Cultural Adoption of AI" (2025).
- Stripe Dev Blog. "Minions: Stripe's one-shot, end-to-end coding agents" Parts 1 and 2 (2025–2026).
- GitLab Handbook. AI-assisted features; AI Usage Principles; AI feature development playbook.
- Atlassian Support. Rovo documentation; TWG CLI Agent Skills (2025).
- Dell'Acqua, F., McFowland, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., Lakhani, K. "Navigating the Jagged Technological Frontier" (2023; Organization Science publication 2025).
- Mollick, E. "The Cybernetic Teammate" (2025, P&G field experiment).
- Brynjolfsson, E., Li, D., Raymond, L. "Generative AI at Work" (MIT Sloan / NBER).
- BCG. "AI at Work 2025: Momentum Builds, but Gaps Remain" (June-2025); "To Unlock the Full Value of AI, Invest in Your People" (2025); "The Widening AI Value Gap" (Oct-2025); "Organizations Combining Organizational Learning and AI-Specific Learning Are up to 80% More Effective at Managing Uncertainty" (Nov-2024).
- McKinsey. "The State of AI" (March-2025); "The State of AI 2025" (Nov-2025).
- Stanford HAI. "AI Index Report 2025."
- DX. "AI-assisted engineering: Q4 2025 impact report"; "AI-assisted engineering: Q1 2026 impact report"; "AI tooling benchmarks: PR throughput and usage by tool (Q1 2026)."
- Gartner — cited in Creati AI news (Feb-2026) and Xenoss summary: enterprise Copilot pilot-to-scale rates.
- Husain, H. Evals writings at hamel.dev; Maven course "AI Evals for Engineers & PMs."
- Yan, E. Writings at eugeneyan.com on product evals, LLM-evaluators, eval-driven development.
- Kelly, W. "Stop building prompt libraries. Start building prompt ownership." (2025).
- ALM Corp. "Prompt Library Burnout" (2025).
- Klarna reversal coverage: Fast Company, mlq.ai, Tech.co, HR Director (2025–2026).
- Stulberg, H. "Claude Code Team OS" (public talk / news.aakashg.com, 2026).
- Argyris, C. "Double-Loop Learning in Organizations" (HBR 1977); Argyris & Schön "Theory in Practice" (1974).
- Cohen, W., Levinthal, D. "Absorptive Capacity: A New Perspective on Learning and Innovation" (1990).
- March, J. "Exploration and Exploitation in Organizational Learning" (1991).
- Nonaka, I. "A Dynamic Theory of Organizational Knowledge Creation" (1994).
- Senge, P. "The Fifth Discipline" (1990).
- Meadows, D. "Leverage Points: Places to Intervene in a System" (1999).
- GenAI-SECI / GRAI / HAC-SECI proposals, 2025 academic literature (RealKM syntheses; arxiv working papers).
