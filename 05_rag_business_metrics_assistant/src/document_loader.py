from pathlib import Path


def load_markdown_documents(directory: str | Path) -> list[dict]:
    directory = Path(directory)
    documents = []

    for path in sorted(directory.glob("*.md")):
        documents.append(
            {
                "source": path.name,
                "text": path.read_text(encoding="utf-8"),
            }
        )

    return documents
