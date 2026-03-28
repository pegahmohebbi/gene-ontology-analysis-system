from abc import ABC, abstractmethod


class Annotation(ABC):
    """
    Abstract base class for a gene annotation.
    """

    def __init__(self, gene_symbol: str, go_id: str, evidence_code: str, aspect: str):
        self._gene_symbol = gene_symbol
        self._go_id = go_id
        self._evidence_code = evidence_code
        self._aspect = aspect

    @property
    def gene_symbol(self):
        return self._gene_symbol

    @property
    def go_id(self):
        return self._go_id

    @property
    def evidence_code(self):
        return self._evidence_code

    @property
    def aspect(self):
        return self._aspect

    @abstractmethod
    def annotation_type(self) -> str:
        pass

    def to_dict(self):
        return {
            "gene_symbol": self.gene_symbol,
            "go_id": self.go_id,
            "evidence_code": self.evidence_code,
            "aspect": self.aspect,
            "annotation_type": self.annotation_type()
        }