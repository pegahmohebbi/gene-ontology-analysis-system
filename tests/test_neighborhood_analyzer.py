from src.parsers.obo_parser import OBOParser
from src.models.gene_ontology import GeneOntology
from src.analysis.neighborhood_analyzer import NeighborhoodAnalyzer


def main():
    parser = OBOParser("data/go-basic.obo")
    terms = parser.parse()

    ontology = GeneOntology()
    for term in terms.values():
        ontology.add_term(term)

    ontology.build_edges()

    analyzer = NeighborhoodAnalyzer(ontology)

    go_id = "GO:0000001"
    result = analyzer.analyze(go_id)

    if result is None:
        print("Term not found.")
    else:
        print("Neighbourhood analysis result:")
        print(result)


if __name__ == "__main__":
    main()