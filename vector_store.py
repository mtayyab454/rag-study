"""
VECTOR STORE + dense retrieval.

A transparent in-memory store (numpy cosine similarity) is ideal for a small
corpus -- you can see exactly what's happening.
"""
import numpy as np


class VectorStore:
    def __init__(self):
        self.chunks = []     # list of chunk records (dicts)
        self.vectors = None  # matrix aligned row-for-row with self.chunks

    def build(self, chunk_records, vectors):
        """Store the chunks and their embedding matrix."""
        self.chunks = chunk_records
        self.vectors = np.asarray(vectors, dtype="float32")

    def search(self, query_vector, top_k):
        """Return the top_k chunk records most similar to query_vector (with a score)."""
        q = np.asarray(query_vector, dtype="float32")
        sims = self.vectors @ q                      # dot == cosine when normalized
        idx = np.argsort(-sims)[:top_k]
        return [dict(self.chunks[i], score=float(sims[i])) for i in idx]
