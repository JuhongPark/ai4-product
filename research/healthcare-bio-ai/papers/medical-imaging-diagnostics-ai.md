# Medical Imaging & Diagnostics AI: SaMD Reference Architecture and the Foundation-Model Inflection

> **Date:** 2026-04-21
> **SDM lens:** Software-as-a-Medical-Device (SaMD) reference architecture, FDA 510(k)/De Novo/PMA tradespace, workflow integration, narrow-to-foundation model transition

---

## 1. Thesis

Medical imaging AI is the **most mature healthcare AI sub-domain** — 1,451 FDA-authorized AI/ML-enabled devices through end-2025, 295 new clearances in 2025 alone, with radiology accounting for ~76% of cumulative clearances. But the field is at an **architectural inflection point**: the FDA 510(k) framework is built around narrow single-indication predicates, while the market and research are moving toward **foundation models** (Paige Virchow2, Aidoc CARE, Google Med-Gemini) that span multiple indications in one architecture. The SDM question is not "which AI is best at reading X-rays?" — it is "**what is the regulatory reference architecture for a foundation-model SaMD?**"

---

## 2. SaMD Reference Architecture

A canonical FDA-cleared imaging AI system decomposes as:

```
┌─────────────────────────────────────────────────────────────────┐
│                    HOSPITAL ENVIRONMENT                         │
│                                                                 │
│   Imaging modality  →  PACS/VNA  →  Worklist/RIS  →  Viewer     │
│   (CT, MRI, X-ray,     (Sectra,     (Epic Radiant,   (PACS +    │
│    mammo, ultrasound)  Change,      Epic, Oracle)     Aidoc,    │
│                        Merge, GE)                     PowerScribe)│
│                          │                            │         │
│                          ▼                            ▼         │
│                     ┌─────────────────────────────────┐         │
│                     │        AI INFERENCE LAYER       │         │
│                     │                                 │         │
│                     │  DICOM router + AI orchestrator │         │
│                     │  (Aidoc aiOS, Nuance PIN,       │         │
│                     │   Blackford, Ferrum, NewtonAI)  │         │
│                     │                                 │         │
│                     │  AI models (narrow + compound)  │         │
│                     └─────────────────────────────────┘         │
│                          │                                      │
│                          ▼                                      │
│                     Audit log + PCCP envelope                   │
│                     (lifecycle-governed change control)         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                      FDA 510(k) clearance
                      (predicate lineage)
```

The **orchestration layer** (Aidoc aiOS, Nuance Precision Imaging Network, Blackford) is now a distinct architectural component — it abstracts the coupling between PACS and individual AI models, enabling hospitals to stack multiple vendors without per-vendor integration.

---

## 3. The FDA AI/ML-Enabled Device Ecosystem

| Metric | Value | Source |
|---|---|---|
| Cumulative authorizations (end-2025) | 1,451 | FDA AI-Enabled Medical Devices list |
| 2025 new clearances | 295 (record year) | Innolitics 2025 Year in Review |
| 2024 new clearances | 253 | — |
| 2023 new clearances | 221 | — |
| Cumulative radiology share | ~76% | The Imaging Wire, Dec 2025 |
| 2025 specialty mix | Radiology 75%, Cardiovascular 8.8%, Neurology 4.7% | IntuitionLabs FDA tracker |

The database URL slug itself reflects regulatory evolution: **"ai-enabled" replaced "aiml"** in 2025, signaling FDA's expanded view beyond ML.

### Tradespace: 510(k) vs. De Novo vs. PMA

| Pathway | Use case | Evidence burden | Time/cost | Example |
|---|---|---|---|---|
| **510(k)** | Substantial equivalence to predicate | Moderate | 6-12 months, ~$500k-$1M | Most radiology AI |
| **De Novo** | No predicate exists | Higher | 12-18 months, ~$1-2M | Viz.ai (first AI stroke) |
| **PMA** | Class III (highest risk) | Highest (clinical trials) | 2-3+ years, ~$10-20M+ | Rare in imaging |

**Predicate-lineage risk**: A failure mode unique to 510(k) — when one predicate is withdrawn, all downstream substantially-equivalent devices inherit the concern. Foundation models break the predicate-lineage assumption.

---

## 4. Key Organizations and Architectural Positioning

| Organization | Founded | 2025-2026 status | Architectural bet |
|---|---|---|---|
| **Aidoc** | 2016 (NYC/Tel Aviv) | Total funding $370M after **$150M round Sep 2025**. 31 FDA clearances. **CARE** — first "comprehensive foundation model AI" covering 14 acute indications, mean sensitivity 97% / specificity 98%, ~10× fewer false alerts. | Foundation-model worklist triage |
| **Viz.ai** | 2016 | Series D $100M at $1.2B valuation (2022), total raised $289M. First AI De Novo clearance for stroke. **First AI software to get CMS NTAP reimbursement**. | Care-coordination mobile + AI |
| **Paige AI** | 2017 (MSK spinout) | **Virchow2 (632M params)** + **Virchow2G (1.85B params)** — trained on 3.1M whole-slide images, 2.4PB, 225,000 patients, 45 countries. Open non-commercial via Hugging Face. | Pathology foundation model |
| **PathAI** | 2016 | Series C $165M (2024), total $255M. Strategic investors BMS, Labcorp, Merck GHI. | Pharma-dx + pathology |
| **Harrison.ai / Annalise.ai** | 2018 | Series C $112M (Feb 2025); total >$240M. 12 FDA clearances (CXR + brain CT). Rebranded Annalise.ai → Harrison.ai Radiology (Oct 2025). | Multi-modal narrow AI |
| **Rad AI** | 2018 | Series C +$8M (May 2025), total $68M. Strategic: Advocate Health, Memorial Hermann, Corewell, Atlantic Health. | Reporting AI + enterprise platform |
| **Gleamer** | 2017 (Paris) | €27M round → **acquired by RadNet for up to $270M (March 2026)**. ARR CAGR >90% (2022-2025), ~$30M ARR. | Narrow-AI rollup target |
| **Digital Diagnostics (LumineticsCore / IDx-DR)** | 2010 | First **autonomous** AI diagnostic (De Novo 2018). Pooled sensitivity 0.95, specificity 0.91. | Autonomous dx — no physician confirmation needed |
| **Eyenuk EyeArt** | 2010 | Multi-camera DR screener; sens 96% / spec 88% mtmDR. | Autonomous DR screening |
| **AEYE Health** | 2018 | Third FDA-cleared autonomous DR screener. | Autonomous DR screening |
| **Mayo Clinic ECG AI (low EF)** | 2019 onward | **Multisite external validation published JACC Advances Feb 2026**; 78% test-negative rate; CNN on 44,959 ECG-echo pairs. | Academic-medical-center-originated |
| **AliveCor KardiaMobile 6L Max + KardiaAlert (May 2025)** | 2011 | Detects up to 20 arrhythmias with clinician review; >300M ECGs recorded. | Consumer-grade w/ clinician backstop |

---

## 5. The Foundation-Model Inflection

Until 2023, FDA-cleared imaging AI was almost exclusively **narrow** — one model, one indication, one anatomy, one modality. 2024-2025 introduces a new architectural class:

### Foundation models (multi-indication, multi-modality)
- **Aidoc CARE** — 14 acute indications in one workflow, FDA-cleared 2025.
- **Paige Virchow2G** — 1.85B-parameter pathology foundation model, trained on ~3.1M whole-slide images.
- **Google Med-Gemini (April 2024)** — SoTA on 10 of 14 medical benchmarks, MedQA 91.1%, beats GPT-4 on NEJM Image Challenges.
- **Google AMIE** — conversational diagnostic AI beat unassisted clinicians 59.1% vs. 33.6% top-10 accuracy on 303 NEJM CPCs (Nature 2025).
- **MedGemma** — open Gemma-3-based model.
- **CONCH, UNI (Mahmood Lab, Harvard/Brigham, Nature Medicine 2024)** — pathology foundation models, outperformed PLIP on 30+ tasks, NSCLC zero-shot 90.7%.

### Regulatory architecture question
The 510(k) substantial-equivalence paradigm assumes narrow predicates. **How does a foundation model clear 14 indications?**

Options the field is exploring:
1. **Multiple 510(k)s per indication** — Aidoc's path; slow but orthodox.
2. **Single De Novo for foundation model** — no predicate; sets new category.
3. **PCCP envelope for planned indication expansion** — file 510(k) for N indications + PCCP for N+k future additions.
4. **CHAI assurance labels** — voluntary certification supplements FDA (emerging 2025-2026).

The **FDA has not yet issued foundation-model-specific guidance**. This is the open architectural frontier.

---

## 6. The Six Systemic Tensions, Applied

| Tension | How it plays out in imaging AI |
|---|---|
| **Speed vs. evidence** | 510(k) preserves speed (6-12 mo); foundation models strain the predicate framework |
| **Generalization vs. site-specificity** | Domain shift across scanners, stains, demographics — Paige's 45-country training is a counter-strategy |
| **Autonomy vs. oversight** | LumineticsCore / Eyenuk fully autonomous; 99% of other AI remains physician-confirmed |
| **Integration vs. standalone** | Orchestration layer (aiOS, Nuance PIN) enables multi-vendor hospital stacks |
| **Transparency vs. IP** | ONC HTI-1 DSI (2025) — but DSI rule applies at EHR layer, not PACS; imaging AI largely escapes |
| **Equity vs. performance average** | Dermatology (DermAssist not FDA-cleared; skin-tone-bias history); pulse ox; DR screening across populations |

---

## 7. Workflow Integration — The Real Failure Mode

Technical performance is well-characterized; **workflow integration** is where most deployments fail.

**Alert fatigue from narrow-AI stacking**: A hospital that licenses 10 point-solutions (stroke, PE, rib fracture, intracranial hemorrhage, large-vessel occlusion, C-spine, pneumothorax, aortic dissection, vertebral compression, incidental pulmonary nodule) produces a stream of alerts that degrades signal-to-noise. Aidoc CARE's reported 10× fewer false alerts is precisely a solution to this architectural problem, not a model-accuracy claim.

**PACS integration cost**: Each AI vendor must integrate with the hospital's PACS/VNA and RIS; each integration costs $50k-$250k per site per AI, making narrow AI economically infeasible beyond a few vendors. Orchestration platforms (Nuance PIN, Blackford, aiOS) reduce this coupling from O(N×M) hospital-AI pairs to O(N+M).

**Radiologist workflow displacement**: Reading speed vs. interpretation accuracy is a tradespace. AI that is fast-and-noisy costs more cognitive load than it saves. AI that is slow-and-accurate misses real-time triage value.

---

## 8. Key Benchmarks and Datasets

| Benchmark | Scale | Domain |
|---|---|---|
| **RadImageNet** | 1.35M images, 11 anatomic regions | Multi-modality foundation training |
| **CheXpert / CheXpert Plus** (Stanford AIMI) | 223,462 report-image pairs, 64,725 patients | Chest X-ray |
| **HAM10000, ISIC** | Dermatology | Skin cancer (known skin-tone bias) |
| **Diverse Dermatology Images (DDI)** — Daneshjou 2022 | Balanced for Fitzpatrick V-VI | Dermatology equity |
| **UK Biobank** | 500k+ participants, multi-modality | Epidemiology + imaging |

**Observation**: Benchmarks reveal architectural choices. Training on HAM10000 alone produces skin-tone-biased dermatology AI — a **data-provenance-as-interface** issue.

---

## 9. Reimbursement — The NTAP/CPT Interface

An imaging AI that clears FDA but lacks a reimbursement path cannot reach scale. Key milestones:

- **Viz.ai** — first AI software to achieve CMS New Technology Add-on Payment (NTAP).
- **Annalise.ai** — received NTAP.
- **Cleerly (cardiac CCTA)** — 4 Medicare Administrative Contractors began coverage Nov 2024; Aetna approved.
- **CPT codes** for AI — AMA has issued interim codes (e.g., Category III) but permanent codes remain patchy.

**SDM observation**: Reimbursement is **the true Go/No-Go gate** for market scale — not FDA clearance. This is a payer-regulator interface that is often missed in technology-first SDM analyses.

---

## 10. Failure Modes

| Failure mode | Description | Example |
|---|---|---|
| **Domain shift at deployment** | Scanner/stain/demographic differs from training | Paige mitigates via 45-country training |
| **Automation bias** | Clinician defers to AI against their own judgment | Ahn et al. 2023 Eur Radiol — FP rose from 51.4% to 86.0% under incorrect AI |
| **Alert fatigue** | Narrow-AI stacks produce too many false alerts | Motivation for foundation models |
| **Predicate-lineage cascade** | Withdrawn predicate affects downstream devices | Hypothetical under 510(k) framework |
| **Equity degradation** | Population-mean optimization underperforms subgroups | Dermatology (skin tone), pulse oximetry (race) |
| **PACS integration breakage** | Model updates break hospital systems | Routine per-deployment concern |
| **Foundation-model regulatory mismatch** | No clear FDA pathway for multi-indication AI | Open architectural question 2026 |

---

## 11. Connection to Other SDM Methods

| Method | Imaging AI application |
|---|---|
| **Architecture** | SaMD reference architecture (§2); orchestration layer as first-class component |
| **Tradespace** | 510(k) × De Novo × PMA × PCCP × CHAI (§3, §5) |
| **System dynamics** | Alert fatigue as balancing loop; PCCP enables controlled drift |
| **STS** | Radiologist workflow + AI integration (§7) — canonical Trist joint-optimization problem |
| **Risk / resilience** | Automation bias (§10); Safety-II view: radiologists compensate for AI errors through skepticism |
| **Governance** | CHAI assurance; ONC HTI-1 limits; state-level enforcement emerging |

---

## 12. Research Gaps

1. **Regulatory reference architecture for foundation-model SaMD** — open.
2. **Cross-site generalization quantification** — standardized domain-shift benchmarks.
3. **Economic model of orchestration-layer ROI** — value of aiOS vs. point-integration is under-quantified.
4. **Equity-parity certification** — standardized evaluation per Fitzpatrick, age, sex.
5. **Automation-bias countermeasures at UX level** — how AI is *shown* to radiologist affects interpretation.

---

## 13. Sources

- FDA AI-Enabled Medical Devices list. https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices
- Innolitics 2025 Year in Review. https://innolitics.com/articles/year-in-review-ai-ml-medical-device-k-clearances/
- IntuitionLabs FDA AI Medical Device Tracker. https://intuitionlabs.ai/articles/fda-ai-medical-device-tracker
- The Imaging Wire (Dec 2025). https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/
- Aidoc CARE FDA clearance. https://www.aidoc.com/about/news/aidoc-secures-fda-clearance-for-healthcares-first-comprehensive-foundation-model-ai/
- Aidoc $150M round (2025). https://radiologybusiness.com/topics/artificial-intelligence/radiology-artificial-intelligence-firm-aidoc-raises-150m
- Viz.ai Series D. https://www.viz.ai/news/viz-ai-raises-100-million-in-series-d-funding
- Paige Virchow2 press. https://www.paige.ai/press-releases/unlocking-the-complexities-of-cancer-paige-launches-worlds-largest-ai-model
- Virchow2 on Hugging Face. https://huggingface.co/paige-ai/Virchow2
- PathAI Series C. https://www.pathai.com/resources/pathai-announces-completion-of-165-million-financing-for-advancing-medicine-with-ai-powered-pathology
- Harvard CONCH paper. https://hms.harvard.edu/news/researchers-design-foundation-ai-models-use-pathology
- CONCH GitHub. https://github.com/mahmoodlab/CONCH
- Stanford AIMI CheXpert Plus. https://aimi.stanford.edu/datasets/chexpert-plus
- RadImageNet PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC9530758/
- Harrison.ai Series C (TechCrunch). https://techcrunch.com/2025/02/11/australian-healthtech-startup-harrison-ai-scores-112m-series-c/
- Rad AI strategic investments. https://www.radai.com/news/rad-ai-announces-strategic-investments-from-four-leading-health-systems-to-advance-enterprise-ai-in-healthcare
- RadNet acquires Gleamer. https://www.radnet.com/about-radnet/news/radnet-acquires-gleamer-making-radnet-s-deephealth-the-largest-provider-of-radiology-clinical-ai-solutions-worldwide
- Mayo ECG AI JACC Advances (Feb 2026). https://www.jacc.org/doi/10.1016/j.jacadv.2025.102537
- AliveCor KardiaMobile 6L Max launch. https://alivecor.com/press/press_release/alivecor_launches_ai_powered_kardiamobile_6l_max_and_kardiaalert_to_deliver_the_most_advanced_personal_ecg_solution_on_the_market
- Digital Diagnostics LumineticsCore. https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/
- Retina Specialist 2025 DR AI review. https://www.retina-specialist.com/article/ai-for-dr-screening-where-are-we-in-2025
- Google Med-Gemini. https://research.google/blog/advancing-medical-ai-with-med-gemini/
- Google AMIE blog. https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/
- AMIE Nature/PubMed. https://pubmed.ncbi.nlm.nih.gov/40205050/
- MedGemma developer page. https://developers.google.com/health-ai-developer-foundations/medgemma
- Google DermAssist JEADV paper. https://onlinelibrary.wiley.com/doi/full/10.1002/jvc2.246
- Nature Medicine German mammography AI (2024). https://www.nature.com/articles/s41591-024-03408-6
- Ahn et al. Eur Radiol 2023 (automation bias). https://link.springer.com/article/10.1007/s00330-023-09528-w
