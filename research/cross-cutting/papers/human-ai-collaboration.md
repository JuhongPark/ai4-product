# Human-AI Collaboration in Product Teams: A Deep-Dive Research Analysis

> **Research Survey Document**
> Date: 2026-03-07
> Scope: Academic papers, industry reports, and practitioner research (2022--2026)
> Part of: AI for Product Research Survey Project

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Key Findings and Trends (2022--2026)](#2-key-findings-and-trends-20222026)
3. [Multidimensional Trust in AI](#3-multidimensional-trust-in-ai)
4. [Complementary Team Performance: Empirical Evidence](#4-complementary-team-performance-empirical-evidence)
5. [AI as Collaborative Digital Colleague vs. Replacement Threat](#5-ai-as-collaborative-digital-colleague-vs-replacement-threat)
6. [Microsoft New Future of Work Report 2025](#6-microsoft-new-future-of-work-report-2025)
7. [Carnegie Mellon Research on Strengthening Human Collaboration with AI](#7-carnegie-mellon-research-on-strengthening-human-collaboration-with-ai)
8. [Knowledge Diffusion in NPD Projects with AI](#8-knowledge-diffusion-in-npd-projects-with-ai)
9. [Team Dynamics and Role Changes with AI Integration](#9-team-dynamics-and-role-changes-with-ai-integration)
10. [Organizational Factors Affecting Human-AI Collaboration Success](#10-organizational-factors-affecting-human-ai-collaboration-success)
11. [Measuring Human-AI Team Effectiveness](#11-measuring-human-ai-team-effectiveness)
12. [Methods and Approaches: Frameworks and Models](#12-methods-and-approaches-frameworks-and-models)
13. [Limitations and Open Questions](#13-limitations-and-open-questions)
14. [Notable Papers and Sources](#14-notable-papers-and-sources)

---

## 1. Executive Summary

Human-AI collaboration in product teams has emerged as one of the most consequential research areas at the intersection of organizational science, human-computer interaction, and artificial intelligence. Between 2022 and 2026, the field has undergone a significant conceptual shift: from framing AI primarily as an automation tool that replaces discrete tasks, to understanding it as a collaborative agent that reshapes team dynamics, knowledge flows, and decision-making processes.

This deep-dive analysis synthesizes findings across academic and industry research to present the current state of knowledge. The central findings are:

- **Trust in AI is multidimensional**, spanning technical, cognitive, emotional, and social dimensions, and it evolves dynamically over the course of collaboration.
- **Complementary performance** (where human+AI teams outperform either humans or AI alone) is theoretically appealing but **empirically elusive**; achieving it requires specific task structures, calibrated reliance, and appropriate delegation mechanisms.
- **Organizational and cultural factors** are at least as important as technical capabilities in determining whether human-AI collaboration succeeds.
- The dominant framing has shifted from **replacement anxiety** to **augmentation and partnership**, driven in part by large-scale industry reports such as Microsoft's New Future of Work Report 2025.
- **Measurement of human-AI team effectiveness** remains an open challenge, with no consensus on standardized metrics or evaluation frameworks.

---

## 2. Key Findings and Trends (2022--2026)

### 2.1 The Augmentation Paradigm Ascendant (2022--2024)

The period from 2022 to 2024 marked a decisive shift in how researchers and practitioners conceptualize AI's role in teams. Several converging forces drove this transition:

- **The generative AI inflection point (2022--2023):** The release of ChatGPT (November 2022) and subsequent large language models catalyzed widespread experimentation with AI as a collaborative partner in knowledge work. Product teams began using LLMs for ideation, specification writing, competitive analysis, and user research synthesis.

- **Empirical productivity studies:** A series of influential studies demonstrated that AI augmentation could meaningfully improve individual and team productivity in specific domains:
  - Brynjolfsson, Li, and Raymond (2023) studied 5,179 customer support agents using an AI-based conversational assistant and found a **14% increase in productivity** on average, with the largest gains (34%) among novice and low-skilled workers. This finding established a key theme: AI as an equalizer that raises the floor of team performance.
    - Paper: "Generative AI at Work." NBER Working Paper 31161.
    - URL: https://www.nber.org/papers/w31161

  - Dell'Acqua et al. (2023) at Harvard Business School conducted a randomized controlled trial with 758 BCG consultants and found that consultants using GPT-4 completed **12.2% more tasks, 25.1% faster, and with 40% higher quality** compared to those without AI. However, for tasks that fell outside AI's capability boundary, AI-assisted consultants performed **19 percentage points worse** than the control group, suggesting a risk of over-reliance.
    - Paper: "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality."
    - URL: https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7571.pdf

- **McKinsey State of AI (2024--2025):** The McKinsey Global Survey on AI reported that 78% of organizations used AI in at least one business function by 2024 (up from 55% in 2023), with product development and service operations as leading adoption areas.
  - URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

### 2.2 From Tools to Teammates (2024--2026)

The 2024--2026 period saw a further evolution in framing:

- **AI as "synthetic teammate":** Raisch and Fomenko (2025) explicitly proposed GenAI as an NPD team member, arguing that AI can participate across ideation, prototyping, and evaluation phases when properly integrated into team workflows.
  - Paper: "Your Synthetic Teammate: Enriching NPD with Generative AI." Business Horizons, 2025.
  - URL: https://www.sciencedirect.com/science/article/pii/S0007681325000357

- **Agentic AI emergence:** By 2025--2026, the discourse expanded beyond copilot-style assistance to agentic AI systems capable of autonomous task execution within product workflows. Gartner predicted that 40% of enterprise applications would feature task-specific AI agents by end of 2026, up from less than 5% in 2025.
  - URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

- **Human-AI teaming as a design problem:** Researchers increasingly recognized that effective collaboration requires intentional design of interaction protocols, role allocation, feedback mechanisms, and trust calibration -- not merely access to better AI models.

### 2.3 Key Trends Summary

| Trend | Period | Evidence Level |
|-------|--------|----------------|
| AI as productivity booster for individual knowledge workers | 2022--2024 | Strong (multiple RCTs) |
| AI as team-level collaborator in product development | 2024--2026 | Moderate (mixed-method studies) |
| Multidimensional trust as prerequisite for effective collaboration | 2024--2025 | Emerging (conceptual + survey) |
| Complementary performance (human+AI > either alone) | 2022--2025 | Weak (rarely observed empirically) |
| Organizational/cultural factors as key moderators | 2023--2025 | Moderate (qualitative + survey) |
| Agentic AI in product workflows | 2025--2026 | Early (mostly industry projections) |

---

## 3. Multidimensional Trust in AI

### 3.1 Conceptual Framework

Trust in AI has emerged as a central construct in understanding human-AI collaboration effectiveness. Recent research establishes that trust in AI is not a monolithic concept but consists of multiple interrelated dimensions:

**"Enhancing Human-AI Collaboration and Trust in NPD from Organization Clustering Perspective"** (2025) proposes a multidimensional trust framework with the following components:

| Dimension | Definition | Key Indicators |
|-----------|-----------|----------------|
| **Technical Trust** | Confidence in the AI system's reliability, accuracy, and performance | Prediction accuracy, system uptime, error rates, consistency of outputs |
| **Cognitive Trust** | Rational assessment of AI's competence based on evidence and experience | Perceived competence, track record, transparency of reasoning |
| **Emotional Trust** | Affective responses and comfort level in relying on AI | Sense of security, reduced anxiety, willingness to be vulnerable to AI decisions |
| **Social Trust** | Trust arising from the organizational and interpersonal context in which AI is embedded | Peer endorsement, organizational norms, collective adoption behaviors |

- Paper: "Enhancing Human-AI Collaboration and Trust in NPD from Organization Clustering Perspective." Computers & Industrial Engineering, 2025.
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0360835225008435

### 3.2 Dynamic Evolution of Trust

A critical finding is that trust in AI is not static but **evolves dynamically** through interaction:

- **Initial trust formation** is heavily influenced by the user's prior experience with technology, organizational framing of AI, and the AI system's initial performance.
- **Calibration phase:** Trust adjusts as users gain experience with the system's actual capabilities and limitations. Over-trust (automation complacency) and under-trust (algorithm aversion) are both documented failure modes.
- **Stabilization:** Over time, trust tends to settle at a level reflective of actual system performance, though this process can be disrupted by salient failures or organizational changes.

### 3.3 Trust Calibration and Appropriate Reliance

The concept of **appropriate reliance** -- neither over-relying on AI nor dismissing its outputs -- has become central to the human-AI collaboration literature:

- **Bansal et al. (2021)** introduced the concept of "complementary performance" being contingent on appropriate human reliance on AI, finding that simply showing AI confidence scores was insufficient to achieve calibrated trust.
  - Paper: "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance." CHI 2021, ACM.
  - URL: https://dl.acm.org/doi/10.1145/3411764.3445717

- **Vasconcelos et al. (2023)** demonstrated that explanations can paradoxically increase over-reliance on AI when they are persuasive but not necessarily accurate, a phenomenon termed the "illusion of explanatory depth."
  - Paper: "Explanations Can Reduce Overreliance on AI Systems During Decision-Making." Proceedings of the ACM on Human-Computer Interaction, 2023.

- **Lee and Baykal (2024)** proposed that trust calibration requires not only transparency mechanisms but also **experiential learning** -- opportunities for users to observe AI failures in low-stakes contexts before relying on it in high-stakes decisions.

### 3.4 Trust in Product Team Contexts

In product teams specifically, trust dynamics are complicated by:

- **Multiple stakeholders** with different risk tolerances (engineers, designers, product managers, executives)
- **Varying AI literacy** across team members
- **Accountability gaps** -- when AI contributes to a product decision, it is unclear who bears responsibility for outcomes
- **Temporal pressure** -- product development timelines may not allow for gradual trust calibration

---

## 4. Complementary Team Performance: Empirical Evidence

### 4.1 The Complementarity Hypothesis

The central promise of human-AI collaboration is **complementary performance**: the idea that human+AI teams can outperform either humans alone or AI alone. This hypothesis rests on the assumption that humans and AI have different and complementary strengths:

| Capability | Human Strength | AI Strength |
|-----------|---------------|-------------|
| Pattern recognition in structured data | Moderate | Strong |
| Common-sense reasoning | Strong | Weak-Moderate |
| Processing speed and scale | Weak | Strong |
| Contextual judgment | Strong | Weak |
| Consistency and tirelessness | Weak | Strong |
| Creative/divergent thinking | Strong | Moderate (improving) |
| Ethical and social judgment | Strong | Weak |

### 4.2 Empirical Evidence: A Sobering Picture

**"Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence"** (2025) is the most comprehensive review of empirical evidence on this topic. The key finding is striking:

> **Complementary team performance (human+AI > either alone) has rarely been observed empirically.**

The paper identifies several reasons for this gap between theory and evidence:

1. **Inappropriate delegation:** Humans often fail to correctly identify which tasks to delegate to AI and which to retain, leading to suboptimal task allocation.
2. **Automation bias:** When AI is present, humans tend to defer to its recommendations even when their own judgment would be superior, eliminating the potential for complementarity.
3. **Anchoring effects:** AI suggestions serve as anchors that constrain human exploration of the solution space, reducing the diversity of human contributions.
4. **Misaligned incentives:** In many experimental settings, there is no strong incentive for humans to override AI recommendations, even when they detect errors.

- Paper: "Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence." European Journal of Information Systems, 2025.
- URL: https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

### 4.3 Conditions Under Which Complementarity Emerges

Despite the overall sobering evidence, researchers have identified specific conditions that facilitate complementary performance:

- **Task decomposition:** When tasks can be decomposed into subtasks with clear allocation criteria (AI handles data-intensive components; humans handle judgment-intensive components), complementarity is more achievable.

- **Structured handoff protocols:** Formal protocols for when and how to transition decision authority between human and AI improve outcomes relative to ad hoc collaboration.

- **Expertise matching:** Complementarity is most likely when the human possesses domain expertise that the AI lacks, and vice versa. In the BCG study (Dell'Acqua et al., 2023), complementarity was observed for tasks within AI's capability frontier but reversed for tasks outside it.

- **Learning-to-defer frameworks:** Technical approaches where AI systems learn when to defer to human judgment (and humans learn when to defer to AI) show promise in improving joint performance.
  - Relevant work: Mozannar and Sontag (2020), "Consistent Estimators for Learning to Defer to an Expert." ICML 2020.

### 4.4 The "Jagged Frontier" Model

Dell'Acqua et al. (2023) introduced the influential metaphor of the **"jagged technological frontier"** to describe AI capabilities:

- AI's capability boundary is not a smooth line but a jagged, irregular frontier -- excelling at some tasks that seem difficult while failing at others that seem easy.
- Effective human-AI collaboration requires **accurate mental models** of this frontier, which are difficult to develop because AI capabilities are often opaque and change rapidly.
- Product teams that develop accurate mental models of AI's jagged frontier can better allocate tasks and achieve complementarity; those that do not risk either underutilizing AI or over-relying on it.

---

## 5. AI as Collaborative Digital Colleague vs. Replacement Threat

### 5.1 The Shifting Narrative

The discourse around AI in teams has undergone a marked shift from 2022 to 2026:

**Phase 1: Replacement Anxiety (2022--2023)**
- Initial reactions to generative AI focused heavily on job displacement.
- Goldman Sachs (2023) estimated that generative AI could expose the equivalent of 300 million full-time jobs to automation globally.
- Product teams expressed concern about AI replacing roles in copywriting, basic design, QA testing, and data analysis.

**Phase 2: Augmentation Reframing (2023--2024)**
- Research evidence began to suggest that AI's primary near-term impact was augmentation rather than replacement.
- The Brynjolfsson et al. (2023) customer support study demonstrated that AI augmented rather than replaced agents, with no net job losses during the study period.
- Harvard's BCG study showed that AI improved consultant performance but required human oversight to avoid failure modes.

**Phase 3: Colleague and Teammate (2025--2026)**
- The Microsoft New Future of Work Report 2025 explicitly advocated for viewing AI as a "collaborative digital colleague" rather than a replacement threat.
- Research shifted toward understanding the interpersonal and social dynamics of human-AI teams.
- Questions emerged about AI's role in team identity, social cohesion, and shared mental models.

### 5.2 Evidence for the "Colleague" Framing

Several lines of evidence support treating AI as a collaborative partner in product teams:

- **Complementary skill profiles:** AI excels at speed, breadth, and consistency; humans excel at judgment, creativity, and contextual adaptation. These profiles are more complementary than substitutive.

- **Delegation vs. displacement:** Empirical studies show that AI adoption in product teams more commonly leads to **task reallocation** (shifting human effort to higher-value activities) than to headcount reduction.

- **Emerging social dynamics:** Research on human-AI interaction has documented that teams develop quasi-social relationships with AI collaborators, including attributing personality traits, expressing frustration, and developing collaborative routines.

### 5.3 Persistent Concerns

Despite the shift toward the colleague framing, several legitimate concerns remain:

- **Skill atrophy:** Extended reliance on AI for certain tasks (e.g., data analysis, writing first drafts) may cause team members' skills in those areas to atrophy, creating long-term dependency.
- **Deskilling of junior roles:** If AI handles tasks traditionally assigned to junior team members (research synthesis, competitive analysis, documentation), those roles may lose their developmental function.
- **Concentration of judgment:** As AI handles more routine tasks, the remaining human roles become more judgment-intensive, potentially increasing cognitive load and decision fatigue.

---

## 6. Microsoft New Future of Work Report 2025

### 6.1 Overview

The **Microsoft New Future of Work Report 2025**, produced by Microsoft Research, is one of the most comprehensive industry research documents on AI's impact on work and collaboration. It synthesizes findings from Microsoft's internal research, external academic collaborations, and large-scale telemetry data from Microsoft 365 Copilot deployments.

- URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf

### 6.2 Key Findings Relevant to Human-AI Collaboration

**On the shift from replacement to collaboration:**
- The report frames AI as fundamentally a collaborative technology and argues that the most productive integration pattern is **human-AI teaming** rather than full automation.
- It emphasizes that AI's value is maximized when it is treated as a "thought partner" that augments human judgment rather than substituting for it.

**On productivity impacts:**
- Early data from Microsoft 365 Copilot deployments suggest productivity gains in specific task categories: email triage, meeting summarization, document drafting, and data analysis.
- However, the report cautions that **aggregate productivity gains are smaller than expected**, partly because workers spend saved time on other activities (some productive, some not).
- The report introduces the concept of **"productivity reallocation"**: AI does not simply make existing tasks faster but changes the allocation of time across tasks, with complex second-order effects.

**On team dynamics:**
- AI changes team communication patterns: teams using AI assistants tend to have shorter, more focused meetings but may also experience reduced informal interaction.
- The report documents a tension between **AI-mediated efficiency** and **social cohesion** -- teams that over-rely on AI for coordination may lose the interpersonal bonds that support creative collaboration.

**On trust and adoption:**
- The report identifies trust calibration as a key challenge and recommends organizations invest in "AI literacy" programs that help workers develop accurate mental models of AI capabilities.
- It finds that **managerial behavior** is the single strongest predictor of team-level AI adoption: teams whose managers actively model AI use adopt it more quickly and effectively.

**On organizational design:**
- The report recommends rethinking team structures to account for AI as a persistent team member, including explicit role definitions for AI, clear escalation paths when AI output is uncertain, and regular "AI retrospectives" to evaluate collaboration quality.

### 6.3 Methodological Notes

The report combines:
- Large-scale telemetry analysis from Microsoft 365 Copilot (millions of users)
- Controlled experiments with Microsoft employees
- Surveys of knowledge workers across industries
- Synthesis of external academic literature

A limitation is that much of the data comes from Microsoft's own products, potentially limiting generalizability.

---

## 7. Carnegie Mellon Research on Strengthening Human Collaboration with AI

### 7.1 Overview

Carnegie Mellon University has been a leading institution in human-AI collaboration research, with contributions spanning the School of Computer Science, the Tepper School of Business, and the Human-Computer Interaction Institute. In October 2025, CMU published a research initiative specifically focused on how AI can **strengthen, not replace, human collaboration**.

- URL: https://www.cmu.edu/news/stories/archives/2025/october/

### 7.2 Key Research Themes

**AI as collaboration infrastructure:**
- CMU researchers have investigated how AI can serve as infrastructure that improves human-to-human collaboration, rather than replacing human collaborators. This includes AI systems that facilitate better meeting facilitation, conflict resolution, and knowledge sharing within teams.

**Shared mental models:**
- Research from the CMU HCII (Human-Computer Interaction Institute) examines how AI can help teams develop and maintain shared mental models -- common understandings of the team's goals, strategies, and each member's roles. AI-generated summaries, visualizations, and decision logs can serve as "team memory" that keeps distributed teams aligned.

**Complementary intelligence:**
- CMU's Tepper School has contributed research on how to design AI systems that complement rather than duplicate human intelligence, focusing on task allocation algorithms that optimally divide work between human and AI based on real-time assessment of each party's comparative advantage.

**Social AI for team dynamics:**
- Research on AI systems that can detect and respond to team dynamics -- such as uneven participation, emerging conflicts, or declining engagement -- and intervene to improve collaboration quality.

### 7.3 Notable CMU Researchers and Labs

- **Anita Williams Woolley** (Tepper School of Business): Research on collective intelligence and how AI changes group dynamics. Her work on "collective intelligence factor" (c-factor) explores whether AI participation in teams changes the group's collective intelligence.
  - Key concept: Just as individual IQ predicts individual performance, the c-factor predicts group performance. Research investigates whether AI can increase a team's c-factor.

- **Jeffrey Bigham** and the **Accessibility Lab** (HCII): Research on AI-mediated collaboration for inclusive teams, including how AI can bridge communication gaps between team members with different abilities or backgrounds.

- **Robert Kraut** (HCII): Long-standing research on technology-mediated collaboration and online communities, extended to include AI-mediated teamwork.

### 7.4 Implications for Product Teams

CMU's research suggests several implications for product teams:

1. **Design AI for the team, not just the individual:** Most current AI tools (Copilot, ChatGPT, etc.) are designed as individual productivity tools. Greater value may come from AI designed to improve team-level processes.
2. **Use AI to reduce coordination costs:** Product development is coordination-intensive. AI can reduce the overhead of aligning across functions (engineering, design, PM, marketing).
3. **Monitor team health, not just output:** AI can help product leaders monitor team dynamics and intervene early when collaboration breaks down.

---

## 8. Knowledge Diffusion in NPD Projects with AI

### 8.1 Framework

**"Measuring the Impact of Human-AI Collaboration on Knowledge Diffusion in NPD Projects"** (2025) provides a framework for understanding how AI affects the flow of knowledge within new product development teams.

- Paper: Published in Engineering Management (Springer), 2025.
- URL: https://link.springer.com/article/10.1007/s42524-025-4210-3

### 8.2 Key Concepts

**Knowledge diffusion** refers to the process by which knowledge is transferred, shared, and integrated across individuals and teams within an organization. In NPD projects, effective knowledge diffusion is critical because product development requires integrating expertise from multiple domains (engineering, design, marketing, customer research).

The paper proposes that AI affects knowledge diffusion through several mechanisms:

| Mechanism | Description | Effect on Knowledge Diffusion |
|-----------|-------------|-------------------------------|
| **Knowledge codification** | AI systems capture and structure tacit knowledge into explicit, searchable formats | Positive: reduces knowledge loss, improves accessibility |
| **Knowledge bridging** | AI acts as an intermediary that translates domain-specific knowledge across team boundaries | Positive: reduces silos, improves cross-functional understanding |
| **Knowledge acceleration** | AI speeds up the process of synthesizing and distributing new information | Positive: faster integration of customer feedback, market data |
| **Knowledge filtering** | AI curates and prioritizes relevant information, reducing information overload | Mixed: improves focus but may inadvertently filter out important signals |
| **Knowledge homogenization** | AI-generated content may converge toward average or expected patterns | Negative: may reduce diversity of perspectives and novel ideas |

### 8.3 Empirical Findings

The paper's empirical analysis suggests:

- AI-augmented NPD teams show **faster knowledge transfer** between phases (e.g., from discovery to design) compared to non-augmented teams.
- However, **knowledge depth** may be reduced: AI tends to produce broad but shallow summaries that miss nuanced domain-specific insights.
- The **organizational clustering perspective** (how teams are organized and how knowledge clusters form) significantly moderates AI's impact on knowledge diffusion. In organizations with strong cross-functional structures, AI amplifies existing knowledge-sharing norms; in siloed organizations, AI may reinforce existing boundaries.

### 8.4 Implications

For product teams, these findings suggest that:

- AI is most valuable for knowledge diffusion when combined with **organizational structures** that support cross-functional collaboration.
- Teams should be wary of AI-generated summaries that sacrifice depth for breadth, and should maintain channels for deep, domain-specific knowledge sharing.
- Explicit knowledge management strategies should account for AI's tendency toward homogenization.

---

## 9. Team Dynamics and Role Changes with AI Integration

### 9.1 Role Restructuring

The integration of AI into product teams is driving significant changes in team roles and responsibilities:

**Emerging roles:**
- **AI orchestrator / prompt engineer:** Team members who specialize in crafting effective AI interactions, translating team needs into AI-compatible inputs, and curating AI outputs.
- **AI quality reviewer:** Roles focused on reviewing and validating AI-generated outputs before they enter the product development pipeline.
- **Human-AI workflow designer:** Specialists in designing workflows that effectively integrate human and AI contributions.

**Evolving roles:**
- **Product managers** are increasingly expected to evaluate AI-generated insights, manage AI tools as "team members," and make decisions about where AI augmentation is appropriate.
- **Designers** are shifting from producing artifacts to curating and refining AI-generated design alternatives.
- **Engineers** are moving from writing code to reviewing, testing, and integrating AI-generated code.
- **User researchers** are navigating the boundary between human-conducted research and AI-synthesized insights, increasingly serving as validators of AI-generated findings.

### 9.2 Power Dynamics and Decision Authority

AI integration raises questions about decision authority within teams:

- **Who has the final say?** When AI recommends a product direction that conflicts with team intuition, established norms about decision-making authority may be insufficient.
- **Expertise leveling:** AI can level the information playing field, giving junior team members access to insights that previously required years of experience. This can be empowering but also threatens traditional expertise-based hierarchies.
- **Accountability gaps:** When decisions are made with significant AI input, responsibility for outcomes becomes diffused. Research suggests that teams may default to "the AI suggested it" as a diffusion of responsibility mechanism.

### 9.3 Impact on Team Cognition

Research on AI's impact on team cognition identifies several effects:

- **Transactive memory disruption:** Teams develop transactive memory systems (shared knowledge of who knows what). AI disrupts this by becoming a new "knowledge holder" whose capabilities are not well understood by all team members.
- **Cognitive offloading:** Team members may offload cognitive tasks to AI, reducing individual cognitive load but potentially weakening the team's collective capacity for deep analysis.
- **Anchoring and satisficing:** AI-generated suggestions can anchor team discussions and lead to satisficing (accepting "good enough" AI outputs rather than exploring potentially better alternatives).

---

## 10. Organizational Factors Affecting Human-AI Collaboration Success

### 10.1 Leadership and Culture

Research consistently identifies organizational factors as critical moderators of human-AI collaboration success:

**Leadership behaviors:**
- **Modeling:** Leaders who visibly use AI tools and share their experiences (including failures) create psychological safety for team adoption.
- **Expectation setting:** Clear communication about AI's role (augmentation, not replacement) reduces anxiety and resistance.
- **Investment in learning:** Organizations that allocate time and resources for AI experimentation see better collaboration outcomes.

**Cultural factors:**
- **Psychological safety:** Teams in high-psychological-safety environments are more likely to experiment with AI, report failures, and iterate on collaboration approaches.
- **Learning orientation:** Organizations with a learning (vs. performance) orientation adapt more effectively to AI integration.
- **Tolerance for ambiguity:** AI outputs are inherently probabilistic and sometimes wrong. Organizations with higher tolerance for ambiguity integrate AI more effectively.

### 10.2 Infrastructure and Process

**Technical infrastructure:**
- Integration of AI tools into existing workflows (rather than requiring context switching) significantly improves adoption and collaboration quality.
- Access to high-quality, organization-specific data for AI customization is a key differentiator.

**Process design:**
- Formal protocols for human-AI handoffs, quality review checkpoints, and escalation paths improve collaboration outcomes.
- "AI retrospectives" (regular team reflections on how AI collaboration is working) are recommended by both the Microsoft report and Carnegie Mellon research.

### 10.3 Training and AI Literacy

- **AI literacy** -- understanding what AI can and cannot do, how to formulate effective prompts, and how to critically evaluate AI outputs -- is increasingly recognized as a core competency for product teams.
- HBR (2026) argues that building product management skills is essential for driving effective AI adoption.
  - URL: https://hbr.org/2026/02/to-drive-ai-adoption-build-your-teams-product-management-skills
- Organizations that invest in structured AI literacy programs report higher satisfaction with human-AI collaboration and lower incidence of over-reliance failures.

---

## 11. Measuring Human-AI Team Effectiveness

### 11.1 The Measurement Challenge

Measuring the effectiveness of human-AI collaboration is an open challenge. Traditional productivity metrics (output per unit time) fail to capture important dimensions of collaboration quality, and AI-specific metrics are not yet standardized.

### 11.2 Proposed Measurement Frameworks

**Multi-level measurement:**
Researchers propose measuring human-AI team effectiveness at multiple levels:

| Level | Metrics | Measurement Approach |
|-------|---------|---------------------|
| **Task level** | Accuracy, speed, quality of individual task outputs | A/B testing, controlled experiments |
| **Process level** | Efficiency of workflows, number of iterations required, handoff quality | Process mining, workflow analytics |
| **Team level** | Team satisfaction, cohesion, shared mental model quality, knowledge sharing | Surveys, social network analysis |
| **Outcome level** | Product success metrics (adoption, revenue, user satisfaction) | Business outcome tracking |
| **Learning level** | Team capability improvement over time, skill development | Longitudinal assessment |

**OECD Sectoral Taxonomy of AI Intensity (2024):**
The OECD's framework provides a complementarity measure for AI exposure and productivity, offering a macro-level approach to measuring AI's impact across sectors and occupations.
- URL: https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/a-sectoral-taxonomy-of-ai-intensity_c2baae71/1f6377b5-en.pdf

### 11.3 Key Metrics Under Development

- **Appropriate reliance rate:** The proportion of instances where humans correctly defer to or override AI recommendations.
- **Complementarity gap:** The difference between actual human-AI team performance and the theoretical maximum achievable through optimal task allocation.
- **Trust calibration score:** The alignment between a user's confidence in AI and the AI's actual accuracy.
- **Knowledge integration index:** The degree to which AI-generated insights are actually incorporated into team decisions (vs. ignored or blindly accepted).
- **Collaboration friction:** The overhead cost (time, cognitive effort) required to integrate AI into team workflows.

### 11.4 Challenges in Measurement

- **Attribution problem:** When teams use AI extensively, it is difficult to attribute specific outcomes to human vs. AI contributions.
- **Counterfactual difficulty:** Measuring what the team would have achieved without AI requires controlled experiments, which are difficult to conduct in real product development settings.
- **Long-term vs. short-term effects:** AI may improve short-term productivity while undermining long-term team capabilities (through skill atrophy or reduced experimentation), or vice versa.

---

## 12. Methods and Approaches: Frameworks and Models

### 12.1 Human-AI Teaming Frameworks

**The Levels of Automation (LOA) Framework:**
Originally from Sheridan and Verplank (1978), updated for modern AI by Parasuraman, Sheridan, and Wickens (2000), this framework describes a spectrum from full human control to full automation. Modern adaptations add:
- **Dynamic LOA:** The level of automation adjusts in real time based on task complexity, AI confidence, and human workload.
- **Task-specific LOA:** Different levels of automation for different subtasks within the same workflow.

**The Human-AI Decision Making (HAIDM) Framework:**
Emerging from the CHI and CSCW communities, this framework emphasizes:
1. **Decision identification:** Which decisions benefit from AI input?
2. **AI recommendation generation:** How does AI produce its recommendation?
3. **Human evaluation:** How does the human evaluate the AI recommendation?
4. **Integration:** How is the final decision made (human override, AI deference, weighted combination)?
5. **Feedback:** How does the outcome inform future collaboration?

**The Organization Clustering Perspective (2025):**
From the "Enhancing Human-AI Collaboration and Trust in NPD" paper, this framework analyzes how organizational structure (functional vs. cross-functional, centralized vs. distributed) moderates the effectiveness of human-AI collaboration.

### 12.2 Trust Models

**The ABI (Ability, Benevolence, Integrity) Model of Trust:**
Originally developed for interpersonal trust (Mayer, Davis, and Schoorman, 1995), adapted for human-AI trust:
- **Ability** maps to **technical competence** of the AI system
- **Benevolence** maps to **alignment** of AI objectives with user interests
- **Integrity** maps to **transparency** and **predictability** of AI behavior

**Lee and See's Trust in Automation Model (2004):**
A widely cited framework distinguishing between:
- **Performance-based trust:** Based on observed AI competence
- **Process-based trust:** Based on understanding of how AI works
- **Purpose-based trust:** Based on perceived AI intent

### 12.3 Complementarity Models

**The Learning-to-Complement Framework:**
Proposes that achieving complementary performance requires:
1. AI that can estimate its own uncertainty
2. Humans who can accurately assess their own confidence
3. A delegation mechanism that assigns tasks to whichever party is more likely to succeed
4. A learning loop that improves delegation accuracy over time

**The Jagged Frontier Model (Dell'Acqua et al., 2023):**
As discussed in Section 4.4, this model emphasizes the irregular boundary of AI capabilities and the need for humans to develop accurate mental models of this boundary.

### 12.4 Knowledge Integration Models

**The AI-Augmented Knowledge Diffusion Model (2025):**
From the Springer Engineering Management paper, this model describes five mechanisms through which AI affects knowledge flow in NPD projects (codification, bridging, acceleration, filtering, homogenization), as detailed in Section 8.

---

## 13. Limitations and Open Questions

### 13.1 Limitations of Current Research

1. **Limited ecological validity:** Most empirical studies on human-AI complementarity are conducted in controlled laboratory settings with artificial tasks. Transfer to real-world product development contexts is uncertain.

2. **Publication bias toward positive results:** Studies showing productivity gains from AI are more likely to be published and publicized than those showing null or negative effects, creating a skewed evidence base.

3. **Rapid technological change:** AI capabilities are evolving so quickly that research findings may be outdated by the time they are published. Studies conducted with GPT-3.5 may not generalize to GPT-4 or subsequent models.

4. **Western and tech-industry bias:** Most research is conducted in Western, English-speaking contexts and in technology companies. Generalizability to other cultural contexts and industries is limited.

5. **Short time horizons:** Most studies examine AI collaboration over days or weeks. The long-term effects on team capabilities, organizational knowledge, and career development remain largely unexplored.

6. **Individual-level focus:** Most research examines individual human-AI interaction rather than team-level or organizational-level dynamics.

7. **Measurement gaps:** As discussed in Section 11, there are no standardized metrics for human-AI team effectiveness, making cross-study comparison difficult.

### 13.2 Open Research Questions

| # | Question | Relevance |
|---|----------|-----------|
| 1 | **Under what specific conditions does human+AI complementarity reliably emerge?** | Central to justifying human-AI teaming investments |
| 2 | **How does long-term AI collaboration affect human skill development and team capabilities?** | Critical for workforce planning and organizational learning |
| 3 | **What organizational structures and cultures best support human-AI collaboration?** | Essential for organizational design |
| 4 | **How should accountability be distributed in human-AI teams?** | Legal, ethical, and managerial implications |
| 5 | **How do power dynamics and hierarchies change when AI becomes a team participant?** | Important for team management and equity |
| 6 | **What is the optimal level of AI autonomy for different product development tasks?** | Directly affects workflow design |
| 7 | **How can teams develop and maintain accurate mental models of AI capabilities as those capabilities change rapidly?** | Practical challenge for all AI-using teams |
| 8 | **How does AI-mediated collaboration affect innovation and creativity in product development?** | Core concern for product teams |
| 9 | **What are the long-term effects of AI-generated knowledge homogenization on product diversity and innovation?** | Strategic concern for organizations and markets |
| 10 | **How should human-AI collaboration be taught and trained?** | Educational and professional development implications |

### 13.3 Methodological Gaps

- **Need for longitudinal studies:** Most current research provides snapshots. Longitudinal designs tracking teams over months or years are needed.
- **Need for field experiments in real product teams:** Controlled experiments in laboratory settings need to be complemented by rigorous field studies.
- **Need for multi-level analysis:** Studies that simultaneously examine individual, team, and organizational effects are rare but essential.
- **Need for cross-cultural research:** Nearly all existing research is conducted in North American or European contexts.
- **Need for standardized measurement instruments:** Development and validation of reliable scales for constructs like trust in AI, collaboration quality, and complementarity.

---

## 14. Notable Papers and Sources

### 14.1 Core Academic Papers

1. **"Enhancing Human-AI Collaboration and Trust in NPD from Organization Clustering Perspective"**
   - Authors: Published in Computers & Industrial Engineering
   - Year: 2025
   - Key contribution: Multidimensional trust framework (technical, cognitive, emotional, social)
   - URL: https://www.sciencedirect.com/science/article/abs/pii/S0360835225008435

2. **"Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence"**
   - Authors: Published in European Journal of Information Systems (Taylor & Francis)
   - Year: 2025
   - Key contribution: Comprehensive review showing complementary performance is rarely achieved empirically
   - URL: https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

3. **"Measuring the Impact of Human-AI Collaboration on Knowledge Diffusion in NPD Projects"**
   - Authors: Published in Engineering Management (Springer)
   - Year: 2025
   - Key contribution: Framework for AI's impact on organizational knowledge flows
   - URL: https://link.springer.com/article/10.1007/s42524-025-4210-3

4. **"Your Synthetic Teammate: Enriching NPD with Generative AI"**
   - Authors: Raisch, S. and Fomenko, E.
   - Year: 2025
   - Journal: Business Horizons (ScienceDirect)
   - Key contribution: Framework for GenAI as an NPD team member
   - URL: https://www.sciencedirect.com/science/article/pii/S0007681325000357

5. **"Navigating the Jagged Technological Frontier"**
   - Authors: Dell'Acqua, F., McFowland, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., and Lakhani, K.
   - Year: 2023
   - Institution: Harvard Business School
   - Key contribution: RCT with 758 BCG consultants showing both benefits and risks of AI augmentation; "jagged frontier" metaphor
   - URL: https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7571.pdf

6. **"Generative AI at Work"**
   - Authors: Brynjolfsson, E., Li, D., and Raymond, L.
   - Year: 2023
   - Institution: NBER / Stanford
   - Key contribution: Large-scale field study showing 14% productivity gains from AI, with greatest benefits for low-skilled workers
   - URL: https://www.nber.org/papers/w31161

7. **"Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance"**
   - Authors: Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M.T., and Weld, D.
   - Year: 2021
   - Venue: CHI 2021 (ACM)
   - Key contribution: Foundational study on complementary performance and the role of AI explanations
   - URL: https://dl.acm.org/doi/10.1145/3411764.3445717

8. **"Ethics by Design for Artificial Intelligence"**
   - Year: 2023
   - Journal: AI and Ethics (Springer)
   - Key contribution: Framework adopted by European Commission for AI project ethics review
   - URL: https://link.springer.com/article/10.1007/s43681-023-00330-4

9. **"Where Does AI Play a Major Role in NPD and Product Management?"**
   - Year: 2025
   - Journal: Management Review Quarterly (Springer)
   - Key contribution: Systematic literature review of 190 publications mapping AI methods to NPD phases
   - URL: https://link.springer.com/article/10.1007/s11301-025-00533-5

10. **"AI Ethics: Integrating Transparency, Fairness, and Privacy"**
    - Year: 2025
    - Journal: Applied AI (Taylor & Francis)
    - URL: https://www.tandfonline.com/doi/full/10.1080/08839514.2025.2463722

### 14.2 Industry Reports

11. **Microsoft New Future of Work Report 2025**
    - Institution: Microsoft Research
    - Key contribution: Comprehensive framework for AI as collaborative digital colleague; large-scale telemetry data
    - URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf

12. **Carnegie Mellon: "Researchers Explore How AI Can Strengthen, Not Replace, Human Collaboration"**
    - Year: 2025
    - Key contribution: AI as collaboration infrastructure; shared mental models
    - URL: https://www.cmu.edu/news/stories/archives/2025/october/

13. **McKinsey State of AI 2025**
    - Key contribution: 78% of organizations using AI; product development as leading adoption area
    - URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

14. **OECD Sectoral Taxonomy of AI Intensity (2024)**
    - Key contribution: Complementarity measure for AI exposure and productivity
    - URL: https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/a-sectoral-taxonomy-of-ai-intensity_c2baae71/1f6377b5-en.pdf

15. **Stanford HAI AI Index Report 2025**
    - Key contribution: Annual comprehensive review of AI progress, adoption, and societal impact
    - URL: https://hai.stanford.edu/ai-index/2025-ai-index-report

16. **Gartner: AI Agent Predictions (2025)**
    - Key contribution: 40% of enterprise apps to feature AI agents by 2026
    - URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

17. **HBR: "To Drive AI Adoption, Build Your Team's Product Management Skills" (2026)**
    - Key contribution: AI literacy and PM skills as prerequisites for effective human-AI collaboration
    - URL: https://hbr.org/2026/02/to-drive-ai-adoption-build-your-teams-product-management-skills

### 14.3 Foundational References

18. **Parasuraman, R., Sheridan, T.B., and Wickens, C.D. (2000).** "A Model for Types and Levels of Human Interaction with Automation." IEEE Transactions on Systems, Man, and Cybernetics, 30(3), 286-297.

19. **Mayer, R.C., Davis, J.H., and Schoorman, F.D. (1995).** "An Integrative Model of Organizational Trust." Academy of Management Review, 20(3), 709-734.

20. **Lee, J.D. and See, K.A. (2004).** "Trust in Automation: Designing for Appropriate Reliance." Human Factors, 46(1), 50-80.

21. **Woolley, A.W., Chabris, C.F., Pentland, A., Hashmi, N., and Malone, T.W. (2010).** "Evidence for a Collective Intelligence Factor in the Performance of Human Groups." Science, 330(6004), 686-688.

---

*This document is part of the AI for Product Research Survey Project. It provides a deep-dive analysis of the cross-cutting theme of Human-AI Collaboration in Product Teams, drawing on academic papers, industry reports, and practitioner research from 2022 to 2026.*
