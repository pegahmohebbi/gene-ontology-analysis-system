from src.models.annotation import Annotation


class ElectronicAnnotation(Annotation):
    """
    Represents an electronically inferred annotation.
    """

    def annotation_type(self) -> str:
        return "Electronic"