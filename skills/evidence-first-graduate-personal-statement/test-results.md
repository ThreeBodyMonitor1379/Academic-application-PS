# Routing Test Results

- **Version:** `0.1.0`
- **Date:** 2026-08-24
- **Suite:** 8 fixed Darwin-compatible prompts from `test-prompts.json`
- **Evaluators:** two independent clean-context agents given only the complete routing table and anonymous prompt text
- **Final result:** **8/8**, **100%** in round A; **8/8**, **100%** in round B
- **False activation on bait cases:** 0/3 in each round

| Case | Expected primary route | Round A | Round B |
|---|---|---|---|
| `should-trigger-01` | this skill | pass | pass |
| `should-trigger-02` | this skill | pass | pass |
| `should-trigger-03` | this skill | pass | pass |
| `should-not-trigger-01` | `graduate-ps-prompt-calibration` | pass | pass |
| `should-not-trigger-02` | `graduate-ps-trajectory-bridge` | pass | pass |
| `should-not-trigger-03` | `academic-cover-letter-evidence-map` | pass | pass |
| `edge-01` | this skill, then readiness hold/override behavior | pass | pass |
| `edge-02` | this skill with a disclosure boundary | pass | pass |

The product workflow also passed 9/9 fictional instruction-conformance simulations: discoverable information, vague-answer follow-up, sensitive disclosure refusal, informed early exit, official-source conflict, readiness hold, taught master's, research master's/PhD, and cross-field/weakness scenarios.

These results test routing and written workflow behavior only. They do not verify applicant facts, current programme information, essay quality in an unseen case, or admissions outcomes.
