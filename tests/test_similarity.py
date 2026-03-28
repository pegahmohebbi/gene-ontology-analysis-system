import pandas as pd

from src.models.annotation_store import AnnotationStore
from src.analysis.jaccard_similarity_analyzer import JaccardSimilarityAnalyzer
from src.analysis.cosine_similarity_analyzer import CosineSimilarityAnalyzer


def build_store():
    data = [
        {"DB_Object_Symbol": "GENE1", "GO_ID": "GO:1", "Evidence_Code": "EXP", "Aspect": "P"},
        {"DB_Object_Symbol": "GENE1", "GO_ID": "GO:2", "Evidence_Code": "EXP", "Aspect": "P"},
        {"DB_Object_Symbol": "GENE2", "GO_ID": "GO:2", "Evidence_Code": "IEA", "Aspect": "P"},
        {"DB_Object_Symbol": "GENE2", "GO_ID": "GO:3", "Evidence_Code": "IEA", "Aspect": "P"},
    ]

    df = pd.DataFrame(data)

    store = AnnotationStore()
    store.load_from_dataframe(df)
    return store


def test_jaccard_similarity():
    store = build_store()
    analyzer = JaccardSimilarityAnalyzer(store)

    score = analyzer.analyze("GENE1", "GENE2")

    assert score == 1 / 3


def test_cosine_similarity():
    store = build_store()
    analyzer = CosineSimilarityAnalyzer(store)

    score = analyzer.analyze("GENE1", "GENE2")

    assert round(score, 5) == round(1 / 2, 5)


def test_missing_gene():
    store = build_store()

    jaccard = JaccardSimilarityAnalyzer(store)
    cosine = CosineSimilarityAnalyzer(store)

    assert jaccard.analyze("GENE1", "UNKNOWN") == 0.0
    assert cosine.analyze("GENE1", "UNKNOWN") == 0.0


if __name__ == "__main__":
    test_jaccard_similarity()
    test_cosine_similarity()
    test_missing_gene()
    print("All tests passed ✅")