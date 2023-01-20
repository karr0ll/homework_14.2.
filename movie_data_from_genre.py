import sqlite3

con = sqlite3.connect("../homework_14.2/netflix.db")
cur = con.cursor()
sqlite_query = """
        SELECT title, type, release_year, listed_in, description
        FROM netflix
        WHERE description != ".\n"
        OR description != ""
        GROUP BY title, release_year
        """

cur.execute(sqlite_query)
sqlite_query_result = cur.fetchall()
con.close()


def get_movie_data(type_=None, release_year=None, genre=None):
    """
    получает из аргумета искомое название фильма,
    передает в запрос переменную
    и выводит данные о фильме в словаре

    :param type_: Moive или TV Show
    :param release_year: дата выпуска
    :param genre: жанр
    :return: список словарей
    """
    movie_list = []
    for line in sqlite_query_result:
        if type_.lower() == line[1].lower() \
                and release_year == line[2] \
                and genre.lower() in line[3].lower():
            movie_list.append({"title": line[0], "description": line[4]})
    return movie_list


for item in get_movie_data("movie", 2020, "thriller"):
    print(item)
