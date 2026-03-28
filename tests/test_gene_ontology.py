from src.parsers.obo_parser import OBOParser
from src.models.gene_ontology import GeneOntology


def main():
    parser = OBOParser("data/go-basic.obo")
    terms = parser.parse()

    ontology = GeneOntology()

    for term in terms.values():
        ontology.add_term(term)

    ontology.build_edges()

    print("Total ontology terms:", ontology.total_terms())

    example_id = "GO:0000001"
    term = ontology.get_term(example_id)

    if term:
        print("\nExample term:")
        print("ID:", term.id)
        print("Name:", term.name)
        print("Parents:", ontology.get_parents(example_id))
        print("Children:", ontology.get_children(example_id))
    else:
        print("Term not found.")


if __name__ == "__main__":
    main()