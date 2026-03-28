from src.parsers.gaf_parser import GAFParser
from src.models.annotation_store import AnnotationStore


def main():
    parser = GAFParser("data/goa_human.gaf.gz")
    df = parser.parse()

    store = AnnotationStore()
    store.load_from_dataframe(df)

    print("Total annotation objects:", store.total_annotations())

    example_gene = "A1BG"
    terms = store.get_terms_for_gene(example_gene)

    print(f"\nGO terms for gene {example_gene}:")
    print(terms)


if __name__ == "__main__":
    main()