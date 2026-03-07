# AI Frameworks & Taxonomies for Product: A Deep-Dive Analysis

> **Research Survey Section** | AI for Product Research Project
> **Date:** 2026-03-07
> **Scope:** Academic papers, institutional reports, and industry frameworks (2022--2026)
> **Status:** Draft for review

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [OECD Sectoral Taxonomy of AI Intensity](#2-oecd-sectoral-taxonomy-of-ai-intensity-2024)
3. [AI Agents vs. Agentic AI: Conceptual Taxonomy](#3-ai-agents-vs-agentic-ai-conceptual-taxonomy)
4. [AI Maturity Models for Product Organizations](#4-ai-maturity-models-for-product-organizations)
5. [Frameworks for Classifying AI Capabilities in Products](#5-frameworks-for-classifying-ai-capabilities-in-products)
6. [AI Readiness Assessment Frameworks](#6-ai-readiness-assessment-frameworks)
7. [Product-Market Fit Frameworks for AI Products](#7-product-market-fit-frameworks-for-ai-products)
8. [AI Integration Levels in Product Development](#8-ai-integration-levels-in-product-development)
9. [Stanford HAI AI Index Classification](#9-stanford-hai-ai-index-classification)
10. [Gartner AI Maturity Curve and Hype Cycle](#10-gartner-ai-maturity-curve-and-hype-cycle)
11. [Academic Taxonomies of AI in Product Management](#11-academic-taxonomies-of-ai-in-product-management)
12. [Synthesis: Cross-Framework Comparison](#12-synthesis-cross-framework-comparison)
13. [Limitations & Open Questions](#13-limitations--open-questions)
14. [References](#14-references)

---

## 1. Executive Summary

The proliferation of AI across product development, management, and strategy has generated a growing body of frameworks and taxonomies aimed at classifying, measuring, and guiding AI adoption. This analysis surveys the major classification systems proposed between 2022 and 2026, spanning institutional frameworks (OECD, Stanford HAI, Gartner), academic taxonomies (agentic AI distinctions, AI-in-NPD mappings), and practitioner models (maturity curves, readiness assessments, product-market fit adaptations for AI).

**Key findings include:**

- There is no single, universally accepted taxonomy for AI in product contexts; instead, frameworks tend to address specific slices of the problem -- sectoral intensity, organizational maturity, capability classification, or integration depth.
- The OECD (2024) introduced the first large-scale empirical taxonomy measuring AI intensity at the sector level, using complementarity between AI exposure and productivity gains.
- The distinction between "AI Agents" and "Agentic AI" has crystallized as a critical conceptual taxonomy for product teams building autonomous systems (2025).
- AI maturity models have converged toward five- or six-stage progressions, but empirical validation remains sparse.
- Product-market fit for AI products requires fundamentally different frameworks than traditional software, due to data dependency, performance variability, and trust requirements.
- The Stanford HAI AI Index (annually since 2018, latest 2025) provides the most comprehensive longitudinal benchmarking of AI capabilities, but is not product-specific.
- Gartner's Hype Cycle for AI remains the most widely cited industry positioning tool, though criticized for lack of methodological transparency.

---

## 2. OECD Sectoral Taxonomy of AI Intensity (2024)

### 2.1 Overview

The Organisation for Economic Co-operation and Development (OECD) published "A Sectoral Taxonomy of AI Intensity" in December 2024 as part of its ongoing AI Policy Observatory work. This represents one of the first large-scale, empirically grounded attempts to classify economic sectors by their degree of AI adoption and the productivity implications thereof.

**Full citation:**
- OECD (2024). "A Sectoral Taxonomy of AI Intensity." OECD Artificial Intelligence Papers, No. 21. Paris: OECD Publishing.
- URL: https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/a-sectoral-taxonomy-of-ai-intensity_c2baae71/1f6377b5-en.pdf

### 2.2 Methodology

The OECD taxonomy employs a **complementarity-based measure** of AI intensity, distinguishing it from simpler exposure-based indices. The approach involves:

1. **AI Exposure Measurement:** Quantifying the extent to which occupations within a sector are exposed to AI capabilities (drawing on prior OECD work on AI and the labor market, notably Felten et al.'s AI Occupational Exposure measure).
2. **Productivity Complementarity:** Measuring the degree to which AI exposure translates into measurable productivity gains, rather than mere task substitution.
3. **Sectoral Aggregation:** Mapping occupation-level data to ISIC (International Standard Industrial Classification) sectors to produce sector-level AI intensity scores.

The key innovation is the **complementarity condition**: a sector is classified as "AI-intensive" not merely because its workers are exposed to AI, but because that exposure is associated with productivity improvements. This avoids the problem of over-counting sectors where AI is present but not yet productive.

### 2.3 Key Findings

- Sectors with the highest AI intensity include information and communication technology (ICT), professional and scientific services, and financial services.
- Manufacturing shows moderate AI intensity, driven primarily by advanced manufacturing sub-sectors (automotive, aerospace, semiconductor fabrication).
- Agriculture, construction, and extractive industries show lower AI intensity, despite growing exposure, because complementarity gains have not yet materialized at scale.
- The taxonomy reveals a **"complementarity gap"**: many sectors have high AI exposure but low productivity complementarity, suggesting that exposure alone is an insufficient measure of AI transformation.

### 2.4 Relevance to Product

For product organizations, the OECD taxonomy offers:
- A **benchmarking framework** for understanding how AI-intensive a given industry context is, which informs product strategy decisions (e.g., where AI features will be most valued).
- An evidence-based counter to hype: high AI exposure does not automatically imply productive AI integration.
- A basis for **sectoral AI product positioning**: products targeting high-complementarity sectors can emphasize productivity gains, while those targeting low-complementarity sectors must address adoption barriers.

### 2.5 Limitations

- The taxonomy operates at the sector level and does not provide firm-level or product-level granularity.
- Data availability varies significantly across OECD member countries, limiting cross-national comparability.
- The framework is backward-looking (based on observed productivity data) and may not capture emerging AI applications.

---

## 3. AI Agents vs. Agentic AI: Conceptual Taxonomy

### 3.1 Overview

As autonomous AI systems have become central to product roadmaps, a conceptual confusion has emerged between "AI Agents" and "Agentic AI." A 2025 paper on arXiv introduced a structured taxonomy to resolve this ambiguity.

**Full citation:**
- "AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications, and Challenges" (2025). arXiv.
- URL: https://arxiv.org/html/2505.10468v4

### 3.2 The Taxonomy

The paper distinguishes between:

| Concept | Definition | Characteristics |
|---------|-----------|-----------------|
| **AI Agent** | A discrete software entity that perceives its environment, reasons about goals, and takes autonomous actions. | Bounded scope; single-task or narrow-domain; operates within defined tool and API boundaries; typically stateless or short-context. |
| **Agentic AI** | A system-level property describing AI architectures that exhibit agency -- planning, multi-step reasoning, tool use, memory, and self-correction -- across complex workflows. | Emergent from orchestration of multiple components; may involve multiple AI agents; exhibits goal persistence, adaptive planning, and delegation. |

### 3.3 Key Dimensions of Distinction

The taxonomy identifies several axes along which AI Agents and Agentic AI differ:

1. **Autonomy Spectrum:** AI Agents execute within predefined action spaces; Agentic AI systems dynamically expand their action space through tool discovery and sub-goal generation.
2. **Architecture:** AI Agents are typically monolithic (single model + tool interface); Agentic AI involves orchestrated multi-agent systems, often with a planner/executor/evaluator architecture.
3. **Memory and State:** AI Agents may be stateless; Agentic AI requires persistent memory (short-term working memory, long-term knowledge stores, episodic memory of past actions).
4. **Human-in-the-Loop:** AI Agents often operate with implicit human oversight; Agentic AI systems must have explicit escalation and oversight mechanisms due to their broader autonomy.

### 3.4 Relevance to Product

This taxonomy has direct implications for product teams:

- **Product Design:** Understanding whether a feature requires an AI Agent (bounded, predictable) or an Agentic AI system (open-ended, adaptive) fundamentally changes the UX design, error handling, and trust model.
- **Product Management Tooling:** The analysis of 51 AI-powered PM tools (see aipmtools.org) found that agentic capabilities are the least mature dimension, with only approximately 25% exhibiting meaningful agentic behavior.
- **Market Positioning:** Products positioning as "agentic" must distinguish between single-agent task automation and true multi-step, goal-persistent workflows.

### 3.5 Related Work

- Gartner (2025) predicts that 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025. Source: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Deloitte (2026). "Agentic AI Strategy: From Pilot to Production." Source: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
- The AI agent market is projected to grow from $7.84B (2025) to $52.62B (2030), with a CAGR of 46.3%.

---

## 4. AI Maturity Models for Product Organizations

### 4.1 Overview

AI maturity models provide staged frameworks for assessing how advanced an organization is in its AI adoption journey. Multiple models have been proposed by consulting firms, research institutions, and academic researchers. Most converge on a five- to six-stage progression from ad hoc experimentation to organization-wide AI-native operations.

### 4.2 Major Models

#### 4.2.1 Gartner AI Maturity Model (2023-2025)

Gartner's model defines five levels of AI maturity:

| Level | Name | Description |
|-------|------|-------------|
| 1 | **Awareness** | Organization recognizes AI potential; no active projects. |
| 2 | **Active** | Proof-of-concept and pilot projects underway; limited production deployment. |
| 3 | **Operational** | AI is deployed in production for specific use cases; governance emerging. |
| 4 | **Systemic** | AI is integrated across multiple business functions; centralized AI platform and governance. |
| 5 | **Transformational** | AI is core to business strategy; continuous learning and adaptation; AI-native culture. |

**Source:** Gartner, "AI Maturity Model" (updated annually in Gartner IT Score reports).

#### 4.2.2 McKinsey AI Maturity Framework (2024-2025)

McKinsey's "State of AI" annual survey (most recently 2025) implicitly defines maturity tiers based on organizational capabilities:

- **Experimenters:** Using AI in one or two functions; typically GenAI chatbots or productivity tools.
- **Scalers:** AI deployed across three or more functions with measurable business impact.
- **Transformers:** AI embedded in core business processes; significant revenue or cost impact attributable to AI.

The 2025 survey found that 78% of organizations reported using AI in at least one business function (up from 55% in 2023), but only a small fraction qualify as "transformers."

**Source:** McKinsey & Company (2025). "The State of AI." https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

#### 4.2.3 Microsoft/BCG AI Maturity Model (2024)

A joint research effort between Microsoft and BCG produced a four-quadrant model mapping AI maturity across two dimensions:

1. **Technical Maturity:** Infrastructure, data readiness, model deployment capabilities.
2. **Organizational Maturity:** Skills, governance, change management, leadership commitment.

Organizations fall into quadrants: **Nascent** (low-low), **Technical-Led** (high-tech, low-org), **Strategy-Led** (low-tech, high-org), or **AI-Native** (high-high).

#### 4.2.4 Academic Models

- **Alsheibani, Cheung, and Messom (2020).** "Artificial Intelligence Adoption: AI-readiness at Firm-Level." PACIS 2020 Proceedings, 37. This paper proposed a firm-level AI readiness model drawing on technology-organization-environment (TOE) theory.
  - URL: https://aisel.aisnet.org/pacis2020/37/

- **Pumplun, Taez, and Buxmann (2021).** "A New Organizational Chassis for Artificial Intelligence: Exploring Organizational Readiness Factors." ECIS 2021.
  - Identifies organizational readiness as multidimensional: technology infrastructure, data management, talent and skills, organizational culture, and strategic alignment.

### 4.3 Relevance to Product

For product organizations specifically, AI maturity models help:
- **Prioritize AI feature development:** Organizations at Level 1-2 benefit most from assistive AI (copilots, recommendations); those at Level 4-5 can pursue agentic and autonomous AI features.
- **Sequence AI product roadmaps:** Maturity models inform a crawl-walk-run approach to AI feature rollout.
- **Benchmark against peers:** Especially relevant for B2B product teams selling AI capabilities to enterprise customers at varying maturity levels.

### 4.4 Limitations

- Most maturity models are proposed by consulting firms and lack rigorous empirical validation.
- Stage progression is often presented as linear, but real-world AI adoption is frequently non-linear, with organizations regressing or leapfrogging stages.
- Product-specific maturity models (as opposed to enterprise-wide models) are notably absent from the literature.

---

## 5. Frameworks for Classifying AI Capabilities in Products

### 5.1 The AI Capability Spectrum

Multiple frameworks attempt to classify the types of AI capabilities that can be embedded in products. A useful synthesis identifies four capability tiers:

| Tier | Capability | Examples | Complexity |
|------|-----------|----------|------------|
| 1 | **Descriptive/Analytical AI** | Dashboards, anomaly detection, pattern recognition | Low |
| 2 | **Predictive AI** | Demand forecasting, churn prediction, recommendation engines | Medium |
| 3 | **Generative AI** | Content generation, code synthesis, design generation, conversational interfaces | Medium-High |
| 4 | **Autonomous/Agentic AI** | Self-driving workflows, autonomous decision-making, multi-step task completion | High |

### 5.2 The "AI for Innovation" Diagram

A systematic review of 53 peer-reviewed articles and 218 AI models (2022-2024) introduced the "AI for Innovation" conceptual framework, aligning AI capabilities with innovation phases in new product development (NPD).

**Source:** "AI and New Product Development" (2024). ResearchGate. https://www.researchgate.net/publication/377460646

Key mappings:
- **Ideation phase:** NLP-based sentiment analysis, knowledge extraction from patents and literature, LLM-based brainstorming.
- **Development phase:** Generative design, simulation-based optimization, automated testing.
- **Launch phase:** Demand forecasting, pricing optimization, recommendation systems.
- **Post-launch:** Customer feedback analysis, churn prediction, adaptive personalization.

### 5.3 Springer NPD-AI Mapping (2025)

The most comprehensive academic mapping of AI methods to NPD phases comes from a systematic literature review of 190 publications plus expert interviews.

**Full citation:**
- "Where Does AI Play a Major Role in NPD and Product Management?" Management Review Quarterly, Springer, 2025.
- URL: https://link.springer.com/article/10.1007/s11301-025-00533-5

Key findings:
- Sentiment analysis, knowledge extraction, and demand forecasting dominate the early (discovery and design) phases.
- The later stages -- concept testing, validation, and post-launch optimization -- are **significantly under-researched** with respect to AI application.
- No existing framework spans the full NPD lifecycle with integrated AI support.

### 5.4 Three-Part Product AI Distinction

A useful conceptual distinction that has emerged in both academic and practitioner discourse:

| Term | Definition | Example |
|------|-----------|---------|
| **AI for Product** | Using AI to improve how products are built, managed, and optimized. | AI-assisted user research, AI-powered prioritization, automated testing. |
| **AI Product** | A product whose core value proposition is powered by AI. | ChatGPT, Midjourney, GitHub Copilot. |
| **Product AI** | AI features embedded within an existing non-AI product. | Spotify's recommendation engine, Gmail's Smart Compose. |

This distinction matters for frameworks because each category has different success criteria, development methodologies, and evaluation metrics.

---

## 6. AI Readiness Assessment Frameworks

### 6.1 Overview

AI readiness frameworks assess whether an organization (or product team) has the prerequisites to successfully adopt AI. They typically evaluate multiple dimensions: data infrastructure, talent, governance, strategy, and culture.

### 6.2 Major Frameworks

#### 6.2.1 OECD AI Readiness (2023-2024)

The OECD AI Policy Observatory has developed country-level AI readiness indicators organized around:
- **Government AI readiness:** Policy frameworks, public sector AI adoption, digital infrastructure.
- **Technology sector readiness:** Research output, startup ecosystem, venture capital.
- **Data ecosystem readiness:** Data availability, quality, interoperability, and governance.

While designed for national policy, these dimensions map to organizational readiness when adapted for firm-level assessment.

**Source:** OECD AI Policy Observatory. https://oecd.ai/

#### 6.2.2 Oxford Insights Government AI Readiness Index (2023-2024)

Published annually, this index ranks governments on AI readiness across three pillars:
1. **Government:** Vision, governance and ethics, digital capacity, adaptability.
2. **Technology Sector:** Innovation capability, technology infrastructure, data representativeness.
3. **Data and Infrastructure:** Data availability, quality, and infrastructure maturity.

**Source:** Oxford Insights. "Government AI Readiness Index 2024." https://oxfordinsights.com/ai-readiness/ai-readiness-index/

#### 6.2.3 Firm-Level AI Readiness (Academic)

- **Jockel, Grimm, and Coners (2022).** "AI Readiness: A Systematic Literature Review." Proceedings of the European Conference on Information Systems (ECIS).
  - Identifies six readiness dimensions: strategy, organization, data, technology, people, and governance.
  - Synthesizes 23 prior AI readiness models.

- **Alsheibani, Cheung, and Messom (2020).** "Artificial Intelligence Adoption: AI-readiness at Firm-Level." PACIS 2020.
  - Applies TOE (Technology-Organization-Environment) theory to AI readiness.
  - URL: https://aisel.aisnet.org/pacis2020/37/

### 6.3 Product-Specific Readiness

Product teams can adapt AI readiness frameworks by evaluating:

1. **Data Readiness:** Does the product generate sufficient, high-quality data to train/fine-tune AI models? Is there a data pipeline?
2. **Technical Readiness:** Does the engineering team have ML infrastructure (model serving, monitoring, A/B testing for AI features)?
3. **User Readiness:** Are users prepared for AI-powered features? Is there trust? Do they understand AI limitations?
4. **Organizational Readiness:** Does the product team include data scientists, ML engineers, or AI product managers? Is there cross-functional alignment?
5. **Ethical Readiness:** Are there frameworks for responsible AI deployment, bias testing, and transparency?

### 6.4 Limitations

- Most AI readiness frameworks are designed for enterprise-wide assessment and do not translate directly to product-level readiness.
- Self-assessment bias: organizations tend to overestimate their readiness.
- Readiness is necessary but not sufficient: many "AI-ready" organizations still fail at AI product execution due to unclear use cases or poor problem framing.

---

## 7. Product-Market Fit Frameworks for AI Products

### 7.1 The Challenge

Traditional product-market fit (PMF) frameworks (e.g., Sean Ellis's 40% test, Superhuman's PMF engine) assume deterministic product behavior: the product works the same way every time. AI products violate this assumption because:

- **Performance is probabilistic:** AI features have accuracy distributions, not binary success/failure.
- **Data dependency:** Product quality depends on data quality, volume, and freshness.
- **Expectation calibration:** Users must learn to trust (but not over-trust) AI outputs.
- **Cold start problem:** AI features may underperform initially and improve with usage data.

### 7.2 Emerging Frameworks

#### 7.2.1 The AI-PMF Stack (Practitioner Framework, 2023-2025)

Emerging from the AI startup ecosystem (notably articulated by practitioners at a]16z, Sequoia, and Greylock), the AI-PMF stack adds layers to traditional PMF:

1. **Model-Market Fit:** Does a model exist (or can one be built) that delivers the required accuracy for the target use case?
2. **Data-Market Fit:** Does the target market generate sufficient data to train, fine-tune, and maintain the AI system?
3. **UX-Market Fit:** Can the AI's capabilities be wrapped in a user experience that manages expectations, handles errors gracefully, and builds trust?
4. **Business-Market Fit:** Is the unit economics of AI inference (compute cost, latency, accuracy trade-offs) viable at scale?

#### 7.2.2 The "AI Product Wedge" (2024)

Coined in venture capital and product strategy discourse, this framework suggests AI products should enter markets through a narrow, high-confidence "wedge" use case where AI demonstrably outperforms alternatives, then expand outward:

- **Wedge phase:** Narrow use case; deterministic-like accuracy; high user trust.
- **Expansion phase:** Broaden to adjacent use cases; tolerate lower accuracy; invest in user education.
- **Platform phase:** AI becomes horizontal infrastructure; ecosystem effects.

#### 7.2.3 Grammarly as Case Study

Grammarly (30M DAU, ~$400M ARR) exemplifies the AI product wedge approach:
- **Wedge:** Grammar and spelling correction (high confidence, deterministic-like).
- **Expansion:** Tone detection, clarity suggestions (probabilistic, requires user judgment).
- **Platform:** Full writing intelligence platform with GenAI capabilities (2023-2025).

### 7.3 Limitations

- AI-PMF frameworks remain largely practitioner-driven; academic research on PMF for AI products is sparse.
- Existing frameworks do not adequately address the "trust ramp": how users progressively build confidence in AI capabilities over time.
- Multi-modal and agentic AI products require new PMF frameworks that account for compound error rates across multi-step workflows.

---

## 8. AI Integration Levels in Product Development

### 8.1 A Taxonomy of Integration Depth

Drawing on both academic literature and practitioner models, AI integration in product development can be classified into five levels:

| Level | Name | Description | Product Example |
|-------|------|-------------|-----------------|
| 0 | **No AI** | Traditional product development without AI. | Manual user research, rule-based features. |
| 1 | **AI-Assisted** | AI provides suggestions that humans review and act upon. | AI-generated code suggestions (Copilot), AI-summarized user feedback. |
| 2 | **AI-Augmented** | AI automates sub-tasks within human-directed workflows. | Automated A/B test analysis, AI-driven bug triage. |
| 3 | **AI-Driven** | AI makes decisions within defined boundaries; humans provide oversight. | AI-optimized pricing, automated content moderation with human appeal. |
| 4 | **AI-Native** | Product is fundamentally built around AI capabilities; AI is not a feature but the core. | ChatGPT, autonomous vehicles, AI drug discovery. |
| 5 | **AI-Autonomous** | AI operates independently with minimal human intervention; self-improving. | Fully autonomous trading systems, self-healing infrastructure. |

### 8.2 MIT Sloan Perspective

MIT Sloan Management Review (2024-2025) has highlighted that most organizations are currently at Level 1-2, with GenAI accelerating the transition to Level 2-3. The critical challenge is moving from Level 2 (augmentation) to Level 3 (AI-driven), which requires:
- Robust AI governance frameworks
- Clear accountability models for AI decisions
- User trust and transparency mechanisms

**Source:** MIT Sloan Management Review. "When Generative AI Meets Product Development." https://sloanreview.mit.edu/article/when-generative-ai-meets-product-development/

### 8.3 The Copilot-to-Autopilot Transition

A widely discussed trajectory in 2024-2026 product strategy discourse:

1. **Copilot era (2022-2025):** AI assists human work -- suggests, drafts, summarizes. The human retains full decision authority.
2. **Agent era (2025-2027):** AI executes multi-step tasks with human oversight at checkpoints. The human defines goals and reviews outcomes.
3. **Autopilot era (2027+):** AI manages workflows end-to-end with exception-based human involvement. The human sets strategy and handles edge cases.

This trajectory is reflected in Gartner's prediction that 15% of daily work decisions will be made by agentic AI by 2028.

---

## 9. Stanford HAI AI Index Classification

### 9.1 Overview

The Stanford Institute for Human-Centered Artificial Intelligence (HAI) publishes the annual **AI Index Report**, providing the most comprehensive longitudinal dataset on AI progress. The 2025 report (8th edition) is the latest available.

**Full citation:**
- Stanford HAI (2025). "Artificial Intelligence Index Report 2025." Stanford University.
- URL: https://hai.stanford.edu/ai-index/2025-ai-index-report

### 9.2 Classification System

The AI Index organizes its analysis across several chapters, each representing a classification dimension:

1. **Research and Development:** Publication volume, citation patterns, open-source model releases, benchmark performance.
2. **Technical Performance:** Standardized benchmarks across computer vision, NLP, reasoning, multimodal tasks, code generation.
3. **Responsible AI:** Metrics on bias, fairness, safety, and alignment research.
4. **Economy and Labor:** AI's impact on jobs, wages, productivity, and investment.
5. **Science and Medicine:** AI applications in scientific discovery, drug development, and healthcare.
6. **Education:** AI in teaching, learning, and academic research.
7. **Policy and Governance:** AI regulation, national strategies, and institutional frameworks.
8. **Diversity, Equity, and Inclusion:** Representation in AI research and industry.
9. **Public Opinion:** Surveys of public attitudes toward AI.

### 9.3 Key 2025 Findings Relevant to Product

- AI models now match or exceed human performance on several benchmarks previously considered out of reach (e.g., complex reasoning, graduate-level science).
- The cost of training frontier models has increased exponentially, raising barriers to entry for AI product companies.
- Open-source model releases have surged, democratizing AI capability but creating new challenges for product differentiation.
- Investment in generative AI companies reached record levels in 2024, with a significant portion directed toward AI-native products.
- Responsible AI research is growing but remains a small fraction of overall AI research output.

### 9.4 Relevance to Product Frameworks

The Stanford HAI AI Index does not provide a product-specific taxonomy, but its classification system is valuable for:
- **Capability benchmarking:** Product teams can track which AI capabilities are mature enough for production use.
- **Market timing:** The technical performance data helps product managers assess when specific AI capabilities cross the "good enough" threshold for their use case.
- **Policy awareness:** The governance chapter informs product compliance requirements (e.g., EU AI Act, US Executive Order on AI).

### 9.5 Limitations

- The AI Index is a measurement and tracking framework, not a prescriptive taxonomy.
- It is not product-specific; product teams must interpret the data through their own domain lens.
- The report is published annually, which means it may lag behind rapidly evolving AI capabilities by six to twelve months.

---

## 10. Gartner AI Maturity Curve and Hype Cycle

### 10.1 Overview

Gartner's **Hype Cycle for Artificial Intelligence** is the most widely cited industry positioning tool for AI technologies. Published annually, it maps AI technologies and concepts along the well-known Hype Cycle curve: Innovation Trigger, Peak of Inflated Expectations, Trough of Disillusionment, Slope of Enlightenment, and Plateau of Productivity.

### 10.2 Recent Hype Cycle Positioning (2024-2025)

Based on Gartner's 2024 and 2025 Hype Cycle publications:

| Technology | Position (2024-2025) | Time to Plateau |
|-----------|---------------------|-----------------|
| **Generative AI** | Sliding from Peak toward Trough | 2-5 years |
| **AI Agents / Agentic AI** | Approaching Peak of Inflated Expectations | 5-10 years |
| **Foundation Models** | At or near Peak | 2-5 years |
| **AI Engineering** | Slope of Enlightenment | 2-5 years |
| **Responsible AI** | Slope of Enlightenment | 2-5 years |
| **Composite AI** | Trough of Disillusionment | 2-5 years |
| **AI-Augmented Software Engineering** | Innovation Trigger to Peak | 2-5 years |
| **Digital Twins** | Slope of Enlightenment | 5-10 years |
| **Autonomous Systems** | Innovation Trigger | >10 years |

### 10.3 Gartner's AI Maturity Model

Separate from the Hype Cycle, Gartner maintains an **AI Maturity Model** (part of the broader "IT Score for AI" toolkit) with five levels (see Section 4.2.1 above). The model is used prescriptively: organizations are assessed on their current level and given a roadmap for advancement.

### 10.4 Key Gartner Predictions (2025-2028)

- By end of 2026, 40% of enterprise applications will feature task-specific AI agents (up from <5% in 2025).
- By 2028, 15% of daily work decisions will be made autonomously by agentic AI.
- By 2028, 33% of enterprise software applications will include agentic AI, up from <1% in 2024.
- By 2027, Gartner predicts that 70% of AI projects will fail to deliver expected value, largely due to organizational -- not technical -- factors.

### 10.5 Relevance to Product

The Hype Cycle is particularly useful for product managers because:
- It provides a shared vocabulary for positioning AI features relative to market expectations.
- It helps manage stakeholder expectations ("this technology is at the Peak of Inflated Expectations; expect a correction").
- It informs competitive strategy: entering the Trough of Disillusionment can be a strategic advantage for well-funded, patient companies.

### 10.6 Limitations

- The Hype Cycle methodology is proprietary and not transparent; positioning is based on Gartner analyst judgment rather than quantitative data.
- Technologies can "skip" stages or remain indefinitely at one position, undermining the model's predictive value.
- The framework does not distinguish between different application domains (e.g., GenAI for marketing vs. GenAI for drug discovery may have very different maturity profiles).
- Academic criticism (e.g., Steinert and Leifer, 2010) has noted that the Hype Cycle conflates market expectations with technical maturity, creating an ambiguous signal.

---

## 11. Academic Taxonomies of AI in Product Management

### 11.1 Systematic Literature Reviews

Two major systematic reviews provide academic taxonomies of AI in product management and new product development:

#### 11.1.1 Springer Management Review Quarterly (2025)

**Full citation:** "Where Does AI Play a Major Role in NPD and Product Management?" Management Review Quarterly, Springer, 2025.
- URL: https://link.springer.com/article/10.1007/s11301-025-00533-5

This review of 190 publications maps AI methods to NPD phases, creating a **method-phase matrix**:

| NPD Phase | Dominant AI Methods | Research Volume |
|-----------|-------------------|-----------------|
| Opportunity identification | NLP, sentiment analysis, trend detection | High |
| Concept development | Generative models, knowledge extraction | Medium |
| Design & prototyping | Computer vision, generative design, simulation | Medium |
| Testing & validation | Predictive analytics, automated testing | **Low** |
| Launch & commercialization | Demand forecasting, pricing optimization | Medium |
| Post-launch management | Recommendation systems, churn prediction | **Low** |

The key taxonomic finding is the **imbalance**: early-phase AI applications (discovery, ideation) are heavily researched, while later-phase applications (testing, post-launch) are significantly under-studied.

#### 11.1.2 ResearchGate NPD-AI Review (2024)

**Full citation:** "AI and New Product Development." ResearchGate, 2024. 53 peer-reviewed articles, 218 AI models analyzed.
- URL: https://www.researchgate.net/publication/377460646

This review introduces the **"AI for Innovation" diagram**, a conceptual framework with three layers:
1. **AI Methods Layer:** The specific AI techniques (NLP, computer vision, reinforcement learning, generative models, etc.)
2. **Innovation Activities Layer:** The NPD activities where AI is applied (ideation, prototyping, testing, launch, optimization)
3. **Outcome Layer:** The measurable impacts (time-to-market reduction, cost savings, quality improvement, customer satisfaction)

### 11.2 AI in Product Management Tooling

An empirical analysis of 51 AI-powered product management tools provides a capabilities-based taxonomy:

**Source:** https://aipmtools.org/articles/future-of-ai-product-management

| Capability Category | Description | Maturity |
|--------------------|-------------|----------|
| **Data Analysis & Insights** | AI-powered analytics, feedback synthesis, trend detection | Moderate-High |
| **Content Generation** | PRD drafting, release notes, documentation | High |
| **Prioritization & Roadmapping** | AI-assisted backlog scoring, roadmap optimization | Moderate |
| **User Research Automation** | Synthetic users, interview analysis, persona generation | Moderate |
| **Agentic Capabilities** | Autonomous multi-step workflow execution, self-directed task completion | **Low** |

The finding that agentic capabilities are the least mature dimension is consistent with the broader Agent/Agentic AI taxonomy discussed in Section 3.

### 11.3 Academic Frameworks for AI-Augmented Decision Making

Several academic papers have proposed taxonomies for how AI augments product management decision-making:

- **Brynjolfsson and McAfee (2017).** "The Business of Artificial Intelligence." Harvard Business Review. While pre-dating the survey period, this foundational work introduced the distinction between AI as **prediction machines** and humans as **judgment providers**, creating a taxonomy of decision tasks based on the prediction-judgment decomposition.

- **Agrawal, Gans, and Goldfarb (2018).** "Prediction Machines: The Simple Economics of Artificial Intelligence." Harvard Business Review Press. Extended the prediction-judgment framework into a practical decision-making taxonomy for product and business leaders.

- **"Enhancing Human-AI Collaboration and Trust in NPD from Organization Clustering Perspective"** (2025). ScienceDirect.
  - Proposes a multidimensional trust taxonomy for AI in NPD: technical/cognitive trust, emotional trust, and social trust.
  - URL: https://www.sciencedirect.com/science/article/abs/pii/S0360835225008435

- **"Complementarity in Human-AI Collaboration"** (2025). European Journal of Information Systems.
  - Introduces a taxonomy of complementarity types: task complementarity (AI handles some tasks, humans handle others), process complementarity (AI and humans collaborate on the same task), and outcome complementarity (combined output exceeds either alone).
  - Critically, finds that outcome complementarity **has rarely been observed empirically**.
  - URL: https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

---

## 12. Synthesis: Cross-Framework Comparison

### 12.1 Mapping Frameworks to Product Lifecycle Concerns

| Framework/Taxonomy | Primary Focus | Granularity | Empirical Basis | Product Relevance |
|-------------------|---------------|-------------|-----------------|-------------------|
| **OECD AI Intensity** | Sectoral AI adoption & productivity | Sector-level | Strong (labor data) | Indirect (market context) |
| **Agent vs. Agentic AI** | Architectural/conceptual distinction | System-level | Moderate (conceptual + examples) | Direct (product architecture) |
| **AI Maturity Models** | Organizational readiness stages | Org-level | Weak-Moderate (survey-based) | Moderate (roadmap sequencing) |
| **AI Capability Tiers** | Types of AI in products | Feature-level | Moderate (review-based) | Direct (feature planning) |
| **AI Readiness Frameworks** | Prerequisites for AI adoption | Org/team-level | Moderate (multi-dimensional) | Moderate (go/no-go decisions) |
| **AI-PMF Frameworks** | Market fit for AI products | Product-level | Weak (practitioner-driven) | Direct (product strategy) |
| **Integration Levels** | Depth of AI in product dev | Process-level | Weak (conceptual) | Direct (dev methodology) |
| **Stanford HAI AI Index** | Longitudinal AI capability tracking | Global/benchmark | Strong (quantitative benchmarks) | Indirect (capability timing) |
| **Gartner Hype Cycle** | Market expectations vs. maturity | Technology-level | Weak (analyst judgment) | Direct (positioning, expectation mgmt) |
| **NPD-AI Taxonomies** | AI methods mapped to NPD phases | Phase/method-level | Moderate-Strong (SLR-based) | Direct (R&D planning) |

### 12.2 Key Patterns Across Frameworks

1. **Convergent staging:** Whether framed as maturity levels, integration depths, or adoption stages, most frameworks converge on a roughly five-stage progression from no AI to fully autonomous AI.

2. **The agentic frontier:** Across all frameworks, autonomous/agentic AI is consistently identified as the least mature, most hyped, and most transformative category. The gap between current capabilities and expectations is largest here.

3. **The measurement problem:** Frameworks for measuring AI intensity, readiness, and maturity all struggle with the same fundamental challenge -- distinguishing between AI presence (exposure) and AI impact (productivity, quality, user value).

4. **The product-specificity gap:** Most frameworks are designed for enterprise-wide or sector-wide analysis. Product-specific frameworks (for individual products or product teams) are notably underdeveloped.

5. **Practitioner-academic divide:** The most actionable frameworks (AI-PMF, integration levels, maturity models) tend to come from practitioners and consulting firms with weak empirical grounding. The most rigorous work (OECD, Stanford HAI, academic SLRs) tends to be less actionable for product teams.

---

## 13. Limitations & Open Questions

### 13.1 Limitations of This Analysis

- **Web access constraints:** This analysis draws on the author's training knowledge and project-internal references. Real-time verification of URLs, retrieval of papers published after the knowledge cutoff, and discovery of very recent (2026) frameworks was limited.
- **Selection bias:** The frameworks surveyed reflect English-language, Western-centric (OECD, US, EU) perspectives. AI taxonomies from Chinese, Indian, or other research ecosystems may differ significantly.
- **Rapid evolution:** The AI frameworks landscape is changing faster than any single survey can capture. Frameworks that are current at time of writing may be superseded within months.

### 13.2 Open Research Questions

1. **Can a unified taxonomy of AI in product be developed?** No existing framework spans the full product lifecycle (discovery through growth) while also covering all dimensions (capability type, integration depth, organizational maturity, market fit). Is a unified framework feasible, or is the domain inherently multi-taxonomic?

2. **How should AI product quality be measured?** Traditional software quality metrics (uptime, latency, error rate) are necessary but insufficient for AI products. What additional metrics are needed (accuracy, fairness, calibration, user trust, explanation quality)?

3. **When does AI augmentation become AI dependence?** As products move from Level 1 (AI-assisted) to Level 4-5 (AI-native/autonomous), at what point does the organization lose the ability to function without AI? What are the risks?

4. **How do users develop mental models of AI product capabilities?** Frameworks classify AI capabilities from a technical perspective, but users' mental models of what AI can and cannot do are often misaligned. How should product frameworks incorporate the user's perspective?

5. **What is the right unit of analysis for AI taxonomies -- the firm, the product, the feature, or the use case?** Different frameworks operate at different granularities, and there is no consensus on which level is most useful.

6. **How should AI maturity models account for regression?** Organizations can lose AI capabilities (talent departure, data quality degradation, model drift). Existing maturity models assume monotonic progression.

7. **Is product-market fit for AI products fundamentally different from traditional PMF, or merely an extension?** The emerging AI-PMF frameworks suggest fundamental differences, but this has not been empirically validated.

8. **How do sector-specific AI intensity patterns (OECD taxonomy) interact with product-level AI integration decisions?** If a product serves a low-AI-intensity sector, should it lead the market or follow?

---

## 14. References

### Institutional and Policy Reports

1. OECD (2024). "A Sectoral Taxonomy of AI Intensity." OECD Artificial Intelligence Papers, No. 21. Paris: OECD Publishing. https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/a-sectoral-taxonomy-of-ai-intensity_c2baae71/1f6377b5-en.pdf

2. Stanford HAI (2025). "Artificial Intelligence Index Report 2025." Stanford University. https://hai.stanford.edu/ai-index/2025-ai-index-report

3. OECD AI Policy Observatory. https://oecd.ai/

4. Oxford Insights (2024). "Government AI Readiness Index 2024." https://oxfordinsights.com/ai-readiness/ai-readiness-index/

### Academic Papers

5. "AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications, and Challenges" (2025). arXiv. https://arxiv.org/html/2505.10468v4

6. "Where Does AI Play a Major Role in NPD and Product Management?" (2025). Management Review Quarterly, Springer. https://link.springer.com/article/10.1007/s11301-025-00533-5

7. "AI and New Product Development" (2024). ResearchGate. https://www.researchgate.net/publication/377460646

8. "Enhancing Human-AI Collaboration and Trust in NPD from Organization Clustering Perspective" (2025). Computers & Industrial Engineering, ScienceDirect. https://www.sciencedirect.com/science/article/abs/pii/S0360835225008435

9. "Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence" (2025). European Journal of Information Systems, Taylor & Francis. https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

10. "Artificial Intelligence, Firm Growth, and Product Innovation" (2023). Journal of Financial Economics, ScienceDirect. https://www.sciencedirect.com/science/article/pii/S0304405X2300185X

11. Agrawal et al. (2024). "Artificial Intelligence, Scientific Discovery, and Product Innovation." arXiv:2412.17866. https://arxiv.org/abs/2412.17866

12. Alsheibani, Cheung, and Messom (2020). "Artificial Intelligence Adoption: AI-readiness at Firm-Level." PACIS 2020 Proceedings. https://aisel.aisnet.org/pacis2020/37/

13. Pumplun, Taez, and Buxmann (2021). "A New Organizational Chassis for Artificial Intelligence: Exploring Organizational Readiness Factors." ECIS 2021.

14. Jockel, Grimm, and Coners (2022). "AI Readiness: A Systematic Literature Review." ECIS 2022.

15. "Ethics by Design for Artificial Intelligence" (2023). AI and Ethics, Springer. https://link.springer.com/article/10.1007/s43681-023-00330-4

16. "Responsible AI Governance: A Review and Research Framework" (2024). ScienceDirect. https://www.sciencedirect.com/science/article/pii/S0963868724000672

17. Brynjolfsson and McAfee (2017). "The Business of Artificial Intelligence." Harvard Business Review.

18. Agrawal, Gans, and Goldfarb (2018). "Prediction Machines: The Simple Economics of Artificial Intelligence." Harvard Business Review Press.

19. Steinert and Leifer (2010). "Scrutinizing Gartner's Hype Cycle Approach." PICMET Technology Management Conference.

### Industry and Practitioner Reports

20. McKinsey & Company (2025). "The State of AI." https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

21. Gartner (2025). "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026." https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

22. Deloitte (2026). "Agentic AI Strategy: From Pilot to Production." https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html

23. MIT Sloan Management Review. "When Generative AI Meets Product Development." https://sloanreview.mit.edu/article/when-generative-ai-meets-product-development/

24. HBR (2026). "To Drive AI Adoption, Build Your Team's Product Management Skills." https://hbr.org/2026/02/to-drive-ai-adoption-build-your-teams-product-management-skills

25. Microsoft (2025). "New Future of Work Report 2025." https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf

26. AI PM Tools Analysis. "Future of AI Product Management." https://aipmtools.org/articles/future-of-ai-product-management

---

*This document is part of the AI for Product Research Survey Project. It covers the "AI Frameworks & Taxonomies for Product" cross-cutting theme. Last updated: 2026-03-07.*
