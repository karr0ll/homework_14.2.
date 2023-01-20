import sqlite3


def get_genre(genre):
    """
    получает из аргумета искомый жанр,
    передает в запрос переменную
    и выводит данные о фильме и жанре в списке

    :param genre: строковое значение
    :return: список словарей
    """
    con = sqlite3.connect("../homework_14.2/netflix.db")
    cur = con.cursor()
    sqlite_query_result = """
                        SELECT title, listed_in, release_year, description
                        FROM netflix
                        WHERE lower(listed_in) LIKE '%{}%'
                        ORDER BY release_year DESC
                        LIMIT 10
                        """.format(genre)

    cur.execute(sqlite_query_result)
    sqlite_query_result = cur.fetchall()
    con.close()

    movies_by_genre = []
    for item in sqlite_query_result:
        movies_by_genre.append({"title": item[0], "description": item[2]})

    return movies_by_genre
