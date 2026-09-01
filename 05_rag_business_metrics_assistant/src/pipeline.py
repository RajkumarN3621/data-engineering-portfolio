import sys
from pathlib import Path

from .document_loader import load_markdown_documents
from .text_processing import prepare_documents
from .embeddings import EmbeddingModel
from .vector_store import VectorStore
from .retriever import Retriever
from .prompt_builder import build_grounded_prompt


BASE = Path(__file__).parents[1]
DATA_DIR = BASE / "data" / "sample_metrics"


def build_retrieval_pipeline():
    documents = load_markdown_documents(DATA_DIR)
    chunks = prepare_documents(documents)

    embedding_model = EmbeddingModel()
    vectors = embedding_model.fit([item["text"] for item in chunks])

    vector_store = VectorStore()
    vector_store.build(vectors, chunks)

    return Retriever(embedding_model, vector_store)


def run(question: str):
    retriever = build_retrieval_pipeline()
    contexts = retriever.retrieve(question, top_k=3)

    prompt = build_grounded_prompt(question, contexts)

    print("Retrieved context:")
    for item in contexts:
        print(f"- {item['source']} | score={item['score']:.3f}")

    print("\nGrounded prompt:")
    print(prompt)


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]).strip()

    if not question:
        question = "What is the conversion rate formula?"

    run(question)
