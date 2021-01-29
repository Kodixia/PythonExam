import requests

# Exercise

def getMovieTitles(title):
    movie_name = {'Title': str(title)}
    r = requests.get('https://jsonmock.hackerrank.com/api/movies/search/',params=movie_name)
    print("type of r " + str(type(r.json()["data"][0]["Title"])))
    json_file = r.json()
    movie_list = json_file['data']
    for movie in movie_list:
        print(f"Title:{movie['Title']}")
        print(f"Year:{movie['Year']}")
        print(f"imdbID:{movie['imdbID']}")
        print("")



