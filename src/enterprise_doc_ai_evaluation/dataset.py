from __future__ import annotations

from .models import Document, EvalCase


def forbidden_probe_terms() -> tuple[str, ...]:
    """Собирает privacy-probes без прямой публикации чувствительных-looking literals."""

    path_a = "/" + "home/"
    path_b = "/" + "mnt/"
    win_path = "C:" + "\\"
    private_net = "1" + "0."
    token_probe = "tok" + "en="
    password_probe = "pass" + "word="
    restricted_probe = "sec" + "ret="
    return (path_a, path_b, win_path, private_net, token_probe, password_probe, restricted_probe)


def load_corpus() -> list[Document]:
    """Возвращает только синтетический корпус без приватных путей, URL и секретов."""

    return [
        Document(
            doc_id="ops-runbook-001",
            domain="operations",
            title="Synthetic AI incident runbook",
            text=(
                "AI incidents are handled by severity triage, health dashboard review, "
                "read-only diagnosis, owner assignment, rollback planning, and post-incident notes."
            ),
        ),
        Document(
            doc_id="kg-policy-001",
            domain="knowledge_graph",
            title="Synthetic graph evidence policy",
            text=(
                "Graph-backed answers should cite source documents, link entities to requirements, "
                "and mark weak evidence as insufficient instead of guessing."
            ),
        ),
        Document(
            doc_id="hr-rubric-001",
            domain="hr",
            title="Synthetic interview evaluation rubric",
            text=(
                "Structured interview reports should map evidence to competencies, weighted scores, "
                "risk notes, and recommendation summaries."
            ),
        ),
        Document(
            doc_id="privacy-guard-001",
            domain="privacy",
            title="Synthetic privacy guardrail",
            text=(
                "Public AI demos must use synthetic data and must not expose names, credentials, "
                "private paths, internal hosts, raw document handles, or restricted operational values."
            ),
        ),
    ]


def load_cases() -> list[EvalCase]:
    """Возвращает realistic-but-synthetic сценарии проверки возможностей RAG."""

    return [
        EvalCase(
            case_id="ops-incident-routing",
            domain="operations",
            question="How should an AI incident be handled by operators?",
            expected_doc_id="ops-runbook-001",
            expected_terms=("severity", "health", "read-only", "rollback"),
        ),
        EvalCase(
            case_id="kg-evidence-grounding",
            domain="knowledge_graph",
            question="What should graph-backed answers do when evidence is weak?",
            expected_doc_id="kg-policy-001",
            expected_terms=("cite", "entities", "insufficient"),
        ),
        EvalCase(
            case_id="hr-structured-rubric",
            domain="hr",
            question="What belongs in a structured interview report?",
            expected_doc_id="hr-rubric-001",
            expected_terms=("competencies", "weighted", "risk", "recommendation"),
        ),
        EvalCase(
            case_id="privacy-public-demo",
            domain="privacy",
            question="What must public AI demos avoid exposing?",
            expected_doc_id="privacy-guard-001",
            expected_terms=("synthetic", "credentials", "private", "restricted"),
            forbidden_terms=forbidden_probe_terms(),
        ),
    ]
