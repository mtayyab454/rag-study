"""
CHUNKING -- split documents into retrievable pieces.

WEEK 2 EXPERIMENTS: vary chunk_size, chunk_overlap, and chunk_strategy (in
config.py) and measure the effect on retrieval recall and answer faithfulness.
There is no universal "right" size -- you are finding it for THIS corpus.

>>> YOUR JOB: implement chunk_text(). The commented BASELINE below is one
    working fixed-size chunker -- uncomment it to see a reference, then write
    your own and experiment.
"""


def chunk_text(text, chunk_size, overlap, strategy):
    """Return a list of string chunks for one document's text."""
    # # TODO (Week 2): implement chunking. Match the baseline first, then
    # # experiment with size, overlap, and the "recursive" / "structure" strategies.
    # raise NotImplementedError("Implement chunk_text -- see commented baseline below")

    # -------------------- BASELINE REFERENCE (fixed-size, word-based) --------
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
    # -------------------------------------------------------------------------
    #
    # IDEAS TO EXPERIMENT WITH:
    #   - token-based sizing with tiktoken instead of str.split() (words != tokens)
    #   - "recursive": split on paragraph/sentence boundaries, then pack to
    #     roughly chunk_size so you don't cut mid-sentence
    #   - "structure": split on markdown headings (##, ###) so each chunk
    #     respects a document section -- often strong on structured docs


def chunk_corpus(docs, cfg):
    """
    Chunk every document; return chunk records with provenance.

    Provided working -- it calls YOUR chunk_text(). Each record keeps doc_id so
    the retrieval metrics can check whether the correct source doc was retrieved.
    """
    records = []
    for doc in docs:
        pieces = chunk_text(doc["text"], cfg.chunk_size, cfg.chunk_overlap, cfg.chunk_strategy)
        for i, piece in enumerate(pieces):
            records.append({
                "chunk_id": f'{doc["id"]}::{i}',
                "doc_id": doc["id"],
                "title": doc["title"],
                "category": doc["category"],
                "text": piece,
            })
    return records
