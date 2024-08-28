import os
import requests
from dotenv import load_dotenv

load_dotenv()


def rooms_list():
    url = os.getenv('ROOMS_LIST')
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


