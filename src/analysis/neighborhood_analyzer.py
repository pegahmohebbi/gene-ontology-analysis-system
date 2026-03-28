from src.analysis.base_analyzer import BaseAnalyzer


class NeighborhoodAnalyzer(BaseAnalyzer):
    """
    Analyzes the local neighbourhood of a GO term
    using its parent and child relationships.
    """

    def __init__(self, ontology):
        self.ontology = ontology

    def analyze(self, go_id):
        term = self.ontology.get_term(go_id)

        if term is None:
            return None

        parents = self.ontology.get_parents(go_id)
        children = self.ontology.get_children(go_id)

        return {
            "go_id": go_id,
            "name": term.name,
            "namespace": term.namespace,
            "parents": parents,
            "children": children,
            "parent_count": len(parents),
            "child_count": len(children),
            "neighborhood_size": len(parents) + len(children)
        }