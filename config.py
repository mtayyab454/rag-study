"""
Central configuration -- the knobs for every experiment.

Change values here (or override on the command line) to run a new experiment,
then re-run the evaluation harness and log the numbers. Keep ONE knob changing
at a time so you can attribute any metric change to that knob.
"""
from dataclasses import dataclass, asdict


@dataclass
class Config:
    # --- corpus ---
    corpus_dir: str = "corpus"

    # --- chunking (Week 2 experiments) ---
    chunk_size: int = 512            # try 128 / 256 / 512
    chunk_overlap: int = 0           # try 0, then ~10% and ~20% of chunk_size
    chunk_strategy: str = "fixed"    # "fixed" | "recursive" | "structure"

    # --- embedding (Week 3 experiments) ---
    embedding_backend: str = "local"           # "local" | "cloud"
    embedding_model: str = "all-MiniLM-L6-v2"  # try a bge / e5 / gte model too
    query_prefix: str = ""    # e.g. "query: " for e5/bge models    <-- GOTCHA
    passage_prefix: str = ""  # e.g. "passage: " for e5/bge models  <-- GOTCHA

    # --- retrieval (Week 4 experiments) ---
    top_k: int = 3               # try 1 / 3 / 5 / 10
    use_hybrid: bool = False     # combine dense similarity with BM25 keyword
    use_reranker: bool = False   # cross-encoder re-scores the top candidates
    rerank_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    # --- generation (Week 5 experiments) ---
    # Free model ids on OpenRouter carry a ":free" suffix and change over time --
    # check https://openrouter.ai/models and paste a current one here.
    llm_model: str = "meta-llama/llama-3.3-70b-instruct:free"
    temperature: float = 0.0
    prompt_style: str = "baseline"   # name each prompt variant you try

    # --- eval ---
    gold_set_path: str = "corpus/eval/gold_set.jsonl"
    judge_model: str = "meta-llama/llama-3.3-70b-instruct:free"  # verify current id
    results_path: str = "results.csv"
    run_name: str = "baseline"

    def summary(self):
        return dict(asdict(self))
