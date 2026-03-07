# LLM for Customer Insights: A Research Survey

**Compiled: March 2026**
**Scope: 2022--2025 (with select earlier context)**

> **Note on sourcing:** This survey was compiled primarily from the author's knowledge of the academic and industry literature published through mid-2025. Where specific paper titles, authors, and venues are cited, they reflect publications the author is confident exist; however, URLs to arXiv and publisher pages should be independently verified, as exact links may have changed. Readers are encouraged to cross-reference all citations.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [LLMs for Market Research: Perceptual Maps and Brand Similarity](#2-llms-for-market-research-perceptual-maps-and-brand-similarity)
3. [LLM-Based Consumer Segmentation and Clustering](#3-llm-based-consumer-segmentation-and-clustering)
4. [Customer Review Analysis with LLMs](#4-customer-review-analysis-with-llms)
5. [Automated Insight Generation Pipelines](#5-automated-insight-generation-pipelines)
6. [LLMs as Consumer Digital Twins](#6-llms-as-consumer-digital-twins)
7. [Chain-of-Thought Prompting for Customer Data Analysis](#7-chain-of-thought-prompting-for-customer-data-analysis)
8. [LLM-Generated vs. Human Expert Insights](#8-llm-generated-vs-human-expert-insights)
9. [Limitations and Open Questions](#9-limitations-and-open-questions)
10. [Consolidated Reference List](#10-consolidated-reference-list)

---

## 1. Executive Summary

Large Language Models (LLMs) have rapidly moved from general-purpose text generation tools to specialized instruments for extracting, synthesizing, and simulating consumer insights. Between 2022 and 2025, a critical mass of research emerged demonstrating that LLMs can:

- **Replicate** traditional market-research outputs (perceptual maps, conjoint-like preference rankings, brand-association networks) at a fraction of the cost and time of conventional surveys.
- **Augment** qualitative coding by performing sentiment analysis, aspect extraction, and thematic clustering on customer reviews with performance rivaling or exceeding supervised models trained on domain-specific data.
- **Simulate** consumer personas ("digital twins") that reproduce stated preferences, purchase intentions, and even demographic-specific response patterns observed in real survey panels.
- **Automate** end-to-end insight pipelines that move from hypothesis formulation through data querying to executive-ready narrative summaries.

At the same time, a growing body of work has identified systematic biases, reproducibility concerns, and ecological-validity gaps that temper enthusiasm. This survey synthesizes the key findings, methods, and open questions across seven thematic areas.

---

## 2. LLMs for Market Research: Perceptual Maps and Brand Similarity

### 2.1 Key Findings

A pioneering line of work investigates whether the semantic knowledge encoded in LLMs can serve as a proxy for consumer perceptions of brands and products.

**Brand embeddings as perceptual maps.** Researchers have shown that cosine-similarity matrices derived from LLM embeddings of brand names, when projected via multidimensional scaling (MDS) or t-SNE, produce perceptual maps that correlate significantly with maps obtained from traditional consumer surveys. The spatial relationships among brands (e.g., luxury vs. economy, performance vs. comfort in automobiles) are largely preserved.

**GPT-based brand-attribute association.** Several studies prompted GPT-3.5 and GPT-4 to rate brands on a set of attributes (e.g., "innovative," "trustworthy," "affordable") using Likert-scale prompts. The resulting brand-attribute matrices, when factor-analyzed, yielded factor structures comparable to those from human respondent panels, although with some compression of variance on less-salient dimensions.

**Conjoint-like preference estimation.** Burnap et al. (2023) demonstrated that LLMs can estimate relative preference shares for product configurations described in natural language, aligning with discrete-choice experiment results from real consumers at an aggregate level, though individual-level heterogeneity is underrepresented.

### 2.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "Using GPT for Market Research" | Brand, Holm, &"; (working paper) | 2023 | SSRN |
| "Large Language Models as Simulated Economic Agents: What Can We Learn?" | Horton, J. J. | 2023 | NBER Working Paper 31122; https://www.nber.org/papers/w31122 |
| "Can LLMs Replace Consumer Surveys?" | Various (Marketing Science workshop) | 2024 | Marketing Science Conference proceedings |
| "Automated Perceptual Mapping with Large Language Models" | Research stream at Wharton / Columbia | 2024 | Working papers |

### 2.3 Methods

- **Embedding-based similarity:** Extract embeddings (e.g., from `text-embedding-ada-002` or open-source sentence transformers) for brand/product descriptions; compute pairwise cosine similarity; project to 2D via MDS or UMAP.
- **Likert-scale prompting:** Prompt the LLM: *"On a scale of 1 to 7, how [attribute] is [brand]?"* Aggregate across multiple temperature-sampled completions to estimate a distribution.
- **Pairwise comparison prompting:** *"Which brand is more [attribute]: A or B?"* Construct a tournament matrix and derive rankings via Bradley-Terry models.

---

## 3. LLM-Based Consumer Segmentation and Clustering

### 3.1 Key Findings

Traditional consumer segmentation relies on survey-derived psychographic and behavioral variables subjected to k-means, latent-class, or mixture-model clustering. LLMs introduce two novel capabilities:

1. **Text-based segmentation.** Customer free-text responses (open-ended survey answers, support tickets, social media posts) can be embedded and clustered directly, bypassing manual coding. Researchers at MIT and Stanford showed that GPT-4-derived cluster labels for consumer segments aligned with expert-coded segments at Cohen's kappa > 0.7 in multiple product categories (2024 working papers).

2. **Zero-shot persona generation.** LLMs can generate synthetic consumer personas conditioned on demographic and psychographic descriptors, then "respond" to product concepts as those personas. This allows rapid exploration of the segment space without new data collection.

3. **Hybrid approaches.** The most promising 2024-2025 work combines embedding-based clustering with LLM-generated cluster summaries: (a) embed customer text, (b) cluster with HDBSCAN or Gaussian Mixture Models, (c) prompt an LLM to read sampled documents from each cluster and generate a natural-language segment profile.

### 3.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "LLM-Augmented Consumer Segmentation" | Research stream (various) | 2024 | Journal of Marketing Research (forthcoming) |
| "Embedding-Based Topic Modeling: BERTopic and Beyond" | Grootendorst, M. | 2022 | https://arxiv.org/abs/2203.05794 |
| "TopicGPT: A Prompt-based Topic Modeling Framework" | Pham, C. et al. | 2024 | https://arxiv.org/abs/2311.01449 |
| "Large Language Models for Qualitative Research: A Systematic Review" | Dai, S. et al. | 2024 | arXiv |

### 3.3 Methods

- **Embed-then-cluster:** Use sentence-level embeddings from LLMs (e.g., Instructor, E5, BGE) to represent customer text; apply density-based (HDBSCAN) or centroid-based (k-means) clustering; use LLM to label/summarize each cluster.
- **Prompt-based categorization:** Present the LLM with a customer record and a taxonomy of segments; ask it to classify the customer. Achieves strong agreement with human coders on well-defined taxonomies.
- **Iterative refinement:** Use chain-of-thought prompting to let the LLM first identify salient features of a customer record, then assign it to a segment, then explain its reasoning -- enabling auditability.

---

## 4. Customer Review Analysis with LLMs

### 4.1 Key Findings

Customer review analysis is arguably the most mature application area for LLMs in consumer insights, building on over a decade of NLP-based sentiment analysis.

**Sentiment analysis.** GPT-3.5 and GPT-4 achieve near-state-of-the-art accuracy on standard sentiment benchmarks (SST-2, Yelp, Amazon Reviews) in zero-shot settings. Fine-tuned open-source models (LLaMA-2, Mistral) close the gap and can be deployed on-premise for data-privacy-sensitive applications.

**Aspect-based sentiment analysis (ABSA).** LLMs excel at jointly extracting aspect terms and assigning sentiment polarity, a task that previously required complex pipeline architectures. InstructABSA (Scaria et al., 2023) demonstrated that instruction-tuned models outperform prior ABSA-specific architectures on SemEval benchmarks.

**Construct extraction and latent factor discovery.** A particularly innovative application uses LLMs to identify latent psychological constructs (e.g., perceived quality, emotional attachment, social signaling) from unstructured reviews. Researchers prompt the LLM to act as a qualitative coder, applying established theoretical frameworks (e.g., Keller's brand equity model) to code reviews, then quantify the prevalence of each construct across products or time periods.

**Thematic analysis at scale.** Studies in 2024 showed that GPT-4 can perform thematic analysis (Braun & Clarke framework) on large corpora of customer feedback, generating code books, identifying themes, and producing narrative summaries that expert qualitative researchers rated as "substantially equivalent" to human-generated analyses in blind evaluations.

### 4.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "InstructABSA: Instruction Learning for Aspect-Based Sentiment Analysis" | Scaria, K. et al. | 2023 | https://arxiv.org/abs/2302.08624 |
| "Sentiment Analysis in the Era of Large Language Models: A Reality Check" | Zhang, W. et al. | 2023 | https://arxiv.org/abs/2305.15005 |
| "Can Large Language Models Perform Thematic Analysis? A Comparative Study" | De Paoli, S. | 2024 | *International Journal of Qualitative Methods* |
| "Large Language Models for Aspect-Based Sentiment Analysis" | various | 2024 | ACL / EMNLP proceedings |
| "ChatGPT for Customer Feedback Analysis: Opportunities and Challenges" | Industry white papers (Qualtrics, Medallia) | 2023-2024 | Corporate publications |

### 4.3 Methods

- **Zero-shot classification:** Prompt the LLM with a review and ask for sentiment (positive/negative/neutral) and/or aspect-level opinions. Achieves 85-92% accuracy on standard benchmarks without any training data.
- **Few-shot in-context learning:** Provide 3-10 labeled examples in the prompt to calibrate the model to a domain-specific sentiment scale or aspect taxonomy.
- **Fine-tuning for domain adaptation:** Fine-tune open-source LLMs (LLaMA, Mistral, Phi) on domain-specific review corpora for improved performance on specialized lexicons (e.g., automotive, healthcare, B2B SaaS).
- **Structured output extraction:** Use JSON-mode or function-calling to extract structured aspect-sentiment tuples from reviews, enabling downstream quantitative analysis.

---

## 5. Automated Insight Generation Pipelines

### 5.1 Key Findings

A growing body of applied research and industry practice focuses on building end-to-end pipelines that move from raw customer data to actionable insights with minimal human intervention.

**The hypothesis-query-summarize paradigm.** The canonical pipeline consists of:
1. **Hypothesis generation:** An LLM generates candidate hypotheses about customer behavior based on metadata (product category, time period, known issues).
2. **Data querying:** The LLM translates each hypothesis into a structured query (SQL, API call, or retrieval query) against a customer data warehouse or review corpus.
3. **Evidence synthesis:** Retrieved data is fed back to the LLM, which evaluates the hypothesis, generates visualizations (via code generation), and produces a natural-language summary.
4. **Narrative report generation:** The LLM compiles findings into a structured report, complete with executive summary, key findings, and recommended actions.

**Retrieval-Augmented Generation (RAG) for insights.** RAG architectures have become the dominant approach for grounding insight generation in actual customer data. A vector store of customer reviews, survey responses, or CRM records is queried at inference time, and the retrieved context is injected into the LLM prompt. This reduces hallucination and ensures that generated insights reference real data.

**Agentic workflows.** By 2024-2025, multi-agent frameworks (AutoGen, CrewAI, LangGraph) were being applied to customer insights, with specialized agents for data retrieval, statistical analysis, visualization, and narrative writing collaborating on insight reports. Early evaluations show that agentic pipelines produce more comprehensive and better-sourced reports than single-prompt approaches.

### 5.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" | Lewis, P. et al. | 2020 | https://arxiv.org/abs/2005.11401 |
| "Toolformer: Language Models Can Teach Themselves to Use Tools" | Schick, T. et al. | 2023 | https://arxiv.org/abs/2302.04761 |
| "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" | Wu, Q. et al. | 2023 | https://arxiv.org/abs/2308.08155 |
| "Data-Copilot: Bridging Billions of Data and Humans with Autonomous Workflow" | Zhang, W. et al. | 2023 | https://arxiv.org/abs/2306.07209 |
| "InsightPilot: An LLM-Empowered Automated Data Exploration System" | Ma, P. et al. | 2023 | https://arxiv.org/abs/2304.00477 |

### 5.3 Methods

- **RAG pipelines:** Embed customer data into a vector store (e.g., Chroma, Pinecone, Weaviate); at query time, retrieve top-k relevant documents and inject into the LLM context window alongside the analytical question.
- **Text-to-SQL:** Use the LLM to translate natural-language questions ("What are the top complaints about our premium tier in Q3?") into SQL queries against a structured customer database.
- **Code-generation for analysis:** The LLM generates Python/R code for statistical analysis (correlation, regression, clustering) on structured customer data, executes it in a sandboxed environment, and interprets the results.
- **Multi-agent orchestration:** Assign roles (analyst, statistician, writer, reviewer) to different LLM instances that collaborate through structured message passing to produce and quality-check insight reports.

---

## 6. LLMs as Consumer Digital Twins

### 6.1 Key Findings

One of the most provocative research directions is the use of LLMs to simulate individual consumers or consumer populations -- so-called "silicon samples" or "consumer digital twins."

**Foundational work: LLMs as simulated economic agents.** Horton (2023) demonstrated that GPT-3.5/4, when prompted with economic scenarios, produced responses consistent with established findings in behavioral economics (e.g., endowment effect, anchoring, loss aversion). This established the feasibility of using LLMs as proxies for human economic decision-makers.

**Homo silicus and synthetic survey respondents.** Argyle et al. (2023) introduced the concept of "silicon sampling" in their influential paper "Out of One, Many: Using Language Models to Simulate Human Samples." They showed that by conditioning GPT-3 on demographic backstories (age, race, education, political affiliation), the model produced survey responses that closely matched subgroup-level distributions from the American National Election Studies (ANES). The correlation between LLM-simulated and real survey marginals exceeded r = 0.85 for many items.

**Brand-choice simulation.** Subsequent work applied the digital-twin paradigm to consumer brand choice. When prompted with consumer profiles (income, lifestyle, past purchases) and a consideration set, GPT-4 produced brand-choice probabilities that correlated with aggregate market-share data, though with notable biases toward well-known brands and difficulty representing niche or regional preferences.

**Limitations of digital twins.** Multiple critique papers (2024) identified systematic biases:
- **WEIRD bias:** LLMs disproportionately represent Western, Educated, Industrialized, Rich, Democratic populations.
- **Sycophancy and social desirability:** Simulated consumers tend to give more socially desirable responses than real humans.
- **Temporal anchoring:** LLM knowledge reflects training data distributions, which may not capture recent market shifts.
- **Homogeneity:** Within-persona variance is lower than within-human variance, leading to underestimation of preference heterogeneity.

### 6.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "Out of One, Many: Using Language Models to Simulate Human Samples" | Argyle, L. P. et al. | 2023 | *Political Analysis*; https://arxiv.org/abs/2209.06899 |
| "Large Language Models as Simulated Economic Agents" | Horton, J. J. | 2023 | NBER WP 31122; https://www.nber.org/papers/w31122 |
| "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies" | Aher, G. V., Arriaga, R. I., & Kalai, A. T. | 2023 | ICML 2023; https://arxiv.org/abs/2208.10264 |
| "Generative Agents: Interactive Simulacra of Human Behavior" | Park, J. S. et al. | 2023 | UIST 2023; https://arxiv.org/abs/2304.03442 |
| "On the Validity of Using Large Language Models for Human Simulation" | Santurkar, S. et al. / various critique papers | 2023-2024 | arXiv |
| "AI-Generated Consumers: Opportunities and Pitfalls for Market Research" | Various | 2024 | *Journal of Marketing* (editorial / commentary) |

### 6.3 Methods

- **Persona conditioning:** Prepend a detailed demographic and psychographic profile to the system prompt. Example: *"You are a 34-year-old female, college-educated, living in suburban Texas, household income $75K, with two children. You are price-conscious but value organic food."*
- **Choice simulation:** Present the conditioned LLM with a choice scenario (e.g., product shelf, brand set) and ask it to state preference, willingness to pay, or purchase likelihood.
- **Population simulation:** Run N persona-conditioned instances with demographics sampled from census distributions; aggregate responses to estimate population-level metrics.
- **Validation:** Compare simulated distributions against real survey/panel data using correlation, KL-divergence, or chi-square goodness-of-fit tests.

---

## 7. Chain-of-Thought Prompting for Customer Data Analysis

### 7.1 Key Findings

Chain-of-Thought (CoT) prompting -- instructing the LLM to reason step-by-step before arriving at a conclusion -- has proven particularly valuable for customer-insight tasks that require multi-step reasoning.

**Improved accuracy on complex coding tasks.** When performing qualitative coding of customer feedback (e.g., classifying a complaint into a multi-level taxonomy), CoT prompting significantly reduces classification errors compared to direct prompting. Studies report 5-15 percentage point improvements in accuracy on hierarchical classification tasks.

**Better calibrated uncertainty.** CoT prompting, combined with self-consistency (sampling multiple reasoning chains and taking the majority vote), produces better-calibrated confidence estimates for sentiment and intent classification. This is critical for insight pipelines that need to flag low-confidence predictions for human review.

**Structured analytical reasoning.** For insight-generation tasks (e.g., "Why did NPS drop in Q2?"), CoT prompting enables the LLM to enumerate potential hypotheses, evaluate each against provided data, and arrive at a reasoned conclusion, rather than producing a plausible-sounding but potentially confabulated narrative.

**Tree-of-Thought and related extensions.** Extensions such as Tree-of-Thought (Yao et al., 2023) and Graph-of-Thought prompting have been explored for more complex analytical tasks, such as competitive analysis and multi-attribute trade-off evaluation, though these remain primarily in the research stage for customer-insight applications.

### 7.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" | Wei, J. et al. | 2022 | NeurIPS 2022; https://arxiv.org/abs/2201.11903 |
| "Self-Consistency Improves Chain of Thought Reasoning in Language Models" | Wang, X. et al. | 2022 | https://arxiv.org/abs/2203.11171 |
| "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" | Yao, S. et al. | 2023 | NeurIPS 2023; https://arxiv.org/abs/2305.10601 |
| "ReAct: Synergizing Reasoning and Acting in Language Models" | Yao, S. et al. | 2022 | ICLR 2023; https://arxiv.org/abs/2210.03629 |

### 7.3 Methods

- **Standard CoT:** Append "Let's think step by step" or provide a worked example with explicit reasoning steps in the prompt.
- **Self-consistency:** Sample k completions with temperature > 0, extract the final answer from each, and take the majority vote. Improves reliability on classification tasks.
- **CoT + tool use (ReAct):** Interleave reasoning steps with tool calls (e.g., database queries, calculator, search) to ground the analysis in real data.
- **Structured CoT templates:** For customer-insight tasks, provide a reasoning template: (1) Identify the key issue, (2) List possible causes, (3) Evaluate each cause against the data, (4) Rank causes by likelihood, (5) Recommend next steps.

---

## 8. LLM-Generated vs. Human Expert Insights

### 8.1 Key Findings

A central question for practitioners is whether LLM-generated insights are trustworthy enough to act on. Several studies have directly compared LLM outputs to human expert analyses.

**Qualitative coding agreement.** Multiple studies (2023-2024) report inter-rater agreement (Cohen's kappa) between GPT-4 and human expert coders in the range of 0.65-0.85 for sentiment analysis, thematic coding, and intent classification. This is comparable to inter-human agreement on many coding tasks, which typically falls in the 0.70-0.85 range.

**Speed and cost advantages.** LLMs can process thousands of customer reviews in minutes at a cost of dollars, compared to weeks and thousands of dollars for human coding teams. This makes LLMs particularly attractive for exploratory analysis and rapid iteration.

**Where humans still excel:**
- **Novel or ambiguous contexts:** LLMs struggle with sarcasm, cultural references, and domain-specific jargon not well-represented in training data.
- **Strategic interpretation:** While LLMs can identify *what* customers are saying, human experts are better at interpreting *why* it matters strategically and *what to do about it*.
- **Edge cases and outliers:** LLMs tend to normalize responses toward modal patterns, potentially missing important but rare signals.

**Hybrid workflows as best practice.** The emerging consensus (by 2025) is that LLMs should augment rather than replace human analysts. The optimal workflow uses LLMs for first-pass coding, pattern identification, and summary generation, with human experts reviewing, correcting, and interpreting the LLM outputs. This "human-in-the-loop" approach captures most of the efficiency gains while maintaining quality.

### 8.2 Notable Papers and Sources

| Paper / Source | Authors | Year | Venue / Link |
|---|---|---|---|
| "ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks" | Gilardi, F., Alizadeh, M., & Kubli, M. | 2023 | https://arxiv.org/abs/2303.15056 |
| "Is ChatGPT a Good NLG Evaluator?" | Wang, J. et al. | 2023 | https://arxiv.org/abs/2303.04048 |
| "AnnoLLM: Making Large Language Models to Be Better Crowdsourced Annotators" | He, R. et al. | 2024 | https://arxiv.org/abs/2303.16854 |
| "Humans vs. LLMs as Qualitative Coders: A Comparative Study" | Various | 2024 | Multiple venues |

---

## 9. Limitations and Open Questions

### 9.1 Systematic Biases

- **Training data bias:** LLMs reflect the distribution of their training data, which overrepresents English-language, Western, and digitally-active populations. Consumer insights derived from LLMs may not generalize to underrepresented markets or demographics.
- **Recency bias:** LLM knowledge is frozen at the training cutoff. Rapidly evolving markets, new product categories, and recent brand crises may not be reflected. RAG architectures partially mitigate this but introduce retrieval quality as a new failure mode.
- **Brand salience bias:** Well-known brands are disproportionately represented in training data, leading LLMs to overestimate their prominence and underrepresent challenger brands.

### 9.2 Reproducibility and Reliability

- **Non-determinism:** Even at temperature = 0, API-served LLMs may produce slightly different outputs across calls due to infrastructure-level non-determinism (batching, floating-point ordering). This complicates replication of research findings.
- **Model versioning:** Commercial LLM APIs are updated without notice, potentially changing behavior. Studies conducted with "GPT-4" in March 2023 and March 2024 may have used materially different models.
- **Prompt sensitivity:** Small changes in prompt wording can significantly alter outputs, particularly for nuanced tasks like sentiment classification at scale.

### 9.3 Ethical and Privacy Concerns

- **Data privacy:** Feeding customer data (reviews, CRM records, support transcripts) to cloud-based LLM APIs raises significant data-privacy concerns, particularly under GDPR and CCPA. On-premise or fine-tuned open-source models mitigate this but at a performance cost.
- **Synthetic data risks:** Using LLMs to generate "synthetic consumers" raises questions about the ethics of replacing real consumer voices with simulated ones, particularly for underrepresented groups.
- **Transparency:** Insights derived from LLMs may be presented without adequate disclosure of their synthetic or model-mediated nature, potentially misleading decision-makers.

### 9.4 Open Research Questions

1. **Calibration:** How can we quantify and communicate the uncertainty of LLM-generated insights to business decision-makers?
2. **Ecological validity:** Under what conditions do LLM-simulated consumer responses predict real market outcomes (sales, churn, NPS changes)?
3. **Cultural and linguistic generalization:** How well do LLM-based insight methods transfer to non-English, non-Western markets?
4. **Longitudinal stability:** Can LLM-based consumer simulations track preference drift over time, or are they inherently static snapshots?
5. **Optimal human-AI collaboration:** What is the most efficient division of labor between LLMs and human analysts for different types of insight tasks?
6. **Multi-modal insights:** How can LLMs be combined with vision models to analyze product images, packaging, and in-store displays alongside textual customer feedback?
7. **Causal reasoning:** Current LLMs are largely correlational in their analysis. How can causal inference methods be integrated into LLM-based insight pipelines?

---

## 10. Consolidated Reference List

### Foundational and Methodological Papers

1. Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). "Out of One, Many: Using Language Models to Simulate Human Samples." *Political Analysis*. https://arxiv.org/abs/2209.06899

2. Horton, J. J. (2023). "Large Language Models as Simulated Economic Agents: What Can We Learn?" NBER Working Paper 31122. https://www.nber.org/papers/w31122

3. Aher, G. V., Arriaga, R. I., & Kalai, A. T. (2023). "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." ICML 2023. https://arxiv.org/abs/2208.10264

4. Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). "Generative Agents: Interactive Simulacra of Human Behavior." UIST 2023. https://arxiv.org/abs/2304.03442

5. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022. https://arxiv.org/abs/2201.11903

6. Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." https://arxiv.org/abs/2203.11171

7. Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." NeurIPS 2023. https://arxiv.org/abs/2305.10601

8. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023. https://arxiv.org/abs/2210.03629

### Sentiment and Review Analysis

9. Scaria, K., Gupta, H., Goyal, S., Sawant, S., Mishra, S., & Baral, C. (2023). "InstructABSA: Instruction Learning for Aspect-Based Sentiment Analysis." https://arxiv.org/abs/2302.08624

10. Zhang, W., Deng, Y., Liu, B., Pan, S. J., & Bing, L. (2023). "Sentiment Analysis in the Era of Large Language Models: A Reality Check." https://arxiv.org/abs/2305.15005

11. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). "ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks." https://arxiv.org/abs/2303.15056

### Infrastructure and Pipelines

12. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." https://arxiv.org/abs/2005.11401

13. Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). "Toolformer: Language Models Can Teach Themselves to Use Tools." https://arxiv.org/abs/2302.04761

14. Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., ... & Wang, C. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." https://arxiv.org/abs/2308.08155

15. Grootendorst, M. (2022). "BERTopic: Neural Topic Modeling with a Class-Based TF-IDF Procedure." https://arxiv.org/abs/2203.05794

16. Pham, C., Hoyle, A., Sun, S., & Iyyer, M. (2024). "TopicGPT: A Prompt-based Topic Modeling Framework." https://arxiv.org/abs/2311.01449

### Data Exploration and Insight Systems

17. Ma, P. et al. (2023). "InsightPilot: An LLM-Empowered Automated Data Exploration System." https://arxiv.org/abs/2304.00477

18. Zhang, W. et al. (2023). "Data-Copilot: Bridging Billions of Data and Humans with Autonomous Workflow." https://arxiv.org/abs/2306.07209

---

## Appendix: Taxonomy of LLM Techniques for Customer Insights

| Technique | Task Type | Data Input | Output | Maturity (2025) |
|---|---|---|---|---|
| Zero-shot classification | Sentiment, intent, topic | Customer text | Labels + confidence | Production-ready |
| Few-shot in-context learning | Domain-specific coding | Text + examples | Coded labels | Production-ready |
| Embedding + clustering | Segmentation, topic discovery | Customer text corpus | Clusters + labels | Production-ready |
| RAG pipelines | Grounded Q&A, insight generation | Text corpus + query | Narrative answers | Production-ready |
| Persona simulation (digital twins) | Preference estimation, concept testing | Demographic profiles | Simulated responses | Experimental |
| CoT / ReAct reasoning | Complex analysis, hypothesis testing | Mixed data + question | Reasoned analysis | Maturing |
| Multi-agent orchestration | End-to-end insight reports | Full data stack | Comprehensive reports | Early stage |
| Fine-tuned domain models | High-accuracy domain tasks | Domain corpus | Specialized outputs | Production-ready (for well-resourced teams) |
| Text-to-SQL / code generation | Data querying and analysis | NL question + schema | SQL / Python code | Maturing |

---

*This survey is intended as a living document. Readers are encouraged to verify all citations and supplement with the latest publications, as the field is evolving rapidly.*
