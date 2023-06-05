import argparse
import sys

from dotenv import load_dotenv

from movie_app import MovieApp
from storage_classes.istorage import IStorage
from storage_classes.storage_json import StorageJson
from storage_classes.storage_csv import StorageCsv


def parse_args() -> IStorage:
    """
    parses the file_path command line argument
    and returns a suitable storage object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path",
                        help="path to set the storage (csv or json file)")
    file_path = parser.parse_args().file_path
    if file_path.lower().endswith(".csv"):
        return StorageCsv(file_path)
    if file_path.lower().endswith(".json"):
        return StorageJson(file_path)

    parser.print_help()
    sys.exit()


def main():
    load_dotenv()
    storage = parse_args()
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
