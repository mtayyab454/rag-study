# RAG Pipeline Study — code scaffold

A skeleton for the 6-week RAG study. Each pipeline stage is a `TODO` for you to
implement, with a **working baseline commented out right below it** — uncomment
the baseline any time you want to see one reference implementation, then write
and experiment with your own.

## The one rule

Build the eval harness first. Change **one knob at a time**. Re-run the harness.
Log the number. Keep the winner. Every experiment is a controlled comparison
against the same gold set — that's what makes this a study and not a tutorial.

## Which files are yours to implement

These have `TODO` stubs (and commented baselines). This is the actual work:

| File | Stage | Week |
|------|-------|------|
| `chunking.py` | chunk_text() | 2 |
| `embeddings.py` | embed_texts() | 3 |
| `vector_store.py` | build(), search() | 1 / 4 |
| `retrieval.py` | retrieve() (dense → hybrid → rerank) | 1 / 4 |
| `generation.py` | build_prompt(), generate() | 5 |
| `evaluation/retrieval_metrics.py` | recall_at_k(), mrr() | 1 |
| `evaluation/judge.py` | judge_answer(), refusal_correct() | 1 |

**Provided working** (you shouldn't need to touch the plumbing): `config.py`,
`corpus_loader.py`, `pipeline.py`, `evaluation/gold_set.py`,
`evaluation/run_eval.py`, `run_experiment.py`.

## Setup

Use **either** a Python venv **or** a conda environment — you don't need both.

**Option A — Python venv:**

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # then paste your OpenRouter key into .env
```

**Option B — conda:**

```bash
conda create -n rag-study python=3.11 -y
conda activate rag-study
pip install -r requirements.txt
cp .env.example .env        # then paste your OpenRouter key into .env
```

Generate the corpus (see the project spec) so `corpus/app/*.md`,
`corpus/fitness/*.md`, `corpus/manifest.json`, and `corpus/eval/gold_set.jsonl`
exist. Then curate the draft gold set — that's Week 1 work.

## Run

```bash
python run_experiment.py --run-name baseline
python run_experiment.py --run-name chunk256_ov32 --chunk-size 256 --chunk-overlap 32
python run_experiment.py --run-name topk10 --top-k 10
python run_experiment.py --run-name hybrid_rerank --use-hybrid --use-reranker
```

Each run appends a row to `results.csv` — that's your single source of truth for
the report.

## Want a working end-to-end run immediately?

Uncomment the `BASELINE` blocks in `chunking.py`, `embeddings.py`,
`vector_store.py`, `retrieval.py`, `generation.py`,
`evaluation/retrieval_metrics.py`, and `evaluation/judge.py`. That gives you a
naive-but-working pipeline you can run and measure — a useful reference before
you replace each piece with your own and start experimenting.

## Config = the knobs

`config.py` holds every knob (chunk size, embedding model, top-k, hybrid,
reranker, prompt style, models). Override on the command line or edit the file.

## Free vs. paid, and the embedding gotcha

- **LLM + judge:** free models on OpenRouter use a `:free` suffix and change over
  time — check <https://openrouter.ai/models> and update `config.py`.
- **Embeddings:** OpenRouter embeddings are cheap but *not* free. For a strictly
  $0 cloud embedding, use Google's Gemini embedding free tier (add a small branch
  in `embed_texts()` and a `GEMINI_API_KEY`). For local dev, `sentence-transformers`
  is free and offline.
- **Prefix gotcha:** e5 / bge embedding models need `"query: "` / `"passage: "`
  prefixes (set them in `config.py`). Forgetting them silently wrecks retrieval.

## Suggested order of work

1. Week 1 — baseline + eval harness (metrics, judge, gold-set curation)
2. Week 2 — chunking · 3 — embedding · 4 — retrieval (the big lever)
3. Week 5 — generation + refusal, then combine the winners and re-measure
4. Week 6 — write up

Keep a dated lab notebook and commit often. The repo is part of the deliverable.
