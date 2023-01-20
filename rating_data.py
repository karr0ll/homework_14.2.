import sqlite3

con = sqlite3.connect("../homework_14.2/netflix.db")
cur = con.cursor()
sqlite_query_result = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
                    OR rating = 'PG'
                    OR rating = 'PG-13'
                    OR rating = 'R'
                    OR rating = 'NC-17'
                    ORDER BY title
                    """

cur.execute(sqlite_query_result)
sqlite_query_result = cur.fetchall()
con.close()



def get_rating(rating):
    """
    получает из аргумета искомый рейтинг,
    передает в запрос переменную
    и выводит данные о фильмах в словаре

    :param rating: строковое значениу
    :return: список с фильмами
    """
    children = ["G"]
    family = ["G", "PG", "PG-13"]

    children_movies = []
    family_movies = []
    adult_movies = []
    movies_rated_data = []

    for item in sqlite_query_result:
        if item[1] in children:
            children_movies.append({"title": item[0], "rating": item[1], "description": item[2]})
        elif item[1] in family:
            family_movies.append({"title": item[0], "rating": item[1], "description": item[2]})
        else:
            adult_movies.append({"title": item[0], "rating": item[1], "description": item[2]})

    for item in children_movies:
        if rating == "children":
            movies_rated_data.append(item)
    for item in family_movies:
        if rating == "family":
            movies_rated_data.append(item)
    for item in adult_movies:
        if rating == "adult":
            movies_rated_data.append(item)

    return movies_rated_data


