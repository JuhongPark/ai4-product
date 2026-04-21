# Drug Discovery AI: Pipeline Architecture and Tradespace

> **Date:** 2026-04-21
> **SDM lens:** Architecture decomposition (discovery pipeline as a system), tradespace exploration (physics-based vs. deep-learning vs. hybrid), lifecycle (target ID → preclinical → clinical), real options (pipeline portfolio value)

---

## 1. Thesis

Drug discovery is an SDM problem disguised as chemistry. The **drug-discovery pipeline** is a 10-15-year, $1-2B, multi-gated system with attrition rates above 90% from preclinical to approval. AI has entered this pipeline not as a single tool but as a **set of architectural components** — structure prediction, generative chemistry, property prediction, virtual screening, lab automation. The SDM question is not "which AI model wins" but **"which architecture of the pipeline maximizes expected NPV across the tradespace of evidence, speed, and attrition risk?"** The canonical 2024-2026 evidence shows no single architecture dominates; the Pareto frontier is populated by hybrid physics + DL approaches, not pure foundation models.

---

## 2. The Drug Discovery Pipeline as a System

```
Basic biology      Target ID      Hit discovery     Lead opt       Preclinical    Clinical
─────────────      ─────────      ─────────────     ───────        ───────────    ────────
Disease assoc.  →  Validated   →  Virtual +      →  ADMET, PK  →   Tox, safety →  Phase I→II→III → Approval
                   target         physical                         IND filing       NDA/BLA
                                  screens
                                  ↓
Role of AI:        Genomics ML    AlphaFold-class   Gen. chem.     Pred ADMET     Synthetic controls
                   target omics   struct. pred      (MolGPT,       models         (Unlearn)
                   causal inf     Docking + DL      Chai-1)        QSAR           Patient ID (Deep6)
                                                    Active learn   Surrogate EP   Protocol opt
```

Time: 3-6 yr discovery + 6-7 yr clinical. AI historically touched **only the first columns**. 2024-2026 movement: AI now proposes candidates that enter the clinic *and* reshapes how clinical evidence is generated (see [Clinical Trials AI paper](clinical-trials-ai.md)).

---

## 3. The Four AI Sub-Architectures

### 3.1 Protein structure prediction

- **AlphaFold 2 (2021, Nature)** — transformer-based single-protein structure prediction, CASP14 breakthrough.
- **AlphaFold 3 (May 2024, Nature)** — Evoformer (48 blocks) replaced by simpler Pairformer (4 blocks); Structure Module replaced by a Diffusion Module generating raw atom coordinates; MSA shrunk and discarded after 4 blocks. Predicts protein-ligand, protein-nucleic-acid, protein-protein, ion, and modified-residue complexes. Source code released Nov 2024 under **CC-BY-NC-SA 4.0 (non-commercial)** — AlphaFold Server is free for academics only.
- **ESMFold (Meta, 2022)** — language-model embeddings replace MSA; faster but lower accuracy on novel folds.
- **OpenFold / RoseTTAFold / RoseTTAFold All-Atom** — open-source alternatives.
- **Boltz-1 (MIT Jameel Clinic, 2024)** — open-source AlphaFold 3-class model.

**SDM interpretation**: Structure prediction is a **boundary condition** for downstream pipelines — it is not a drug, it is an input. Its value is captured by pipelines that feed it into generative chemistry or docking, not by use in isolation. The **AF3 non-commercial license is a first-class architectural interface constraint** — it forces commercial pharma onto Isomorphic Labs partnerships or open alternatives (Chai-1, Boltz-1). Licensing is a system interface, not a legal footnote.

### 3.2 Generative chemistry

- **MolGPT, MolMIM, Chemformer** — transformer-decoder language-model approaches to molecule generation on SMILES.
- **Chai-1 (Chai Discovery, bioRxiv Oct 2024)** — multi-modal foundation model; 77% PoseBusters ligand-RMSD success (beats AF3's 76%), 75.1% DockQ on protein-protein (beats AF-Multimer 2.3's 67.7%). Open-source `chai_lab` pip, CC-licensed weights.
- **Chai-2 (2025)** — zero-shot antibody design demonstrated at 24-well plate scale.
- **Diffusion models for molecules** (MolDiff, DiffDock).
- **RetroSynth / RXNMapper** — retrosynthesis planning so generated molecules are *synthesizable*.

**Architectural issue**: Generative chemistry produces *candidates*, not drugs. The Pareto trade is **diversity vs. synthesizability vs. target affinity** — all three rarely co-optimized.

### 3.3 Property & ADMET prediction

- **ChemProp (MIT)** — graph neural networks for molecular properties, foundational.
- **DeepPurpose, MolBERT** — pretrained molecular property models.
- **QSAR (classical)** — regression on chemical descriptors; still often outperforms DL on small, well-curated datasets.

**SDM interpretation**: Property prediction is where **data debt** matters most — bench datasets rarely generalize to clinical pharmacology. The Pareto frontier here favors **ensemble (physics + ML + QSAR) over pure DL**.

### 3.4 Autonomous / self-driving labs

- **Berkeley A-Lab (Szymanski et al., *Nature*, Nov 2023)** — autonomous synthesis and characterization of inorganic materials; 36 of 57 target compounds in 17 days; 50-100x human throughput. Palgrave et al. critique (2024) disputed the novelty of claimed "new materials," showing many were known phases — a canonical validation-layer failure mode for self-driving-lab claims.
- **Eli Lilly Life Sciences Studio + Strateos** (San Diego, $90M, expanded 2024): 100+ instruments, 5M-compound storage, remote-controlled closed-loop.
- **Strateos pivot (2024)** — abandoned public cloud-subscription model for private on-prem — a business-model failure mode distinct from technical validity.
- **Carnegie Mellon Cloud Lab (2024)** — first university autonomous lab; 100+ concurrent experiments.
- **NVIDIA + Lilly co-innovation lab (announced 2025)** — up to **$1B over 5 years** on NVIDIA Vera Rubin architecture; Lilly TuneLab integrates NVIDIA Clara foundation models.
- **MIT, Toronto (Aspuru-Guzik), Liverpool (Cooper)** — academic self-driving-lab research groups.

**SDM interpretation**: Self-driving labs are the **cyber-physical component** of the discovery system — software orchestration meets instrument actuation. Architecture: scheduler → instrument abstraction layer → robotic arm + reader → data pipeline → planner. This is compound-AI-as-lab, not just ML-on-data. The A-Lab critique and Strateos pivot are both validation-layer (not model-layer) failures — a recurring theme in healthcare/bio AI systems.

---

## 4. Key Organizations and Their Architectural Positioning

| Organization | Founded | 2024-2026 status | Architectural bet |
|---|---|---|---|
| **Isomorphic Labs** (Alphabet spinout, 2021) | 2021 | Lilly deal Jan 2024: $45M upfront + $1.7B milestones. Novartis Jan 2024: $37.5M + $1.2B, expanded Feb 2025. **Series A $600M (Mar 2025, Thrive Capital)** — first external round. Oncology candidates approaching first-in-human. | AlphaFold 3 as closed platform; partnering > internal clinic |
| **Recursion Pharmaceuticals** (NASDAQ: RXRX) | 2013 | Exscientia merger closed Nov 2024, $688M deal. BioHive-2 (504 H100, 2 exaflops). Q1 2025 rework: 6 active programs. NVIDIA $50M PIPE (2023). | Phenotypic image-based ML + gen chem; pipeline company |
| **Insilico Medicine** | 2014 | **Rentosertib (INS018_055) Phase IIa GENESIS-IPF**: 60 mg QD FVC +98.4 mL vs placebo −20.3 mL; Nature Medicine Jun 2025. HK IPO Dec 30, 2025 raised **$293M**, opened ~$2.7B mkt cap. | End-to-end AI pipeline; first AI-discovered + AI-designed Phase II drug |
| **Schrödinger** (NASDAQ: SDGR) | 1990 | Physics-based FEP+ hybrid with ML active learning; Takeda zasocitinib (TAK-279, Nimbus) in Phase III. Mkt cap ~$946M (Apr 2026), down 37% YoY. | Physics-first, ML-augmented — anti-pure-DL thesis |
| **Chai Discovery** | 2024 | Chai-1 open-source AF3-class (bioRxiv Oct 2024); Chai-2 zero-shot antibody design 2025. | Open science + foundation model |
| **Xaira Therapeutics** | 2024 | **$1B Series A** launch Apr 2024 (Arch, Foresite), ~$2.7B valuation. | Ex-Genentech leadership; broad platform |
| **Generate:Biomedicines** | 2018 | Nasdaq IPO early 2026, $425M raised; ~$2B market cap. Novartis, Samsung, NVIDIA backed. | Generative protein design |
| **NVIDIA (BioNeMo / Clara)** | 2023 platform | **$1B Lilly co-innovation lab** (2025); EVO 2 foundation model Feb 2025 w/ Arc / Stanford / Berkeley. | Infrastructure layer |
| **Tempus AI** (NASDAQ: TEM) | 2015 | IPO June 2024 at $37/share, $410.7M raised, ~$6B initial mkt cap. 2025 rev $1.27B (+83.4% YoY). Ambry ($600M) + Deep 6 AI acquisitions. | Multimodal data + AI platform, biology-to-clinic |
| **AbsCI** | 2020 | Protein-design-focused biologics | Generative protein design |
| **Atomwise, BenevolentAI** | 2012/2013 | BenevolentAI BEN-2293 (atopic dermatitis, pan-TRK) failed efficacy vs placebo despite meeting safety — canonical AI-validation-chasm case. Company scaled down, closed US offices, pivoted to early-stage partnerships. | Pre-foundation-model generation |

**SDM observation**: The field is **not converging on a single architecture**. Physics-first (Schrödinger), phenotypic-first (Recursion), structure-first (Isomorphic), and end-to-end (Insilico) all produce candidates that reach clinic. This is Pareto behavior, not dominant-design behavior.

---

## 5. Tradespace Analysis

Plotting drug discovery architectures on a simplified tradespace:

| Axis | Pure physics (Schrödinger class) | Hybrid (Recursion, Isomorphic) | Pure DL foundation models |
|---|---|---|---|
| **Cost per candidate** | High (compute-intensive MD simulations) | Medium | Low (inference) |
| **Generalization to novel targets** | High (physical laws) | Medium | Low (training data distribution) |
| **Throughput** | Low | Medium-high | Very high (virtual library scan) |
| **Explainability to FDA reviewers** | High | Medium | Low |
| **Evidence burden for first human dose** | Baseline | Baseline (no extra AI burden) | Baseline (AI is not the drug) |
| **Dependency on proprietary data** | Low | High (phenotypic images) | High (training corpus) |

No corner dominates. The Pareto frontier is populated by **hybrid architectures** that mix methods at each pipeline stage — physics for free-energy calculations, DL for hit expansion, phenotypic ML for target validation.

---

## 6. Lifecycle — AI-Native Pipeline vs. AI-Assisted Pipeline

Two architectural paradigms for deploying AI in drug discovery:

### 6.1 AI-assisted (majority)

AI is a **tool** used by medicinal chemists, computational biologists, DMPK scientists. The pipeline stages are unchanged; AI accelerates specific steps. Most pharma use this.

**Pros**: Low organizational disruption, bounded risk, no new validation regime.
**Cons**: Benefits limited to local speedups; pipeline throughput unchanged if the bottleneck is elsewhere (e.g., wet-lab validation, IND-enabling tox).

### 6.2 AI-native (minority — Recursion, Insilico, Isomorphic)

The pipeline is **re-architected around AI** — phenotypic-first, massive ML-inferred candidate pools, AI-driven hypothesis generation at the front end. Wet-lab and clinic remain but serve an AI-planned agenda.

**Pros**: Throughput step-change possible; novel target classes reachable.
**Cons**: Organizational reinvention; still-pending clinical validation that AI-native candidates outperform classically-derived ones.

**SDM question**: Is AI-native a new dominant design, or a parallel form that will co-exist? 2026 evidence is inconclusive — AI-native companies have produced IND-ready and Phase II candidates but not yet approved drugs at the rate required to invalidate classical pharma.

---

## 7. Feedback Loops and Emergent Behavior

**Virtuous loop**: Each AI-designed candidate that reaches clinic creates **labeled data** for the next training cycle. Recursion's phenotypic imaging is the canonical example.

**Vicious loop — data debt**: Public molecular datasets (ChEMBL, PubChem, BindingDB) are **biased toward published, often-failed chemistry**. Models trained on these inherit publication bias, underperforming when extrapolating to novel chemical space.

**Vicious loop — target fashion**: High-profile targets (e.g., KRAS G12C, PROTACs) attract AI attention; AI output accumulates in the same target classes, causing herding rather than exploration. System dynamics lens: AI lowers the cost of "me-too" work faster than it lowers the cost of genuinely novel work.

**Risk loop**: Poorly-validated AI tools can generate **plausible but wrong** candidates that consume wet-lab and clinical resources. The value of AI is strictly bounded by downstream **real-world assay gating**.

---

## 8. Interfaces and Standards

The drug discovery AI stack has several emerging interface specifications:

- **mmCIF / PDB** — Structural data exchange (classical).
- **SMILES, InChI, SELFIES** — Molecule representation (classical + DL-friendly).
- **BioNeMo (Nvidia)** — Software platform for hosting biology models.
- **OpenAPI / gRPC** for cloud lab APIs — Strateos, Emerald.
- **SiLA 2** — laboratory instrument interface standard; not AI-specific but critical for self-driving labs.
- **FAIR data principles** — research data stewardship.

**SDM observation**: Unlike software SaaS (where MCP is emerging as the dominant AI-tool interface), drug discovery AI lacks a dominant interface standard for model ↔ pipeline coupling. Each vendor defines its own. This is a strategic opportunity for the first open standard to emerge.

---

## 9. Stakeholder Map (Discovery-Specific)

| Stakeholder | Primary interest | Interface to discovery AI |
|---|---|---|
| Medicinal chemist | Synthesizable, novel candidates | Desktop or web UI, SMILES, structure viewer |
| Computational chemist | Workflow, benchmarks | Python / Jupyter / scripting |
| DMPK / tox scientist | Predictive ADMET | Property prediction pipelines |
| Biology / target ID | Target validation | omics + phenotypic screens |
| Translational scientist | Preclinical → clinical bridge | Biomarker + disease models |
| Clinical development | IND-ready candidates | CMC + tox package |
| Business development | Licensing-ready assets | IP + data room |
| Regulatory affairs | IND package, AI disclosure | FDA/EMA regulatory submissions |
| IT / research informatics | Compute, data governance | Cluster, cloud, storage |
| Partners / CROs | Integration | APIs, data contracts |

The multi-interface, multi-stakeholder nature is why **generic "AI drug discovery" platforms underperform**: they optimize one interface and lose the others.

---

## 10. Failure Modes

| Failure mode | Description | Prior cases |
|---|---|---|
| **Overfit virtual screen** | Model proposes candidates that bind in silico, fail biophysically | Historical virtual-screening disappointments, 1990s-2000s |
| **Clinical attrition despite AI** | Candidate progresses to clinic, fails efficacy or safety for reasons AI didn't model | **BenevolentAI BEN-2293 (atopic dermatitis, pan-TRK)** failed efficacy vs placebo |
| **Reproducibility / novelty-claim failure** | Results depend on unreleased data, disputed "new" discoveries | **Berkeley A-Lab critique** (Palgrave et al., 2024) showed many claimed new materials were known phases |
| **Business-model failure despite technical success** | Platform works but market/pricing model breaks | **Strateos pivot** (2024) — abandoned public cloud subscription for private on-prem |
| **Regulatory surprise** | FDA/EMA requires additional non-AI validation | Emerging as FDA (Jan 2025 draft guidance) and EMA (PROCOVA qualification path) diverge |
| **IP contamination** | Training data includes copyrighted / competitor structures | Ongoing dispute (Isomorphic vs. public dataset boundaries) |
| **Licensing-as-interface constraint** | Model license prohibits commercial use of outputs | AlphaFold 3 CC-BY-NC-SA forces commercial pharma onto Isomorphic partnerships or Chai-1/Boltz-1 |

---

## 11. Connection to Other SDM Methods

| SDM method | Drug-discovery application |
|---|---|
| **Architecture** | Pipeline decomposition + sub-architectural choice (§3–4) |
| **Tradespace** | Physics vs. DL vs. hybrid Pareto (§5) |
| **Real options** | Pipeline portfolio valuation — each AI-discovered candidate is an option on clinical success |
| **System dynamics** | Target fashion, data-debt, virtuous-loop dynamics (§7) |
| **DSM** | Task coupling between medicinal chemistry, biology, DMPK teams (AI changes the DSM by abstracting some handoffs) |
| **STS** | Chemist-AI joint work is closer to the sales-skill frame (information work) than CDS is — but still STS |

---

## 12. Research Gaps

1. **No SDM reference architecture** for AI-native drug discovery pipelines — INCOSE-style modeling is absent.
2. **Empirical AI-vs-classical attrition comparison** — we lack matched cohorts of AI-discovered vs. classically-discovered candidates progressing through clinic.
3. **Data provenance standards** — training data contamination, dataset licensing, and IP leakage are not standardized.
4. **Economic model** — NPV of AI-accelerated discovery under different attrition assumptions is rarely published.
5. **Safety-by-design** — AlphaFold 3 can predict off-target binding; integrating this into a STAMP-style hazard analysis of candidates is unexplored.

---

## 13. Sources

- Jumper, J. et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature*. https://www.nature.com/articles/s41586-021-03819-2
- Abramson, J. et al. (2024). "Accurate structure prediction of biomolecular interactions with AlphaFold 3." *Nature*. https://www.nature.com/articles/s41586-024-07487-w
- Isomorphic Labs. (2024). "Isomorphic Labs and Eli Lilly partnership." https://www.isomorphiclabs.com/articles
- Recursion Pharmaceuticals (2024). Exscientia merger announcement. https://ir.recursion.com/
- Insilico Medicine (2024). "INS018_055 Phase IIa trial results." https://insilico.com/
- Schrödinger / Lilly collaboration (2024). Press releases via https://www.schrodinger.com/
- Chai Discovery (2024). "Chai-1 open-source model release." https://www.chaidiscovery.com/
- Szymanski, N. J. et al. (2023). "An autonomous laboratory for the accelerated synthesis of novel materials." *Nature*. https://www.nature.com/articles/s41586-023-06734-w
- Palmer, T. et al. (2024). "Critique of the A-Lab claims." (retraction and response published in *Nature*)
- NVIDIA BioNeMo documentation. https://docs.nvidia.com/bionemo-framework/
- FDA. "Using Artificial Intelligence and Machine Learning in the Development of Drug and Biological Products — Discussion Paper and Request for Feedback." (2023). https://www.fda.gov/
- ChemProp. https://github.com/chemprop/chemprop
- Boltz-1 (MIT Jameel Clinic, 2024). https://jclinic.mit.edu/
- OpenFold. https://github.com/aqlaboratory/openfold
- RoseTTAFold. https://www.ipd.uw.edu/
