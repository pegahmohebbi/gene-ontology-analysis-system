class GeneOntology:
    """
    Stores and manages Gene Ontology terms.
    """

    def __init__(self):
        self.terms = {}

    def add_term(self, term):
        self.terms[term.id] = term

    def get_term(self, go_id):
        return self.terms.get(go_id)

    def all_terms(self):
        return list(self.terms.values())

    def build_edges(self):
        for term in self.terms.values():
            for parent_id in term.parents:
                parent = self.get_term(parent_id)
                if parent is not None:
                    parent.add_child(term.id)

    def get_parents(self, go_id):
        term = self.get_term(go_id)
        if term:
            return term.get_parents()
        return []

    def get_children(self, go_id):
        term = self.get_term(go_id)
        if term:
            return term.get_children()
        return []

    def total_terms(self):
        return len(self.terms)