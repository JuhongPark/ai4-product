# Speculative Methods for AI-for-Product Research: Beyond Scenarios to Research Implications

> Design fiction, science fiction prototyping, and anticipatory ethics are not just storytelling — they are research methods with specific, empirically grounded functions for AI product development.

---

## 1. Design Fiction as a Research Method (Not Just Storytelling)

### Academic Status

Design fiction is now recognized as a legitimate HCI research method within the "fifth wave" of design research and "fourth wave" of HCI (Futures & Foresight Science, 2024). It creates **"materialised thought experiments that prototype near-future worlds"** — diegetic artifacts that make abstract AI possibilities concrete and debatable.

Key sources:
- "How HCI Integrates Speculative Thinking to Envision Futures" — Journal of Futures Studies, 2024. https://jfsdigital.org/wp-content/uploads/2024/05/Zhu-Chao-Fu-1.pdf
- "Reviewing the expansion in design futuring research" — Futures (Elsevier), 2025. https://www.sciencedirect.com/science/article/abs/pii/S0016328725000771
- "A systematic literature review of the speculative design process" — Design Science (Cambridge), 2024. https://www.cambridge.org/core/journals/design-science/article/systematic-literature-review-of-the-speculative-design-process-and-a-proposed-framework-for-speculative-design/DEEE583F28D2A32AA5965BF85608C17A

### What It Does That Other Methods Can't

| Traditional Method | Limitation | Design Fiction Fills |
|-------------------|-----------|---------------------|
| User interviews | Users can only articulate current needs | Fiction materializes needs that don't yet exist |
| A/B testing | Tests what is, not what could be | Fiction tests implications of what doesn't yet exist |
| Literature review | Synthesizes past findings | Fiction extrapolates forward from current evidence |
| Prototyping | Constrained by current technical feasibility | Fiction ignores feasibility to explore desirability |

### Specific Research Function for ai4-product

**Problem**: Our research identifies 15 gaps (e.g., "end-to-end AI integration," "multi-agent PM orchestration"). These gaps exist partly because the futures they describe don't exist yet — we can't study what hasn't been built.

**Solution**: Design fiction creates **diegetic prototypes** of these futures that can be studied, critiqued, and used to elicit requirements from practitioners *before* building the real system.

**Example**: Wadinambiarachchi et al. (2025) created "Idy" — a fictional AI agent for design teams. Through this fiction, they discovered 5 distinct agent roles designers actually want (Work Coordinator, Resource Steward, Guardian, Reframer, Creative Catalyst) and a critical finding: designers insist on retaining creative authority. This is a **research result**, not a story.

Source: https://arxiv.org/html/2509.20731v1

---

## 2. Science Fiction Prototyping: Empirical Track Record in Industry

### Method

Brian David Johnson (Intel, 2009-2019) formalized **Science Fiction Prototyping (SFP)**: writing short SF stories based on science fact to explore future products and their human implications.

5-step process: World-building → Characters → Science inflection point → Ramifications → Resolution

Source: https://link.springer.com/book/10.1007/978-3-031-01796-4

### Empirical Evidence

**Wu (2013)** — "Imagination Workshops: An empirical exploration of SFP for technology-based business innovation"
- Published in *Futures* (Elsevier), Vol. 50
- Two case studies applying SFP to UK small businesses
- Proposed iterative evolutionary model (not linear) with feedback loops
- Key finding: SFP is most effective for **long-term product innovation and futuristic business strategies**, less so for immediate operational improvements
- Source: https://www.sciencedirect.com/science/article/abs/pii/S0016328713000505

### Corporate Adoption as Evidence of Value

| Company | Application | Outcome |
|---------|------------|---------|
| **Intel** | SFP embedded in chip specifications for smart TV team | Informed product direction for 2B+ processors over a decade |
| **Visa** | SF prototypes for future of payments | Technology kiosks and immersive touchscreen environments |
| **Shell** | Scenario planning since 1970s | Anticipated OPEC oil embargo; continues for energy transition |
| **SciFutures** (agency) | 300+ SF writers for corporate clients | Clients include Visa, Ford, Colgate, Intel, US military |

### Research Implication for ai4-product

SFP provides a **structured method to explore the "what to build" question** that our AADM framework identifies as the domain where AI is least useful (low Data, low Reversibility, low Subjectivity → "AI Absent" zone).

**Paradox resolved**: The decisions that AI can't help with (strategic vision, "what to build next") are precisely where speculative methods are most valuable. SFP fills the gap that AI leaves.

---

## 3. Anticipatory Ethics: From "What Could Happen" to "What Should We Prevent"

### Framework

**Seth Lazar (ANU/Oxford, 2024)** — "Anticipatory AI Ethics"
- Published by Knight First Amendment Institute, Columbia University
- Source: https://knightcolumbia.org/content/anticipatory-ai-ethics

### Core Argument

> "If new technologies are likely to cause significant societal harm before we can develop adequate post hoc measures, then we need to design those technologies to mitigate those risks."

### The "Technological Horizon" Method

Rather than unconstrained speculation, Lazar proposes analyzing **"possible worlds reasonably understood given current knowledge"**:

1. Identify discrete hazards and opportunities (not comprehensive forecasts)
2. Hold institutional context relatively constant, vary AI capabilities
3. Focus on **affordances** — system properties that make outcomes more/less likely without determining them

### Three Levels of Analysis

| Level | Method | Epistemic Risk | Example |
|-------|--------|---------------|---------|
| **Near-term** | Internal critique | Low | "If you claim 'safe' AI without democratic controls, what happens to democracy?" |
| **Medium-term** | Institutional analysis | Medium | "How would AI agents undermine assumptions about human equality in hiring?" |
| **Long-term** | First-order ethics | High | "What moral frameworks apply in a world with superhuman AI?" |

### Research Implication for ai4-product

Our research gaps include **"AI Governance for Product Teams" (High severity)** and **"AI Cognitive Atrophy" (Medium)**. Anticipatory ethics provides a **rigorous method to study these before they fully materialize**:

- Apply Lazar's "technological horizon" to each product lifecycle phase
- For each phase, identify affordances of current AI tools that could produce harm
- Design governance interventions at each identified affordance point

This transforms our research gap from "governance is needed" (descriptive) to **"here's what governance should prevent and how"** (prescriptive).

---

## 4. Responsible Computational Foresight: AI Studying Its Own Future

### Framework

**Perez-Ortiz (2025)** — "From Prediction to Foresight: The Role of AI in Designing Responsible Futures"
- Source: https://arxiv.org/abs/2511.21570

Introduces "responsible computational foresight" — using AI itself to model and evaluate future AI scenarios while maintaining human-centered decision-making.

### Key Principles

1. AI as **supportive tool** in foresight, complementing (not substituting) human judgment
2. Systems-level analysis of interdependencies across social, environmental, economic, political dimensions
3. Ethical safeguards ensuring long-term accountability

### OECD/WEF Data (2025)

- **2/3 of foresight practitioners** already use AI in strategic foresight work
- Most-cited AI benefit: **time efficiency** (39%) — handling scanning/synthesis, freeing humans for interpretation
- Source: https://www.weforum.org/stories/2025/12/ai-strategic-foresight-future-thinking/

### Research Implication for ai4-product

This directly maps to our Selective Complementarity Framework:
- **Foresight scanning and synthesis** = AI-led (data-rich, pattern-based)
- **Interpretation and narrative building** = Human-led (judgment under uncertainty)
- The foresight domain itself follows the same human-AI allocation pattern we proposed for product development

---

## 5. Synthesis: How Speculative Methods Fill Specific Research Gaps

| ai4-product Research Gap | Speculative Method | How It Helps |
|-------------------------|-------------------|-------------|
| **#1 End-to-End AI Integration** | Design fiction | Create diegetic prototypes of full-lifecycle AI systems to study before building |
| **#4 Human-AI Complementarity** | Speculative enactments | Let practitioners experience human-AI workflows that don't exist yet and evaluate them |
| **#13 AI Governance for Product Teams** | Anticipatory ethics | Identify affordances in current AI tools that create governance risks; design interventions |
| **#15 AI Cognitive Atrophy** | Science fiction prototyping | Explore long-term cognitive consequences through narrative; identify early warning signs |
| **"What to build next?"** | SFP + scenario planning | Fill the AADM "AI Absent" zone with structured human imagination methods |
| **Emerging research directions** | Responsible computational foresight | Use AI to model scenarios of its own impact on product teams |

### The Meta-Insight

Our three frameworks (Selective Complementarity, Successful 5% Patterns, AADM) all identify a zone where **AI has no useful role**: strategic vision, ethical judgment, "what to build." Speculative methods are the research toolkit for that zone. They're not an alternative to empirical research — they're the **complement** that covers what empirical methods can't reach (futures that don't exist yet).

---

## 6. Proposed Research Agenda: Speculative Methods for AI-for-Product

### Near-Term (Can Start Now)

1. **Design Fiction Workshop Series**: Create diegetic prototypes of AI-integrated product teams for each lifecycle phase; use as research instruments to elicit practitioner requirements
2. **Anticipatory Ethics Audit**: Apply Lazar's technological horizon method to map affordances of current AI PM tools (the 51 tools analyzed in our survey) that could produce unintended harms
3. **SFP for AADM Validation**: Write short SF prototypes for each cell of the AI-Augmented Decision Matrix to test whether the proposed human-AI allocation "feels right" to practitioners

### Medium-Term (Requires Collaboration)

4. **Speculative Enactments of Selective Complementarity**: Let product teams role-play scenarios where AI handles different degrees of autonomy at each lifecycle phase; measure decision quality, satisfaction, and trust
5. **Responsible Computational Foresight for Product Lifecycle**: Use AI to model multiple futures for AI-integrated product development; compare human interpretation of AI-generated scenarios with scenarios written by SFP practitioners

### Validation Need

- Speculative methods have growing academic legitimacy (Cambridge Design Science, Futures, HCI journals) but remain **methodologically underspecified**
- The field needs standardized evaluation criteria: not "is the fiction good?" but "did the fiction reveal requirements/risks that other methods missed?"

---

## Key Sources

1. Wadinambiarachchi et al. (2025). "Imagining Design Workflows in Agentic AI Futures." https://arxiv.org/html/2509.20731v1
2. Johnson (2011). "Science Fiction Prototyping." Springer. https://link.springer.com/book/10.1007/978-3-031-01796-4
3. Wu (2013). "Imagination Workshops." Futures, Vol. 50. https://www.sciencedirect.com/science/article/abs/pii/S0016328713000505
4. Lazar (2024). "Anticipatory AI Ethics." Knight First Amendment Institute. https://knightcolumbia.org/content/anticipatory-ai-ethics
5. Perez-Ortiz (2025). "From Prediction to Foresight." arXiv:2511.21570. https://arxiv.org/abs/2511.21570
6. Lin (2023). "Generative AI Futures: A Speculative Design Exploration." ACM C&C. https://dl.acm.org/doi/10.1145/3591196.3596616
7. WEF/OECD (2025). "How to responsibly integrate AI into strategic foresight." https://www.weforum.org/stories/2025/12/ai-strategic-foresight-future-thinking/
8. Chiang (2010). "The Lifecycle of Software Objects." Subterranean Press.
