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

### 4.1 Sales coverage (mostly new to this repo — 12 papers)

See [research/sales-skills/](../research/sales-skills/):

**A1. Selling**
| Topic | Paper |
|---|---|
| Agentic AI SDR | [ai-sales-automation-agentic-sdr.md](../research/sales-skills/papers/ai-sales-automation-agentic-sdr.md) |
| Revenue Operations | [ai-revenue-operations.md](../research/sales-skills/papers/ai-revenue-operations.md) |
| Account-Based Marketing + intent data | [ai-abm-intent-data.md](../research/sales-skills/papers/ai-abm-intent-data.md) |
| Customer Success + retention | [ai-customer-success.md](../research/sales-skills/papers/ai-customer-success.md) |
| Sales coaching + call intelligence | [ai-sales-coaching-conversation.md](../research/sales-skills/papers/ai-sales-coaching-conversation.md) |
| Dynamic pricing | [ai-dynamic-pricing.md](../research/sales-skills/papers/ai-dynamic-pricing.md) |
| Forecasting, CLV, churn | [ai-sales-forecasting-clv.md](../research/sales-skills/papers/ai-sales-forecasting-clv.md) |
| B2C conversational commerce | [ai-conversational-commerce.md](../research/sales-skills/papers/ai-conversational-commerce.md) |
| Negotiation & contract automation | [ai-negotiation-contract.md](../research/sales-skills/papers/ai-negotiation-contract.md) |

**A2. Investing & Fundraising**
| Topic | Paper |
|---|---|
| AI pitch decks + fundraising | [ai-pitch-deck-fundraising.md](../research/sales-skills/papers/ai-pitch-deck-fundraising.md) |
| Investor Relations automation | [ai-investor-relations.md](../research/sales-skills/papers/ai-investor-relations.md) |
| VC deal sourcing + DD | [ai-vc-deal-sourcing-dd.md](../research/sales-skills/papers/ai-vc-deal-sourcing-dd.md) |

### 4.2 Productization coverage (2026 empirical layer — 10 papers)

See [research/productization-skills/](../research/productization-skills/):

**B1. Code generation & review**
| Topic | Paper |
|---|---|
| AI coding assistants | [ai-coding-assistants-2026.md](../research/productization-skills/papers/ai-coding-assistants-2026.md) |
| Code review (CodeRabbit, Copilot) | [ai-code-review.md](../research/productization-skills/papers/ai-code-review.md) |
| Refactoring | [ai-code-refactoring.md](../research/productization-skills/papers/ai-code-refactoring.md) |
| Vibe coding paradigm | [vibe-coding-agentic-engineering.md](../research/productization-skills/papers/vibe-coding-agentic-engineering.md) |
| METR productivity paradox | [metr-productivity-paradox.md](../research/productization-skills/papers/metr-productivity-paradox.md) |

**B2. Prototyping & build**
| Topic | Paper |
|---|---|
| Rapid prototyping (v0/Lovable/Bolt/Replit/Figma Make) | [ai-rapid-prototyping.md](../research/productization-skills/papers/ai-rapid-prototyping.md) |

**B3. Test, secure, operate**
| Topic | Paper |
|---|---|
| Test automation | [ai-test-automation-2026.md](../research/productization-skills/papers/ai-test-automation-2026.md) |
| DevSecOps (Snyk, AI code vulnerabilities) | [ai-devsecops-security.md](../research/productization-skills/papers/ai-devsecops-security.md) |
| SRE & incident response | [ai-sre-incident-response.md](../research/productization-skills/papers/ai-sre-incident-response.md) |

**B4. Modernization**
| Topic | Paper |
|---|---|
| Legacy modernization (COBOL, Project Bob) | [ai-legacy-modernization.md](../research/productization-skills/papers/ai-legacy-modernization.md) |

### 4.3 Cross-cutting coverage (new — 4 papers)

Not strictly sales or productization, but shaping both:

| Topic | Paper |
|---|---|
| EU AI Act enforcement 2026 | [eu-ai-act-product-impact-2026.md](../research/cross-cutting/papers/eu-ai-act-product-impact-2026.md) |
| Korean AI ecosystem | [korean-ai-product-ecosystem-2026.md](../research/cross-cutting/papers/korean-ai-product-ecosystem-2026.md) |
| Solo founder AI stack | [solo-founder-ai-stack.md](../research/cross-cutting/papers/solo-founder-ai-stack.md) |
| AI labor market impact | [ai-labor-market-impact-2026.md](../research/cross-cutting/papers/ai-labor-market-impact-2026.md) |

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
