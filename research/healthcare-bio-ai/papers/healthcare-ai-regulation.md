# Healthcare AI Regulation & Governance: Architecture Across FDA + EU AI Act + HIPAA + ONC

> **Date:** 2026-04-21
> **SDM lens:** Governance architecture, enterprise architecture (Madnick/CAMS), RACI, regulatory-interface alignment, multi-jurisdictional tradespace

---

## 1. Thesis

Healthcare AI governance is not a single regulation but **a layered enterprise-architecture problem**: FDA (device safety, lifecycle), EU AI Act (high-risk horizontal), HIPAA (privacy), ONC HTI-1 (transparency at EHR), state AGs (UDAP enforcement), and voluntary coalitions (CHAI, Joint Commission) each assert jurisdiction over overlapping slices of the same AI system. For an SDM analyst, the question is not "which regulation applies" but **"what is the RACI across the regulatory stack, and where are the unoccupied gaps?"** The 2024-2026 period is the definitive window: FDA PCCP became final (Dec 2024), EU AI Act high-risk enforcement begins Aug 2026, ONC HTI-1 DSI rule went live Jan 1 2025, and state AGs stepped in (Texas Pieces Sep 2024, California Bonta Jan 2025).

---

## 2. The Regulatory Stack — Architectural View

```
┌────────────────────────────────────────────────────────────────┐
│  HORIZONTAL: cross-sector AI law                               │
│     EU AI Act (2024, high-risk enforcement Aug 2, 2026)        │
│     US — no federal AI law; state UDAP enforcement             │
└────────────────────────────────────────────────────────────────┘
                              ↕
┌────────────────────────────────────────────────────────────────┐
│  VERTICAL: healthcare-specific product regulation              │
│     FDA SaMD / PCCP / GMLP (US)                                │
│     EU MDR / IVDR (EU; overlaps AI Act)                        │
│     Section 3060 CDS carve-out (US)                            │
└────────────────────────────────────────────────────────────────┘
                              ↕
┌────────────────────────────────────────────────────────────────┐
│  DATA: privacy and anti-discrimination                         │
│     HIPAA + HIPAA Security Rule (US; 2025 update proposed)     │
│     Section 1557 ACA (US, anti-discrimination, AI from 2025)   │
│     GDPR Art. 9 (EU, health data)                              │
└────────────────────────────────────────────────────────────────┘
                              ↕
┌────────────────────────────────────────────────────────────────┐
│  INTEROP / TRANSPARENCY at EHR                                 │
│     ONC HTI-1 DSI rule (US, effective Jan 1, 2025)             │
│     45 CFR 170.315(b)(11); 13 or 31 Source Attributes          │
└────────────────────────────────────────────────────────────────┘
                              ↕
┌────────────────────────────────────────────────────────────────┐
│  VOLUNTARY / INDUSTRY / STANDARDS                              │
│     CHAI + Joint Commission (Jun 2025 partnership)             │
│     NIST AI RMF 1.0 (2023); GenAI Profile (Jul 2024)           │
│     BS/AAMI 34971:2023; IEEE 2802-2022                         │
│     WHO LMM Guidance (Jan 2024)                                │
└────────────────────────────────────────────────────────────────┘
                              ↕
┌────────────────────────────────────────────────────────────────┐
│  ENFORCEMENT                                                   │
│     State AGs (TX Pieces Sep 2024; CA Bonta Jan 2025)          │
│     Class action (nH Predict — survived motion to dismiss 2025)│
│     Senate Permanent Subcommittee on Investigations            │
└────────────────────────────────────────────────────────────────┘
```

**SDM observation**: There is no single "healthcare AI regulator." A compliance architecture must trace a system against every layer and assign responsibility — this is the **RACI problem** the SDM-governance lens makes explicit.

---

## 3. FDA Layer: PCCP + TPLC

### Predetermined Change Control Plans (PCCP) — final guidance Dec 3, 2024

- Title: "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions."
- Allows **pre-authorized algorithmic changes post-market** without new 510(k)/De Novo/PMA submission.
- Three mandatory components: (1) Description of Modifications, (2) Modification Protocol, (3) Impact Assessment.
- **Final guidance broadened scope** from ML-only to all AI-enabled devices; softened intended-use restriction.
- **SDM framing**: PCCP is the **first regulatory acknowledgement that AI is a lifecycle artifact, not a static artifact.** It redefines the interface between FDA and vendor from "pre-market gate" to "governed envelope of change."

### TPLC Draft Guidance — Jan 6, 2025

- "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations."
- Federal Register 2024-31543; comment period closed Apr 7, 2025.
- Applies Total Product Life Cycle (TPLC) approach.
- Requires: model description, data lineage/splits, performance tied to claims, bias analysis/mitigation, human-AI workflow, monitoring.
- **Market scale**: As of July 2025, FDA database lists **>1,250 AI-enabled medical devices** (up from 950 in Aug 2024); **1,451 through end-2025** (see [medical imaging paper](medical-imaging-diagnostics-ai.md)).

### GMLP and Transparency Principles

- **Oct 2021** — 10 Guiding Principles jointly FDA + Health Canada + UK MHRA.
- **Jun 13, 2024** — Transparency for Machine Learning-Enabled Medical Devices: Guiding Principles.
- **Oct 2024** — PCCP Guiding Principles trilateral document.
- **Voluntary** — not rulemaking.

### FDA AI in Drug Development (CDER)

- **Jan 7, 2025** — draft guidance for AI/ML in drug and biological product development (see [clinical trials paper](clinical-trials-ai.md)); seven-step risk-based credibility framework; context-of-use (COU) assessment.

---

## 4. EU Layer: AI Act + MDR Overlap

### EU AI Act (Regulation (EU) 2024/1689)

- **Aug 1, 2024** — entered into force.
- **Aug 2, 2026** — high-risk systems (Annex III) provisions enforceable; CE marking, conformity assessment, EU database registration.
- Healthcare AI is high-risk via two paths:
  1. **Annex I** — MDR/IVDR-regulated devices with notified-body conformity assessment.
  2. **Annex III** — emergency triage/dispatch and patient-evaluation systems.
- **Exception**: Class I self-certified / IVDR Class A non-sterile = not high-risk.
- **Max penalties**: €35M or 7% of global turnover for prohibited practices; €15M or 3% for high-risk non-compliance.

### MDR + AI Act overlap problem

- MDR already covers risk assessment, QMS, technical file, post-market surveillance.
- **AI Act adds duplicative obligations** on data governance, human oversight, accuracy/robustness.
- **Dec 2025** — European Commission "Digital Omnibus" proposal attempts to streamline MDR/AI Act duplication.
- **SDM framing**: **Multi-regulator interface failure** — same artifact assessed twice under different taxonomies. A candidate for tradespace analysis of compliance cost vs. safety margin.

---

## 5. Data Layer: HIPAA, Section 1557, GDPR

### HIPAA Security Rule proposed update (Jan 6, 2025)

- **First update in 20 years.**
- Requires AI tools as part of risk analysis.
- Mandatory encryption, vulnerability scans every 6 months, penetration testing annually.
- OCR **explicitly declined** to propose stand-alone AI privacy rules in 2025 update — deferred for RFI.

### Section 1557 (ACA) final rule — July 5, 2024

- Prohibits discrimination via **patient-care decision-support tools including AI**.
- Effective date for AI/emerging-tech provisions: **May 1, 2025**.
- **Jan 10, 2025** — OCR "Dear Colleague" letter on non-discrimination & AI.
- **Authority**: HIPAA Privacy/Security Rules (45 CFR 160, 164); Section 1557 (42 USC 18116).

### GDPR Article 9 (EU health data)

- General prohibition on processing "data concerning health."
- Requires explicit consent (9(2)(a)) or derogation (public health, medical diagnosis 9(2)(h)).
- **2024 enforcement**: Swedish DPA fined a healthcare provider €12M for inadequate consent mechanisms.
- **Tension**: AI Act Article 10 requires "high quality" datasets — clashes with Art 9 minimization principle.

---

## 6. Interoperability Layer: ONC HTI-1 DSI

### HTI-1 final rule — Dec 13, 2023

- 45 CFR 170.315(b)(11).
- **DSI (Decision Support Intervention) certification criterion replaced CDS criterion in Base EHR definition Jan 1, 2025.**
- Requires **Source Attributes** disclosure:
  - **13 attributes for evidence-based DSIs** (e.g., UpToDate-class).
  - **31 attributes for Predictive DSIs** (e.g., sepsis risk score).
- Includes intervention use, fairness/validity, risk management practices, bias detection.
- **Developers had to comply by Dec 31, 2024.**
- **SDM framing**: ONC HTI-1 is the **first US mandatory AI transparency at EHR layer**. An "algorithmic nutrition label" with informational interface between vendor and clinical stakeholder.

---

## 7. Section 3060 (21st Century Cures Act) — the CDS Carve-Out

- Amended FD&C §520(o): certain CDS functions **excluded from "device" definition**.
- Requires HCP can **independently review basis** of recommendation and not "rely primarily" on it.
- **FDA final guidance Sep 27, 2019** — "Changes to Existing Medical Software Policies Resulting from Section 3060."
- **Gap**: LLM chatbots and black-box AI frequently fail the "independently review" test — **ambiguous whether regulated**.
- This ambiguity is the regulatory-arbitrage space that ambient scribes and diagnostic LLMs operate in (see [CDS paper](clinical-decision-support-ai.md)).

---

## 8. State Enforcement Layer

### Texas — Pieces Technologies settlement (Sept 18, 2024)

- **First-in-nation GenAI healthcare settlement**.
- Texas AG Paxton acted under **DTPA (Deceptive Trade Practices Act)**.
- Charge: false claims of **"<.001% and <1 per 100,000" hallucination rates** for a chart-summarization tool deployed at Texas hospitals.
- **SDM observation**: UDAP statutes are functioning as **de facto FDA enforcement proxy** for AI that evades device classification.

### California — AG Bonta legal advisory (Jan 13, 2025)

- Covers consumer protection, anti-discrimination, privacy in healthcare AI.
- Actively investigating commercial decision-making platforms.

### New York — SB 7896 + AB 1456 (2025)

- Require AI utilization-review tools to base decisions on clinical record.
- Prohibit supplanting provider decision-making.
- **NY DFS Insurance Circular Letter No. 7 (2024)** on AI / external data in underwriting.

### Texas SB 1822 (2025) — parallels NY SB 7896.

---

## 9. Voluntary / Industry Standards

### Coalition for Health AI (CHAI)

- Founded Dec 2021. Founding: Microsoft, Google, MITRE, Johns Hopkins, Mayo, Stanford, Berkeley, Duke, Change Healthcare, UCSF.
- **Apr 2023** — "Blueprint for Trustworthy AI Implementation Guidance and Assurance for Healthcare."
- **Jun 26, 2024** — Draft Responsible Health AI framework + Assurance Standards Guide (public comment).
- **Apr 2025** — CHAI Applied Model Card v0.1 and Assurance Lab certification framework.
- **Jun 12, 2025** — **Joint Commission partnership announced** — the key development.
- **Sep 2025** — First installment "Guidance on Responsible Use of AI in Healthcare" with 7 core elements.
- **SDM framing**: CHAI is private multi-stakeholder governance filling the vacuum between FDA/ONC — quasi-standard emerging via Joint Commission conduit.

### Joint Commission

- **Jun 12, 2025** — JC + CHAI partnership.
- **Sep 2025** — "Responsible Use of AI in Healthcare" guidance (non-binding).
- **2026** — Voluntary AI certification program planned across **22,000+ accredited organizations**.

### Standards bodies

- **BS/AAMI 34971:2023** — "Application of ISO 14971 to Machine Learning in AI." FDA-recognized consensus standard (2022).
- **ISO/IEC 42001:2023** — AI Management System.
- **IEEE 2802-2022** — Performance and Safety Evaluation of AI Medical Device: Terminology.
- **IEEE P2801** — Recommended Practice for Quality Management of Datasets for Medical AI (in development).

### NIST AI RMF 1.0

- Published Jan 26, 2023. Voluntary. Four functions: GOVERN, MAP, MEASURE, MANAGE.
- **Jul 2024** — Generative AI Profile (NIST AI 600-1).
- No dedicated healthcare profile; AAMI criticism — RMF not aligned with ISO 14971 hazard analysis.

### WHO

- **Jun 28, 2021** — "Ethics and governance of AI for health" (6 principles).
- **Jan 18, 2024** — "Ethics and governance of AI for health: Guidance on large multi-modal models" — 40+ recommendations; mandatory post-release audits by independent third parties.
- **2024** — Global Initiative on AI for Health (GI-AI4H) — WHO/ITU/WIPO joint.

---

## 10. Governance RACI Matrix (Illustrative)

For a hypothetical ambient-scribe deployment in a US health system:

| Function | FDA | HHS/OCR | ONC | State AG | CHAI/JC | Health system | Vendor |
|---|---|---|---|---|---|---|---|
| Device classification | **A** | I | C | I | C | R | R |
| Data privacy (HIPAA) | I | **A** | I | I | C | **R** | R |
| Anti-discrimination (1557) | I | **A** | I | I | C | R | R |
| EHR transparency (DSI) | I | I | **A** | I | C | R | **R** |
| Accuracy marketing claims | C | I | I | **A/R** | C | I | R |
| Ongoing safety monitoring | C | I | I | I | **C/R** | **R** | R |
| Patient disclosure | I | C | C | **A** | C | **R** | C |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

**Observation**: *No single party is Accountable for "the whole AI system."* The gap between vertical device regulation (FDA) and horizontal operational compliance (HHS/OCR, ONC, state AGs) is the **systemic blind spot** — and where CHAI + Joint Commission voluntary frameworks now position as de facto assurance layer.

---

## 11. The Six Systemic Tensions, Applied

| Tension | Regulatory manifestation |
|---|---|
| Speed vs. evidence | PCCP loosens pre-market gate; TPLC tightens post-market monitoring |
| Generalization vs. site-specificity | GMLP emphasizes local validation; foundation-model scale conflicts |
| Autonomy vs. oversight | Section 3060 carve-out requires physician independent review — poorly defined |
| Integration vs. standalone | ONC HTI-1 applies at EHR layer; standalone imaging AI largely escapes |
| Transparency vs. IP | HTI-1 mandates disclosure; vendors resist |
| Equity vs. performance average | Section 1557 + OCR 2025 letter — explicit anti-discrimination as AI requirement |

---

## 12. Research Gaps

1. **Cross-jurisdictional RACI**: Formal mapping of FDA + EU AI Act + HIPAA + ONC responsibilities for a canonical AI system.
2. **Digital Omnibus impact**: Does the Dec 2025 MDR/AI Act streamlining actually reduce compliance burden, or redistribute it?
3. **State AG pattern analysis**: Is UDAP enforcement converging toward a de facto federal framework?
4. **PCCP scope creep**: How far can pre-authorized change plans extend before FDA revokes blanket authority?
5. **CHAI Assurance Lab validation**: Does the voluntary framework materially change deployment outcomes?
6. **Equity certification**: Can Section 1557 AI provisions be operationalized as measurable audit criteria?

---

## 13. Sources

- FDA PCCP Final Guidance. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence
- FDA AI-Enabled Device Software Draft (Jan 2025). https://www.federalregister.gov/documents/2025/01/07/2024-31543/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing
- FDA GMLP Principles. https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles
- FDA Transparency Principles. https://www.fda.gov/medical-devices/software-medical-device-samd/transparency-machine-learning-enabled-medical-devices-guiding-principles
- EU AI Act Annex III. https://artificialintelligenceact.eu/annex/3/
- EU AI Act implementation timeline. https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
- ONC HTI-1 DSI fact sheet. https://www.healthit.gov/sites/default/files/page/2023-12/HTI-1_DSI_fact%20sheet_508.pdf
- ONC DSI certification criterion. https://healthit.gov/test-method/decision-support-interventions/
- HHS Proposed Security Rule (Jan 2025). https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information
- HHS OCR Jan 10, 2025 letter. https://ismg-cdn.nyc3.cdn.digitaloceanspaces.com/asset_files/external/hhs-ocr-dear-colleagues-letter-re-ai-non-discrimination-1-10-25.pdf
- GDPR Art 9. https://gdpr-info.eu/art-9-gdpr/
- FDA Section 3060 Guidance. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/changes-existing-medical-software-policies-resulting-section-3060-21st-century-cures-act
- Texas AG Pieces settlement. https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-reaches-settlement-first-its-kind-healthcare-generative-ai-investigation
- CA AG Jan 2025 advisory. https://www.wsgr.com/en/insights/california-ag-issues-legal-advisory-regarding-use-of-ai-in-healthcare.html
- NY DFS Circular Letter 7 (2024). https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
- WHO LMM Guidance 2024. https://www.who.int/publications/i/item/9789240084759
- WHO 2021 AI Ethics. https://www.who.int/publications/i/item/9789240029200
- NIST AI RMF 1.0. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- CHAI Blueprint. https://www.chai.org/workgroup/responsible-ai/blueprint-for-trustworthy-ai
- JC + CHAI (Sep 2025). https://www.jointcommission.org/en-us/knowledge-library/news/2025-09-jc-and-chai-release-initial-guidance-to-support-responsible-ai-adoption
- BS/AAMI 34971:2023. https://knowledge.bsigroup.com/articles/how-to-tackle-hazards-in-ai-medical-devices-using-bs-aami-34971
- IEEE 2802-2022. https://standards.ieee.org/ieee/2802/7460/
