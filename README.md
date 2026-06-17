# Enterprise Document AI Evaluation

A public-safe, synthetic evaluation harness for RAG/GraphRAG answer quality.

This demo shows how to evaluate enterprise document AI without publishing private documents:

- synthetic document corpus;
- realistic query cases;
- deterministic baseline answerer;
- citation/source recall checks;
- forbidden disclosure checks;
- aggregate quality report;
- pytest coverage and GitHub Actions CI.

Portfolio: https://tsamat.github.io/

## Why this matters

Enterprise AI quality cannot be managed with a few hand-picked prompts. A useful quality loop should test capabilities:

- Can the system route to the right document domain?
- Does it cite the expected evidence?
- Does it refuse or downgrade when evidence is weak?
- Does it avoid leaking private or forbidden values?
- Are regressions measurable after each change?

This repository demonstrates that loop with fully synthetic data.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
enterprise-doc-ai-eval --format markdown
enterprise-doc-ai-eval --format json
```

## Privacy note

All examples are synthetic. The repository intentionally contains no production documents, credentials, internal URLs, real names, or private paths.
