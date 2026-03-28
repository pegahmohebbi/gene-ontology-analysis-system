import numpy as np
from src.analysis.base_similarity_analyzer import BaseSimilarityAnalyzer


class CosineSimilarityAnalyzer(BaseSimilarityAnalyzer):
    """
    Computes cosine similarity between two genes
    based on GO term vectors.
    """

    def analyze(self, gene1, gene2):
        terms1 = self.annotation_store.get_terms_for_gene(gene1)
        terms2 = self.annotation_store.get_terms_for_gene(gene2)

        if not terms1 or not terms2:
            return 0.0

        union_terms = list(terms1.union(terms2))

        vec1 = np.array([1 if term in terms1 else 0 for term in union_terms], dtype=float)
        vec2 = np.array([1 if term in terms2 else 0 for term in union_terms], dtype=float)

        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return float(np.dot(vec1, vec2) / (norm1 * norm2))