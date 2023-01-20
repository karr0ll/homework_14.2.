import sqlite3


def get_release_date_interval(year_from, year_to):
    """
    получает из аргументов интервал для передачи в запрос
    и выводит список фильмов, подходящих под условие
    :param year_from: int начальный год интервала
    :param year_to: int конечный год интервала
    :return: список фильмов
    """
    con = sqlite3.connect("../homework_14.2/netflix.db")
    cur = con.cursor()

    sqlite_query_result = """SELECT title, release_year FROM netflix
                           WHERE release_year
                           BETWEEN {} AND {} AND title != '"'
                           ORDER BY title ASC LIMIT 100
                           """.format(int(year_from), int(year_to))

    cur.execute(sqlite_query_result)
    sqlite_query_result = cur.fetchall()
    con.close()

    release_date_data = []
    for item in sqlite_query_result:
        release_date_data.append({"title": item[0], "release_year": item[1]})
    return release_date_data


print(get_release_date_interval(2000, 2010))
