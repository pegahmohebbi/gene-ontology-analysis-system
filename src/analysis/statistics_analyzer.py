from src.analysis.base_analyzer import BaseAnalyzer


class StatisticsAnalyzer(BaseAnalyzer):
    """
    Computes summary statistics for ontology and annotation data.
    """

    def __init__(self, ontology, annotation_store):
        self.ontology = ontology
        self.annotation_store = annotation_store

    def analyze(self):
        namespace_counts = {
            "biological_process": 0,
            "molecular_function": 0,
            "cellular_component": 0
        }

        for term in self.ontology.all_terms():
            if term.namespace in namespace_counts:
                namespace_counts[term.namespace] += 1

        return {
            "total_go_terms": self.ontology.total_terms(),
            "total_annotations": self.annotation_store.total_annotations(),
            "namespace_counts": namespace_counts
        }