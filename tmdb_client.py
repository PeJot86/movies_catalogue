import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MWQyMWEyMTYxOGY4YTZjYzQ4YTg0OTc0OTBmMzM1MCIsInN1YiI6IjYyNGQ1NThmNGNiZTEyMDA2NWI5ZGQxOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gKlIXnw03n5gXXr_KkkVoKUCzgT-iR-tJsE0JQhoavw" 


def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return call_tmdb_api(f"movie/{list_type}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, type_list):
    if type_list == 'popular':
        data = get_movies_list('popular')
    elif type_list == 'top_rated':
        data =  get_movies_list('top_rated')
    elif type_list == 'upcoming':
        data =  get_movies_list('upcoming')
    elif type_list == 'now_playing':
        data =  get_movies_list('now_playing')
    random.shuffle (data["results"])
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

