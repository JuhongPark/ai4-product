# AI Risk & Resilience: STAMP/STPA, Safety-II/III, and Resilience Engineering

> **Date:** 2026-04-21
> **SDM lens:** MIT-canonical safety engineering (Leveson STAMP/STPA, Safety-III); resilience engineering (Hollnagel Safety-II, Rhodes)

---

## 1. Thesis

Traditional risk analysis for AI systems — enumerating vulnerabilities, measuring adversarial robustness, listing failure modes — treats safety as a **component-level** property. **Nancy Leveson's STAMP** (MIT; System-Theoretic Accident Model and Processes) reframes safety as a **control problem**: accidents result from inadequate **constraints on interactions between components**, not from component failures alone. This is the only safety method that natively handles emergent-behavior failures that characterize compound AI systems.

---

## 2. STAMP: The MIT Reference Model

Leveson developed **STAMP** at MIT. Foundational paper: Leveson (2004). "A New Accident Model for Engineering Safer Systems." http://sunnyday.mit.edu/accidents/safetyscience-single.pdf

### Core shift
- **Old view**: Accident = chain of component failures
- **STAMP view**: Accident = lack of adequate **control** over component interactions and system state
- **Unit of analysis**: **Constraints**, not events

### STAMP-based methods
| Method | Purpose |
|---|---|
| **STPA** (Systems-Theoretic Process Analysis) | Proactive hazard analysis during development |
| **CAST** (Causal Analysis Based on STAMP) | Accident investigation post-event |

MIT OCW 16.863J "System Safety" (Leveson) is the canonical course. https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/

### Safety-III (de Weck, Leveson)
MIT Engineering Systems Lab has extended STAMP to "Safety-III: A Systems Approach to Safety and Resilience." http://sunnyday.mit.edu/safety-3.pdf — a synthesis of STAMP with resilience engineering.

---

## 3. Applying STPA to a Compound AI System

STPA's four steps applied to an AI product feature:

### Step 1 — Purpose and hazards
- **Purpose**: AI customer service agent answers billing questions.
- **Hazards**:
  - H1: Agent gives incorrect financial information → customer loss, legal exposure
  - H2: Agent leaks customer PII → privacy breach
  - H3: Agent becomes unresponsive → customer frustration, churn
  - H4: Agent behavior diverges from policy → reputational risk (Klarna pattern)

### Step 2 — Control structure
Identify controllers and controlled processes:

```
        Regulator
            │
            ▼ (policy)
         Product Team
            │
            ▼ (prompts, guardrails)
         Orchestrator ──► LLM ──► Response
            │                        │
            ▼ (tool calls)           ▼
        Enterprise System        Customer
            │                        │
            └─── Customer data ◄─────┘
            (via MCP)
```

### Step 3 — Unsafe control actions
For each control action, identify:
- Not provided
- Provided when shouldn't
- Provided too early/late
- Stopped too soon / applied too long

Example (Orchestrator → LLM):
- **UCA-1**: Orchestrator invokes LLM without retrieving current customer state → answers about outdated balance (hazard H1)
- **UCA-2**: Orchestrator allows LLM to execute refund tool without confirmation → unauthorized refund (H1)
- **UCA-3**: Orchestrator exposes PII in prompt context → privacy leak via model logging (H2)

### Step 4 — Loss scenarios
For each UCA, identify scenarios:
- **UCA-3 scenario A**: Developer adds customer email to prompt for personalization → vendor logs retained → PII exposure
- **UCA-3 scenario B**: Multi-agent flow passes state without sanitization → PII crosses trust boundary

Mitigations become **constraints** on the control structure (policy: no PII in prompts; architectural: PII sanitization middleware; audit: log scanning for PII patterns).

---

## 4. STAMP Applied to the Klarna Reversal

As a CAST exercise (retrospective):

**Hazard that materialized**: Customer satisfaction degradation → business reversal.

**Control failures**:
- **Product team → Orchestrator**: Insufficient constraint on "when to escalate to human" — the policy was implicitly "never" rather than a graded ladder
- **LLM → Customer**: No feedback signal on customer dissatisfaction being surfaced to Orchestrator in real time
- **Customer → Product team**: Complaint signal dampened by AI handling all Tier 1; problems accumulated invisibly
- **External → Product team**: Public reporting lagged; when reputation damage became visible, remediation cost exceeded original savings

**Systemic fix (STAMP-style)**: Not "add humans back" but redesign the control structure so that customer-dissatisfaction signals propagate fast enough to trigger constraint-adjustment on the Orchestrator.

This is the SDM-analytic way to reason about 2024–2025 AI service reversals — diagnostic, not judgmental.

---

## 5. Safety-II (Hollnagel)

Erik Hollnagel's **Safety-II** reframes safety not as the **absence of failures** but as the **presence of successful adaptive work**. Complementary to STAMP:

- Safety-I: "Why do things go wrong?" → eliminate failures
- Safety-II: "Why do things go right?" → sustain adaptive capacity
- Safety-III (Leveson): synthesis — control structures must support adaptive work

For AI systems, Safety-II asks: **what are humans + AI doing daily to keep the system working despite imperfect design?** Those adaptive practices should be protected and reinforced, not automated away.

Sources: Hollnagel (2013) *Safety-I and Safety-II.* Ashgate. / ScienceDirect (2020) "Safety-II and Resilience Engineering in a Nutshell." https://www.sciencedirect.com/science/article/pii/S2093791120303619

---

## 6. Resilience Engineering (Hollnagel's four capabilities)

A resilient system has four abilities:
1. **Monitor** — know what's happening now
2. **React** — respond to disturbance
3. **Learn** — update from experience
4. **Anticipate** — imagine future disturbances

Applied to AI systems:
- **Monitor**: comprehensive observability (see [governance paper](ai-governance-measurement.md)) — traces, latency, hallucination rates, user sentiment
- **React**: graceful degradation — fallback models, circuit breakers on tool calls, human-handoff paths
- **Learn**: incident post-mortems, red-team playbook updates, eval suite expansion
- **Anticipate**: red-teaming for unknown failure modes, scenario planning (design fiction / anticipatory ethics — see [speculative-methods paper](../../cross-cutting/papers/speculative-methods-research-implications.md))

This is **Donna Rhodes's** framing (MIT SEAri) applied to AI.

---

## 7. AI-Specific Hazards for STPA Inventory

Based on 2025–2026 industry incidents and the [DevSecOps paper](../../productization-skills/papers/ai-devsecops-security.md):

| Hazard class | Example | STPA-relevant control |
|---|---|---|
| **Hallucination with harm** | Financial/medical advice | Output validation, source citation gates |
| **PII leakage** | User data in prompts, model logs | Input sanitization, vendor data policies |
| **Prompt injection** | Malicious content executes unintended actions | Input classification, tool-call allowlist |
| **Tool misuse** | LLM invokes destructive tool incorrectly | Permission graduation, human confirmation |
| **Cross-agent state corruption** | Multi-agent handoff leaks context | Explicit interface validation |
| **Drift** | Output quality degrades over time | Continuous eval, drift alarms |
| **Silent coordination / collusion** | AI agents converging on emergent behavior | Behavioral monitoring, independent audit |
| **Vendor dependency failure** | Upstream LLM API outage or policy change | Multi-vendor routing, fallback paths |

Each is a candidate control-structure design decision, not just a risk register entry.

---

## 8. Operationalizing: A Safety Case for AI Products

A **safety case** (SDM-canonical) argues that a system is sufficiently safe given its context. For an AI product, a safety case includes:

1. **Purpose + hazards** (STPA Step 1)
2. **Control structure** diagram (STPA Step 2)
3. **Unsafe control actions** and mitigating constraints (STPA Step 3/4)
4. **Operational monitoring** evidence — live observability data showing constraints hold
5. **Incident response plan** — what happens when constraints fail
6. **Resilience capabilities** — Hollnagel's four abilities documented
7. **Review cadence** — when the safety case is revisited

A safety case is the **artifact** that an AI product team produces for regulators, auditors, and their own architecture review. EU AI Act compliance overlaps substantially with safety-case production (see [EU AI Act paper](../../cross-cutting/papers/eu-ai-act-product-impact-2026.md)).

---

## 9. Stakeholders

| Stakeholder | Role in safety work |
|---|---|
| System architect | Produces STPA artifacts, defines control constraints |
| Security | Integrates hazard analysis with threat modeling |
| Legal / compliance | Uses safety case for audit defense |
| Operations | Implements monitoring and response for Safety-II capabilities |
| Executive | Accepts residual risk; signs safety case |
| End user / public | Benefits from constraints (often invisibly) |

---

## 10. Research Gaps

1. **STPA for compound AI systems** — No published STPA reference analysis for canonical agentic patterns
2. **Safety-III for AI specifically** — MIT Safety-III framework not yet fully adapted to LLM-specific failure modes
3. **AI-agent CAST investigations** — Klarna-style reversals publicly documented but not rigorously analyzed with CAST
4. **Resilience metrics** — Hollnagel's four capabilities lack standard operational metrics
5. **Safety-case tooling** — No widely-adopted tool for AI-specific safety cases (aerospace/automotive have GSN; AI doesn't)

---

## 11. Sources

- Leveson, N. (2004). "A New Accident Model for Engineering Safer Systems." http://sunnyday.mit.edu/accidents/safetyscience-single.pdf
- Leveson & Thomas (2018). *STPA Handbook.* https://www.flighttestsafety.org/images/STPA_Handbook.pdf
- Leveson. "Applying STAMP in Accident Analysis." NASA. https://shemesh.larc.nasa.gov/iria03/p13-leveson.pdf
- MIT OCW. 16.863J System Safety. https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/9b08616e217ffd3fafc2dd1c19fff8be_MIT16_863JS16_LecNotes2.pdf
- MIT ESL. "Safety III." http://sunnyday.mit.edu/safety-3.pdf
- Hollnagel, E. (2013). *Safety-I and Safety-II.* https://www.amazon.com/Safety-I-Safety-II-Erik-Hollnagel/dp/1472423089
- Hollnagel. "Safety-II and Resilience Engineering in a Nutshell." ScienceDirect 2020. https://www.sciencedirect.com/science/article/pii/S2093791120303619
- Functional Safety Engineer. "Introduction to STAMP." https://www.functionalsafetyengineer.com/introduction-to-stamp/
- UL. "Understanding STAMP, STPA, and CAST." https://www.ul.com/sis/blog/introduction-to-stamp-stpa-and-cast
- ScienceDirect (2021). "STAMP Scoping Review." https://www.sciencedirect.com/science/article/abs/pii/S0925753521004082
- MIT SERC (2025). "A Systems Engineering Perspective on Safety of AI-based Systems." https://sercuarc.org/wp-content/uploads/2025/06/Track-4_05.-Reginald-Holmes.pdf
- Resilience Engineering Association. https://www.resilience-engineering-association.org/resources/where-do-i-start/
- PSNet. "Safety-I, Safety-II, and New Views of Safety." https://psnet.ahrq.gov/primer/safety-i-safety-ii-and-new-views-safety
