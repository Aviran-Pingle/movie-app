from abc import ABC, abstractmethod


class IStorage(ABC):
    """ Abstract class that represents a movies storage with CRUD methods """

    def __init__(self, file_path: str):
        self._file_path = file_path

    @abstractmethod
    def list_movies(self) -> dict:
        """
        Returns a dictionary of dictionaries that contains the movies
        information in the database
        """
        pass

    @abstractmethod
    def add_movie(self, title: str, year: int,
                  rating: float, poster: str) -> None:
        """ Adds a movie to the storage """
        pass

    def delete_movie(self, title: str) -> None:
        """
        Deletes a movie from the movies' database.
        Loads the information from the storage file, deletes the movie
        and saves it.
        """
        movies_db = self.list_movies()
        del movies_db[title]
        self._update_db(movies_db)

    def update_movie(self, title: str, rating: float) -> None:
        """
        Updates a movie from the movies' database.
        Loads the information from the storage file, updates the movie
        and saves it.
        """
        movies_db = self.list_movies()
        movies_db[title]["rating"] = rating
        self._update_db(movies_db)

    @abstractmethod
    def _update_db(self, new_db: dict) -> None:
        pass
