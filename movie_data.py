import sqlite3


def get_movie_data(title):
    """
    получает из аргумета искомое название фильма,
    передает в запрос переменную
    и выводит данные о фильме в словаре

    :param title: строковое значение
    :return: словарь
    """
    con = sqlite3.connect("../homework_14.2/netflix.db")
    cur = con.cursor()
    sqlite_query = """
            SELECT DISTINCT title, country, release_year, listed_in, description
            FROM netflix
            WHERE lower(title) LIKE '%{}%'
            ORDER BY release_year DESC
            LIMIT 1
            """.format(title)

    cur.execute(sqlite_query)
    sqlite_query_result = cur.fetchall()
    con.close()
    for item in sqlite_query_result:
        movie_data = {"title": item[0],
                      "country": item[1],
                      "release_year": item[2],
                      "genre": item[3],
                      "description": item[4]}
        return movie_data
