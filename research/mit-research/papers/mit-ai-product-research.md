# Comprehensive Survey of AI for Product Research across MIT Labs

> **Research Survey Document**
> Date: 2026-03-08
> Scope: AI x Product Lifecycle research by MIT research institutions (2022--2026)
> Part of: AI for Product Research Survey Project

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [MIT Sloan Management Review (SMR)](#2-mit-sloan-management-review-smr)
3. [MIT Initiative on the Digital Economy (IDE)](#3-mit-initiative-on-the-digital-economy-ide)
4. [MIT Sloan School of Management — Faculty Research](#4-mit-sloan-school-of-management--faculty-research)
5. [MIT CSAIL](#5-mit-csail)
6. [MIT Media Lab](#6-mit-media-lab)
7. [MIT Engineering and Design Labs](#7-mit-engineering-and-design-labs)
8. [MIT Economics — AI & Labor](#8-mit-economics--ai--labor)
9. [MIT SDM (System Design and Management)](#9-mit-sdm-system-design-and-management)
10. [MIT Generative AI Impact Consortium (MGAIC)](#10-mit-generative-ai-impact-consortium-mgaic)
11. [MIT Educational Programs](#11-mit-educational-programs)
12. [Mapping MIT Research to ai4-product Domains](#12-mapping-mit-research-to-ai4-product-domains)
13. [Sources](#13-sources)

---

## 1. Executive Summary

MIT has built a comprehensive ecosystem spanning academic research, industry-academia collaboration, and professional education for the application of AI to product development. Launched in 2025, the **MIT Generative AI Impact Consortium (MGAIC)** received 180 proposals from 250 faculty members and selected 55 seed grants, serving as a hub for AI for Product research.

### Key Findings

- **95% of generative AI pilots fail to deliver business impact** (MIT IDE/NANDA report, 2025) — root cause is organizational design, not technology
- **14% productivity improvement** — empirical study of 5,172 employees at a Fortune 500 company (Brynjolfsson, Li, Raymond, 2025)
- **80% of AI agent work is invisible work** — data engineering, stakeholder alignment, governance, etc. (Kellogg et al., 2025)
- **50% reduction in product development time** — GPT-4 + Midjourney combined use case (MIT SMR, 2024)

---

## 2. MIT Sloan Management Review (SMR)

### 2.1 "When Generative AI Meets Product Development" (2024)

- **Authors**: Tucker J. Marion, Mahdi Srour, Frank Piller
- **Published**: MIT Sloan Management Review, Fall 2024
- **URL**: https://sloanreview.mit.edu/article/when-generative-ai-meets-product-development/
- **Relevant Areas**: Discovery & User Research, Design & Prototyping
- **Key Findings**:
  - Three pathways for using generative AI in product development: (1) ideation, (2) market/customer insights, (3) user-friendly interfaces
  - Loft Design case study: 50% reduction in product development time by combining GPT-4 + Midjourney
  - AI is most effective in early exploration and conceptualization stages

### 2.2 Responsible AI Annual Survey Series (2022--2025, MIT SMR + BCG)

- **URL**: https://sloanreview.mit.edu/big-ideas/responsible-ai/
- **Relevant Areas**: Cross-cutting (Responsible AI)
- **Key Findings**:
  - Based on global executive surveys across 59 industries, 87 countries, with 1,240 respondents
  - 2023 report: warning about risks of third-party AI tools
  - Most organizations recognize responsible AI as important, but few actually prioritize it

### 2.3 "The Emerging Agentic Enterprise" (2025, MIT SMR + BCG)

- **URL**: https://sloanreview.mit.edu/projects/the-emerging-agentic-enterprise-how-leaders-must-navigate-a-new-age-of-ai/
- **Relevant Areas**: Management & Decision Making, Growth & Lifecycle
- **Key Findings**:
  - Analysis of four tensions faced by enterprises adopting agentic AI
  - Agentic AI emerging as the key issue in AI strategy for 2025

### 2.4 Five Key Trends in AI Strategy (2025)

- **URL**: https://www.prnewswire.com/news-releases/five-trends-in-ai-and-data-science-for-2025-from-mit-sloan-management-review-302345115.html
- **Relevant Areas**: Management & Decision Making
- **Key Findings**:
  1. The promise and hype of Agentic AI
  2. The urgency of measuring generative AI experiment outcomes
  3. Redefining data-driven culture
  4. The renewed importance of unstructured data
  5. The debate over data/AI C-suite leadership roles
  - 92% of respondents identified cultural and change management barriers as the biggest obstacle to AI adoption

### 2.5 "AI for Simulated User Research" (2025, MIT Sloan EdTech)

- **URL**: https://mitsloanedtech.mit.edu/2025/08/15/simulated-personas-real-insights-an-mit-sloan-students-perspective-on-ai-for-user-research/
- **Relevant Areas**: Discovery & User Research
- **Key Findings**:
  - Experiment using AI personas for user demand exploration in the "Generative AI for Managers" course
  - Useful for identifying early product risks before reaching real users
  - Cannot replace human input — positioned as a complementary tool

---

## 3. MIT Initiative on the Digital Economy (IDE)

> **Director**: Sinan Aral (MIT Sloan, David Austin Professor)
> **Co-founders**: Erik Brynjolfsson (currently Stanford), Andrew McAfee
> **URL**: https://ide.mit.edu/

### 3.1 "The GenAI Divide: State of AI in Business 2025"

- **Authors**: Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari (MIT NANDA)
- **Relevant Areas**: Growth & Lifecycle, Management & Decision Making
- **Key Findings**:
  - Analysis of over 300 AI initiatives, 52 structured interviews, 153 survey respondents
  - **95% of generative AI pilots fail to deliver business impact**
  - Poor results relative to $35-40 billion in investment
  - External vendor purchase/partnership success rate 67% vs. in-house build 33%
  - Core failure cause: organizational design, not technology

### 3.2 Pairit (MindMeld) Experimental Platform (2025)

- **Researchers**: Sinan Aral, Harang Ju
- **URL**: https://mitsloan.mit.edu/ideas-made-to-matter/4-new-studies-about-agentic-ai-mit-initiative-digital-economy
- **Relevant Areas**: Cross-cutting (Human-AI Collaboration)
- **Key Findings**:
  - Comparative experiment between human-human and human-AI pairs on collaborative tasks
  - Human-AI pairs: superior at text generation, inferior at image generation
  - AI agent "personality matching" contributes to collaboration optimization

### 3.3 Four Studies on Agentic AI (2025)

- **Lead Researchers**: Kate Kellogg (MIT Sloan), Sinan Aral, et al.
- **URL**: https://mitsloan.mit.edu/ideas-made-to-matter/4-new-studies-about-agentic-ai-mit-initiative-digital-economy
- **Relevant Areas**: Development & Engineering, Management & Decision Making
- **Key Findings**:
  - Experiment on AI agent detection of adverse effects in clinical records
  - **80% of work is "invisible work"** — data engineering, stakeholder alignment, governance, workflow integration
  - Empirically demonstrates the real-world complexity of implementing agentic AI

### 3.4 The 2025 AI Agent Index

- **URL**: https://aiagentindex.mit.edu/
- **Relevant Areas**: Development & Engineering, Cross-cutting (AI Frameworks)
- **Key Findings**:
  - Documentation of the origins, design, capabilities, ecosystem, and safety features of 30 major AI agents
  - Systematic classification based on publicly available information
  - In 2025, Google Scholar papers on "AI agent" exceeded the combined total of all previous years

### 3.5 MIT Conference on Digital Experimentation (CODE)

- **Host**: Sinan Aral
- **Relevant Areas**: Growth & Lifecycle (A/B testing, digital experimentation)
- **Key Findings**:
  - Research on large-scale digital experiment design, causal inference, and social network effects
  - Annual conference connecting academia and industry

---

## 4. MIT Sloan School of Management — Faculty Research

### 4.1 Danielle Li — "Generative AI at Work"

- **Position**: MIT Sloan Associate Professor of Management
- **Co-authors**: Erik Brynjolfsson (Stanford), Lindsey Raymond (MIT Sloan PhD)
- **Published**: Quarterly Journal of Economics, Vol. 140, Issue 2 (2025)
- **URL**: https://academic.oup.com/qje/article/140/2/889/7990658
- **Relevant Areas**: Development & Engineering, Growth & Lifecycle
- **Key Findings**:
  - Analysis of 3 million chat records from 5,172 customer support agents at a Fortune 500 company
  - **Average 14% productivity improvement with access to generative AI tools**
  - Greatest effect on less experienced, newer employees; minimal effect on highly skilled workers
  - Additional effects: reduction in customer verbal abuse and employee turnover

### 4.2 Thomas Malone — Collective Intelligence & Superminds

- **Position**: MIT Sloan Patrick J. McGovern Professor, Founding Director of the MIT Center for Collective Intelligence (CCI)
- **URL**: https://cci.mit.edu/malone/
- **Relevant Areas**: Management & Decision Making, Cross-cutting (Human-AI Collaboration)
- **Key Findings**:
  - Core question: "How can people and computers be connected so that collectively they act more intelligently than any individual, group, or computer?"
  - **"Superminds" concept**: Groups organized as hierarchies, communities, markets, and democracies combine with AI to achieve unprecedented collective intelligence
  - The key is dividing tasks so that humans and AI each do what they do best

### 4.3 Andrew McAfee — The Geek Way & AI Organizational Theory

- **Position**: MIT Principal Research Scientist, MIT IDE Co-founder
- **URL**: https://ide.mit.edu/people/andrew-mcafee/
- **Relevant Areas**: Management & Decision Making
- **Key Findings**:
  - **"Geek Way" management theory**: data/experiment-driven decision-making instead of HIPPO (Highest Paid Person's Opinion)
  - Emphasis on autonomous small teams, speed, and openness
  - Warning that bureaucratic organizations that fail to adapt in the AI era will become obsolete

### 4.4 Sinan Aral — Digital Experimentation & AI

- **Position**: MIT Sloan David Austin Professor, MIT IDE Director
- **URL**: https://www.sinanaral.io/
- **Relevant Areas**: Growth & Lifecycle, Management & Decision Making
- **Key Findings**:
  - World-leading authority in digital experimentation (A/B testing), social networks, and causal inference
  - Hosts MIT Conference on Digital Experimentation (CODE)
  - "Pareto Machines: Training AI Agents to Find Positive-Sum Solutions" project (MGAIC)

### 4.5 "Designing Human-AI Collaboration: A Sufficient-Statistic Approach" (2025)

- **URL**: https://economics.mit.edu/sites/default/files/2025-06/AI_Design__Sufficient_Statistics.pdf
- **Relevant Areas**: Cross-cutting (Human-AI Collaboration), Management & Decision Making
- **Key Findings**:
  - An economics-based approach to optimal human-AI collaboration design
  - Also published as an NBER Working Paper

### 4.6 Dean Eckles — Causal Inference & Social Networks

- **Position**: MIT Sloan Associate Professor, KDD Professor of Marketing
- **Relevant Areas**: Growth & Lifecycle (A/B testing, causal inference)
- **Key Findings**:
  - Research on network interference problems in large-scale online experiments
  - Development of AI-based causal inference methodologies
  - Research on product diffusion and virality in social networks

### 4.7 Duncan Simester — AI-Based Experimental Design

- **Position**: MIT Sloan NTU Professor of Marketing
- **Relevant Areas**: Growth & Lifecycle, Discovery & User Research
- **Key Findings**:
  - Optimization of experimental design using machine learning
  - Research on customer behavior prediction and personalization strategies
  - Analysis of heterogeneous treatment effects in large-scale field experiments

### 4.8 Catherine Tucker — AI Privacy & Policy

- **Position**: MIT Sloan Sloan Distinguished Professor of Management
- **Relevant Areas**: Cross-cutting (Responsible AI), Growth & Lifecycle
- **Key Findings**:
  - Research on the tension between data privacy and personalization in the AI era
  - Analysis of privacy regulation impacts on ad targeting and recommendation systems
  - Empirical research on the effects of regulations like GDPR on AI-based products

### 4.9 Retsef Levi — AI for Operations & Supply Chain

- **Position**: MIT Sloan J. Spencer Standish Professor
- **Relevant Areas**: Growth & Lifecycle (PLM), Development & Engineering
- **Key Findings**:
  - Research on AI-based supply chain risk management
  - MGAIC project: "GenAI for Software Supply Chain Risk Management"
  - Combining operations optimization with AI

### 4.10 John Hauser — Product Design & Voice of the Customer

- **Position**: MIT Sloan Kirin Professor of Marketing (Emeritus)
- **Relevant Areas**: Discovery & User Research, Design & Prototyping
- **Key Findings**:
  - Pioneer of the "Voice of the Customer" methodology
  - Framework for extracting customer needs in product design
  - **"Transforming the Voice of the Customer: LLMs for Identifying Customer Needs"** (Timoshenko, Mao & Hauser, 2026) — blind study with a marketing consulting firm on whether LLMs can replace traditional VOC methodologies
  - Research on AI/ML-based customer preference modeling

---

## 5. MIT CSAIL

> MIT Computer Science and Artificial Intelligence Laboratory
> URL: https://www.csail.mit.edu/

### 5.1 "Challenges and Paths Towards AI for Software Engineering" (2025)

- **Published**: ICML 2025 (Vancouver)
- **URL**: https://news.mit.edu/2025/can-ai-really-code-study-maps-roadblocks-to-autonomous-software-engineering-0716
- **Relevant Areas**: Development & Engineering
- **Key Findings**:
  - Mapping AI bottlenecks across the full spectrum of software engineering (refactoring, large-scale migrations, etc.), beyond just code generation
  - Points out that "reducing software engineering to undergraduate-level programming is a mistake"
  - Calls for new benchmarks that acknowledge the complexity of software engineering

### 5.2 EnCompass Framework (2025, NeurIPS)

- **Research Team**: MIT CSAIL + Asari AI
- **URL**: https://www.csail.mit.edu/news/helping-ai-agents-search-get-best-results-out-large-language-models
- **Relevant Areas**: Development & Engineering
- **Key Findings**:
  - Framework that enables LLMs to automatically backtrack when they make mistakes during program execution
  - Creates program runtime clones for parallel attempts
  - **Up to 80% reduction in coding effort for search implementation**

### 5.3 Generative AI-Based Robot Design (2025)

- **URL**: https://news.mit.edu/2025/using-generative-ai-help-robots-jump-higher-land-safely-0627
- **Relevant Areas**: Design & Prototyping
- **Key Findings**:
  - Generates optimal robot part geometries on a personal computer, then simulates and 3D prints them
  - Produced robots that **jump 41% higher** than manually designed counterparts

### 5.4 GenSQL — Generative AI for Databases

- **URL**: https://www.csail.mit.edu/news/mit-researchers-introduce-generative-ai-databases
- **Relevant Areas**: Development & Engineering, Discovery & User Research
- **Key Findings**:
  - Automatic integration of tabular datasets with generative probabilistic models
  - Generation and analysis of synthetic data that mimics real data

### 5.5 MIT CSAIL HCI Group

- **URL**: https://hci.csail.mit.edu/
- **Relevant Areas**: Design & Prototyping, Discovery & User Research
- **Key Findings**:
  - UX design principles research: learnability, efficiency, safety
  - Research on non-traditional interactions such as eye tracking and voice/vision tools
  - Research on prototyping and user testing automation

### 5.6 Armando Solar-Lezama — Program Synthesis

- **Position**: MIT EECS Professor, CSAIL Associate Director & COO
- **Awards**: Inaugural Distinguished College of Computing Professor; Robin Milner Young Researcher Award
- **Relevant Areas**: Development & Engineering
- **Key Findings**:
  - World-leading pioneer in Program Synthesis
  - Research on AI automatically generating programs from specifications
  - Provides the theoretical foundation for code-generating AI
  - Co-author of the 2025 "AI for SE" paper — systematically mapping the limitations of current AI coding tools

### 5.7 Martin Rinard — Program Repair & Approximate Computing

- **Position**: MIT EECS Professor, CSAIL PI
- **Awards**: ACM SIGSOFT Outstanding Research Award (2025)
- **Relevant Areas**: Development & Engineering
- **Key Findings**:
  - Pioneer in Program Repair and approximate computing
  - "Emergent Representations of Program Semantics in Language Models Trained on Programs" (ICML 2024) — demonstrates that LLMs develop internal world models when trained on programs
  - "Software Engineering Research in a World with Generative AI" (ICSE 2024 keynote)
  - Foundational technology for AI-based code quality and debugging

### 5.8 Daniel Jackson — Software Design & Concept Design

- **Position**: MIT CSAIL Associate Director, Professor of Computer Science, ACM Fellow
- **Relevant Areas**: Development & Engineering, Design & Prototyping
- **Key Findings**:
  - Software design methodology, creator of the Alloy modeling language
  - Author: *The Essence of Software: Why Concepts Matter for Great Design*
  - **2024 key argument**: LLMs can write individual functions but cannot design entire applications; apps must be structured into independent modules ("concepts") to enable LLM-based development
  - Highlights the need to combine AI code generation with robust design methodologies

### 5.9 Daniela Rus — Robotics & Manufacturing Automation

- **Position**: MIT CSAIL Director, MIT Panasonic Professor of EECS
- **Awards**: IEEE Edison Medal (2025)
- **Relevant Areas**: Design & Prototyping, Development & Engineering
- **Key Findings**:
  - Research in robotics, mobile computing, and manufacturing automation
  - **Robot Compiler**: A system enabling non-experts to design and build custom robots — an example of democratized AI-enabled manufacturing/prototyping
  - Author: *The Heart and the Chip: Our Bright Future with Robots* (2024), *The Mind's Mirror: Risk and Reward in the Age of AI* (2024)

### 5.10 Srini Devadas — AI Privacy & Security

- **Position**: MIT EECS Professor, CSAIL PI
- **Relevant Areas**: Cross-cutting (Responsible AI)
- **Key Findings**:
  - Research on computer security, cryptography, and Physical Unclonable Functions (PUFs)
  - **PAC Privacy (2025)**: A method for automatically estimating the minimum noise needed for privacy while maintaining accuracy during AI model training (IEEE S&P 2025)
  - Foundational technology for privacy protection in AI products that handle user data

### 5.7 Tim Kraska — A2rchi (AI for Research & Education)

- **Position**: MIT EECS Associate Professor, CSAIL
- **Relevant Areas**: Development & Engineering
- **Key Findings**:
  - MGAIC project: A2rchi — AI-powered course/research support system
  - Research on learned index-based database systems
  - AI-based data infrastructure optimization

### 5.8 Samuel Madden — Agentic AI for Data Curation

- **Position**: MIT EECS Professor, CSAIL
- **Relevant Areas**: Development & Engineering, Management & Decision Making
- **Key Findings**:
  - MGAIC project: "Agentic AI-Based Enterprise Data Curation"
  - Utilizing AI agents in large-scale data systems

---

## 6. MIT Media Lab

> URL: https://www.media.mit.edu/

### 6.1 Advancing Humans with AI (AHA) Initiative

- **Led by**: Pattie Maes and multiple faculty members
- **URL**: https://aha.media.mit.edu/
- **Relevant Areas**: Cross-cutting (Human-AI Collaboration)
- **Key Findings**:
  - Interdisciplinary initiative: understanding the human experience in the age of pervasive AI
  - Designing human-AI interaction for human flourishing
  - Research on augmenting decision-making, learning, health, and well-being

### 6.2 Pattie Maes — Fluid Interfaces Group

- **Position**: MIT Media Lab Germeshausen Professor
- **URL**: https://www.media.mit.edu/people/pattie/overview/
- **Relevant Areas**: Design & Prototyping, Cross-cutting (Human-AI Collaboration)
- **Key Projects**:
  - **Memoro**: Wearable AI memory assistant (bone-conduction headset, conversation memory support)
  - **AttentivU**: Wearable brain-computer interface (attention monitoring)
  - **WatchThis**: Vision-language model-based point-and-ask wearable interface

### 6.3 Cynthia Breazeal — Personal Robots Group

- **Position**: MIT Media Lab Professor, MIT Dean for Digital Learning
- **Awards**: TIME100 AI (Thinkers category, 2025), AAAS Fellow (2024)
- **Relevant Areas**: Design & Prototyping, Cross-cutting (Human-AI Collaboration)
- **Key Findings**:
  - Research on long-term relationship formation between social robots and humans
  - Emotional interaction design in AI products — education, health, and aging domains
  - Jibo (social robot) spin-off — a pioneering example of AI product commercialization
  - *Science Robotics* cover article (March 2025) — comprehensive social robotics research

### 6.4 Rosalind Picard — Affective Computing Group

- **Position**: MIT Media Lab Professor, MIT EECS; Founder of Affectiva & Empatica
- **Relevant Areas**: Discovery & User Research, Design & Prototyping
- **Key Findings**:
  - Pioneer of the Affective Computing field
  - Inferring user emotional states via wearable sensors
  - NeurIPS 2024 invited talk: saving lives with skin electrical signal + AI wearables
  - Foundational technology for emotion recognition in AI products — Affectiva and Empatica spin-offs

### 6.5 Human-AI Interaction Research Theme (2025)

- **URL**: https://www.media.mit.edu/projects/theme-human-ai/overview/
- **Relevant Areas**: Cross-cutting (Human-AI Collaboration), Design & Prototyping
- **Key Projects**:
  - **Be the Beat**: AI-powered boombox that suggests music based on dancer movements (PoseNet + LLM)
  - **Memorscope**: A collective memory device combining face-to-face interaction with AI
  - **Narratron**: Interactive projector for co-creating children's stories through shadow puppetry (LLM)

### 6.6 Hiroshi Ishii — Tangible Media Group

- **Position**: MIT Media Lab Jerome B. Wiesner Professor
- **Relevant Areas**: Design & Prototyping
- **Key Findings**:
  - "Tangible Bits" (1997) to "Radical Atoms" (2012): interfaces enabling physical manipulation of digital information
  - **DESAI25 Workshop**: Exploring the future of AI-based design
  - **Pocket Ink** (NeurIPS 2025): Hyper-personalized tangible card game for the AI era
  - **PixBric** (UIST 2025): Novel physical-digital interface
  - Charting future directions for product interaction design

---

## 7. MIT Engineering and Design Labs

### 7.1 DeCoDE Lab — Faez Ahmed

- **Position**: MIT Mechanical Engineering Assistant Professor
- **URL**: https://decode.mit.edu/
- **Relevant Areas**: Design & Prototyping, Development & Engineering
- **Key Findings**:
  - Using AI as a "copilot" for engineering design
  - Bicycle frame design experiment: similarity-focused AI vs. engineering performance-targeted AI
  - Models aligned with engineering performance objectives produced more innovative and higher-performing results
  - MGAIC seed grant: "Manufacturability-Aware Generative AI for Next-Gen Topology Optimization"

### 7.2 MIT Design Intelligence Lab

- **URL**: https://designintelligence.mit.edu/
- **Relevant Areas**: Design & Prototyping
- **Key Projects**:
  - **Large Language Objects (LLO)**: Physical interfaces for LLMs — interaction beyond chatbots/GUIs
  - **Geni**: Generative AI-based children's audio storytelling platform
  - **Light Craft**: Experiments combining physical design with AI

### 7.3 MIT Collective Intelligence Design Lab

- **Affiliation**: MIT Center for Collective Intelligence
- **URL**: https://cci.mit.edu/research/cidesignlab/
- **Relevant Areas**: Management & Decision Making
- **Key Findings**:
  - Developing innovative methods for group problem-solving leveraging interdisciplinary MIT research
  - Research on AI-based collective decision-making tools

### 7.4 MIT Senseable City Lab — Carlo Ratti

- **Position**: MIT DUSP Professor
- **URL**: https://senseable.mit.edu/
- **Relevant Areas**: Discovery & User Research, Growth & Lifecycle
- **Key Findings**:
  - Urban data analysis using computer vision, laser scanning, and remote sensing
  - Copenhagen Wheel: transforming bicycles into hybrid vehicles + mobile sensing units (startup founded)
  - Urban data-driven approach to product innovation

### 7.5 MIT Auto-ID Lab

- **URL**: https://autoid.mit.edu/
- **Relevant Areas**: Growth & Lifecycle (PLM, digital twins)
- **Key Findings**:
  - First use of the term "Internet of Things" in 1999
  - Birthplace of RFID and IoT technology
  - Research on product lifecycle tracking and digital twin-based technologies
  - Combining supply chain visibility with AI

### 7.6 MIT LIDS (Laboratory for Information and Decision Systems)

- **URL**: https://lids.mit.edu/
- **Four research focus areas**: ML & Data Science, Autonomy & Agency, Computing & Sustainability, Computing & Society
- **Relevant Areas**: Management & Decision Making, Growth & Lifecycle
- **Key Researchers**:
  - **Devavrat Shah** (Andrew and Erna Viterbi Professor): First to provide theoretical performance guarantees for recommendation systems (in sparse sampling settings); causal inference; misinformation-aware news feed algorithms. ACM SIGMETRICS Achievement Award (2025)
  - **Munther Dahleh** (MIT IDSS Director): Data marketplace economics — algorithmic data buying/selling mechanisms and social welfare optimization. Built the Data Lab (cloud-based data storage/processing)
- **Key Findings**:
  - Sequential decision-making, reinforcement learning, network inference, optimization under uncertainty
  - Theoretical foundations for AI-based product decision-making frameworks
  - Data marketplace economics — valuation of training data for AI products

### 7.7 MIT CISR (Center for Information Systems Research)

- **URL**: https://cisr.mit.edu/
- **Key Researchers**: Peter Weill, Stephanie Woerner, Ina Sebastian, Evgeny Kaganer
- **Relevant Areas**: Management & Decision Making, Growth & Lifecycle
- **Key Findings**:
  - **4-Stage Enterprise AI Maturity Model** (2024, based on 721 companies + 9 case studies):
    - Stage 1: Exploring
    - Stage 2: Piloting & Building Capabilities
    - Stage 3: Scaling AI Ways of Working
    - Stage 4: AI-Native
  - **Key finding**: Stage 1-2 companies perform below industry average; Stage 3-4 companies perform above average. The Stage 2 to 3 transition is the most critical
  - **Four transformation challenges**: Strategy, Systems, Synchronization, Stewardship
  - 2025 updates: "Grow Enterprise AI Maturity for Bottom-Line Impact" (Aug 2025), "AI-Era Business Models" (Oct 2025)

### 7.8 MIT MIMO (Machine Intelligence for Manufacturing and Operations)

- **URL**: https://mimo.mit.edu/
- **Relevant Areas**: Development & Engineering, Growth & Lifecycle
- **Key Findings**:
  - 2025 symposium theme: transforming manufacturing/operations with generative AI — expanding domestic production, addressing labor shortages
  - 2024 symposium: AI for sustainability/resilience, 20+ research posters. Emphasis on "human"-centered theme
  - Core insight: successful AI deployment must account for the unique perspectives of humans on the manufacturing floor

### 7.9 MIT Leaders for Global Operations (LGO)

- **Relevant Areas**: Development & Engineering, Growth & Lifecycle
- **Key Findings**:
  - Added Northrop Grumman and Stanley Black & Decker as partners in 2024 (total of 24 industry partners)
  - Focus on AI/ML, additive manufacturing, and supply chain optimization
  - Developing data-driven leaders in product design, manufacturing, and service delivery

---

## 8. MIT Economics — AI & Labor

### 8.1 Daron Acemoglu — Macroeconomics of AI (2024 Nobel Prize in Economics)

- **Position**: MIT Institute Professor; 2024 Nobel Prize in Economics laureate
- **Relevant Areas**: Cross-cutting, Management & Decision Making
- **Key Paper**: "The Simple Macroeconomics of AI" (*Economic Policy*, 2024)
  - Predicts AI will increase GDP by 1.1-1.6% over a decade (approximately 0.05% annual productivity growth) — significantly lower than industry expectations
  - Current AI is overly focused on automation (replacing humans) vs. "machine usefulness" (augmenting human expertise)
  - **Core argument**: AI capabilities should augment users rather than replace them
- **MIT Initiative**: Shaping the Future of Work Initiative (co-led with David Autor and Simon Johnson)

### 8.2 David Autor — AI & Future of Work

- **Position**: MIT EECS Professor; 2024 AI2050 Senior Fellow (Schmidt Sciences)
- **Relevant Areas**: Cross-cutting, Growth & Lifecycle
- **Key Findings**:
  - Research on AI's dual effect of simultaneously devaluing and amplifying expertise
  - Argues that AI can restore the core of "middle-skill, middle-class" labor markets — when designed for collaboration
  - Defines the automation vs. augmentation trade-off — a framework product designers must consider

### 8.3 Sendhil Mullainathan — AI Fairness & Algorithmic Bias

- **Position**: MIT Peter de Florez Professor (Economics + EECS); returned to MIT from U Chicago in 2024
- **Relevant Areas**: Cross-cutting (Responsible AI)
- **Key Findings**:
  - **"The Bike Shop @ MIT"**: A new research center for human-centered AI — "scalable bicycles for the mind"
  - Using AI to uncover hidden biases in human decision-making (e.g., detecting appearance-based bias in bail decisions)
  - "Economics in the Age of Algorithms" (*AEA Papers and Proceedings*, 2025)
  - Co-teaches MIT 14.163 (Algorithms and Behavioral Science)
  - Key researcher in algorithmic fairness and bias detection within products

---

## 9. MIT SDM (System Design and Management)

> MIT SDM is a graduate program jointly operated by the School of Engineering and MIT Sloan, focusing on systems thinking, product architecture, and engineering leadership.
> URL: https://sdm.mit.edu/

### 9.1 SDM Faculty AI-Related Research

#### Bryan Moser (SDM Academic Director & Sr. Lecturer)

- **Research Areas**: Agent-based sociotechnical systems modeling, complex systems teamwork, model-based team performance analysis
- **Career**: Applied AI to CAD, multi-objective optimization, and robot control at Nissan Motor Company's Basic Science Research Laboratory
- **Key Contributions**:
  - CAS 2025 Best Student Paper co-author: "Designing Generative Multi-Agent Systems for Resilience" (with Nguyen-Luc Dao)
  - Research on how architectural decisions (group size, prompting, topology) in generative multi-agent systems affect resilience against malicious agents

#### Bruce Cameron (System Architecture Lab Director)

- **Research Areas**: Technology strategy, system architecture, product platforms, digital platforms
- **Key Contributions**:
  - Co-author of *System Architecture: Strategy and Product Development for Complex Systems* (with Crawley and Selva)
  - Research on customer loyalty retention in digital platforms (Uber, Apple App Store)

#### Edward Crawley (Professor of Aeronautics & Astronautics)

- **Research Areas**: Complex system design and architecture
- **Key Contributions**: Co-author of the "System Architecture" textbook — the foundation of the SDM system architecture curriculum

#### Olivier de Weck (Apollo Program Professor)

- **Affiliation**: Aeronautics & Astronautics + IDSS (Institute for Data, Systems, and Society)
- **Research Areas**: Design and evolution of complex technological systems, multidisciplinary design optimization, technology roadmapping
- **Track Record**: 400+ publications, 12 best paper awards

#### Daniel Frey (Professor of Mechanical Engineering)

- **Research Areas**: Robust Design, experimental design methodology
- **Key Contributions**:
  - AI-based design: Using ML models for bicycle design — grouping similar designs, predicting key components, generating new designs based on performance parameters
  - MIT D-Lab Research Director

#### Daniel Selva (System Architecture textbook co-author)

- **Key Contributions**: First to apply ML tools to system architecture analysis; received a best paper award related to NASA research

### 9.2 SDM Master's Theses (AI + Product)

| Thesis Title | Author | Year | Relevant Area |
|----------|------|------|-----------|
| "A Strategic Perspective on the Commercialization of AI" | - | - | Management & Decision Making |
| "AI Product Economics" | Nicholas Borge | 2022 | Management & Decision Making |
| "AI/ML Capabilities and APIs at Amazon, Google, Microsoft" | - | - | Development & Engineering |
| "AI-Based Approach to Automate Document Processing" | Brandon Chen | 2021 | Development & Engineering |
| "Designing Generative Multi-Agent Systems for Resilience" | Nguyen-Luc Dao | 2022 | Development & Engineering, Cross-cutting |
| "ML for Detection of Cyberattacks on Industrial Control Systems" | Geet Kalra | 2023 | Cross-cutting (Responsible AI) |
| "Digital Transformation and Its Influence on Platform Business" | - | - | Growth & Lifecycle |
| "Improving Complex Sale Cycles Using ML and Predictive Analytics" | - | - | Growth & Lifecycle |
| "Data-Driven Decision Making: An Adoption Framework" | - | - | Management & Decision Making |

### 9.3 SDM Events & Conferences

#### Complex Adaptive Systems (CAS) 2025

- **Hosted by**: MIT SDM, March 5-7, 2025, MIT Campus
- **Theme**: "Transdisciplinary Systems & Solutions for Adaptability"
- **Featured Presentation**: BAE's Mark Vriesenga — Zero Trust AI System Architecture
- **Best Student Paper**: Luc Dao, "Designing Generative Multi-Agent Systems for Resilience"
- **URL**: https://sdm.mit.edu/sdm-hosts-cas-2025/

#### SDM Webinar: "Building an AI Product"

- **Presenter**: Bryan Pirtle (SDM Fellow, Nova.ai CTO / Y Combinator W16)
- **Content**: Sharing experience building an AI product for high-tech sales organizations
- **URL**: https://sdm.mit.edu/building-an-ai-product-to-improve-high-tech-sales/

### 9.4 SERC (Social and Ethical Responsibilities of Computing) Program

- SDM Fellows Dave Kmiec, Emily Lauber, and Luc Dao were selected as 2024-2025 SERC Scholars
- Luc Dao's SERC research: A framework for data ownership, privacy, and ethical/legal implications in AI
- **Relevant Areas**: Cross-cutting (Responsible AI)

### 9.5 Connections Between SDM Systems Thinking and AI for Product

1. **System Architecture for AI Products**: The Crawley-Cameron-Selva "System Architecture" framework (decomposition, interfaces, emergence) directly applies to AI-based product system design
2. **Agent-Based Modeling**: Moser's agent-based simulation of sociotechnical systems is applicable to modeling AI agent-human team interactions in product development
3. **Technology Strategy & Platforms**: Cameron's digital platform research explains how AI capabilities are embedded in product platform architectures
4. **Robust Design + AI**: Frey's ML-integrated robust design provides methods for ensuring the robustness of AI-assisted design processes
5. **Ethical AI Systems**: Data ownership/governance framework research through the SERC program

---

## 10. MIT Generative AI Impact Consortium (MGAIC)

- **Founded**: 2025
- **URL**: https://genai.mit.edu/
- **Founding Members**: Analog Devices, Coca-Cola, OpenAI, Tata Group, SK Telecom, TWG Global
- **Consulting Advisor**: McKinsey
- **Scale**: 250 faculty members, 180 proposals, **55 seed grants selected**

### Key Selected Projects (ai4-product related)

| Project | Researcher | Affiliation | Relevant Area |
|----------|--------|------|-----------|
| Manufacturability-Aware GenAI for Topology Optimization | Faez Ahmed | MechE | Design & Prototyping |
| A2rchi: AI Course/Research Support | Tim Kraska | CSAIL/EECS | Development & Engineering |
| Agentic AI-Based Enterprise Data Curation | Samuel Madden | EECS | Development & Engineering |
| GenAI for Software Supply Chain Risk Management | Retsef Levi | MIT Sloan | Growth & Lifecycle |
| Pareto Machines: Positive-Sum Solution AI Agents | Sinan Aral | MIT Sloan | Management & Decision Making |
| HypSynth: Multi-Agent Hypothesis Refinement | Satrajit Ghosh | MIT/HMS | Discovery & User Research |
| LLM-Based Transportation/Logistics Decision Models | Alexandre Jacquillat | MIT Sloan | Management & Decision Making |

---

## 11. MIT Educational Programs

### AI + Product Related Courses

| Program | Duration | Key Content | URL |
|----------|------|-----------|-----|
| **MIT xPRO: Designing and Building AI Products and Services** | 10 weeks | AI technology fundamentals, UX design, information design, capstone project | https://executive-ed.xpro.mit.edu/designing-building-ai-products-services |
| **MIT xPRO: AI Strategy and Product Innovation** | 6 months | Integrated course on AI product design + AI strategy leadership | https://executive-ed.xpro.mit.edu/ai-strategy-and-product-innovation |
| **MIT Professional: Product Innovation in the Age of AI** | 4 days | Lead User process, AI innovation opportunities, ML scaling | https://professional.mit.edu/course-catalog/product-innovation-age-ai |
| **MIT Professional: Ethics and Risks of AI** | Short-term | Bias, hallucination, privacy, governance strategies | https://professional.mit.edu/course-catalog/ethics-and-risks-ai-building-responsible-ai-machine-learning-and-gpts |
| **MIT Professional Certificate in Product Management** | 9 months | Design thinking, product architecture, includes Agentic AI module | https://professionalprograms.mit.edu/professional-certificate-program-product-management/ |
| **MIT Sloan Executive: AI for Business Strategy** | Short-term | Strategic business implications of AI | https://executive.mit.edu/course/artificial-intelligence/a056g00000URaa3AAD.html |
| **MIT Professional: AI for Computational Design and Manufacturing** | Short-term | AI for computational design and manufacturing | https://professional.mit.edu/course-catalog/ai-computational-design-and-manufacturing |

---

## 12. Mapping MIT Research to ai4-product Domains

| ai4-product Domain | Key MIT Research/Resources | Key Researchers |
|---|---|---|
| **Discovery & User Research** | MIT Sloan AI persona experiment, SMR "GenAI Meets Product Development", GenSQL, Senseable City Lab, Hauser LLM-VOC (2026) | John Hauser, Duncan Simester, Carlo Ratti |
| **Design & Prototyping** | DeCoDE Lab (AI copilot, CAD-Coder), Design Intelligence Lab, CSAIL robot design (Rus), Media Lab (Tangible Media, Fluid Interfaces) | Faez Ahmed, Daniela Rus, Pattie Maes, Hiroshi Ishii, Cynthia Breazeal, Daniel Jackson |
| **Development & Engineering** | CSAIL "AI for SE" (ICML 2025), EnCompass (NeurIPS 2025), Program Synthesis, "Generative AI at Work", MIMO, LGO | Armando Solar-Lezama, Martin Rinard, Tim Kraska, Samuel Madden, Danielle Li |
| **Management & Decision Making** | IDE GenAI Divide, CCI Superminds, Geek Way, LIDS decision-making, CISR 4-stage AI maturity model, Agentic Enterprise | Thomas Malone, Andrew McAfee, Sinan Aral, Kate Kellogg, Devavrat Shah |
| **Growth & Lifecycle** | GenAI Divide (95% failure), CODE@MIT, CISR AI maturity, Tucker AI privacy, LIDS data marketplace, Auto-ID Lab | Sinan Aral, Dean Eckles, Catherine Tucker, Retsef Levi, Munther Dahleh |
| **Cross-cutting** | SMR-BCG Responsible AI, Media Lab AHA, Pairit, MGAIC, Economics of AI (automation vs. augmentation), Mullainathan bias, PAC Privacy | Daron Acemoglu, David Autor, Sendhil Mullainathan, Pattie Maes, Rosalind Picard, Srini Devadas |

---

## 13. Sources

### MIT Sloan Management Review
- Marion, T.J., Srour, M., Piller, F. (2024). "When Generative AI Meets Product Development." MIT SMR. https://sloanreview.mit.edu/article/when-generative-ai-meets-product-development/
- MIT SMR & BCG (2022-2025). Responsible AI Series. https://sloanreview.mit.edu/big-ideas/responsible-ai/
- MIT SMR & BCG (2025). "The Emerging Agentic Enterprise." https://sloanreview.mit.edu/projects/the-emerging-agentic-enterprise-how-leaders-must-navigate-a-new-age-of-ai/
- MIT SMR (2025). "Five Trends in AI and Data Science for 2025." https://www.prnewswire.com/news-releases/five-trends-in-ai-and-data-science-for-2025-from-mit-sloan-management-review-302345115.html

### MIT IDE & Sloan Faculty
- Brynjolfsson, E., Li, D., Raymond, L. (2025). "Generative AI at Work." QJE 140(2). https://academic.oup.com/qje/article/140/2/889/7990658
- MIT IDE (2025). "4 New Studies about Agentic AI." https://mitsloan.mit.edu/ideas-made-to-matter/4-new-studies-about-agentic-ai-mit-initiative-digital-economy
- MIT IDE (2025). "The 2025 AI Agent Index." https://aiagentindex.mit.edu/
- MIT NANDA (2025). "The GenAI Divide: State of AI in Business 2025."
- MIT (2025). "Designing Human-AI Collaboration: A Sufficient-Statistic Approach." https://economics.mit.edu/sites/default/files/2025-06/AI_Design__Sufficient_Statistics.pdf

### MIT CSAIL
- MIT News (2025). "Challenges and Paths Towards AI for Software Engineering." https://news.mit.edu/2025/can-ai-really-code-study-maps-roadblocks-to-autonomous-software-engineering-0716
- MIT CSAIL (2025). "EnCompass Framework." https://www.csail.mit.edu/news/helping-ai-agents-search-get-best-results-out-large-language-models
- MIT News (2025). "Using Generative AI to Help Robots." https://news.mit.edu/2025/using-generative-ai-help-robots-jump-higher-land-safely-0627
- MIT CSAIL. "GenSQL." https://www.csail.mit.edu/news/mit-researchers-introduce-generative-ai-databases
- Rinard, M. (2024). "Emergent Representations of Program Semantics in Language Models." ICML 2024.
- Rinard, M. (2024). "Software Engineering Research in a World with Generative AI." ICSE 2024 Keynote.
- Devadas, S. (2025). "PAC Privacy." IEEE S&P 2025. https://news.mit.edu/2025/new-method-efficiently-safeguards-sensitive-ai-training-data-0411

### MIT Media Lab
- MIT Media Lab. "Advancing Humans with AI (AHA)." https://aha.media.mit.edu/
- MIT Media Lab. "Human-AI Interaction Theme." https://www.media.mit.edu/projects/theme-human-ai/overview/

### MIT Economics
- Acemoglu, D. (2024). "The Simple Macroeconomics of AI." Economic Policy.
- Autor, D. (2024). AI & Future of Work. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4722981
- Mullainathan, S. (2025). "Economics in the Age of Algorithms." AEA Papers and Proceedings.

### MIT SDM
- MIT SDM. https://sdm.mit.edu/
- Dao, N.L. & Moser, B. (2025). "Designing Generative Multi-Agent Systems for Resilience." CAS 2025 Best Student Paper. https://sdm.mit.edu/research-practice/dao-best-paper-cas-2025/
- MIT SDM (2025). CAS 2025 Conference. https://sdm.mit.edu/sdm-hosts-cas-2025/
- Borge, N. (2022). "AI Product Economics." SDM Thesis. https://dspace.mit.edu/bitstream/handle/1721.1/144985/borge-njborge-sm-sdm-2022-thesis.pdf
- SDM Webinar: "Building an AI Product." https://sdm.mit.edu/building-an-ai-product-to-improve-high-tech-sales/

### MIT Labs & Centers
- DeCoDE Lab. https://decode.mit.edu/
- MIT Design Intelligence Lab. https://designintelligence.mit.edu/
- MIT CCI. https://cci.mit.edu/
- MIT Senseable City Lab. https://senseable.mit.edu/
- MIT CISR. https://cisr.mit.edu/
- MIT LIDS. https://lids.mit.edu/
- MIT MIMO. https://mimo.mit.edu/
- MIT Auto-ID Lab. https://autoid.mit.edu/

### MIT MGAIC
- MIT Generative AI Impact Consortium. https://genai.mit.edu/
- MIT News (2025). "MGAIC Kickoff." https://news.mit.edu/2025/researchers-present-bold-ideas-ai-mit-generative-ai-impact-consortium-event-0620

### MIT Education
- MIT xPRO. https://executive-ed.xpro.mit.edu/designing-building-ai-products-services
- MIT Professional Education. https://professional.mit.edu/
- MIT Sloan Executive Education. https://executive.mit.edu/

### Upcoming
- BIG.AI@MIT 2026. https://ide.mit.edu/events/2026-the-business-implications-of-generative-ai-mit-big-aimit/
