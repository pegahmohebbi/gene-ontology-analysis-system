from pathlib import Path
from typing import Dict

from src.models.go_term import GOTerm


class OBOParser:
    """
    Parser for Gene Ontology OBO files.
    """

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def parse(self) -> Dict[str, GOTerm]:
        terms = {}

        current_term = None

        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "[Term]":
                    if current_term:
                        terms[current_term.id] = current_term

                    current_term = GOTerm(id="", name="")

                elif current_term is not None:

                    if line.startswith("id:"):
                        current_term.id = line.split("id:")[1].strip()

                    elif line.startswith("name:"):
                        current_term.name = line.split("name:")[1].strip()

                    elif line.startswith("namespace:"):
                        current_term.namespace = line.split("namespace:")[1].strip()

                    elif line.startswith("def:"):
                        current_term.definition = line.split("def:")[1].strip()

                    elif line.startswith("is_a:"):
                        parent_id = line.split("is_a:")[1].split()[0]
                        current_term.add_parent(parent_id)

        if current_term:
            terms[current_term.id] = current_term

        return terms