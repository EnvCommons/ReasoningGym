"""One-off audit: does ReasoningGym's existing regex-only filter miss any
genuine post-2000 knowledge dependency an LLM motivation-rule check would
catch? Runs the two-stage pipeline (regex + deepseek-v4.1-flash verdict)
against a 30-per-dataset sample across all 103 successfully-instantiated
generators (matching the sample size used to build the original filter).
"""
import asyncio
import json
import os

import httpx

from cutoff1999_full import SYSTEM_PROMPT, TERMS_RE, YEAR_RE

URL = "https://infer.gr.inc/hi/v1/chat/completions"
MODEL = "deepseek-v4.1-flash"
CONCURRENCY = 15


async def classify(client, api_key, sem, uid, text):
    async with sem:
        for attempt in range(4):
            try:
                r = await client.post(
                    URL,
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": MODEL,
                        "messages": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": text},
                        ],
                        "max_tokens": 120,
                        "temperature": 0.0,
                    },
                    timeout=30.0,
                )
                r.raise_for_status()
                content = r.json()["choices"][0]["message"]["content"].strip()
                start, end = content.find("{"), content.rfind("}")
                parsed = json.loads(content[start:end + 1])
                return {"id": uid, "keep": bool(parsed.get("keep")),
                        "reason": str(parsed.get("reason", ""))[:200],
                        "disqualifying_terms": parsed.get("disqualifying_terms", []),
                        "question": text[:200]}
            except Exception as e:
                if attempt == 3:
                    return {"id": uid, "keep": None, "reason": f"error: {e}", "question": text[:200]}
                await asyncio.sleep(2 ** attempt)


async def main():
    api_key = os.environ["KIMI_API_KEY"]
    samples = json.load(open("samples.json"))
    all_rows = [(f"{name}_{i}", q) for name, qs in samples.items() for i, q in enumerate(qs)]
    print(f"auditing {len(all_rows)} sampled questions across {len(samples)} datasets", flush=True)

    regex_hits = [uid for uid, q in all_rows if YEAR_RE.search(q) or TERMS_RE.search(q)]
    print(f"regex-stage hits: {len(regex_hits)}", flush=True)

    sem = asyncio.Semaphore(CONCURRENCY)
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*(classify(client, api_key, sem, uid, q) for uid, q in all_rows))

    dropped = [r for r in results if r["keep"] is False]
    errors = [r for r in results if r["keep"] is None]
    print(f"LLM-stage drops: {len(dropped)} (out of {len(all_rows)}, {len(errors)} errors)", flush=True)
    for r in dropped:
        print(f"  DROP {r['id']}: {r['reason']} | terms={r.get('disqualifying_terms')} | {r['question']!r}")

    json.dump(results, open("audit_results.json", "w"), indent=2)
    print("wrote audit_results.json")


asyncio.run(main())
