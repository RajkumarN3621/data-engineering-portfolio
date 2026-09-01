from .embeddings import EmbeddingModel
from .vector_store import VectorStore


class Retriever:
    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, question: str, top_k: int = 3):
        query_vector = self.embedding_model.transform([question])
        return self.vector_store.search(query_vector, top_k=top_k)
