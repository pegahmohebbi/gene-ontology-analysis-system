from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """
    Abstract base class for analysis components.
    """

    @abstractmethod
    def analyze(self, *args, **kwargs):
        pass