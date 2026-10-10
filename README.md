# ai4-product

> Research survey on the application of artificial intelligence across the entire product lifecycle — from discovery and research, through design and development, to management, growth, and lifecycle optimization.
## Research Areas

This repository is organized in **three complementary frames** — use whichever matches the question you're asking.

### Layer 3 — AI Systems Design & Management (meta)

Treating AI-for-product as a **systems engineering and management** problem. MIT SDM-canonical methods: architecture, MBSE, system dynamics, socio-technical systems, lifecycle, risk/resilience, tradespace, governance.

→ [docs/ai-systems-design-management-framework.md](docs/ai-systems-design-management-framework.md) · [research/ai-systems/](research/ai-systems/)

### Layer 2 — Skill domain (cross-section)

Cuts the lifecycle by **who does the work**. Useful for team composition, tool selection, budget allocation.

| Skill domain | Covers | Directory |
|---|---|---|
| **Sales skills** (판매 + 투자) | Selling, pricing, CLV/churn, fundraising, IR, VC DD | [research/sales-skills/](research/sales-skills/) |
| **Productization skills** (제품 구현) | Code generation, prototyping, generative UI, test automation, refactoring, vibe coding | [research/productization-skills/](research/productization-skills/) |

→ [docs/sales-productization-framework.md](docs/sales-productization-framework.md)

### Layer 1 — Product lifecycle (phases)

The canonical lifecycle cross-section.

| # | Area | Description |
|---|------|-------------|
| 1 | [Discovery & User Research](research/01-discovery/) | AI-automated UX evaluation, LLM-powered customer insights, synthetic user research |
| 2 | [Design & Prototyping](research/02-design/) | Generative AI in design, adaptive interfaces, trust in AI-designed experiences |
| 3 | [Development & Engineering](research/03-development/) | AI in NPD processes, firm growth impact, time-to-market acceleration |
| 4 | [Management & Decision Making](research/04-management/) | AI-powered PM tools, agentic AI, automated prioritization |
| 5 | [Growth & Lifecycle](research/05-growth-lifecycle/) | PLM, digital twins, personalization, A/B test automation |
| 6 | [Cross-Cutting Themes](research/cross-cutting/) | Human-AI collaboration, responsible AI, AI governance, frameworks & taxonomies |
| 7 | [Industry Trends](research/industry-trends/) | Tech companies, AI startups/tools, consulting reports, industry applications |
| 8 | [MIT Research](research/mit-research/) | MIT labs, researchers, SDM, Sloan predictions |

### Special Topic — Sector verticals

Sector-specific cross-sections that re-apply Layers 1-3 to one industry. Not the main topic, but used to stress-test generic SDM claims against a regulated domain.

| Vertical | Covers | Directory |
|---|---|---|
| **Healthcare / Bio AI** (헬스케어·바이오 AI) | Drug discovery, clinical trials, medical imaging, CDS + ambient scribes, hospital ops, patient-facing, regulation, safety | [research/healthcare-bio-ai/](research/healthcare-bio-ai/) |

→ [docs/healthcare-bio-ai-framework.md](docs/healthcare-bio-ai-framework.md)

### Research Extension — Organizational adaptability

How AI usage, organizational structure, and technical infrastructure change together as AI capabilities evolve. Includes a research plan and eleven draft memos on model transitions, workflow and role redesign, learning, infrastructure, system dynamics, and measurement.

→ [research/adaptability-framework/](research/adaptability-framework/) · [Research plan](research/adaptability-framework/plan.md)

## Project Structure

```
ai4-product/
├── docs/                      # Completed documents
│   ├── survey-report.md       # Full research survey report (lifecycle frame)
│   ├── prototyping-research-plan.md  # Prototyping research plan
│   ├── simulation-study-plan.md      # Simulation study plan
│   ├── sales-productization-framework.md  # Skill-domain frame (Layer 2)
│   ├── ai-systems-design-management-framework.md  # SDM meta-frame (Layer 3)
│   └── healthcare-bio-ai-framework.md  # Healthcare/Bio AI sector vertical (special topic)
├── research/                  # Research by area
│   ├── 01-discovery/          # Discovery & User Research
│   ├── 02-design/             # Design & Prototyping
│   ├── 03-development/        # Development & Engineering
│   ├── 04-management/         # Management & Decision Making
│   ├── 05-growth-lifecycle/   # Growth & Lifecycle
│   ├── cross-cutting/         # Cross-cutting themes
│   ├── industry-trends/       # Company research & industry trends
│   ├── sales-skills/          # AI for selling + investing (Layer 2)
│   ├── productization-skills/ # AI for product implementation (Layer 2)
│   ├── ai-systems/            # AI Systems Design & Management — SDM meta-frame (Layer 3)
│   ├── healthcare-bio-ai/     # Healthcare/Bio AI sector vertical (special topic)
│   └── adaptability-framework/  # Organizational adaptability research extension
│       ├── plan.md           # Research questions and eleven prompts
│       └── memos/            # AI usage, organization, infrastructure, and integration
├── product/                   # AI Work Advisor — single-file tool
│   └── index.html             # Open in any browser, no install needed
├── prototypes/                # Research prototypes
│   ├── p1-complementarity-dashboard/  # Selective Complementarity task classifier
│   ├── p2-aadm-scoring/              # AADM decision scoring tool
│   ├── p3-design-fiction-kit/         # Workshop protocol & materials
│   └── p4-success-checklist/          # AI adoption readiness diagnostic
├── references/                # Reference lists
│   ├── academic.md            # Academic papers
│   ├── industry.md            # Industry & practitioner reports
│   ├── venues.md              # Key conferences, journals, institutions
│   └── reading-list.md        # Recommended books (research + fiction)
└── notes/                     # Working notes
    └── research-gaps.md       # Research gaps & future directions
```

## Scope

- **Time range:** 2022–2026 (latest research snapshot: 2026-04-22)
- **Sources:** Academic papers, practitioner research, and industry reports
- **Disciplines:** HCI, software engineering, management science, machine learning, **systems engineering (MIT SDM methods)**

## License

See [LICENSE](LICENSE) for details.
