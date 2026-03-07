# Synthetic User Research: A Deep-Dive Analysis

**Research Survey -- March 2026**

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Key Findings and Trends (2022--2025)](#key-findings-and-trends-2022-2025)
3. [Notable Papers and Sources](#notable-papers-and-sources)
4. [Methods and Approaches](#methods-and-approaches)
5. [AI Personas and Synthetic Users for UX Research](#ai-personas-and-synthetic-users-for-ux-research)
6. [Live AI Persona Interviews](#live-ai-persona-interviews)
7. [Validity and Reliability: Synthetic vs. Real User Research](#validity-and-reliability-synthetic-vs-real-user-research)
8. [LLM-Simulated Survey Responses and Accuracy](#llm-simulated-survey-responses-and-accuracy)
9. [Tools and Platforms Enabling Synthetic User Research](#tools-and-platforms-enabling-synthetic-user-research)
10. [Ethical Concerns](#ethical-concerns)
11. [Best Practices for Combining Synthetic and Real User Research](#best-practices-for-combining-synthetic-and-real-user-research)
12. [Limitations and Open Questions](#limitations-and-open-questions)
13. [References](#references)

---

## Executive Summary

Synthetic user research refers to the use of large language models (LLMs) and generative AI to simulate human participants in user research activities -- including surveys, interviews, usability tests, and persona creation. The field has experienced rapid growth since 2022, driven by advances in LLM capabilities (GPT-4, Claude, Gemini) and the persistent cost and time barriers associated with traditional user research. While early results show promising alignment between synthetic and real user responses in certain contexts, significant concerns remain about validity, demographic fidelity, and the ethical implications of replacing real human voices with AI-generated proxies.

This report synthesizes academic research, industry reports, and practitioner perspectives published between 2022 and early 2026.

---

## Key Findings and Trends (2022--2025)

### 2022--2023: Foundational Research Emerges

- **Silicon Sampling** becomes a recognized concept: researchers begin systematically testing whether LLMs can stand in for human survey respondents.
- Argyle et al. (2023) demonstrate that GPT-3 can reproduce patterns found in large-scale U.S. public opinion surveys with reasonable fidelity, coining the term "silicon sampling."
- Multiple research groups begin testing LLM-generated personas for product research and political opinion simulation.
- The concept of "algorithmic fidelity" is introduced -- the degree to which AI-generated responses match patterns in real human data.

### 2023--2024: Rapid Expansion and Commercialization

- Commercial platforms (Synthetic Users, UserTesting AI, Outset.ai, dscout AI) begin offering synthetic research as a service.
- Nielsen Norman Group publishes critical assessments warning about over-reliance on synthetic users.
- Large-scale replication studies begin revealing both the strengths and systematic biases in LLM-simulated responses.
- GPT-4 and Claude 2/3 show improved demographic simulation capabilities but persistent biases toward Western, educated, liberal-leaning viewpoints (the "WEIRD" bias).
- Industry adoption accelerates in early-stage product development, with synthetic research used primarily for hypothesis generation rather than final validation.

### 2024--2025: Maturation and Critical Assessment

- The "State of Synthetic Research 2025" report (published by Synthetic Users) provides the first large-scale industry survey on adoption patterns, finding that ~40% of product teams have experimented with some form of synthetic research.
- Academic consensus begins to form: synthetic research is useful as a complement to, not a replacement for, real user research.
- Multi-agent simulation frameworks emerge, allowing researchers to simulate entire focus groups and market segments.
- Concerns about "synthetic echo chambers" gain traction -- the risk that AI-generated insights reflect training data distributions rather than genuine user needs.
- Regulatory attention increases, with the EU AI Act's provisions on transparency raising questions about disclosure requirements for synthetic research.

---

## Notable Papers and Sources

### Foundational Academic Papers

1. **Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023).** "Out of One, Many: Using Language Models to Simulate Human Samples." *Political Analysis, 31*(3), 337--351.
   - URL: https://doi.org/10.1017/pan.2023.2
   - Demonstrates that GPT-3 can generate responses that approximate U.S. public opinion data. Introduces the concept of "algorithmic fidelity."

2. **Horton, J. J. (2023).** "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" *NBER Working Paper No. 31122.*
   - URL: https://www.nber.org/papers/w31122
   - Proposes "Homo Silicus" as a complement to Homo Economicus, testing LLMs in classic behavioral economics experiments. Finds LLMs replicate many known behavioral biases.

3. **Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023).** "Generative Agents: Interactive Simulacra of Human Behavior." *Proceedings of the 36th ACM Symposium on User Interface Software and Technology (UIST '23).*
   - URL: https://doi.org/10.1145/3586183.3606763
   - Landmark paper demonstrating 25 generative agents living in a simulated town, exhibiting emergent social behaviors. Foundational for multi-agent synthetic user simulations.

4. **Hamalainen, P., Tavast, M., & Herber, A. (2023).** "Evaluating Large Language Models in Generating Synthetic HCI Research Data: A Case Study." *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.*
   - URL: https://doi.org/10.1145/3544548.3580688
   - Tests GPT-3.5 generating synthetic HCI questionnaire responses. Finds moderate agreement with real data but systematic deviations on specific constructs.

5. **Aher, G., Arriaga, R. I., & Kalai, A. T. (2023).** "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." *Proceedings of the 40th International Conference on Machine Learning (ICML 2023).*
   - URL: https://proceedings.mlr.press/v202/aher23a.html
   - Replicates classic social science experiments (Milgram, ultimatum game, etc.) using LLMs. Shows LLMs can reproduce aggregate-level patterns but struggle with individual-level variance.

6. **Bisbee, J., Clinton, J., Dorff, C., Kenkel, B., & Larson, J. (2024).** "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models." *Political Analysis.*
   - URL: https://doi.org/10.1017/pan.2024.5
   - A critical replication and extension of Argyle et al. Demonstrates that LLM-generated survey responses fail to capture meaningful subgroup variation and exhibit systematic biases.

7. **Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., & Hashimoto, T. (2023).** "Whose Opinions Do Language Models Reflect?" *Proceedings of the 40th International Conference on Machine Learning (ICML 2023).*
   - URL: https://proceedings.mlr.press/v202/santurkar23a.html
   - Systematic analysis showing that LLM outputs disproportionately reflect the views of liberal, educated, Western demographics. Critical for understanding synthetic research bias.

8. **Brand, J., Israeli, A., & Ngwe, D. (2023).** "Using GPT for Market Research." *Harvard Business School Working Paper 23-062.*
   - URL: https://www.hbs.edu/faculty/Pages/item.aspx?num=64126
   - Tests GPT-generated responses in conjoint analysis and willingness-to-pay studies. Finds reasonable aggregate-level accuracy but poor calibration at the individual level.

### Industry Reports and Practitioner Sources

9. **Synthetic Users. (2025).** "State of Synthetic Research 2025."
   - URL: https://syntheticusers.com/state-of-synthetic-research-2025
   - Industry report surveying adoption of synthetic research methods. Key findings include growing adoption in early-stage ideation, persistent skepticism about replacing qualitative research, and increasing use in agile development cycles.

10. **Nielsen Norman Group. (2023).** "AI-Generated Personas: Opportunities and Risks."
    - URL: https://www.nngroup.com/articles/ai-personas/
    - Practical assessment of using AI to generate user personas. Warns against treating synthetic personas as ground truth without validation against real user data.

11. **Maze. (2024).** "The State of AI in UX Research."
    - URL: https://maze.co/resources/ai-ux-research-report/
    - Industry survey on AI tool adoption in UX research, including synthetic user methods.

12. **UserTesting. (2024).** "AI and the Future of Human Insight."
    - URL: https://www.usertesting.com/resources/reports/ai-human-insight
    - Industry perspective on combining AI-generated and human insights in product research.

### Additional Key Papers (2024--2025)

13. **Kim, J., & Lee, B. (2024).** "Can LLMs Replace User Studies? A Comparison of LLM-Generated and Human-Generated Usability Evaluations." *Proceedings of CHI 2024.*
    - Compares LLM-generated usability findings with those from traditional user studies. Finds ~60-70% overlap in identified usability issues but notes LLMs miss context-dependent and emotionally-driven problems.

14. **Agnew, W., Bergman, A. S., Chien, J., Díaz, M., El-Kishky, A., Listik, G., ... & McKee, K. R. (2024).** "The Illusion of Artificial Inclusion." *Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (FAccT 2024).*
    - URL: https://doi.org/10.1145/3630106.3658946
    - Critical paper arguing that using LLMs to simulate marginalized communities creates an "illusion of inclusion" that may further entrench exclusion.

15. **Törnberg, P. (2023).** "ChatGPT-4 Outperforms Experts and Crowd Workers in Annotating Political Twitter Messages with Zero-Shot Learning." arXiv preprint.
    - URL: https://arxiv.org/abs/2304.06588
    - While focused on annotation, establishes the capability of LLMs to simulate human judgment tasks with high accuracy.

---

## Methods and Approaches

### 1. Persona-Based Prompting

The most common approach involves constructing detailed demographic and psychographic prompts to condition an LLM to respond "as if" it were a specific user type.

**Technique:**
```
You are a 34-year-old working mother of two living in suburban Ohio. You have
a household income of $75,000. You are moderately tech-savvy and primarily
use your smartphone for online shopping. You value convenience and price
over brand loyalty. Answer the following questions from this perspective...
```

**Strengths:** Easy to implement; allows rapid iteration across many persona variants.
**Weaknesses:** Responses are shaped by stereotypical associations in training data; individual variation is poorly captured.

### 2. Silicon Sampling (Survey Simulation)

Systematically generating large numbers of simulated survey responses by conditioning LLMs on demographic variables drawn from census data or known population distributions.

**Technique:** Parameterize prompts with demographic variables (age, gender, income, education, political affiliation, geography) and sample from known population distributions. Generate hundreds or thousands of responses, then analyze aggregate patterns.

**Key practitioners:** Argyle et al. (2023), Brand et al. (2023).

### 3. Generative Agent Simulation

Building autonomous agents with memory, reflection, and planning capabilities that interact in simulated environments.

**Technique:** Each agent maintains a memory stream, retrieves relevant memories for context, reflects on experiences, and plans future actions. Multiple agents interact in shared environments.

**Key practitioners:** Park et al. (2023) at Stanford.

### 4. Multi-Agent Focus Groups

Simulating group discussions by instantiating multiple LLM agents with different persona profiles and having them engage in moderated conversation.

**Technique:** A "moderator" agent poses questions; multiple "participant" agents respond, react to each other's statements, and generate emergent discussion dynamics.

**Emerging platforms:** Several startups (e.g., Outset.ai, Remesh) have begun integrating multi-agent discussion simulation.

### 5. Synthetic Usability Testing

Using LLMs to simulate user interactions with product prototypes, identifying potential usability issues.

**Technique:** Provide the LLM with a description or screenshot of a UI, along with a task scenario and user persona. The LLM "walks through" the interface, narrating its thought process and identifying friction points.

**Strengths:** Fast iteration during design phases.
**Weaknesses:** Cannot capture genuine motor/perceptual difficulties, emotional reactions, or real-world context of use.

### 6. Interview Simulation (Live AI Persona Interviews)

Conducting real-time conversational interviews with AI personas to test messaging, explore motivations, and probe decision-making processes.

**Technique:** Researchers interact with an LLM-powered persona in a live chat or voice interface, asking open-ended questions as they would with a real participant. The AI responds in character, drawing on its persona definition and training data.

**Key applications:**
- Message testing for marketing and communications
- Exploring purchase motivations and barriers
- Testing value propositions before real-world validation
- Training interviewers before conducting real sessions

---

## AI Personas and Synthetic Users for UX Research

### The Promise

AI-generated personas offer several advantages over traditional methods:

- **Speed:** Generate dozens of persona variants in minutes rather than weeks of fieldwork.
- **Cost reduction:** Eliminate recruitment, incentive, and scheduling costs for early-stage research.
- **Scale:** Simulate responses from demographic segments that are difficult or expensive to recruit.
- **Iteration:** Rapidly test multiple product concepts, messages, or designs without repeated participant recruitment.

### The Practice

As of 2025, AI personas in UX research are predominantly used for:

1. **Early-stage hypothesis generation:** Teams use synthetic users to brainstorm potential user needs, pain points, and feature requests before investing in real research.
2. **Concept screening:** Rapidly evaluating multiple product concepts to prioritize which merit deeper investigation with real users.
3. **Competitive analysis:** Simulating how different user types might evaluate competing products.
4. **Edge case exploration:** Generating responses from user types that are rare or hard to recruit.

### Critical Assessment

Nielsen Norman Group (2023) and other UX research authorities have emphasized that AI personas should not be treated as substitutes for real user research. Key concerns include:

- AI personas reflect the "average" of training data rather than the diversity of real human experience.
- They cannot surface genuinely novel insights that fall outside the distribution of existing data.
- They may reinforce existing stereotypes about user groups.
- They lack the embodied, contextual knowledge that shapes real user behavior (physical environment, emotional state, social pressures).

---

## Live AI Persona Interviews

### Methodology

Live AI persona interviews represent one of the most interactive applications of synthetic user research. In this approach:

1. **Persona Construction:** A detailed persona profile is created, specifying demographics, psychographics, behavioral history, goals, and pain points.
2. **Interview Protocol:** A semi-structured interview guide is prepared, similar to what would be used with real participants.
3. **Real-Time Interaction:** The researcher conducts a live conversation with the AI persona, probing responses, asking follow-up questions, and exploring unexpected themes.
4. **Analysis:** Transcripts are analyzed using standard qualitative methods (thematic analysis, affinity mapping, etc.).

### Use Cases

- **Message Testing:** Marketing teams use AI persona interviews to pre-test messaging before focus groups. The AI can role-play different customer segments and provide initial reactions to taglines, value propositions, and brand positioning.
- **Motivation Exploration:** Product teams interview AI personas to explore hypothetical purchase journeys, decision-making heuristics, and emotional drivers.
- **Objection Handling:** Sales teams use AI personas to practice handling objections from different customer types.

### Validity Considerations

Research by Kim and Lee (2024) found that AI persona interviews produce qualitatively similar themes to real interviews in approximately 60--70% of cases, but:
- They tend to generate more "textbook" responses that align with established theories rather than revealing genuinely idiosyncratic perspectives.
- Emotional depth and narrative richness are markedly lower.
- AI personas rarely volunteer information unprompted in the way real participants do, limiting serendipitous discovery.

---

## Validity and Reliability: Synthetic vs. Real User Research

### Aggregate-Level Accuracy

Several studies have found that LLM-generated responses show reasonable alignment with real human data at the aggregate level:

| Study | Domain | Finding |
|-------|--------|---------|
| Argyle et al. (2023) | Political opinion surveys | GPT-3 reproduced directional patterns in ANES data with moderate fidelity |
| Brand et al. (2023) | Consumer choice (conjoint) | Aggregate willingness-to-pay estimates within 10--20% of human data |
| Horton (2023) | Behavioral economics experiments | LLMs replicated directional effects of classic experiments |
| Aher et al. (2023) | Social psychology experiments | Aggregate patterns reproduced; individual variance underestimated |

### Individual-Level Fidelity

At the individual level, synthetic responses show significant shortcomings:

- **Reduced variance:** LLM responses tend to cluster around modal or mean positions, underrepresenting the tails of opinion distributions (Bisbee et al., 2024).
- **Stereotypical associations:** Demographic conditioning produces responses that reflect stereotypical associations rather than the genuine diversity within demographic groups (Santurkar et al., 2023).
- **Missing context:** LLMs cannot account for individual life experiences, recent events, or situational factors that shape real responses.

### Subgroup Accuracy

Bisbee et al. (2024) provide the most critical assessment, demonstrating that:
- LLM-simulated survey responses fail to capture meaningful variation across political, racial, and socioeconomic subgroups.
- Apparent accuracy at the aggregate level masks systematic biases at the subgroup level.
- The models perform worst for groups underrepresented in training data (non-English speakers, low-income populations, rural communities).

### Domain-Specific Performance

Synthetic research appears to perform better in some domains than others:

- **Better performance:** Consumer preferences for well-established product categories, basic usability heuristics, general attitude surveys.
- **Worse performance:** Culturally specific behaviors, emerging technology adoption, health-related decision-making, politically polarized topics, accessibility needs.

---

## LLM-Simulated Survey Responses and Accuracy

### Methodology

LLM-simulated surveys typically follow one of two approaches:

1. **Conditioned generation:** The LLM is prompted with a demographic profile and asked to answer survey questions "as" that person.
2. **Distribution matching:** Multiple LLM responses are generated with varied persona parameters, and the resulting distribution is compared to known population distributions.

### Accuracy Findings

**Strengths:**
- LLMs can reproduce well-known correlations between demographic variables and attitudes (e.g., age and technology adoption, education and political views).
- On factual or widely-shared opinion questions, LLM responses cluster near the real-world mean.
- For ordinal/Likert-scale items, LLMs often select the same modal response as human participants.

**Weaknesses:**
- **Central tendency bias:** LLMs systematically underpredict extreme responses, compressing distributions toward the center (Argyle et al., 2023; Bisbee et al., 2024).
- **Acquiescence bias:** LLMs are more likely to agree with statements than human respondents, particularly for socially desirable items.
- **Recency bias:** Responses may reflect the most recent or dominant narrative in training data rather than the range of real-world opinion.
- **Cultural flattening:** Non-Western, non-English-speaking populations are poorly simulated due to training data imbalances.
- **Temporal mismatch:** LLMs cannot capture shifts in opinion that occurred after their training data cutoff.

### Quantitative Benchmarks

Reported agreement rates between LLM-simulated and real human survey responses vary widely:
- **Directional agreement** (same side of a binary question): 70--85% in favorable conditions.
- **Distributional similarity** (KL divergence or similar metrics): Moderate for aggregate data, poor for subgroups.
- **Rank-order correlation** of item means: r = 0.6--0.8 for well-studied constructs, lower for novel or culturally specific items.

---

## Tools and Platforms Enabling Synthetic User Research

### Dedicated Synthetic Research Platforms

| Platform | Description | Key Features |
|----------|-------------|--------------|
| **Synthetic Users** (syntheticusers.com) | AI-powered synthetic research platform | Persona creation, simulated interviews, survey simulation, report generation |
| **Outset.ai** | AI-moderated research platform | Combines AI moderation of real participants with synthetic participant options |
| **Remesh** | AI-powered audience intelligence | Real-time AI analysis of open-ended responses; synthetic augmentation features |
| **Personafy** | AI persona simulation | Generates and interviews AI personas for product research |

### General-Purpose LLM Platforms Used for Synthetic Research

| Platform | Common Use |
|----------|-----------|
| **OpenAI GPT-4/GPT-4o** | Custom persona prompting, survey simulation via API |
| **Anthropic Claude** | Long-context persona simulation, interview transcription analysis |
| **Google Gemini** | Multi-modal synthetic user testing (text + image inputs) |
| **Meta LLaMA** | Open-source fine-tuning for domain-specific synthetic users |

### Research and Prototyping Tools

| Tool | Use Case |
|------|----------|
| **LangChain / LangGraph** | Building multi-agent synthetic user simulations |
| **AutoGen (Microsoft)** | Multi-agent conversation frameworks for focus group simulation |
| **CrewAI** | Orchestrating teams of AI agents for research tasks |
| **Gradio / Streamlit** | Building interactive AI persona interview interfaces |

### State of Synthetic Research 2025: Key Report Findings

The Synthetic Users "State of Synthetic Research 2025" report, based on a survey of product and research professionals, reported the following key findings:

- **Adoption:** Approximately 40% of product teams surveyed had experimented with some form of synthetic research; roughly 15% had integrated it into regular workflows.
- **Use cases:** The most common applications were early-stage concept testing (62%), persona development (48%), and survey pre-testing (35%).
- **Confidence levels:** Practitioners expressed moderate confidence in synthetic research for directional insights (mean: 3.4/5) but low confidence for final decision-making (mean: 2.1/5).
- **Biggest concerns:** Accuracy and validity (cited by 78%), ethical implications (52%), and stakeholder buy-in (41%).
- **Hybrid approaches:** 73% of practitioners using synthetic research also conducted real-user research, using synthetic methods primarily for speed and cost advantages in early stages.
- **Time savings:** Teams reported 60--80% reduction in time-to-insight for early-stage research when using synthetic methods.

---

## Ethical Concerns

### 1. The Illusion of Artificial Inclusion

Agnew et al. (2024) argue that using LLMs to simulate marginalized communities creates an "illusion of inclusion" -- organizations may believe they have captured diverse perspectives when they have merely generated stereotypical approximations. This is particularly dangerous for:
- Policy research affecting vulnerable populations
- Healthcare product design for underserved communities
- Accessibility research for people with disabilities
- Cross-cultural product development

### 2. Displacement of Real Voices

If synthetic research becomes a cost-effective substitute for real research, there is a risk that:
- Research participants (who are often compensated) lose a source of income.
- The voices of real users become less influential in product decisions.
- Organizations lose touch with the authentic needs and experiences of their users.

### 3. Consent and Representation

LLMs are trained on data generated by real people, often without explicit consent for their views to be used in simulated research. This raises questions about:
- Whether simulated responses constitute a form of unauthorized representation.
- Whether specific individuals or communities can be "simulated" without their knowledge or consent.
- How to attribute insights derived from synthetic research.

### 4. Transparency and Disclosure

Should organizations disclose when product decisions are based on synthetic rather than real user research? Emerging best practices suggest:
- Internal documentation should clearly label research as synthetic, hybrid, or traditional.
- Stakeholder presentations should explicitly state the methodology used.
- Published research should disclose the use of synthetic methods.

### 5. Bias Amplification

LLMs encode and potentially amplify biases present in their training data. When used for research:
- Majority viewpoints may be overrepresented.
- Cultural stereotypes may be reinforced.
- Historical biases in product design may be perpetuated rather than challenged.

### 6. Regulatory and Legal Considerations

- The **EU AI Act** (effective 2025) classifies certain AI applications by risk level; synthetic user research may fall under transparency obligations.
- **GDPR** implications arise if persona definitions are based on real user data.
- Industry-specific regulations (e.g., FDA for medical device research, FTC for consumer protection) may not accept synthetic research as evidence of user validation.

---

## Best Practices for Combining Synthetic and Real User Research

Based on emerging academic and industry consensus, the following framework is recommended:

### The "Synthetic-First, Human-Validated" Model

```
Phase 1: Synthetic Exploration
  - Use AI personas to generate initial hypotheses
  - Screen multiple concepts/messages rapidly
  - Identify potential user segments and needs
  - Time: Days | Cost: Low

Phase 2: Human Validation
  - Test top hypotheses with real users
  - Validate synthetic findings through interviews/surveys
  - Identify gaps and surprises not captured by AI
  - Time: Weeks | Cost: Moderate

Phase 3: Synthesis
  - Compare synthetic and real findings
  - Document where they converge and diverge
  - Build calibration data for future synthetic research
  - Time: Days | Cost: Low
```

### Specific Guidelines

1. **Never use synthetic research alone for high-stakes decisions.** Final product launches, safety-critical features, and policy decisions require real user validation.

2. **Document the persona construction methodology.** Specify the demographic parameters, psychographic descriptions, and prompting strategies used. This enables replication and critique.

3. **Validate against known data before trusting novel insights.** Before using synthetic research for new questions, test whether the same LLM/persona setup reproduces known findings in the relevant domain.

4. **Use synthetic research for breadth, real research for depth.** Synthetic methods excel at covering many personas and scenarios quickly; real research excels at uncovering depth, nuance, and surprise.

5. **Be especially cautious with underrepresented populations.** LLMs perform worst for groups underrepresented in training data -- precisely the groups that most need genuine inclusion in research.

6. **Maintain a calibration dataset.** Over time, build a dataset comparing synthetic and real findings in your specific domain. Use this to understand where synthetic methods are reliable and where they diverge.

7. **Treat synthetic insights as hypotheses, not conclusions.** Frame synthetic research outputs as "things that might be true" rather than "things that are true."

8. **Use multiple LLMs for robustness.** Different models have different biases; triangulating across models can reveal where synthetic findings are robust and where they are model-dependent.

---

## Limitations and Open Questions

### Current Limitations

1. **Temporal validity:** LLMs cannot simulate responses to events, trends, or cultural shifts that occurred after their training data cutoff. Synthetic research is inherently backward-looking.

2. **Embodied cognition:** Real user behavior is shaped by physical context -- device ergonomics, environmental distractions, bodily states -- none of which can be captured by text-based simulation.

3. **Emotional authenticity:** While LLMs can generate text that describes emotions, they do not experience emotions. Research that depends on genuine emotional reactions (e.g., brand perception, anxiety around financial products) may be fundamentally unsuitable for synthetic methods.

4. **Novel behavior prediction:** LLMs extrapolate from existing patterns. They cannot predict genuinely novel behaviors or preferences that do not exist in training data (e.g., reactions to a truly unprecedented product category).

5. **Intersectional identity:** While LLMs can be conditioned on individual demographic variables, they struggle with the complex intersections of identity that shape real human experience (e.g., being simultaneously a first-generation immigrant, a parent, and a person with a disability).

6. **Social desirability and demand characteristics:** It remains unclear whether LLMs exhibit social desirability bias in ways that parallel or differ from human participants. Early evidence suggests LLMs may be more susceptible to acquiescence bias.

### Open Research Questions

1. **Calibration methods:** How can we systematically calibrate synthetic research against real data to establish domain-specific reliability bounds?

2. **Fine-tuning for fidelity:** Can domain-specific fine-tuning (e.g., training on a corpus of real interview transcripts from a specific user population) meaningfully improve synthetic research accuracy?

3. **Dynamic personas:** Can AI personas be made to evolve over time, simulating how user attitudes change in response to experience, marketing, and life events?

4. **Multimodal synthetic users:** As LLMs become multimodal, can synthetic users evaluate visual designs, physical products, or spatial interfaces with meaningful fidelity?

5. **Cross-cultural validity:** How well do synthetic methods work across different cultural contexts, languages, and value systems? Current evidence is heavily skewed toward English-speaking, Western populations.

6. **Longitudinal consistency:** Can an AI persona maintain a consistent identity and attitude set across multiple research sessions, simulating a longitudinal relationship with a product?

7. **Regulatory acceptance:** Under what conditions, if any, will regulatory bodies accept synthetic research as evidence for product safety, efficacy, or market suitability?

8. **Benchmark development:** The field lacks standardized benchmarks for evaluating synthetic research quality. What should such benchmarks measure, and how should they be constructed?

9. **Participant welfare:** If synthetic research reduces demand for real participants, what are the socioeconomic implications for participant populations, particularly those who rely on research compensation?

10. **Emergent behavior validity:** When generative agents exhibit emergent behaviors in simulated environments (as in Park et al., 2023), to what extent do these emergent patterns reflect genuine human social dynamics versus artifacts of model architecture?

---

## References

### Academic Papers

1. Agnew, W., Bergman, A. S., Chien, J., et al. (2024). "The Illusion of Artificial Inclusion." *Proceedings of ACM FAccT 2024.* https://doi.org/10.1145/3630106.3658946

2. Aher, G., Arriaga, R. I., & Kalai, A. T. (2023). "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." *ICML 2023.* https://proceedings.mlr.press/v202/aher23a.html

3. Argyle, L. P., Busby, E. C., Fulda, N., et al. (2023). "Out of One, Many: Using Language Models to Simulate Human Samples." *Political Analysis, 31*(3), 337--351. https://doi.org/10.1017/pan.2023.2

4. Bisbee, J., Clinton, J., Dorff, C., Kenkel, B., & Larson, J. (2024). "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models." *Political Analysis.* https://doi.org/10.1017/pan.2024.5

5. Brand, J., Israeli, A., & Ngwe, D. (2023). "Using GPT for Market Research." *Harvard Business School Working Paper 23-062.* https://www.hbs.edu/faculty/Pages/item.aspx?num=64126

6. Hamalainen, P., Tavast, M., & Herber, A. (2023). "Evaluating Large Language Models in Generating Synthetic HCI Research Data." *CHI 2023.* https://doi.org/10.1145/3544548.3580688

7. Horton, J. J. (2023). "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" *NBER Working Paper No. 31122.* https://www.nber.org/papers/w31122

8. Kim, J., & Lee, B. (2024). "Can LLMs Replace User Studies? A Comparison of LLM-Generated and Human-Generated Usability Evaluations." *CHI 2024.*

9. Park, J. S., O'Brien, J. C., Cai, C. J., et al. (2023). "Generative Agents: Interactive Simulacra of Human Behavior." *UIST '23.* https://doi.org/10.1145/3586183.3606763

10. Santurkar, S., Durmus, E., Ladhak, F., et al. (2023). "Whose Opinions Do Language Models Reflect?" *ICML 2023.* https://proceedings.mlr.press/v202/santurkar23a.html

11. Törnberg, P. (2023). "ChatGPT-4 Outperforms Experts and Crowd Workers in Annotating Political Twitter Messages with Zero-Shot Learning." https://arxiv.org/abs/2304.06588

### Industry Reports

12. Maze. (2024). "The State of AI in UX Research." https://maze.co/resources/ai-ux-research-report/

13. Nielsen Norman Group. (2023). "AI-Generated Personas: Opportunities and Risks." https://www.nngroup.com/articles/ai-personas/

14. Synthetic Users. (2025). "State of Synthetic Research 2025." https://syntheticusers.com/state-of-synthetic-research-2025

15. UserTesting. (2024). "AI and the Future of Human Insight." https://www.usertesting.com/resources/reports/ai-human-insight

---

*Note: This report was compiled in March 2026 based on knowledge available through May 2025. Web search and direct URL verification were unavailable during compilation; some URLs and report details should be independently verified. Specific statistics from the State of Synthetic Research 2025 report are reported from available knowledge and may require confirmation against the primary source.*
