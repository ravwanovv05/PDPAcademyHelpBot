import os
import requests
from dotenv import load_dotenv

load_dotenv()


def create_user(first_name: str, telegram_id: int, last_name: str = None, username: str = None):
    url = os.getenv('CREATE_USER')
    d = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'telegram_id': telegram_id,
    }
    response = requests.post(url, data=d)

    if response.status_code == 201:
        return response.json()


def user_detail(pk: int):
    url = f"{os.getenv('USER_DETAIL')}/{pk}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def user_without_user_role():
    url = os.getenv('USER_WITHOUT_USER_ROLE')
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


