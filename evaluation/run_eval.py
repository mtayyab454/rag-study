"""
Evaluation harness -- runs ONE configuration over the gold set and writes the
model's answers to a CSV so you can eyeball them against the reference answers.

For each gold question it builds context, generates an answer, and writes a row:
question, answer, reference.
"""
import csv

from evaluation.gold_set import load_gold_set


def run_eval(pipeline, cfg):
    gold = load_gold_set(cfg.gold_set_path)
    if cfg.limit:
        gold = gold[:cfg.limit]

    rows = []
    for item in gold:
        result = pipeline.answer(item["question"])
        rows.append({
            "question": item["question"],
            "answer": result["answer"],
            "reference": item.get("reference_answer", ""),
        })

    _write_rows(cfg.results_path, rows)
    return rows


def _write_rows(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question", "answer", "reference"])
        writer.writeheader()
        writer.writerows(rows)
