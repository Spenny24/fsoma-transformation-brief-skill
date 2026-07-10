# FSOMA Transformation Report Kit, v0.9, Public Preview

## Release status

- Private and internal testing: approved.
- Trusted dogfooding: approved.
- GitHub public preview: approved, conditional on your final manual check of the sample docx before you push. See the Final Sweep section below for what's already been checked.
- Claude marketplace listing: not approved yet.
- Client-facing use: partial. One benchmark (McKinsey, marketing productivity uplift) is Primary verified and usable in client-facing output. Every other claim in the skill's output still needs Mode 3 graceful degradation or a user-supplied register.

## Architecture change this pass: the skill no longer depends on its own benchmark library

Previously, the skill's client-facing output was blocked entirely until Craig traced and signed off a full benchmark register. That was the wrong dependency to build. The skill now runs in three benchmark modes, checked in order every run:

1. User-provided benchmark register, if the user supplies one, preferred over the default register for any metric both cover.
2. The skill's own default verified register (`references/default-benchmark-register.md`), Primary verified and Client-facing rows only, nothing else lives there.
3. No verified benchmark available for a claim, the report does not fail. It uses client-owned baseline data only, states the gap in fixed required wording, and adds the gap to Leadership Decisions Needed and Recommended Next Steps.

This means public release does not require a large benchmark library. It requires the schema, the three-mode logic, and a default register that only ever contains rows that actually pass all ten client-facing conditions, even if that register is one row deep.

## What is validated, three test runs plus this hardening pass

1. Separates AI productivity, spend recovery, tooling rationalisation, and revenue growth into four distinct commercial model categories, never blended into one figure. Each category now has its own benchmark rule, not just its own evidence basis, spend recovery and tooling rationalisation never use an AI productivity benchmark, verified or not.
2. Refuses to invent a revenue growth case when no revenue-linked KPI exists, states "No revenue growth case is presented" instead.
3. Cross-checks top-down, client-stated, bottom-up, and benchmark-derived commercial estimates, labels the result converges, diverges, not comparable, or not evidenced, and turns a divergence into a validation action rather than smoothing over it.
4. Flags RACI gaps instead of inventing accountable owners, excludes ungoverned activities from the future-state RACI.
5. Turns material gaps into named leadership decisions and matching Recommended Next Steps actions, checked line by line, not just once per report.
6. Uses chart-safe numbered markers and a legend whenever item count, label collision, or label length would otherwise produce an unreadable chart.
7. Separates every KPI, RACI row, and technology entry by evidence confidence: Validated, Partially validated, Needs validation, Not evidenced.
8. Uses Data Inventory and Risk & Assumption Register inputs when present, feeding KPI confidence, roadmap sequencing, automation readiness, reporting feasibility, commercial model confidence, the Executive Readout, and Recommended Next Steps.
9. Produces a leadership report with a clear consultant point of view, "Our recommendation" callouts after every major table, not a data dump.
10. Renders wide tables (more than 6 columns) as decision-critical summaries in the main body with full data in a landscape appendix, no header or ID wrapping.
11. New this pass: runs in three benchmark modes and degrades gracefully to client-owned baseline data when no verified benchmark exists, rather than blocking report generation entirely.
12. New this pass: validates user-provided benchmark rows against the schema independently, never takes a user's own evidence_status or allowed_use label at face value.

## Benchmark register status

- `references/default-benchmark-register.md`: 1 row. McKinsey, "The economic potential of generative AI: The next productivity frontier," 5-15% marketing function productivity uplift, published 14 June 2023. Traced directly against mckinsey.com. All ten client-facing conditions met. This is the load-bearing figure for Commercial Model Category 1, so this one row already unlocks a real client-facing productivity claim in Mode 2, not just internal-challenge output.
- `references/benchmark-sourcing-backlog.md`: 12 candidate rows, all Secondary/internal or Draft/unverified. One rejected finding worth flagging directly: the commonly repeated "87% of marketers use generative AI in at least one workflow" Salesforce figure could not be confirmed on a Salesforce-owned page. The primary Salesforce page found and fetched directly states 75% general AI adoption, a related but different metric, published 19 February 2026. Do not use 87% anywhere in client-facing output until the full downloadable report PDF is checked directly.

## Test history

- Test 1: sanitized real client dataset from a live enterprise engagement, sanitized mid-session after the gap was caught. Process lesson: sanitize at intake on any future real-data test, not after ingestion. Client name and specifics excluded from this document per public packaging rules.
- Test 2 and Test 3 (final): synthetic NexaGlow Beauty dataset, richer input including Data Inventory and Risk Register categories. Test 3 is the accepted quality bar. Two real bugs were caught and fixed in that pass: a Section 1 decision that never reached Section 14, and a benchmark status label wrapping across two lines in a narrow table column.
- No further mock-report iteration has run since Test 3. This pass was schema and logic hardening plus real source verification, not a new mock report. Per the standing instruction, the next test should be a focused benchmark-mode test, not another full report, covering: a user-provided Primary verified benchmark, a user-provided Draft/unverified benchmark, no benchmark available, the default verified benchmark in use, no revenue-linked KPI present, and a revenue-linked KPI present.

## Public marketplace release gate

All of the following must be true before Claude marketplace listing. This is separate from the GitHub public preview gate above, which is already cleared.

1. Skill package validates. Done.
2. Two or more synthetic test cases pass. Done, three runs completed.
3. Chart collision fix passes. Done, verified against a 12-item dataset that previously produced overlapping labels.
4. Four-category commercial model passes. Done.
5. Benchmark schema implemented, user-provided register supported, default register contains only Primary verified Client-facing rows, graceful degradation on missing benchmarks. Done, this pass. The default register is intentionally small, 1 row, but every row in it is real.
6. Claude marketplace listing copy is written. Not done. Draft positioning line exists in SKILL.md, full copy still needed. This is separate from the GitHub public preview, which does not require marketplace copy.
7. Example input/output is sanitised for public display, and a GitHub README exists confirming FSOMA branding throughout. Done. Full public-packaging sweep passed: no legacy internal codename references, no agency-holding-company references, no real client names, no internal platform names from any prior engagement, sample output labelled fictional/synthetic on its cover page, no overstated automation claims anywhere in the public copy. README.md now exists at repo root, FSOMA-branded, and was missing before this sweep caught it.
8. Client-facing benchmark mode excludes every non-Primary-verified source. Done, enforced in SKILL.md Behaviour 7 and proven against a real case (the Salesforce figure was correctly excluded, not smoothed over).
9. Final QA checklist (16 items, SKILL.md, Mandatory pre-delivery visual QA) passes on the release candidate report. Items 1-11 passed on the Test 3 rebuild. Items 12-16 (title-page appendix mislabelling, numbered-list rendering, appendix placement, appendix labelling, table header/column-width consistency) are new this pass, added after the BrightBite Foods test run surfaced exactly these polish defects, and have not yet been re-run end to end against a freshly generated report.

## This pass: Brief to Report rename, NexaGlow contract restored, Word polish hardening

This pass found that the published GitHub repo was behind the working copy of this skill: it still carried the pre-NexaGlow-contract SKILL.md and the old 6-section current-state-only `output-structure.md`, neither of which had been pushed here yet. Both are now brought up to date as part of this pass, alongside the rename:

- Product and repo wording renamed from "Brief" to "Report" throughout: public name, technical identifier (`fsoma-transformation-report-skill`), section headings, example filenames. Ordinary uses of "brief" that refer to a client/creative brief (creative briefing, brief intake, pre-brief) were left unchanged, they are not the product name.
- `SKILL.md` restored to include the Output Format Contract — NexaGlow Standard, the Stage 5 "Assemble in NexaGlow Report Format" heading, and Section 13 (Data Foundation Readiness) as unconditionally mandatory, none of which were present in the previously published version.
- `references/output-structure.md` rewritten from the old 6-section current-state template to the full locked 14-section NexaGlow structure, matching what SKILL.md's Stage 5 has specified for several sessions.
- Word output polish rules added: title-page format lock, appendix placement and labelling rules, numbered-list-to-bullet fallback, consistent table header styling, long-table-to-appendix rule, no orphaned page labels.
- Mandatory pre-delivery visual QA extended from 11 to 16 checks, covering the polish rules above.
- No change to any analytical or evidence rule: evidence tagging, RACI governance, the four-category commercial model split, the cross-check logic, or the Mode 3 required wording are all unchanged from the prior version.

Six of nine gate items are now done, up from five before this pass.

## Open items, escalate to Craig, not solvable through more testing

- Continue tracing `references/benchmark-sourcing-backlog.md`, one row at a time. Highest value next: confirm the Salesforce adoption figure via the full report PDF, since it is the second most commonly needed marketing-AI-maturity stat after the McKinsey productivity figure.
- Final skill naming. Renamed this pass from "Brief" to "Report." Public name is FSOMA Transformation Report Kit, repo name fsoma-transformation-report-skill. No longer an open item.
- Supabase/storage decision, whether this skill logs outputs to the existing FSOMA memory layer or stays standalone.
- Marketplace listing copy, full version.
- Example input/output packaging for public display.

## Next workstream

A focused benchmark-mode test (the six scenarios listed under Test History), then continued backlog tracing. Not another full mock report.
