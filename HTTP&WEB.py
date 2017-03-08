import requests

SEARCH_ENDPOINT = 'http://www.omdbapi.com/?t='

def search_movie(query):
    response = requests.get(SEARCH_ENDPOINT + query)
    movie = response.json()
    return movie

if __name__ == "__main__":
    query = input("Enter movie?")
    movie = search_movie(query)
    print("Title:" + movie.get("Title"))
