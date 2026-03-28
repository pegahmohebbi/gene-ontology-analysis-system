from src.parsers.gaf_parser import GAFParser
from src.models.annotation_store import AnnotationStore
from src.analysis.similarity_analyzer import SimilarityAnalyzer


def main():
    parser = GAFParser("data/goa_human.gaf.gz")
    df = parser.parse()

    store = AnnotationStore()
    store.load_from_dataframe(df)

    analyzer = SimilarityAnalyzer(store)

    gene1 = "A1BG"
    gene2 = "A1CF"

    score = analyzer.analyze(gene1, gene2)

    print(f"Similarity between {gene1} and {gene2}: {score}")


if __name__ == "__main__":
    main()