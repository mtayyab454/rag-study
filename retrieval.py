"""
RETRIEVAL -- find the most relevant chunks for a query. THE BIGGEST QUALITY
LEVER, usually. Spend real time here.

WEEK 4 EXPERIMENTS:
  - top_k sweep (more is NOT automatically better -- irrelevant chunks distract
    the LLM and hurt faithfulness; measure it)
  - hybrid: combine dense similarity with BM25 keyword scores
  - re-ranking: a cross-encoder re-scores the top candidates

Dense-only retrieval is the baseline. Hybrid and re-ranking are the experiments,
gated by cfg.use_hybrid and cfg.use_reranker.

>>> YOUR JOB: implement retrieve(). Start with the dense baseline below, then
    build up hybrid and reranking using the sketches.
"""


def retrieve(query, store, cfg, embed_fn):
    """Return the top chunks for a query, applying the configured strategy."""
    # # TODO (Week 4): start dense-only, then add hybrid and reranking.
    # raise NotImplementedError("Implement retrieve -- see commented baseline below")

    # -------------------- BASELINE: dense-only -------------------------------
    qvec = embed_fn([query], cfg, is_query=True)[0]
    return store.search(qvec, cfg.top_k)
    # -------------------------------------------------------------------------
    #
    # EXPERIMENT -- hybrid (dense + BM25). Sketch:
    #   from rank_bm25 import BM25Okapi
    #   # build the BM25 index ONCE (cache it on the store), not per query:
    #   corpus_tokens = [c["text"].lower().split() for c in store.chunks]
    #   bm25 = BM25Okapi(corpus_tokens)
    #   bm25_scores = bm25.get_scores(query.lower().split())
    #   # get dense scores too, min-max normalise BOTH to [0, 1], combine
    #   # (e.g. 0.5 * dense + 0.5 * bm25), sort, take cfg.top_k.
    #
    # EXPERIMENT -- re-ranking. Sketch:
    #   from sentence_transformers import CrossEncoder
    #   reranker = CrossEncoder(cfg.rerank_model)     # cache it, don't reload
    #   qvec = embed_fn([query], cfg, is_query=True)[0]
    #   candidates = store.search(qvec, cfg.top_k * 4)    # over-fetch, then rerank
    #   pairs = [(query, c["text"]) for c in candidates]
    #   scores = reranker.predict(pairs)
    #   ranked = [c for _, c in sorted(zip(scores, candidates),
    #                                  key=lambda x: -x[0])]
    #   return ranked[:cfg.top_k]
