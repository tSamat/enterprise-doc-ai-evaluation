from __future__ import annotations

import argparse

from .dataset import load_cases, load_corpus
from .evaluator import evaluate_suite
from .report import render_json_report, render_markdown_report


def main() -> None:
    """CLI-точка входа для локального smoke и GitHub Actions."""

    parser = argparse.ArgumentParser(
        description="Run a synthetic enterprise document AI evaluation suite."
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format for the synthetic evaluation report.",
    )
    args = parser.parse_args()
    result = evaluate_suite(load_cases(), load_corpus())
    if args.format == "json":
        print(render_json_report(result))
    else:
        print(render_markdown_report(result))


if __name__ == "__main__":
    main()
