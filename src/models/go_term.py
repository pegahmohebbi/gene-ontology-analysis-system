from dataclasses import dataclass, field
from typing import Set

from src.models.ontology_element import OntologyElement


@dataclass
class GOTerm(OntologyElement):
    """
    Represents a Gene Ontology term.
    """

    namespace: str = ""
    definition: str = ""

    parents: Set[str] = field(default_factory=set)
    children: Set[str] = field(default_factory=set)

    def add_parent(self, parent_id: str):
        self.parents.add(parent_id)

    def add_child(self, child_id: str):
        self.children.add(child_id)

    def get_parents(self):
        return list(self.parents)

    def get_children(self):
        return list(self.children)