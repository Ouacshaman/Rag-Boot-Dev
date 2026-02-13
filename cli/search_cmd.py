import json
import string


def search_cmd(query):
    with open("./data/movies.json") as f:
        movies_file = json.load(f)
        movies = movies_file['movies']

        movie_list = []

        query = query.lower()
        query = remove_punctuation(query)

        for i in range(0, len(movies), 1):
            title_mov = remove_punctuation(movies[i]['title'].lower())
            q_tok = tokenization(query)
            for q in q_tok:
                if q in title_mov:
                    movie_list.append(movies[i])
                    break

        sorted_asc = sorted(movie_list, key=lambda x: x["id"])

        i = 1
        for movie in sorted_asc:
            if i > 5:
                break
            print(f'{i}. {movie["title"]}')
            i += 1

    return


def remove_punctuation(val):
    table = str.maketrans("", "", string.punctuation)
    res = val.translate(table)
    return res


def tokenization(val):
    vals = val.split()
    return vals
