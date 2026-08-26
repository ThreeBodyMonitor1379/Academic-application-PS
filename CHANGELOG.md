# Changelog

All notable changes to this project are documented here.

## [0.2.0] - 2026-08-26

### Added

- Order-preserving interviewing for user-supplied PS/SOP outlines, with a six-part default framework when no schema is provided.
- An answer-state model covering `confirmed`, `tentative`, `unknown`, `forgotten`, `none`, `not_involved`, `excluded_by_user`, `do_not_disclose`, and `conflicting` material.
- Claim calibration for source ownership, modification scope, validation stage, metric meaning, team attribution, claim ceilings, and permitted verbs.
- `PS_CHINESE_OUTLINE.md` plus an explicit applicant-approval gate before English drafting.
- Drafting and release guidance for current official requirements, LaTeX/PDF generation, font and layout inspection, and visual QA.
- Source-contamination handling, artifact version invalidation, a human-readable method digest, and anonymous conversation-derived provenance notes.

### Changed

- Upgraded `evidence-first-graduate-personal-statement` from `0.1.0` to `0.2.0`; the two focused sibling skills remain at `0.1.0`.
- Expanded the orchestrator from four to five persistent project artifacts and extended the evidence-map schema with answer, source, modification, validation, metric, claim-ceiling, evidence-availability, and release fields.
- Added a per-dimension readiness hard cap so an aggregate score cannot hide a wholly unresolved target or evidence dimension.
- Restricted completed PS/CV files to explicitly authorised, low-confidence fact leads and prohibited reuse of their wording.
- Updated repository validation to support per-skill versions and test-suite sizes.

### Validation

- Passed the skill structure validator, JSON/YAML parsing, internal-link checks, and anonymous-source scans.
- Passed two independent 17-case routing rounds for the upgraded orchestrator: `17/17` each, with `0/6` false activations on bait cases.
- Passed five focused boundary regressions and a fully fictional end-to-end smoke test through approved outline, English draft, XeLaTeX compilation, and rendered PDF inspection.

### Boundaries

- The extension records observable decision protocols only; it does not store or claim hidden chain-of-thought.
- Applicant motivation, interpretation, values, causal meaning, and goals remain applicant-owned unless the applicant explicitly requests and then confirms candidate wording.
- No English draft may become active before the applicant approves a specific Chinese-outline version.
- Official programme requirements remain controlling; working typography must not be presented as an institutional rule.

## [0.1.0] - 2026-08-24

### Added

- `evidence-first-graduate-personal-statement`, a transparently labelled product-layer orchestrator with one-question-at-a-time evidence grilling and a five-dimension drafting gate.
- `graduate-ps-prompt-calibration`, a source-verified skill for interpreting the actual programme task instead of relying on PS/SOP labels.
- `graduate-ps-trajectory-bridge`, a source-verified skill for building a non-binding past–present–future academic trajectory.
- Internal references for project state, evidence mapping, paragraph construction, programme-fit routing, privacy, and final QA.
- Darwin-compatible routing tests, anonymous workflow scenarios, a release validator, and a conflict-safe installer.
- Chinese human documentation and a copy-ready Agent installation instruction pinned to `v0.1.0`.

### Boundaries

- No applicant material, source PDF, screenshots, or full before/after examples are distributed.
- No user-level installation, application submission, faculty contact, or GitHub publication occurs without the corresponding explicit user approval.
