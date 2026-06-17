import json

from enterprise_doc_ai_evaluation.dataset import load_cases, load_corpus
from enterprise_doc_ai_evaluation.evaluator import evaluate_case, evaluate_suite
from enterprise_doc_ai_evaluation.report import render_markdown_report


def test_synthetic_corpus_has_no_private_markers() -> None:
    corpus = load_corpus()
    text = json.dumps([doc.__dict__ for doc in corpus], ensure_ascii=False)
    forbidden = ["/home/", "/mnt/", "C:\\", "10.", "token", "password", "secret"]
    assert corpus
    assert not any(marker in text for marker in forbidden)


def test_single_case_scores_expected_citation_and_privacy() -> None:
    corpus = load_corpus()
    case = next(case for case in load_cases() if case.case_id == "ops-incident-routing")
    result = evaluate_case(case, corpus)
    assert result.passed is True
    assert result.expected_citation_found is True
    assert result.forbidden_disclosure_found is False
    assert result.score >= 0.8


def test_suite_report_tracks_capability_metrics() -> None:
    result = evaluate_suite(load_cases(), load_corpus())
    assert result.total_cases >= 4
    assert result.passed_cases >= 3
    assert result.metrics["citation_recall"] >= 0.75
    assert result.metrics["privacy_pass_rate"] == 1.0
    assert result.metrics["average_score"] >= 0.75


def test_markdown_report_is_public_safe_and_actionable() -> None:
    result = evaluate_suite(load_cases(), load_corpus())
    report = render_markdown_report(result)
    assert "# Enterprise Document AI Evaluation Report" in report
    assert "citation_recall" in report
    assert "privacy_pass_rate" in report
    assert "ops-incident-routing" in report
    forbidden = ["/home/", "/mnt/", "C:\\", "10.", "token", "password", "secret"]
    assert not any(marker in report.lower() for marker in forbidden)
