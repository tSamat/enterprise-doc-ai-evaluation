# Enterprise Document AI Evaluation

[![CI](https://github.com/tSamat/enterprise-doc-ai-evaluation/actions/workflows/ci.yml/badge.svg)](https://github.com/tSamat/enterprise-doc-ai-evaluation/actions/workflows/ci.yml)

A public-safe, synthetic evaluation harness for RAG/GraphRAG answer quality.

Portfolio: https://tsamat.github.io/

## What it demonstrates

This demo shows how to evaluate enterprise document AI without publishing private documents:

- synthetic document corpus;
- realistic query cases;
- deterministic baseline answerer;
- citation/source recall checks;
- forbidden disclosure checks;
- aggregate quality report;
- Markdown and JSON output;
- pytest coverage and GitHub Actions CI.

## Why this matters

Enterprise AI quality cannot be managed with a few hand-picked prompts. A useful quality loop should test capabilities:

- Can the system route to the right document domain?
- Does it cite the expected evidence?
- Does it refuse or downgrade when evidence is weak?
- Does it avoid leaking private or forbidden values?
- Are regressions measurable after each change?

This repository demonstrates that loop with fully synthetic data.

## Stack

- Python 3.11+
- dataclass-based evaluation model
- deterministic baseline answerer
- pytest
- GitHub Actions
- synthetic fixtures only

## Architecture

```text
Synthetic corpus
  |
  v
Evaluation cases
  |
  +--> Deterministic baseline answerer
  |
  +--> Citation recall check
  |
  +--> Expected term coverage check
  |
  +--> Privacy disclosure check
  |
  v
Suite metrics + Markdown/JSON report
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
enterprise-doc-ai-eval --format markdown
enterprise-doc-ai-eval --format json
```

## Example report excerpt

```text
# Enterprise Document AI Evaluation Report

Total cases: 4
Passed cases: 4

## Metrics

- citation_recall: 1.0000
- privacy_pass_rate: 1.0000
- average_score: 1.0000
```

## Verification

```bash
pytest
enterprise-doc-ai-eval --format markdown
enterprise-doc-ai-eval --format json
python -m compileall -q src tests
```

The CI workflow runs the test suite and a JSON CLI smoke check on every push.

## Maturity note

This demo represents an evaluation pattern for RAG/GraphRAG systems. It uses synthetic fixtures and should not be read as a claim that all internal AI evaluation or GraphRAG initiatives are live services.

## Privacy boundary

All examples are synthetic. The repository intentionally contains no production documents, credentials, internal URLs, real names, private paths, runtime databases, or raw client data.

## Portfolio fit

This project demonstrates quality engineering for document-grounded AI: capability-based tests, measurable regression signals, and privacy-aware evaluation design.
