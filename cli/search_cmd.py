import json


def search_cmd(query):
    with open("./data/movies.json") as f:
        movies_file = json.load(f)
        movies = movies_file['movies']

        movie_list = []

        query = query.lower()

        for i in range(0, len(movies), 1):
            if query in movies[i]['title'].lower():
                movie_list.append(movies[i])

        sorted_asc = sorted(movie_list, key=lambda x: x["id"])

        for i in range(0, 5, 1):
            print(f'{i+1}. {sorted_asc[i]["title"]}')

    return
