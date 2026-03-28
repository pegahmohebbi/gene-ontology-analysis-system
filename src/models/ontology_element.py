from abc import ABC
from dataclasses import dataclass, asdict


@dataclass
class OntologyElement(ABC):
    """
    Base class for ontology elements
    """

    id: str
    name: str
    description: str = ""

    def to_dict(self):
        return asdict(self)