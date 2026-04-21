# Healthcare & Bio AI: A Sector-Vertical Special Topic

> **Date:** 2026-04-21
> **Purpose:** Special-topic vertical applying this repository's three-layer SDM frame to healthcare, hospitals, and pharmaceutical/biotech AI. Not a vendor landscape — a systems analysis of how AI is architected, regulated, and operated in one of the most constrained socio-technical domains in industry.

---

## 1. Why Healthcare/Bio AI Is a Distinct SDM Problem

The main repository frames AI-for-product generically. Healthcare/bio breaks most of the generic assumptions:

| Generic AI product assumption | Healthcare/bio reality |
|---|---|
| Software failure is a bug | Software failure is a **Class II/III medical device adverse event** — FDA reportable, potentially life-threatening |
| Data is a commodity | Data is **PHI under HIPAA / Article 9 GDPR** — regulated at the *record* level |
| Users choose the tool | Hospitals buy, **clinicians use, patients are affected** — three-body user problem |
| Drift is retrained continuously | Drift may trigger a **510(k) re-submission** — change control is regulatory, not DevOps |
| Evidence is A/B tests | Evidence is **RCT, prospective cohort, or FDA pre-market review** — months to years |
| Reimbursement follows adoption | CMS/payer reimbursement codes (**CPT, HCPCS**) determine survival — no code, no product |
| Liability is EULA-bounded | **Medical malpractice + product liability + HIPAA penalties** — unbounded |
| Market = buyers | Market = **payer + provider + patient + regulator + pharma** — five-sided |

The canonical SDM answer: healthcare AI is a **highly regulated socio-technical system with irreversible patient-level consequences**, so every SDM sub-discipline (architecture, STS, risk, tradespace, governance) applies with sharper teeth than in generic SaaS.

---

## 2. Three-Layer Frame, Re-Applied to Healthcare/Bio

This vertical re-uses the repository's existing three-layer frame, with healthcare-specific instantiation:

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3 (meta): AI Systems Design & Management                 │
│  ─────────────────────────────────────────                      │
│  Healthcare-specific: SaMD architecture, STAMP for clinical AI, │
│  STS for clinician-AI teaming, tradespace of evidence vs speed, │
│  governance under FDA+EU AI Act+HIPAA overlap                   │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2 (cross-section): Skill domain                          │
│  ────────────────────────────────────                           │
│  Healthcare-specific: clinician skills (documentation, dx,      │
│  treatment planning), scientist skills (target ID, trial        │
│  design), operator skills (RCM, scheduling)                     │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1 (phases): Product lifecycle                            │
│  ────────────────────────────────                               │
│  Healthcare-specific pipeline: Discovery → Preclinical →        │
│  Trial → Submission → Reimbursement → Post-market surveillance  │
└─────────────────────────────────────────────────────────────────┘
```

The healthcare product lifecycle is **longer and more gated** than the generic lifecycle — which reshapes every Layer 1, 2, 3 analysis.

---

## 3. Sub-Domain Decomposition

This vertical is decomposed into eight sub-domains, each a coherent SDM research unit:

| # | Sub-domain | What the AI system does | Primary SDM concern |
|---|---|---|---|
| 1 | **Drug discovery AI** | Target identification, molecule design, property prediction, AlphaFold-class structure prediction | Pipeline architecture, tradespace vs. physics-based methods |
| 2 | **Clinical trials AI** | Protocol optimization, patient recruitment, synthetic control arms, real-world evidence | Evidence-generation architecture, FDA qualification |
| 3 | **Medical imaging & diagnostics AI** | Radiology triage, pathology classification, ophthalmology screening | SaMD architecture, FDA 510(k) trajectory, workflow integration |
| 4 | **Clinical decision support & ambient scribes** | EHR-integrated recommendations, ambient documentation, diagnostic LLMs | STS joint optimization of clinician + AI |
| 5 | **Hospital operations AI** | RCM, scheduling, staffing, capacity, prior auth | System dynamics of hospital ops, prior-auth arms race |
| 6 | **Patient-facing health AI** | Symptom triage, mental-health chatbots, remote monitoring | Consumer-product SDM with clinical-grade liability |
| 7 | **Healthcare AI regulation & governance** | Who decides what's allowed, measured, reimbursed | Governance architecture across FDA + EU AI Act + HIPAA |
| 8 | **Healthcare AI safety & resilience** | Preventing and absorbing AI-caused patient harm | STAMP, resilience engineering, bias-as-hazard |

---

## 4. Stakeholder Map — Healthcare/Bio-Specific

Generic AI product stakeholder maps (see Layer 3 framework) undercount healthcare/bio. The real map:

| Stakeholder | Primary interest | Interface to AI system |
|---|---|---|
| **Patient** | Outcome, safety, privacy, cost | Portal, consent, bedside |
| **Clinician (physician, nurse, allied)** | Accuracy, burnout, liability, fit in workflow | EHR, CPOE, PACS, voice |
| **Hospital / health system C-suite** | Margin, compliance, reputation, staffing | Procurement, governance committee |
| **Medical staff office** | Credentialing, competency, training | LMS, training protocols |
| **IT / CIO / CMIO** | Interoperability (FHIR, HL7), security | EHR integration, SSO, audit logs |
| **Risk / compliance / legal** | Malpractice exposure, HIPAA, FDA reporting | Audit, incident review |
| **Pharma / biotech sponsor** | Discovery throughput, trial efficiency | Internal pipelines, CRO integrations |
| **Payer (commercial, Medicare, Medicaid)** | Medical necessity, cost, outcomes | Prior auth, claims adjudication |
| **Regulator — FDA (US)** | Device safety, efficacy, change control | 510(k), De Novo, PMA, PCCP |
| **Regulator — EMA / national (EU)** | CE marking, MDR + AI Act compliance | Technical file, PMS plan |
| **Regulator — HHS / OCR (privacy)** | HIPAA breach, civil rights, disparate impact | OCR investigations |
| **Regulator — ONC** | Interoperability, DSI transparency (HTI-1) | Certification programs |
| **Standards bodies** (AAMI, IEEE, ISO, HL7) | Interoperability, process standards | Voluntary standards adoption |
| **CHAI / industry coalitions** | Trust frameworks, voluntary evaluation | Assurance labels |
| **Academic medical center researchers** | Evidence generation, validation | IRB-governed studies |
| **Investors (public + VC)** | Returns, exit paths | Cap table, earnings |
| **Professional societies** (ACR, ASH, ASCO, AMA) | Practice guidelines, advocacy | Policy statements, clinical practice guidelines |

Joint optimization across this set is harder than in generic SaaS — **the Pareto frontier is small** because payer, regulator, and patient interests frequently conflict.

---

## 5. Lifecycle — Healthcare Product Is Not a SaaS Product

```
  Generic AI product:                Healthcare/bio AI:

  Ideation                           Basic research
     ↓                                  ↓
  MVP                                Translational / preclinical
     ↓                                  ↓
  Beta                               Clinical trial (Phase I/II/III)
     ↓                                  ↓                ↔ FDA/EMA review
  Launch                             Regulatory submission (510k/De Novo/PMA)
     ↓                                  ↓
  Scale                              Reimbursement coding (CPT/HCPCS/DRG)
     ↓                                  ↓
  Sunset                             Commercial launch
                                        ↓                ↔ Post-market surveillance
                                     Real-world use + updates (PCCP governed)
                                        ↓                ↔ MDR/FDA reporting
                                     Discontinuation / recall
```

**Lifecycle consequence**: AI-for-healthcare cannot be iterated like SaaS. "Continuous deployment" lives inside the Predetermined Change Control Plan envelope — the *architecture* of allowed change is itself a regulated artifact.

---

## 6. The Six Systemic Tensions of Healthcare AI

Across all eight sub-domains, the same six tensions recur. An SDM-framed analysis must name where each paper sits on each tension:

1. **Speed vs. evidence** — FDA prefers prospective validation; market prefers rapid iteration.
2. **Generalization vs. site-specificity** — Foundation models vs. locally-tuned deployments.
3. **Autonomy vs. oversight** — Fully autonomous dx (IDx-DR) vs. physician-confirmed (most 510(k)-cleared AI).
4. **Integration vs. standalone** — Deep EHR integration (Abridge in Epic) vs. standalone apps (Ada Health).
5. **Transparency vs. IP** — ONC HTI-1 demands disclosure of DSI source, logic, training data; vendors resist.
6. **Equity vs. performance average** — Optimizing for population mean degrades subgroups (Optum 2019, dermatology AI).

Every paper in this vertical positions its subject on these six tensions.

---

## 7. Connection to Repository's Other Layers

Healthcare/bio AI is **not orthogonal** to the main repo — it is a sector instance that tests every generic claim:

| Generic claim in repo | Healthcare/bio stress test |
|---|---|
| "Vibe coding accelerates MVP" | Vibe-coded SaMD is an FDA violation under Part 820/QMSR |
| "METR shows -19% slowdown in OSS" | What does the METR analogue look like in EHR-integrated coding? Unknown — no equivalent RCT |
| "Agentic AI in sales" | Agentic AI in **prior auth** triggered the UnitedHealth nH Predict lawsuit |
| "Compound AI systems" | Clinical compound AI (LLM + retrieval + imaging model + orchestrator) is the emerging SaMD reference architecture |
| "Joint optimization" (STS) | Clinician-AI joint optimization is the canonical 2024-2026 empirical question |
| "Tradespace exploration" | FDA-cleared AI is a Pareto-limited tradespace (evidence × breadth × autonomy) |

Findings from the vertical flow back to the main layers as *validation cases*: if an SDM theory cannot explain the healthcare case, it is incomplete.

---

## 8. Thesis-Scale Research Questions Specific to This Vertical

1. **Reference architecture for a FDA-cleared compound AI clinical system** — What are the minimum coherent components (LLM, retrieval, rule engine, human-in-loop, audit log, PCCP envelope) for a Class II SaMD compound AI system?
2. **STAMP analysis of Epic Sepsis Model retrospective** — What control loops failed between EHR vendor, hospital deployers, and clinicians?
3. **System dynamics of the prior-authorization AI arms race** — Two-sided AI deployment (payer denial AI vs. provider appeal AI) modeled as coupled feedback loops.
4. **Tradespace of drug discovery AI architectures** — Pareto between physics-based (Schrödinger), deep-learning (AlphaFold), and hybrid approaches across cost × accuracy × generalization.
5. **STS joint optimization of ambient scribes** — Measured burnout, note quality, and throughput as joint DVs across Abridge / DAX / Suki deployments.
6. **Governance architecture under FDA PCCP + EU AI Act Annex III** — RACI matrix for a clinical AI system under both regimes.
7. **Resilience engineering for AI-augmented clinical workflows** — Safety-II/III framing of what clinicians actually do when the AI is wrong.
8. **Socio-technical equity analysis** — Where does the Optum 2019-class bias originate architecturally — data, proxy, objective, deployment?

Each is defensible as an MIT SDM master's thesis.

---

## 9. What This Vertical Is NOT

- **Not** a vendor buying guide. This is an SDM-framed analysis, not a Gartner Magic Quadrant.
- **Not** a clinical endorsement. Nothing here is medical advice or should inform patient care.
- **Not** comprehensive. Specialties like surgical robotics, hospice AI, veterinary AI, and agricultural/food bio AI are omitted.
- **Not** a policy brief. Regulatory discussion is descriptive; prescriptive policy is out of scope.

---

## 10. Related Documents

- [Layer 1 lifecycle survey](survey-report.md)
- [Layer 2 skill frame](sales-productization-framework.md)
- [Layer 3 SDM meta-frame](ai-systems-design-management-framework.md)
- [research/healthcare-bio-ai/](../research/healthcare-bio-ai/) — sector-vertical papers (this special topic)
