# Default Verified Benchmark Register

This file ships with the skill. It contains only benchmark rows that pass every one of the ten client-facing conditions in SKILL.md's benchmark governance rule. Nothing here is a placeholder. Nothing here is a draft. If a row is in this file, it is usable in client-facing and marketplace-demo output today.

Do not add a row to this file unless you have personally checked it against the source, not a secondary site quoting it. See `benchmark-sourcing-backlog.md` for everything still being traced.

Schema: benchmark_id, benchmark_name, metric, value_or_range, unit, source_title, source_organisation, source_url, publication_date, industry_scope, functional_scope, geography_scope, allowed_use, evidence_status, notes.

---

## BM-DEFAULT-001

- benchmark_id: BM-DEFAULT-001
- benchmark_name: GenAI marketing function productivity uplift
- metric: Generative AI's potential uplift to marketing function productivity
- value_or_range: 5-15
- unit: percent of total marketing spending
- source_title: The economic potential of generative AI: The next productivity frontier
- source_organisation: McKinsey & Company (McKinsey Digital)
- source_url: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
- publication_date: 2023-06-14
- industry_scope: Cross-sector, global economy, 47 countries analysed
- functional_scope: Marketing function specifically, one of 16 business functions analysed across 63 use cases
- geography_scope: Global
- allowed_use: Client-facing
- evidence_status: Primary verified
- notes: Confirmed directly on mckinsey.com. Full quote basis: "We estimate that generative AI could increase the productivity of the marketing function with a value between 5 and 15 percent of total marketing spending." This is the load-bearing figure for Commercial Model Category 1 (AI productivity). Report also gives adjacent figures for customer operations (30-45%) and sales (3-5%), not marketing-specific, do not substitute those in for a marketing claim.

---

## Verification log

- 2 July 2026: BM-DEFAULT-001 traced and added. Source fetched directly, all ten client-facing conditions confirmed present.
- 2 July 2026: Salesforce "87% of marketers use generative AI in at least one workflow" checked and rejected for this register. Salesforce's own primary page for the Tenth Edition State of Marketing report (salesforce.com/news/stories/state-of-marketing-2026/, published 19 Feb 2026) states 75% AI adoption, not 87%. The 87% figure appears only on secondary aggregator sites citing "Salesforce State of Marketing 2026" without a traceable primary page stating it. Held in the backlog as Draft/unverified pending a direct check of the full downloadable report, not promoted here on the strength of repetition alone.
