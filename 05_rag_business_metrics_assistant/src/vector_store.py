import pickle
from pathlib import Path

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:
    """Small local vector store used to demonstrate retrieval mechanics."""

    def __init__(self):
        self.vectors = None
        self.documents = []

    def build(self, vectors, documents):
        self.vectors = vectors
        self.documents = documents

    def search(self, query_vector, top_k=3):
        if self.vectors is None:
            raise RuntimeError("Vector store has not been built")

        scores = cosine_similarity(query_vector, self.vectors)[0]
        indices = np.argsort(scores)[::-1][:top_k]

        return [
            {
                **self.documents[index],
                "score": float(scores[index]),
            }
            for index in indices
        ]

    def save(self, path: str | Path):
        with open(path, "wb") as file:
            pickle.dump(
                {
                    "vectors": self.vectors,
                    "documents": self.documents,
                },
                file,
            )

    @classmethod
    def load(cls, path: str | Path):
        with open(path, "rb") as file:
            data = pickle.load(file)

        store = cls()
        store.vectors = data["vectors"]
        store.documents = data["documents"]
        return store
