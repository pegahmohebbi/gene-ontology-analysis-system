import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from src.parsers.gaf_parser import GAFParser
from src.parsers.obo_parser import OBOParser
from src.models.annotation_store import AnnotationStore
from src.models.gene_ontology import GeneOntology
from src.analysis.jaccard_similarity_analyzer import JaccardSimilarityAnalyzer
from src.analysis.cosine_similarity_analyzer import CosineSimilarityAnalyzer
from src.analysis.statistics_analyzer import StatisticsAnalyzer
from src.analysis.neighborhood_analyzer import NeighborhoodAnalyzer

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def load_ontology(obo_path):
    obo_parser = OBOParser(obo_path)
    terms = obo_parser.parse()

    ontology_obj = GeneOntology()
    for term in terms.values():
        ontology_obj.add_term(term)
    ontology_obj.build_edges()

    return ontology_obj


def load_annotation_store(gaf_path):
    gaf_parser = GAFParser(gaf_path)
    df = gaf_parser.parse()

    annotation_store = AnnotationStore()
    annotation_store.load_from_dataframe(df)

    return annotation_store


# Load default ontology
ontology = load_ontology("data/go-basic.obo")

# Load default annotations
store = load_annotation_store("data/goa_human.gaf.gz")

# Create analyzers
jaccard_analyzer = JaccardSimilarityAnalyzer(store)
cosine_analyzer = CosineSimilarityAnalyzer(store)
statistics_analyzer = StatisticsAnalyzer(ontology, store)
neighborhood_analyzer = NeighborhoodAnalyzer(ontology)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/statistics")
def statistics():
    stats = statistics_analyzer.analyze()
    return render_template("statistics.html", stats=stats)


@app.route("/similarity", methods=["GET", "POST"])
def similarity():
    score = None
    gene1 = ""
    gene2 = ""
    metric = "jaccard"

    if request.method == "POST":
        gene1 = request.form["gene1"].strip()
        gene2 = request.form["gene2"].strip()
        metric = request.form.get("metric", "jaccard")

        if metric == "cosine":
            score = cosine_analyzer.analyze(gene1, gene2)
        else:
            score = jaccard_analyzer.analyze(gene1, gene2)

    return render_template(
        "similarity.html",
        score=score,
        gene1=gene1,
        gene2=gene2,
        metric=metric
    )


@app.route("/gene", methods=["GET", "POST"])
def gene():
    gene_symbol = ""
    terms = None

    if request.method == "POST":
        gene_symbol = request.form["gene_symbol"].strip()
        terms = store.get_terms_for_gene(gene_symbol)

    return render_template("gene.html", gene_symbol=gene_symbol, terms=terms)


@app.route("/term", methods=["GET", "POST"])
def term():
    go_id = ""
    term_obj = None

    if request.method == "POST":
        go_id = request.form["go_id"].strip()

        if go_id and not go_id.startswith("GO:"):
            go_id = f"GO:{go_id}"

        term_obj = ontology.get_term(go_id)

    return render_template("term.html", go_id=go_id, term=term_obj)


@app.route("/neighborhood", methods=["GET", "POST"])
def neighborhood():
    go_id = ""
    result = None

    if request.method == "POST":
        go_id = request.form["go_id"].strip()

        if go_id and not go_id.startswith("GO:"):
            go_id = f"GO:{go_id}"

        result = neighborhood_analyzer.analyze(go_id)

    return render_template("neighborhood.html", go_id=go_id, result=result)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    message = ""

    global ontology, store
    global jaccard_analyzer, cosine_analyzer, statistics_analyzer, neighborhood_analyzer

    if request.method == "POST":
        obo_file = request.files.get("obo_file")
        gaf_file = request.files.get("gaf_file")

        try:
            if obo_file and obo_file.filename:
                obo_filename = secure_filename(obo_file.filename)
                obo_path = os.path.join(UPLOAD_FOLDER, obo_filename)
                obo_file.save(obo_path)
                ontology = load_ontology(obo_path)

            if gaf_file and gaf_file.filename:
                gaf_filename = secure_filename(gaf_file.filename)
                gaf_path = os.path.join(UPLOAD_FOLDER, gaf_filename)
                gaf_file.save(gaf_path)
                store = load_annotation_store(gaf_path)

            jaccard_analyzer = JaccardSimilarityAnalyzer(store)
            cosine_analyzer = CosineSimilarityAnalyzer(store)
            statistics_analyzer = StatisticsAnalyzer(ontology, store)
            neighborhood_analyzer = NeighborhoodAnalyzer(ontology)

            message = "Files uploaded and system updated successfully!"

        except Exception as e:
            message = f"Error: {e}"

    return render_template("upload.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, use_reloader=False)