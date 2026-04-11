# Selective Complementarity: When to Use AI vs Humans Across the Product Lifecycle

> Mapping the Nature meta-analysis (creation vs decision tasks) and Stanford's selective recommendation model onto each phase of the product lifecycle.

---

## Theoretical Foundation

### Nature Human Behaviour Meta-Analysis (Vaccaro et al., 2024)

106 experiments, 370 effect sizes:
- **Decision tasks**: AI alone > Human+AI > Human alone (adding humans hurts)
- **Creation tasks**: Human+AI > Human alone > AI alone (combination helps)

### Stanford Complementary Algorithm (Spiess et al., 2025)

- AI that offers selective recommendations only when humans are likely uncertain → **best decisions overall**
- Outperforms: full AI, full human, and standard AI recommendations
- Key insight: "The best algorithm takes into account how a human will interact with the information it provides"
- Source: https://www.gsb.stanford.edu/faculty-research/working-papers/designing-algorithmic-recommendations-achieve-human-ai

### EJIS Complementarity Sources (2025)

Two preconditions for complementarity to emerge:
1. **Information asymmetry**: Human has context AI lacks (or vice versa)
2. **Capability asymmetry**: Human excels at things AI cannot (or vice versa)

Source: https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

---

## Product Lifecycle Phase Mapping

### Classification Framework

Each product phase contains a mix of task types. The Nature meta-analysis distinction (creation vs decision) determines the optimal human-AI allocation:

| Phase | Primary Task Type | Optimal Model | Rationale |
|-------|------------------|---------------|-----------|
| **Discovery** | Mixed (empathy + pattern) | Human-led, AI-augmented | Customer empathy requires human context; AI scales data analysis |
| **Design** | Creation | Human+AI collaboration | Nature: creation tasks benefit most from combination |
| **Development** | Execution | AI-led, human-reviewed | Clear input→output; AI excels; human reviews for quality |
| **Testing** | Verification | AI-led, human-reviewed | Pattern matching at scale; human validates edge cases |
| **Launch** | Decision (strategic) | Human-led, AI-informed | Political/strategic judgment; AI provides data, human decides |
| **Growth** | Mixed (analysis + judgment) | Selective complementarity | AI detects patterns; human interprets meaning and acts |

### Detailed Phase Analysis

#### Discovery: Human-Led, AI-Augmented
```
Human strengths: Empathy, reading between lines, identifying unspoken needs
AI strengths:   Scale (80K interviews), pattern detection in review data, segmentation
Failure mode:   AI alone → misses context, gives generic insights (Klarna pattern)
Success model:  AI conducts at-scale interviews, human interprets and synthesizes
Evidence:       HBR April 2026 — 7x longer responses to AI, but human interpretation needed
```

#### Design: Human+AI Collaboration (Highest Complementarity)
```
Human strengths: Aesthetic judgment, brand coherence, creative vision
AI strengths:   Rapid variation generation, adaptive interfaces, personalization
Failure mode:   AI alone → technically correct but lacks soul/coherence
Success model:  Human sets creative direction, AI generates variations, human curates
Evidence:       Nature meta-analysis — creation tasks show positive complementarity
                Figma Make — 40-60% faster with human+AI, not AI alone
```

#### Development: AI-Led, Human-Reviewed
```
Human strengths: Architecture decisions, system design, complex debugging
AI strengths:   Code generation, test writing, documentation, boilerplate
Failure mode:   AI alone → 15% success (Devin), 45% security vulnerabilities
Success model:  AI generates, human reviews; AI handles routine, human handles novel
Evidence:       Devin — senior at understanding, junior at execution
                EPAM PostNL — 80% time savings but human oversight maintained
```

#### Testing: AI-Led, Human-Reviewed
```
Human strengths: Edge case identification, user scenario design, acceptance criteria
AI strengths:   Test generation, regression testing, continuous testing, anomaly detection
Failure mode:   AI alone → 8.3% flaky tests; misses semantic intent
Success model:  AI generates and runs tests, human defines what to test and validates
Evidence:       EY.ai PDLC — 95%+ automated test coverage with human oversight
```

#### Launch: Human-Led, AI-Informed
```
Human strengths: Strategic timing, stakeholder management, risk tolerance, market sense
AI strengths:   Market data analysis, competitive monitoring, demand prediction
Failure mode:   AI alone → cannot judge organizational readiness or market timing
Success model:  AI provides data-driven scoring (AI-PRISM), human makes go/kill decision
Evidence:       Cooper AI-PRISM — decision support tool, not autonomous decision-maker
                ~80% of NPD investment decisions wrong → inherently uncertain
```

#### Growth: Selective Complementarity (Stanford Model)
```
Human strengths: Interpreting why users churn, causal reasoning, strategic pivots
AI strengths:   Pattern detection, A/B test analysis, personalization at scale
Failure mode:   AI alone → optimizes for short-term metrics, misses long-term health
                Human alone → cannot process data at scale
Success model:  AI flags anomalies and provides recommendations ONLY when human
                is likely uncertain; human decides when signal is ambiguous
Evidence:       Stanford complementary algorithm — best decisions when AI is selective
                OpenTable — 73% autonomous for routine, human for complex
```

---

## The Selective Complementarity Decision Tree

```
For any product task, ask:

1. Is there a clear, verifiable correct answer?
   YES → AI-led (development, testing, data processing)
   NO  → Go to 2

2. Does the task require creative/aesthetic judgment?
   YES → Human+AI collaboration (design, ideation, content)
   NO  → Go to 3

3. Is the decision data-rich with clear patterns?
   YES → AI recommends, human decides (growth analytics, prioritization)
   NO  → Go to 4

4. Does the decision involve genuine uncertainty, ethics, or strategy?
   YES → Human-led, AI-informed (launch, pivot, go/kill)
   NO  → Evaluate case by case
```

---

## Key Sources

1. Vaccaro et al. (2024). Nature Human Behaviour. https://www.nature.com/articles/s41562-024-02024-1
2. Spiess et al. (2025). Stanford GSB. https://www.gsb.stanford.edu/faculty-research/working-papers/designing-algorithmic-recommendations-achieve-human-ai
3. "Complementarity in Human-AI Collaboration." EJIS, 2025. https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962
4. "Human-AI complementarity needs augmentation, not emulation." Nature Reviews Psychology, 2026. https://www.nature.com/articles/s44159-026-00536-3
5. "Three Challenges for AI-Assisted Decision-Making." Perspectives on Psychological Science, 2024. https://journals.sagepub.com/doi/full/10.1177/17456916231181102
