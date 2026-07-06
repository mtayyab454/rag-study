"""
GENERATION -- assemble the retrieved context into a prompt and call the LLM.

The baseline builds a grounded prompt from the retrieved chunks and asks the
model to answer from that context.
"""
import os

from openai import OpenAI


def build_prompt(query, chunks, cfg):
    """Return the chat messages for the LLM given the query and retrieved chunks."""
    context = "\n\n".join(f"[{i + 1}] {c['text']}" for i, c in enumerate(chunks))
    system = (
        "You are a helpful assistant for a gym/fitness app. Use the CONTEXT to "
        "answer. For questions about the app, rely ONLY on the context; if the "
        "context does not contain the answer, say you don't have that information "
        "rather than guessing. For general fitness questions you may use common "
        "knowledge. Cite context passages like [1] when you use them."
    )
    user = f"CONTEXT:\n{context}\n\nQUESTION: {query}"
    return [{"role": "system", "content": system},
            {"role": "user", "content": user}]


def generate(query, chunks, cfg):
    """Return the model's answer string."""
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.environ["OPENROUTER_API_KEY"])
    messages = build_prompt(query, chunks, cfg)
    resp = client.chat.completions.create(
        model=cfg.llm_model, messages=messages, temperature=cfg.temperature)
    return resp.choices[0].message.content
