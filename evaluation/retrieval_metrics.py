"""
Retrieval metrics -- cheap, deterministic, run on EVERY experiment.

Matching is at the DOCUMENT level: did we retrieve a chunk from the gold item's
source_doc within the top k? (Section-level matching is a nice later extension.)

>>> YOUR JOB (Week 1): implement recall_at_k() and mrr(). These are quick and
    genuinely worth writing yourself -- baselines are below if you get stuck.
"""


def recall_at_k(retrieved_chunks, gold_source_doc, k):
    """Return 1.0 if any of the top-k chunks come from gold_source_doc, else 0.0."""
    # TODO (Week 1): implement. See baseline.
    raise NotImplementedError("Implement recall_at_k -- see baseline")

    # -------------------- BASELINE --------------------
    # top = retrieved_chunks[:k]
    # return 1.0 if any(c["doc_id"] == gold_source_doc for c in top) else 0.0
    # --------------------------------------------------


def mrr(retrieved_chunks, gold_source_doc):
    """Return the reciprocal rank of the first chunk from gold_source_doc (0 if none)."""
    # TODO (Week 1): implement. See baseline.
    raise NotImplementedError("Implement mrr -- see baseline")

    # -------------------- BASELINE --------------------
    # for rank, c in enumerate(retrieved_chunks, start=1):
    #     if c["doc_id"] == gold_source_doc:
    #         return 1.0 / rank
    # return 0.0
    # --------------------------------------------------
