from src.parsers.gaf_parser import GAFParser


def main():
    parser = GAFParser("data/goa_human.gaf.gz")
    df = parser.parse()

    print("Total annotations loaded:", len(df))
    print()
    print(df.head())


if __name__ == "__main__":
    main()