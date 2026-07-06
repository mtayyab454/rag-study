"""
Load the curated gold evaluation set (JSONL).

Provided working. Skips blank lines and comment lines so an auto-generated
"this is a DRAFT" header at the top of the file won't break parsing.

>>> Remember: the auto-generated gold set is a DRAFT. Curating it -- especially
    the unanswerable and paraphrased items -- is core Week 1 work, not a
    formality.
"""
import json


def load_gold_set(path):
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("//"):
                continue
            obj = json.loads(line)
            if "question" not in obj:
                # e.g. the leading _meta/DRAFT header line; not an eval item
                continue
            items.append(obj)
    return items
