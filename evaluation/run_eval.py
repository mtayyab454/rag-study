"""
Evaluation harness -- runs ONE configuration over the gold set and appends a row
to the results table. This is the fixed yardstick; every experiment goes through
it, so the results table lets you compare runs at a glance.

Provided working -- it orchestrates the functions you implement.
"""
import csv
import os
import statistics

from evaluation.gold_set import load_gold_set
from evaluation.retrieval_metrics import recall_at_k, mrr
from evaluation.judge import judge_answer, refusal_correct

_LOGGED_COLS = ("chunk_size", "chunk_overlap", "chunk_strategy", "embedding_model",
                "top_k", "use_hybrid", "use_reranker", "llm_model", "prompt_style")


def run_eval(pipeline, cfg):
    gold = load_gold_set(cfg.gold_set_path)
    recalls, rrs, faith, rel, refus = [], [], [], [], []

    for item in gold:
        result = pipeline.answer(item["question"])
        retrieved = result["retrieved"]
        context = "\n\n".join(c["text"] for c in retrieved)

        if item.get("query_type") == "unanswerable":
            refus.append(1.0 if refusal_correct(result["answer"], True) else 0.0)
            continue

        src = item.get("source_doc")
        if src:
            recalls.append(recall_at_k(retrieved, src, cfg.top_k))
            rrs.append(mrr(retrieved, src))

        scores = judge_answer(item["question"], context, result["answer"], cfg)
        faith.append(float(scores["faithfulness"]))
        rel.append(float(scores["relevance"]))

    row = {
        "run_name": cfg.run_name,
        "recall@k": _mean(recalls),
        "mrr": _mean(rrs),
        "faithfulness": _mean(faith),
        "relevance": _mean(rel),
        "refusal_acc": _mean(refus),
    }
    cfg_summary = cfg.summary()
    for col in _LOGGED_COLS:
        row[col] = cfg_summary.get(col)

    _append_row(cfg.results_path, row)
    return row


def _mean(xs):
    return round(statistics.mean(xs), 4) if xs else None


def _append_row(path, row):
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not exists:
            writer.writeheader()
        writer.writerow(row)
