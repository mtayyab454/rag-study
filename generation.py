"""
GENERATION -- assemble the retrieved context into a prompt and call the LLM.

WEEK 5 EXPERIMENTS: prompt template, grounding instructions, and refusal.
The key design tension:
  - answer GENERAL FITNESS questions freely (common knowledge is fine), but
  - for APP questions answer ONLY from the retrieved context, and REFUSE / hedge
    when nothing relevant was retrieved -- do NOT invent a feature.
This refusal behaviour is measurable (see evaluation/judge.py) and makes a
strong report section.

>>> YOUR JOB: implement build_prompt() and generate(). Commented baselines below.
"""


def build_prompt(query, chunks, cfg):
    """Return the chat messages for the LLM given the query and retrieved chunks."""
    # TODO (Week 5): design the prompt. Experiment with grounding + refusal wording,
    # and with how you format / number the context.
    raise NotImplementedError("Implement build_prompt -- see commented baseline below")

    # -------------------- BASELINE PROMPT ------------------------------------
    # context = "\n\n".join(f"[{i + 1}] {c['text']}" for i, c in enumerate(chunks))
    # system = (
    #     "You are a helpful assistant for a gym/fitness app. Use the CONTEXT to "
    #     "answer. For questions about the app, rely ONLY on the context; if the "
    #     "context does not contain the answer, say you don't have that information "
    #     "rather than guessing. For general fitness questions you may use common "
    #     "knowledge. Cite context passages like [1] when you use them."
    # )
    # user = f"CONTEXT:\n{context}\n\nQUESTION: {query}"
    # return [{"role": "system", "content": system},
    #         {"role": "user", "content": user}]
    # -------------------------------------------------------------------------


def generate(query, chunks, cfg):
    """Return the model's answer string."""
    # # TODO (Week 5): call the LLM with your prompt and return the answer text.
    # raise NotImplementedError("Implement generate -- see commented baseline below")

    # -------------------- BASELINE: OpenRouter (OpenAI-compatible) ------------
    from openai import OpenAI
    import os
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.environ["OPENROUTER_API_KEY"])
    messages = build_prompt(query, chunks, cfg)
    resp = client.chat.completions.create(
        model=cfg.llm_model, messages=messages, temperature=cfg.temperature)
    return resp.choices[0].message.content
    # -------------------------------------------------------------------------
