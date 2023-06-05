import Levenshtein


class SearchMixin:

    def __get_fuzzy_matches(self, movies: dict, search_term: str) -> list:
        """
        finds movie names that matches a term closely instead of exactly
        :param search_term: string representing a part of a movie name
        :param movies: dictionary that stores movies as keys
        and their data as values
        :return: a list with the fuzzy matches for the search term
        """
        edit_threshold = 3
        return [
            movie for movie in movies
            if self.__check_entire_name_match(movie, edit_threshold,
                                              search_term)
            or self.__check_single_word_match(movie, edit_threshold,
                                              search_term)
        ]

    @staticmethod
    def __check_entire_name_match(movie_name: str,
                                  threshold: int,
                                  term: str) -> bool:
        """
        checks if a term searched by the user matches closely to a full name
        :param movie_name: full movie name
        :param threshold: maximum allowable Levenshtein distance between values
        :param term: a part of a movie name searched by the user
        :return: True if there is a match, False otherwise
        """
        return Levenshtein.distance(term, movie_name.lower()) <= threshold

    @staticmethod
    def __check_single_word_match(movie_name: str,
                                  threshold: int,
                                  term: str) -> bool:
        """
        checks if a term searched by the user matches closely to a single word
        in a movie name
        :param movie_name: full movie name
        :param threshold: maximum allowable Levenshtein distance between values
        :param term: a part of a movie name searched by the user
        :return: True if there is a match, False otherwise
        """
        return any([Levenshtein.distance(term, word.lower()) <= threshold
                    for word in movie_name.split()])

    def _search_movies(self, movies: dict) -> None:
        """
        finds and prints exact or close matches to a partial movie name
        :param movies: dictionary that stores movies as keys
        and their data as values
        """
        term = input("Enter part of a movie name: ")
        fuzzy_matches = []
        matched_movies = [movie for movie in movies if
                          term.lower() in movie.lower()]
        if not matched_movies:
            print(f"No matches for {term}.")
            fuzzy_matches = self.__get_fuzzy_matches(movies, term.lower())
            if fuzzy_matches:
                print("Did you mean: ")
        for match in matched_movies if matched_movies else fuzzy_matches:
            print(f"{match}, {movies[match]['rating']}")
