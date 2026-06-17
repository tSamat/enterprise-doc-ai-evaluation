from __future__ import annotations

from .models import Answer, Document, EvalCase


def answer_case(case: EvalCase, corpus: list[Document]) -> Answer:
    """Простая baseline-модель: выбирает документ домена и формирует цитируемый ответ.

    В production здесь был бы RAG/GraphRAG pipeline. Для публичного demo важна
    проверяемая структура оценки, поэтому baseline детерминированный.
    """

    candidates = [doc for doc in corpus if doc.domain == case.domain]
    if not candidates:
        return Answer(text="Insufficient synthetic evidence to answer safely.", citations=())
    doc = candidates[0]
    return Answer(text=doc.text, citations=(doc.doc_id,))
