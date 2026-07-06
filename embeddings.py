"""
EMBEDDING -- turn text into vectors so similar meanings sit close together.

WEEK 3 EXPERIMENTS: compare embedding models. Use a LOCAL model
(sentence-transformers) for development; a CLOUD model (OpenRouter, or Google's
free Gemini embedding tier) for the deploy-style setup.

>>> GOTCHA (this one wastes days): e5 / bge models expect prefixes --
    "query: " on the question and "passage: " on the documents. Set them in
    config.py (query_prefix / passage_prefix). Forget them and retrieval
    silently degrades and looks like a model problem. Always read the model card.

>>> OPTIMISATION: the documents don't change, so embed them ONCE and reuse the
    vectors. At query time you only embed the short query.

>>> YOUR JOB: implement embed_texts(). Two commented baselines below -- local
    first, then cloud.
"""

_MODELS = {}  # cache loaded local models across calls


def embed_texts(texts, cfg, is_query=False):
    """Return a list/array of vectors for the given texts."""
    # # TODO (Week 3): implement the local backend first, then add the cloud
    # # backend. Remember to apply the query/passage prefix.
    # raise NotImplementedError("Implement embed_texts -- see commented baselines below")

    # -------------------- BASELINE: local (sentence-transformers) ------------
    from sentence_transformers import SentenceTransformer
    model = _MODELS.get(cfg.embedding_model)
    if model is None:
        model = SentenceTransformer(cfg.embedding_model)
        _MODELS[cfg.embedding_model] = model
    prefix = cfg.query_prefix if is_query else cfg.passage_prefix
    prefixed = [f"{prefix}{t}" for t in texts]
    return model.encode(prefixed, normalize_embeddings=True)
    # -------------------------------------------------------------------------

    # -------------------- BASELINE: cloud (OpenRouter, OpenAI-compatible) -----
    # NOTE: OpenRouter embeddings are cheap but NOT free. A strictly-$0 option is
    # Google's Gemini embedding tier -- see the README for that variant.
    # from openai import OpenAI
    # import os
    # client = OpenAI(base_url="https://openrouter.ai/api/v1",
    #                 api_key=os.environ["OPENROUTER_API_KEY"])
    # prefix = cfg.query_prefix if is_query else cfg.passage_prefix
    # resp = client.embeddings.create(
    #     model=cfg.embedding_model,
    #     input=[f"{prefix}{t}" for t in texts],
    # )
    # return [d.embedding for d in resp.data]
    # -------------------------------------------------------------------------
