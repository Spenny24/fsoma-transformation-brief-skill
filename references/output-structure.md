# Output Structure Reference — NexaGlow Standard

This is the locked client-output structure for the FSOMA Transformation Report Kit.

Use the supplied client or n8n source data as the evidence base. Use this file as the final report structure, tone and sequencing reference. Do not output a QA memo, two-part review, Apex-style report, generic markdown report, or a different section order unless the user explicitly asks for a different format.

## Title page

The title page must use this pattern:

```text
[Client Name]
AI Operating Model Report
Future-State Operating Model Assessment
Prepared for: [Client leadership group]
Sector: [Sector]
Source audit reference: [Audit ID]
Report date: [Date]
[Environment / synthetic / draft status, if relevant]
```

Never put "Appendix" in the title unless the page is actually an appendix.

## Contents

The contents list must match the section order below exactly:

1. Executive Readout
2. Current State: Priority Workflow Opportunities
3. Current State: Operating Accountability (RACI)
4. KPI Model and Evidence Gaps
5. Technology Role Validation
6. Future State: Roadmap
7. Future State: RACI
8. Technology Recommendations
9. KPI Model and Benchmarks
10. Impact vs Effort
11. Commercial Model
12. Risk Flags and Validation Needed
13. Data Foundation Readiness
14. Recommended Next Steps

Appendices may follow Section 14 only.

## Section 1 — Executive Readout

Open with 4-6 leadership takeaways, not a data dump.

Cover:

- Where the opportunity concentrates.
- Which workflows or clusters should enter the first pilot.
- What RACI or governance constraints exist.
- What baseline data is missing or low-confidence.
- Whether the commercial model is evidenced, directional, divergent or not evidenced.
- Any revenue-growth limitation if no revenue-linked KPI exists.

Then add **Leadership Decisions Needed**. Each item must be a named decision. Every item must have a matching action in Section 14.

## Section 2 — Current State: Priority Workflow Opportunities

State how many workflows were identified and the repeated automation pattern.

Use a decision-ready table:

| Workflow | Impact area | Automation pattern | Benefit | Evidence tag |
|---|---|---|---|---|

Keep benefits outcome-led, not tool-led.

Add an **Our recommendation** callout after the table.

## Section 3 — Current State: Operating Accountability (RACI)

State how many activities the RACI extract covers and whether each has a named Responsible and Accountable owner.

AI must never be Accountable.

Use:

| Activity | Responsible | Accountable | Evidence tag |
|---|---|---|---|

If a row lacks a responsible or accountable owner, do not infer one. Flag it as a governance gap, add a leadership decision in Section 1, exclude it from the future-state RACI, and close it with a Section 14 action.

Add an **Our recommendation** callout.

## Section 4 — KPI Model and Evidence Gaps

State how many KPIs exist and how many have missing or low-confidence baselines.

Use:

| KPI | Baseline | Target | Evidence tag |
|---|---|---|---|

Where a baseline is absent, use "Baseline requires validation" or "Not evidenced". Do not fabricate a number.

Add any required leadership KPIs that should exist even where source evidence is incomplete.

Add an **Our recommendation** callout.

## Section 5 — Technology Role Validation

Frame this as a dependency map for operating-model design, not a confirmed stack recommendation.

Use:

| Tool | Current role | Evidence tag |
|---|---|---|

Add an **Our recommendation** callout.

## Section 6 — Future State: Roadmap

Use 3-4 phases where supported by the source evidence.

Use:

| Phase | Focus | Dependencies | Evidence tag |
|---|---|---|---|

Do not approve later scale phases unless pilot evidence exists. Phrase them as conditional when needed.

Add an **Our recommendation** callout.

## Section 7 — Future State: RACI

Use the same governed activities as the current-state RACI unless a current-state row had a governance gap.

Use:

| Activity | Responsible | Accountable | AI role | Evidence tag |
|---|---|---|---|---|

AI can support preparation, routing, evidence capture, summarisation and reporting. AI must never be Accountable.

Add an **Our recommendation** callout.

## Section 8 — Technology Recommendations

For each tool, mark keep / replace / consolidate / validate.

Use:

| Tool | Recommendation | Rationale | Evidence tag |
|---|---|---|---|

Add an **Our recommendation** callout.

## Section 9 — KPI Model and Benchmarks

Show client baseline, benchmark where verified, source, and evidence tag.

Use:

| KPI | Client baseline | Industry benchmark | Source | Evidence tag |
|---|---|---|---|---|

Where no verified benchmark exists, state that directly and use the required Mode 3 wording from SKILL.md where applicable.

Add an **Our recommendation** callout.

## Section 10 — Impact vs Effort

Embed the 2x2 chart when numeric or source-supported impact/effort data exists.

If numeric coordinates are not supplied and plotting would require invention, present the source quadrant grouping instead and state why a chart was not plotted.

Use chart-safe numbered markers and a legend whenever item count, label collision or label length requires it.

Add an **Our recommendation** callout.

## Section 11 — Commercial Model

Never carry forward a blended savings headline as the commercial case.

Separate the model into four categories:

1. AI productivity
2. Spend recovery
3. Tooling rationalisation
4. Revenue growth

Each category must include its evidence basis and cross-check result.

Commercial model cross-check rows:

- Top-down: benchmark percentage applied to relevant spend.
- Client-stated: any internal estimate in the source data.
- Bottom-up / tooling: named workflow, duplicate tool or spend-line sum.
- Benchmark-derived: raw benchmark figure before client application.

Label the relationship as converges, diverges, not comparable, or not evidenced.

If no revenue-linked KPI exists, state exactly:

```text
No revenue growth case is presented.
```

Add an **Our recommendation** callout.

## Section 12 — Risk Flags and Validation Needed

Use source risks where available, preserving their IDs. Add review risks separately.

Use:

| ID | Risk | Why it matters | Mitigation | Owner | Evidence tag |
|---|---|---|---|---|---|

Any commercial divergence, missing benchmark, RACI gap, data-foundation gap or unmitigated risk must also close in Section 14.

## Section 13 — Data Foundation Readiness

This section must always appear.

If no formal Data Inventory was supplied, use this exact opening:

```text
No formal data inventory was supplied with this source report. The readiness signal below is drawn from evidence gaps surfaced during this review, not a structured completeness audit.
```

Use:

| Data area | Signal | Evidence tag |
|---|---|---|

Add an **Our recommendation** callout.

## Section 14 — Recommended Next Steps

Every Section 1 leadership decision and every material Section 11 commercial gap must have a matching action here.

Use concrete action wording:

- action
- owner or accountable function
- timing where source-supported
- which decision or gap it closes

Do not use this section for general commentary.

## Appendices

Appendices start only after Section 14.

Label clearly:

- Appendix A: [Title]
- Appendix B: [Title]

Long tables, full technology inventories, full workbook extracts and context-only source financial models belong in appendices.

Do not insert appendix continuation text before the appendix section begins.

## Word output polish rules

- Numbered lists must render as real Word numbering.
- If reliable numbering cannot be guaranteed, use bullets instead.
- Table headers must be styled consistently.
- Tables must have clear header rows, readable spacing and sensible column widths.
- Long tables must go into appendices.
- No orphaned page labels.
- No appendix text before appendices begin.
