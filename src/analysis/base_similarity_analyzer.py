from abc import abstractmethod
from src.analysis.base_analyzer import BaseAnalyzer


class BaseSimilarityAnalyzer(BaseAnalyzer):
    """
    Abstract base class for gene similarity analyzers.
    All similarity analyzers must implement the same interface.
    """

    def __init__(self, annotation_store):
        self.annotation_store = annotation_store

    @abstractmethod
    def analyze(self, gene1, gene2):
        pass