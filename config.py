"""
Central configuration -- the knobs for the pipeline.

Change values here (or override on the command line), then re-run.
"""
from dataclasses import dataclass, asdict


@dataclass
class Config:
    # --- corpus ---
    corpus_dir: str = "corpus"

    # --- chunking ---
    chunk_size: int = 512      # try 128 / 256 / 512
    chunk_overlap: int = 0     # try 0, then ~10% and ~20% of chunk_size

    # --- embedding ---
    embedding_model: str = "all-MiniLM-L6-v2"

    # --- retrieval ---
    top_k: int = 3             # try 1 / 3 / 5 / 10

    # --- generation ---
    # Free model ids on OpenRouter carry a ":free" suffix and change over time --
    # check https://openrouter.ai/models and paste a current one here.
    llm_model: str = "tencent/hy3:free"
    temperature: float = 0.0

    # --- eval ---
    gold_set_path: str = "corpus/eval/gold_set.jsonl"
    limit: int = 0             # 0 = all gold items; set e.g. 5 for quick tests
    results_path: str = "results.csv"
    run_name: str = "baseline"

    def summary(self):
        return dict(asdict(self))
