# AI for Productization Skills (제품 구현)

> Scope: Application of AI to **product implementation itself** — code generation, UI/UX construction, prototyping, testing, and shipping. Excludes upstream discovery, management meta-layer, and downstream sales/growth activities.

This area is a reframe of "AI for Product" around the **engineering and construction** dimensions of building a product, distinct from monetization. Productization Skills here includes:

- **B1. Code Generation & Assistance** — Copilot, Cursor, Claude Code, Devin-class agents
- **B2. Rapid Prototyping & Generative UI** — v0, Lovable, Bolt, Replit Agent, Figma Make
- **B3. Test Automation & QA** — Self-healing tests, AI test generation, AI in CI/CD
- **B4. AI-Assisted Refactoring & Architecture** — Structural code changes, migrations
- **B5. Vibe Coding / Agentic Engineering** — Paradigm shift from writing code to steering intent

This complementary pair with [sales-skills/](../sales-skills/) divides the product-building skillset into **"what gets built"** (productization) vs **"how it is monetized and capitalized"** (sales).

---

## Sub-topics

### B1. Code Generation & Assistance
- GitHub Copilot, Cursor, Claude Code, Codex-class agents
- SWE-bench Verified performance (Opus 4.7: 87.6%, vs Opus 4.6: 80.8%)
- Vendor claims vs. independent empirical evidence (METR RCT)
- Code quality: clone rates, refactoring decline

### B2. Rapid Prototyping & Generative UI
- v0 (Vercel): 6M+ developers, full-stack agentic platform (Feb 2026)
- Lovable (launched Nov 2024): $17M ARR at 4 months → $100M at 8 months → $200M Series A at $1.8B valuation; $330M Series B at $6.6B (Dec 2025)
- Bolt.new, Replit Agent, Figma Make
- PM-to-pixel workflow shift

### B3. Test Automation & QA
- Self-healing tests: UI changes auto-repaired
- AI test generation: 8.3% flaky rate (Pysmennyi et al. 2025)
- CI/CD: test cycle times down up to 80%
- Adoption: 75% prioritize AI testing, only 16% implemented

### B4. AI-Assisted Refactoring & Architecture
- AI outperforms humans on correctness of implementing refactoring practices
- Humans still superior at problem identification and quality-attribute trade-offs
- Missing context cited by 65% of developers as top refactoring barrier
- Refactored-line share dropped 25% (2021) → <10% (2024)

### B5. Vibe Coding / Agentic Engineering
- Karpathy paradigm (early 2025) → "agentic engineering" reframe (late 2025)
- 41% of code AI-generated globally; 92% US developer daily usage
- Founders compress idea → working product to days
- Security: 2.74x more vulnerabilities in AI-generated code

---

## Key Stats (2026)

### Adoption & Market
- **73%** of developers use AI coding tools regularly (up from 45% in 2023)
- **84%** of developers use or plan to use AI in dev workflow (Stack Overflow 2025)
- **42%** of committed code is AI-assisted
- **v0 by Vercel**: 6M+ developers on platform (March 2026)
- **Claude Code**: 18% adoption, 91% CSAT (highest of any AI coding tool)

### Performance
- **Claude Opus 4.7**: 87.6% on SWE-bench Verified (+7pt vs 4.6); Gemini 3.1 Pro 80.6%
- **Cursor study (UChicago)**: +39% merged PRs
- **GitHub Copilot vendor study**: 55% faster task completion
- **METR RCT (2025)**: experienced OSS devs **19% SLOWER** with AI — self-report says 20% faster; 2026-02 follow-up suggests selection-bias makes the true number unresolved

### Test Automation
- **89%** of orgs piloting GenAI-augmented QA; **19%** productivity gain
- By 2026: **40%** of large enterprises integrate AI into CI/CD
- Test cycle time reduction: up to **80%** (impact-aware test selection)

---

## Research Gaps

1. **Productivity paradox** — Vendor-reported gains (50–100%) vs. independent METR RCT (-19% in 2025, flipped in unreliable 2026 replication); mechanism and true magnitude both unresolved
2. **Code quality long-term effects** — 4x growth in code clones (GitClear); refactoring share declining — hidden technical debt
3. **Full SDLC automation** — EY.ai PDLC (80x acceleration claim) lacks independent verification; Devin at 15% success on independent tests
4. **Vibe coding safety** — AI-generated code 1.7x more likely to have major issues, 2.74x more vulnerable to security issues; no accepted safety framework
5. **Human-AI complementarity in engineering** — Nature 2024 meta-analysis finds Human+AI does NOT beat AI alone for decision tasks; implications for code review/architecture unclear
6. **Measurement crisis** — No accepted benchmark reflecting real-world developer value; SWE-bench ≠ production; DORA metrics not updated for AI
7. **Narrow-task vs. agentic** — Tools narrow on tasks (Copilot) still outperform broad agents (Devin) in production, but investment flows to agentic

---

## Papers in this directory

### B1. Code Generation & Review
- [ai-coding-assistants-2026.md](papers/ai-coding-assistants-2026.md) — Copilot, Cursor, Claude Code, SWE-bench
- [ai-code-review.md](papers/ai-code-review.md) — CodeRabbit, Copilot review, PR automation
- [ai-code-refactoring.md](papers/ai-code-refactoring.md) — Structural refactoring, human-AI split
- [vibe-coding-agentic-engineering.md](papers/vibe-coding-agentic-engineering.md) — Paradigm shift and limits
- [metr-productivity-paradox.md](papers/metr-productivity-paradox.md) — METR RCT and the measurement crisis

### B2. Prototyping & Build
- [ai-rapid-prototyping.md](papers/ai-rapid-prototyping.md) — v0, Lovable, Bolt, Replit Agent, Figma Make

### B3. Test, Secure, Operate
- [ai-test-automation-2026.md](papers/ai-test-automation-2026.md) — Self-healing, CI/CD integration
- [ai-devsecops-security.md](papers/ai-devsecops-security.md) — Snyk, AI-generated code vulnerabilities
- [ai-sre-incident-response.md](papers/ai-sre-incident-response.md) — Azure SRE Agent, agentic DevOps

### B4. Modernization
- [ai-legacy-modernization.md](papers/ai-legacy-modernization.md) — COBOL/mainframe, Claude Code, IBM Project Bob
