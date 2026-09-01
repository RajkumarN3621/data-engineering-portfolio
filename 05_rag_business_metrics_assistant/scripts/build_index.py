from pathlib import Path

from src.document_loader import load_markdown_documents
from src.text_processing import prepare_documents
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


BASE = Path(__file__).parents[1]
DATA_DIR = BASE / "data" / "sample_metrics"
INDEX_DIR = BASE / "index"
INDEX_DIR.mkdir(exist_ok=True)

documents = load_markdown_documents(DATA_DIR)
chunks = prepare_documents(documents)

model = EmbeddingModel()
vectors = model.fit([item["text"] for item in chunks])

store = VectorStore()
store.build(vectors, chunks)
store.save(INDEX_DIR / "vector_store.pkl")

print(f"Indexed {len(documents)} documents into {len(chunks)} chunks.")
print(f"Index written to: {INDEX_DIR / 'vector_store.pkl'}")
