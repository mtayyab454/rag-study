"""
Entry point: build the pipeline for the current config and answer the gold set.

    python run_experiment.py
    python run_experiment.py --chunk-size 256 --chunk-overlap 32
    python run_experiment.py --top-k 10

Change knobs via flags or by editing config.py. Answers are written to results.csv
(question, answer, reference).
"""
import argparse

from dotenv import load_dotenv

load_dotenv()  # read OPENROUTER_API_KEY (and friends) from .env into os.environ

from config import Config
from pipeline import RagPipeline
from evaluation.run_eval import run_eval


def parse_args():
    p = argparse.ArgumentParser(description="Run one RAG configuration over the gold set.")
    p.add_argument("--run-name")
    p.add_argument("--chunk-size", type=int)
    p.add_argument("--chunk-overlap", type=int)
    p.add_argument("--embedding-model")
    p.add_argument("--top-k", type=int)
    p.add_argument("--limit", type=int, help="only evaluate the first N gold items (0 = all)")
    return p.parse_args()


def apply_overrides(cfg, args):
    if args.run_name:                  cfg.run_name = args.run_name
    if args.chunk_size is not None:    cfg.chunk_size = args.chunk_size
    if args.chunk_overlap is not None: cfg.chunk_overlap = args.chunk_overlap
    if args.embedding_model:           cfg.embedding_model = args.embedding_model
    if args.top_k is not None:         cfg.top_k = args.top_k
    if args.limit is not None:         cfg.limit = args.limit
    return cfg


def main():
    args = parse_args()
    cfg = apply_overrides(Config(), args)

    print(f"Running '{cfg.run_name}' ...")
    pipeline = RagPipeline(cfg).build()
    rows = run_eval(pipeline, cfg)

    print(f"Answered {len(rows)} questions. Wrote {cfg.results_path}")


if __name__ == "__main__":
    main()
