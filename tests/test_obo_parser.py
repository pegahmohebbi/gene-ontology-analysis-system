from src.parsers.obo_parser import OBOParser


def main():
    parser = OBOParser("data/go-basic.obo")
    terms = parser.parse()

    print("Total terms parsed:", len(terms))

    example_id = "GO:0000001"
    if example_id in terms:
        term = terms[example_id]
        print("\nExample term:")
        print("ID:", term.id)
        print("Name:", term.name)
        print("Namespace:", term.namespace)
        print("Definition:", term.definition)
        print("Parents:", term.get_parents())
    else:
        print(f"{example_id} not found.")


if __name__ == "__main__":
    main()