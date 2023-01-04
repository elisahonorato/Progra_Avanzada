from typing import Tuple, List
import requests
import json
import re

from parametros import GITHUB_BASE_URL, GITHUB_REPO_OWNER, GITHUB_REPO_NAME
from parametros import GITHUB_USERNAME
from parametros import ANIME_BASE_URL, ANIME_NUMERO
from utils.anime import Anime


def get_animes() -> Tuple[int, List[Anime]]:

    status_code = 404
    respuesta = requests.get(ANIME_BASE_URL.format(f"AB?id={ANIME_NUMERO}"))
    dict_animes = respuesta.json()["animes"]
    animes = []
    for anime in dict_animes:
        print(anime)
        print("")
        nuevo_anime = Anime(nombre = anime["name"], ano= str(anime["season"]), etiquetas= str(anime["tags"]))
        animes.append(nuevo_anime)

    status_code = respuesta.status_code
    return status_code, animes


def post_issue(token, animes: List[Anime]) -> Tuple[int, int]:
    status_code = 404
    issue_number = 1
    header = {'Accept': 'application/vnd.github+json',
              "Authorization": "token %s" %token,}

    url = GITHUB_BASE_URL.format(f"%s/%s/issues")% (
        GITHUB_REPO_OWNER, GITHUB_REPO_NAME)

    anime_string = ''
    for anime in animes:
        anime_string += f"{(anime.nombre)}\n"    
    
    data = {
        "title": GITHUB_USERNAME,
        "number": issue_number,
        "body": anime_string
    }
    
    respuesta = requests.post(url, data=json.dumps(data), headers=header)
    status_code = respuesta.status_code
    issue_number = respuesta.json()["number"]

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    status_code = 404
    header = {'Accept': 'application/vnd.github+json',
              "Authorization": "token %s" %token,}
    url = GITHUB_BASE_URL.format(f"%s/%s/issues/%s/lock")% (
        GITHUB_REPO_OWNER, GITHUB_REPO_NAME, numero_issue)
    respuesta = requests.put(url, headers=header)
    status_code = respuesta.status_code

    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    status_code = 404

    header = {'Accept': 'application/vnd.github+json',
              "Authorization": "token %s" %token,}
    url = GITHUB_BASE_URL.format(f"%s/%s/issues/%s/lock")% (
        GITHUB_REPO_OWNER, GITHUB_REPO_NAME, numero_issue)
    respuesta = requests.delete(url, headers=header)
    status_code = respuesta.status_code

    return status_code
