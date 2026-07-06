"""
Load the generated corpus (markdown docs + manifest).

Provided working -- you don't need to reimplement file IO. It returns one record
per document with its text and metadata.
"""
import json
import os
import glob


def load_manifest(corpus_dir):
    path = os.path.join(corpus_dir, "manifest.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_documents(corpus_dir):
    """
    Return a list of dicts: {id, title, category, path, text}.
    Reads every .md under the corpus directory (app + fitness).
    """
    manifest = []
    try:
        manifest = load_manifest(corpus_dir)
    except FileNotFoundError:
        pass

    # index manifest entries by a few possible path spellings for robustness
    by_key = {}
    for m in manifest:
        p = m.get("path", "")
        by_key[p] = m
        by_key[os.path.basename(p)] = m

    docs = []
    for md_path in glob.glob(os.path.join(corpus_dir, "**", "*.md"), recursive=True):
        rel = os.path.relpath(md_path, corpus_dir)
        with open(md_path, encoding="utf-8") as f:
            text = f.read()
        meta = by_key.get(rel) or by_key.get(md_path) or by_key.get(os.path.basename(md_path)) or {}
        docs.append({
            "id": meta.get("id", rel),
            "title": meta.get("title", os.path.basename(md_path)),
            "category": meta.get("category", "unknown"),
            "path": rel,
            "text": text,
        })
    if not docs:
        raise FileNotFoundError(
            f"No .md documents found under '{corpus_dir}'. "
            "Generate the corpus first (see the project spec)."
        )
    return docs
