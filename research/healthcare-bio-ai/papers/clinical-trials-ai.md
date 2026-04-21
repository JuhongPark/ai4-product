# Clinical Trials AI: Evidence Architecture Under Regulatory Asymmetry

> **Date:** 2026-04-21
> **SDM lens:** Evidence-generation architecture, FDA/EMA qualification lifecycle, interface asymmetry between regulatory regimes, real-world-evidence tradespace

---

## 1. Thesis

Clinical trials are a **regulated evidence-generation system**, not a research activity. AI enters this system at four architectural points — protocol design, patient recruitment, synthetic control arms, and real-world evidence. The canonical SDM observation: **regulatory interfaces are non-uniform** — EMA has a formal qualification path for AI methodologies (PROCOVA), while FDA operates through soft guidance. This **regulatory-interface asymmetry** is a first-class architectural constraint that shapes where AI is deployable and who bears the validation burden.

---

## 2. The Clinical Trial as a System

```
Protocol        Sites        Recruitment       Conduct           Analysis        Submission
────────        ─────        ───────────       ───────           ────────        ──────────
Design the      Identify     Find + consent    Execute per       Statistical     NDA/BLA
question &      PI, sites,   eligible          protocol; data    analysis per    or MAA
endpoints       IRBs         patients          collection        SAP             + RWE

AI entry:       AI-assisted  Patient ID (Deep  Adaptive design   Surrogate end-  Digital twin
protocol        site sel.    6, Tempus, TrialX) amendment tools  points, RWE      synthetic
optimization                                    NLP for source   integration      arms; AI
                                                document verif.                   dossier
```

Each gate has regulatory oversight; each AI insertion creates a qualification question.

---

## 3. The Four AI Entry Points

### 3.1 Protocol design & optimization

- **Saama AI Platform** (SaaS, June 2023) — clinical-development automation suite. **Saama ownership**: majority acquired by Carlyle Group (Oct 2021, $430M strategic) with Amgen, Merck GHI, McKesson, Northpond, Pfizer Ventures as co-investors. Merck partnership extended 2023 for AI on clinical data.
- **Medidata Rave Lite (Oct 2024)**, **Clinical Data Studio (June 2024)**, 300+ new customers in 2024 (Sanofi, Eisai, PPD). Source-agnostic orchestration layer.
- **Veeva SiteVault CTMS (April 2025)** — site-first CTMS with eISF/eConsent and bidirectional sponsor data flow.

### 3.2 Patient recruitment & site selection

- **Deep 6 AI** — NLP/ML over EHR for trial matching. **Acquired by Tempus AI March 2025**; reach across 750+ provider sites.
- **Tempus AI (NASDAQ: TEM, IPO June 2024)** — multimodal molecular-clinical data platform. 2025 revenue $1.27B (+83.4% YoY); losses −$245M; market cap ~$7.7B (Apr 2026). **Ambry Genetics acquisition Feb 2025 ($600M, $375M cash + $225M shares)** expanded into pediatrics, rare disease, cardiology. **AstraZeneca + Pathos 3-year $200M data-licensing deal** for oncology multimodal foundation model (300+ PB).
- **TrialX, Antidote, Inato** — patient-recruitment tools.

### 3.3 Synthetic control arms / digital twins

- **Unlearn.ai (founded 2017, SF)** — **$130M+ raised**, Series C $50M Feb 2024 (Altimeter, Radical, Wittington, Mubadala, Epic, DCVC).
- **PROCOVA methodology** — digital-twin prognostic scores that reduce required control-arm size 20-30% while preserving statistical power; 10-20% variance reduction on treatment effect estimation.
- **EMA qualification**: Draft qualification opinion for PROCOVA as a statistical methodology for Phase 2/3 continuous-outcome RCTs — a **formal regulatory pathway**.
- **FDA status**: **No analogous formal qualification program**. Sponsors align methodology with FDA guidance principles but face case-by-case review. The EMA↔FDA asymmetry is the defining feature of this sub-domain.

### 3.4 Real-world evidence (RWE)

- **21st Century Cures Act Section 3022** directed FDA to incorporate RWE into approvals. **2022-2024 data**: RWE appears in 23-28% of FDA approvals.
- **FDA RWE Guidance**: July 25, 2024 final guidance; December 18, 2025 device-focused update added AI clarifications.
- **ICH E6(R3) Good Clinical Practice (Jan 2025, Step 4)**: integrates decentralized clinical trials (DCT), digital health technology, AI/ML; requires validation audits for AI used in source-data validation; projects ~30% data-cleaning time reduction.
- **FDA Draft Guidance (Jan 7, 2025)** — "Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products": seven-step risk-based credibility framework; **scope exclusion**: drug discovery and operational efficiencies; centers on context-of-use (COU) assessment. Comments closed April 7, 2025.
- **FDA DCT Final Guidance (Sept 2024)** — "Conducting Clinical Trials with Decentralized Elements."

---

## 4. Regulatory-Interface Asymmetry as SDM Problem

A central architectural observation: **EMA and FDA have adopted different AI-methodology interfaces**.

| Regulator | AI-methodology pathway | Burden on sponsor | Portability of approval |
|---|---|---|---|
| **EMA** | Formal qualification opinion (CHMP SAWP) — PROCOVA draft opinion issued | Scientific dossier; methodological evidence | Re-used across subsequent trials |
| **FDA** | Soft guidance (GMLP, draft AI-for-drug guidance Jan 2025) | Per-trial justification in IND / NDA | Case-by-case; limited precedent value |
| **PMDA (Japan)** | Emerging — no formal AI qualification pathway | Case-by-case | — |
| **NMPA (China)** | Emerging — supports AI but through different tooling | Case-by-case | — |

**SDM consequence**: Sponsors face a **compliance tradespace** — invest in EMA-first methodology (expensive dossier, re-usable) or FDA-first trial-specific justification (flexible, non-portable). Global programs require both, multiplying cost. This is regulatory-interface arbitrage and is architectural, not tactical.

---

## 5. The Tempus Vertical-Integration Thesis

Tempus AI is a natural experiment for the **vertical-integration-as-AI-strategy** thesis:

- **Horizontally:** Tempus offers molecular testing (NGS), radiology AI, cardiology AI, mental health, connects to clinical trials.
- **Vertically:** Tempus has *data* (300+ PB), *tools* (AI platform), *matching* (Deep 6), *genetic testing* (Ambry), and *licensing-out* (AstraZeneca/Pathos $200M).

In an SDM frame, Tempus is pursuing **joint optimization across the clinical-trial value chain** — not a point solution. The hypothesis: the value of AI in clinical trials depends on **data-interface ownership** more than model sophistication. 2025 revenue growth (+83.4%) supports the thesis; −$245M losses show it remains unproven.

---

## 6. Interfaces and Standards

| Standard / spec | Purpose | Role in AI trials |
|---|---|---|
| **CDISC SDTM / ADaM** | Clinical data tabulation + analysis | AI must output SDTM-conformant data for FDA submission |
| **HL7 FHIR + IG Clinical Research** | Site-to-sponsor data | AI recruitment tools read FHIR to match |
| **ICH E6(R3) GCP** | Good Clinical Practice | AI use must pass audit trail requirements |
| **ICH E9(R1)** | Statistical principles (estimands) | AI methods must be pre-specified under estimand framework |
| **EDC standards** (Veeva, Medidata) | Data capture | AI integrates into study builds |
| **21 CFR Part 11** | Electronic records & signatures | AI outputs used for regulatory must be Part 11-compliant |

**Observation**: Unlike drug discovery (no dominant interface standard, §8 of [drug-discovery-ai.md](drug-discovery-ai.md)), clinical trials have mature standards. AI must *conform*, not redefine. This is a **constrained architectural envelope**.

---

## 7. Stakeholder Map (Clinical-Trial-Specific)

| Stakeholder | Primary interest | AI-relevant interface |
|---|---|---|
| Sponsor (pharma / biotech) | Speed to approval, cost | Protocol, analysis, recruitment pipelines |
| CRO (Medidata, Veeva-operated) | Execution margin | Operations AI in EDC/CTMS |
| Principal Investigator (PI) | Patient enrollment, quality | eConsent, AI-flagged candidates |
| IRB / Ethics Committee | Patient safety, informed consent | AI-methodology review (emerging) |
| Patient / participant | Access, safety, burden | Digital-twin disclosure, decentralized visits |
| Regulator (FDA / EMA) | Evidence quality, reproducibility | Qualification opinion, dossier, audit |
| Payer | Post-approval coverage | RWE outputs, subgroup efficacy |
| Data Safety Monitoring Board | Ongoing safety/futility | Interim-analysis AI tooling (rare) |
| Contract research lab | Sample processing | AI QC on assays |

Each interface is a potential **coupling constraint** on AI design.

---

## 8. Feedback Loops and Emergent Behavior

**Virtuous loop — portable methodology**: Once a methodology qualifies (e.g., PROCOVA at EMA), subsequent sponsors reuse it. Cost amortizes; methodology standardizes. EMA has explicitly adopted this loop; FDA has not.

**Vicious loop — regulator-specific overfit**: If FDA and EMA adopt divergent AI-evaluation standards, global sponsors build **two methodologies** — more cost, more error surface, less cumulative validation.

**Vicious loop — RWE-as-evidence substitution**: RWE supplements but should not *replace* prospective evidence. A system-dynamics view: if sponsors under-invest in RCTs because RWE is "good enough," the evidence base drifts away from causal inference (population-level vs. treatment-specific). FDA is alert to this.

**Virtuous loop — patient-matching retention**: An AI tool that reliably identifies eligible patients accelerates recruitment *and* improves trial diversity, both regulatory priorities. Tempus + Deep 6 positioning is optimized for this loop.

---

## 9. Failure Modes

| Failure mode | Description | Concrete case |
|---|---|---|
| **Methodology-qualification failure** | AI method not validated for context-of-use | FDA sponsors pre-Jan-2025 guidance navigated uncertainty case-by-case |
| **EHR-extraction hallucination** | NLP fabricates eligibility criteria or comorbidities | Ongoing with LLM-based recruitment |
| **Digital-twin spec drift** | Prognostic-score distribution shifts from training to deployment population | Active research risk for synthetic-control-arm methods |
| **Part 11 audit failure** | AI outputs lack required signature / trail | Possible in DIY tooling |
| **AI fabricates trial outcomes** | Adversarial or misuse of AI to synthesize results | Ethics / research-integrity risk |

---

## 10. AI Clinical Success and Failure Cases

### Success (narrow): repurposing
- **BenevolentAI / baricitinib COVID-19** — AI hypothesis (AAK1 endocytosis inhibition) led to EUA for baricitinib. **Caveat**: this is drug *repurposing*, not de novo AI-designed molecule.

### Failure: AI-designed efficacy
- **BenevolentAI BEN-2293** (atopic dermatitis, pan-TRK) — met safety endpoint, failed efficacy vs placebo. Company laid off staff, closed US offices, pivoted to early-stage partnerships. Illustrates the **clinical-validation chasm**: AI-designed targets can be biochemically plausible and clinically useless.

### Partial success (methodological): synthetic controls
- **Unlearn.ai PROCOVA** — EMA draft qualification opinion shows methodological route works; widespread adoption pending; no single "AI-controlled" pivotal trial has yet approved a drug solely on synthetic-control-arm evidence.

### Industry baseline
- Clinical failure rate remains ~90%; ~$2.6B per approved drug; 10-15-year timeline. **AI has not yet measurably moved Phase II/III attrition**, contrary to marketing claims.

---

## 11. Tradespace: Evidence × Speed × Cost

Plotting AI-in-trials architectures:

| Axis | Traditional RCT | AI-augmented RCT (Unlearn, Tempus) | AI-native trial (hypothetical) |
|---|---|---|---|
| Evidence strength | Gold standard | Equivalent (if qualified) | Unproven |
| Speed | 3-7 years (Phase II/III) | 0.7-0.85× | Unknown |
| Cost | $100M-$500M+ | 0.7-0.9× | Unknown |
| FDA acceptance | Established | Case-by-case (Jan 2025 guidance) | Not yet |
| EMA acceptance | Established | PROCOVA qualification path | Not yet |
| Portability across indications | Variable | Digital twin must revalidate per disease | Not yet |

The Pareto frontier today is "AI-augmented RCT" — full AI-native trials are not yet regulatory-acceptable.

---

## 12. Connection to Other SDM Methods

| Method | Clinical-trial application |
|---|---|
| **Architecture** | The trial as a system (§2), AI entry points (§3) |
| **Tradespace** | Evidence × speed × cost Pareto (§11) |
| **System dynamics** | Portable-methodology vs. regulator-overfit loops (§8) |
| **Risk / resilience** | ICH E6(R3) hazard analysis for AI sub-systems; FDA COU credibility framework |
| **Governance** | EMA/FDA qualification asymmetry (§4) |
| **DSM** | Coupling between sponsor-CRO-site-regulator must be explicit in AI-augmented trials; new interfaces introduce new couplings |

---

## 13. Research Gaps

1. **Cross-regulator AI qualification framework** — A formal harmonized FDA/EMA/PMDA pathway does not exist; candidate for ICH work.
2. **Digital-twin generalization bounds** — How far can PROCOVA-style prognostic twins generalize across indications?
3. **AI-native trial validation** — No pivotal trial has relied solely on AI-generated evidence; what would one look like?
4. **Economic model of AI trial acceleration** — Realistic NPV model incorporating regulator risk, qualification cost, amortization.
5. **AI-augmented DSMB** — Safety monitoring AI for interim analysis is under-explored.

---

## 14. Sources

- Unlearn.ai EMA qualification blog. https://www.unlearn.ai/blog/success-is-never-a-straight-line--reflecting-on-our-ema-draft-qualification-opinion
- Unlearn.ai digital twins. https://www.unlearn.ai/digital-twins
- Unlearn.ai methodology paper (PROCOVA). https://pmc.ncbi.nlm.nih.gov/articles/PMC12639399/
- Tempus AI IPO announcement. https://www.tempus.com/news/pr/tempus-announces-pricing-of-initial-public-offering/
- Tempus + Ambry Genetics acquisition. https://www.tempus.com/news/acquisition-of-ambry-genetics/
- Tempus + Deep 6 AI acquisition. https://www.tempus.com/news/pr/tempus-announces-acquisition-of-deep-6-ai/
- FDA Draft Guidance on AI for drug development (Jan 7, 2025). https://www.federalregister.gov/documents/2025/01/07/2024-31542/considerations-for-the-use-of-artificial-intelligence-to-support-regulatory-decision-making-for-drug
- FDA — Artificial Intelligence in Drug Development. https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development
- ICH E6(R3) Step 4 Final Guideline (Jan 2025). https://database.ich.org/sites/default/files/ICH_E6(R3)_Step4_FinalGuideline_2025_0106.pdf
- CTTI AI workshop series. https://ctti-clinicaltrials.org/2025-ai-in-drug-biological-product-development/
- AI drug discovery critical review (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12472608/
- BenevolentAI baricitinib COVID-19. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.709856/full
- CDISC standards. https://www.cdisc.org/
- HL7 FHIR IG Clinical Research. https://www.hl7.org/fhir/
- 21st Century Cures Act. https://www.congress.gov/bill/114th-congress/house-bill/34
