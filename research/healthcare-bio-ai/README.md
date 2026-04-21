# Healthcare & Bio AI — Sector-Vertical Special Topic

> **Scope:** Re-apply the repository's three-layer SDM frame (lifecycle / skill / SDM meta) to one sector vertical — healthcare, hospitals, pharma, and biotech AI. Emphasis on architecture, interfaces, regulation, feedback loops, failure modes, stakeholder map — not vendor landscape.

> See [docs/healthcare-bio-ai-framework.md](../../docs/healthcare-bio-ai-framework.md) for the sector-vertical framework.

---

## Sub-domains

| # | Paper | SDM methods applied |
|---|---|---|
| 1 | [Drug Discovery AI](papers/drug-discovery-ai.md) | Pipeline architecture, tradespace exploration (physics vs. DL vs. hybrid), lifecycle (target→clinical) |
| 2 | [Clinical Trials AI](papers/clinical-trials-ai.md) | Evidence architecture, FDA qualification lifecycle, synthetic-control-arm interface design |
| 3 | [Medical Imaging & Diagnostics AI](papers/medical-imaging-diagnostics-ai.md) | SaMD reference architecture, FDA 510(k)/De Novo/PMA tradespace, workflow integration |
| 4 | [Clinical Decision Support & Ambient Scribes](papers/clinical-decision-support-ai.md) | STS joint optimization (clinician + AI), compound AI for documentation |
| 5 | [Hospital Operations AI](papers/hospital-operations-ai.md) | System dynamics of RCM + scheduling, prior-auth arms-race feedback loop |
| 6 | [Patient-Facing Health AI](papers/patient-facing-health-ai.md) | Consumer-SaaS × clinical-liability, three-body stakeholder problem |
| 7 | [Healthcare AI Regulation & Governance](papers/healthcare-ai-regulation.md) | Governance architecture across FDA + EU AI Act + HIPAA + ONC HTI-1 |
| 8 | [Healthcare AI Safety & Resilience](papers/healthcare-ai-safety.md) | STAMP/STPA for clinical AI failures, Safety-II/III, resilience engineering |

---

## Why this vertical exists in this repo

The repository's main frames (lifecycle / skill / SDM) are generic. Healthcare/bio is the domain where every generic assumption is *stress-tested*: failure is regulated, users are three-layered (clinician/patient/payer), change control is a pre-submitted plan, and outcomes are measured in QALYs and lawsuits — not DAU.

A healthcare-specific vertical validates or refutes each generic claim. If a generic SDM theory cannot explain the Epic Sepsis retrospective, the IBM Watson Oncology retrospective, the Optum 2019 bias paper, or the Abridge-DAX workflow integration — the generic theory is incomplete.

---

## Six systemic tensions (re-used across all papers)

1. **Speed vs. evidence** — FDA pre-market vs. market iteration
2. **Generalization vs. site-specificity** — Foundation models vs. local tuning
3. **Autonomy vs. oversight** — Autonomous dx vs. physician-confirmed
4. **Integration vs. standalone** — EHR-embedded vs. external app
5. **Transparency vs. IP** — DSI disclosure (HTI-1) vs. trade secrets
6. **Equity vs. performance average** — Population mean vs. subgroup parity

Each paper positions its subject on these tensions.

---

## Key SDM-canonical references applied

| Method | Canonical | How used |
|---|---|---|
| STAMP / STPA | Leveson (MIT) | Safety paper — Epic Sepsis, Watson Oncology |
| System dynamics | Forrester / Sterman (MIT) | Hospital ops — prior-auth arms race |
| STS / joint optimization | Trist (Tavistock) | CDS paper — clinician-AI teaming |
| Tradespace | Ross / Hastings (MIT) | Drug discovery architectural choices |
| Architecture | Crawley, de Weck (MIT) | SaMD reference architecture |
| OPM | Dori (MIT) | Clinical trial process models |
| Resilience eng. | Hollnagel, Rhodes (MIT) | Safety paper — Safety-II/III |
| Governance | Madnick / CAMS (MIT) | Regulation paper — RACI, enterprise architecture |

---

## Thesis-scale research questions

1. Reference architecture for a FDA-cleared compound AI clinical system
2. STAMP of Epic Sepsis Model retrospective
3. System dynamics of prior-auth arms race
4. Tradespace of drug discovery AI architectures
5. STS joint optimization of ambient scribes (Abridge / DAX / Suki)
6. Governance architecture under FDA PCCP + EU AI Act Annex III
7. Resilience engineering for AI-augmented clinical workflow
8. Socio-technical equity analysis of healthcare algorithmic bias

---

## Scope boundary

- **In scope:** Healthcare delivery AI, pharma/biotech R&D AI, hospital operations AI, patient-facing digital health AI, healthcare AI regulation and safety.
- **Out of scope:** Surgical robotics autonomy, veterinary/food-bio AI, medical education AI (except as it intersects CDS), medical device hardware unless AI-controlled.
