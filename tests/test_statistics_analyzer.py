from src.parsers.obo_parser import OBOParser
from src.parsers.gaf_parser import GAFParser
from src.models.gene_ontology import GeneOntology
from src.models.annotation_store import AnnotationStore
from src.analysis.statistics_analyzer import StatisticsAnalyzer


def main():
    obo_parser = OBOParser("data/go-basic.obo")
    terms = obo_parser.parse()

    ontology = GeneOntology()
    for term in terms.values():
        ontology.add_term(term)
    ontology.build_edges()

    gaf_parser = GAFParser("data/goa_human.gaf.gz")
    df = gaf_parser.parse()

    store = AnnotationStore()
    store.load_from_dataframe(df)

    analyzer = StatisticsAnalyzer(ontology, store)
    stats = analyzer.analyze()

    print("Statistics:")
    print(stats)


if __name__ == "__main__":
    main()