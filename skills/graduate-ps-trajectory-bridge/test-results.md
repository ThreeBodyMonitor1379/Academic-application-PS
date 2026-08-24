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
| `should-not-trigger-02` | `two-way-academic-fit` | pass | pass |
| `should-not-trigger-03` | `evidence-first-graduate-personal-statement` | pass | pass |
| `edge-case-01` | this skill, while rejecting invented causality | pass | pass |
| `edge-case-02` | this skill with a disclosure boundary | pass | pass |

The two rounds used the complete name/description routing table, including sibling and adjacent external skills. Evaluators did not receive case types, expected behavior, notes, workspace files, or prior test outcomes.

These results test routing precision only. They do not validate applicant facts, causal claims in a real life history, or admissions outcomes.
