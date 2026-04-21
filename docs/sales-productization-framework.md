# Sales ↔ Productization: A Skill-Based Frame for AI-for-Product

> **Date:** 2026-04-21
> **Purpose:** Re-frame the repo's lifecycle-organized research through a complementary skill lens — sales (selling + investing) vs. productization (product implementation).

---

## 1. Why This Frame

The main repo organizes AI-for-product research by **product lifecycle phase** (Discovery → Design → Development → Management → Growth). This is the canonical academic framing and traces the product's journey.

This document introduces a complementary frame: **organizing by skill domain**. Building and sustaining a product requires two fundamentally different skill domains:

- **Sales skills** — Turning the product into revenue and capital (selling + investing)
- **Productization skills** — Turning ideas into shipped software (implementation only)

These are **not** competing frames — they are different cross-sections of the same work. The lifecycle frame is best for research synthesis; the skill frame is best for **team composition, hiring, and tool selection**.

---

## 2. Definitions

| Term | Scope |
|---|---|
| **Sales skills** | 판매 + 투자 — GTM, revenue generation, fundraising, investor relations. Ends when a deal closes or a round closes. |
| **Productization skills** | 제품 구현 — Writing, designing, testing, shipping, maintaining code. Ends when code is in production. |

Activities outside both domains (discovery research, management meta-layer, governance, growth strategy) remain in the lifecycle frame but are not the focus of this document.

---

## 3. Lifecycle ↔ Skill Mapping

| Existing lifecycle area | Sales skills? | Productization skills? | Neither (cross-cutting) |
|---|---|---|---|
| [01-discovery](../research/01-discovery/) | Partial — customer insights inform GTM | — | Mostly upstream research |
| [02-design](../research/02-design/) | — | **Yes** — generative UI, AI-driven UX | Trust in AI design |
| [03-development](../research/03-development/) | — | **Yes** — NPD, testing, coding | Firm-level growth (macro) |
| [04-management](../research/04-management/) | — | — | PM tools, meta-layer |
| [05-growth-lifecycle](../research/05-growth-lifecycle/) | Partial — CLV, personalization | Partial — PLM, digital twins | — |
| [cross-cutting](../research/cross-cutting/) | — | — | Human-AI, governance |
| [industry-trends](../research/industry-trends/) | B2B SaaS AI (partial) | Dev tool adoption (partial) | — |

**Key observation**: The repo's coverage of **sales skills is thin** (most activity sits outside the 5-area structure). The coverage of **productization skills is partial** (03-development and 02-design cover core topics, but 2026-specific empirical data on coding assistants, METR, vibe coding is new).

---

## 4. What the Skill Frame Adds

### 4.1 Sales coverage (mostly new to this repo)

See [research/sales-skills/](../research/sales-skills/):

| Topic | Coverage in repo prior | Coverage now |
|---|---|---|
| Agentic AI SDR | None | [ai-sales-automation-agentic-sdr.md](../research/sales-skills/papers/ai-sales-automation-agentic-sdr.md) |
| Revenue Operations | None | [ai-revenue-operations.md](../research/sales-skills/papers/ai-revenue-operations.md) |
| Dynamic Pricing | None | [ai-dynamic-pricing.md](../research/sales-skills/papers/ai-dynamic-pricing.md) |
| Sales forecasting, CLV, churn | None | [ai-sales-forecasting-clv.md](../research/sales-skills/papers/ai-sales-forecasting-clv.md) |
| AI pitch decks + fundraising | None | [ai-pitch-deck-fundraising.md](../research/sales-skills/papers/ai-pitch-deck-fundraising.md) |
| Investor Relations automation | None | [ai-investor-relations.md](../research/sales-skills/papers/ai-investor-relations.md) |
| VC deal sourcing + DD | None | [ai-vc-deal-sourcing-dd.md](../research/sales-skills/papers/ai-vc-deal-sourcing-dd.md) |

### 4.2 Productization coverage (new 2026 empirical layer)

See [research/productization-skills/](../research/productization-skills/):

| Topic | Existing coverage | Added |
|---|---|---|
| AI coding assistants | Mentioned (practical-applications.md) | [ai-coding-assistants-2026.md](../research/productization-skills/papers/ai-coding-assistants-2026.md) — SWE-bench Opus 4.7 87.6%, tool comparison |
| Rapid prototyping (v0/Lovable/Bolt) | Not covered | [ai-rapid-prototyping.md](../research/productization-skills/papers/ai-rapid-prototyping.md) |
| Test automation | 03-development has it | [ai-test-automation-2026.md](../research/productization-skills/papers/ai-test-automation-2026.md) — 2026 adoption & CI/CD integration |
| Refactoring | Not dedicated | [ai-code-refactoring.md](../research/productization-skills/papers/ai-code-refactoring.md) |
| Vibe coding paradigm | Not covered | [vibe-coding-agentic-engineering.md](../research/productization-skills/papers/vibe-coding-agentic-engineering.md) |
| METR productivity RCT | Not covered | [metr-productivity-paradox.md](../research/productization-skills/papers/metr-productivity-paradox.md) |

---

## 5. Cross-Frame Insights

### 5.1 Parallel Productivity Paradoxes

Both domains exhibit the same vendor-vs-independent measurement gap:

| Domain | Vendor claim | Independent evidence |
|---|---|---|
| Productization (code) | +55% faster (GitHub) / +39% more PRs (Cursor) | -19% slower (METR RCT) |
| Sales | +40% productivity, +25% win rate | **<40% of sellers will report AI agents improved productivity by 2028** (Gartner) |

Both point to the same root: **vendor studies use self-selected adopters; real-world deployment has heterogeneous results**.

### 5.2 The Arms Race Pattern

Both domains show two-sided AI adoption creating an arms race:

- **Productization**: AI generates boilerplate → AI reviews boilerplate → signal-to-noise of "shipped lines" degrades
- **Sales (founders vs. VCs)**: AI drafts pitch decks → AI filters pitch decks → differentiation pushed upstream to traction/team
- **Sales (sellers vs. buyers)**: AI writes cold emails → AI filters cold emails → reply rates declining

The arms race compresses **human attention** into smaller but more decisive zones.

### 5.3 Complementarity Zones Map Similarly

Applying the Nature (2024) meta-analysis framework:

| Skill area | Typical task type | Optimal model |
|---|---|---|
| Productization: code generation | Creation | Human+AI (complementarity highest) |
| Productization: refactoring | Mixed (judgment + execution) | Selective |
| Productization: architecture | Decision (strategic) | Human-led |
| Sales: content generation (emails, decks) | Creation | Human+AI |
| Sales: qualification | Decision | AI-led, human-reviewed (emerging) |
| Sales: pricing | Decision under uncertainty | AI-led with bounds |
| Investing: deal sourcing | Pattern matching | AI-led |
| Investing: conviction | Decision (strategic) | Human-led |

This parallels the [Selective Complementarity Framework](../research/cross-cutting/papers/selective-complementarity-framework.md) in cross-cutting research: AI value is task-dependent within each skill area, not uniform.

---

## 6. Team Composition Implications

The skill frame informs 2026 team design decisions:

### 6.1 Sales-skills AI investment
Most organizations can adopt **sales-AI tools off-the-shelf** (Copilot for sales, Gong, Clari, Outreach). Differentiation comes from:
- Data integration (unified RevOps prerequisite)
- Training sales managers (Vorobyeva et al. 2025 literacy gap)
- Governance for outbound outreach ethics

### 6.2 Productization-skills AI investment
Most organizations cannot adopt **productization-AI tools** without engineering changes. Differentiation comes from:
- Codebase readiness (context-supplying tools: Sourcegraph, Cody)
- Engineering practice adaptation (review process, testing norms)
- Team composition (vibe-coder PMs + engineers collaborating)

### 6.3 Investing-skills AI investment
Fundraising teams and investors both adopt AI. Differentiation comes from:
- Proprietary signal sources (AI amplifies signal but doesn't create it)
- Relationship quality (AI-mediated outreach cannot replace trust)
- Speed advantage (faster DD enables better round positioning)

---

## 7. Research Direction Implications

New research gaps emerge from the skill frame that the lifecycle frame obscures:

1. **Full-stack founder productization** — When one person does both sales and productization with AI, what breaks?
2. **Cross-skill AI tool integration** — Sales AI sees product usage → productization AI sees sales feedback. Who owns the loop?
3. **Sales-productization feedback latency** — AI-accelerated sales (days to deal) meets AI-accelerated productization (days to feature); does the organization keep up?
4. **Investor-founder information asymmetry** — When both sides use AI, does capital allocation efficiency improve or degrade?

---

## 8. Related Documents

- [Selective Complementarity Framework](../research/cross-cutting/papers/selective-complementarity-framework.md) — Task-type-based AI-human split
- [Successful 5% Patterns](../research/cross-cutting/papers/successful-5-percent-patterns.md) — 7 patterns from successful AI deployments
- [AI-Augmented Decision Framework (AADM)](../research/04-management/papers/ai-product-decision-framework.md) — D/R/S scoring model
- [Full Automation Reality Check](../research/cross-cutting/papers/ai-full-automation-reality.md) — Why end-to-end autonomy fails

---

## 9. Summary

The skill frame (Sales ↔ Productization) is a complementary lens to the repo's lifecycle frame. It:

1. **Surfaces new research areas** the lifecycle frame missed — AI SDR, dynamic pricing, IR, VC DD
2. **Adds 2026 empirical depth** to productization topics — METR RCT, SWE-bench Opus 4.7, vibe coding
3. **Reveals parallel patterns** — productivity paradoxes, arms races, and complementarity zones apply symmetrically across skill domains
4. **Informs team-composition decisions** — how to adopt AI differs by skill type

Use the lifecycle frame for **research synthesis**; use the skill frame for **organizational design**.
