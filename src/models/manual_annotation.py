from src.models.annotation import Annotation


class ManualAnnotation(Annotation):
    """
    Represents a manually curated annotation.
    """

    def annotation_type(self) -> str:
        return "Manual"