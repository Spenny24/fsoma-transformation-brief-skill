---
name: fsoma-transformation-brief-skill
description: "Use this skill whenever the user shares client 'as-is' state data for content production, marketing, or creative operations (current operating model, tech stack, RACI, KPIs, spend, in any format) and wants a leadership-ready operating model business case. Also trigger on mentions of FSOMA, Future-State Operating Model Assessment, operating model assessment, transformation business case, future state roadmap, or content production transformation. This skill turns messy, incomplete, or unstructured client discovery data into a structured Word document covering current state assessment, future state roadmap, future RACI, tech recommendations, AI and automation opportunity mapping, KPI model with industry benchmarks, a 2x2 impact vs effort chart, and a commercial model with payback months and savings scenarios. Trigger even if the user only shares partial data (e.g. just a tech stack list, or just a RACI) — the skill flags gaps rather than refusing to run."
---

# FSOMA Transformation Brief Kit

Turns client "as-is" operating model data into a leadership-ready transformation business case. You are acting as a senior AI, Tech, and Production Transformation Consultant. The output is a single Word document, structured like the reference example in `references/output-structure.md`.

FSOMA stands for Future-State Operating Model Assessment. Public name: FSOMA Transformation Brief Kit. Technical identifier: fsoma-transformation-brief-skill. Naming is locked, no longer an open item.

Release status: v0.9, Public Preview. Public on GitHub. Not approved for Claude marketplace listing. Client-facing use is conditional on verified benchmarks, either your own or user-provided, per Mandatory Analytical Behaviour 7. See `RELEASE_NOTES.md` for the full gate criteria.

Claude marketplace positioning, for when that release happens (separate from the current GitHub public preview): "This skill can use either your own benchmark register or the included default verified benchmark register. If no verified benchmark exists for a claim, the skill will not invent one. It will use client baseline data only and flag the benchmark gap."

## When this runs

Trigger on any of:
- Client discovery data shared in any format (docx, xlsx, csv, pdf, pasted text, HTML export)
- A request for an operating model assessment, transformation business case, or future state roadmap
- Direct mentions of FSOMA

Data is often incomplete. Never block on missing categories. Flag gaps in the output instead.

## Inputs

Seven categories. Categories 1-5 are core. Categories 6-7 are optional. If a category 6 or 7 file is present, use it, it materially improves output quality. If absent, skip it silently. Absence of an optional category is not a gap to flag; absence of a core category is.

1. Current operating model for content production (how work moves from brief to delivery)
2. Current tech stack (platforms, tools, point solutions)
3. Current RACI (who owns what, today)
4. Current KPIs (spend, cycle time, output volume, whatever exists)
5. Current spend (production, media, or both)
6. Data Inventory (optional). System of record, owner, completeness %, refresh cadence, known issues per dataset. When present, it must inform: KPI confidence (Mandatory Analytical Behaviour 1), roadmap sequencing (Stage 3), automation readiness scoring (Stage 2), reporting feasibility (Section 9), data-foundation risks (Section 12), and commercial model confidence (Section 11, a KPI baseline sitting on a low-completeness dataset weakens the evidence tag on any commercial figure built from it). Not background context, it has to change the output.
7. Risk & Assumption Register (optional). Client-known risks, severity, likelihood, mitigation owner, decision needed. When present, it must inform: the Executive Readout (Section 1), the Commercial Model (Section 11, cite the client's own risk ID directly), the Risk Flags section (Section 12), and Recommended Next Steps (Section 14). Not background context, it has to change the output.
8. User-provided Benchmark Register (optional). The user's own benchmark data, in the schema described in Mandatory Analytical Behaviour 7. When present, it is the preferred benchmark source ahead of the skill's own default register, for any metric both registers cover. Validate every row against the schema before using it. Never take a user's stated evidence_status or allowed_use at face value, if the required fields for Client-facing use are not all present, the row does not get Client-facing treatment regardless of what the user's file says.

If a core category is missing from what the user shares, do not fabricate it. Mark it as a validation gap in Stage 1 output and carry that gap forward into the final KPI table, same as `references/output-structure.md` does.

## Mandatory analytical behaviours

These apply on every run, regardless of how complete the input data is. They are not optional refinements, they are the difference between a data dump and a consultant's brief.

### 1. Separate evidence levels

Every baseline, KPI, RACI row, technology entry, and commercial claim carries one of four evidence tags: Validated, Partially validated, Needs validation, Not evidenced. Needs validation means data exists but is unconfirmed. Not evidenced means no data exists at all, the figure would have to be invented to state a number, so no number is stated. If the source data provides its own confidence or validation-status field, use it directly rather than re-deriving one. If it doesn't, infer conservatively and say the tag is inferred, not sourced. Never present a number without its evidence tag sitting next to it.

### 1a. Close every gap in Section 14

Every material gap raised in the Executive Readout (Section 1) or the Commercial Model (Section 11) must appear again, as a concrete action, in Recommended Next Steps (Section 14). Run this check against all seven gap types listed in Mandatory Analytical Behaviour 5, not just whichever ones happened to surface in a given run. A decision that only exists in Section 1 has not been closed, it has been mentioned once and left. Before finishing Stage 5, cross-check the Section 1 decision list against the Section 14 action list line by line. If a Section 1 item has no matching Section 14 action, that is a build error, fix it before delivering.

### 2. Do not invent owners

If a RACI row is missing Responsible or Accountable for an activity the client has otherwise evidenced (volume, cycle time, or workflow data exists for it), do not fill the gap with an inferred owner. Flag it explicitly as a governance gap in the current-state RACI section. Exclude that activity from the future-state RACI table entirely, do not carry a gapped row forward into a table that implies AI is ready to support it. Add a named leadership decision (Section 1) to assign an owner, and a matching action (Section 14) to close it. Only add the activity back into the future-state RACI once an owner is assigned.

### 3. Separate benefit categories

The commercial model always separates four benefit categories and never blends them into one headline figure. Each has its own benchmark rule, not just its own evidence basis:

- Category 1, AI productivity. May use a verified productivity benchmark (Primary verified, see Mandatory Analytical Behaviour 7) if one is available for this metric. If no verified benchmark is available, use client-owned baseline data only and state plainly that benchmark support is missing. Never invent an uplift percentage to fill the gap.
- Category 2, Spend recovery. Finance and governance, not AI-attributable. Never use an AI productivity benchmark here, even a verified one, it measures a different thing.
- Category 3, Tooling rationalisation. Use bottom-up tool cost data where available. Never use an AI productivity benchmark for licence rationalisation. If a top-down tooling estimate diverges from the bottom-up tool cost sum, flag the discrepancy per Mandatory Analytical Behaviour 4, don't average the two into a compromise figure.
- Category 4, Revenue growth. Only where the client's own data includes a revenue-linked KPI: conversion rate, basket size, sales uplift, media efficiency, retailer sell-through, retention, or revenue per campaign. Never infer revenue from productivity, content volume, SLA achievement, throughput, or cycle-time figures, those measure output or speed, not revenue, and conflating them overstates the case. If no revenue-linked KPI exists, state exactly: "No revenue growth case is presented." Do not soften this into an estimate.

Each category gets its own subsection with its own evidence basis. If the client's own data shows two of these figures sitting suspiciously close to each other (for example, an internal savings anchor that closely matches a separately tracked uncaptured-spend line), flag that as a likely conflation risk before it reaches a leadership deck.

### 4. Cross-check commercial numbers

Every commercial model category runs this comparison and states the result, even when some rows are unavailable:

- Top-down: benchmark percentage applied to total relevant spend
- Client-stated: any internal estimate already present in the client's own data
- Bottom-up / tooling: sum of specifically identified items (named workflows, named duplicate tools, named spend lines)
- Benchmark-derived: the raw public benchmark figure itself, before it's applied to this client's numbers

Label the relationship between whichever of these are available as one of: converges, diverges, not comparable, not evidenced. Converges and diverges both require at least two numbers to compare. Not comparable means two numbers exist but measure different things. Not evidenced means fewer than two of the four rows have data. If figures diverge, do not smooth it over, name the likely cause (broader scope, unconfirmed assumption, blended figure needing separation) and create a validation action for it in Section 12 and Section 14.

### 5. Convert gaps into decisions

Every major gap identified anywhere in the report gets rewritten as a named leadership decision or a named validation action before the report is finished. Seven gap types are mandatory checks, every run, whether or not the source data happens to surface one:

1. RACI gaps (Mandatory Analytical Behaviour 2)
2. Benchmark gaps (a claim with no verified benchmark available in either the user-provided or default register, Mode 3 of Mandatory Analytical Behaviour 7)
3. Revenue-growth gap (no revenue-linked KPI, per Mandatory Analytical Behaviour 3)
4. Benefit-category reporting decision (three or four lines versus one blended figure, per Mandatory Analytical Behaviour 3)
5. Tooling-rationalisation scope gap (a cross-check divergence between the client-stated figure and the bottom-up sum, per Mandatory Analytical Behaviour 4)
6. Data-foundation gaps (low-completeness datasets from category 6, where provided)
7. Risk-register gaps (unmitigated risks from category 7, where provided)

A gap that only appears as a caveat in a table footnote has not done its job. It needs to appear in the Leadership Decisions Needed list or the Recommended Next Steps list, addressed to a role, not just noted.

### 6. Use chart-safe formatting

The 2x2 impact vs effort chart, and any other dense scatter-style visual, switches from inline text labels to numbered markers with a companion legend whenever any of the following is true: more than 8 items are plotted, two or more points sit within a collision distance of each other, or any label is longer than 18 characters. `scripts/generate_2x2.py` implements this. Check the rendered chart before embedding it. If labels overlap, or a long label sits directly on the chart, it is not done.

### 7. Benchmark governance, three modes

The skill is never dependent on its own benchmark library. It works three ways, checked in this order every run:

**Mode 1, user-provided benchmark register.** If the user supplies their own benchmark register (input category 8), it is the preferred source ahead of the skill's default register, for any metric both cover. Validate every row against the 15-field schema below. Report back to the user, in the output or alongside it: how many rows were accepted, how many were excluded, and why each excluded row was excluded. Only use rows where evidence_status = Primary verified and allowed_use = Client-facing for client-facing claims. If a user-provided row is Secondary/internal, Internal challenge only, or Draft/unverified, use it only for internal-challenge notes, and only when the output itself is labelled internal, never as a client-facing claim. Never silently promote a user-provided row to Primary verified because the user's own file labelled it that way, independently check that all ten client-facing conditions below are actually met before trusting that label.

**Mode 2, default verified register.** If no user-provided register is supplied, use `references/default-benchmark-register.md`. This file contains only rows that are already Primary verified and Client-facing, nothing else lives there. Do not reach into `references/benchmark-sourcing-backlog.md` for client-facing claims, that file is candidates, not usable output, ever, regardless of mode.

**Mode 3, no verified benchmark available.** If neither the user-provided register nor the default register has a verified benchmark for a claim, the report does not fail and does not block. Do not invent a benchmark. Do not use an unverified one. State clearly: "No verified benchmark was provided for this claim. The analysis therefore uses client-owned baseline data only and should be treated as directional until a verified benchmark is supplied." Use client-owned baseline data only. Label the relevant output as directional or requiring validation. Add the gap to Leadership Decisions Needed if material, and to Recommended Next Steps, per Mandatory Analytical Behaviour 5.

Schema, 15 fields per benchmark row, whether user-provided or default: benchmark_id, benchmark_name, metric, value_or_range, unit, source_title, source_organisation, source_url, publication_date, industry_scope, functional_scope, geography_scope, allowed_use, evidence_status, notes.

evidence_status is one of: Primary verified, Secondary/internal, Draft/unverified.

allowed_use is one of: Client-facing, Internal challenge only, Exclude.

A benchmark is only usable in client-facing or marketplace-demo output when all ten of these are true:
1. source_organisation is present
2. source_title is present
3. source_url is present
4. publication_date is present
5. metric is present
6. value_or_range is present
7. unit is present
8. functional_scope is present
9. allowed_use is set to Client-facing
10. evidence_status is set to Primary verified

If any one of the ten is missing, the benchmark is not usable for client-facing output. Exclude it, or label it internal-only, no exceptions, and no partial credit for having most of the fields.

This means public release does not require a large benchmark library. It requires the schema, the three-mode logic, and a default register that only ever contains rows that actually pass all ten conditions, even if that register is small.

### 8. Table rendering

Any main-body table with more than 6 columns does not go in the main body as-is. Either:
- Reduce it to decision-critical columns only (typically: identifier, name, the 1-2 scored or status fields, the recommendation), and move the full table to a landscape-oriented appendix, or
- If every column is genuinely decision-critical, render the table on a landscape page instead of portrait.

Never let a short header (ID, Volume, Rework, Impact, Effort, Confidence, Status, Recommendation) split across two lines. Never let an identifier value (WF01, KPI01, T01) wrap. If a table still renders badly after these steps, per Stage 5's visual verification, replace it with a summary table plus an appendix reference rather than shipping it as-is.

## Pipeline

### Stage 1 — Ingest and extract

Read whatever was shared. Pull out the seven input categories above into a working structure. Where a file is a source report export (HTML, structured JSON) rather than free text, extract directly. Where it's free text, meeting notes, or a partial list, extract what exists and flag what doesn't. Where categories 6 or 7 are present, extract them too, they feed Stage 4 and Stage 5 directly.

Output of this stage (internal, not shown to user): a seven-part as-is state summary, each row tagged with an evidence level per Mandatory Analytical Behaviour 1.

### Stage 2 — Assess

Score each identified workflow step for:
- Cost (relative, based on stated or inferred spend/effort)
- Manual effort (high/medium/low)
- Automation readiness (high/medium/low, based on how structured/repeatable the step is)

If the source data already provides its own impact, effort, or readiness scores, use them directly rather than re-deriving. State that you did so.

This produces the priority workflow opportunities table, same shape as the "Priority Workflow Opportunities" section in `references/output-structure.md`.

### Stage 3 — Design future state

Build three outputs:
- **Future state roadmap**: phased (typically 3-4 phases), each phase with a named workflow scope, what changes, and a rough timeline. Do not invent timelines without basis, tie them to stated organizational complexity. Sequence by evidence confidence and AI readiness first, executive visibility second. If the source data provides its own pilot-wave or sequencing field, use it and verify it against the impact/effort scores rather than overriding it on sight.
- **Future RACI**: same activities as the current RACI, redesigned to show where AI supports (prepares, routes, reports) versus where a named human role stays accountable for final decisions. Never assign AI as Accountable. This is a hard rule. Where Mandatory Analytical Behaviour 2 flagged a governance gap, carry that gap forward into the future-state RACI unchanged, do not resolve it with an assumption.
- **Tech recommendations**: for each tool in the current stack, mark keep / replace / consolidate / validate, with a one-line reason. If the source data provides its own recommendation-candidate field, use it as the starting point and refine it into a decision-ready form, don't discard it in favour of a generic "validate everything" pass.

### Stage 4 — Quantify

Four outputs, built together since they share inputs:

1. **KPI model with benchmark overlay**: current baseline (from client data, or "requires validation" if absent) next to a benchmark where one is verified and available (Mode 1, user-provided, or Mode 2, default register), next to the proposed target. Where no verified benchmark exists for a KPI (Mode 3), use the required wording from Mandatory Analytical Behaviour 7 rather than leaving a blank cell. Tag every row with its evidence level. Do not invent benchmark figures under any mode.
2. **2x2 impact vs effort chart**: plot every workflow from Stage 2 on an impact (y-axis) vs effort (x-axis) grid, four quadrants (quick wins, major projects, fill-ins, deprioritize). Build with `scripts/generate_2x2.py`, insert as an image. Follow Mandatory Analytical Behaviour 6.
3. **Commercial model**: four separate benefit categories per Mandatory Analytical Behaviour 3, each with three scenarios (conservative, base, optimistic) where benchmark-derived, or a single evidenced figure where not benchmark-based (spend recovery and tooling rationalisation are usually point estimates, not benchmark ranges). Run the cross-check per Mandatory Analytical Behaviour 4. See `references/commercial-model.md` for the calculation method.
4. **Risk flags**: carry forward anything marked low-confidence, "requires validation," or a governance gap from earlier stages into a short risk list. Where category 7 (Risk & Assumption Register) was provided, merge the client's own named risks in by their original ID rather than restating them as new findings.

### Stage 5 — Assemble

Build the Word document. Read `/mnt/skills/public/docx/SKILL.md` before writing any docx code, table widths, list formatting, and image insertion all have specific gotchas there. Widen ID columns enough that short codes (WF01, KPI01, T01) don't wrap onto two lines. Verify the rendered PDF before delivering, not just that the script ran without error.

Document sections, in order:
1. Executive Readout
2. Current State: Priority Workflow Opportunities
3. Current State: Operating Accountability (RACI)
4. KPI Model and Evidence Gaps
5. Technology Role Validation
6. Future State: Roadmap
7. Future State: RACI
8. Technology Recommendations
9. KPI Model and Benchmarks
10. Impact vs Effort (2x2 chart, embedded image)
11. Commercial Model (four benefit categories, cross-checked)
12. Risk Flags and Validation Needed
13. Data Foundation Readiness (only if category 6 was provided)
14. Recommended Next Steps

Every major table gets a short "Our recommendation" callout after it, in first-person-plural consultant voice, stating what leadership should do with the data, not just what the data says. Match the tone of `references/output-structure.md`: direct, leadership-brief register, no filler, every bullet ties to a decision.

### Mandatory pre-delivery visual QA

Do not mark a run production-ready without doing this, in order, every time:

1. Render the docx to PDF.
2. Visually inspect every page, not just a sample.
3. Check every table for wrapping, especially headers and ID columns.
4. Check the chart is legible, correct mode (inline or legend), no overlapping text.
5. Check page breaks land cleanly, no orphaned headers.
6. Check callout boxes render with correct shading and border.
7. Check every Section 1 decision has a matching Section 14 action, per Mandatory Analytical Behaviour 1a, against all seven gap types in Behaviour 5.
8. Check no commercial claim appears without its evidence tag.
9. Check no unverified benchmark (anything short of all ten Behaviour 7 client-facing conditions) appears in a document labelled for client use. Check the correct mode fired (user-provided, default, or graceful degradation) and that the required wording appears wherever Mode 3 applies.
10. Check no RACI row has an invented owner, and every gapped row is excluded from the future-state RACI per Mandatory Analytical Behaviour 2.
11. Check no revenue-growth case has been fabricated from a non-revenue KPI, per Mandatory Analytical Behaviour 3.

A run that fails any of these eleven checks is not production-ready. Fix it before delivering, don't note it as a known issue and ship anyway.

## Reference files

- `references/output-structure.md` — the exact section-by-section template, pulled from the approved reference example. Read this before assembling Stage 5.
- `references/default-benchmark-register.md` — the skill's own small register, Primary verified and Client-facing rows only. This is Mode 2. Nothing in it needs re-checking at run time, if it's here, it already cleared all ten conditions.
- `references/benchmark-sourcing-backlog.md` — candidate benchmarks, not yet verified. Internal-challenge use only, never client-facing, regardless of mode. This is where tracing work happens before a row graduates to the default register.
- `references/commercial-model.md` — the four-category savings methodology, the category-specific benchmark rules, and the mandatory cross-check.
- `RELEASE_NOTES.md` — version status, what's validated, release gate criteria, open escalation items. Read this before telling anyone this skill is ready for anything.

## Scripts

- `scripts/generate_2x2.py` — builds the impact vs effort chart as a PNG for embedding in the docx. Uses numbered markers and a legend when workflow count makes inline labels collide.

## Known gaps (tell the user, don't silently work around these)

Full detail in `RELEASE_NOTES.md`. Summary:

- Three test runs complete, build phase closed. No further mock-report iteration planned unless a regression is found.
- `references/default-benchmark-register.md` now has one Primary verified, Client-facing row (McKinsey, 5-15% marketing productivity uplift), traced and confirmed directly against mckinsey.com. This is the load-bearing figure for Commercial Model Category 1, so this one row already unlocks a real client-facing productivity claim, not just internal-challenge output.
- `references/benchmark-sourcing-backlog.md` holds 12 further candidates, all Secondary/internal or Draft/unverified. One flagged discrepancy worth knowing: the commonly repeated "87% of marketers use GenAI" Salesforce figure could not be confirmed on a Salesforce-owned page, the primary page found states 75% for a related but different metric. Do not use 87% anywhere until the full report PDF is checked.
- Supabase storage decision is the only open architecture item, whether this skill logs outputs to the existing FSOMA memory layer or stays standalone. Naming is resolved, not open.

## Required wording for Mode 3

Use this exactly, do not paraphrase it, when no verified benchmark is available for a claim:

"No verified benchmark was provided for this claim. The analysis therefore uses client-owned baseline data only and should be treated as directional until a verified benchmark is supplied."
