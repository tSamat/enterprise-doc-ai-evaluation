from __future__ import annotations

from statistics import mean

from .baseline import answer_case
from .models import CaseResult, Document, EvalCase, SuiteResult


def evaluate_case(case: EvalCase, corpus: list[Document]) -> CaseResult:
    """Оценивает один сценарий по цитированию, покрытию терминов и privacy-запретам."""

    answer = answer_case(case, corpus)
    answer_lower = answer.text.lower()
    expected_citation_found = case.expected_doc_id in answer.citations
    missing_terms = tuple(term for term in case.expected_terms if term.lower() not in answer_lower)
    forbidden_disclosure_found = any(term.lower() in answer_lower for term in case.forbidden_terms)

    term_score = 1.0 - (len(missing_terms) / max(len(case.expected_terms), 1))
    citation_score = 1.0 if expected_citation_found else 0.0
    privacy_score = 0.0 if forbidden_disclosure_found else 1.0
    score = round((0.45 * term_score) + (0.35 * citation_score) + (0.20 * privacy_score), 4)
    passed = score >= 0.75 and expected_citation_found and not forbidden_disclosure_found

    return CaseResult(
        case_id=case.case_id,
        passed=passed,
        score=score,
        expected_citation_found=expected_citation_found,
        forbidden_disclosure_found=forbidden_disclosure_found,
        missing_terms=missing_terms,
        citations=answer.citations,
    )


def evaluate_suite(cases: list[EvalCase], corpus: list[Document]) -> SuiteResult:
    """Считает агрегированные capability-метрики для набора synthetic cases."""

    results = tuple(evaluate_case(case, corpus) for case in cases)
    total = len(results)
    passed = sum(1 for result in results if result.passed)
    scores = [result.score for result in results]
    metrics = {
        "pass_rate": _safe_ratio(passed, total),
        "citation_recall": _safe_ratio(sum(1 for result in results if result.expected_citation_found), total),
        "privacy_pass_rate": _safe_ratio(sum(1 for result in results if not result.forbidden_disclosure_found), total),
        "average_score": round(mean(scores), 4) if scores else 0.0,
    }
    return SuiteResult(total_cases=total, passed_cases=passed, metrics=metrics, case_results=results)


def _safe_ratio(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0
