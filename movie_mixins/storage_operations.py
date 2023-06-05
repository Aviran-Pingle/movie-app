from colorama import Fore

from storage_classes.istorage import IStorage
import movies_data_fetcher


class StorageOpsMixin:
    def __init__(self, storage: IStorage):
        self._storage = storage

    @staticmethod
    def _list_movies(movies: dict) -> None:
        """
        prints all the movies and their ratings and release year
        :param movies: dictionary that stores movies their data
        """
        print(f"\n{len(movies)} movies in total")
        for movie in movies:
            print(f"{movie}:")
            for attr, val in movies[movie].items():
                if attr != "poster":
                    print(f"\t{attr}: {val}")

    def _add_movie(self, movies: dict) -> None:
        """
        adds new movie to the db. asks the user for the new movie's details
        :param movies: dictionary that stores movies their data
        """
        movie_name = input("Enter new movie name: ")
        if movie_name not in movies:
            movie = movies_data_fetcher.fetch_movie_data(movie_name)
            if not movie:
                print(Fore.RED + "connection error" + Fore.RESET)
            elif movie["Response"] == "False":
                print(Fore.RED + f"The movie {movie_name} doesn't exist")
            else:
                self._storage.add_movie(movie["Title"], movie["Year"],
                                        float(movie["imdbRating"]),
                                        movie["Poster"])
                print(Fore.GREEN + f"The movie {movie_name}"
                                   f" was successfully added")
        else:
            print(Fore.RED + f"The movie {movie_name} already exists!")

    def _delete_movie(self, movies: dict) -> None:
        """
        deletes a movie from the db
        :param movies: dictionary that stores movies their data
        """
        movie_name = input("Movie to be deleted: ")
        if movie_name in movies:
            self._storage.delete_movie(movie_name)
            print(
                Fore.GREEN + f"The movie {movie_name} "
                             f"was successfully deleted")
        else:
            print(Fore.RED + f"The movie {movie_name} doesn't exist!")

    def _update_movie(self, movies: dict) -> None:
        """
        updates the rating of an existing movie
        :param movies: dictionary that stores movies their data
        """
        movie_name = input("Movie to be updated: ")
        if movie_name in movies:
            self._storage.update_movie(movie_name,
                                       float(input("Enter new movie "
                                                   "rating (0-10): ")))
            print(
                Fore.GREEN + f"The movie {movie_name} "
                             f"was successfully updated")
        else:
            print(Fore.RED + f"The movie {movie_name} doesn't exist!")
