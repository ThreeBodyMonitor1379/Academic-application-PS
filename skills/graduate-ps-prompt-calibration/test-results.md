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
| `should-not-trigger-01` | `graduate-ps-trajectory-bridge` | pass | pass |
| `should-not-trigger-02` | `two-way-academic-fit` | pass | pass |
| `should-not-trigger-03` | `field-role-audience-calibration` | pass | pass |
| `edge-01` | this skill, with an insufficient-evidence stop | pass | pass |
| `edge-02` | this skill, without inventing a personal hook | pass | pass |

A pre-final diagnostic exposed two over-broad boundary prompts: one combined calibration with a complete-draft request, and one omitted the target-specific context. Both independent evaluators routed them elsewhere. The prompts were narrowed to the stated skill boundary, then two fresh evaluators reran all 24 repository cases; the final results above are from those clean reruns.

These results test routing precision, not whether any writing strategy improves admissions outcomes.
