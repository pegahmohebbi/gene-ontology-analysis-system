import numpy as np
from src.analysis.base_similarity_analyzer import BaseSimilarityAnalyzer


class JaccardSimilarityAnalyzer(BaseSimilarityAnalyzer):
    """
    Computes Jaccard similarity between two genes
    based on shared GO terms.
    """

    def analyze(self, gene1, gene2):
        terms1 = self.annotation_store.get_terms_for_gene(gene1)
        terms2 = self.annotation_store.get_terms_for_gene(gene2)

        if not terms1 or not terms2:
            return 0.0

        union_terms = list(terms1.union(terms2))

        vec1 = np.array([1 if term in terms1 else 0 for term in union_terms])
        vec2 = np.array([1 if term in terms2 else 0 for term in union_terms])

        intersection = np.sum((vec1 == 1) & (vec2 == 1))
        union = np.sum((vec1 == 1) | (vec2 == 1))

        if union == 0:
            return 0.0

        return float(intersection / union)