# Responsible AI in Product Design: A Research Survey

**Compiled: March 2026**
**Scope: 2022--2026 literature, policy, and industry practice**

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Key Findings and Trends (2022--2026)](#2-key-findings-and-trends-20222026)
3. [Ethics by Design Framework](#3-ethics-by-design-framework)
4. [Three Pillars of Responsible AI: Lawful, Ethical, Robust](#4-three-pillars-of-responsible-ai-lawful-ethical-robust)
5. [Bias Mitigation in Generative AI](#5-bias-mitigation-in-generative-ai)
6. [AI Transparency, Fairness, and Privacy Integration](#6-ai-transparency-fairness-and-privacy-integration)
7. [Responsible AI Governance Frameworks](#7-responsible-ai-governance-frameworks)
8. [EU AI Act: Implications for Product Design](#8-eu-ai-act-implications-for-product-design)
9. [Inclusive and Equitable AI Product Design](#9-inclusive-and-equitable-ai-product-design)
10. [AI Impact Assessments and Audit Tools](#10-ai-impact-assessments-and-audit-tools)
11. [Industry Responsible AI Guidelines](#11-industry-responsible-ai-guidelines)
12. [Methods and Approaches](#12-methods-and-approaches)
13. [Limitations and Open Questions](#13-limitations-and-open-questions)
14. [Notable Papers and Sources](#14-notable-papers-and-sources)

---

## 1. Introduction

Responsible AI in product design has emerged as one of the defining themes of the 2020s in technology governance, human-computer interaction, and software engineering. As AI-powered products---from large language models to autonomous decision-support systems---have become pervasive across healthcare, finance, education, criminal justice, and consumer technology, the question of how to design these products responsibly has moved from an academic niche to a central concern of regulators, corporations, and civil society alike.

This survey synthesizes the major developments between 2022 and 2026, covering regulatory frameworks (particularly the EU AI Act), academic research on fairness, transparency, and accountability, industry self-governance initiatives from major technology companies, and practical methodologies for embedding responsibility throughout the AI product lifecycle.

---

## 2. Key Findings and Trends (2022--2026)

### 2.1 Regulatory Crystallization

The period 2022--2026 witnessed the transition of responsible AI from aspirational principles to binding law. The **EU AI Act**, politically agreed upon in December 2023 and formally adopted in 2024, established the world's first comprehensive, risk-based regulatory framework for AI systems. This catalyzed similar regulatory efforts globally, including updates to Canada's Artificial Intelligence and Data Act (AIDA), Brazil's AI regulatory framework, and China's series of sector-specific AI regulations.

### 2.2 Generative AI as a Catalyst

The release of ChatGPT (November 2022), GPT-4 (March 2023), and subsequent foundation models fundamentally reshaped the responsible AI landscape. Generative AI introduced novel risks---hallucination, deepfakes, intellectual property concerns, and amplification of biases at unprecedented scale---that existing frameworks were not designed to address. This drove a wave of new research, updated guidelines, and regulatory amendments (e.g., the EU AI Act's late-stage provisions on general-purpose AI models).

### 2.3 From Principles to Operationalization

A persistent finding across the literature is the "principles-to-practice gap" (Mittelstadt, 2019; Morley et al., 2020). By 2024--2025, the field shifted decisively toward operationalization: concrete tools (model cards, datasheets, fairness toolkits), organizational processes (AI ethics boards, impact assessments), and design methodologies (value-sensitive design, participatory AI design) gained traction in industry practice.

### 2.4 Intersectionality and Global Perspectives

Research increasingly recognized that responsible AI cannot be defined through a single cultural or legal lens. Work by scholars such as Abeba Birhane, Shakir Mohamed, and Sabelo Mhlambi emphasized the need for decolonial and pluralistic approaches to AI ethics, challenging Western-centric framings and foregrounding the perspectives of communities most affected by AI systems.

### 2.5 Accountability Infrastructure

The emergence of AI audit ecosystems---third-party auditors, internal red teams, regulatory sandboxes, and standardized assessment frameworks (ISO/IEC 42001, NIST AI RMF)---marked a maturation of the field. Product teams increasingly adopted structured accountability mechanisms rather than ad hoc ethics reviews.

---

## 3. Ethics by Design Framework

### 3.1 Origins and Conceptual Foundation

The **Ethics by Design (EbD)** framework draws on the tradition of **Privacy by Design** (Cavoukian, 2009) and **Value Sensitive Design** (Friedman & Hendry, 2019), extending these approaches to encompass the full spectrum of ethical considerations in AI system development. The European Commission's **High-Level Expert Group on Artificial Intelligence (AI HLEG)** was instrumental in promoting this concept.

The AI HLEG's *Ethics Guidelines for Trustworthy AI* (April 2019) articulated the foundational vision: ethical considerations should be integrated into every phase of AI system development---from problem formulation and data collection through model training, deployment, and monitoring---rather than treated as a post-hoc compliance exercise.

### 3.2 European Commission Adoption

The European Commission formally adopted the Ethics by Design approach through several key instruments:

- **Ethics Guidelines for Trustworthy AI** (AI HLEG, 2019): Established the conceptual framework and seven key requirements.
- **Assessment List for Trustworthy AI (ALTAI)** (2020): A practical self-assessment tool operationalizing the guidelines.
- **AI Act** (Regulation (EU) 2024/1689): Codified many EbD principles into binding law, requiring risk assessments, transparency measures, and human oversight to be designed into high-risk AI systems from inception.
- **AI Pact** (2024): A voluntary initiative encouraging organizations to adopt responsible AI practices ahead of the AI Act's full implementation timeline.

### 3.3 Core Principles of Ethics by Design

1. **Proactive, not reactive**: Ethical considerations are anticipated and embedded before harms materialize.
2. **Ethics as default**: Systems are designed with ethical safeguards enabled by default, not requiring user opt-in.
3. **Ethics embedded into design**: Ethical requirements are treated as functional requirements in the system design process.
4. **Full lifecycle coverage**: Ethical governance spans from conception through decommissioning.
5. **Stakeholder participation**: Affected communities are involved in design decisions.

### 3.4 Key References

- European Commission AI HLEG. (2019). *Ethics Guidelines for Trustworthy AI*. URL: https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai
- European Commission AI HLEG. (2020). *Assessment List for Trustworthy AI (ALTAI)*. URL: https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment
- Friedman, B., & Hendry, D. G. (2019). *Value Sensitive Design: Shaping Technology with Moral Imagination*. MIT Press.
- Cavoukian, A. (2009). *Privacy by Design: The 7 Foundational Principles*. Information and Privacy Commissioner of Ontario.

---

## 4. Three Pillars of Responsible AI: Lawful, Ethical, Robust

### 4.1 Framework Overview

The AI HLEG's *Ethics Guidelines for Trustworthy AI* established three interdependent pillars that a trustworthy AI system must satisfy simultaneously:

| Pillar | Description |
|--------|-------------|
| **Lawful** | The AI system complies with all applicable laws and regulations. |
| **Ethical** | The AI system adheres to ethical principles and values beyond mere legal compliance. |
| **Robust** | The AI system is technically and socially robust, performing reliably and safely even under adversarial conditions. |

### 4.2 Pillar 1: Lawful AI

Lawful AI requires compliance with fundamental rights (as enshrined in the EU Charter of Fundamental Rights), sector-specific regulations (e.g., GDPR for data protection, MDR for medical devices), and emerging AI-specific legislation. The EU AI Act operationalizes this pillar through a risk-based classification system:

- **Unacceptable risk**: Banned practices (e.g., social scoring by governments, real-time remote biometric identification in public spaces with narrow exceptions).
- **High risk**: Strict requirements (e.g., AI in hiring, credit scoring, law enforcement). Requires conformity assessments, quality management systems, and post-market monitoring.
- **Limited risk**: Transparency obligations (e.g., chatbots must disclose their AI nature).
- **Minimal risk**: No specific requirements beyond existing law.

### 4.3 Pillar 2: Ethical AI

The ethical pillar is grounded in four foundational ethical principles derived from bioethics and human rights:

1. **Respect for human autonomy**: AI systems should support human agency and decision-making, not undermine it.
2. **Prevention of harm**: AI systems must avoid causing or exacerbating harm (non-maleficence).
3. **Fairness**: AI systems should be free from unfair bias and should promote equal treatment and opportunity.
4. **Explicability**: AI systems should be transparent and their decisions should be explainable to affected individuals.

These principles map onto **seven key requirements** for Trustworthy AI:
1. Human agency and oversight
2. Technical robustness and safety
3. Privacy and data governance
4. Transparency
5. Diversity, non-discrimination, and fairness
6. Societal and environmental well-being
7. Accountability

### 4.4 Pillar 3: Robust AI

Technical robustness encompasses several dimensions that are directly relevant to product design:

- **Resilience to attack**: Resistance to adversarial inputs, data poisoning, and model extraction.
- **Fallback plans and general safety**: Graceful degradation, fail-safe mechanisms, and human override capabilities.
- **Accuracy and reliability**: Consistent performance across operational conditions.
- **Reproducibility**: Results should be reproducible and verifiable.

Recent work (2023--2025) has expanded this pillar to address robustness challenges specific to large language models and generative AI, including prompt injection attacks, jailbreaking, and hallucination mitigation.

### 4.5 Key References

- AI HLEG. (2019). *Ethics Guidelines for Trustworthy AI*. European Commission.
- Floridi, L., et al. (2018). "AI4People---An Ethical Framework for a Good AI Society: Opportunities, Risks, Principles, and Recommendations." *Minds and Machines*, 28(4), 689--707. DOI: 10.1007/s11023-018-9482-5
- Jobin, A., Ienca, M., & Vayena, E. (2019). "The global landscape of AI ethics guidelines." *Nature Machine Intelligence*, 1(9), 389--399. DOI: 10.1038/s42256-019-0088-2
- Smuha, N. A. (2019). "The EU Approach to Ethics Guidelines for Trustworthy Artificial Intelligence." *Computer Law Review International*, 20(4), 97--106.

---

## 5. Bias Mitigation in Generative AI

### 5.1 The Bias Landscape in Generative Systems

Generative AI systems---including large language models (LLMs), text-to-image models, and code generation tools---present qualitatively new bias challenges compared to traditional ML classifiers. These systems are trained on vast internet-scale corpora that reflect historical and systemic biases across race, gender, sexuality, disability, religion, nationality, and other dimensions.

Key research findings include:

- **Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021)**. "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *Proceedings of FAccT 2021*. This landmark paper warned about the environmental and social costs of large language models, including their propensity to encode and amplify biases from training data. URL: https://dl.acm.org/doi/10.1145/3442188.3445922

- **Liang, P., et al. (2023)**. "Holistic Evaluation of Language Models (HELM)." *Transactions on Machine Learning Research*. Provided a comprehensive benchmark framework for evaluating LLMs across multiple dimensions including fairness and bias. URL: https://crfm.stanford.edu/helm/

- **Bianchi, F., et al. (2023)**. "Easily Accessible Text-to-Image Generation Amplifies Demographic Stereotypes at Large Scale." *Proceedings of FAccT 2023*. Demonstrated systematic demographic biases in text-to-image models like Stable Diffusion. DOI: 10.1145/3593013.3594095

### 5.2 Data Diversity Strategies

Addressing bias at the data level is widely considered a necessary (though insufficient) condition for responsible generative AI:

1. **Curated and balanced datasets**: Projects like **BigScience's ROOTS corpus** (used to train BLOOM) employed systematic data governance with documented provenance, language coverage, and content filtering. (Laurençon et al., 2022)

2. **Data documentation**: **Datasheets for Datasets** (Gebru et al., 2021) and **Data Statements for NLP** (Bender & Friedman, 2018) provide structured templates for documenting dataset composition, collection processes, intended uses, and known biases.

3. **Participatory data collection**: Engaging diverse communities in data collection and annotation to ensure representativeness. The **Masakhane** project (Orife et al., 2020) exemplifies community-driven NLP dataset creation for African languages.

4. **Synthetic data augmentation**: Using controlled generation to supplement underrepresented categories, though with caution about introducing new forms of distributional bias.

### 5.3 Algorithmic Audits

Algorithmic auditing has matured significantly:

- **Internal audits**: Systematic testing across demographic subgroups before deployment. Companies like OpenAI, Google DeepMind, and Anthropic publish system cards and red-teaming results.
- **External/third-party audits**: Organizations such as the **Algorithmic Justice League** (founded by Joy Buolamwini), **AI Forensics**, and **ORCAA** (O'Neil Risk Consulting & Algorithmic Auditing, founded by Cathy O'Neil) conduct independent assessments.
- **Regulatory audits**: The EU AI Act mandates conformity assessments for high-risk AI systems, and NYC Local Law 144 (effective July 2023) requires bias audits for automated employment decision tools.

### 5.4 Algorithmic Clarity and Interpretability

"Algorithmic clarity" refers to the broader goal of making AI decision-making processes understandable to stakeholders:

- **Model cards** (Mitchell et al., 2019): Standardized documentation of model performance across demographic groups. URL: https://arxiv.org/abs/1810.03993
- **Explainable AI (XAI) techniques**: SHAP (Lundberg & Lee, 2017), LIME (Ribeiro et al., 2016), and attention visualization methods.
- **Constitutional AI** (Bai et al., 2022, Anthropic): A method for training AI assistants to be harmless and helpful using a set of principles ("constitution") to guide self-supervised refinement. URL: https://arxiv.org/abs/2212.08073
- **Mechanistic interpretability**: Emerging research on understanding the internal representations of neural networks (Olah et al., Anthropic, 2023--2025).

### 5.5 Key References

- Gebru, T., et al. (2021). "Datasheets for Datasets." *Communications of the ACM*, 64(12), 86--92. DOI: 10.1145/3458723
- Mitchell, M., et al. (2019). "Model Cards for Model Reporting." *Proceedings of FAccT 2019*. DOI: 10.1145/3287560.3287596
- Buolamwini, J., & Gebru, T. (2018). "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." *Proceedings of FAccT 2018*. URL: http://proceedings.mlr.press/v81/buolamwini18a.html
- Weidinger, L., et al. (2022). "Taxonomy of Risks Posed by Language Models." *Proceedings of FAccT 2022*. (Google DeepMind)

---

## 6. AI Transparency, Fairness, and Privacy Integration

### 6.1 Transparency

Transparency in AI product design operates at multiple levels:

- **Algorithmic transparency**: Making the logic and decision processes of AI systems understandable. The EU AI Act requires providers of high-risk AI systems to ensure "sufficient transparency to enable deployers to interpret the system's output and use it appropriately" (Article 13).
- **Organizational transparency**: Disclosing the existence and nature of AI systems to affected individuals. The AI Act mandates that users be informed when they are interacting with an AI system (Article 50).
- **Data transparency**: Clear documentation of training data sources, processing methods, and known limitations.

Notable frameworks:

- **Transparency Notes** (Microsoft, 2022--present): Standardized documentation accompanying AI services that explain intended uses, limitations, and responsible deployment practices. URL: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/transparency-note
- **System Cards** (OpenAI, 2023--present): Comprehensive technical and safety documentation released alongside model launches.

### 6.2 Fairness

Fairness in AI product design remains a deeply contested concept with multiple mathematical formalizations that can be mutually incompatible (Chouldechova, 2017; Kleinberg et al., 2016):

- **Group fairness**: Statistical parity across protected groups (demographic parity, equalized odds, predictive parity).
- **Individual fairness**: Similar individuals should receive similar predictions (Dwork et al., 2012).
- **Counterfactual fairness**: Predictions should remain unchanged in a counterfactual world where the individual's protected attribute were different (Kusner et al., 2017).
- **Procedural fairness**: Focus on the process by which decisions are made rather than outcomes alone.

Practical fairness tools developed and maintained by industry:

| Tool | Developer | Description |
|------|-----------|-------------|
| **Fairlearn** | Microsoft | Open-source toolkit for assessing and improving AI fairness. URL: https://fairlearn.org/ |
| **AI Fairness 360 (AIF360)** | IBM | Comprehensive open-source library with 70+ fairness metrics and 10+ bias mitigation algorithms. URL: https://aif360.mybluemix.net/ |
| **What-If Tool** | Google | Visual interface for probing ML model behavior and fairness. URL: https://pair-code.github.io/what-if-tool/ |
| **Responsible AI Toolbox** | Microsoft | Suite of tools for model debugging, fairness assessment, and interpretability. URL: https://responsibleaitoolbox.ai/ |

### 6.3 Privacy Integration

Privacy and AI are deeply intertwined, particularly in product design:

- **Privacy by Design and by Default**: Mandated by GDPR Article 25 and reinforced by the AI Act's data governance requirements for high-risk systems.
- **Federated Learning**: Training models on distributed data without centralizing sensitive information (McMahan et al., 2017, Google).
- **Differential Privacy**: Providing mathematical guarantees about individual privacy in aggregate data releases and model training (Dwork, 2006; Abadi et al., 2016). Apple and Google have deployed differential privacy in consumer products.
- **Privacy-Enhancing Technologies (PETs)**: Homomorphic encryption, secure multi-party computation, and synthetic data generation for privacy-preserving AI development.

### 6.4 Integration Challenges

A key finding in the literature is the tension between transparency, fairness, and privacy---optimizing for one may compromise another:

- Full transparency about training data may conflict with privacy requirements.
- Privacy-preserving techniques (e.g., differential privacy) can disproportionately reduce model accuracy for underrepresented groups, exacerbating fairness concerns (Bagdasaryan et al., 2019).
- Fairness interventions may require collecting sensitive demographic data, creating privacy risks.

Product designers must navigate these trade-offs explicitly, making them a core design decision rather than a technical afterthought.

### 6.5 Key References

- Chouldechova, A. (2017). "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments." *Big Data*, 5(2), 153--163.
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). "Inherent Trade-Offs in the Fair Determination of Risk Scores." *Proceedings of ITCS 2017*. URL: https://arxiv.org/abs/1609.05807
- Bagdasaryan, E., Poursaeed, O., & Shmatikov, V. (2019). "Differential Privacy Has Disparate Impact on Model Accuracy." *NeurIPS 2019*.
- Selbst, A. D., et al. (2019). "Fairness and Abstraction in Sociotechnical Systems." *Proceedings of FAccT 2019*. DOI: 10.1145/3287560.3287598

---

## 7. Responsible AI Governance Frameworks

### 7.1 International Standards

Several major standardization efforts have shaped responsible AI governance:

- **NIST AI Risk Management Framework (AI RMF 1.0)** (January 2023): Developed by the U.S. National Institute of Standards and Technology, this voluntary framework provides a structured approach to managing AI risks across four functions: Govern, Map, Measure, and Manage. A companion **Generative AI Profile** was released in 2024. URL: https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence
- **ISO/IEC 42001:2023**: The first international management system standard for AI, specifying requirements for establishing, implementing, maintaining, and continually improving an AI management system within organizations. URL: https://www.iso.org/standard/81230.html
- **ISO/IEC 23894:2023**: Guidance on AI risk management, extending ISO 31000 to AI-specific contexts.
- **IEEE 7000-2021**: Standard for the model process for addressing ethical concerns during system design.
- **OECD AI Principles** (2019, updated 2024): Adopted by 46 countries, these principles emphasize inclusive growth, sustainable development, human-centered values, transparency, robustness, and accountability. URL: https://oecd.ai/en/ai-principles

### 7.2 Organizational Governance Models

Research and practice have identified several organizational models for AI governance:

1. **Centralized AI Ethics Board**: A dedicated body (e.g., a Chief AI Ethics Officer or committee) with authority to review and approve AI projects. Examples include Microsoft's Office of Responsible AI (ORA) and Salesforce's Office of Ethical and Humane Use.

2. **Distributed Responsibility Model**: Embedding responsible AI practices within existing product development teams, supported by guidelines, training, and tooling. Google's approach integrates responsible AI review into standard product launch processes.

3. **Hybrid Models**: Combining centralized oversight with distributed execution, often using "responsible AI champions" or liaisons within product teams.

4. **External Advisory Bodies**: Independent advisory boards providing external perspective. (Note: Google's Advanced Technology External Advisory Council, launched in 2019, was dissolved within a week due to controversy, highlighting the challenges of this model.)

### 7.3 Governance Lifecycle Integration

Modern frameworks emphasize governance across the full AI product lifecycle:

```
Problem       Data          Model         Deployment    Monitoring &
Formulation → Collection → Development → & Launch   → Maintenance
    ↕              ↕            ↕             ↕            ↕
Impact        Data         Bias &        Transparency  Continuous
Assessment    Governance   Fairness      & Disclosure  Auditing
              & Privacy    Testing                     & Feedback
```

### 7.4 Key References

- NIST. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. URL: https://doi.org/10.6028/NIST.AI.100-1
- Raji, I. D., et al. (2020). "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing." *Proceedings of FAccT 2020*. DOI: 10.1145/3351095.3372873
- Mäntymäki, M., Minkkinen, M., Birkstedt, T., & Viljanen, M. (2022). "Defining organizational AI governance." *AI and Ethics*, 2, 603--609. DOI: 10.1007/s43681-022-00143-x

---

## 8. EU AI Act: Implications for Product Design

### 8.1 Overview

The **EU AI Act** (Regulation (EU) 2024/1689) was published in the Official Journal of the European Union on 12 July 2024, with a phased implementation timeline:

- **February 2025**: Prohibitions on unacceptable-risk AI practices take effect.
- **August 2025**: Requirements for general-purpose AI (GPAI) models take effect; governance structures must be established.
- **August 2026**: Full requirements for high-risk AI systems apply.
- **August 2027**: Requirements for high-risk AI systems that are also regulated products (e.g., medical devices, machinery) apply.

### 8.2 Direct Implications for Product Design

#### 8.2.1 Risk Classification as a Design Requirement

Product teams must classify their AI systems by risk level at the design stage, as the classification determines the applicable regulatory requirements. This requires early-stage risk assessment integrated into product planning.

#### 8.2.2 High-Risk AI System Requirements (Title III, Chapter 2)

For AI systems classified as high-risk (Annex III), the following design requirements apply:

- **Risk management system** (Article 9): A continuous, iterative process of risk identification, analysis, estimation, and evaluation throughout the system lifecycle.
- **Data governance** (Article 10): Training, validation, and testing datasets must be "relevant, sufficiently representative, and to the best extent possible, free of errors and complete."
- **Technical documentation** (Article 11): Comprehensive documentation of system design, development, and capabilities.
- **Record-keeping** (Article 12): Automatic logging of events during operation for traceability.
- **Transparency and information provision** (Article 13): Instructions for use, intended purpose, level of accuracy, and known limitations.
- **Human oversight** (Article 14): Systems must be designed to allow effective human oversight, including the ability to override or reverse outputs.
- **Accuracy, robustness, and cybersecurity** (Article 15): Systems must perform consistently and be resilient to errors and attacks.

#### 8.2.3 General-Purpose AI Models (Title IIIa)

Providers of GPAI models must:
- Maintain up-to-date technical documentation.
- Provide information and documentation to downstream deployers integrating the model into high-risk systems.
- Comply with the EU Copyright Directive.
- Publish a sufficiently detailed summary of training data content.

GPAI models posing **systemic risk** (based on computational power thresholds, initially set at 10^25 FLOPs) face additional obligations including model evaluation, adversarial testing, incident reporting, and cybersecurity measures.

#### 8.2.4 Transparency Requirements for All AI Systems

- AI systems interacting with natural persons must disclose their AI nature (chatbot transparency).
- AI-generated or manipulated content (deepfakes) must be labeled as such.
- Emotion recognition and biometric categorization systems must inform subjects of their operation.

### 8.3 Practical Design Adaptations

Product design teams must adapt their processes to comply:

1. **Documentation-first design**: Establishing technical documentation frameworks at the design stage.
2. **Conformity assessment readiness**: Designing systems with testability and auditability in mind.
3. **Post-market monitoring**: Building in telemetry and monitoring infrastructure from inception.
4. **User-facing transparency**: Integrating disclosure mechanisms into user interfaces.
5. **Override mechanisms**: Designing human oversight interfaces that are meaningful, not perfunctory.

### 8.4 Key References

- European Parliament and Council. (2024). *Regulation (EU) 2024/1689 (AI Act)*. Official Journal of the European Union. URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Veale, M., & Zuiderveen Borgesius, F. (2021). "Demystifying the Draft EU Artificial Intelligence Act." *Computer Law Review International*, 22(4), 97--112. DOI: 10.9785/cri-2021-220402
- Edwards, L. (2022). "Regulating AI in Europe: Four Problems and Four Solutions." *Ada Lovelace Institute*.
- Hacker, P., Engel, A., & Mauer, M. (2023). "Regulating ChatGPT and Other Large Generative AI Models." *Proceedings of FAccT 2023*.

---

## 9. Inclusive and Equitable AI Product Design

### 9.1 The Case for Inclusive Design

Inclusive AI product design goes beyond bias mitigation to fundamentally rethink who is included in the design process and who benefits from AI systems. Key works include:

- **Costanza-Chock, S. (2020)**. *Design Justice: Community-Led Practices to Build the Worlds We Need*. MIT Press. This foundational text articulates how design processes can reproduce or challenge structural inequality, proposing principles for centering marginalized communities in technology design. URL: https://designjustice.mitpress.mit.edu/

- **Mohamed, S., Png, M.-T., & Isaac, W. (2020)**. "Decolonial AI: Decolonial Theory as Sociotechnical Foresight in Artificial Intelligence." *Philosophy & Technology*, 33, 659--684. This paper critiques the power asymmetries embedded in AI development and proposes decolonial frameworks for more equitable AI. DOI: 10.1007/s13347-020-00405-8

### 9.2 Participatory Design Methods

Several participatory approaches have been applied to AI product design:

1. **Participatory Machine Learning**: Engaging affected communities in defining problem formulations, selecting features, and evaluating model outputs (Birhane et al., 2022).
2. **Community-Based System Dynamics**: Modeling the social systems AI products operate within, co-designed with community stakeholders.
3. **Deliberative Alignment**: OpenAI and Anthropic have experimented with democratic deliberation processes (e.g., OpenAI's "Democratic Inputs to AI" program, 2023) to inform AI system behavior.
4. **Accessibility-first design**: Ensuring AI products are usable by people with disabilities, including considerations for screen readers, cognitive accessibility, and alternative interaction modalities.

### 9.3 Equity-Focused Evaluation

- **Disaggregated evaluation**: Breaking down performance metrics by demographic subgroups to identify disparities (Barocas et al., 2019).
- **Intersectional analysis**: Evaluating performance across intersecting identity dimensions (e.g., race and gender jointly), following Buolamwini and Gebru's (2018) "Gender Shades" methodology.
- **User experience equity**: Assessing not just accuracy but the quality of the user experience across different populations, languages, and cultural contexts.

### 9.4 Global and Multilingual Considerations

- Responsible AI product design must account for the extreme imbalance in NLP resources across languages. As of 2024, fewer than 100 of the world's approximately 7,000 languages have significant digital NLP resources.
- The **BLOOM** model (BigScience, 2022) and **Aya** model (Cohere for AI, 2024) represent efforts to create more linguistically inclusive foundation models.

### 9.5 Key References

- Birhane, A., et al. (2022). "Power to the People? Opportunities and Challenges for Participatory AI." *Equity and Access in Algorithms, Mechanisms, and Optimization (EAAMO 2022)*. DOI: 10.1145/3551624.3555290
- Zhi-Xuan, T., et al. (2024). "Beyond Preferences in AI Alignment." *arXiv preprint*. (Discussion of pluralistic approaches to AI value alignment.)
- Singh, A., et al. (2024). "Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model." *arXiv:2402.07827*.

---

## 10. AI Impact Assessments and Audit Tools

### 10.1 AI Impact Assessments (AIIAs)

AI Impact Assessments are structured evaluations of the potential effects of an AI system on individuals, groups, and society. They have become a central mechanism for responsible AI governance:

- **Algorithmic Impact Assessment (AIA)** (Canada, 2019): The Canadian government's mandatory assessment tool for federal agencies deploying AI in public services. URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html

- **Human Rights Impact Assessment for AI** (Access Now, 2018; Mantelero, 2018): Frameworks adapting human rights due diligence processes to AI contexts.

- **AI Impact Assessment frameworks** have been proposed by the Ada Lovelace Institute (2022), the AI Now Institute, and academic researchers (Selbst, 2021; Reisman et al., 2018).

Key components of a comprehensive AIIA:

1. **System description**: Purpose, functionality, intended users, and affected populations.
2. **Data assessment**: Sources, representativeness, quality, and privacy implications.
3. **Bias and fairness analysis**: Testing for discriminatory outcomes across protected characteristics.
4. **Rights impact analysis**: Effects on fundamental rights including privacy, freedom of expression, due process, and non-discrimination.
5. **Risk mitigation plan**: Specific measures to address identified risks.
6. **Ongoing monitoring plan**: Post-deployment evaluation and reporting mechanisms.
7. **Stakeholder engagement record**: Documentation of consultations with affected communities.

### 10.2 Audit Tools and Frameworks

#### 10.2.1 Technical Audit Tools

| Tool | Purpose | Developer |
|------|---------|-----------|
| **Fairlearn** | Fairness assessment and mitigation | Microsoft (open-source) |
| **AI Fairness 360** | Bias detection and mitigation | IBM (open-source) |
| **Aequitas** | Bias and fairness audit toolkit | University of Chicago (open-source) |
| **ML-Check** | Property-based testing for ML models | Academic |
| **Google Model Cards Toolkit** | Standardized model documentation | Google (open-source) |
| **Holistic Evaluation of Language Models (HELM)** | Comprehensive LLM evaluation | Stanford CRFM |
| **DeepEval** | LLM evaluation framework | Open-source |

#### 10.2.2 Process-Oriented Audit Frameworks

- **Raji et al. (2020)**: *End-to-End Internal Algorithmic Auditing Framework* (SMACTR: Scoping, Mapping, Artifact Collection, Testing, Reflection). A five-stage framework developed based on practices at organizations including Google and other technology companies.

- **IEEE 7010-2020**: *Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being*. Provides a structured methodology for well-being impact assessment.

- **ALTAI** (Assessment List for Trustworthy AI): The European Commission's self-assessment checklist operationalizing the seven requirements of trustworthy AI.

### 10.3 Third-Party Auditing Ecosystem

The period 2022--2025 saw the emergence of a growing ecosystem of third-party AI auditors:

- **ORCAA** (O'Neil Risk Consulting & Algorithmic Auditing): Founded by Cathy O'Neil, focuses on mathematical auditing of algorithmic systems.
- **Holistic AI**: Provides AI audit and risk management services and has developed the first AI audit tool certified to ISO standards.
- **ForHumanity**: Nonprofit developing audit rules and certification schemes for AI systems, particularly focused on the EU AI Act.
- **Credo AI**: AI governance platform providing risk assessment, policy management, and compliance tracking.

### 10.4 Key References

- Raji, I. D., et al. (2020). "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing." *FAccT 2020*.
- Metaxa, D., et al. (2021). "Auditing Algorithms: Understanding Algorithmic Systems from the Outside In." *Foundations and Trends in Human-Computer Interaction*, 14(4), 272--344.
- Ada Lovelace Institute. (2022). *Algorithmic Impact Assessment: A Case Study in Healthcare*. URL: https://www.adalovelaceinstitute.org/report/algorithmic-impact-assessment-healthcare/
- Mökander, J., et al. (2023). "Auditing Large Language Models: A Three-Layered Approach." *AI and Ethics*. DOI: 10.1007/s43681-023-00289-2

---

## 11. Industry Responsible AI Guidelines

### 11.1 Google

**Principles** (published June 2018, updated periodically):
1. Be socially beneficial
2. Avoid creating or reinforcing unfair bias
3. Be built and tested for safety
4. Be accountable to people
5. Incorporate privacy design principles
6. Uphold high standards of scientific excellence
7. Be made available for uses that accord with these principles

Google also identified AI applications it "will not pursue," including weapons, surveillance violating norms, and technologies contravening international law.

**Operational mechanisms**:
- Centralized AI Principles review process integrated into product launches.
- **PAIR (People + AI Research)** initiative: Produces research and design guidelines for human-AI interaction. URL: https://pair.withgoogle.com/
- **Responsible AI Toolkit**: Collection of tools and guidance including the What-If Tool, Model Cards, and fairness indicators. URL: https://www.tensorflow.org/responsible_ai
- Published *Responsible Generative AI Toolkit* (2023) specifically addressing risks of generative models.

**Key publication**: Google DeepMind. (2024). "Sociotechnical Safety Evaluation of Generative AI Systems." *arXiv preprint*.

### 11.2 Microsoft

**Principles** (six core principles):
1. Fairness
2. Reliability and safety
3. Privacy and security
4. Inclusiveness
5. Transparency
6. Accountability

**Operational mechanisms**:
- **Office of Responsible AI (ORA)**: Sets company-wide policies and governance.
- **Responsible AI Standard v2** (2022): Internal standard specifying requirements for AI systems across the product lifecycle. URL: https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf
- **Responsible AI Dashboard**: Integrated tool in Azure ML for model debugging, fairness assessment, and error analysis.
- **AI Impact Assessment template**: Internal process document requiring teams to assess potential harms before launch.
- **Transparency Notes**: Published documentation for each AI service.

**Key publication**: Microsoft. (2022). *Microsoft Responsible AI Standard, v2*. Notably detailed in its operational requirements, moving beyond high-level principles to specific, testable criteria.

### 11.3 Meta

**Principles** (five pillars):
1. Privacy and security
2. Fairness and inclusion
3. Robustness and safety
4. Transparency and control
5. Accountability and governance

**Operational mechanisms**:
- **Responsible AI (RAI) team**: Cross-functional team within Meta working on tools, processes, and research.
- **Fairness Flow**: Internal tool for measuring and mitigating bias in ML systems at Meta's scale.
- **System Cards**: Published for major AI systems (e.g., the Llama model family).
- Open-sourcing of models (Llama 2, Llama 3) with Acceptable Use Policies and responsible use guides.
- **Purple Llama** (2023): An umbrella project for open trust and safety tools for generative AI, including CyberSecEval and Llama Guard. URL: https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/

**Key publication**: Meta. (2023). *Llama 2: Open Foundation and Fine-Tuned Chat Models*. Included an extensive responsible use section and safety evaluation.

### 11.4 Cross-Industry Initiatives

- **Partnership on AI** (founded 2016): Multi-stakeholder organization developing best practices. URL: https://partnershiponai.org/
- **Frontier Model Forum** (founded 2023 by Anthropic, Google, Microsoft, OpenAI): Focused on safety research for frontier AI models.
- **AI Safety Summit** (Bletchley Park, November 2023; Seoul, May 2024): International governmental summits producing the Bletchley Declaration and Seoul Declaration on AI safety.
- **White House Executive Order on AI** (October 2023, EO 14110): Required safety testing and reporting for powerful AI models, though elements were rescinded in early 2025.

---

## 12. Methods and Approaches

### 12.1 Value Sensitive Design (VSD)

Value Sensitive Design, developed by Batya Friedman and colleagues at the University of Washington, provides a tripartite methodology for integrating human values into technology design:

1. **Conceptual investigations**: Identifying stakeholders (direct and indirect) and the values at stake.
2. **Empirical investigations**: Studying stakeholder perspectives, needs, and contexts through qualitative and quantitative research.
3. **Technical investigations**: Designing system properties and features that support identified values.

VSD has been applied to AI product design in domains including healthcare AI (Zhu et al., 2022), autonomous vehicles, and content moderation systems.

### 12.2 Responsible AI Pattern Catalogue

Lu et al. (2023) proposed a **Responsible AI Pattern Catalogue** providing reusable design patterns for responsible AI, organized across the AI system lifecycle:

- **Governance patterns**: RAI governance structures, risk assessment templates.
- **Process patterns**: Continuous documentation, iterative stakeholder engagement.
- **Product patterns**: Explainability interfaces, appeal mechanisms, human-in-the-loop designs.

**Reference**: Lu, Q., et al. (2023). "Responsible AI Pattern Catalogue: A Collection of Best Practices for AI Governance and Engineering." *ACM Computing Surveys*, 56(3). DOI: 10.1145/3626234

### 12.3 AI Ethics Frameworks Comparison

Hagendorff (2020) conducted a systematic analysis of 22 AI ethics guidelines, finding significant convergence on principles of transparency, justice/fairness, non-maleficence, responsibility, and privacy, but notable gaps in attention to sustainability, labor impacts, and power asymmetries.

**Reference**: Hagendorff, T. (2020). "The Ethics of AI Ethics: An Evaluation of Guidelines." *Minds and Machines*, 30, 99--120. DOI: 10.1007/s11023-020-09517-8

### 12.4 Red Teaming and Adversarial Testing

Red teaming has become a standard practice for responsible AI product design, particularly for generative AI:

- **Structured red teaming**: Systematic probing for harmful outputs across predefined risk categories. Anthropic, OpenAI, and Google DeepMind all conduct extensive red teaming before major model releases.
- **Crowdsourced red teaming**: Programs like Anthropic's bug bounty and HackerOne-style engagements for AI safety.
- **Automated red teaming**: Using AI systems to systematically probe other AI systems for vulnerabilities (Perez et al., 2022). **Reference**: Perez, E., et al. (2022). "Red Teaming Language Models with Language Models." *EMNLP 2022*.

### 12.5 Responsible AI Maturity Models

Several maturity models have been proposed to help organizations assess and improve their responsible AI practices:

- **Microsoft's Responsible AI Maturity Model** (2023): Five stages from Ad Hoc to Optimizing.
- **Capgemini's AI Ethics Maturity Framework** (2022): Assesses organizational readiness across governance, culture, and technical dimensions.
- **WEF's AI Governance Alliance** frameworks (2024): Industry-specific maturity assessments.

---

## 13. Limitations and Open Questions

### 13.1 Persistent Challenges

1. **The principles-to-practice gap remains**: Despite significant progress, many organizations still struggle to translate high-level ethical principles into concrete engineering practices. Morley et al. (2023) found that the availability of tools does not automatically lead to their adoption; organizational culture, incentives, and expertise are critical mediators.

2. **Defining and measuring fairness**: The impossibility theorems (Chouldechova, 2017; Kleinberg et al., 2016) demonstrate that certain mathematical fairness criteria cannot be simultaneously satisfied, requiring normative choices that technical frameworks alone cannot resolve.

3. **Explainability vs. capability trade-off**: More capable AI systems (particularly deep learning and large language models) tend to be less inherently interpretable. Post-hoc explanation methods (SHAP, LIME) provide approximations but may not faithfully represent the model's actual decision process (Rudin, 2019).

4. **Global regulatory fragmentation**: Despite convergence on high-level principles, significant divergence exists in regulatory approaches across jurisdictions, creating compliance challenges for global products.

5. **Evaluation of generative AI**: Traditional fairness metrics designed for classification tasks do not straightforwardly apply to open-ended generative systems. New evaluation paradigms are still maturing.

### 13.2 Open Research Questions

1. **How should responsibility be distributed across the AI value chain?** The EU AI Act distinguishes between providers, deployers, importers, and distributors, but the practical allocation of responsibility---especially for foundation models used in diverse downstream applications---remains contested.

2. **Can AI systems be truly "aligned" with human values?** The alignment problem, particularly for advanced AI systems, remains a fundamental open question. Whose values should be encoded, and how can pluralistic values be represented in a single system?

3. **What constitutes adequate transparency for different stakeholders?** Technical transparency (model architecture, training data) may differ vastly from user-facing transparency (clear explanations of AI involvement). Research is needed on what forms of transparency are actually effective for different audiences.

4. **How should environmental costs of AI be factored into responsible design?** Training large AI models has significant carbon footprints (Strubell et al., 2019; Patterson et al., 2021). Responsible AI product design should account for environmental sustainability, but frameworks for doing so are underdeveloped.

5. **How can responsible AI practices scale to open-source and decentralized AI ecosystems?** Open-source models (Llama, Mistral, Stable Diffusion) can be fine-tuned and deployed by anyone, challenging governance frameworks designed for centralized providers.

6. **What role should affected communities play in AI governance?** Meaningful participation requires resources, access, and power that are often lacking. Research on effective participatory mechanisms for AI governance is still nascent.

7. **How should AI-generated content be governed?** Issues of attribution, intellectual property, misinformation, and authenticity in AI-generated content represent frontier challenges for responsible product design.

### 13.3 Methodological Limitations of the Field

- Much responsible AI research is concentrated in Western academic institutions and technology companies, potentially limiting the generalizability of findings.
- Empirical studies of responsible AI practices in industry often rely on self-reported data from companies, introducing potential bias.
- The rapid pace of AI development means that research findings and regulatory frameworks may lag behind deployed capabilities.
- Interdisciplinary integration between computer science, law, philosophy, and social science remains challenging, with disciplinary silos limiting holistic analysis.

---

## 14. Notable Papers and Sources

### 14.1 Foundational Papers

| Year | Authors | Title | Venue | URL/DOI |
|------|---------|-------|-------|---------|
| 2018 | Floridi, L., et al. | AI4People---An Ethical Framework for a Good AI Society | *Minds and Machines* | DOI: 10.1007/s11023-018-9482-5 |
| 2018 | Buolamwini, J. & Gebru, T. | Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification | *FAccT 2018* | http://proceedings.mlr.press/v81/buolamwini18a.html |
| 2019 | Jobin, A., Ienca, M., & Vayena, E. | The Global Landscape of AI Ethics Guidelines | *Nature Machine Intelligence* | DOI: 10.1038/s42256-019-0088-2 |
| 2019 | AI HLEG | Ethics Guidelines for Trustworthy AI | European Commission | https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai |
| 2019 | Mitchell, M., et al. | Model Cards for Model Reporting | *FAccT 2019* | DOI: 10.1145/3287560.3287596 |
| 2019 | Friedman, B. & Hendry, D. G. | Value Sensitive Design: Shaping Technology with Moral Imagination | MIT Press | ISBN: 978-0262039536 |
| 2019 | Selbst, A. D., et al. | Fairness and Abstraction in Sociotechnical Systems | *FAccT 2019* | DOI: 10.1145/3287560.3287598 |
| 2020 | Costanza-Chock, S. | Design Justice: Community-Led Practices to Build the Worlds We Need | MIT Press | https://designjustice.mitpress.mit.edu/ |
| 2020 | Mohamed, S., Png, M.-T., & Isaac, W. | Decolonial AI: Decolonial Theory as Sociotechnical Foresight in Artificial Intelligence | *Philosophy & Technology* | DOI: 10.1007/s13347-020-00405-8 |
| 2020 | Morley, J., et al. | From What to How: An Initial Review of Publicly Available AI Ethics Tools, Methods and Research | *Science and Engineering Ethics* | DOI: 10.1007/s11948-019-00165-5 |

### 14.2 Key Papers (2021--2023)

| Year | Authors | Title | Venue | URL/DOI |
|------|---------|-------|-------|---------|
| 2021 | Bender, E. M., et al. | On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? | *FAccT 2021* | DOI: 10.1145/3442188.3445922 |
| 2021 | Gebru, T., et al. | Datasheets for Datasets | *Communications of the ACM* | DOI: 10.1145/3458723 |
| 2022 | Bai, Y., et al. | Constitutional AI: Harmlessness from AI Feedback | *arXiv* | https://arxiv.org/abs/2212.08073 |
| 2022 | Weidinger, L., et al. | Taxonomy of Risks Posed by Language Models | *FAccT 2022* | DOI: 10.1145/3531146.3533088 |
| 2022 | Mäntymäki, M., et al. | Defining Organizational AI Governance | *AI and Ethics* | DOI: 10.1007/s43681-022-00143-x |
| 2023 | NIST | AI Risk Management Framework (AI RMF 1.0) | NIST | https://doi.org/10.6028/NIST.AI.100-1 |
| 2023 | Liang, P., et al. | Holistic Evaluation of Language Models | *TMLR* | https://crfm.stanford.edu/helm/ |
| 2023 | Lu, Q., et al. | Responsible AI Pattern Catalogue | *ACM Computing Surveys* | DOI: 10.1145/3626234 |
| 2023 | Mökander, J., et al. | Auditing Large Language Models: A Three-Layered Approach | *AI and Ethics* | DOI: 10.1007/s43681-023-00289-2 |
| 2023 | Bianchi, F., et al. | Easily Accessible Text-to-Image Generation Amplifies Demographic Stereotypes at Large Scale | *FAccT 2023* | DOI: 10.1145/3593013.3594095 |

### 14.3 Recent Papers (2024--2025)

| Year | Authors | Title | Venue | URL/DOI |
|------|---------|-------|-------|---------|
| 2024 | EU Parliament & Council | Regulation (EU) 2024/1689 (AI Act) | Official Journal of the EU | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| 2024 | Singh, A., et al. | Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model | *arXiv* | https://arxiv.org/abs/2402.07827 |
| 2024 | OECD | Updated OECD AI Principles | OECD | https://oecd.ai/en/ai-principles |
| 2024 | ISO/IEC | ISO/IEC 42001:2023 (AI Management System Standard) | ISO | https://www.iso.org/standard/81230.html |

### 14.4 Industry Resources

| Organization | Resource | URL |
|-------------|----------|-----|
| Microsoft | Responsible AI Standard v2 | https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf |
| Microsoft | Fairlearn | https://fairlearn.org/ |
| Microsoft | Responsible AI Toolbox | https://responsibleaitoolbox.ai/ |
| Google | PAIR (People + AI Research) | https://pair.withgoogle.com/ |
| Google | Responsible AI Toolkit | https://www.tensorflow.org/responsible_ai |
| IBM | AI Fairness 360 | https://aif360.mybluemix.net/ |
| Meta | Purple Llama | https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/ |
| Partnership on AI | Multi-stakeholder best practices | https://partnershiponai.org/ |
| Stanford CRFM | HELM benchmark | https://crfm.stanford.edu/helm/ |
| Ada Lovelace Institute | Research and policy | https://www.adalovelaceinstitute.org/ |
| AI Now Institute | Policy research | https://ainowinstitute.org/ |
| Algorithmic Justice League | Advocacy and research | https://www.ajl.org/ |

### 14.5 Key Books

- Friedman, B., & Hendry, D. G. (2019). *Value Sensitive Design: Shaping Technology with Moral Imagination*. MIT Press.
- Costanza-Chock, S. (2020). *Design Justice: Community-Led Practices to Build the Worlds We Need*. MIT Press.
- O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.
- Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. St. Martin's Press.
- Benjamin, R. (2019). *Race After Technology: Abolitionist Tools for the New Jim Code*. Polity.
- Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.

---

## Appendix: Glossary of Key Terms

| Term | Definition |
|------|------------|
| **AI Impact Assessment (AIIA)** | A structured evaluation of the potential effects of an AI system on individuals, groups, and society. |
| **Algorithmic audit** | A systematic evaluation of an algorithm's behavior, typically assessing fairness, accuracy, and compliance. |
| **Constitutional AI** | A method for training AI systems to be helpful and harmless using a set of written principles for self-supervised refinement. |
| **Datasheets for Datasets** | A documentation framework providing structured information about dataset composition, collection, and intended use. |
| **Ethics by Design (EbD)** | An approach integrating ethical considerations into every phase of AI system development. |
| **Explainable AI (XAI)** | Techniques and methods for making AI system decisions understandable to humans. |
| **Foundation model** | A large AI model trained on broad data that can be adapted to a wide range of downstream tasks. |
| **General-Purpose AI (GPAI)** | AI models that can perform a wide range of tasks, as defined in the EU AI Act. |
| **Model card** | A standardized document reporting a model's intended use, performance metrics, and known limitations. |
| **Red teaming** | Adversarial testing of AI systems to identify potential harms, vulnerabilities, and failure modes. |
| **Value Sensitive Design (VSD)** | A design methodology that accounts for human values in a principled and systematic manner throughout the design process. |

---

*Note: This survey was compiled using the author's knowledge base through early 2025. URLs were provided based on known stable locations of referenced documents. Readers are encouraged to verify URLs and consult primary sources for the most current versions of cited works. Web-based search was unavailable during compilation; some very recent publications (late 2025--early 2026) may not be fully represented.*
