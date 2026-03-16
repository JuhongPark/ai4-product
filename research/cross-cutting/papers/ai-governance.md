# AI Governance: A Research Survey

**Compiled: March 2026**  
**Scope: 2022-2026 literature, standards, and public policy**

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Key Findings and Trends (2022-2026)](#2-key-findings-and-trends-2022-2026)
3. [What AI Governance Means](#3-what-ai-governance-means)
4. [The Multi-Level AI Governance Stack](#4-the-multi-level-ai-governance-stack)
5. [Global Policy, Standards, and Regulatory Landscape](#5-global-policy-standards-and-regulatory-landscape)
6. [An Operating Model for Organizational AI Governance](#6-an-operating-model-for-organizational-ai-governance)
7. [Governance Across the AI Product Lifecycle](#7-governance-across-the-ai-product-lifecycle)
8. [Generative and Agentic AI Governance](#8-generative-and-agentic-ai-governance)
9. [Implications for Product Teams](#9-implications-for-product-teams)
10. [Research Gaps and Open Questions](#10-research-gaps-and-open-questions)
11. [Notable Papers and Sources](#11-notable-papers-and-sources)

---

## 1. Introduction

AI governance has moved from a largely aspirational topic to an operational requirement. Between 2022 and 2026, organizations shifted from publishing high-level AI principles to building concrete governance systems: inventories, risk-tiering workflows, impact assessments, model and system documentation, human oversight controls, monitoring processes, incident response procedures, and procurement rules. This transition was accelerated by the public release of generative AI systems in late 2022 and by the growth of foundation-model platforms, copilots, and autonomous or semi-autonomous agents.

In practice, AI governance now sits at the intersection of:

- public policy and regulation,
- organizational management systems,
- technical risk controls,
- procurement and vendor management,
- and product lifecycle decision-making.

For product teams, AI governance is no longer just a compliance concern. It changes which use cases are viable, how products are scoped, what evidence must be collected before launch, how vendors are selected, and how systems are monitored after release.

---

## 2. Key Findings and Trends (2022-2026)

### 2.1 From Principles to Operational Controls

The dominant pattern in the literature and policy landscape is the move from ethics principles to implementation mechanisms. Governance is increasingly expressed through management systems, lifecycle gates, documented responsibilities, and measurable controls rather than solely through principle statements about fairness, transparency, or accountability.

### 2.2 Risk and Impact Assessment Became the Core Mechanism

Across standards and policy frameworks, risk assessment and impact assessment emerged as the central governance instruments. This is visible in the EU AI Act's risk-based architecture, NIST's AI RMF, ISO/IEC 23894 risk management guidance, ISO/IEC 42005 impact assessment guidance, and the Council of Europe's HUDERIA methodology.

### 2.3 Governance Expanded Beyond the Model to the Full Sociotechnical System

A major insight from recent research is that governance cannot focus only on models. Governance must address data pipelines, prompting layers, tool access, user interfaces, organizational incentives, vendor dependencies, monitoring, and downstream uses. This is especially important for generative AI and agentic systems whose behavior depends heavily on deployment context.

### 2.4 Interoperability Is Now a Strategic Requirement

Organizations increasingly operate across multiple jurisdictions and must align internal controls with overlapping frameworks: OECD principles, UNESCO guidance, EU AI Act requirements, NIST AI RMF practices, ISO standards, sector rules, and procurement obligations. Governance maturity now depends partly on the ability to crosswalk these frameworks instead of managing each in isolation.

### 2.5 Generative and Agentic AI Exposed New Governance Gaps

Generative AI magnified governance concerns around opacity, copyright, misinformation, data provenance, prompt injection, model misuse, and dynamic outputs. Agentic AI adds further challenges: action autonomy, tool permissions, environment access, memory management, and difficulty assigning accountability when systems act across multiple steps or tools.

### 2.6 Governance Is Becoming a Product Capability

In 2026, leading governance programs increasingly treat documentation, oversight, testing, auditability, and post-deployment controls as part of the product architecture itself. In other words, governance is no longer purely external to product development; it is part of how modern AI products are designed.

---

## 3. What AI Governance Means

AI governance is best understood as the set of structures, processes, controls, and accountability mechanisms used to direct, constrain, and monitor the development, deployment, use, and retirement of AI systems.

It is related to, but distinct from, neighboring concepts:

| Concept | Primary focus |
|--------|---------------|
| **AI ethics** | Normative values such as fairness, autonomy, justice, and non-maleficence |
| **AI regulation** | Legally binding external obligations imposed by governments and regulators |
| **AI risk management** | Identifying, assessing, mitigating, and monitoring AI-related risks |
| **AI governance** | The broader organizational and institutional system that translates principles and rules into decisions, controls, and accountability |

Recent review work reinforces this distinction. Papagiannidis, Mikalef, and Conboy (2025) argue that the field must distinguish between responsible AI principles and the governance practices required to operationalize them. Their review frames responsible AI governance through **structural, relational, and procedural practices**, which is a useful way to connect ethics, management, and implementation.

Similarly, Batool, Zowghi, and Bano (2025) show that AI governance artifacts operate at multiple layers: **team, organization, industry, national, and international levels**. That layered view is especially useful for product teams because many practical failures happen when governance responsibilities are clear at one layer but absent at another.

---

## 4. The Multi-Level AI Governance Stack

AI governance is not a single framework. It is a stack of interacting layers.

| Layer | Main question | Typical artifacts |
|------|---------------|------------------|
| **International norms** | What broad values and public-interest goals should shape AI? | OECD AI Principles, UNESCO Recommendation, Council of Europe Convention |
| **Regulation and public policy** | What is legally required? | EU AI Act, sector rules, procurement rules, agency policy |
| **Organizational governance** | Who is accountable internally, and how are decisions made? | AI policies, governance boards, role charters, approval workflows |
| **Risk and impact management** | How are harms identified, evaluated, and mitigated? | Risk registers, AI impact assessments, red-teaming, testing plans |
| **Technical and operational controls** | What controls make governance enforceable in practice? | Logging, access controls, evaluations, monitoring, fallback mechanisms |
| **Lifecycle and product governance** | How do controls map to product stages? | Intake, launch reviews, post-market monitoring, incident response, retirement plans |

This stack matters because governance failures often happen at the seams:

- a regulator requires transparency, but the product team lacks documentation processes;
- a company adopts AI principles, but procurement allows opaque vendor dependencies;
- a system passes pre-launch review, but nobody owns monitoring after deployment;
- an LLM is safe in isolation, but unsafe once given tools, memory, and production access.

---

## 5. Global Policy, Standards, and Regulatory Landscape

### 5.1 OECD and UNESCO

The OECD AI Principles remain one of the foundational international governance reference points. The OECD updated the Principles on **3 May 2024** to better reflect the realities of general-purpose and generative AI, explicitly highlighting privacy, intellectual property, safety, and information integrity. This matters because it shows how governance language is evolving from abstract trustworthiness toward more concrete problem categories.

In **February 2025**, the OECD launched the **Hiroshima AI Process Reporting Framework**, giving companies a structured mechanism to report their risk management and accountability practices for advanced AI systems. This is significant because it pushes governance toward comparable, cross-company disclosure rather than one-off principle statements.

UNESCO's **Recommendation on the Ethics of Artificial Intelligence** remains influential because it combines global legitimacy with implementation-oriented tools. UNESCO emphasizes four core values:

1. human rights and human dignity,
2. peaceful, just, and interconnected societies,
3. diversity and inclusiveness,
4. environmental and ecosystem flourishing.

UNESCO also developed practical implementation mechanisms such as the **Readiness Assessment Methodology (RAM)** and **Ethical Impact Assessment (EIA)**. These tools are especially relevant for governments and public-interest institutions, but they also offer a useful model for firms building human-rights-oriented governance processes.

### 5.2 The EU AI Act

The EU AI Act is the most consequential binding governance development of the 2022-2026 period.

Key dates matter here:

- The Act entered into force on **1 August 2024**.
- It becomes fully applicable on **2 August 2026**.
- Prohibitions, definitions, and AI literacy provisions have applied since **2 February 2025**.
- Governance rules and obligations for general-purpose AI models have applied since **2 August 2025**.
- Some high-risk rules for AI embedded in regulated products extend to **2 August 2027**.

The Act is built around a **risk-based approach**:

- prohibited practices,
- high-risk systems,
- transparency obligations for certain systems,
- and lower-risk uses subject mostly to existing law.

For product teams, the AI Act has three especially important implications:

1. **Classification becomes strategic.** Teams must determine whether a system is prohibited, high-risk, subject to transparency duties, or outside the added AI Act obligations.
2. **Documentation becomes mandatory infrastructure.** Providers of high-risk systems and providers of general-purpose AI models must maintain technical and governance documentation.
3. **Post-launch governance matters.** The Act is not just about pre-market controls; it also creates expectations around monitoring, human oversight, and lifecycle accountability.

The Act also pushed governance upstream into foundation-model development. Providers of general-purpose AI models face obligations around documentation and copyright-related measures, while providers of GPAI models with systemic risk face additional obligations to assess and mitigate systemic risks. The EU's **General-Purpose AI Code of Practice**, finalized in **July 2025**, is an example of how governance is being translated into operational expectations for model providers.

### 5.3 NIST and the United States

In the United States, the most important governance reference remains the **NIST AI Risk Management Framework (AI RMF 1.0)**, released on **26 January 2023**. NIST positions the framework as:

- **voluntary**,
- **rights-preserving**,
- **non-sector specific**,
- and applicable across the AI lifecycle.

Its four core functions are:

1. **Govern**
2. **Map**
3. **Measure**
4. **Manage**

This structure has become one of the most influential organizing logics for enterprise AI governance programs because it is practical without being overly prescriptive.

NIST extended this work through the **Generative AI Profile** released on **26 July 2024**, a cross-sectoral companion resource for applying AI RMF concepts to generative AI. As of early 2026, NIST's AI Resource Center indicates that **AI RMF 1.0 is being revised** and that the Playbook will be updated after **AI RMF 1.1** is published. That is an important signal that governance guidance is becoming iterative rather than static.

The federal policy picture changed materially in 2025. On **23 January 2025**, President Trump issued **Executive Order 14179**, revoking Executive Order 14110 and directing agencies to revise existing AI policies. The next major federal governance move came with OMB's revised memos, issued **3 April 2025** and publicly announced **7 April 2025**:

- **M-25-21**, on federal AI use, introduced the category of **high-impact AI**, required minimum risk management practices for such use cases, required inventories, and reinforced Chief AI Officer governance roles.
- **M-25-22**, on AI procurement, emphasized privacy protections, cross-functional review, interoperability, and safeguards against vendor lock-in.

These memos are notable not because they create a general private-sector AI law, but because they show what operational governance looks like in practice: inventories, accountable officers, impact assessments, pre-deployment testing, ongoing monitoring, and procurement controls.

### 5.4 ISO and Formal Management Standards

The ISO/IEC standards ecosystem became substantially more relevant to AI governance during this period.

Three standards are particularly important:

- **ISO/IEC 23894:2023**: guidance on AI-specific risk management.
- **ISO/IEC 42001:2023**: the first AI management system standard.
- **ISO/IEC 42005:2025**: guidance on AI system impact assessment.

ISO/IEC 42001 is especially significant because it treats AI governance as an organization-wide management system rather than a set of isolated controls. ISO describes it as the world's first AI management system standard and frames it as a structured way to manage AI-related risks and opportunities across an organization.

ISO/IEC 23894 adds risk management guidance tailored specifically to AI, while ISO/IEC 42005 focuses on how organizations should identify, evaluate, and document the impacts of AI systems on people and society throughout the lifecycle.

Together, these standards suggest a maturing governance architecture:

- **42001** for management system structure,
- **23894** for risk management,
- **42005** for impact assessment.

### 5.5 Council of Europe: Rights-Based Governance

The **Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law** was opened for signature on **5 September 2024**. It is the first international legally binding treaty in this area.

The Convention is important because it anchors AI governance explicitly in:

- human rights,
- democracy,
- and the rule of law,

rather than only in innovation policy or technical safety.

The Council of Europe also developed **HUDERIA**, a risk and impact assessment approach tailored to these values. HUDERIA combines:

- a structured methodology for risk and impact assessment,
- a context-based risk analysis model,
- and stakeholder engagement as part of the assessment process.

In **February 2026**, the Council of Europe approved the HUDERIA COBRA resources, further operationalizing this approach. For organizations working in public-sector, civic, or high-stakes contexts, HUDERIA is one of the clearest examples of a governance method that integrates technical review with democratic and rights-based analysis.

---

## 6. An Operating Model for Organizational AI Governance

The strongest recent literature suggests that effective AI governance requires three interacting practice types:

1. **structural practices**,
2. **relational practices**,
3. **procedural practices**.

### 6.1 Structural Practices

Structural practices define who owns AI governance and where decisions are made.

Common structural components include:

- executive accountability for AI use,
- a cross-functional AI governance board,
- designated AI leadership roles such as Chief AI Officer or Responsible AI Office,
- central policy and standards repositories,
- and role clarity between builders, deployers, risk owners, and auditors.

The main design challenge is balancing central consistency with local product velocity. Highly centralized governance can become a bottleneck; highly decentralized governance creates inconsistency and "shadow AI."

### 6.2 Relational Practices

Relational practices determine how governance is coordinated across functions and with external actors.

These include:

- coordination between product, legal, security, privacy, and compliance teams,
- supplier and vendor governance,
- stakeholder participation,
- escalation and exception management,
- and communication pathways between technical teams and senior decision-makers.

This dimension is often overlooked. In practice, governance fails when cross-functional coordination fails, even when policies exist on paper.

### 6.3 Procedural Practices

Procedural practices are the repeatable workflows that turn governance into daily operations.

Typical procedural controls include:

- intake and registration of AI use cases,
- risk classification and tiering,
- AI impact assessment,
- pre-deployment testing and red-teaming,
- documentation requirements,
- human oversight plans,
- launch approval,
- monitoring and incident response,
- and retirement or decommissioning procedures.

The OMB memos are useful here because they show how procedural governance can be specified concretely: public inventories, high-impact use case determination, impact assessments, testing, waiver tracking, and discontinuation of non-compliant systems.

### 6.4 A Practical Enterprise Pattern

Across the standards and policy landscape, a recurring enterprise operating pattern is emerging:

| Governance capability | Purpose |
|----------------------|---------|
| **AI inventory** | Know what AI systems exist, where they operate, and who owns them |
| **Risk tiering** | Apply more intensive review where harms are higher |
| **Impact assessment** | Analyze effects on rights, safety, groups, and society |
| **Documentation** | Preserve traceability for internal review and external accountability |
| **Human oversight** | Define when humans approve, intervene, override, or stop the system |
| **Testing and evaluation** | Validate intended performance and surface harmful failure modes |
| **Monitoring** | Detect drift, misuse, performance degradation, and emerging harms |
| **Incident response** | Escalate, remediate, notify, and learn from failures |
| **Vendor governance** | Control data use, IP rights, portability, and vendor dependencies |

---

## 7. Governance Across the AI Product Lifecycle

For AI product teams, governance works best when mapped directly onto lifecycle stages.

| Lifecycle stage | Key governance questions | Example controls |
|----------------|--------------------------|------------------|
| **Problem framing** | Is the use case legitimate, necessary, and proportionate? Who could be harmed? | Use-case review, stakeholder mapping, red-line policies |
| **Data sourcing** | Is the data lawful, representative, licensed, and fit for purpose? | Data provenance checks, licensing review, privacy review |
| **Model selection / build** | What are the model's known limits and risks? What third-party dependencies exist? | Model cards, vendor due diligence, evaluation plans |
| **System design** | How will users understand, challenge, or override AI outputs? | UX disclosures, human-in-the-loop design, fallback paths |
| **Pre-launch evaluation** | Has the system been tested for intended and foreseeable misuse? | Red-teaming, scenario testing, impact assessment, sign-off |
| **Deployment** | Are controls in place for access, logging, observability, and change management? | Audit logs, permissions, rollout gates, version control |
| **Post-launch monitoring** | How will drift, incidents, complaints, and external changes be handled? | Ongoing evaluations, incident playbooks, periodic review |
| **Retirement** | How will the system be decommissioned, archived, or replaced safely? | Decommission plan, record retention, dependency removal |

Two practical lessons follow from this mapping:

1. Governance is most effective when embedded into existing product and engineering gates rather than added as a parallel bureaucracy.
2. Governance should be strongest at transition points: procurement, launch approval, major model changes, new tool connections, and retirement.

---

## 8. Generative and Agentic AI Governance

### 8.1 Why Generative AI Is Harder to Govern

Generative AI systems complicate governance because they are:

- highly general-purpose,
- difficult to evaluate exhaustively,
- capable of producing novel outputs,
- often dependent on opaque upstream training practices,
- and increasingly integrated with search, tools, enterprise data, and external APIs.

This changes governance in at least four ways:

1. **Capability boundaries are less stable.** The same model can behave very differently depending on prompts, system instructions, retrieval context, and tool access.
2. **Evaluation must become continuous.** Static pre-launch testing is not enough.
3. **Copyright and data provenance become first-order concerns.**
4. **System governance matters more than model governance.** Product behavior depends on orchestration, not just on the base model.

### 8.2 Agentic AI Raises the Accountability Bar

Agentic systems introduce additional governance challenges because they can:

- plan over multiple steps,
- choose tools,
- take actions in external environments,
- store and reuse memory,
- and trigger consequential outcomes without a human reviewing every intermediate step.

As a result, governance must expand from output quality to action control.

Important controls for agentic systems include:

- scoped permissions for tools and data,
- approval thresholds for consequential actions,
- full trajectory logging, not just final outputs,
- evaluation of planning behavior and recovery behavior,
- time, budget, and action limits,
- kill switches and fallback modes,
- and strong separation between testing and production environments.

### 8.3 Governance Needs to Be Adaptive

Recent governance scholarship argues that generative AI requires an **adaptive** rather than static governance model. Taeihagh (2025) emphasizes the need for iterative governance, sandboxes, and approaches that do not become obsolete as model capabilities change. The same literature also warns that **self-regulation alone is insufficient**, even if industry codes of conduct remain useful complements to formal regulation.

This is one of the central governance lessons of 2022-2026: for generative and agentic AI, fixed checklists are not enough. Governance must be revisited as systems, interfaces, and uses evolve.

---

## 9. Implications for Product Teams

### 9.1 Governance Shapes Product Strategy

AI governance affects product scope, sequencing, and business model choices. Teams may avoid certain use cases entirely, ship lower-autonomy versions first, or prioritize human-review workflows to reduce risk and compliance burden.

### 9.2 Documentation Is a Product Artifact

Model cards, system cards, risk logs, impact assessments, and monitoring plans are not peripheral paperwork. They are part of the product package needed to launch and maintain AI systems responsibly.

### 9.3 Procurement Is Governance

Many organizations now assemble AI products through vendors and APIs rather than internal model development. Governance therefore depends heavily on contract terms, data rights, portability, auditability, and the ability to switch suppliers without losing critical capabilities.

### 9.4 Product Governance Must Continue After Launch

Because AI behavior can drift or change through model updates, retrieval changes, prompt changes, and user adaptation, post-launch monitoring is essential. Governance maturity depends on feedback loops, not just launch reviews.

### 9.5 UX and Governance Are Tightly Coupled

Human oversight, contestability, user disclosure, and safe fallback behavior are partly user-experience design problems. Governance therefore has to be co-designed with product design, not handled only by legal or policy teams.

---

## 10. Research Gaps and Open Questions

Despite rapid progress, major gaps remain.

### 10.1 Measuring Governance Effectiveness

There is still limited empirical evidence showing which governance structures actually reduce harms, improve trust, or enable better product outcomes. Many frameworks define what should exist, but few rigorously measure whether the controls work.

### 10.2 Governance for Small and Mid-Sized Teams

Most mature governance guidance assumes large organizations with legal, risk, compliance, and platform teams. Research on lightweight governance models for startups and mid-market firms remains thin.

### 10.3 Agent Accountability

The governance literature is still behind the capabilities of agentic systems. Open questions include:

- how to assign accountability across multi-agent workflows,
- how to audit action chains,
- how to define meaningful human oversight when autonomy is high,
- and how to govern memory and tool-use policies.

### 10.4 Cross-Jurisdiction Interoperability

Firms operating globally need governance systems that map across OECD, NIST, ISO, EU, UNESCO, and sector-specific rules. More work is needed on practical crosswalks and interoperable evidence models.

### 10.5 Participatory and Democratic Governance

Much governance remains expert-led and top-down. Rights-based frameworks increasingly emphasize stakeholder participation, but effective and scalable participatory methods are still underdeveloped.

### 10.6 Data Governance, Copyright, and Provenance

Generative AI has made data lineage, licensing, and intellectual property governance much more consequential. Research is still catching up on how to operationalize these concerns in fast-moving product environments.

---

## 11. Notable Papers and Sources

### Academic and Scholarly Sources

1. Batool, A., Zowghi, D., & Bano, M. (2025). **AI governance: a systematic literature review.** *AI and Ethics*, 5, 3265-3279. DOI: https://doi.org/10.1007/s43681-024-00653-w
2. Papagiannidis, E., Mikalef, P., & Conboy, K. (2025). **Responsible artificial intelligence governance: A review and research framework.** *Journal of Strategic Information Systems*, 34(2), 101885. DOI: https://doi.org/10.1016/j.jsis.2024.101885
3. Taeihagh, A. (2025). **Governance of Generative AI.** *Policy and Society*, 44(1), 1-22. DOI: https://doi.org/10.1093/polsoc/puaf001
4. Janssen, M. (2025). **Responsible governance of generative AI: conceptualizing GenAI as complex adaptive systems.** *Policy and Society*, 44(1), 38-51. DOI: https://doi.org/10.1093/polsoc/puae040

### International Policy and Governance Frameworks

5. OECD. **OECD updates AI Principles to stay abreast of rapid technological developments.** 3 May 2024. URL: https://www.oecd.org/en/about/news/press-releases/2024/05/oecd-updates-ai-principles-to-stay-abreast-of-rapid-technological-developments.html
6. OECD. **OECD launches global framework to monitor application of G7 Hiroshima AI Code of Conduct.** 7 February 2025. URL: https://www.oecd.org/en/about/news/press-releases/2025/02/oecd-launches-global-framework-to-monitor-application-of-g7-hiroshima-ai-code-of-conduct.html
7. UNESCO. **Ethics of Artificial Intelligence / Recommendation on the Ethics of AI.** URL: https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
8. Council of Europe. **Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law.** URL: https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence
9. Council of Europe. **HUDERIA - risk and impact assessment of AI systems.** URL: https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems

### Regulation, Standards, and Operational Guidance

10. European Commission. **AI Act.** URL: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
11. European Commission. **Navigating the AI Act.** URL: https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act
12. EUR-Lex. **Regulation (EU) 2024/1689.** URL: https://eur-lex.europa.eu/eli/reg/2024/1689/
13. European Commission. **Guidelines for providers of general-purpose AI models.** URL: https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers
14. NIST. **Artificial Intelligence Risk Management Framework (AI RMF 1.0).** 26 January 2023. DOI: https://doi.org/10.6028/NIST.AI.100-1
15. NIST. **AI RMF Playbook.** URL: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
16. NIST. **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.** 26 July 2024. DOI: https://doi.org/10.6028/NIST.AI.600-1
17. NIST AI Resource Center. URL: https://airc.nist.gov/
18. The White House / OMB. **M-25-21: Accelerating Federal Use of AI through Innovation, Governance, and Public Trust.** URL: https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
19. The White House / OMB. **M-25-22: Driving Efficient Acquisition of Artificial Intelligence in Government.** URL: https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf
20. The White House. **Removing Barriers to American Leadership in Artificial Intelligence.** 23 January 2025. URL: https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/
21. ISO. **ISO/IEC 23894:2023 - AI - Guidance on risk management.** URL: https://www.iso.org/standard/77304.html
22. ISO. **ISO/IEC 42001:2023 - AI management systems.** URL: https://www.iso.org/standard/42001
23. ISO. **ISO/IEC 42005:2025 - AI system impact assessment.** URL: https://www.iso.org/standard/42005

---

## Bottom Line

The most important shift in AI governance between 2022 and 2026 is that governance became operational. The field is converging on a practical architecture built from inventories, risk-tiering, impact assessments, management systems, human oversight, procurement controls, and continuous monitoring. For product teams, the strategic challenge is no longer whether governance matters. It is how to build governance into the product lifecycle without turning it into dead process or late-stage compliance theater.
