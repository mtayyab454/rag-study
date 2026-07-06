"""
RETRIEVAL -- find the most relevant chunks for a query.

The baseline is dense-only retrieval: embed the query, then return the top_k most
similar chunks from the vector store.
"""


def retrieve(query, store, cfg, embed_fn):
    """Return the top_k chunks for a query."""
    qvec = embed_fn([query], cfg, is_query=True)[0]
    return store.search(qvec, cfg.top_k)
