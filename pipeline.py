"""
PIPELINE -- wires the stages together.

Provided working: it calls the functions YOU implement in the stage modules.
Build the index once, then answer queries against it.
"""
from corpus_loader import load_documents
from chunking import chunk_corpus
from embeddings import embed_texts
from vector_store import VectorStore
from retrieval import retrieve
from generation import generate


class RagPipeline:
    def __init__(self, cfg):
        self.cfg = cfg
        self.store = VectorStore()

    def build(self):
        """Load -> chunk -> embed -> index. Call once before answering."""
        docs = load_documents(self.cfg.corpus_dir)
        chunks = chunk_corpus(docs, self.cfg)
        vectors = embed_texts([c["text"] for c in chunks], self.cfg, is_query=False)
        self.store.build(chunks, vectors)
        return self

    def answer(self, query):
        """Retrieve context and generate a grounded answer."""
        chunks = retrieve(query, self.store, self.cfg, embed_texts)
        answer = generate(query, chunks, self.cfg)
        return {"query": query, "answer": answer, "retrieved": chunks}
