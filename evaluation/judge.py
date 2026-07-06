"""
LLM-as-judge for generation quality: faithfulness, relevance, and refusal.

Use a capable FREE model (OpenRouter) as the judge, with a clear rubric that
returns a score AND a short rationale.

>>> VALIDATE THE JUDGE before trusting it: hand-label ~10-15 items yourself and
    confirm the judge agrees with you. This judge-validation step is a genuinely
    marketable skill -- treat it as first-class work, not a formality. Write a
    small script that prints judge score vs. your label for those items.

>>> YOUR JOB (Week 1): implement judge_answer() and refusal_correct().
    Baselines below.
"""
import json

JUDGE_RUBRIC = """You are grading a RAG answer. Given the QUESTION, the retrieved
CONTEXT, and the ANSWER, score each dimension 1-5 and reply with STRICT JSON only,
no prose and no code fences:
{"faithfulness": <1-5>, "relevance": <1-5>, "rationale": "<one short sentence>"}
- faithfulness: is the ANSWER supported by the CONTEXT (not invented)?
- relevance: does the ANSWER actually address the QUESTION?"""


def judge_answer(question, context, answer, cfg):
    """Return a dict: {"faithfulness": int, "relevance": int, "rationale": str}."""
    # TODO (Week 1): call the judge model and parse its JSON response.
    raise NotImplementedError("Implement judge_answer -- see commented baseline below")

    # -------------------- BASELINE (OpenRouter, OpenAI-compatible) ------------
    # from openai import OpenAI
    # import os
    # client = OpenAI(base_url="https://openrouter.ai/api/v1",
    #                 api_key=os.environ["OPENROUTER_API_KEY"])
    # user = f"QUESTION:\n{question}\n\nCONTEXT:\n{context}\n\nANSWER:\n{answer}"
    # resp = client.chat.completions.create(
    #     model=cfg.judge_model, temperature=0.0,
    #     messages=[{"role": "system", "content": JUDGE_RUBRIC},
    #               {"role": "user", "content": user}])
    # raw = resp.choices[0].message.content.strip()
    # raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    # return json.loads(raw)
    # -------------------------------------------------------------------------


def refusal_correct(answer, should_refuse):
    """
    For 'unanswerable' gold items: did the answer correctly refuse?

    A keyword heuristic is a fine STARTING point. Improving this (e.g. asking the
    judge model 'did this answer refuse? yes/no') is itself a small experiment.
    """
    # TODO (Week 1): implement a refusal check. See baseline.
    raise NotImplementedError("Implement refusal_correct -- see baseline")

    # -------------------- BASELINE (simple heuristic) --------------------
    # markers = ("don't have", "do not have", "not covered", "no information",
    #            "cannot find", "couldn't find", "not in the", "unable to")
    # refused = any(m in answer.lower() for m in markers)
    # return refused == should_refuse
    # --------------------------------------------------------------------
