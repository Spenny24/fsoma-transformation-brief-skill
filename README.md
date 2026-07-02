# FSOMA Transformation Brief Kit

FSOMA stands for Future-State Operating Model Assessment.

A Claude skill that turns a client's "as-is" operating model data, current workflows, tech stack, RACI, KPIs, spend, into a leadership-ready transformation business case. Output is a single Word document covering current state assessment, future state roadmap, future RACI, technology recommendations, a KPI model with benchmark overlay, a 2x2 impact vs effort chart, and a four-category commercial model.

Release status: v0.9, Public Preview. Public on GitHub. Not yet approved for Claude marketplace listing. See `RELEASE_NOTES.md` for the full gate criteria and what is and isn't done.

This is not client-ready ROI automation. Every commercial figure this skill produces depends on either a verified benchmark, your own or the small default register bundled here, or falls back to your own baseline data with the gap stated plainly. Read `SKILL.md`'s benchmark governance section before you trust any number it gives you.

## What this does

Feed it client discovery data, in any format, complete or partial, and it produces a structured leadership brief with:

1. Executive Readout with named leadership decisions, not just findings.
2. Current state workflow, RACI, KPI, and technology assessment, every row tagged by evidence confidence.
3. Future state roadmap, sequenced by evidence and AI readiness, not executive visibility.
4. Future state RACI, AI never assigned as Accountable, governance gaps flagged rather than papered over.
5. Technology recommendations, keep, replace, consolidate, or validate, with reasoning.
6. A commercial model split into four categories, AI productivity, spend recovery, tooling rationalisation, and revenue growth, never blended into one number.
7. A 2x2 impact vs effort chart, collision-safe by design.
8. Risk flags and recommended next steps, every material gap converted into a named decision or action.

## Benchmark handling

This skill is not dependent on any particular benchmark library. It works three ways, checked in order:

1. Your own benchmark register, if you provide one. Preferred over the default register for any metric both cover.
2. A small default verified register bundled with the skill. Only rows that are fully source-traced and Primary verified live here.
3. No verified benchmark available. The skill does not invent one and does not block. It uses your own baseline data, states the gap plainly, and flags it as a decision to make or a validation to run.

Full schema and rules are in `SKILL.md` and `references/default-benchmark-register.md`.

## Install

This is a Claude skill. Drop the `fsoma-transformation-brief-skill` folder into your skills directory, or package it with Anthropic's skill-creator tooling into a `.skill` file and install it through your Claude environment's skill manager.

## Folder structure

```
fsoma-transformation-brief-skill/
  SKILL.md                                  Main skill definition and pipeline
  README.md                                 This file
  RELEASE_NOTES.md                          Version status and release gate
  references/
    output-structure.md                     Section-by-section document template
    default-benchmark-register.md           Verified benchmarks, client-facing ready
    benchmark-sourcing-backlog.md           Candidate benchmarks, internal only
    commercial-model.md                     Four-category savings methodology
  scripts/
    generate_2x2.py                         Impact vs effort chart generator
  examples/
    NexaGlow_FSOMA_Transformation_Brief_FINAL.docx   Fictional test-brand sample output
    impact_effort_nexaglow_final.png                 Sample chart output
```

## Example

The bundled example uses NexaGlow Beauty, a fictional test brand built specifically for validating this skill. No real client, no real company. The document itself states this on its cover page. Do not treat any figure in it as a real benchmark or a real client result.

## What's not done yet

See `RELEASE_NOTES.md` for the full list. Short version: the default benchmark register is intentionally small, one verified row today, and grows only when a figure is traced to its actual primary source, not copied from a secondary site repeating it. Client-facing use is real but partial. Claude marketplace listing copy and a full sanitised example pass are still open.

## License

License pending. No open-source license has been granted yet. This repository is public on GitHub for preview and reference. Do not redistribute, resell, or reuse the code or methodology without written permission from Craig Spence. A formal license will be added before this moves past Public Preview.
