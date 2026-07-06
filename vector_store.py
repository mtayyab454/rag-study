"""
VECTOR STORE + dense retrieval.

A transparent in-memory store (numpy cosine similarity) is ideal for a ~30-doc
corpus -- you can see exactly what's happening. FAISS / Chroma are upgrades to
try LATER, not requirements for this project.

>>> YOUR JOB: implement build() and search(). Commented baselines below.
"""


class VectorStore:
    def __init__(self):
        self.chunks = []     # list of chunk records (dicts)
        self.vectors = None  # matrix aligned row-for-row with self.chunks

    def build(self, chunk_records, vectors):
        """Store the chunks and their embedding matrix."""
        # # TODO: keep the chunk records and vectors so search() can use them.
        # raise NotImplementedError("Implement VectorStore.build -- see baseline")

        # -------------------- BASELINE --------------------
        import numpy as np
        self.chunks = chunk_records
        self.vectors = np.asarray(vectors, dtype="float32")
        # --------------------------------------------------

    def search(self, query_vector, top_k):
        """Return the top_k chunk records most similar to query_vector (with a score)."""
        # # TODO: compute similarity and return the top_k chunk records.
        # raise NotImplementedError("Implement VectorStore.search -- see baseline")

        # -------------------- BASELINE (cosine; vectors assumed normalized) ---
        import numpy as np
        q = np.asarray(query_vector, dtype="float32")
        sims = self.vectors @ q                      # dot == cosine if normalized
        idx = np.argsort(-sims)[:top_k]
        return [dict(self.chunks[i], score=float(sims[i])) for i in idx]
        # ---------------------------------------------------------------------
