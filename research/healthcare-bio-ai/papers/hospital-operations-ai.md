# Hospital Operations AI: System Dynamics of RCM and the Prior-Auth Arms Race

> **Date:** 2026-04-21
> **SDM lens:** System dynamics (Forrester/Sterman), two-sided AI adoption, stakeholder game theory, arms-race feedback loops, revenue-cycle architecture

---

## 1. Thesis

Hospital operations AI is the **most consequential and under-studied** healthcare AI sub-domain. Medical documentation and back-office RCM (revenue-cycle management) constitute **~60% of all healthcare IT spending**. The defining 2024-2026 development is not a new model — it is the **emergence of two-sided AI adoption between payers and providers**, producing a system-dynamics arms race that is already reshaping access to care. The **UnitedHealth / nH Predict** lawsuit is the canonical case: AI-assisted denial at scale generated 22.7% denial rate (2022) from 10.9% (2020). The SDM question is not about ROI of any one tool; it is about the **coupled feedback loops** between payer AI and provider AI and the regulatory gate that may or may not close them.

---

## 2. The Hospital as a System

```
┌───────────────────────────────────────────────────────────────┐
│                   FRONT-OFFICE OPERATIONS                     │
│  Patient access · Scheduling · Registration · Eligibility     │
└───────────────────────────────────────────────────────────────┘
                              ↓
┌───────────────────────────────────────────────────────────────┐
│                   CLINICAL DELIVERY                           │
│  OR · ED · Inpatient · Ambulatory · Imaging · Lab             │
└───────────────────────────────────────────────────────────────┘
                              ↓
┌───────────────────────────────────────────────────────────────┐
│                   MID- AND BACK-OFFICE                        │
│  Coding · Billing · Claims · Denials · Appeals · Collections  │
└───────────────────────────────────────────────────────────────┘
                              ↓
┌───────────────────────────────────────────────────────────────┐
│                   PAYER INTERFACE                             │
│  Prior auth · Claim adjudication · Contract · Utilization mgmt│
└───────────────────────────────────────────────────────────────┘
```

AI is deployed at every layer. The **payer-interface layer** is where arms-race dynamics are most severe.

---

## 3. Revenue Cycle Management (RCM) AI Landscape

| Organization | Focus | 2024-2026 status |
|---|---|---|
| **Waystar** (NASDAQ: WAY) | End-to-end RCM | **NASDAQ IPO June 7, 2024 at $21.50/share, raised $967.5M** — largest health-tech IPO since 2022. Market cap $3.58B at IPO, $4.30B by Q4 2024. AI denial-prevention + appeals generator |
| **Nym Health** | Autonomous medical coding (Clinical Language Understanding) | **$47M growth round Oct 2024** (PSG led). Processes >6M charts annually, 6 specialties. Epic Showroom Toolbox "Fully Autonomous Coding" designation Aug 2024 |
| **CodaMetrix** (MGH spinout) | AI coding | **$40M Series B Mar 2024** ($220M valuation); $109M total. Claims 60% coding-cost reduction, 70% denial reduction, 5-week AR acceleration, 96%+ autonomous. Epic Toolbox Aug 2024 |
| **Fathom Health** | AI coding | Google Ventures, Lightspeed backed |
| **Notable Health** | Ambient revenue cycle ("Notable Assistant") | 80% of health systems exploring/piloting/deploying GenAI for RCM in 2025 |
| **Commure + Athelas** | RCM + ambient AI rollup | **$6B valuation merger Oct 2023**. Acquired Augmedix 2024. **HCA Healthcare exclusive ambient AI partner Oct 2024**. $200M growth financing June 2025 (General Catalyst) |
| **Thoughtful AI** | RCM automation | $20M Series A (Drive Capital); 350% YoY revenue growth 2024 |
| **Adonis** | RCM | $31M June 2024 |

**Market**: AI in healthcare RCM projected to $180.33B by 2034 (24.2% CAGR). AI health-tech investment $10.7B in 2025 (+24.4% YoY).

### Architectural observation

RCM is the **most ambient-AI-ready** domain in healthcare: (a) the work product is structured (ICD, CPT, HCPCS codes), (b) error tolerance is financial not clinical, (c) the payer interface is codified. This explains why RCM AI went from novelty to $6B-merger consolidation in 18 months.

---

## 4. Prior Authorization AI — The Arms Race

Prior authorization (PA) is where AI dynamics become adversarial.

### 4.1 The UnitedHealth / nH Predict case

- **Class action filed Nov 14, 2023** (*Estate of Gene B. Lokken v. UnitedHealth Group*) by Clarkson Law Firm.
- Complaint alleges **90% error rate** (measured via reversal rate on appeal).
- Internal documents: managers required clinical staff to keep rehab stays within **1% of algorithm-projected days**.
- **0.2% of denied patients appeal** — the algorithm's PA denial effectively becomes final for 99.8% of cases.
- **Feb 13, 2025 ruling**: federal court denied UnitedHealth motion to dismiss; breach-of-contract and bad-faith claims proceed.

### 4.2 The Senate Permanent Subcommittee on Investigations Report (Oct 17, 2024)

- **UHC prior-auth denial rate: 10.9% (2020) → 16.3% (2021) → 22.7% (2022)**.
- UHC + CVS denied post-acute care at **3× their overall denial rate**. Humana at **16× overall**.
- CVS initially projected $10-15M savings from its algorithm, later revised to $77.3M.
- Humana LTACH denial rate rose 54% 2020-2022.

### 4.3 The provider-side response

- **Epic "Penny"** (RCM) and agents that auto-generate PA appeals.
- **Waystar** and other RCM vendors promote AI-driven appeal generation explicitly.
- **AMA survey**: physicians + staff spend **12 hours/week on prior auth** — a direct cost driver for AI automation.

### 4.4 System-dynamics arms race

```
Payer AI denies more   ←────┐
     │                      │   feedback delay:
     ▼                      │   appeals take weeks;
Provider AI appeals more    │   patients harmed during delay
     │                      │
     ▼                      │
Payer tightens AI criteria  │
     │                      │
     ▼                      │
Provider escalates AI ──────┘
```

**SDM diagnosis**: A classic two-sided arms race with asymmetric stakes — the patient, not either AI, bears the delay cost. Regulatory intervention (NY SB 7896, CA AG advisory, Senate report) is the only exogenous variable capable of breaking the loop.

---

## 5. Scheduling, Bed Management, Patient Flow

| Organization | Focus | Status |
|---|---|---|
| **LeanTaaS** | OR, infusion, inpatient-bed scheduling (iQueue products) | **Acquired Hospital IQ January 2023**, combined EV >$1B. 180+ US health systems, 500+ hospitals, 43 states. Real-Time View (mobile-first) 2024. Example: Inova 46% block fill rate |
| **Qventus** | Inpatient-discharge origin, expanded to perioperative | Surgeon gamification as differentiator |
| **Apella** | Newer OR optimization | Competes w/ LeanTaaS + Qventus + Epic OR Marketplace |

---

## 6. Supply Chain and Labor

- **GHX** (Healthcare supply-chain platform): **Acquired Prodigo Solutions April 2023**. **GHX ResiliencyAI suite July 2025** (Perfect Order Co-Pilot + Resiliency Center). Supports **$220B annual supply-chain spend**.
- **Staffing AI** (ShiftPixy, WorkLlama, CLEARESULT) — fragmented, no breakout leader.

---

## 7. The EHR-Vendor RCM Integration

- **Epic Emma / Art / Penny** (UGM 2024) — ~200 GenAI features.
  - **Emma** = patient assistant
  - **Art** = clinician assistant (deployed across 150 systems, 1M drafts/month for documentation)
  - **Penny** = RCM
- **Oracle Health CAA + next-gen EHR (Aug 2025)** — ambulatory first, acute 2026.

**SDM observation**: EHR vendors are *absorbing* RCM AI functionality natively. This reshapes the tradespace for independent RCM AI vendors — they must either become Epic/Oracle-toolbox partners (Nym, CodaMetrix) or differentiate on specialty/scale (Waystar). The platform-vs-point tension plays out architecturally.

---

## 8. Stakeholder Map (Hospital-Ops-Specific)

| Stakeholder | Primary interest | AI interface |
|---|---|---|
| Hospital CFO / CRO (Chief Revenue Officer) | Collections, AR days | RCM dashboards, denial analytics |
| Revenue-cycle staff | Throughput, denial rate | Coding AI, appeal generators |
| Physician | Documentation burden, reimbursement | Ambient scribe, coding suggestions |
| Patient | Out-of-pocket cost, PA delay | Portal explanations, PA status |
| Payer | Medical necessity, cost | PA AI, claim-adjudication AI |
| Federal regulator (CMS, OIG) | Fraud, waste, abuse | Audit trails, billing pattern detection |
| State AG / commissioner | Consumer protection | UDAP, PA law enforcement |
| Plaintiff bar | Harm recovery | Discovery on AI decisions |
| Congressional oversight | Policy / public interest | Subcommittee reports (PSI Oct 2024) |

The **plaintiff bar + state AGs** emerge as the enforcement layer where federal regulators have been slow.

---

## 9. The Six Systemic Tensions, Applied

| Tension | Hospital-ops manifestation |
|---|---|
| Speed vs. evidence | RCM AI deploys without regulatory gate; errors are financial not clinical |
| Generalization vs. site-specificity | Local payer-mix dictates RCM AI tuning; national platforms struggle |
| Autonomy vs. oversight | Nym "autonomous coding" vs. human-in-loop — liability allocation unresolved |
| Integration vs. standalone | EHR-native (Epic Penny) vs. best-of-breed (Waystar, Nym) |
| Transparency vs. IP | Payer PA algorithms remain opaque — nH Predict case |
| Equity vs. performance average | Post-acute denials fall disproportionately on older, sicker patients |

---

## 10. Failure Modes

| Failure mode | Description | Case |
|---|---|---|
| **Proxy-variable inversion** | AI optimizes cost/denial rate, proxy-fails on care-appropriateness | nH Predict, Humana post-acute |
| **Automation-bias lock-in** | Staff accept AI-generated denials without review | UHC rehab 1%-of-projected rule |
| **Regulatory-coverage gap** | Payer AI falls between FDA (not a device), FTC, state insurance dept | Pre-2024; NY SB 7896 / CA advisory now closing |
| **Arms-race spend** | Payer and provider both spend on AI, cancel each other out | Systemic outcome — no single culprit |
| **Coding-AI hallucination** | Billing codes fabricated from ambiguous charts | Known pattern in coding AI |
| **Equity degradation** | High-cost specialties (post-acute, rehab) denied disproportionately | Senate PSI data |

---

## 11. Connection to Other SDM Methods

| Method | Hospital-ops application |
|---|---|
| **System dynamics** | Two-sided arms race (§4); classic balancing + reinforcing loops |
| **Architecture** | Hospital system layers (§2); RCM AI as mid-office module |
| **Tradespace** | EHR-native vs. best-of-breed RCM (§7) |
| **STS** | RCM staff role changes under autonomous coding (Nym) |
| **Governance** | nH Predict as canonical AI-governance failure — private algorithm at public-safety scale |
| **Real options** | Flexible contracts with multiple RCM vendors as hedge against platform lock-in |

---

## 12. Research Gaps

1. **Formal system-dynamics model** of payer/provider AI arms race, calibrated on Senate PSI data.
2. **STAMP analysis** of nH Predict as safety-critical system (see [safety paper](healthcare-ai-safety.md)).
3. **Economic impact model** of AI-driven PA on hospital margin and patient access.
4. **Legal-architecture analysis** of UDAP/state enforcement as de facto federal regulation.
5. **Interoperability standards** for payer↔provider AI communication — no FHIR-equivalent exists for PA AI.
6. **Workforce-impact model** of autonomous coding on RCM staff (Nym, CodaMetrix).

---

## 13. Sources

- UnitedHealth class action (STAT). https://www.statnews.com/2023/11/14/unitedhealth-class-action-lawsuit-algorithm-medicare-advantage/
- Medicare Advantage AI denials (HealthcareDive). https://www.healthcaredive.com/news/medicare-advantage-AI-denials-cvs-humana-unitedhealthcare-senate-report/730383/
- STAT Senate investigation recap. https://www.statnews.com/2024/10/17/medicare-advantage-insurers-ai-technology-prior-authorization-claims-denials-senate-investigation/
- UnitedHealth suit survives motion to dismiss. https://skillednursingnews.com/2025/02/lawsuit-against-unitedhealth-over-ai-based-denials-of-post-acute-care-moves-ahead/
- Class-action advances. https://www.healthcarefinancenews.com/news/class-action-lawsuit-against-unitedhealths-ai-claim-denials-advances
- Waystar IPO (CNBC). https://www.cnbc.com/2024/06/07/waystar-shares-slip-in-debut-after-pricing-ipo-in-middle-of-range-.html
- Nym Health $47M. https://www.healthcareittoday.com/2024/11/08/autonomous-medical-coding-engine-nym-announces-47-million-growth-investment-led-by-psg/
- CodaMetrix Series B. https://hitconsultant.net/2024/03/12/codametrix-secures-40m-for-ai-driven-medical-coding-solutions/
- Commure $200M. https://www.commure.com/press-releases/commure-raises-200m-in-growth-financing-from-general-catalysts-cvf-to-accelerate-ai-powered-rcm-platform
- Commure + Athelas merger. https://www.fiercehealthcare.com/health-tech/health-tech-companies-commure-athelas-unveil-merger-plans-drive-automation-llm-tech
- LeanTaaS + Hospital IQ. https://leantaas.com/press-releases/leantaas-acquires-hospital-iq-to-create-ai-innovator-for-hospital-operations-optimization/
- Apella landscape blog. https://apella.io/blog/exploring-the-or-schedule-optimization-landscape-leantaas-qventus-epic-or-marketplace-and-apella
- GHX ResiliencyAI. https://www.ghx.com/news-releases/2025/ghx-deploys-new-wave-of-ai-capabilities-to-advance-the-healthcare-supply-chain/
- NY SB 7896 (legislative context). https://www.nysenate.gov/legislation/bills/2023/S7896
- NY DFS Circular Letter No. 7 (2024). https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
- CA AG Jan 2025 advisory. https://www.wsgr.com/en/insights/california-ag-issues-legal-advisory-regarding-use-of-ai-in-healthcare.html
