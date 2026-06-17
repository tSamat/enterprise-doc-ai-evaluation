from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    """Безопасный синтетический документ для оценки retrieval/answer quality."""

    doc_id: str
    domain: str
    title: str
    text: str


@dataclass(frozen=True)
class EvalCase:
    """Один проверочный сценарий: вопрос, ожидаемая ссылка и privacy-запреты."""

    case_id: str
    domain: str
    question: str
    expected_doc_id: str
    expected_terms: tuple[str, ...]
    forbidden_terms: tuple[str, ...] = ()


@dataclass(frozen=True)
class Answer:
    """Детерминированный ответ baseline-модели с цитатами."""

    text: str
    citations: tuple[str, ...]


@dataclass(frozen=True)
class CaseResult:
    """Результат оценки одного сценария."""

    case_id: str
    passed: bool
    score: float
    expected_citation_found: bool
    forbidden_disclosure_found: bool
    missing_terms: tuple[str, ...]
    citations: tuple[str, ...]


@dataclass(frozen=True)
class SuiteResult:
    """Агрегированный результат набора evaluation cases."""

    total_cases: int
    passed_cases: int
    metrics: dict[str, float]
    case_results: tuple[CaseResult, ...]
