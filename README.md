# RAG Pipeline Study — minimal baseline

A small, end-to-end RAG pipeline over a fitness/app corpus. It's deliberately
minimal: load → chunk → embed → index → retrieve → generate, then answer every
question in the gold set and write the answers to a CSV.

## The pipeline

| File | Stage |
|------|-------|
| `corpus_loader.py` | load markdown docs + manifest |
| `chunking.py` | split docs into fixed-size chunks |
| `embeddings.py` | local sentence-transformers embeddings |
| `vector_store.py` | in-memory numpy cosine-similarity store |
| `retrieval.py` | dense top-k retrieval |
| `generation.py` | build a grounded prompt + call the LLM |
| `evaluation/run_eval.py` | answer the gold set, write `results.csv` |
| `pipeline.py` | wires the stages together |
| `run_experiment.py` | entry point |

## Setup

Use **either** a Python venv **or** a conda environment.

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

The corpus (`corpus/app/*.md`, `corpus/fitness/*.md`, `corpus/manifest.json`,
`corpus/eval/gold_set.jsonl`) is already in the repo.

## Run

```bash
python run_experiment.py
python run_experiment.py --chunk-size 256 --chunk-overlap 32
python run_experiment.py --top-k 10
```

Each run writes `results.csv` with three columns: **question**, **answer** (the
model's answer), and **reference** (the gold reference answer) so you can eyeball
them side by side.

## Config = the knobs

`config.py` holds the knobs: chunk size/overlap, embedding model, top-k, LLM
model. Override on the command line or edit the file.

## Notes

- **LLM:** free models on OpenRouter use a `:free` suffix and change over time —
  check <https://openrouter.ai/models> and update `config.py`.
- **Embeddings:** `sentence-transformers` runs locally and offline, no API key.
