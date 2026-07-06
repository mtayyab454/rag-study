# RAG Pipeline Study — Summer Project Spec

*A 6-week mentored project. You'll build a retrieval-augmented-generation (RAG) chatbot for a gym/fitness app, then run a controlled study of the design decisions inside it and write up what you found. The deliverable is not "a working chatbot" — plenty of tutorials give you that. The deliverable is **evidence**: a report that shows which design choices mattered, by how much, and why, measured against a fixed yardstick.*

---

## Read this first: the one principle that makes or breaks the project

A RAG system has a dozen knobs. It is trivial to change one, look at three answers, decide it "seems better," and move on. That teaches you nothing and is worthless in a portfolio.

The entire project rests on a single discipline:

> **Build one evaluation harness. Change one knob at a time. Re-run the harness. Log the number. Keep the winner.**

Every experiment below is a controlled comparison against the same fixed test set. If you internalise nothing else, internalise this — it's the difference between "I followed a RAG tutorial" and "I ran an ablation study on a RAG pipeline," and only one of those is worth talking about in an interview.

---

## Architecture: the pipeline as an experiment surface

Data flows top-to-bottom. Each stage is a set of knobs you will experiment on. The evaluation harness on the side is the fixed instrument that measures the pipeline's output at two points — what was retrieved, and what was generated.

```
CORPUS  (app docs + fitness Q&A — generated from the real codebase)
   |
   v
CHUNKING       knobs:  chunk size · overlap · splitting strategy
   |
   v
EMBEDDING      knobs:  model · dimensions · query/passage prefixes
   |
   v
RETRIEVAL      knobs:  top-k · hybrid (dense + keyword) · re-ranking
   |
   v
PROMPT + LLM   knobs:  prompt template · grounding · refusal behaviour
   |
   v
ANSWER  (grounded, cited response)


   +--------------------------------------------------+
   |  EVALUATION HARNESS  — the fixed yardstick       |
   |  taps RETRIEVAL output and GENERATION output     |
   |                                                  |
   |  gold Q&A set  ·  recall@k / MRR (retrieval)     |
   |                ·  faithfulness + relevance       |
   |                   via LLM-as-judge (generation)  |
   +--------------------------------------------------+
```

The harness is built **first**, in week 1, before any experimentation. Nothing you do afterwards means anything without it.

---

## The pipeline stages, and what to experiment with at each

For each stage: what it does, the knobs to vary, the gotcha that eats people's time, and what "better" looks like.

### 1. Corpus
The knowledge base — app documentation (grounded in the real codebase) plus general fitness content. You're not experimenting *on* the corpus; it's the fixed ground truth. But understand its shape: it deliberately mixes document lengths and formats, covers some topics in more than one place, and includes questions the corpus can't answer. That variety is what lets the downstream experiments show a signal.

### 2. Chunking
Splits documents into retrievable pieces.
- **Knobs:** chunk size (e.g. 128 / 256 / 512 tokens), overlap (0% / 10% / 20%), and strategy (fixed-size vs. recursive/character vs. structure-aware splitting on headings).
- **Gotcha:** chunks too small lose context; too big dilute the relevant signal and waste the LLM's context window. There is no universal "right" size — that's the point, you're finding it *for this corpus*.
- **Better looks like:** higher retrieval recall and higher answer faithfulness without bloating context.

### 3. Embedding
Turns text into vectors so similar meanings sit close together.
- **Knobs:** model (e.g. `all-MiniLM-L6-v2` vs. a `bge`/`e5`/`gte` model), embedding dimensions, and normalisation.
- **Gotcha (this one wastes days):** `e5` and `bge` models expect **prefixes** — `"query: ..."` on the question and `"passage: ..."` on the documents. Forget them and retrieval silently degrades and looks like a model problem. Always check the model card.
- **Better looks like:** improved retrieval metrics. Note honestly if the fancy model barely moves the needle — that's a real and common finding.

### 4. Retrieval
Finds the most relevant chunks for a query. **Usually the biggest quality lever — spend real time here.**
- **Knobs:** top-k (how many chunks to pull), hybrid search (dense vectors + keyword/BM25), and a cross-encoder **re-ranker** over the top candidates.
- **Gotcha:** more chunks (higher k) is not automatically better — irrelevant chunks distract the LLM and hurt faithfulness. Measure, don't assume.
- **Better looks like:** the right chunk lands in the top results more often (recall@k, MRR), especially on paraphrased and near-duplicate-topic questions.

### 5. Prompt + LLM (generation)
Assembles the retrieved context into a prompt and generates the answer.
- **Knobs:** prompt template, how context is injected, grounding instructions, citation of sources, and — the interesting one — **refusal behaviour**.
- **The key design tension:** the bot should answer general fitness questions freely, but for app-specific questions it must answer *only* from the retrieved docs, and **refuse or hedge when nothing relevant was retrieved** rather than hallucinate a feature. This behaviour is measurable (see the harness) and makes a strong report section.
- **Better looks like:** high faithfulness (answers grounded in context, not invented) and correct refusals on unanswerable questions.

---

## The evaluation harness (build this in week 1)

This is the backbone. It has three parts.

**1. The gold set.** ~50 questions (a draft is auto-generated with the corpus; you must *curate* it — curating it is itself core learning). Each item: the question, a reference answer, a `query_type` (`app` / `fitness` / `unanswerable`), the source document/section, and a difficulty. The mix deliberately includes multi-hop questions (answer spans two docs), paraphrased questions (so keyword matching alone won't find the chunk), and unanswerable questions (so refusal is testable).

**2. Retrieval metrics.** Because you logged the "correct" source chunk for each answerable question, you can measure retrieval directly:
- **Recall@k / hit-rate** — was the right chunk in the top k?
- **MRR** — how high up was it ranked?
These are cheap, deterministic, and fast — run them on every experiment.

**3. Generation metrics via LLM-as-judge.** For the final answer quality:
- **Faithfulness** — is the answer supported by the retrieved context, or invented?
- **Answer relevance** — does it actually address the question?
- **Refusal accuracy** — on `unanswerable` questions, did it correctly decline?

Use a capable **free** model (via OpenRouter) as the judge, with a clear scoring rubric that returns a score *and* a one-line rationale. **Validate the judge:** hand-label ~10–15 items yourself and confirm the judge agrees with you before trusting it at scale. (This judge-validation step is a genuinely marketable skill — treat it as a first-class part of the work, not a formality.)

Keep a single results table: one row per experiment run, columns for every metric, so deltas are visible at a glance.

---

## Week-by-week plan

Each week has a focus, concrete tasks, a deliverable, and a mentor checkpoint. Draft the matching report section *in the same week* as the experiment — do not leave writing for the end.

### Week 1 — Foundations *(the most important week; resist rushing it)*
- **Focus:** a baseline RAG end-to-end, plus the evaluation harness.
- **Tasks:** load the generated corpus; build a naive baseline (fixed 512-token chunks, one embedding model, top-k = 3, a plain prompt); curate the gold eval set from the auto-generated draft; implement retrieval metrics; implement and validate the LLM-as-judge.
- **Deliverable:** baseline numbers in the results table. This is your control — every later experiment is measured as a delta from here.
- **Checkpoint:** review the gold set together (especially the unanswerable and paraphrased items) and sanity-check the baseline numbers.

### Week 2 — Chunking
- **Focus:** chunk size, overlap, splitting strategy.
- **Tasks:** vary one dimension at a time, holding everything else at baseline; re-run the harness for each; log results.
- **Deliverable:** a chunking results table + the chosen configuration, with reasoning. Draft the chunking report section.
- **Checkpoint:** discuss *why* the winner won, not just which won.

### Week 3 — Embedding
- **Focus:** embedding model comparison.
- **Tasks:** compare 2–3 models (mind the query/passage prefixes!); note cost/speed/size, not just quality; re-run the harness.
- **Deliverable:** embedding results table + choice + reasoning. Draft the embedding report section.
- **Checkpoint:** was the delta big or small? Interpret honestly.

### Week 4 — Retrieval *(the big one)*
- **Focus:** top-k, hybrid search, re-ranking.
- **Tasks:** sweep top-k; add keyword/BM25 alongside dense; add a cross-encoder re-ranker over top candidates; measure each addition separately.
- **Deliverable:** retrieval results table + chosen retrieval stack. Draft the retrieval report section.
- **Checkpoint:** which single change moved retrieval most? Did it match your prediction?

### Week 5 — Generation, then combine
- **Focus:** prompt design, grounding, refusal — then assemble the winning config.
- **Tasks:** iterate on the prompt template; implement and measure refusal on unanswerable questions; then combine the winning choices from weeks 2–4 and re-measure **end-to-end**.
- **Deliverable:** generation results + the final combined configuration's numbers. Draft the generation section.
- **Checkpoint:** did the individual wins *compound* when stacked, or did some cancel out? (Both outcomes are interesting — report whichever happened.)

### Week 6 — Synthesis
- **Focus:** finish the report and present.
- **Tasks:** finalise the report, write the limitations and reflection, assemble the final results table, prepare a short walkthrough presentation.
- **Deliverable:** the complete report + a 10-minute presentation of the study.
- **Checkpoint:** present the whole thing as if to a hiring panel — low-stakes practice for the real thing.

---

## The report: structure and checklists

The report is a single document structured as a methodology section, one section per experiment, and a synthesis. Below is the target structure, then a checklist for each section. Tick every box before calling a section done.

### Report structure
1. Introduction & problem (what the bot does, why RAG)
2. Corpus & evaluation methodology
3. Baseline
4. Experiment: Chunking
5. Experiment: Embedding
6. Experiment: Retrieval
7. Experiment: Generation & refusal
8. Final configuration & end-to-end results
9. Limitations & what you'd do next
10. Conclusion

### Checklist — Methodology section
- [ ] Corpus described (size, document types, how it was generated/grounded)
- [ ] Gold set described: size, the three query types, how items were curated
- [ ] Every metric defined in plain language (recall@k, MRR, faithfulness, relevance, refusal accuracy)
- [ ] LLM-as-judge setup described, **including how the judge was validated against human labels**
- [ ] Enough detail that someone could reproduce the setup

### Checklist — each Experiment section (chunking / embedding / retrieval / generation)
- [ ] The question this experiment answers, stated in one sentence
- [ ] Exactly which knob was varied, and what was held constant
- [ ] A results table with numbers for every variant (not prose hand-waving)
- [ ] The chosen setting, stated explicitly
- [ ] **Interpretation:** *why* the winner won — the mechanism, not just the number
- [ ] At least one honest surprise, null result, or thing that didn't work
- [ ] A concrete example (a query where the change visibly helped or hurt)

### Checklist — Final configuration section
- [ ] The full winning pipeline listed end-to-end
- [ ] End-to-end numbers vs. the week-1 baseline (the headline result)
- [ ] A clear statement of whether the stacked wins compounded or interfered

### Checklist — Limitations & Conclusion
- [ ] Honest limitations (small corpus, single domain, judge imperfections, etc.)
- [ ] What you'd try with more time
- [ ] No overclaiming — conclusions are supported by the numbers shown

### Checklist — Overall report quality
- [ ] Every claim is backed by a number in a table or a cited example
- [ ] One consolidated results table lets a reader see all experiments at once
- [ ] Figures/tables are labelled and readable on their own
- [ ] A newcomer to RAG could follow it start to finish
- [ ] Code is in a clean, documented repo linked from the report

---

## Working practices (small habits, big payoff)

- **Lab notebook.** Keep a dated running log: what you tried, what happened, what's next. This one habit builds more research discipline than anything else, and it makes the report almost write itself.
- **One results table.** Everything funnels into it. If a run isn't in the table, it didn't happen.
- **Git from day one.** Commit often. The repo is part of the deliverable.
- **Twice-weekly async update** to your mentor: what I did, what I'm stuck on, what's next. Writing it clearly is half the skill.
- **Expect a stuck week.** Around the middle it will feel like nothing works. That's normal, not failure. Say so early and we'll unstick it together.

---

## Definition of done

- [ ] A working RAG pipeline over the gym-app corpus
- [ ] An evaluation harness with a curated gold set and validated judge
- [ ] Ablation results for chunking, embedding, retrieval, and generation
- [ ] A final tuned configuration measured end-to-end against the baseline
- [ ] A complete report meeting the checklists above
- [ ] A clean, documented GitHub repo
- [ ] A 10-minute presentation of the study
