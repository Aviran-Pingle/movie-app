from colorama import Fore, init

from movie_mixins.website_generator import WebsiteMixin
from movie_mixins.storage_operations import StorageOpsMixin
from movie_mixins.statistics_operations import StatisticsMixin
from movie_mixins.search_operations import SearchMixin

EXIT_PROGRAM = "0"


class MovieApp(StorageOpsMixin, StatisticsMixin, WebsiteMixin, SearchMixin):

    def _dispatch_operation(self, choice: int) -> None:
        """
        calls the requested operation
        :param choice: user's choice
        """
        movies_operations = {
            1: self._list_movies,
            2: self._add_movie,
            3: self._delete_movie,
            4: self._update_movie,
            5: self._print_movies_stats,
            6: self._print_random_movie,
            7: self._search_movies,
            8: self._print_sorted_by_rating,
            9: self._create_rating_histogram,
            10: self._generate_website,
        }
        movies_operations[choice](self._storage.list_movies())

    @staticmethod
    def _choose_from_menu() -> str:
        """
        prints the menu to the user and gives him the possibility
        to choose from it
        :return: The option that the user chose
        """
        menu = """
Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create rating histogram
10. Generate website
"""
        print(Fore.BLUE + menu)

        return input("Enter choice (0-10): ")

    def run(self):
        init(autoreset=True)  # undo color changes at the end of every print

        print(Fore.MAGENTA + "********** My Movies Database **********")
        while True:
            choice = self._choose_from_menu()

            if choice == EXIT_PROGRAM:
                print("Bye!")
                break

            try:
                self._dispatch_operation(int(choice))
            except (KeyError, ValueError):
                print(Fore.RED + "Invalid choice")
            input("\npress enter to continue")
