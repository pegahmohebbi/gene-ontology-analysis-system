import gzip
import pandas as pd


class GAFParser:
    """
    Parser for GAF annotation files.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def parse(self) -> pd.DataFrame:
        rows = []

        open_func = gzip.open if self.filepath.endswith(".gz") else open

        with open_func(self.filepath, "rt", encoding="utf-8") as file:
            for line in file:
                if line.startswith("!"):
                    continue

                parts = line.strip().split("\t")

                if len(parts) > 8:
                    rows.append({
                        "DB": parts[0],
                        "DB_Object_ID": parts[1],
                        "DB_Object_Symbol": parts[2],
                        "Qualifier": parts[3],
                        "GO_ID": parts[4],
                        "DB_Reference": parts[5],
                        "Evidence_Code": parts[6],
                        "With_From": parts[7],
                        "Aspect": parts[8],
                    })

        return pd.DataFrame(rows)