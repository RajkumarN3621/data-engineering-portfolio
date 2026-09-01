from sklearn.feature_extraction.text import TfidfVectorizer


class EmbeddingModel:
    """Local deterministic embedding adapter for portfolio execution."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
        )

    def fit(self, texts: list[str]):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts: list[str]):
        return self.vectorizer.transform(texts)
