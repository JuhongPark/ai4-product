# AI Rapid Prototyping: v0, Lovable, Bolt, Replit Agent, Figma Make

> **Date:** 2026-04-21
> **Scope:** Platform growth data, product evolution (2024–2026)

---

## 1. Summary

Between 2024 and 2026, a new class of tool emerged — **text-to-app** platforms that compress idea → working prototype from days to minutes. These tools are reorganizing startup productization: PMs and designers ship functional prototypes; engineers hand off from *prototype*, not from spec.

---

## 2. The Landscape (2026)

| Platform | Sweet spot | Notable metric |
|---|---|---|
| **v0 (Vercel)** | UI generation, React + Next.js + shadcn/ui | 6M+ developers (March 2026); Feb 2026 update made it production-ready full-stack |
| **Lovable** | Non-technical PM flows, natural-language app creation | $20M ARR in 2 months (fastest European startup growth) |
| **Bolt.new** | Browser-native polished IDE experience | Fastest idea → demo iteration |
| **Replit Agent** | Full-stack with built-in DB/auth/hosting | $1.16B valuation |
| **Figma Make** | Prompt-to-UI with design-system coherence | Design-to-code continuity |

---

## 3. v0 Evolution: Prototyping → Production

v0 started in 2023 as a text-to-component experiment. By February 2026, it had expanded:

- **Git integration**
- **VS Code-style editor**
- **Database connectivity**
- **Agentic workflows**
- **Production deployment pipeline**

This trajectory mirrors other platforms: each started as "prototyping-only," all moved toward production because the hand-off friction to traditional codebases was too high.

---

## 4. Lovable: The Non-Technical Founder Path

Lovable's growth ($20M ARR in 2 months) reveals a latent market: **non-technical founders and PMs who want to ship functional software without engineers**. It is the canonical example of *vibe coding for builders* (see [vibe-coding-agentic-engineering.md](vibe-coding-agentic-engineering.md)).

Limits:
- Generated applications often skip auth/security production rigor
- Scaling the generated code beyond MVP frequently requires full engineer rewrite
- Platform lock-in — applications depend on Lovable's runtime

---

## 5. Workflow Shift: PM-to-Pixel

Historical: PM writes PRD → designer mocks → engineer builds.
2026: PM prompts prototype → engineer refines → designer informs.

Engineers increasingly start from the latest prototype and use Cursor/Windsurf/Claude Code to get it production-ready, rather than starting from scratch.

This is a structural shift in the productization pipeline — compressing the idea-to-shipped-feature loop.

---

## 6. When Each Tool Wins

| Use case | Best tool |
|---|---|
| Pure UI from design brief | v0 |
| Non-technical founder building SaaS | Lovable |
| Browser-first interactive demo | Bolt.new |
| Full-stack app with DB/auth | Replit Agent |
| Design-system-consistent UI from Figma | Figma Make |

Most teams mix: Lovable/Bolt for rapid exploration; v0 for UI-heavy components; Cursor/Claude Code for production hardening.

---

## 7. Research Gaps

1. **Production survival rate** — What fraction of prototypes built in these tools reach production? Unpublished
2. **Quality of generated architecture** — How often does the generated code meet production scalability/security norms?
3. **Integration friction** — When handed off to engineering, how much is rewritten vs. retained?
4. **Non-engineer adoption** — Who actually builds with these? Demographics, success rates, retention — all unmeasured publicly

---

## 8. Sources

- News.aakashg. "Ultimate Guide to AI Prototyping Tools." https://www.news.aakashg.com/p/ai-prototyping-tutorial
- Medium (Anna Arteeva). "Choosing your AI prototyping stack." https://annaarteeva.medium.com/choosing-your-ai-prototyping-stack-lovable-v0-bolt-replit-cursor-magic-patterns-compared-9a5194f163e9
- Addyo Substack. "AI-Driven Prototyping: v0, Bolt, and Lovable Compared." https://addyo.substack.com/p/ai-driven-prototyping-v0-bolt-and
- Capacity.so. "What Is V0.dev? Vercel's AI UI Builder Explained (2026)." https://capacity.so/blog/what-is-v0-dev
- Vercel. "Announcing v0: Generative UI." https://vercel.com/blog/announcing-v0-generative-ui
- Vercel. "AI SDK 3.0." https://vercel.com/blog/ai-sdk-3-generative-ui
- NxCode. "v0 by Vercel: Complete Guide 2026." https://www.nxcode.io/resources/news/v0-by-vercel-complete-guide-2026
- Emergent.sh. "Bolt vs Replit vs Lovable." https://emergent.sh/learn/bolt-new-vs-replit-vs-lovable-vs-emergent
- Lovable. "Best Vibe Coding Tools in 2026." https://lovable.dev/guides/best-vibe-coding-tools-2026-build-apps-chatting
- GetMocha. "Best AI App Builder 2026." https://getmocha.com/blog/best-ai-app-builder-2026/
