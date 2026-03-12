# Asian Companies: AI-for-Product Initiatives (2023-2026)

A comprehensive survey of AI-for-Product use cases from leading Korean, Japanese, and Chinese companies. This document complements the existing [tech-companies.md](tech-companies.md) survey, which primarily covers US and European firms.

---

## South Korea

---

### 1. Samsung

#### Galaxy AI — On-Device Consumer AI

Samsung launched Galaxy AI with the Galaxy S24 series in January 2024, making it the first major Android OEM to ship a comprehensive suite of on-device AI features.

| Feature | Description |
|---------|-------------|
| Circle to Search | Visual search by circling objects on screen (co-developed with Google) |
| Live Translate | Real-time phone call translation across 20+ languages |
| Chat Assist | Tone adjustment, translation, and grammar correction in messaging apps |
| Note Assist | Summarization, formatting, and translation of handwritten/typed notes |
| Photo Assist | Generative Edit (object removal/repositioning), AI-powered image enhancement |
| Transcript Assist | Recording transcription with AI summaries |
| Browsing Assist | Web page summarization and translation |

**Adoption metrics:**
- 200M+ Galaxy AI-enabled devices shipped by end of 2024
- 400M+ Galaxy AI devices targeted by end of 2025
- 70%+ of Galaxy S25 users actively engaging with AI features
- Google Gemini usage tripled on the Galaxy S series between S24 and S25

**MWC 2026 announcements:** Samsung demonstrated cross-device AI experiences connecting Galaxy smartphones, tablets, wearables, and SmartThings-enabled home appliances as a unified AI ecosystem.

Sources:
- https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026
- https://betanews.com/2025/07/14/samsung-to-bring-galaxy-ai-to-400-million-devices-globally-by-end-of-the-year/
- https://www.samsungmobilepress.com/feature-stories/samsung-continues-to-expand-galaxy-ai-as-consumers-show-increasing-reliance-on-mobile-ai

#### Samsung Gauss — Foundation Models

Samsung Gauss is Samsung's in-house family of generative AI models, unveiled at the Samsung AI Forum in November 2023 and named after mathematician Carl Friedrich Gauss.

| Model | Parameters | Use Case |
|-------|-----------|----------|
| Gauss 2 Compact | Small | On-device inference in resource-constrained environments |
| Gauss 2 Balanced | Medium | General-purpose enterprise and consumer tasks |
| Gauss 2 Supreme | Large | High-performance specialized applications |
| Gauss 2.3 / Gauss 2.3 Think | Latest generation | Advanced reasoning for enterprise use |
| Gauss O Flash | Optimized | Fast inference for real-time applications |

**Enterprise adoption:** The coding assistant "code.i," powered by Gauss 2, is used extensively within Samsung's DX Division and by international research teams, with up to 60% of developers engaging regularly. Gauss also powers an internal no-code Agent Builder platform.

**Future direction:** Gauss models are being positioned for both internal enterprise use and integration into consumer products (smartphones, laptops, autonomous driving).

Sources:
- https://www.sammobile.com/news/samsung-develops-own-agentic-ai-tools-improves-gauss-ai-models/
- https://www.androidcentral.com/apps-software/samsung-next-gen-model-gauss-2-ai-model-reveal

#### R&D Investment

| Year | R&D Spending | Facility Investment | YoY Change (R&D) |
|------|-------------|--------------------|--------------------|
| 2024 | $24.1B (35T KRW) | $32.3B (47.7T KRW) | +23.5% |
| 2025 | $25.6B (37.7T KRW) | $35.7B (52.7T KRW) | +7.8% |

The majority of R&D investment is directed toward advanced memory chips (HBM, DDR5) critical for AI infrastructure, positioning Samsung as both a consumer AI company and an AI infrastructure supplier.

Sources:
- https://www.koreatimes.co.kr/business/companies/20260310/samsung-electronics-spends-w377-tril-in-rd-in-2025
- https://www.koreaherald.com/article/10439155

#### Differentiation from Western Counterparts
Unlike Apple's closed-ecosystem approach to on-device AI, Samsung adopts a **multi-model strategy**: Galaxy AI integrates Google Gemini, Samsung Gauss, and other models depending on the task. Samsung also uniquely leverages its semiconductor division (HBM, Exynos) to vertically integrate AI hardware and software, a capability no Western smartphone OEM possesses.

---

### 2. LG

#### EXAONE — Enterprise AI Foundation Model

LG AI Research has built EXAONE into one of the most competitive non-US/non-China AI model families, with a clear B2B focus that differentiates it from consumer-oriented Western models.

| Model | Release | Parameters | Notable Achievement |
|-------|---------|-----------|---------------------|
| EXAONE 3.0 | Aug 2024 | 7.8B | Open-sourced, strong Korean language performance |
| EXAONE 3.5 | Dec 2024 | 2.4B / 7.8B / 32B | Three-tier architecture (ultra-lightweight to high-performance) |
| EXAONE Deep | Mar 2025 | 2.4B-32B | 7.8B model outperforms OpenAI o1-mini on reasoning tasks |
| EXAONE 4.0 | Jul 2025 | Hybrid | Combines general language processing with advanced reasoning; multimodal (VL variant) |
| K-EXAONE | Jan 2026 | 236B (23B active, MoE) | Only non-US/non-China model in global top 10 open-weight rankings |

**Enterprise products:**
- **ChatExaone**: Internal AI agent for LG employee corporate workflows
- **EXAONE Data Foundry**: Accelerated data generation platform
- **EXAONE On-Premise**: Full-stack agent deployed in isolated, secure environments using entirely proprietary Korean technology

Sources:
- https://spectrum.ieee.org/exaone-lg-ai-research
- https://www.prnewswire.com/news-releases/lg-rolls-outs-k-exaone-south-korea-joins-the-global-frontier-ai-race-with-world-class-ai-model-302658264.html
- https://www.koreaherald.com/article/10652980

#### ThinQ AI — Smart Home Ecosystem

LG ThinQ AI represents LG's approach to "Affectionate Intelligence" — appliances that learn from user behavior rather than operating on fixed commands.

**Key milestones:**
- **IFA 2024:** Unveiled ThinQ ON AI Home Hub as centerpiece of connected smart home
- **Sep 2025:** Launched integrated ThinQ AI platform combining ThinQ UP (customization) and ThinQ Care (proactive maintenance)
- **2025-2026:** European rollout of ThinQ AI across appliances

**AI-powered product features:**
- Washing machines that use AI to weigh contents and auto-select optimal programs
- Dryers that detect fabric type to prevent damage
- Refrigerators with Night View (brightness adjustment) and Smart Fill (precision water dispensing)
- OLED TVs with AI Picture Pro (scene-by-scene optimization) and AI Sound Pro

Sources:
- https://lgcorp.com/media/release/28061
- https://www.lgnewsroom.com/2025/09/lg-brings-seamless-evolving-smart-home-experiences-to-europe-with-thinq-ai/

#### Differentiation from Western Counterparts
LG uniquely combines a **frontier AI research lab** (EXAONE, ranked globally) with a **massive appliance manufacturing base**. While Google and Amazon compete in smart home via software platforms, LG embeds AI directly into hardware appliances — and its EXAONE On-Premise solution addresses enterprise data sovereignty concerns that Western cloud-first models often cannot.

---

### 3. Hyundai / Kia

#### AI Robotics Strategy (CES 2026)

Hyundai Motor Group unveiled its AI Robotics Strategy at CES 2026 under the theme "Partnering Human Progress," featuring Boston Dynamics' new Atlas humanoid robot in its first public demonstration.

**Key initiatives:**

| Initiative | Description | Timeline |
|-----------|-------------|----------|
| Boston Dynamics Atlas | Humanoid robot for manufacturing; initial focus on repetitive tasks (component sequencing) | Factory deployment from 2028 |
| Robotics Facility | New U.S. facility with 30,000-unit annual capacity | Part of $26B U.S. investment (2025-2029) |
| Boston Dynamics + Google DeepMind | Strategic partnership for next-gen humanoid AI | Announced 2025 |
| Hyundai Mobis Actuators | High-performance actuators and standardized components for robotics platform | Ongoing |

#### Software-Defined Vehicle (SDV) and Factory (SDF)

At E-FOREST TECH DAY 2024, Hyundai and Kia presented their vision for Software-Defined Factories integrating AI-driven manufacturing. The SDV strategy centers on continuous OTA updates and AI-powered in-vehicle experiences.

#### Differentiation from Western Counterparts
Hyundai's acquisition of Boston Dynamics ($1.1B, 2021) gives it a **robotics capability no other automaker possesses**. While Tesla develops Optimus in-house, Hyundai leverages Boston Dynamics' decades of research plus new partnerships with Google DeepMind, creating a uniquely diversified AI robotics ecosystem spanning vehicles, factories, and humanoid robots.

Sources:
- https://www.hyundai.com/worldwide/en/newsroom/detail/0000001093
- https://www.hyundainews.com/releases/4664
- https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-and-kia-present-future-vision-for-software-defined-factories-at-e-forest-tech-day-2024-0000000849

---

### 4. Naver

#### HyperCLOVA X — Korea's Leading LLM

HyperCLOVA X is Naver's hyperscale Korean-language AI model, trained on 6,500x more Korean data than GPT-3. It serves as the backbone of Naver's entire service ecosystem.

**Product integrations (2024-2025):**

| Product | AI Application | Timeline |
|---------|---------------|----------|
| Naver Search | AI Briefing: summarized AI-generated answers with source verification | H1 2025 |
| Naver PlusStore | Personalized product recommendation understanding hidden search intent | Mar 2025 |
| NAVER Shopping Live | AI Cue Sheet Helper auto-drafts product scripts for live commerce merchants | 2024 |
| CLOVA X | Conversational AI chatbot for productivity (document summarization, translation, email drafting) | 2023- |
| CLOVA Studio | LLMOps platform for managing LLM lifecycle (design, develop, deploy, operate) | 2024- |

**Language leadership:** HyperCLOVA X is recognized as the best-performing AI model for East Asian languages (Korean, Chinese, Japanese) in 2025, with strong results in Vietnamese, Tagalog, Hindi, and Hokkien.

**Research output:** 450+ published papers, 47,000+ citations as of 2025.

Sources:
- https://www.interad.com/en/insights/naver-ai-the-ultimate-guide-to-artifitial-intelligence
- https://www.kedglobal.com/artificial-intelligence/newsView/ked202411110012
- https://koreatechtoday.com/naver-pushes-inference-ai-frontier-with-hyperclova-x-think/

#### Differentiation from Western Counterparts
Naver's "On-Service AI" strategy is distinct: rather than building a standalone AI product (like ChatGPT or Gemini), Naver embeds HyperCLOVA X **invisibly into every existing service** — search, shopping, payments, maps — creating an AI-native super-app experience. Its Korean-language specialization also gives it a structural advantage over English-centric Western models in the Korean market.

---

### 5. Kakao

#### Kanana — AI-Native Messenger and Model Family

Kakao's AI strategy centers on Kanana, a conversational AI agent designed as a standalone messenger app separate from KakaoTalk (Korea's dominant messaging platform with 48M+ MAU).

**Model lineup:**

| Model | Purpose |
|-------|---------|
| Kanana Flag | Large-scale flagship model |
| Kanana Essence | Mid-sized general-purpose model |
| Kanana Nano | Lightweight on-device model |
| Kanana-o | Multimodal model (text, voice, images) |
| Kanana-2 (open-source) | Agentic AI optimized; Base, Instruct, and Thinking variants |

**Timeline:**
- Oct 2024: Kanana announced at if(kakaoAI)2024
- H1 2025: Kanana beta launch as standalone AI messenger
- May 2025: Kanana-o multimodal model introduced
- Dec 2025: Kanana-2 open-sourced (Base, Instruct, Thinking)
- Oct 2025: ChatGPT integrated into KakaoTalk

**Korean voice AI focus:** Kakao's charts place Kanana-o ahead of mid-tier models across Korean speech recognition, speech synthesis, emotional speech detection, and spoken instruction following.

Sources:
- https://www.kedglobal.com/artificial-intelligence/newsView/ked202410220015
- https://www.koreatimes.co.kr/business/tech-science/20251219/kakao-open-sources-kanana-2-model-optimized-for-agentic-ai
- https://www.kakaocorp.com/page/detail/11299?lang=ENG

#### Differentiation from Western Counterparts
Kakao takes a **narrower, depth-first approach** — optimizing for Korean language and voice rather than competing globally. Its dual strategy of building proprietary Kanana models while also integrating ChatGPT into KakaoTalk gives users access to both specialized Korean AI and frontier Western models within the same ecosystem.

---

### 6. Coupang

#### AI-Driven Commerce and Logistics

Coupang has invested over $3B from 2022-2024 in AI innovations and advanced technologies across the APEC region.

**AI applications across the value chain:**

| Domain | AI Application | Impact |
|--------|---------------|--------|
| Demand Forecasting | Predicts customer demand to forward-deploy inventory | Enables same-day/next-day delivery for 99.6% of orders |
| Fulfillment Optimization | AI generates unique optimized path for each order within seconds | Coordinates employees, AGVs, and sorting robots in real-time |
| Search & Discovery | Vision and language transformer models for product embeddings | More effective ad retrieval, similarity search, and recommendations |
| Pricing | ML-driven dynamic pricing | Real-time competitive pricing optimization |
| Logistics Infrastructure | AI-powered robotics (driverless forklifts, sorting robots, AGVs) | 97% autonomous operations at advanced facilities |

**Infrastructure expansion:** New AI-powered logistics facility in Jecheon, scheduled for completion June 2026 with operations beginning 2027.

Sources:
- https://medium.com/coupang-engineering/accelerating-coupangs-ai-journey-with-llms-2817d55004d3
- https://www.aboutcoupang.com/English/news/news-details/2025/the-future-of-commerce-the-incredible-innovations-powering-the-coupang-experience/
- https://www.koreaherald.com/article/10445164

#### Differentiation from Western Counterparts
Unlike Amazon, which separates AWS (cloud AI) from retail operations, Coupang's AI is **purpose-built and vertically integrated** exclusively for commerce and logistics. Coupang also operates its own last-mile delivery fleet (Coupang Flex), giving it end-to-end AI optimization from demand prediction through doorstep delivery — a level of integration even Amazon does not fully achieve in most markets.

---

### 7. SK Telecom

#### A. (A-dot) and Aster — Personal AI Agents

SK Telecom has transformed from a traditional telecom into an "AI Native" company, with cumulative AI investment planned at 5 trillion KRW (~$3.4B) through 2030, targeting 5 trillion KRW in AI revenue by 2030.

**AI products:**

| Product | Market | Features |
|---------|--------|----------|
| A. (A-dot) | Korea | LLM-powered personal assistant with Daily management (calendar, tasks, routines, sleep); multi-LLM support (Perplexity, ChatGPT, Claude, A.X); specialized agents for music, media, stocks |
| Aster (A*) | North America | "Life Management" AI agent; beta launched March 2025; handles planning through execution |
| NUGU | Korea (legacy) | Voice AI assistant (earlier generation) |
| A. Phone | Korea (2026) | Full AI agent for call summarization, schedule management, and follow-up task execution |

**AI infrastructure:**
- $200M strategic investment in Penguin Solutions (AI data center solutions, July 2024)
- AI Infrastructure Superhighway: AI data centers (AIDC) + GPU-as-a-Service (GPUaaS) + Edge AI
- Partnership with Supermicro and Schneider Electric for modular AI data centers

Sources:
- https://news.sktelecom.com/en/1551
- https://www.sktelecom.com/en/press/press_detail.do?idx=1627
- https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-driving-koreas-leap-in-ai-innovation-302700470.html

#### Differentiation from Western Counterparts
SKT's A. is notable for its **multi-LLM architecture** — users can choose and compare responses from seven different AI models (including competitors like ChatGPT and Claude) within a single app. This "model marketplace" approach differs fundamentally from Western companies like Apple (Siri locked to Apple Intelligence) or Google (Assistant locked to Gemini).

---

## Japan

---

### 8. Sony

#### AI in Gaming — Gran Turismo Sophy and PlayStation AI

Sony AI won the 2024 AI Breakthrough Award for its innovative use of AI in gaming.

**Key AI products:**

| Product | Description | Timeline |
|---------|-------------|----------|
| Gran Turismo Sophy | Deep reinforcement learning agent that masters race car control, racing tactics, and racing etiquette; deployed as in-game AI opponent | 2022 research, 2024 PlayStation deployment |
| PlayStation Spectral Super Resolution (PSSR) | ML-based upscaling adding extraordinary detail; shipped with PS5 Pro | Nov 2024 (PS5 Pro launch) |
| PS5 Pro Ray Tracing | AI-accelerated ray tracing for real-time graphics | Nov 2024 |

#### AI in Imaging and Sensors

Sony's semiconductor division is integrating AI directly into image sensors:

- **LYTIA 901**: ~200-effective-megapixel mobile image sensor with built-in AI image processing circuit (announced 2025)
- **IMX828**: Industry-first automotive CMOS image sensor with built-in MIPI A-PHY interface and industry-leading HDR
- **IMX500**: Intelligent Vision Sensor with on-chip AI processing, open-source Edge AI stack

#### AI Research — Six Flagship Projects

Sony AI operates across six domains: AI for Creators, Gaming and Interactive Agents, Ethics, Scientific Discovery, Imaging and Sensing, and Robotics and Sensing.

**Notable research output:** Multiple papers at NeurIPS 2025 (music generation, text-to-image, diffusion, audio compression) and ICCV 2025 (generative modeling, computer vision, raw sensor data optimization).

**Strategic IP protection:** In May 2024, Sony Music Group sent warning letters to over 700 AI companies prohibiting unauthorized use of its music catalog for AI training.

Sources:
- https://ai.sony/articles/Sony-AI-Wins-2024-AI-Breakthrough-Award-for-Innovative-Use-of-AI-in-Gaming/
- https://www.klover.ai/sony-ai-strategy-analysis-of-dominating-ai-conglomerate-with-integrated-ecosystem/
- https://www.sony-semicon.com/en/info/2025/2025112701.html

#### Differentiation from Western Counterparts
Sony's AI strategy is uniquely **vertically integrated across content and hardware**: it owns both the creative IP (PlayStation Studios, Sony Music, Sony Pictures) and the sensing hardware (image sensors powering ~50% of global smartphones). This "Creation Shift" strategy positions Sony to control both AI inputs (sensor data, creative content) and AI outputs (gaming experiences, imaging quality) — a combination no Western company replicates.

---

### 9. Toyota

#### Woven City — Real-World AI Test Bed

Toyota Woven City officially launched on September 25, 2025, as a 175-acre "test course for mobility" built on the former Higashi-Fuji manufacturing plant site.

| Phase | Status | Residents | Timeline |
|-------|--------|-----------|----------|
| Phase 1 Construction | Completed | ~100 initial, expanding to 360 | Oct 2024 (completed), Sep 2025 (residents move in) |
| Phase 2+ | Planned | ~2,000 total | TBD |

**Technology platforms tested at Woven City:**
- **Arene OS**: Vehicle operating system managing 200+ vehicle functions; first deployed in next-gen RAV4 (FY2025)
- **Digital Twin Platform**: Replicates real-world environments for simulation
- **Vision AI**: Video data analysis with AI to understand movement behavior of people and objects
- Autonomous vehicles, robotics, smart energy systems

#### Arene OS — Vehicle Operating System

Arene OS is Toyota's software-defined vehicle platform, developed by Woven by Toyota:
- Manages 200+ vehicle functions
- Continuous OTA updates for ADAS and safety
- Next-gen voice recognition ("feels like talking to a human")
- First deployment: next-generation RAV4 (FY2025)

#### Autonomous Driving Investment

Toyota and NTT have jointly committed ~$3.3B (2024-2030) to develop AI-assisted autonomous driving software and telecommunications infrastructure. The resulting mobility AI platform targets a 2028 launch.

Sources:
- https://global.toyota/en/newsroom/corporate/43347785.html
- https://woven.toyota/en/our-latest/20250521/
- https://woven.toyota/en/our-latest/20250107-02/

#### Differentiation from Western Counterparts
Toyota's approach is fundamentally different from Tesla's "ship and iterate" model. By building an entire **living city as a controlled AI testbed**, Toyota can test autonomous vehicles, robotics, and urban AI systems with real residents in a safe environment before mass deployment. The $3.3B NTT partnership also reflects Japan's emphasis on **telecommunications-AI convergence** — integrating 5G/6G infrastructure with autonomous driving in ways Western automakers have not pursued.

---

### 10. Rakuten

#### AI-Powered Ecosystem

Rakuten's AI strategy leverages its unique position as Japan's largest e-commerce, fintech, and mobile ecosystem (1.9 billion global members, 44 trillion yen annual GTV).

**AI models:**
- **Rakuten AI 2.0**: First Japanese LLM using Mixture of Experts (MoE) architecture (Dec 2024)
- **Rakuten AI 2.0 mini**: Small language model optimized for Japanese (Dec 2024)

**AI product integrations:**

| Service | AI Feature | Timeline |
|---------|-----------|----------|
| Rakuten Ichiba | RMS AI Assistant (Beta) — AI-powered store management for merchants | 2024 |
| Rakuten Ichiba | AI product descriptions, images, and sizing recommendations | Autumn 2025 rollout |
| 16 Rakuten services | Semantic search and AI recommendations | 2024 (deployed) |
| Rakuten AI app | Free AI assistant integrated across shopping, fintech, travel, education, wellness | Jul 2025 full-scale launch |

**"Brain Twin" concept:** Rakuten envisions an agentic AI ecosystem where a personal "Brain Twin" AI agent understands user preferences across all Rakuten services and acts proactively on the user's behalf.

Sources:
- https://rakuten.today/blog/rakuten-ai-in-2024-a-year-of-empowerment.html
- https://global.rakuten.com/corp/news/press/2025/0730_01.html
- https://www.pymnts.com/news/artificial-intelligence/2025/rakuten-taps-agentic-ai-to-enhance-omotenashi-ultimate-service/

#### Differentiation from Western Counterparts
Rakuten's AI is deeply embedded in **Japan's "Omotenashi" (hospitality) culture** — optimizing for service quality rather than pure efficiency. Its "Rakuten Ecosystem" provides a cross-service AI integration (shopping + banking + mobile + travel) that has no direct Western equivalent. Amazon, for comparison, keeps its commerce and financial services (Amazon Pay, lending) largely separate from an AI perspective.

---

### 11. SoftBank

#### AI Infrastructure and Investment Strategy

SoftBank has transformed from a telecommunications/investment company into an AI infrastructure conglomerate.

**Major AI investments and acquisitions:**

| Initiative | Scale | Timeline |
|-----------|-------|----------|
| Project Stargate | $500B AI infrastructure JV with OpenAI, Oracle, MGX | Jan 2025 announcement |
| Project Izanagi | $100B AI chip venture ($30B own funds + $70B external) | Prototypes summer 2025, shipments 2026 |
| ABB Robotics acquisition | $5.4B (division generated $2.3B revenue in 2024) | Oct 2025, closing 2026 |
| OpenAI Japan JV | $3B joint venture to localize enterprise AI for Japan | Nov 2025 |
| Ampere Computing | Acquired; combined with Arm + Graphcore into "Silicon Trinity" | Nov 2025 |
| Nvidia stake exit | Sold $5.8B stake to fund $30B OpenAI follow-on investment | Late 2025 |

**"Silicon Trinity" — Vertical AI Chip Integration:**
SoftBank now controls:
1. **Arm Holdings**: CPU architecture (97%+ of smartphones)
2. **Ampere Computing**: Server-grade CPUs
3. **Graphcore**: Intelligence Processing Units (IPUs)

This creates a vertically integrated AI semiconductor ecosystem that challenges Nvidia's dominance.

Sources:
- https://markets.financialcontent.com/stocks/article/marketminute-2026-2-26-softbank-shares-surge-as-masayoshi-son-unleashes-the-izanagi-ai-strategy
- https://www.cnbc.com/2025/10/08/softbank-to-buy-abb-robotics-unit-for-5point4-billion-in-ai-push.html
- https://techcrunch.com/2025/11/05/softbank-openai-launch-new-joint-venture-in-japan-as-ai-deals-grow-ever-more-circular/

#### Differentiation from Western Counterparts
SoftBank is pursuing the most **capital-intensive AI strategy of any non-US company**: over $600B in combined commitments across Stargate, Izanagi, and acquisitions. Unlike US tech giants that build AI primarily through software, SoftBank is attempting to control the entire AI value chain from chip architecture (Arm) through GPU alternatives (Graphcore) to data centers (Stargate) and deployment (robotics via ABB + Boston Dynamics partnership).

---

## China

---

### 12. BYD

#### AI in EV Manufacturing and Vehicle Intelligence

BYD has scaled from 500,000 vehicles in 2017 to over 4 million by 2024, powered by pervasive AI integration.

**Manufacturing AI:**

| Application | Impact |
|------------|--------|
| AI quality control (battery production) | 40% reduction in battery defects |
| AI battery lifecycle optimization | 20% improvement in average battery lifespan |
| Factory automation (Xi'an facility) | ~97% autonomous operations |
| Digital twins of battery manufacturing | Simulate and optimize without physical testing |
| AI-powered robotics, AGVs, intelligent warehousing | End-to-end automated fulfillment |

**Vehicle Intelligence — XUANJI Architecture (Dream Day 2024):**
- **XUANJI AI Large Model**: First multimodal vehicular AI applied across all vehicle domains
- **"Intelligent Driving for All" (Feb 2025)**: All new BYD vehicles equipped with ADAS as standard at no additional cost
- **"God's Eye" system**: Three-tiered ADAS deployed across all price points (from $9,555 to luxury)

**Vertical integration advantage:** BYD manufactures ~75% of vehicle components internally (Blade Batteries, electric motors, power electronics). Internal analysis shows a BYD car comparable to the Tesla Model 3 costs 15% less to produce than at Tesla's Shanghai Gigafactory.

Sources:
- https://evmagazine.com/news/how-chinas-byd-is-using-ai-to-scale-global-ev-manufacturing-2025
- https://en.byd.com/news/byd-showcased-the-intelligence-advancement-at-dream-day-2024/
- https://digitaldefynd.com/IQ/byd-using-ai-case-study/

#### Differentiation from Western Counterparts
BYD's AI strategy is **manufacturing-first, not software-first**. While Tesla leads in autonomous driving software (FSD), BYD leads in AI-optimized manufacturing at scale. BYD's "Intelligent Driving for All" initiative — making ADAS standard across all price points — democratizes AI-powered driving in a way no Western automaker has attempted, leveraging its cost advantage from vertical integration.

---

### 13. Alibaba

#### Qwen (Tongyi Qianwen) — AI Foundation and Commerce Platform

Alibaba unified all AI models and applications under the Qwen brand, building one of China's most commercially integrated AI ecosystems.

**Model evolution:**

| Model | Release | Key Capability |
|-------|---------|---------------|
| Qwen (original) | Apr 2023 | Chinese-language LLM |
| Qwen 2 | Jun 2024 | Multilingual, competitive with Llama 3 |
| Qwen 2.5 | Sep 2024 | 72B model, improved coding and math |
| Qwen App | Nov 2025 (public beta) | Consumer-facing AI agent app |
| Qwen + Taobao integration | Jan 2026 | AI shopping agent within Qwen app |

**Adoption metrics:**
- 100M+ monthly active users since public beta launch (Nov 2025)
- 200M one-sentence orders placed during Lunar New Year via Qwen app
- AI-related cloud product revenue: triple-digit growth for 6 consecutive quarters

**Commerce AI integrations:**
- **Taobao/Tmall**: AI-powered shopping via voice and text within Qwen app
- **Accio (Nov 2024)**: AI application for B2B sourcing (market insights, product recommendations)
- **Alipay, Fliggy, Amap**: Integrated AI agent for payments, travel, navigation
- **Taobao Instant Commerce**: Automated food delivery with AI-applied discounts

**Investment:** RMB 380B ($53B) pledged over three years (2025-2028) for AI and cloud infrastructure — exceeding total AI/cloud spending over the previous decade. AI-related cloud revenue growing at triple-digit rates.

Sources:
- https://www.alibabacloud.com/blog/alibaba-to-invest-rmb380-billion-in-ai-and-cloud-infrastructure-over-next-three-years_602007
- https://www.yicaiglobal.com/news/qwen-transforms-ai-that-responds-into-action-ai-across-alibabas-app-suite
- https://www.asiabusinessoutlook.com/news/alibaba-unifies-ai-under-qwen-major-growth-and-consumer-push-nwid-11441.html

#### Differentiation from Western Counterparts
Alibaba has achieved something no Western AI company has: **seamless AI-to-commerce conversion at scale**. The Qwen app processes natural-language shopping requests end-to-end — from product discovery through payment (Alipay) to delivery tracking — across Alibaba's entire ecosystem. Google and OpenAI have no comparable commerce integration. The 200M one-sentence orders during Lunar New Year demonstrate consumer AI driving real transactions, not just engagement.

---

### 14. Huawei

#### Ascend AI Chips — China's Nvidia Alternative

Under US sanctions that cut off access to advanced TSMC nodes and Nvidia GPUs, Huawei has built an indigenous AI chip ecosystem.

| Chip | Performance | Production | Timeline |
|------|------------|-----------|----------|
| Ascend 910B | ~600 TFLOPS FP16 | Mass production | 2024 |
| Ascend 910C | ~800 TFLOPS FP16, 3.2 TB/s memory bandwidth (~80% of Nvidia H100) | ~300K units | 2025 |
| Ascend 910C (doubled output) | Same | ~600K units | 2026 |
| Ascend 950 | In-house HBM, SuperPod architecture | Planned | 2026 |
| Ascend 960 | Next-gen | Planned | Q4 2027 |
| Ascend 970 | Next-gen | Planned | Q4 2028 |

**Key customers:** Alibaba, Tencent, DeepSeek, Baidu, and other Chinese cloud/AI companies.

**Manufacturing:** Partnering with SMIC using enhanced 7nm process (vs. Nvidia's 4nm at TSMC).

#### HarmonyOS — AI-Native Operating System

| Version | Release | AI Features |
|---------|---------|-------------|
| HarmonyOS 5.0 | Jun 2024 | Pangu 5.5 model integration (718B NLP parameters, 15B vision parameters) |
| HarmonyOS 6 (Beta) | 2025 | AI Agent Framework; Celia voice assistant powered by Pangu + DeepSeek |

**Pangu model specialization:** Unlike general-purpose Western models, Pangu 5.5 includes specialized variants for medicine, finance, governance, manufacturing, and automotive.

**AI infrastructure:** CloudMatrix 384 supernode (384 Ascend chips with high-speed interconnects) rivals Nvidia's GB200 NVL72 in compute performance.

Sources:
- https://technode.com/2025/05/18/huawei-to-ship-700000-ascend-ai-chips-in-2025-despite-yield-challenges/
- https://www.trendforce.com/news/2025/09/18/news-huawei-unveils-ascend-950-with-in-house-hbm-in-2026-touts-superpod-to-rival-nvidia/
- https://www.crnasia.com/news/2025/software/huawei-rolls-out-harmonyos-6-beta-with-ai-agents-as-us-sanct

#### Differentiation from Western Counterparts
Huawei is the world's only company building an **end-to-end AI stack under export sanctions**: from custom AI chips (Ascend) to operating system (HarmonyOS) to foundation models (Pangu) to cloud infrastructure (CloudMatrix). While this constrains raw performance (~80% of Nvidia H100), it creates complete technological sovereignty — a strategic posture no Western company needs or pursues.

---

### 15. Xiaomi

#### "Human x Car x Home" AI Ecosystem

Xiaomi's AI strategy connects smartphones, electric vehicles, and smart home devices through HyperOS, creating a unified intelligent ecosystem.

**Electric Vehicle — SU7 Series:**

| Metric | Value |
|--------|-------|
| SU7 launch | Mar 2024 |
| 2024 production run | Sold out within 24 hours |
| 2024 deliveries | 135,000+ units |
| 100K milestone | Reached in 230 days (by Nov 2024) |
| 2025 target | 300,000 deliveries |
| SU7 Ultra launch | Feb 2025, priced at 529,900 yuan ($73,000) |
| YU7 SUV | Mid-2025 launch |
| Market position (2025) | Best-selling large sedan in China's EV market; outsold Tesla Model 3 |

**HyperOS and HyperAI (2025):**
- AI Writing Tools, real-time translation, speech recognition
- AI Art in Mi Canvas, AI Live Wallpapers, AI Cinematic Lock Screens
- Blends Xiaomi proprietary AI with Google Gemini
- "Xiao Ai" voice assistant controls vehicle, home devices, and smartphone seamlessly
- Cross-device automation: phone triggers home actions, car displays home security cameras
- Developed by 3,000+ engineers analyzing 25,000+ scenarios

**EV profitability milestone:** Xiaomi's electric car business became profitable in November 2025.

Sources:
- https://en.wikipedia.org/wiki/Xiaomi_SU7
- https://www.thefastmode.com/devices-and-wearables/39963-xiaomi-displays-enhanced-human-x-car-x-home-smart-ecosystem-at-mwc-2025
- https://www.electrive.com/2025/11/21/xiaomis-electric-car-business-becomes-profitable/

#### Differentiation from Western Counterparts
Xiaomi is the only company globally that has successfully launched a **smartphone-to-EV-to-smart-home AI ecosystem** in under two years. Apple's car project was cancelled. Google has no hardware ecosystem comparable. Xiaomi's ability to cross-pollinate AI features across phones, vehicles, and home devices (all running HyperOS) creates a uniquely integrated user experience at aggressive price points.

---

### 16. ByteDance (Non-TikTok/Doubao AI Products)

#### Volcano Engine — Enterprise AI Infrastructure

Volcano Engine is ByteDance's enterprise technology arm, distinct from its consumer products.

| Metric | Value |
|--------|-------|
| 2024 revenue | RMB 12B+ |
| 2025 revenue target | RMB 25B+ |
| Doubao daily token usage (May 2025) | 16.4T tokens (137x increase since May 2024) |
| China public cloud LLM market share | 46.4% (more than Baidu + Alibaba combined) |

**Key enterprise AI products:**

| Product | Function |
|---------|----------|
| Coze | No-code AI agent development platform; open-sourced (Coze Studio + Coze Loop, 10K+ GitHub stars in 3 days) |
| Coze Space (Apr 2025) | Multi-agent workspace for complex task execution |
| Coze 2.0 | Shift from "instant Q&A" to "workplace AI partner" |
| Doubao Image Editing 3.0 (SeedEdit) | NL-driven visual manipulation for advertising, e-commerce |
| Doubao Simultaneous Interpretation 2.0 | 2-3 second latency (down from 8-10s); zero-shot voice cloning |
| Doubao 3D Generation | Text-to-3D, image-to-3D; high-fidelity 3D assets in under 1 minute |
| Doubao Video Generation | Commercial video generation (launched Jan 2025) |

**Hardware initiatives:**
- "Doubao Phone" (AI smartphone, manufactured by ZTE, late 2025/early 2026)
- Ola Friend smart earbuds (launched 2024)
- AI glasses (in development)

**Pricing strategy:** Aggressively undercutting competitors — RMB 0.15/million input tokens, RMB 1.5/million output tokens, with enterprise discounts up to 47%.

Sources:
- https://en.tmtpost.com/post/7645516
- https://kr-asia.com/bytedance-launches-coze-its-new-ai-agent-platform-in-beta
- https://finance.yahoo.com/news/bytedance-ai-model-usage-grows-093000910.html

#### Differentiation from Western Counterparts
ByteDance's Coze platform represents a different philosophy from Western AI agent frameworks (LangChain, OpenAI Assistants API): **visual, no-code, and optimized for rapid deployment** by non-technical users. The aggressive pricing strategy (70% cheaper than competitors) and the bundling of enterprise AI with a dominant consumer platform (Douyin) gives ByteDance a distribution advantage that has no Western parallel — even OpenAI lacks a consumer app with 600M+ DAU to funnel enterprise leads.

---

## Regional Comparison: AI-for-Product Strategies

### Strategic Orientation

| Dimension | South Korea | Japan | China |
|-----------|-------------|-------|-------|
| **Primary AI focus** | Devices and semiconductors | Manufacturing and infrastructure | Platform ecosystems and scale |
| **Model strategy** | Build proprietary + integrate Western models | Partner with US leaders (OpenAI, Google) | Build sovereign alternatives |
| **Hardware integration** | Deep (Samsung chips + devices, LG appliances) | Moderate (Sony sensors, Toyota vehicles) | Very deep (Huawei full-stack, BYD 75% vertical, Xiaomi ecosystem) |
| **Open-source approach** | Selective (EXAONE, Kanana-2) | Limited | Aggressive (Qwen, Coze, DeepSeek) |
| **Government role** | AI Basic Act (2026 implementation) | Light-touch voluntary governance | Strict registration/labeling + strong industrial policy |

### Investment Scale (2024-2026)

| Company | AI/Tech Investment | Focus |
|---------|-------------------|-------|
| Samsung | $25.6B R&D (2025) + $35.7B capex | AI chips (HBM), on-device AI |
| Alibaba | $53B over 3 years (2025-2028) | Cloud and AI infrastructure |
| SoftBank | $500B+ (Stargate) + $100B (Izanagi) | AI infrastructure, chips, robotics |
| Huawei | Doubling chip output annually | Indigenous AI chip ecosystem |
| Hyundai | $26B in US (2025-2029) | AI robotics, SDV, manufacturing |
| Toyota + NTT | $3.3B (2024-2030) | Autonomous driving, mobility AI |
| Coupang | $3B+ (2022-2024) | Commerce AI, logistics |

### Key Differentiators by Region

**South Korea — "AI Through Hardware"**
Korean companies excel at embedding AI into physical products. Samsung leads in on-device AI (Galaxy AI on 400M devices), LG leads in AI appliances and enterprise models (EXAONE in global top 10), and SK Telecom pioneered multi-LLM personal agents. Korean firms tend to adopt a **dual-model strategy** — building proprietary Korean-language models while integrating Western frontier models — reflecting both technological ambition and pragmatic market focus.

**Japan — "AI Through Precision and Patience"**
Japanese companies approach AI with longer time horizons and deeper infrastructure investments. Toyota built an entire city (Woven City) to test AI before mass deployment. SoftBank is spending $600B+ to control the AI chip value chain. Sony embeds AI into sensors at the silicon level. Japan's personal generative AI adoption rate (26.7%) lags China (81.2%) significantly, but Japanese companies are positioning for **hardware-level AI leadership** that may prove more durable than software-layer advantages.

**China — "AI at Scale, AI for Sovereignty"**
Chinese companies operate at a scale and speed that Asian peers cannot match: Alibaba's Qwen app reached 100M MAU in months; ByteDance processes 16.4T tokens daily; BYD produced 4M+ AI-optimized vehicles in a single year. Under US sanctions, Huawei has built an entirely indigenous AI stack, and the broader Chinese ecosystem has rapidly adopted open-source as a strategic tool. China's AI industry surpassed 700B yuan ($96B) in 2024, with 100+ AI products launched in a single year. The emphasis is on **practical deployment over research novelty** — as evidenced by BYD making ADAS standard across all vehicles, or Alibaba turning a chatbot into a transactional commerce agent.

### Contrasts with Western AI Approach

| Dimension | Asian Companies | Western Companies |
|-----------|----------------|-------------------|
| **Language priority** | Native language optimization first (Korean, Japanese, Chinese) | English-first, multilingual later |
| **AI distribution** | Embedded in existing super-apps and ecosystems | Standalone AI products (ChatGPT, Copilot) |
| **Hardware-software integration** | Extremely tight (chips, sensors, appliances, vehicles) | Primarily software-centric (except Apple) |
| **Manufacturing AI** | Central focus (BYD, Hyundai, Toyota) | Secondary to consumer/enterprise AI |
| **Pricing strategy** | Often free or aggressively subsidized (Rakuten AI free, ByteDance 70% cheaper) | Premium pricing (OpenAI $20/mo, Copilot $30/mo) |
| **Regulatory environment** | Range from strict (China) to permissive (Japan) | Generally moderate (EU AI Act, US executive orders) |
| **AI adoption rates** | China: 81.2%, Korea: high, Japan: 26.7% | US/EU: 40-60% estimated |

---

*Last updated: 2026-03-12*
