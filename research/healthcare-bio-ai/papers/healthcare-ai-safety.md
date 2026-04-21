# Healthcare AI Safety & Resilience: STAMP, Bias, and Safety-II/III

> **Date:** 2026-04-21
> **SDM lens:** STAMP/STPA (Leveson, MIT); resilience engineering (Hollnagel, Rhodes); Safety-II/III; bias as hazard; sociotechnical failure analysis

---

## 1. Thesis

The canonical healthcare AI failures — **Epic Sepsis Model 2021, IBM Watson for Oncology 2017-2018, Optum algorithm 2019, dermatology skin-tone bias, Google's diabetic retinopathy deployment in Thailand, and the medical-LLM hallucination literature** — are not software defects. They are **systems failures** in Leveson's STAMP sense: the control structure between vendor, hospital, clinician, and patient failed to enforce safety constraints, and the AI was the proximate not ultimate cause. Applying Leveson's STAMP, Hollnagel's Safety-II, and Rhodes's resilience engineering produces a diagnostic framework that classical software safety (Fagan inspection, MISRA, DO-178) does not.

---

## 2. STAMP Primer — Why It Applies to Healthcare AI

**STAMP (Systems-Theoretic Accident Model and Processes)** — Nancy Leveson, MIT. Accidents emerge from **inadequate control**, not from component failure alone. A STAMP analysis asks:

1. What are the **safety constraints** the system must enforce?
2. What is the **hierarchical control structure** that enforces them?
3. What are the **unsafe control actions** (UCAs)?
4. What are the **control loop flaws** that cause UCAs?
5. What scenarios produce these flaws?

**STPA (STAMP-based Process Analysis)** is the hazard-analysis method built on STAMP.

Healthcare AI fits STAMP naturally: the AI is one component in a control loop that includes vendor, hospital, clinician, patient, and regulator. When the loop's feedback is degraded — as in the Epic Sepsis Model case — the safety constraint fails even if the AI model performs exactly as trained.

---

## 3. Case Study 1 — Epic Sepsis Model (STAMP analysis)

### Facts (from Wong et al., JAMA Intern Med, Jun 21, 2021)

- n = 27,697 patients, 38,455 hospitalizations at Michigan Medicine, Dec 2018-Oct 2019.
- **AUC 0.63** (developer had claimed 0.76-0.83).
- **Sensitivity 33%**; **PPV 12%**; **missed 67% of sepsis cases** (1,709 of 2,552).
- **18% of patients triggered alerts** → alert fatigue.
- **Oct 2022** — Epic overhauled ESM; now recommends training on hospital's own data (abandoning one-size-fits-all).

### STAMP control structure

```
   ┌────────────────────────────────────────────────────────┐
   │  FDA / Regulator                                       │
   │  (control action: device regulation)                   │
   └──────────────────┬─────────────────────────────────────┘
                      ▼  (Epic ESM claimed clinical decision support
                          — exempt under §3060)
   ┌────────────────────────────────────────────────────────┐
   │  Epic (vendor)                                         │
   │  (control action: ship model with claimed performance) │
   └──────────────────┬─────────────────────────────────────┘
                      ▼  (no requirement for local validation)
   ┌────────────────────────────────────────────────────────┐
   │  Health system (buyer/deployer)                        │
   │  (control action: turn on/off; no local re-training)   │
   └──────────────────┬─────────────────────────────────────┘
                      ▼  (alerts in clinician workflow)
   ┌────────────────────────────────────────────────────────┐
   │  Clinician                                             │
   │  (control action: respond to alert or ignore)          │
   └──────────────────┬─────────────────────────────────────┘
                      ▼
                  Patient outcome
```

### Unsafe control actions (UCAs)

- **UCA-1**: Alert issued when patient did not have sepsis → alert fatigue, clinicians tune out.
- **UCA-2**: No alert when patient did have sepsis → missed treatment window.
- **UCA-3**: Health system turned on ESM without local re-training → model mis-applied to population it was not calibrated for.
- **UCA-4**: Vendor shipped model with generic claim without requiring local validation → control-loop flaw between vendor and health system.

### Control-loop flaws

- **Feedback delay** — the health system had no mechanism to observe ESM's local performance in real time.
- **Missing safety constraint** — no requirement that the model be locally validated before deployment.
- **Regulatory carve-out** — §3060 exempted from FDA; no other regulator held vendor accountable.

### STAMP diagnosis

The canonical failure was **the vendor-deployer interface**: Epic shipped a portable artifact without a local-validation contract; the health system treated it as plug-and-play. This is a **classic Leveson control-structure failure** — no single party was doing the wrong thing individually; the interfaces were inadequate.

### Remediation (Epic 2022)

- Recommend local training on hospital data → closes feedback loop.
- Refined probability thresholds → reduces UCA-1 rate.
- **SDM observation**: The remediation is **architectural, not algorithmic** — it added a control step, it did not tune the model.

---

## 4. Case Study 2 — IBM Watson for Oncology (MD Anderson)

### Facts

- **Feb 2017**: MD Anderson terminated contract with IBM Watson after **$60M+ spent over 3 years** (university audit cited procurement violations).
- **Jul 25, 2018**: STAT News investigation (Ross & Swetlitz) revealed internal IBM docs showing **"unsafe and incorrect" treatment recommendations**.
- Denmark unpublished study: only **~33% agreement with oncologists**.
- **Watson for Oncology was trained on synthetic cases from MSK**, not real patient data — fundamental training-set construct-validity failure.

### STAMP diagnosis

- **UCA**: Treatment recommendation issued without adequate evidence base.
- **Control-loop flaw**: Training distribution (synthetic MSK cases) ≠ deployment distribution (actual oncology patients at MD Anderson and elsewhere).
- **Stakeholder-misalignment**: IBM marketed capability outran evidence; deployer (MD Anderson) trusted vendor claims; no external-validation gate.

### SDM reading

This is the canonical **training-deployment distribution mismatch** — the same failure class as Epic Sepsis, expressed earlier and with more hype. It predates FDA's 2024-2025 attempts to require data-lineage disclosure, which would have caught the synthetic-training problem.

---

## 5. Case Study 3 — Optum Algorithm Racial Bias (Obermeyer et al., 2019)

### Facts

- **Science, Oct 25, 2019** (doi:10.1126/science.aax2342).
- Algorithm used by health systems covering **~200M Americans/year**.
- Used **healthcare costs as proxy for health need** — systematic bias because **less is spent on Black patients for equivalent illness**.
- Reduced Black patients flagged for high-risk care management **by >50%**.
- Optum + Obermeyer replicated on 3.7M patient dataset; **new hybrid (cost + health prediction) achieved 84% bias reduction**.

### STAMP diagnosis

- **UCA**: Flag patient as low-risk when patient is high-risk (misclassification with demographic structure).
- **Control-loop flaw at objective-function layer**: Proxy variable (cost) encoded systemic bias; objective function misaligned with stakeholder outcome (health).
- **SDM framing**: This is a **control-structure failure at design time** — not a model-tuning or data-quality problem but an *architectural choice* of what to optimize. Classical CS+E software verification cannot catch it.

### Remediation

- Objective function reformulated to use health outcomes, not cost.
- **84% bias reduction** is remarkably high — suggests much bias is recoverable once correctly framed.

---

## 6. Case Study 4 — Dermatology Skin-Tone Bias

### Facts

- **Adamson & Smith, JAMA Dermatol, 2018** — training repositories (ISIC, HAM10000) **>70% fair skin**; systematic underrepresentation of Fitzpatrick V-VI.
- **Daneshjou et al., Science Advances, Aug 12, 2022** (doi:10.1126/sciadv.abq6147) — Diverse Dermatology Images (DDI) dataset; existing AI underperformed on dark skin; dermatologists also underperformed on dark skin vs. biopsy-truth; fine-tuning on DDI closed the gap.

### STAMP diagnosis

- **Data-interface failure**: The training dataset was not representative of the deployment population. Upstream data pipeline did not enforce a diversity constraint.
- **Safety-II lens (Hollnagel)**: Dermatologists also underperformed on dark skin. The AI inherits a pre-existing *human* performance gap — the AI is not the only failure point, the human-system baseline was already biased. This is a **system-of-systems** safety issue.

---

## 7. Case Study 5 — Pulse Oximeter Racial Bias

- **Sjoding et al., NEJM, Dec 17, 2020** — **occult hypoxemia in 11.7% Black patients vs. 3.6% White patients**.
- **FDA Safety Communication Feb 19, 2021** — notably did *not* use the word "race."
- **Jan 2025** — FDA issued draft guidance updating premarket evaluation: **n=150 subjects (up from 10)**; mandatory dark/light skin-tone performance testing.
- **SDM reading**: **Physical-layer bias cascades into every downstream AI trained on SpO2.** An architectural defect at the *sensor layer* propagates indefinitely through data and model layers. The only remediation is **upstream** — a sensor redesign — which the 2025 FDA guidance finally forces.

---

## 8. Case Study 6 — Google Diabetic Retinopathy (Thailand Field Study)

### Facts

- **Beede et al., CHI 2020** — "A Human-Centered Evaluation of a Deep Learning System Deployed in Clinics for the Detection of Diabetic Retinopathy."
- **11 clinics, 8 months**.
- Lab accuracy 90% → **>20% images rejected in field** due to low resolution / varied camera conditions.
- **Upload took 60-90 seconds per image** in Thailand connectivity context.
- Nurses discouraged participation fearing patient hardship from referral.

### STAMP diagnosis

- **Context-of-use mismatch**: The sociotechnical system design ignored the environment — infrastructure, workflow, referral logistics.
- **Leavitt-diamond-scale failure**: Tool changed without redesigning task (nurse workflow), people (training), or structure (referral pathway).
- **SDM reading**: The canonical **STS / context-of-use failure**. A lab-accurate AI became field-unusable because its control structure assumed broadband + fast referrals + cooperative nurses.

---

## 9. Medical LLM Hallucination Safety

| Study | Finding |
|---|---|
| **Asgari et al., npj Digital Medicine, May 2025** | 18 experimental configs, 12,999 clinician-annotated sentences: **1.47% hallucination, 3.45% omission** in clinical-note summarization |
| **Omar et al., Communications Medicine, 2025** | Adversarial hallucination attack — 6 leading LLMs, 300 vignettes with single fake clinical entity → models elaborated on planted error in **up to 83% of cases**; mitigation prompt only halved risk |
| **Kim et al. (MIT Media Lab), medRxiv 2025** | "Medical Hallucination in Foundation Models and Their Impact on Healthcare" |
| **MedHallBench** (Pal et al., arXiv:2412.18947, 2024) | Benchmark for medical hallucination |
| **Stanford MyChart AI (JAMA Network Open 2024)** | **7% of unedited drafts would pose risk of severe harm** |

### SDM reading

The LLM hallucination literature shows **safety is a system property, not a model property** — the same model is safe under adversarial-aware prompting and unsafe under naive prompting. The **prompt-engineering interface** is a safety-critical component.

---

## 10. Safety-II / Safety-III — The Resilience View

### Safety-I (classical)

Accidents are failures; safety = absence of failures. Analyze "what went wrong."

### Safety-II (Hollnagel)

Safety emerges from **human adaptive work** that *usually* succeeds. Study "what went right."

- In healthcare AI: the radiologist who catches the AI's false positive, the clinician who edits the MyChart draft before signing, the nurse in Thailand who escalated around the broken referral pipeline — these are **Safety-II successes** that AI safety analysis often ignores.
- **Automation-bias countermeasure**: Designing AI to *support* human adaptive work rather than replace it.

### Safety-III (Leveson, 2023)

Extends STAMP to include **unacceptable losses in sociotechnical systems** beyond accidents — e.g., loss of trust, equity loss, privacy loss. Healthcare AI's equity failures (Optum, dermatology, Thailand DR) are **Safety-III concerns** that Safety-I cannot address.

---

## 11. Resilience Engineering Principles (Hollnagel / Rhodes) for Clinical AI

| Principle | Application to healthcare AI |
|---|---|
| **Monitor** | Post-market AI surveillance (PCCP Impact Assessment) |
| **Anticipate** | Adversarial testing (Omar et al. 2025 methodology) |
| **Respond** | Human override authority; fast rollback |
| **Learn** | Incident database — emerging via CHAI, not yet mandatory |

FDA's PCCP + TPLC guidance is implicitly Safety-II/resilience-aligned — it acknowledges that post-market monitoring, not pre-market gate, is where safety lives.

---

## 12. Automation Bias — The Direct Safety Harm of "Correct" AI

- **Ahn et al., Eur Radiol, 2023** — multi-reader study of AI for chest X-ray lung cancer; **incorrect AI increased both FN (2.7% → 33.0%) and FP (51.4% → 86.0%)** in radiologist reads.

### SDM reading

Even when AI is usually correct, the existence of the AI changes clinician behavior in ways that become *themselves* the safety problem. This is a **second-order safety issue** that classical error-rate metrics miss.

---

## 13. The Failure-Mode Taxonomy

| Failure class | Exemplar | SDM diagnosis |
|---|---|---|
| **Training-deployment distribution mismatch** | Watson Oncology, Epic Sepsis | Architecture: missing local-validation interface |
| **Proxy-variable inversion** | Optum 2019 | Objective-function architectural choice |
| **Data-pipeline bias** | Dermatology AI | Upstream data-interface constraint missing |
| **Physical-layer bias cascade** | Pulse oximetry | Sensor architecture defect |
| **Context-of-use mismatch** | Google DR Thailand | STS failure: tool changed, other 3 dimensions did not |
| **Hallucination (stochastic)** | GPT-4 clinical LLMs | Model architecture; no simple fix |
| **Hallucination (adversarial)** | Omar et al. 2025 | Prompt-interface vulnerability |
| **Automation bias** | Ahn et al. 2023 | UX design as safety property |
| **Alert fatigue** | Epic Sepsis (18% alert rate) | Human-factors failure mode |
| **Non-disclosure** | Stanford/NYU MyChart | Trust/consent safety-III |
| **Regulatory gap** | Babylon (MHRA/CQC) | Inter-regulator interface failure |
| **Unit-economics failure** | Babylon, Forward, Pear | Business architecture, but with safety consequence (care disruption) |

---

## 14. Connection to Other SDM Methods

| Method | Safety application |
|---|---|
| **Architecture** | Every failure above is decomposed to an interface or component |
| **STAMP / STPA** | §3, §4, §5 — the native method |
| **System dynamics** | Alert fatigue as balancing loop; bias amplification as reinforcing |
| **STS** | Thailand DR; MyChart deployments |
| **Resilience engineering** | §10, §11 |
| **Governance** | §13 failure taxonomy is the input to [regulation paper](healthcare-ai-regulation.md) |

---

## 15. Research Gaps

1. **STAMP reference analysis for healthcare AI** — canonical STPA of the Epic Sepsis or Watson Oncology cases published as teaching artifacts.
2. **Safety-II empirical studies** — what do clinicians actually do when AI is wrong, and how often does that preserve safety?
3. **Adversarial safety benchmarks** — MedHallBench is a start; the field lacks a standardized safety-regression suite.
4. **Equity-as-safety certification** — operationalizing Section 1557 AI anti-discrimination as measurable audit.
5. **Incident reporting infrastructure** — an FDA MAUDE-analogue for AI-specific incidents does not exist.
6. **Automation-bias UX guidelines** — how to present AI outputs so clinicians neither over-trust nor under-trust.

---

## 16. Sources

- Wong et al. Epic Sepsis. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
- Obermeyer et al. Optum. https://www.science.org/doi/10.1126/science.aax2342
- Daneshjou et al. dermatology. https://www.science.org/doi/10.1126/sciadv.abq6147
- Sjoding et al. pulse oximetry NEJM. https://www.nejm.org/doi/full/10.1056/NEJMc2029240
- STAT IBM Watson investigation. https://www.statnews.com/2017/09/05/watson-ibm-cancer/
- Beede et al. Google Thailand CHI 2020. https://dl.acm.org/doi/fullHtml/10.1145/3313831.3376718
- Ahn et al. Eur Radiol 2023. https://link.springer.com/article/10.1007/s00330-023-09528-w
- Nature Med German mammography AI (2024). https://www.nature.com/articles/s41591-024-03408-6
- Medical LLM hallucination framework (Asgari et al., npj Digital Medicine 2025). https://www.nature.com/articles/s41746-025-01670-7
- Adversarial hallucination in LLMs (Omar et al., Communications Medicine 2025). https://www.nature.com/articles/s43856-025-01021-3
- MedHallBench (Pal et al.). https://arxiv.org/abs/2412.18947
- Babylon Health (Wikipedia). https://en.wikipedia.org/wiki/Babylon_Health
- Leveson, *Engineering a Safer World* (MIT Press, 2011).
- Hollnagel, *Safety-II in Practice* (Routledge, 2017).
- Rhodes & Ross (MIT), resilience engineering publications via MIT SEARI. http://seari.mit.edu/
