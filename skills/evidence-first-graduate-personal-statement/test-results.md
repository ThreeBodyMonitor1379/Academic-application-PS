# v0.2.0 Validation Results

- **Version:** `0.2.0`
- **Date:** 2026-08-26
- **Suite:** 22 fixed Darwin-compatible cases in `test-prompts.json`
- **Scope:** routing, observable workflow behaviour, schema/structure, and one fully fictional end-to-end smoke test
- **Final acceptance:** pass

## 1. Static validation

| Check | Result |
|---|---|
| `quick_validate.py` frontmatter and skill structure | pass |
| `test-prompts.json` parse and unique IDs | pass: 22/22 unique |
| example `PS_EVIDENCE_MAP.yaml` schema parses | pass |
| internal Markdown references resolve | pass: 0 missing |
| anonymous-source scan for applicant, institution and project identifiers | pass: 0 matches |

`quick_validate.py` was run with an isolated temporary PyYAML dependency because the default Python environment did not include PyYAML.

## 2. Blind routing

Two independent clean-context evaluators classified the original 17-case routing set without reading expected labels or test-result files.

- Round A: **17/17** correct.
- Round B: **17/17** correct.
- False activation on six bait cases in each round: **0/6**.

The bait cases covered prompt-only interpretation, trajectory-only work, academic cover letters, a single CV bullet, programme-fit-only work and pure technical teaching. Positive cases covered technical and non-technical graduate programmes, user-defined ordered interviews, excluded old drafts and LaTeX/PDF delivery.

The five later regression cases (`edge-07` to `edge-11`) were evaluated as focused blind behaviour tests after the core routing run; they did not alter the trigger boundary.

## 3. Blind behaviour and pressure tests

An initial clean agent evaluated nine hypothetical states: order-preserving questioning, mixed negative answers, public-code compatibility work, throughput without latency, team result versus personal action, outline approval, user override, excluded-source handling and working-format LaTeX. It obeyed one-question ownership and the two drafting gates, while identifying four specification gaps:

1. mixed answer states needed atomic claim splitting;
2. readiness needed a per-dimension hard cap;
3. numeric but uncontrolled runs needed their own validation stage;
4. accidental excluded-source access needed a contamination protocol.

All four were repaired. A second blind regression passed the repaired behaviours and found three operational ambiguities: missing-log evidence availability, read-only mutation authority and contaminated artifact versioning. These were also repaired with `evidence_availability`, an explicit no-write gate and `active_version`/`invalidated_versions` handling.

A final clean regression confirmed the contamination sequence has no approval bypass:

`invalidate old outline/draft → rebuild clean unapproved outline → keep active draft null → obtain explicit outline approval → create new English draft`.

Final focused regression result: **pass**, with no remaining bypass reported.

## 4. Fictional end-to-end smoke test

The isolated fixture used invented applicant, institution, courses, results and programme resources. Two trap files, an old PS and CV, were explicitly excluded.

### Before outline approval

- Created the required five artifacts.
- Parsed 10 atomic claims and 3 fit resources.
- Readiness: all five dimensions `0`; aggregate `0.00`; hard cap `PASS`.
- State stopped at `outline-review` with `outline_approved: false`.
- No English, TeX or PDF file existed.
- Excluded trap files were not opened, searched, quoted or paraphrased; `source_contamination` remained empty.

### After explicit approval

- A separate dated fixture explicitly approved outline `v1` and authorised English drafting.
- English and TeX files were created only after that approval record.
- English body: **717 words**, within the fictional 700–800-word requirement.
- All 10 claims carried `evidence_availability`; YAML parsed successfully.
- Claim ceilings remained intact: a public algorithm was only compatibility-adapted and qualitatively observed; `50→120 FPS` remained runtime-reported throughput and was not converted into latency; team assets were not personal achievements; the prototype remained future-only.

### LaTeX/PDF and visual QA

- Engine: XeLaTeX, TeX Live 2026.
- Working format, not an official rule: 12pt exact Times New Roman, letter paper, 1-inch margins and 1.15 line spread.
- PDF: 2 pages, 50,293 bytes, below the fictional 1 MB limit.
- Embedded fonts: `TimesNewRomanPSMT` and `TimesNewRomanPS-BoldMT` TrueType subsets.
- Final log: no errors, missing fonts, overfull/underfull boxes, missing characters or unresolved references.
- Every page was rendered to PNG and visually checked for cropping, overflow, malformed characters, density, page breaks and near-empty pages.
- The first render exposed an almost empty second page; the working layout was revised and recompiled before the final visual pass.
- Final release state: `ready-for-user-review` for the fictional fixture.

## 5. Acceptance matrix

| Criterion | Result |
|---|---|
| Routing tests 100% | pass: 17/17 in both clean rounds |
| Bait zero false activation | pass: 0/6 in both rounds |
| Ordered mode asks one question per turn | pass in blind behaviour audit |
| `forgotten / none / not_involved / excluded_by_user` stop rules | pass after atomic-state regression |
| No unconfirmed applicant facts | pass in fictional smoke test |
| No claim beyond source, modification, validation or metric boundary | pass |
| No English drafting before explicit outline approval | pass, including file-time check |
| LaTeX compile and PDF visual QA | pass after one layout iteration |

These tests validate routing and observable workflow behaviour, not real applicant facts, current programme requirements, admissions quality or outcomes. Real uses must still verify the current official prompt and portal constraints.
