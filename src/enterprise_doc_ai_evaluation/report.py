from __future__ import annotations

import json
from dataclasses import asdict

from .models import SuiteResult


def render_json_report(result: SuiteResult) -> str:
    """Возвращает machine-readable JSON без приватных runtime-данных."""

    return json.dumps(asdict(result), indent=2, sort_keys=True)


def render_markdown_report(result: SuiteResult) -> str:
    """Возвращает компактный публичный Markdown-отчёт для README/портфолио."""

    lines = [
        "# Enterprise Document AI Evaluation Report",
        "",
        f"Total cases: {result.total_cases}",
        f"Passed cases: {result.passed_cases}",
        "",
        "## Metrics",
        "",
    ]
    for name, value in result.metrics.items():
        lines.append(f"- `{name}`: {value:.4f}")
    lines.extend(["", "## Cases", ""])
    for case in result.case_results:
        status = "PASS" if case.passed else "FAIL"
        missing = ", ".join(case.missing_terms) if case.missing_terms else "none"
        citations = ", ".join(case.citations) if case.citations else "none"
        lines.append(
            f"- `{case.case_id}` — {status}; score={case.score:.4f}; "
            f"citations={citations}; missing_terms={missing}"
        )
    lines.append("")
    lines.append("Privacy note: this report is generated from synthetic fixtures only.")
    return "\n".join(lines)
