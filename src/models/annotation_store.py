from collections import defaultdict
from src.models.manual_annotation import ManualAnnotation
from src.models.electronic_annotation import ElectronicAnnotation


class AnnotationStore:
    """
    Stores and manages gene annotations.
    """

    def __init__(self):
        self.annotations = []
        self.gene_to_terms = defaultdict(set)

    def load_from_dataframe(self, df):
        for _, row in df.iterrows():

            gene = row["DB_Object_Symbol"]
            go_id = row["GO_ID"]
            evidence = row["Evidence_Code"]
            aspect = row["Aspect"]

            if evidence == "IEA":
                annotation = ElectronicAnnotation(gene, go_id, evidence, aspect)
            else:
                annotation = ManualAnnotation(gene, go_id, evidence, aspect)

            self.annotations.append(annotation)
            self.gene_to_terms[gene].add(go_id)

    def get_terms_for_gene(self, gene_symbol):
        return self.gene_to_terms.get(gene_symbol, set())

    def total_annotations(self):
        return len(self.annotations)