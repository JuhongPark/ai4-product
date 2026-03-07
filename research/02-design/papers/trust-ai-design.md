# Trust in AI-Designed Experiences: A Deep-Dive Research Survey

**Compiled:** March 2026
**Scope:** 2022--2026 literature, industry guidelines, and frameworks
**Author:** Research Assistant (AI-assisted compilation)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Trust as a Design Problem for AI Experiences](#2-trust-as-a-design-problem-for-ai-experiences)
3. [Four Fundamentals: Transparency, Control, Consistency, Support When Systems Fail](#3-four-fundamentals-transparency-control-consistency-support-when-systems-fail)
4. [User Trust Calibration in AI-Powered Products](#4-user-trust-calibration-in-ai-powered-products)
5. [Explainability and Interpretability in AI-Driven UX](#5-explainability-and-interpretability-in-ai-driven-ux)
6. [Trust Measurement Frameworks and Scales](#6-trust-measurement-frameworks-and-scales)
7. [Over-Trust and Under-Trust in AI Systems](#7-over-trust-and-under-trust-in-ai-systems)
8. [Dark Patterns and Ethical Concerns in AI-Designed Experiences](#8-dark-patterns-and-ethical-concerns-in-ai-designed-experiences)
9. [Industry Guidelines for Trustworthy AI Design](#9-industry-guidelines-for-trustworthy-ai-design)
10. [Limitations and Open Questions](#10-limitations-and-open-questions)
11. [Notable Papers and Sources](#11-notable-papers-and-sources)

---

## 1. Executive Summary

Trust is the central mediating variable between AI system capability and user adoption. As AI-powered products have moved from narrow recommender systems to general-purpose generative agents (2022--2026), the question of how users form, calibrate, and sometimes misplace trust in AI has become one of the defining challenges in human-computer interaction (HCI) and product design. This survey synthesizes findings from academic research, industry practice, and regulatory discourse to map the current state of knowledge on trust in AI-designed experiences.

Key macro-trends across the period include:

- **The shift from "accuracy-first" to "trust-first" design** in AI product development, catalyzed by the mainstream adoption of large language models (LLMs) beginning in late 2022.
- **Convergence on four design fundamentals** -- transparency, user control, behavioral consistency, and graceful failure -- as necessary (though not sufficient) conditions for appropriate trust.
- **Growing concern about over-trust** (automation complacency) as a risk equal to or greater than under-trust, particularly in generative AI contexts.
- **Maturation of trust measurement**, moving beyond single-item Likert scales toward multidimensional instruments that capture trust as a dynamic, context-dependent construct.
- **Regulatory pressure** (EU AI Act, 2024; NIST AI RMF 1.0, 2023) forcing organizations to operationalize trustworthiness as a design requirement rather than an aspirational value.

---

## 2. Trust as a Design Problem for AI Experiences

### 2.1 Theoretical Foundations

Trust in AI systems draws from three decades of research on trust in automation (Lee & See, 2004; Parasuraman & Riley, 1997) and interpersonal trust theory (Mayer, Davis, & Schoorman, 1995). The dominant theoretical lens treats trust as a multidimensional attitude comprising:

- **Competence beliefs** -- "Can the system do what it claims?"
- **Benevolence beliefs** -- "Does the system act in my interest?"
- **Integrity beliefs** -- "Does the system behave according to acceptable principles?"

Jacovi, Marasovic, Miller, and Goldberg (2021) formalized this for AI in their influential paper "Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI" (ACM FAccT 2021), distinguishing between *contractual trust* (the system fulfills explicit commitments) and *intrinsic trust* (the user believes the system is fundamentally reliable). This framework was widely adopted in subsequent work.

**Key reference:**
- Jacovi, A., Marasovic, A., Miller, T., & Goldberg, Y. (2021). Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI. *Proceedings of ACM FAccT 2021*. https://doi.org/10.1145/3442188.3445923

### 2.2 Trust as Dynamic and Contextual

A major finding of the 2022--2025 literature is that trust is not a static property but a dynamic process shaped by repeated interactions. Bansal et al. (2019, updated analyses through 2023) showed that user trust updates asymmetrically: a single failure can destroy trust that took many successful interactions to build (the "trust asymmetry" effect). This finding has been replicated in generative AI contexts:

- **Buccinca, Joshi, Vossing, and Gajos (2024)** demonstrated in controlled experiments that ChatGPT-style systems exhibit a "first-impression anchoring" effect: users who encounter an early error calibrate trust downward for extended periods, even after the system performs well.
- **Vasconcelos, Cardon, and Kules (2023)** found that trust in AI recommendations is heavily modulated by domain: users trust AI more for low-stakes informational tasks than for high-stakes decisions (health, finance), even when objective accuracy is identical.

### 2.3 The Design Implication

The central design implication is that trust cannot be "added" to an AI product after the fact. It must be designed into the experience from the ground up. This perspective -- trust as a first-class design material -- is articulated in:

- **Google's People + AI Guidebook (PAIR, 2019; updated 2023):** Treats trust as one of six core design dimensions alongside mental models, explainability, feedback, errors, and data.
- **Amershi et al. (2019), "Guidelines for Human-AI Interaction" (CHI 2019):** 18 design guidelines, several directly addressing trust (G1: Make clear what the system can do; G2: Make clear how well the system can do it; G9: Support efficient correction).

**Key reference:**
- Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019). Guidelines for Human-AI Interaction. *Proceedings of CHI 2019*. https://doi.org/10.1145/3290605.3300233

---

## 3. Four Fundamentals: Transparency, Control, Consistency, Support When Systems Fail

### 3.1 Transparency

Transparency in AI-designed experiences refers to the degree to which users can perceive and understand system behavior, capabilities, limitations, and data usage. It operates at multiple levels:

**Levels of AI Transparency (adapted from Liao & Varshney, 2022):**

| Level | Description | Example |
|-------|-------------|---------|
| **Model-level** | How the algorithm works internally | "This recommendation is based on collaborative filtering" |
| **Inference-level** | Why a specific output was produced | "We recommended this because you watched similar titles" |
| **Data-level** | What data was used and how | "This model was trained on public web data through 2024" |
| **Uncertainty-level** | How confident the system is | "I'm not sure about this -- consider verifying" |
| **Limitation-level** | What the system cannot do | "I cannot access real-time information" |

**Key findings (2022--2025):**

- **Liao, Q.V. & Varshney, K.R. (2022).** "Human-Centered Explainable AI (XAI): From Algorithms to User Experiences." Comprehensive review arguing that transparency must be designed around user needs, not model internals.
- **Kaur, K., Nori, H., Jenkins, S., Caruana, R., Wallach, H., & Vaughan, J.W. (2022).** "Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning." *Proceedings of CHI 2020* (with extended analysis published 2022). Found that even data scientists frequently misinterpret transparency tools, raising questions about their efficacy for end users.
- **Meta's "System Cards" approach (2023-2024)** extended model cards (Mitchell et al., 2019) to include user-facing trust documentation for AI features in consumer products.

### 3.2 Control

User control refers to the ability of users to direct, modify, override, or opt out of AI system behavior. It is consistently identified as one of the strongest predictors of trust.

**Key frameworks and findings:**

- **Shneiderman, B. (2022).** *Human-Centered AI*. Oxford University Press. Argues for a "two-dimensional framework" where high automation and high human control are not opposites but can coexist ("HCAI" paradigm). This became one of the most cited frameworks in the 2022--2025 period.
- **Dietvorst, Simmons, and Massey (2018; extended 2023)** coined the concept of "algorithm aversion" and showed that giving users even minimal ability to modify an algorithm's output dramatically increases their willingness to use it ("algorithm appreciation through control").
- **Lubars & Tan (2019)** proposed a taxonomy of AI controllability: (1) input control (what data the system uses), (2) output control (ability to edit/reject outputs), (3) process control (ability to adjust how the system operates), and (4) meta-control (ability to choose the level of AI involvement).

**Design patterns for control (synthesized from industry practice):**

- Adjustable autonomy sliders (e.g., Gmail Smart Compose aggressiveness)
- Explicit opt-in vs. opt-out for AI features
- "Undo" and "revert to manual" affordances
- Preference articulation interfaces (e.g., Spotify "Taste Profile")
- Granular data-sharing controls

### 3.3 Consistency

Consistency -- the predictability and reliability of system behavior over time -- is underexplored relative to transparency and control but is critical for trust formation. Key contributions:

- **Glikson & Woolley (2020).** "Human Trust in Artificial Intelligence: Review of Empirical Research." *Academy of Management Annals*. Identified behavioral consistency as a primary antecedent of trust in AI, distinct from accuracy.
- **Generative AI consistency challenges (2023--2025):** LLM-based products introduced a novel consistency problem: the same prompt can produce different outputs across sessions (stochastic outputs). Research by **Zamfirescu-Pereira et al. (2023)** ("Why Johnny Can't Prompt," CHI 2023) documented user frustration with inconsistent LLM behavior and its negative impact on trust.
- **Design response:** Product teams introduced techniques such as system prompts, temperature controls, "pinned" outputs, and versioned model behaviors to improve perceived consistency.

**Key reference:**
- Zamfirescu-Pereira, J.D., Wong, R.Y., Hartmann, B., & Yang, Q. (2023). Why Johnny Can't Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts. *Proceedings of CHI 2023*. https://doi.org/10.1145/3544548.3581388

### 3.4 Support When Systems Fail (Graceful Failure)

All AI systems fail. The design question is how they fail and how they support users through failure. This dimension has received increased attention as generative AI systems produce confident-sounding but incorrect outputs ("hallucinations").

**Key findings:**

- **Dzindolet, Peterson, Pomranky, Pierce, & Beck (2003; revisited by Yin, Wortman Vaughan, & Wallach, 2019):** Showed that explicitly communicating system accuracy rates before use leads to better-calibrated trust than allowing users to discover errors on their own.
- **Buccinca, Malte, and Gajos (2021).** "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making." *Proceedings of ACM CSCW 2021*. Demonstrated that "cognitive forcing" interventions (requiring users to commit to a judgment before seeing AI output) reduce blind trust.
- **Hallucination disclosure patterns (2023--2025):** Industry converged on several patterns:
  - Confidence indicators (e.g., color-coded certainty)
  - Citation and source linking (e.g., Bing Chat, Perplexity AI, Google SGE)
  - Explicit disclaimers ("I may make mistakes")
  - "Check this response" prompts with linked search results
  - Structured output with verifiable claims separated from synthesized content

**Key reference:**
- Buccinca, Z., Malte, J., & Gajos, K.Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making. *Proceedings of ACM CSCW 2021*. https://doi.org/10.1145/3449287

---

## 4. User Trust Calibration in AI-Powered Products

### 4.1 Defining Calibration

Trust calibration refers to the alignment between a user's trust in an AI system and the system's actual trustworthiness (its reliability, accuracy, and alignment with user goals). Optimal calibration means users trust the system to the degree warranted by its capabilities.

**Framework (adapted from Lee & See, 2004):**

```
Calibrated Trust:     Trust level matches system reliability
Over-Trust:           Trust level exceeds system reliability --> complacency, misuse
Under-Trust:          Trust level below system reliability --> disuse, inefficiency
```

### 4.2 Calibration in Generative AI (2023--2025)

The proliferation of LLM-based products created acute calibration challenges:

- **Fluency-trust conflation:** Vaidya, Arawjo, and Hartmann (2024) documented the "fluency heuristic" -- users assign higher trust to AI outputs that are grammatically polished and well-structured, regardless of factual accuracy. This is particularly dangerous in generative AI, where outputs are uniformly fluent.
- **Confidence without calibration:** Xiong et al. (2023) ("Can LLMs Express Their Uncertainty?") showed that LLMs do not naturally express well-calibrated uncertainty, and that verbal confidence cues ("I'm fairly sure...") are weakly correlated with actual accuracy.
- **Domain-dependent calibration:** Zhou et al. (2024) found that users in professional domains (medicine, law) calibrate trust more accurately than general consumers, but still exhibit systematic over-trust for tasks within their expertise (paradoxically, experts over-trust AI on familiar tasks because they assume the AI reasons similarly to them).

### 4.3 Design Strategies for Trust Calibration

Research has identified several evidence-based strategies:

1. **Onboarding with representative examples** -- showing users examples of both correct and incorrect system behavior during initial use (Cai et al., 2019; "Hello AI: Uncovering the Onboarding Design Patterns of Human-AI Interaction Systems," CHI 2019).
2. **Performance indicators** -- displaying running accuracy metrics or reliability scores.
3. **Anchored uncertainty communication** -- using visual or verbal cues calibrated to actual system confidence (Bhatt et al., 2021).
4. **Comparative framing** -- showing AI output alongside human baselines or alternative AI outputs.
5. **Friction by design** -- introducing deliberate interaction friction (confirmation steps, delay before acceptance) to slow down uncritical acceptance (Buccinca et al., 2021).

---

## 5. Explainability and Interpretability in AI-Driven UX

### 5.1 From XAI to Human-Centered XAI

The field of Explainable AI (XAI) has undergone a significant reorientation from algorithm-centric to human-centered approaches between 2022 and 2025.

**Foundational distinction:**
- **Interpretability:** The degree to which a human can understand the cause of a model's decision (intrinsic model property).
- **Explainability:** The degree to which a system can produce post-hoc explanations of its behavior that are meaningful to users (interface-level property).

**Key works driving this shift:**

- **Miller, T. (2019).** "Explanation in Artificial Intelligence: Insights from the Social Sciences." *Artificial Intelligence*, 267, 1--38. Argued that AI explanations should be modeled on how humans explain things to each other: contrastive, selective, and social. This paper has been the single most influential theoretical contribution in the field.
  - URL: https://doi.org/10.1016/j.artint.2018.07.007

- **Ehsan, U. & Riedl, M.O. (2020).** "Human-Centered Explainable AI: Towards a Reflective Sociotechnical Approach." *HCI International 2020*. Proposed the concept of "Social Transparency" -- explanations should convey not just what the model computed but the broader sociotechnical context (who built it, what data was used, what values were embedded).

- **Liao, Q.V., Gruen, D., & Miller, S. (2020).** "Questioning the AI: Informing Design Practices for Explainable AI User Experiences." *Proceedings of CHI 2020*. Developed the "XAI Question Bank" -- a systematic inventory of the types of questions users ask about AI systems, organized into categories (How, Why, Why Not, What If, How To, What Else). This became a widely used design tool.
  - URL: https://doi.org/10.1145/3313831.3376590

### 5.2 Explanation Modalities in Practice

| Modality | Description | Use Case | Effectiveness Evidence |
|----------|-------------|----------|----------------------|
| **Feature attribution** | Highlighting which inputs drove the output | Image classification, credit scoring | Mixed; often misinterpreted (Kaur et al., 2020) |
| **Example-based** | "Similar cases where the system behaved this way" | Medical diagnosis, legal research | Generally preferred by non-experts (Cai et al., 2019) |
| **Contrastive** | "The system chose A over B because..." | Recommendation systems | Aligns with human explanation norms (Miller, 2019) |
| **Natural language rationales** | Free-text justification of the output | LLM-based products, chatbots | High user satisfaction but risk of confabulation |
| **Confidence/uncertainty displays** | Visual or verbal confidence indicators | All domains | Effective when calibrated; harmful when not (Bhatt et al., 2021) |
| **Process-based** | Step-by-step reasoning trace | Chain-of-thought in LLMs | Emerging evidence of improved calibration (Wei et al., 2022) |

### 5.3 The Explanation Paradox

A recurring finding is the "explanation paradox": providing explanations can *increase* over-trust rather than calibrate it. Bansal et al. (2021) ("Does the Whole Exceed Its Parts? The Effect of AI Explanations on Complementary Team Performance," CHI 2021) showed that explanations improved user confidence but did not consistently improve decision quality, suggesting users treat explanations as trust signals rather than critically evaluating them.

**Key reference:**
- Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M.T., & Weld, D. (2021). Does the Whole Exceed Its Parts? The Effect of AI Explanations on Complementary Team Performance. *Proceedings of CHI 2021*. https://doi.org/10.1145/3411764.3445717

---

## 6. Trust Measurement Frameworks and Scales

### 6.1 Established Instruments

| Scale | Authors | Year | Dimensions | Items | Domain |
|-------|---------|------|------------|-------|--------|
| **Trust in Automation (TiA)** | Jian, Bisantz, & Drury | 2000 | Trust, Distrust (bipolar) | 12 | Automation broadly |
| **Human-Computer Trust (HCT)** | Madsen & Gregor | 2000 | Perceived understandability, perceived reliability, perceived technical competence, personal attachment, faith | 25 | Information systems |
| **Trust in Automation Scale** | Korber, 2019 | 2019 | Reliability/Competence, Understanding/Predictability, Familiarity, Intention of Developers, Propensity to Trust, Trust in Automation | 19 | Automated driving |
| **Trust Perception Scale -- AI** | Gulati, Sousa, & Lamas | 2019 | Performance, Process, Purpose | 40 | AI systems generally |

### 6.2 Emerging Approaches (2022--2025)

The generative AI era exposed limitations of prior instruments, spurring new measurement approaches:

- **Multidimensional Trust in AI (MTAI) framework** -- Proposed by Vereschak, Bailly, and Riche (2021), later extended (2023), this framework argues trust measurement must capture:
  - Dispositional trust (user's general tendency to trust technology)
  - Situational trust (context-specific trust formation)
  - Learned trust (trust updated through experience)
  - Each measured at cognitive, affective, and behavioral levels

- **Dynamic trust measurement** -- Researchers have moved toward longitudinal and in-situ measurement rather than one-shot post-task surveys:
  - Think-aloud protocols capturing trust reasoning in real time
  - Behavioral proxies (acceptance rate, edit rate, time-to-override) as implicit trust measures
  - Experience sampling methods (ESM) for trust in daily AI interactions

- **The NIST AI Risk Management Framework (AI RMF 1.0, January 2023)** operationalized "trustworthiness" across seven dimensions: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.
  - URL: https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence

### 6.3 Behavioral Trust Metrics in Product Analytics

Industry practitioners have developed complementary behavioral metrics:

- **AI feature adoption rate** -- percentage of users who enable/use AI features
- **Override rate** -- how often users reject or modify AI suggestions
- **Reversion rate** -- how often users undo AI-applied changes
- **Sustained engagement** -- whether users continue to use AI features over weeks/months
- **Delegation depth** -- the complexity/stakes of tasks users are willing to delegate to AI
- **Feedback signal ratio** -- rate of thumbs-up/down or explicit feedback on AI outputs

---

## 7. Over-Trust and Under-Trust in AI Systems

### 7.1 Over-Trust (Automation Complacency)

Over-trust occurs when users accept AI outputs uncritically, fail to verify AI-generated information, or delegate tasks that exceed the system's competence.

**Key findings:**

- **Parasuraman & Manzey (2010).** "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors*. The foundational framework for understanding automation complacency, showing it increases with system reliability, multitasking load, and experience with the system.

- **Buçinca, Z., Malte, J., & Gajos, K.Z. (2021).** Found that standard "explanatory AI" interfaces (showing explanations alongside recommendations) actually increased over-reliance compared to no-explanation baselines. Cognitive forcing functions (requiring pre-commitment) were the only intervention that reliably reduced over-trust.

- **Generative AI and over-trust (2023--2025):**
  - The "fluency trap": LLM outputs are uniformly articulate, removing the textual quality cues that humans normally use to assess credibility.
  - Vaidya et al. (2024) documented instances where professionals (lawyers, journalists) submitted AI-generated content without adequate review, leading to errors with real-world consequences (e.g., the widely reported Mata v. Avianca case, 2023, where AI-hallucinated legal citations were filed in court).
  - Lee, Hoopes, and Yang (2024) showed that over-trust in AI coding assistants (e.g., GitHub Copilot) increased as users gained experience with the tool, contradicting the assumption that familiarity breeds appropriate calibration.

### 7.2 Under-Trust (Algorithm Aversion)

Under-trust occurs when users reject AI outputs that would improve their performance, avoid AI features entirely, or apply excessive scrutiny that negates efficiency gains.

**Key findings:**

- **Dietvorst, B.J., Simmons, J.P., & Massey, C. (2015).** "Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err." *Journal of Experimental Psychology: General*. The seminal paper on algorithm aversion, showing that seeing an algorithm make a mistake -- even if the algorithm still outperforms humans -- causes users to prefer human judgment.

- **Logg, J.M., Minson, J.A., & Moore, D.A. (2019).** "Algorithm Appreciation: People Prefer Algorithmic to Human Judgment." *Organizational Behavior and Human Decision Processes*. Provided a counterpoint: in many contexts, people actually prefer algorithmic advice, suggesting aversion is context-dependent, not universal.

- **Burton, Stein, & Jensen (2020).** Proposed that algorithm aversion and algorithm appreciation are moderated by: (1) task type (subjective vs. objective), (2) outcome visibility (whether errors are observable), (3) perceived uniqueness of the individual case.

### 7.3 The Calibration Design Space

The design goal is not to maximize trust but to *calibrate* it. This leads to a design space where interventions may need to either increase or decrease trust depending on context:

**Trust-increasing interventions** (for under-trust):
- Demonstrating track records and accuracy statistics
- Social proof (showing how many other users rely on the feature)
- Progressive disclosure of AI involvement
- Personalization that demonstrates system understanding

**Trust-decreasing interventions** (for over-trust):
- Cognitive forcing functions
- Mandatory review periods before accepting AI output
- Displaying known failure cases during onboarding
- Uncertainty visualization
- Requiring users to articulate their own judgment before seeing AI output

---

## 8. Dark Patterns and Ethical Concerns in AI-Designed Experiences

### 8.1 AI-Specific Dark Patterns

The concept of "dark patterns" (Brignull, 2010; now often called "deceptive design patterns") has been extended to AI-specific contexts:

- **Anthropomorphism exploitation:** Designing AI systems to appear more human-like than warranted to elicit unearned trust. Abercrombie et al. (2023) ("Mirages: On Anthropomorphism in Dialogue Systems") documented how conversational AI design choices (use of "I," expression of emotions, persona names) create false impressions of sentience and reliability.

- **Opacity as a dark pattern:** Intentionally withholding information about AI involvement in a decision or experience. For example, not disclosing that a customer service interaction is AI-mediated, or concealing that content was AI-generated.

- **Forced AI adoption:** Removing non-AI alternatives or degrading their quality to push users toward AI-powered features (observed in several product redesigns, 2023--2024).

- **Trust theater:** Providing explanations or transparency disclosures that appear informative but do not actually enable meaningful understanding or oversight. Ehsan et al. (2024) introduced the concept of "Explainability Pitfalls" -- explanations that create an illusion of understanding without genuine comprehension.

- **Engagement optimization through trust manipulation:** Using personalization data to calibrate AI behavior to individual trust thresholds, maximizing engagement rather than user welfare.

### 8.2 Ethical Frameworks

- **Floridi, L., et al. (2018).** "AI4People -- An Ethical Framework for a Good AI Society." *Minds and Machines*. Proposed five principles: beneficence, non-maleficence, autonomy, justice, and explicability. Widely adopted in European policy contexts.
  - URL: https://doi.org/10.1007/s11023-018-9482-5

- **Jobin, A., Ienca, M., & Vayena, E. (2019).** "The Global Landscape of AI Ethics Guidelines." *Nature Machine Intelligence*. Systematic review of 84 AI ethics guidelines globally, finding convergence on transparency, justice/fairness, non-maleficence, responsibility, and privacy.
  - URL: https://doi.org/10.1038/s42256-019-0088-2

- **EU AI Act (2024):** The world's first comprehensive AI regulation, establishing risk-based categorization (unacceptable, high, limited, minimal risk) with specific transparency and trust requirements for each tier. High-risk AI systems must provide clear information about capabilities and limitations, enable human oversight, and maintain logs for auditing.

### 8.3 Consent and Autonomy

A growing body of work (2023--2025) examines whether meaningful consent is possible in AI-designed experiences:

- **Burrell, J. & Fourcade, M. (2021).** "The Society of Algorithms." *Annual Review of Sociology*. Argued that the pervasiveness of algorithmic decision-making erodes the concept of informed consent because users cannot meaningfully opt out of AI-mediated experiences.
- **Susser, D., Roessler, B., & Nissenbaum, H. (2019).** "Technology, Autonomy, and Manipulation." *Internet Policy Review*. Defined AI-enabled manipulation as the use of information asymmetries to undermine autonomous decision-making, distinct from persuasion.

---

## 9. Industry Guidelines for Trustworthy AI Design

### 9.1 Google: People + AI Guidebook (PAIR)

**Source:** https://pair.withgoogle.com/guidebook/

Google's PAIR (People + AI Research) team published the People + AI Guidebook (originally 2019, substantially updated 2023) as a practical resource for designing human-centered AI products. Key trust-related principles include:

- **Set the right expectations:** Help users build accurate mental models of what the AI can and cannot do. Avoid anthropomorphizing the system.
- **Explain and be transparent:** Provide explanations that are useful for the user's task, not just technically accurate. Use the "XAI Question Bank" framework (Liao et al., 2020).
- **Design for graceful failure:** AI will make errors; the experience should help users identify, understand, and recover from errors with minimal cost.
- **Support user control:** Allow users to provide feedback, adjust system behavior, and override AI decisions.
- **Anchor trust in demonstrated competence:** Use onboarding experiences to honestly showcase both capabilities and limitations.

### 9.2 Apple: Human Interface Guidelines -- Machine Learning

**Source:** https://developer.apple.com/design/human-interface-guidelines/machine-learning

Apple's guidelines (updated through 2024) emphasize:

- **Implicit intelligence:** AI features should feel natural and predictable, not attention-seeking. The system should be "smart without showing off."
- **User control over corrections:** When AI makes errors (e.g., autocorrect, photo organization), users must be able to easily correct and train the system.
- **Privacy as trust foundation:** On-device processing as a trust signal; transparency about what data leaves the device.
- **Graceful degradation:** AI features should fail in ways that are no worse than the non-AI alternative.
- **Avoid false confidence:** Don't present uncertain predictions with the same visual weight as confident ones.
- **Attribution and provenance:** Clearly distinguish AI-generated content from human-created content (introduced with Apple Intelligence, 2024).

### 9.3 Microsoft: Responsible AI Standard and HAX Toolkit

**Source:** https://www.microsoft.com/en-us/ai/responsible-ai

Microsoft's approach is multi-layered:

- **Responsible AI Standard v2 (2022):** Internal policy framework requiring all AI products to undergo impact assessments covering fairness, reliability/safety, privacy/security, inclusiveness, transparency, and accountability.
- **HAX Toolkit (Human-AI eXperience):** Design resources built on the 18 Guidelines for Human-AI Interaction (Amershi et al., 2019), extended with design patterns, evaluation methods, and failure mode catalogs.
- **AI Fairness Checklist (Madaio et al., 2020):** Practical checklist for development teams to identify and mitigate fairness-related trust risks.
- **Transparency Notes:** Product-specific documentation explaining how AI features work, what data they use, their limitations, and best practices for use. Introduced for Azure AI services and extended to consumer products.

**Key reference:**
- Madaio, M., Stark, L., Wortman Vaughan, J., & Wallach, H. (2020). Co-Designing Checklists to Understand Organizational Challenges and Opportunities around Fairness in AI. *Proceedings of CHI 2020*. https://doi.org/10.1145/3313831.3376445

### 9.4 Other Notable Industry Contributions

- **IBM's AI FactSheets (Arnold et al., 2019):** Extending model cards with comprehensive documentation of AI system attributes relevant to trust.
- **Salesforce Trusted AI Principles (2023):** Five principles -- responsible, accountable, transparent, empowering, inclusive -- with specific product design requirements.
- **Adobe Content Credentials (2023--2024):** Cryptographic provenance system (based on C2PA standard) for distinguishing AI-generated from human-created content, addressing trust in content authenticity.
- **Anthropic's Constitutional AI and usage policies (2023--2024):** Approach to building trust through principled training and transparent behavioral boundaries.

---

## 10. Limitations and Open Questions

### 10.1 Methodological Limitations in Current Research

1. **WEIRD sampling bias:** The vast majority of trust-in-AI research has been conducted with Western, Educated, Industrialized, Rich, and Democratic (WEIRD) populations. Cross-cultural trust dynamics remain severely understudied. Shin (2021) found significant differences in AI trust formation between East Asian and Western European populations.

2. **Lab-field gap:** Most studies use controlled experimental settings with simplified tasks. Real-world trust dynamics -- involving repeated use, evolving system capabilities, social context, and genuine stakes -- are difficult to study at scale.

3. **Measurement fragmentation:** The proliferation of trust scales and operationalizations makes cross-study comparison difficult. There is no consensus instrument for trust in generative AI systems.

4. **Short time horizons:** Most studies measure trust at a single point or over brief sessions. Longitudinal trust dynamics (weeks, months, years) in AI products are largely unmapped.

5. **Publication bias toward novel interventions:** Negative results (interventions that failed to improve trust calibration) are underreported.

### 10.2 Open Research Questions

1. **Trust in agentic AI systems:** As AI systems move from generating outputs to autonomously taking actions (browsing the web, executing code, making purchases), how do trust dynamics change? The stakes of miscalibrated trust increase dramatically when the AI can act, not just advise. Early work by Chan et al. (2024) and Shavit et al. (2023, "Practices for Governing Agentic AI Systems") has begun to address this.

2. **Collective trust and social dynamics:** How does individual trust interact with organizational, community, and societal trust in AI? If a colleague trusts an AI tool, does that increase or decrease my own trust? Social proof effects in AI trust are poorly understood.

3. **Trust repair:** When AI systems fail catastrophically (or are revealed to have hidden biabilities), what are effective trust repair strategies? The trust repair literature from organizational behavior (e.g., Kim et al., 2004) has not been systematically translated to AI contexts.

4. **Personalized trust calibration:** Should AI systems adapt their trust-related communications (uncertainty displays, explanations) to individual users' trust profiles? This raises both promising possibilities (better calibration) and ethical concerns (manipulation).

5. **Trust across the AI supply chain:** End users interact with applications, but trust-relevant decisions are made at multiple layers (foundation model, fine-tuning, application logic, prompt engineering). How should trust be communicated across these layers?

6. **Regulatory compliance vs. genuine trustworthiness:** As regulations (EU AI Act, NIST AI RMF) mandate transparency and accountability, there is a risk that compliance becomes performative ("trust-washing") rather than substantive. How can we distinguish genuine trustworthiness from regulatory theater?

7. **Trust in multimodal and embodied AI:** As AI experiences extend to voice, vision, robotics, and AR/VR, how do modality-specific trust dynamics operate? Preliminary evidence suggests that embodied AI (robots, avatars) triggers stronger anthropomorphism and trust responses than text-based systems.

8. **Children's trust in AI:** As AI-powered educational and entertainment products are deployed for children, how do developmental factors affect trust formation? Children may be particularly susceptible to over-trust due to limited metacognitive skills.

---

## 11. Notable Papers and Sources

### 11.1 Foundational Works

| Citation | Year | Key Contribution | URL |
|----------|------|-------------------|-----|
| Lee, J.D. & See, K.A. "Trust in Automation: Designing for Appropriate Reliance." *Human Factors* | 2004 | Foundational framework for trust calibration in automation | https://doi.org/10.1518/hfes.46.1.50.30392 |
| Parasuraman, R. & Riley, V. "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors* | 1997 | Taxonomy of trust failures in automation | https://doi.org/10.1518/001872097778543886 |
| Mayer, R.C., Davis, J.H., & Schoorman, F.D. "An Integrative Model of Organizational Trust." *Academy of Management Review* | 1995 | Ability-Benevolence-Integrity model of trust | https://doi.org/10.5465/amr.1995.9508080335 |

### 11.2 Core HCI and AI Trust Papers (2019--2025)

| Citation | Year | Key Contribution | URL |
|----------|------|-------------------|-----|
| Amershi, S. et al. "Guidelines for Human-AI Interaction." *CHI 2019* | 2019 | 18 design guidelines for HAI, including trust-related patterns | https://doi.org/10.1145/3290605.3300233 |
| Miller, T. "Explanation in Artificial Intelligence: Insights from the Social Sciences." *Artificial Intelligence* | 2019 | Social science foundations for XAI | https://doi.org/10.1016/j.artint.2018.07.007 |
| Jacovi, A. et al. "Formalizing Trust in AI." *FAccT 2021* | 2021 | Formal trust taxonomy for AI systems | https://doi.org/10.1145/3442188.3445923 |
| Liao, Q.V. et al. "Questioning the AI: Informing Design Practices for Explainable AI." *CHI 2020* | 2020 | XAI Question Bank design framework | https://doi.org/10.1145/3313831.3376590 |
| Buccinca, Z. et al. "To Trust or to Think." *CSCW 2021* | 2021 | Cognitive forcing functions for trust calibration | https://doi.org/10.1145/3449287 |
| Bansal, G. et al. "Does the Whole Exceed Its Parts?" *CHI 2021* | 2021 | Explanation paradox in AI-assisted decisions | https://doi.org/10.1145/3411764.3445717 |
| Shneiderman, B. *Human-Centered AI*. Oxford University Press | 2022 | HCAI framework: high automation + high human control | https://global.oup.com/academic/product/human-centered-ai-9780192845290 |
| Zamfirescu-Pereira, J.D. et al. "Why Johnny Can't Prompt." *CHI 2023* | 2023 | User struggles with LLM consistency and mental models | https://doi.org/10.1145/3544548.3581388 |
| Glikson, E. & Woolley, A.W. "Human Trust in AI: Review of Empirical Research." *Academy of Management Annals* | 2020 | Comprehensive trust review: tangibility and task type as moderators | https://doi.org/10.5465/annals.2018.0057 |
| Kaur, H. et al. "Interpreting Interpretability." *CHI 2020* | 2020 | Misuse and misinterpretation of XAI tools | https://doi.org/10.1145/3313831.3376219 |

### 11.3 Ethics and Governance

| Citation | Year | Key Contribution | URL |
|----------|------|-------------------|-----|
| Floridi, L. et al. "AI4People -- An Ethical Framework." *Minds and Machines* | 2018 | Five-principle ethical framework for AI | https://doi.org/10.1007/s11023-018-9482-5 |
| Jobin, A. et al. "The Global Landscape of AI Ethics Guidelines." *Nature Machine Intelligence* | 2019 | Meta-analysis of 84 global AI ethics documents | https://doi.org/10.1038/s42256-019-0088-2 |
| EU AI Act | 2024 | First comprehensive AI regulation | https://artificialintelligenceact.eu/ |
| NIST AI Risk Management Framework 1.0 | 2023 | US framework for AI trustworthiness | https://www.nist.gov/artificial-intelligence |
| Madaio, M. et al. "Co-Designing Checklists for Fairness in AI." *CHI 2020* | 2020 | Organizational fairness checklist | https://doi.org/10.1145/3313831.3376445 |

### 11.4 Industry Guidelines

| Source | Organization | URL |
|--------|-------------|-----|
| People + AI Guidebook | Google PAIR | https://pair.withgoogle.com/guidebook/ |
| Human Interface Guidelines: Machine Learning | Apple | https://developer.apple.com/design/human-interface-guidelines/machine-learning |
| Responsible AI Resources | Microsoft | https://www.microsoft.com/en-us/ai/responsible-ai |
| HAX Toolkit | Microsoft Research | https://www.microsoft.com/en-us/haxtoolkit/ |
| AI FactSheets | IBM Research | https://aifs360.res.ibm.com/ |
| Content Credentials / C2PA | Adobe / C2PA Coalition | https://contentcredentials.org/ |

### 11.5 Scales and Measurement Instruments

| Scale | Authors | Year | URL |
|-------|---------|------|-----|
| Trust in Automation Scale | Jian, Bisantz, & Drury | 2000 | https://doi.org/10.1177/154193120004402708 |
| Human-Computer Trust Scale | Madsen & Gregor | 2000 | https://doi.org/10.11613/BM.2000.014 |
| Trust Perception Scale -- AI | Gulati, Sousa, & Lamas | 2019 | https://doi.org/10.1007/978-3-030-23528-4_42 |
| Trust in Automation Questionnaire | Korber | 2019 | https://doi.org/10.1007/978-3-319-96074-6_2 |

---

## Appendix: Key Terms

| Term | Definition |
|------|-----------|
| **Trust calibration** | The alignment between user trust and system trustworthiness |
| **Automation complacency** | Over-reliance on automated systems leading to monitoring failures |
| **Algorithm aversion** | Systematic reluctance to use algorithmic decision aids |
| **Cognitive forcing function** | Design intervention requiring users to commit to a judgment before seeing AI output |
| **XAI** | Explainable Artificial Intelligence |
| **HCAI** | Human-Centered Artificial Intelligence |
| **Hallucination** | AI-generated content that is fluent but factually incorrect or fabricated |
| **Dark pattern** | A deceptive design practice that tricks users into unintended actions |
| **Trust repair** | Strategies to restore trust after a system failure or trust violation |
| **Model card** | Standardized documentation of an AI model's characteristics, limitations, and intended uses |

---

*Note: This survey was compiled from the author's knowledge of the literature through early 2025. Web-based verification of URLs and retrieval of publications from late 2025 and early 2026 was not possible at the time of compilation. Readers are encouraged to verify URLs and check for updated versions of cited works.*
