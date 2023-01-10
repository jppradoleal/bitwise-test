import requests
from http import HTTPStatus
from django.http import Http404


def get_user_data(username):
    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == HTTPStatus.NOT_FOUND:
        response = requests.get(f"https://api.github.com/search/users?q={username}")
        return response.json().get("items")
    
    return response.json()
