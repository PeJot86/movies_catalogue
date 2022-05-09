from unittest.mock import Mock
import tmdb_client
from main import app
import pytest



def test_get_single_movie(monkeypatch):
   mock_movies = ["Movie"]
   requests_mock = Mock()       
   response = requests_mock.return_value
   response.json.return_value = mock_movies
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies = tmdb_client.get_single_movie(movie_id = "id")
   assert movies ==mock_movies


def test_get_single_movie_cast(monkeypatch):
   mock_movie_cast = ["Movie"]     
   request_mock = Mock()
   response = request_mock.return_value
   response.json.return_value = mock_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", request_mock)
   movie_cast = tmdb_client.get_single_movie_cast(movie_id="id"[1])
   assert movie_cast == mock_movie_cast


def test_get_poster_url_uses_default_size():
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   assert expected_default_size in poster_url


def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None


@pytest.mark.parametrize("list_type", (
  "popular", "top_rated", "now_playing","upcoming"
))
def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get("/?list_type={list_type}")
       assert response.status_code == 200
       api_mock.assert_called_once_with({list_type})

