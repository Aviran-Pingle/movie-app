import json

from storage_classes.istorage import IStorage


class StorageJson(IStorage):
    """ Movies storage represented as a Json file """

    def list_movies(self) -> dict:
        """
        The function loads the information from the JSON
        file and returns the data.
        """
        with open(self._file_path) as handle:
            return json.loads(handle.read())

    def add_movie(self, title: str, year: str,
                  rating: float, poster: str) -> None:
        """
        Loads the information from the JSON file, adds new movie
        and saves it.
        """
        movies_db = self.list_movies()
        movies_db[title] = {
            "year": year,
            "rating": rating,
            "poster": poster,
        }

        self._update_db(movies_db)

    def _update_db(self, new_db: dict) -> None:
        """
        Updates movies db in a json format
        :param new_db: dict representing the new db content
        """
        with open(self._file_path, "w") as handle:
            handle.write(json.dumps(new_db))
