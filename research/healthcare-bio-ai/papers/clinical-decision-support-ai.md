# Clinical Decision Support & Ambient Scribes: STS Joint Optimization of Clinician + AI

> **Date:** 2026-04-21
> **SDM lens:** Socio-technical systems (joint optimization), compound AI for documentation, regulatory-arbitrage architecture, Leavitt's diamond applied to clinical workflows

---

## 1. Thesis

Ambient AI scribes and EHR-integrated clinical decision support have produced the most aggressive valuation growth in healthcare AI in 2024-2026 — **Abridge $5.3B (June 2025), OpenEvidence $12B (January 2026)**. The growth is not explained by superior ML — the underlying models are not exotic. It is explained by a **regulatory-arbitrage architecture**: ambient scribes deploy as "clinical documentation" tools that escape FDA device classification, while integrating deeply into EHR-mediated clinician workflows. From an SDM perspective this is a **Trist/Tavistock joint-optimization problem**: the AI tool, the clinician task, the clinician role, and the hospital's documentation structure must co-design, or deployments regress to the METR-style negative or null results.

---

## 2. The Clinical Workflow Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                    PATIENT ENCOUNTER                            │
│                                                                 │
│   Check-in → Triage → Exam → Orders → Documentation → Billing   │
│                                                                 │
│     ↕          ↕        ↕       ↕          ↕              ↕    │
│                                                                 │
│                         EHR (Epic / Oracle Health / athena)     │
│                          ▲                     ▲                │
│                          │                     │                │
│                    ┌─────┴──────────┬──────────┴─────┐          │
│                    ▼                ▼                ▼          │
│              Ambient scribe    Clinical DSS    Diagnostic LLM   │
│              (Abridge,         (Epic Art,      (OpenEvidence,   │
│               DAX Copilot,     Cosmos, IBC)    Glass,           │
│               Suki, Nabla,                     UpToDate         │
│               Heidi, Freed,                    Expert AI)       │
│               DeepScribe)                                       │
└─────────────────────────────────────────────────────────────────┘
                    │                 │
                    ▼                 ▼
              Clinical note     Order/billing    Patient message
              (Part of record)  (Part of record) (MyChart ART)
```

**Key architectural observation**: Ambient scribes, CDS, and patient-message AI are **converging into a single agentic voice-first layer** (Dragon Copilot, Oracle Health Clinical AI Agent, Epic Art + Emmie). The interface boundary that used to separate documentation from decision support is dissolving.

---

## 3. The Regulatory-Arbitrage Architecture

Ambient scribes position as "clinical documentation tools" — non-device under FDA's §3060 Cures Act exemption and under Part 3 of the CDS guidance (HCP independently reviews basis). This permits:

- Rapid deployment without 510(k)/De Novo/PMA
- Continuous model updates outside PCCP
- Integration via Epic App Orchard and Oracle Health without device-level review

The **interface to escape** is critical: the scribe produces *a note the clinician reviews and signs*. If the clinician materially reviews, the AI is non-device. If they do not, FDA or state AG could reclassify (Texas AG Pieces Technologies 2024 is the canonical case: UDAP enforcement on accuracy claims, not FDA device enforcement).

**SDM observation**: Regulatory arbitrage *is* the architecture. Abridge's $5.3B valuation and OpenEvidence's $12B reflect investor confidence that this non-device pathway will hold. If FDA reclassifies, the tradespace collapses.

---

## 4. Key Organizations and Trajectory

### 4.1 Ambient scribes

| Organization | Founded | 2025-2026 status | Architectural position |
|---|---|---|---|
| **Abridge** | 2018 (Pittsburgh) | **Series E $300M at $5.3B valuation (June 2025)**, doubling from $2.75B (Feb 2025 Series D). **150+ health systems**, **$117M contracted ARR Q1 2025**. First ambient AI officially integrated into Epic via "Pal" program (2023). Investors: a16z, Khosla. | Enterprise Epic-integrated; dominant in health systems |
| **Microsoft Dragon Copilot** (Nuance DAX → Dragon) | Launched Mar 3, 2025 | GA US/Canada May 2025; UK/DE/FR/NL following. **Dragon Copilot Nursing GA Dec 2025**. **PowerScribe One preview (RSNA 2025)** adds radiology. Microsoft paid $19.7B for Nuance (2022). | Enterprise via Microsoft ecosystem; Copilot + M365 integration |
| **Suki** | 2017 | Series D $70M (Oct 2024), ~$500M valuation, total $168M. Series D-II Jan 2025. **EHR integrations**: Epic, Oracle Health/Cerner, MEDITECH, athenahealth. Nursing consortium Oct 2025. | Multi-EHR ambient |
| **Nabla** | 2018 (Paris) | **Series C $70M (June 2025)**, total $120M. 130+ healthcare orgs, 85,000 clinicians. Pivoting to agentic (coding agent, context-aware agent). | European-origin + agentic pivot |
| **Heidi Health** | 2019 (Melbourne) | **Series B $65M (Oct 2025)** at $465M valuation, Point72 lead. Total ~$100M. 2M+ consults/week, 110 languages, 116 countries, 20-EHR integrations. | Global + language breadth |
| **Freed** | 2022 | **Series A $30M (Mar 2025)** Sequoia-led. >$20M ARR Apr 2025; 25,000+ clinicians. | Indie-physician / SMB / browser-EHR |
| **DeepScribe** | 2017 | Series A $30M, Series B $24M. **Specialty-focused** (oncology, urology, cardiology). Bidirectional sync Epic/athena/eCW. KLAS 99.5. | Specialty depth |
| **Augmedix** | 2013 | **Acquired by Commure Q3 2024 for $139M**, delisted NASDAQ. Combined Commure+Augmedix run rate >3M appointments/yr. | Rolled into Commure stack |
| **Doximity GPT (DoxGPT)** | Launched 2023 | 3M+ registered members (~85% US physicians). **Acquired Pathway Medical Aug 2025 for $63M**. AI use: 47% → 63% (Apr 2025 → Jan 2026). | Physician-network distribution |

### 4.2 Diagnostic / decision-support LLMs

| Organization | Founded | 2025-2026 status | Architectural position |
|---|---|---|---|
| **OpenEvidence** | 2021 (Mayo Clinic Platform Accelerator alum) | **Feb 2025 $75M Series A @ $1B → Jul 2025 $210M @ $3.5B → Jan 2026 $250M Series D @ $12B**. | Retrieval-augmented, peer-reviewed-corpus-only; doctor-facing |
| **Glass Health** | 2021 (YC) | Seed $5M (Initialized Capital); Google for Startups AI First cohort. Used at Harvard, Stanford, Johns Hopkins. | Differential dx + ambient scribe |
| **UpToDate Expert AI** (Wolters Kluwer) | Sep 2025 | 30-yr UpToDate + GenAI. Closed retrieval from peer-reviewed corpus, no open-web hallucination. **Microsoft partnership** (Dragon Copilot, M365, Teams). Adopted by 70% of WK's largest enterprise customers. UpToDate Lexidrug (drug-ref) added Nov 2025. | Corpus-owner advantage |

### 4.3 EHR-vendor-integrated AI

| Vendor / product | Status | Architectural position |
|---|---|---|
| **Epic Cosmos** | De-identified multi-system EHR (~250M patients) for "similar patient" predictions | Data-network-effect moat |
| **Epic MyChart In-Basket "Art"** | **>1M drafts/month across 150+ health systems.** Stanford Medicine study (JAMA Network Open 2024): AI drafts reduced cognitive load/burnout despite NOT saving objective time; **7% of unedited drafts posed risk of severe harm**. Disclosure policies diverge: UCSD discloses, Stanford/UW/UNC/NYU chose non-disclosure. | Embedded, invisible-to-patient by default |
| **Epic "Emmie"** (MyChart digital concierge, UGM 2025) | Answers lab questions, proposes appointments, screens | Patient-facing agent |
| **Oracle Health Clinical AI Agent** | Launched March 2025; GA across 30+ specialties. ~30% documentation time reduction. Next-gen cloud-native EHR debuted Aug 2025 (ambulatory first; acute 2026). | EHR-vendor competitive response |
| **Epic "Penny"** (RCM) | RCM-focused | Financial ops AI |

---

## 5. The STS Lens — Why Adoption Outcomes Differ

Applying Leavitt's diamond (cf. [socio-technical-ai-systems.md](../../ai-systems/papers/socio-technical-ai-systems.md) in Layer 3):

| Dimension | Before ambient AI | With ambient AI | Joint-optimization question |
|---|---|---|---|
| **Task** | Clinician types/dictates note post-visit | AI listens, drafts note; clinician reviews/signs | What is the reviewable unit — sentence, paragraph, full note? |
| **Technology** | EHR keyboard input + Dragon dictation | Ambient mic + AI transcription/summarization + EHR write-back | Mic quality, room acoustics, multi-speaker, code-switching |
| **People** | Clinician authors note | Clinician becomes editor-in-chief | New literacy: prompt-like "cues" in conversation; training burden |
| **Structure** | Notes signed end-of-day, bulk | Notes signed visit-by-visit, inline | Reshapes the workflow, scheduling, billing-department handoffs |

**The Abridge bet**: Joint optimize all four dimensions by integrating deeply with Epic + dedicating customer-success teams to workflow redesign.
**The "bolt-on" failure mode**: Deploy an AI scribe without redesigning structure/people/task — observe marginal or negative productivity (the METR-style null result in healthcare context).

---

## 6. The Empirical Record (2024-2026)

| Study / source | Finding |
|---|---|
| **Stanford Medicine (JAMA Network Open, 2024)** | MyChart AI draft replies: reduced cognitive load/burnout, **did not save objective time**; 7% unedited drafts would pose severe-harm risk |
| **Oracle Health CAA** | ~30% documentation time reduction (vendor-reported) |
| **Abridge** | 150+ systems, $117M ARR Q1 2025 — adoption signal, not efficacy signal |
| **Doximity physician AI use survey** | 47% → 63% (Apr 2025 to Jan 2026); voice documentation 20% → 29%; accuracy concerns persist |
| **Kung et al. PLOS Digital Health 2023** | ChatGPT passed USMLE at ~60% threshold — baseline LLM capability |
| **Lee, Bubeck, Petro NEJM 2023** | "Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine" — foundational risk doc for clinical LLMs |

**Observation**: Vendor adoption data (Abridge ARR, Dragon Copilot GA expansion) is outpacing **independent efficacy data**. We have a familiar vendor-vs-independent measurement gap — the same productivity-paradox shape as [METR productivity paradox](../../productization-skills/papers/metr-productivity-paradox.md), here in the clinical documentation context.

---

## 7. The Compound AI Architecture of a Modern Ambient Scribe

A 2026 ambient scribe is a **compound AI system**, not a single model:

```
Audio input
   ↓
┌──────────────┐
│ VAD + multi- │
│ speaker sep. │──→ Speech-to-text (Whisper-class)
└──────────────┘
   ↓
┌──────────────┐       ┌─────────────────┐
│  LLM-based   │──────→│ Retrieval over  │
│  summarizer  │       │ specialty notes │
└──────────────┘       └─────────────────┘
   ↓
┌──────────────┐
│  Structure   │
│  extractor   │──→ ICD-10 codes, CPT, orders, medications
└──────────────┘
   ↓
┌──────────────┐
│  Write-back  │──→ Epic/Oracle/athena via FHIR/HL7
└──────────────┘
   ↓
┌──────────────┐
│  Clinician   │
│  sign-off    │
└──────────────┘
```

The **orchestration** (routing, caching, retry, fallback), **FHIR write-back** (EHR interoperability), and **sign-off interface** are where differentiation lives — not in the base LLM. Abridge's Epic "Pal" partnership is a moat *via interfaces*, not via models.

---

## 8. The Equity & Bias Layer

- **Code-switching and non-native-English accents** — ASR accuracy degrades; Heidi Health's 110-language claim is an architectural response.
- **Specialty & regional vocabulary** — DeepScribe's specialty-focus is a direct response to general-purpose scribe underperformance in oncology/cardiology.
- **Documentation bias carry-over** — If the EHR historically documents certain demographics with fewer words, the AI reproduces the gap.
- **MyChart AI patient-message non-disclosure** — An equity/informed-consent issue: Stanford/UW/UNC/NYU's non-disclosure policies raise questions that Texas AG (Pieces) and California AG (Jan 2025 advisory) are watching.

---

## 9. Connection to Other SDM Methods

| Method | CDS / ambient-scribe application |
|---|---|
| **Architecture** | Compound AI pipeline (§7); orchestration as first-class |
| **STS / joint optimization** | §5 — the entire deployment question |
| **System dynamics** | Note-quality balancing loop: AI writes fluent notes → clinician signs more → signed notes become training data → model drifts toward the style observed |
| **Risk / resilience** | Stanford 7% severe-harm rate; Pieces settlement as adversarial test |
| **Governance** | ONC HTI-1 DSI (clinical decision support disclosure, effective Jan 2025) |
| **Tradespace** | Specialty-depth (DeepScribe) vs. breadth (Abridge) vs. global (Heidi); no dominant design |

---

## 10. Failure Modes

| Failure mode | Description | Concrete case |
|---|---|---|
| **Hallucinated content in signed note** | AI invents symptoms, history, meds | Documented across ambient scribes |
| **Non-disclosure to patient** | MyChart AI drafts labeled as physician-authored | Stanford/UW/UNC/NYU policy choice — legal risk |
| **Severe-harm rate** | 7% of unedited drafts could harm | Stanford study |
| **Automation sign-off** | Clinician signs without review under time pressure | Structural failure mode |
| **Regulatory reclassification** | FDA or state AG reclassifies scribe as device | Texas AG Pieces 2024 (accuracy-claim theory) |
| **STS regression** | Tool adopted without redesigning structure/people/task | Canonical Trist failure |

---

## 11. Research Gaps

1. **Independent RCT of ambient scribes** — Burnout, note quality, and patient-safety joint outcomes by site are under-measured.
2. **Equity audit of ambient scribes** — No standardized evaluation across language, accent, specialty, patient demographic.
3. **STS experiment** — Cross over site designs explicitly comparing bolt-on vs. workflow-redesigned deployments.
4. **Reclassification-contingency modeling** — What happens to Abridge/OpenEvidence valuations if FDA moves?
5. **Disclosure requirement economic model** — Cost of mandated AI-authorship disclosure vs. patient-trust gains.

---

## 12. Sources

- Abridge Series E. https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/
- Abridge $300M Series E coverage. https://www.fiercehealthcare.com/ai-and-machine-learning/ambient-ai-startup-abridge-scores-300m-series-e-backed-a16z-and-khosla
- Microsoft Dragon Copilot launch. https://news.microsoft.com/source/2025/03/03/microsoft-dragon-copilot-provides-the-healthcare-industrys-first-unified-voice-ai-assistant-that-enables-clinicians-to-streamline-clinical-documentation-surface-information-and-automate-task/
- Suki Series D. https://sacra.com/c/suki/
- Suki $70M coverage. https://www.fiercehealthcare.com/ai-and-machine-learning/suki-banks-70m-build-out-ai-assistants-doctors-it-inks-more-health-system
- Nabla Series C. https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html
- Heidi Health Series B. https://www.bloomberg.com/news/articles/2025-10-06/ai-health-startup-heidi-gets-point72-funds-at-465-million-value
- Heidi press. https://www.heidihealth.com/blog/blog-heidi-series-b
- Freed $30M. https://www.fiercehealthcare.com/health-tech/fierce-healthcare-fundraising-tracker-freed-picks-30m-ai-clinician-assistant
- Freed VentureBeat. https://venturebeat.com/ai/freed-says-20000-clinicians-are-using-its-medical-ai-transcription-scribe-but-competition-is-rising-fast
- DeepScribe. https://www.deepscribe.ai/
- Commure acquires Augmedix. https://www.healthcaredive.com/news/commure-acquire-augmedix-ai-documentation/721978/
- Doximity Physician AI use survey. https://investors.doximity.com/news/news-details/2026/Doximity-Study-Finds-Physicians-Rapidly-Adopting-AI-But-Accuracy-Concerns-Persist/default.aspx
- OpenEvidence $12B Series D. https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html
- OpenEvidence Business Wire. https://www.businesswire.com/news/home/20260121029132/en/OpenEvidence-Raises-$250-Million-to-Build-Medical-Superintelligence-for-Doctors
- Glass Health. https://glass.health/
- UpToDate Expert AI. https://www.wolterskluwer.com/en/news/uptodate-expert-ai-genai-clinical-decision-support
- Epic UGM 2025 AI features. https://www.fiercehealthcare.com/health-tech/epic-unveils-major-ai-features-ai-charting-microsoft-cosmos-ai-risk-prediction-and-rcm
- Oracle Health Clinical AI Agent. https://www.oracle.com/news/announcement/physicians-reduce-documentation-time-with-oracle-health-clinical-ai-agent-2025-03-04/
- Oracle Health new EHR. https://www.fiercehealthcare.com/health-tech/oracle-health-debuts-ai-powered-ehr-designed-voice-first-solution-embedded-agentic-ai
- Stanford MyChart AI study. https://med.stanford.edu/news/all-news/2024/03/ai-patient-messages.html
- Kung et al. PLOS Digital Health 2023. https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198
- Lee, Bubeck, Petro NEJM 2023. https://www.nejm.org/doi/abs/10.1056/NEJMsr2214184
