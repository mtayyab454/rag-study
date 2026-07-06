"""
Entry point: build the pipeline for the current config and run the eval harness.

    python run_experiment.py --run-name baseline
    python run_experiment.py --run-name chunk256_ov32 --chunk-size 256 --chunk-overlap 32
    python run_experiment.py --run-name hybrid_rerank --use-hybrid --use-reranker

Change knobs via flags or by editing config.py. ONE knob at a time -- that's the
whole discipline. Each run appends a row to results.csv.

Provided working. It will raise NotImplementedError until you've implemented (or
uncommented the baselines in) the stage modules.
"""
import argparse

from dotenv import load_dotenv

load_dotenv()  # read OPENROUTER_API_KEY (and friends) from .env into os.environ

from config import Config
from pipeline import RagPipeline
from evaluation.run_eval import run_eval


def parse_args():
    p = argparse.ArgumentParser(description="Run one RAG experiment configuration.")
    p.add_argument("--run-name")
    p.add_argument("--chunk-size", type=int)
    p.add_argument("--chunk-overlap", type=int)
    p.add_argument("--chunk-strategy")
    p.add_argument("--embedding-model")
    p.add_argument("--top-k", type=int)
    p.add_argument("--use-hybrid", action="store_true")
    p.add_argument("--use-reranker", action="store_true")
    p.add_argument("--prompt-style")
    return p.parse_args()


def apply_overrides(cfg, args):
    if args.run_name:               cfg.run_name = args.run_name
    if args.chunk_size is not None: cfg.chunk_size = args.chunk_size
    if args.chunk_overlap is not None: cfg.chunk_overlap = args.chunk_overlap
    if args.chunk_strategy:         cfg.chunk_strategy = args.chunk_strategy
    if args.embedding_model:        cfg.embedding_model = args.embedding_model
    if args.top_k is not None:      cfg.top_k = args.top_k
    if args.use_hybrid:             cfg.use_hybrid = True
    if args.use_reranker:           cfg.use_reranker = True
    if args.prompt_style:           cfg.prompt_style = args.prompt_style
    return cfg


def main():
    args = parse_args()
    cfg = apply_overrides(Config(), args)

    print(f"Running '{cfg.run_name}' ...")
    pipeline = RagPipeline(cfg).build()
    row = run_eval(pipeline, cfg)

    print("Results:")
    for k, v in row.items():
        print(f"  {k}: {v}")
    print(f"Appended to {cfg.results_path}")


if __name__ == "__main__":
    main()
