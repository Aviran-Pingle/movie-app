import re

from colorama import Fore

TARGET_FILE_NAME = "./_static/index.html"
TEMPLATE_FILE = "./_static/index_template.html"
PLACEHOLDER_BODY = "__TEMPLATE_MOVIE_GRID__"
PLACEHOLDER_TITLE = "__TEMPLATE_TITLE__"
TITLE = "My Movies App"


class WebsiteMixin:
    @staticmethod
    def __serialize_movie(movie_name: str, movie: dict) -> str:
        """
        converts a dictionary representation of a movie
        to an html representation
        :param movie_name: movie to be serialized
        :param movie: dict with the movie's data
        :return: html representation of the movie
        """
        return f"""<li>
        <div class="movie">
            <img class="movie-poster" src="{movie['poster']}" alt="movie 
            poster"> <div class="movie-title">{movie_name}</div>
            <div class="movie-year">{movie['year']}</div>
        </div>
    </li>
    """

    @staticmethod
    def __replace_file_content(file_name: str,
                               replacement_content: dict) -> str:
        """
        replace content of a file
        :param file_name: the fie whose text will be replaced
        :param replacement_content: dict with old content as keys
        and new content as values
        :return: new content after the replacement
        """

        with open(file_name) as handle:
            file_content = handle.read()

        for old_content, new_content in replacement_content.items():
            file_content = re.sub(f"\\b{old_content}\\b", new_content,
                                  file_content)

        return file_content

    def _generate_website(self, movies: dict) -> None:
        """
        generates a website from a movies dictionary
        :param movies: dict that stores movies as keys and their data as values
        """
        movies_html = ""
        for name, data in movies.items():
            movies_html += self.__serialize_movie(name, data)

        website_content = self.__replace_file_content(
            TEMPLATE_FILE,
            {
                PLACEHOLDER_BODY: movies_html,
                PLACEHOLDER_TITLE: TITLE
            }
        )

        with open(TARGET_FILE_NAME, "w") as handle:
            handle.write(website_content)

        print(Fore.GREEN + "Successfully generated the website." + Fore.RESET)
