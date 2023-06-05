import csv

from storage_classes.istorage import IStorage


class StorageCsv(IStorage):
    """ Movies storage represented as a CSV file """

    def __init__(self, file_path):
        super().__init__(file_path)
        self._fieldnames = ["title", "year", "rating", "poster"]

    def list_movies(self) -> dict:
        """
        The function loads the information from the csv file
        and returns the data.
        """
        with open(self._file_path) as handle:
            row: dict
            return {
                row["title"]: {
                    "rating": row["rating"],
                    "year": row["year"],
                    "poster": row["poster"]
                }
                for row in csv.DictReader(handle)
            }

    def add_movie(self, title: str, year: int,
                  rating: float, poster: str) -> None:
        """
        Loads the information from the csv file, adds new movie
        and saves it.
        """
        with open(self._file_path, "a") as handle:
            writer = csv.DictWriter(handle, fieldnames=self._fieldnames)
            writer.writerow({"title": title, "year": year, "rating": rating,
                             "poster": poster})

    def _update_db(self, new_db: dict) -> None:
        """
        Updates movies db in a csv format
        :param new_db: dict representing the new db content
        """
        movies_list = [{"title": title, **info}
                       for title, info in new_db.items()]
        with open(self._file_path, "w") as handle:
            writer = csv.DictWriter(handle, fieldnames=self._fieldnames)
            writer.writeheader()
            writer.writerows(movies_list)
