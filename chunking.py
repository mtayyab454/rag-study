"""
CHUNKING -- split documents into retrievable pieces.

The baseline is a fixed-size, word-based chunker. Vary chunk_size / chunk_overlap
in config.py to see the effect on retrieval.
"""


def chunk_text(text, chunk_size, overlap):
    """Return a list of string chunks for one document's text."""
    words = text.split()
    if chunk_size <= 0:
        return [text]
    step = max(1, chunk_size - overlap)
    chunks = []
    for start in range(0, len(words), step):
        window = words[start:start + chunk_size]
        if not window:
            break
        chunks.append(" ".join(window))
        if start + chunk_size >= len(words):
            break
    return chunks


def chunk_corpus(docs, cfg):
    """Chunk every document; return chunk records that keep doc_id for provenance."""
    records = []
    for doc in docs:
        pieces = chunk_text(doc["text"], cfg.chunk_size, cfg.chunk_overlap)
        for i, piece in enumerate(pieces):
            records.append({
                "chunk_id": f'{doc["id"]}::{i}',
                "doc_id": doc["id"],
                "title": doc["title"],
                "category": doc["category"],
                "text": piece,
            })
    return records
