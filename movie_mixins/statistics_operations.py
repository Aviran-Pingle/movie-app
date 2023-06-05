import statistics
import random

import matplotlib.pyplot as plt


class StatisticsMixin:
    @staticmethod
    def __get_best_and_worst_movies(movies: dict) -> tuple:
        """
        finds and returns the highest and lowest rated movies
        :param movies: dictionary that stores movies and their data
        :return: a tuple with two lists, the first contains the worst movies
        and the second contains the best
        """
        worst_and_best_movies = []
        ratings = [movies[movie]["rating"] for movie in movies]
        for score in [min(ratings), max(ratings)]:
            worst_and_best_movies.append(
                [movie for (movie, data) in movies.items()
                 if data["rating"] == score])
        return worst_and_best_movies[0], worst_and_best_movies[1]

    def _print_movies_stats(self, movies: dict) -> None:
        """
        prints the average rating, median rating,
        highest and lowest rated movies
        :param movies: dictionary that stores movies and their data
        """
        ratings = [movies[movie]["rating"] for movie in movies]

        ratings_mean, ratings_median = (statistics.mean(ratings),
                                        statistics.median(ratings))

        worst_movies, best_movies = self.__get_best_and_worst_movies(movies)

        print(
            f"Average rating: {ratings_mean}\nMedian rating: {ratings_median}")
        for adjective, movies_list in [("Best", best_movies),
                                       ("Worst", worst_movies)]:
            print(f"{adjective} movies: ")
            for movie in movies_list:
                print(f"{movie}, {movies[movie]['rating']}")

    @staticmethod
    def _print_random_movie(movies: dict) -> None:
        """
        prints a random movie
        :param movies: dictionary that stores movies as keys
        and their data as values
        """
        random_movie = random.choice(list(movies))
        print(f"Your movie for tonight: {random_movie}, "
              f"it's rated {movies[random_movie]['rating']}")

    @staticmethod
    def _print_sorted_by_rating(movies: dict) -> None:
        """
        prints the movies in descending order according to their rating
        :param movies: dictionary that stores movies as keys
        and their data as values
        """
        sorted_movies = sorted(movies, key=lambda item: movies[item]['rating'],
                               reverse=True)
        for movie in sorted_movies:
            print(f"{movie}: {movies[movie]['rating']}")

    @staticmethod
    def _create_rating_histogram(movies: dict) -> None:
        """
        creates a histogram from movies ratings and saves it to a file
        :param movies: dictionary that stores movies and their data
        """
        bins = list(range(11))
        plt.hist([float(movies[movie]["rating"]) for movie in movies],
                 bins=bins,
                 edgecolor="black")
        plt.xlabel("Rating")
        plt.ylabel("Movies")
        file_name = input("File name/path (for saving): ")
        plt.savefig(file_name)
