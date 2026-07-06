"""
EMBEDDING -- turn text into vectors so similar meanings sit close together.

The baseline uses a local sentence-transformers model. The documents don't
change, so they're embedded once and reused; at query time only the short query
is embedded.
"""

_MODELS = {}  # cache loaded models across calls


def embed_texts(texts, cfg, is_query=False):
    """Return an array of vectors for the given texts."""
    from sentence_transformers import SentenceTransformer
    model = _MODELS.get(cfg.embedding_model)
    if model is None:
        model = SentenceTransformer(cfg.embedding_model)
        _MODELS[cfg.embedding_model] = model
    return model.encode(texts, normalize_embeddings=True)
