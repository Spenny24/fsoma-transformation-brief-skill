# Commercial Model Methodology

Four scenarios, built from the client's own spend data first. Never invent a base spend figure, if it's not in the client data, the commercial model section states that spend validation is a precondition, same as the KPI section does for other baselines.

## The four benefit categories

Never blend these into one headline number. Each gets its own subsection.

### 1. AI productivity

May use a verified productivity benchmark if one is available for this metric, per SKILL.md's three-mode benchmark system: the user's own register first, then `references/default-benchmark-register.md`. Apply the benchmark-supported productivity range to base spend from client data (production spend, media spend, or both, depending on scope). Do not apply a benchmark figure to a workflow it wasn't measured against, content production workflows should use production-specific figures where available, general marketing figures only with that caveat stated.

If no verified benchmark is available for this metric under either mode, do not invent an uplift percentage. Use client-owned baseline data only, state that benchmark support is missing, and use the required Mode 3 wording from SKILL.md.

Where a verified benchmark exists, build three scenarios:
- **Conservative**: low end of the range, only the highest-automation-readiness workflows convert in year one.
- **Base**: midpoint of the range, applied across all medium-to-high readiness workflows.
- **Optimistic**: high end of the range, faster-than-typical adoption. Label explicitly as upper-bound, not the planning number.

### 2. Spend recovery

Point estimate, not a benchmark range. Sourced from the client's own finance data, typically an "untracked," "unreconciled," or "duplicate" spend line. This is a finance and governance exercise, not an AI outcome. Never use an AI productivity benchmark here, verified or not, it measures a different thing. State the baseline, the target, and the confidence level. Never let this get folded into the AI productivity number, even though both are denominated in the same currency.

### 3. Tooling rationalisation

Point estimate. Sourced from the tech stack data, specifically flagged duplicate or overlapping tools. Never use an AI productivity benchmark for licence rationalisation, it is a procurement question, not a productivity question. Cross-check top-down (any client-stated duplication estimate) against bottom-up (sum of the specifically flagged tools' run-rate cost). If bottom-up is meaningfully smaller than top-down, say so, it means the duplication estimate likely extends beyond the tools already flagged, and that scope needs confirming before the figure is governed. Do not average the two into a compromise figure, name the divergence and create a validation action.

### 4. Revenue growth

Only where the client's own data includes a revenue-linked KPI: conversion rate, basket size, sales uplift, media efficiency, retailer sell-through, retention, or revenue per campaign. Never infer revenue from productivity, content volume, SLA achievement, throughput, or cycle-time, those measure output or speed, not revenue. If no such KPI exists, state exactly: "No revenue growth case is presented." Do not soften this into a directional estimate.

## Mandatory cross-check

Before presenting any commercial figure, compare whichever of these four are available, and state the result, even when only one or two exist:

1. **Top-down**: benchmark percentage applied to total relevant spend.
2. **Client-stated**: any internal estimate already present in the client's own data (an "addressable savings opportunity" KPI, a "savings target anchor," and so on).
3. **Bottom-up / tooling**: sum of specifically identified items (named workflows, named duplicate tools, named spend lines).
4. **Benchmark-derived**: the raw public benchmark figure itself, before it's applied to this client's numbers.

Label the result as one of:
- **Converges**: two or more available numbers land close together.
- **Diverges**: two or more available numbers land meaningfully apart.
- **Not comparable**: two numbers exist but measure different things (for example, a percentage uplift versus a fixed duplication estimate with different scope).
- **Not evidenced**: fewer than two of the four rows have data at all.

Converging numbers are evidence worth citing to leadership directly. Diverging numbers are not something to smooth over, name the likely cause (broader scope than assumed, an unconfirmed assumption, a blended figure that needs separating) and create a validation action in the Risk Flags section and Recommended Next Steps. A divergence without a named validation action is an unfinished analysis.

## Payback in months

Payback = (implementation cost estimate) / (monthly savings, base scenario, AI productivity category only, since the other three categories are not typically implementation-cost-driven in the same way).

Implementation cost estimate should include: tooling/licensing, integration or build cost, and change management/training cost. If any of these three are unknown, state that payback is directionally indicative and needs a costed implementation plan to firm up, don't present a precise month count off an incomplete cost base. Current tool run-rate cost, where available, is operating cost, not implementation cost, don't substitute one for the other.

## Output format for the brief

For each of the four benefit categories: a short subsection stating baseline, target, evidence level, and (for AI productivity) the three-scenario table.

Cross-check result stated as its own short paragraph before the category subsections or immediately after, whichever reads more naturally given what data is available.

One closing sentence stating which category and which scenario is being recommended as the primary planning basis, and why, normally AI productivity, base case, since it is the only category with genuine benchmark support across a range.
