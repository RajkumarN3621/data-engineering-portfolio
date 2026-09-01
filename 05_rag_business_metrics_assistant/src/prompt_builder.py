def build_grounded_prompt(question: str, contexts: list[dict]) -> str:
    context_text = "\n\n".join(
        f"[{item['source']}] {item['text']}" for item in contexts
    )

    return f"""Answer the question using only the supplied context.

Question:
{question}

Context:
{context_text}

If the context does not contain enough information, state that the information is not available.
"""
