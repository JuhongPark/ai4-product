# AI for Product Discovery: A Comprehensive Research Survey

**Compiled: March 2026**
**Scope: 2022--2025 literature and industry developments**

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [AI-Assisted Scientific Discovery Leading to Product Innovation](#1-ai-assisted-scientific-discovery-leading-to-product-innovation)
3. [Generative AI Revolutionizing Commercial Product Discovery](#2-generative-ai-revolutionizing-commercial-product-discovery)
4. [AI-Powered Recommendation and Search for Product Discovery](#3-ai-powered-recommendation-and-search-for-product-discovery)
5. [Conversational AI and Chatbot-Driven Product Discovery](#4-conversational-ai-and-chatbot-driven-product-discovery)
6. [Impact on Patent Filings and Downstream Innovation](#5-impact-on-patent-filings-and-downstream-innovation)
7. [Consumer Behavior Changes and Gen Z Trends](#6-consumer-behavior-changes-and-gen-z-trends)
8. [Industry Perspectives: BCG, McKinsey, and Others](#7-industry-perspectives-bcg-mckinsey-and-others)
9. [Methods and Approaches](#8-methods-and-approaches)
10. [Limitations and Open Questions](#9-limitations-and-open-questions)
11. [Consolidated Reference List](#10-consolidated-reference-list)

---

## Executive Summary

"AI for Product Discovery" spans two interconnected domains: (1) the use of artificial intelligence to accelerate scientific and materials discovery that leads to new physical products (drugs, materials, chemicals), and (2) the use of AI---particularly generative AI, large language models (LLMs), and deep learning---to transform how consumers discover, evaluate, and purchase commercial products (e-commerce search, recommendation, conversational shopping). Between 2022 and 2025, both domains experienced transformative breakthroughs. In scientific discovery, AI systems such as DeepMind's GNoME discovered millions of new stable materials, and generative models dramatically shortened drug-candidate identification timelines. In commercial product discovery, the rise of ChatGPT and multimodal LLMs redefined e-commerce search, enabling conversational and intent-driven shopping experiences. This report surveys the key findings, methods, notable papers, industry perspectives, and open questions across the full landscape.

---

## 1. AI-Assisted Scientific Discovery Leading to Product Innovation

### 1.1 Materials Discovery

One of the most striking demonstrations of AI-driven product discovery in the physical sciences came from DeepMind's **Graph Networks for Materials Exploration (GNoME)** project. Published in *Nature* in November 2023, GNoME used graph neural networks (GNNs) trained on materials data to predict the stability of inorganic crystals, identifying **2.2 million new stable crystal structures**---including 381,000 that were subsequently added to existing materials databases. This expanded the known stable materials by an order of magnitude and opened pathways for new battery materials, superconductors, and catalysts.

- **Key Paper:** Merchant, A., Batzner, S., Schoenholz, S. S., Aykol, M., Cheon, G., & Cubuk, E. D. (2023). "Scaling deep learning for materials discovery." *Nature*, 624, 80--85. https://doi.org/10.1038/s41586-023-06735-9

Complementary work at the **Lawrence Berkeley National Laboratory** used an autonomous robotic lab (the A-Lab) to synthesize materials predicted by GNoME, demonstrating a closed-loop AI-to-synthesis pipeline.

- **Key Paper:** Szymanski, N. J., Rendy, B., Fei, Y., Kumar, R. E., He, T., Milber, D., ... & Ceder, G. (2023). "An autonomous laboratory for the accelerated synthesis of novel materials." *Nature*, 624, 86--91. https://doi.org/10.1038/s41586-023-06734-w

The **Materials Project** (materialsproject.org), an open-access database maintained by Lawrence Berkeley National Laboratory, has served as a foundational data resource for many of these AI-driven materials discovery efforts.

**MatterGen** from Microsoft Research (2024) represented a further advance, using a diffusion-based generative model to design novel inorganic materials with specified properties---moving beyond screening toward de novo materials generation.

- **Key Paper:** Zeni, C., Pinsler, R., Zügner, D., Fowber, A., Horber, M., Fu, C., ... & Shoghi, N. (2024). "MatterGen: A Generative Model for Inorganic Materials Design." arXiv:2312.03687. https://arxiv.org/abs/2312.03687

### 1.2 Drug Discovery

AI-driven drug discovery has been a primary vector for product innovation. **Insilico Medicine** became a landmark case when its AI-designed drug candidate for idiopathic pulmonary fibrosis (IPF), **INS018_055**, entered Phase II clinical trials in 2023---the first fully AI-discovered drug to reach this stage. The molecule was identified and optimized entirely through generative chemistry models.

- **Key Reference:** Insilico Medicine. "INS018_055 Phase II Trials." https://insilico.com/pipeline

**AlphaFold 2** (Jumper et al., 2021, *Nature*) and its successor **AlphaFold 3** (Abramson et al., 2024, *Nature*) revolutionized protein structure prediction, providing the structural biology foundation on which many drug discovery campaigns now rely. AlphaFold 3 extended prediction to protein-ligand, protein-nucleic acid, and protein-protein complexes.

- **Key Paper:** Jumper, J., Evans, R., Pritzel, A., et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature*, 596, 583--589. https://doi.org/10.1038/s41586-021-03819-2
- **Key Paper:** Abramson, J., Adler, J., Dunger, J., et al. (2024). "Accurate structure prediction of biomolecular interactions with AlphaFold 3." *Nature*, 630, 493--500. https://doi.org/10.1038/s41586-024-07487-w

Generative approaches to molecular design have proliferated. **Diffusion models for molecular generation** emerged as a dominant paradigm in 2023--2024, with models such as:

- **DiffSBDD** (Schneuing et al., 2023) for structure-based drug design using 3D equivariant diffusion.
- **Equivariant Flow Matching** approaches for generating drug-like molecules conditioned on protein pockets.

The broader impact is documented in several survey papers:

- **Key Survey:** Deng, J., Yang, Z., Ojima, I., Samaras, D., & Wang, F. (2022). "Artificial intelligence in drug discovery: applications and techniques." *Briefings in Bioinformatics*, 23(1), bbab430. https://doi.org/10.1093/bib/bbab430
- **Key Survey:** Jayatunga, M. K. P., Xie, W., Ruder, L., Schulze, U., & Meier, C. (2022). "AI in small-molecule drug discovery: a coming wave?" *Nature Reviews Drug Discovery*, 21, 175--176. https://doi.org/10.1038/d41573-022-00025-1

### 1.3 Chemical and Catalyst Discovery

Google DeepMind and collaborators applied AI to discover new electrocatalysts for hydrogen fuel cells and related clean-energy applications through the **Open Catalyst Project**, a collaboration between Meta AI (FAIR) and Carnegie Mellon University.

- **Key Paper:** Chanussot, L., Das, A., Goyal, S., et al. (2021). "Open Catalyst 2020 (OC20) Dataset and Community Challenges." *ACS Catalysis*, 11(10), 6059--6072. https://doi.org/10.1021/acscatal.0c04525
- **Updated Dataset:** Tran, R., Lan, J., Shuaibi, M., et al. (2023). "The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts." *ACS Catalysis*, 13, 3066--3084. https://doi.org/10.1021/acscatal.2c05426

---

## 2. Generative AI Revolutionizing Commercial Product Discovery

### 2.1 The LLM Inflection Point in E-Commerce

The release of ChatGPT (November 2022) and subsequent large language models fundamentally altered consumer product discovery. By 2024, major e-commerce platforms had integrated generative AI into their search and browsing experiences:

- **Amazon** launched **Rufus** (February 2024), an LLM-powered shopping assistant embedded in the Amazon app that answers product questions, compares items, and provides recommendations via natural language conversation.
- **Google** integrated generative AI into **Google Shopping** via its Search Generative Experience (SGE), later rebranded as **AI Overviews**, which synthesizes product information, reviews, and comparisons directly in search results.
- **Shopify** released **Shopify Magic** and **Sidekick**, AI tools that assist merchants with product descriptions, and consumers with AI-driven storefront experiences.
- **Walmart** deployed generative AI search capabilities enabling customers to search by use case (e.g., "I need supplies for a kids' birthday party") rather than by specific product keywords.

### 2.2 Visual and Multimodal Product Discovery

Multimodal AI models capable of processing text, images, and video have enabled new product discovery paradigms:

- **Visual search** (e.g., Google Lens, Pinterest Lens, Amazon StyleSnap) allows users to photograph or screenshot items and find similar products.
- **CLIP** (Radford et al., 2021, OpenAI) and its successors enabled zero-shot image-text matching that underpins many visual product search systems.
  - Radford, A., Kim, J. W., Hallacy, C., et al. (2021). "Learning Transferable Visual Models From Natural Language Supervision." *ICML 2021*. https://arxiv.org/abs/2103.00020
- Multimodal LLMs (GPT-4V, Gemini, Claude) can analyze product images and provide detailed descriptions, comparisons, and recommendations.

### 2.3 Social Commerce and AI-Driven Discovery

TikTok Shop and Instagram Shopping leveraged AI-powered content recommendation algorithms to create a new paradigm of **discovery commerce**---where users discover products through algorithmically curated content feeds rather than through intentional search. By 2024, TikTok Shop generated an estimated $20+ billion in global GMV, largely driven by AI recommendation of short-form video content featuring products.

---

## 3. AI-Powered Recommendation and Search for Product Discovery

### 3.1 Evolution of Recommendation Systems (2022--2025)

The period saw a transition from traditional collaborative filtering and matrix factorization toward foundation-model-based recommendation:

**Key architectural shifts:**

1. **Two-tower models with dense retrieval:** Using separate encoders for users and items, with approximate nearest neighbor (ANN) search for candidate retrieval. Widely adopted at Google, Meta, and Amazon.

2. **Sequential recommendation with Transformers:** Models like **SASRec** (Kang & McAuley, 2018) and **BERT4Rec** (Sun et al., 2019) were foundational, but the 2023--2025 period saw scaling these to billions of parameters.
   - Kang, W.-C., & McAuley, J. (2018). "Self-Attentive Sequential Recommendation." *ICDM 2018*. https://arxiv.org/abs/1808.09781
   - Sun, F., Liu, J., Wu, J., et al. (2019). "BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers." *CIKM 2019*. https://arxiv.org/abs/1904.06690

3. **LLM-based recommendation:** A major research direction in 2023--2025 explored using pre-trained LLMs directly for recommendation tasks:
   - **Key Paper:** Bao, K., Zhang, J., Zhang, Y., Wang, W., Feng, F., & He, X. (2023). "TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation." *RecSys 2023*. https://arxiv.org/abs/2305.00447
   - **Key Paper:** Hou, Y., Zhang, J., Lin, Z., Lu, H., Xie, R., McAuley, J., & Zhao, W. X. (2024). "Large Language Models are Zero-Shot Rankers for Recommender Systems." *ECIR 2024*. https://arxiv.org/abs/2305.08845
   - **Key Survey:** Wu, L., Zheng, Z., Qiu, Z., Wang, H., Gu, H., Shen, T., ... & He, X. (2024). "A Survey on Large Language Models for Recommendation." *World Wide Web*, 27, 60. https://arxiv.org/abs/2305.19860

4. **Graph Neural Networks for recommendation:** GNN-based approaches such as **PinSage** (Ying et al., 2018, KDD) at Pinterest and **LightGCN** (He et al., 2020, SIGIR) continued to be deployed at scale.

### 3.2 Semantic and Neural Product Search

Traditional keyword-based product search has been increasingly augmented or replaced by neural/semantic search:

- **Dense retrieval models** (e.g., based on BERT, Sentence-BERT) encode queries and product descriptions into shared embedding spaces.
- **Amazon** published work on their neural product search systems, moving toward understanding shopping intent rather than matching keywords.
  - **Key Paper:** Nigam, P., Song, Y., Mohan, V., et al. (2019). "Semantic Product Search." *KDD 2019*. https://arxiv.org/abs/1907.00937
- **Query understanding** using LLMs: Platforms now use LLMs to interpret ambiguous or conversational queries and map them to structured product attributes.

### 3.3 Retrieval-Augmented Generation (RAG) for Product Discovery

RAG architectures have become standard for product discovery systems that need to combine the fluency of generative models with the accuracy of product catalog data:

- A product catalog is indexed in a vector database.
- User queries are encoded and matched against catalog embeddings.
- Retrieved product information is fed as context to an LLM that generates natural language responses.

This approach mitigates hallucination risks inherent in pure generative approaches and ensures responses are grounded in real, available products.

---

## 4. Conversational AI and Chatbot-Driven Product Discovery

### 4.1 The Rise of Shopping Assistants

2023--2025 saw the deployment of conversational AI shopping assistants at unprecedented scale:

| Platform | Assistant | Launch | Capabilities |
|----------|-----------|--------|-------------|
| Amazon | Rufus | Feb 2024 | Product Q&A, comparison, recommendation |
| Shopify | Sidekick | Jul 2023 | Merchant-side AI assistant |
| Klarna | AI Assistant | Jan 2024 | Shopping, returns, customer service |
| Mercari | MercariAI | 2024 | Conversational listing and buying |
| Instacart | Ask Instacart | May 2023 | Meal planning, ingredient discovery |
| Google | Shopping AI | 2024 | Integrated into Search/SGE |

**Klarna** reported in February 2024 that its AI assistant (powered by OpenAI) handled two-thirds of all customer service chats in its first month---equivalent to the work of 700 full-time agents---and also served a product discovery function by helping users find and compare products.

### 4.2 Conversational Recommendation

Academic research on conversational recommendation systems (CRS) accelerated:

- **Key Survey:** Jannach, D., Manzoor, A., Cai, W., & Chen, L. (2021). "A Survey on Conversational Recommender Systems." *ACM Computing Surveys*, 54(5), 1--36. https://doi.org/10.1145/3453154
- **Key Paper:** Wang, L., & Lim, E.-P. (2023). "Zero-Shot Next-Item Recommendation using Large Pretrained Language Models." arXiv:2304.03153. https://arxiv.org/abs/2304.03153
- The integration of LLMs into CRS marked a paradigm shift from slot-filling dialog systems to open-ended, context-aware product conversations.

### 4.3 Agentic AI for Shopping

By late 2024 and into 2025, the concept of **AI agents** capable of autonomously browsing, comparing, and even purchasing products emerged:

- OpenAI's **Operator** (January 2025) demonstrated an AI agent that could navigate websites and complete shopping tasks.
- Google's **Project Mariner** explored browser-based AI agents.
- Academic benchmarks such as **WebShop** (Yao et al., 2022) provided standardized environments for evaluating AI shopping agents.
  - Yao, S., Chen, H., Yang, J., & Narasimhan, K. (2022). "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents." *NeurIPS 2022*. https://arxiv.org/abs/2207.01206

---

## 5. Impact on Patent Filings and Downstream Innovation

### 5.1 AI and Patent Trends

The intersection of AI and product innovation has had measurable effects on patent activity:

- **WIPO Technology Trends Report (2019, updated analysis through 2024):** The World Intellectual Property Organization documented exponential growth in AI-related patent filings, with machine learning and deep learning patents growing at over 25% CAGR from 2015 to 2023.
  - Source: https://www.wipo.int/tech_trends/en/artificial_intelligence/

- **USPTO AI Patent Landscape:** The United States Patent and Trademark Office reported that AI-related patent applications increased substantially, with particular growth in AI for drug discovery, materials science, and computer vision applications relevant to product identification.

- A 2024 study from the **National Bureau of Economic Research (NBER)** examined how AI affects the rate and direction of innovation:
  - **Key Paper:** Agrawal, A., McHale, J., & Oettl, A. (2024). "Artificial Intelligence and Scientific Discovery." *NBER Working Paper*. Related earlier work: https://www.nber.org/papers/w w31808

### 5.2 AI-Discovered Inventions and Patentability

The legal question of whether AI-generated inventions are patentable remained unresolved through 2025. The landmark **DABUS** case (Thaler v. Vidal) saw the U.S. Federal Circuit rule in August 2022 that an AI system cannot be listed as an inventor on a patent. Similar rulings occurred in the UK and EU, though South Africa and Australia (briefly) allowed AI-named patents. This has implications for AI-driven product discovery, as companies must ensure human inventorship in the discovery pipeline.

### 5.3 Accelerated Innovation Cycles

Companies using AI for product discovery reported compressed innovation timelines:

- **Insilico Medicine** reduced hit-to-lead identification from ~4.5 years to ~18 months using generative AI.
- In materials science, the traditional discovery-to-application cycle of 15--20 years is being compressed, with AI-assisted discovery potentially reducing this to 5--10 years.
- **BCG analysis (2024)** estimated that AI could reduce new product development timelines by 30--50% across industries including pharmaceuticals, consumer goods, and chemicals.

---

## 6. Consumer Behavior Changes and Gen Z Trends

### 6.1 Shift from Search to Discovery

A fundamental behavioral shift has been documented: consumers---especially younger demographics---increasingly **discover** products through AI-curated content rather than **searching** for them:

- **Google internal research (2022--2023)** noted that nearly 40% of young users preferred TikTok or Instagram over Google Search for discovering restaurants and products.
- The concept of **"serendipitous discovery"** powered by recommendation algorithms replaced deliberate search as a primary purchase trigger for categories like fashion, beauty, and food.

### 6.2 Gen Z and AI-Native Shopping

Gen Z (born 1997--2012) represents the first generation of consumers who are AI-native in their shopping behavior:

- **Surveys by Salesforce (2024)** and **McKinsey (2024)** found that Gen Z consumers are 2--3x more likely than older generations to use AI tools (chatbots, visual search, social commerce algorithms) in their purchase journey.
- **Trust dynamics:** While Gen Z is comfortable with AI-curated recommendations, studies show they place high value on authenticity and peer reviews, creating a tension between algorithmic and social trust signals.
- **"TikTok Made Me Buy It"** became a cultural phenomenon, with the hashtag accumulating over 70 billion views by 2024, illustrating algorithmic product discovery at massive scale.

### 6.3 Personalization Expectations

Consumer expectations for personalization have escalated:

- A **McKinsey report (2023)** found that 71% of consumers expect personalized interactions from companies, and 76% get frustrated when this does not happen.
  - Source: McKinsey & Company. "The value of getting personalization right---or wrong---is multiplying." https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-value-of-getting-personalization-right-or-wrong-is-multiplying
- AI-powered personalization in product discovery has moved from segment-level to individual-level, with real-time adaptation based on browsing behavior, context, and stated preferences.

---

## 7. Industry Perspectives: BCG, McKinsey, and Others

### 7.1 Boston Consulting Group (BCG)

BCG has published extensively on AI for product innovation and discovery:

- **"How Generative AI Will Transform Product Innovation" (2024):** BCG argued that GenAI would reshape the full product lifecycle---from ideation through design, testing, and launch. Key claims included a 30--50% reduction in concept-to-market timelines and the ability to generate thousands of product concepts for rapid screening.
  - Source: https://www.bcg.com/publications/2024/how-generative-ai-transforms-product-innovation

- **BCG Henderson Institute** published research on AI as a "general-purpose technology" that enhances innovation across sectors, drawing parallels to electrification and computing.

- **BCG x MIT Sloan (2024):** A joint study found that companies deriving the most value from AI were those that integrated it into core product development processes rather than treating it as a standalone tool.

### 7.2 McKinsey & Company

- **"The State of AI in 2024" (McKinsey Global Survey, 2024):** This annual survey found that 72% of organizations had adopted AI in at least one business function (up from 50% in 2022), with product development and marketing being among the fastest-growing use cases.
  - Source: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

- **"The Economic Potential of Generative AI" (McKinsey, June 2023):** Estimated that generative AI could add $2.6--$4.4 trillion annually to the global economy, with significant impact on product R&D (estimated $60--110 billion in value for pharmaceutical and medical products alone).
  - Source: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier

- McKinsey's research highlighted that AI was shifting product discovery from a hypothesis-driven process to an **exploration-driven** process, where AI systems canvas vast solution spaces that humans could never explore manually.

### 7.3 Gartner

- **Gartner (2024)** identified "AI-Augmented Development" and "Intelligent Applications" as key trends in its Hype Cycle for Emerging Technologies. Gartner predicted that by 2027, 80% of e-commerce platforms would incorporate generative AI in their product discovery workflows.

### 7.4 Forrester

- **Forrester (2024)** published research noting that AI-powered product discovery was shifting retail competitive advantage from inventory breadth to **curation quality**---the ability to surface the right product for the right customer at the right time.

### 7.5 Accenture

- **Accenture Technology Vision (2024)** highlighted the concept of a "digital twin of the customer" enabled by AI, which continuously models individual consumer preferences to anticipate product discovery needs before explicit search behavior occurs.

---

## 8. Methods and Approaches

### 8.1 Foundation Models and Large Language Models

| Method | Application | Key Examples |
|--------|------------|--------------|
| Autoregressive LLMs (GPT-4, Claude, Gemini) | Conversational product search, query understanding, product description generation | Amazon Rufus, Google Shopping AI |
| Instruction-tuned LLMs | Zero-shot and few-shot product recommendation, attribute extraction | TALLRec, Chat-Rec |
| Multimodal LLMs (GPT-4V, Gemini) | Visual product search, image-based Q&A | Google Lens integration |

### 8.2 Embedding and Retrieval Methods

- **Dense retrieval** using bi-encoder architectures (Sentence-BERT, E5, GTE models)
- **Cross-encoder reranking** for precision in product search
- **Approximate Nearest Neighbor (ANN)** search using FAISS, ScaNN, HNSW algorithms
- **Retrieval-Augmented Generation (RAG)** for grounding product recommendations in real catalog data

### 8.3 Graph-Based Methods

- **Graph Neural Networks (GNNs):** PinSage (Pinterest), Alibaba's graph-based recommendation
- **Knowledge Graphs:** Product knowledge graphs connecting products, attributes, brands, categories, and user behavior
- **Heterogeneous Information Networks:** Combining user-item interactions, social signals, and content features

### 8.4 Generative Models for Scientific Discovery

- **Diffusion models:** Used for molecular generation (drug design), materials generation (MatterGen), and protein design (RFdiffusion)
  - Watson, J. L., Juergens, D., Bennett, N. R., et al. (2023). "De novo design of protein structure and function with RFdiffusion." *Nature*, 620, 1089--1100. https://doi.org/10.1038/s41586-023-06415-8
- **Variational Autoencoders (VAEs):** Used for molecular generation and latent-space exploration
- **Reinforcement Learning:** Applied to optimize molecular properties and navigate chemical space
- **Active learning:** Guiding experimental design in materials discovery to maximize information gain from limited experiments

### 8.5 Personalization Techniques

- **Contextual bandits and reinforcement learning** for real-time personalization
- **Federated learning** for privacy-preserving personalization across devices
- **User embedding models** that capture long-term preferences and short-term intent

### 8.6 Evaluation Frameworks

- **Offline metrics:** NDCG, Hit Rate, MRR for recommendation; MRR, Recall@K for retrieval
- **Online A/B testing:** Industry standard for evaluating product discovery changes
- **Human evaluation:** Increasingly important for assessing the quality of conversational product discovery
- **Benchmarks:** WebShop (Yao et al., 2022) for agentic shopping; Amazon Product Search datasets; RecBole framework for recommendation

---

## 9. Limitations and Open Questions

### 9.1 Hallucination and Factual Accuracy

Generative AI systems applied to product discovery can "hallucinate"---generating plausible but incorrect product information, fabricating features, or recommending non-existent products. This is particularly dangerous in:
- **Drug discovery:** False predictions of molecular stability or binding affinity can waste millions in wet-lab validation.
- **E-commerce:** Recommending products with fabricated specifications erodes consumer trust.

**Open question:** How can we provide formal guarantees of factual accuracy in generative product discovery systems? RAG mitigates but does not eliminate this problem.

### 9.2 Bias and Fairness

- Recommendation systems exhibit well-documented popularity biases, favoring established products and brands over niche or novel alternatives.
- AI-driven product discovery may reduce **serendipity** by creating filter bubbles, limiting consumer exposure to diverse products.
- In scientific discovery, AI models trained on existing data may perpetuate biases toward well-studied chemical spaces or protein families.

**Open question:** How do we design AI product discovery systems that balance personalization with diversity and fairness?

### 9.3 Explainability and Trust

- Consumers and regulators increasingly demand explanations for why specific products are recommended.
- In drug and materials discovery, understanding *why* an AI predicts a material is stable or a molecule is active is essential for scientific validation.
- The black-box nature of deep learning models remains a barrier.

**Open question:** Can we develop inherently interpretable AI systems for product discovery that maintain the performance of black-box models?

### 9.4 Evaluation Challenges

- Offline metrics for recommendation systems often do not correlate well with actual user satisfaction.
- Measuring the "quality" of product discovery is inherently subjective and context-dependent.
- Long-term effects of AI-driven discovery (e.g., reduced product diversity in the market, consumer deskilling) are difficult to measure.

### 9.5 Privacy and Data Governance

- Personalized product discovery requires extensive user data, raising privacy concerns.
- Regulations such as GDPR, CCPA, and the EU AI Act impose constraints on data use for personalization.
- The tension between personalization effectiveness and privacy protection remains unresolved.

### 9.6 Scientific Validity of AI Discoveries

- Many AI-predicted materials and molecules have not been experimentally validated.
- The gap between computational prediction and real-world synthesis/testing remains large.
- **Reproducibility** of AI-driven scientific discoveries is a growing concern.

**Open question:** What percentage of AI-discovered materials/molecules will prove practically useful, and how do we prioritize experimental validation?

### 9.7 Economic and Labor Market Impacts

- AI-driven product discovery automation raises questions about displacement of human experts (buyers, merchandisers, bench scientists).
- The concentration of AI capabilities in large technology companies may reduce competition in product discovery.
- Intellectual property frameworks have not fully adapted to AI-generated product innovations.

### 9.8 Agentic AI Risks

- Autonomous shopping agents raise concerns about manipulation, adversarial product listings designed to exploit AI agents, and loss of human agency in purchase decisions.
- The alignment of AI shopping agent objectives with actual consumer preferences is not guaranteed.

---

## 10. Consolidated Reference List

### Scientific Discovery

1. Merchant, A., Batzner, S., Schoenholz, S. S., et al. (2023). "Scaling deep learning for materials discovery." *Nature*, 624, 80--85. https://doi.org/10.1038/s41586-023-06735-9

2. Szymanski, N. J., Rendy, B., Fei, Y., et al. (2023). "An autonomous laboratory for the accelerated synthesis of novel materials." *Nature*, 624, 86--91. https://doi.org/10.1038/s41586-023-06734-w

3. Zeni, C., Pinsler, R., Zügner, D., et al. (2024). "MatterGen: A Generative Model for Inorganic Materials Design." arXiv:2312.03687. https://arxiv.org/abs/2312.03687

4. Jumper, J., Evans, R., Pritzel, A., et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature*, 596, 583--589. https://doi.org/10.1038/s41586-021-03819-2

5. Abramson, J., Adler, J., Dunger, J., et al. (2024). "Accurate structure prediction of biomolecular interactions with AlphaFold 3." *Nature*, 630, 493--500. https://doi.org/10.1038/s41586-024-07487-w

6. Watson, J. L., Juergens, D., Bennett, N. R., et al. (2023). "De novo design of protein structure and function with RFdiffusion." *Nature*, 620, 1089--1100. https://doi.org/10.1038/s41586-023-06415-8

7. Chanussot, L., Das, A., Goyal, S., et al. (2021). "Open Catalyst 2020 (OC20) Dataset and Community Challenges." *ACS Catalysis*, 11(10), 6059--6072. https://doi.org/10.1021/acscatal.0c04525

8. Tran, R., Lan, J., Shuaibi, M., et al. (2023). "The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts." *ACS Catalysis*, 13, 3066--3084. https://doi.org/10.1021/acscatal.2c05426

9. Deng, J., Yang, Z., Ojima, I., Samaras, D., & Wang, F. (2022). "Artificial intelligence in drug discovery: applications and techniques." *Briefings in Bioinformatics*, 23(1), bbab430. https://doi.org/10.1093/bib/bbab430

10. Jayatunga, M. K. P., Xie, W., Ruder, L., Schulze, U., & Meier, C. (2022). "AI in small-molecule drug discovery: a coming wave?" *Nature Reviews Drug Discovery*, 21, 175--176. https://doi.org/10.1038/d41573-022-00025-1

### Recommendation and Search

11. Kang, W.-C., & McAuley, J. (2018). "Self-Attentive Sequential Recommendation." *ICDM 2018*. https://arxiv.org/abs/1808.09781

12. Sun, F., Liu, J., Wu, J., et al. (2019). "BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers." *CIKM 2019*. https://arxiv.org/abs/1904.06690

13. Bao, K., Zhang, J., Zhang, Y., et al. (2023). "TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation." *RecSys 2023*. https://arxiv.org/abs/2305.00447

14. Hou, Y., Zhang, J., Lin, Z., et al. (2024). "Large Language Models are Zero-Shot Rankers for Recommender Systems." *ECIR 2024*. https://arxiv.org/abs/2305.08845

15. Wu, L., Zheng, Z., Qiu, Z., et al. (2024). "A Survey on Large Language Models for Recommendation." *World Wide Web*, 27, 60. https://arxiv.org/abs/2305.19860

16. Nigam, P., Song, Y., Mohan, V., et al. (2019). "Semantic Product Search." *KDD 2019*. https://arxiv.org/abs/1907.00937

17. Radford, A., Kim, J. W., Hallacy, C., et al. (2021). "Learning Transferable Visual Models From Natural Language Supervision." *ICML 2021*. https://arxiv.org/abs/2103.00020

### Conversational AI and Agents

18. Jannach, D., Manzoor, A., Cai, W., & Chen, L. (2021). "A Survey on Conversational Recommender Systems." *ACM Computing Surveys*, 54(5), 1--36. https://doi.org/10.1145/3453154

19. Wang, L., & Lim, E.-P. (2023). "Zero-Shot Next-Item Recommendation using Large Pretrained Language Models." arXiv:2304.03153. https://arxiv.org/abs/2304.03153

20. Yao, S., Chen, H., Yang, J., & Narasimhan, K. (2022). "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents." *NeurIPS 2022*. https://arxiv.org/abs/2207.01206

### Industry Reports

21. McKinsey & Company. (2023). "The economic potential of generative AI: The next productivity frontier." https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier

22. McKinsey & Company. (2024). "The state of AI in early 2024." https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

23. McKinsey & Company. (2023). "The value of getting personalization right---or wrong---is multiplying." https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-value-of-getting-personalization-right-or-wrong-is-multiplying

24. Boston Consulting Group. (2024). "How Generative AI Will Transform Product Innovation." https://www.bcg.com/publications/2024/how-generative-ai-transforms-product-innovation

25. WIPO. (2019; updated). "WIPO Technology Trends: Artificial Intelligence." https://www.wipo.int/tech_trends/en/artificial_intelligence/

### Patents and IP

26. *Thaler v. Vidal*, No. 21-2347 (Fed. Cir. 2022). U.S. Federal Circuit ruling on AI inventorship.

---

## Appendix: Taxonomy of AI for Product Discovery

```
AI for Product Discovery
├── Scientific / Physical Product Discovery
│   ├── Materials Discovery (GNoME, MatterGen, Open Catalyst)
│   ├── Drug Discovery (AlphaFold, Insilico Medicine, diffusion models)
│   ├── Chemical Discovery (catalyst design, reaction prediction)
│   └── Biological Design (protein engineering, RFdiffusion)
│
├── Commercial Product Discovery
│   ├── Search-Based Discovery
│   │   ├── Keyword search (traditional)
│   │   ├── Semantic/neural search (dense retrieval)
│   │   └── Visual search (CLIP, Google Lens)
│   ├── Recommendation-Based Discovery
│   │   ├── Collaborative filtering
│   │   ├── Content-based filtering
│   │   ├── Sequential recommendation (SASRec, BERT4Rec)
│   │   ├── GNN-based recommendation (PinSage, LightGCN)
│   │   └── LLM-based recommendation (TALLRec, Chat-Rec)
│   ├── Conversational Discovery
│   │   ├── Shopping assistants (Rufus, Klarna AI)
│   │   ├── Conversational recommender systems
│   │   └── Agentic shopping (Operator, WebShop)
│   └── Feed/Algorithm-Driven Discovery
│       ├── Social commerce (TikTok Shop, Instagram Shopping)
│       └── Personalized content feeds
│
└── Cross-Cutting Concerns
    ├── Evaluation and benchmarking
    ├── Fairness, bias, and diversity
    ├── Privacy and data governance
    ├── Explainability and trust
    └── Intellectual property and patents
```

---

*This report synthesizes publicly available academic literature, industry reports, and technology developments through early 2025. Some URLs may have changed or become inaccessible since original publication. Readers are encouraged to verify sources and check for updated versions of cited reports.*
