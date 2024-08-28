import os
import requests
from dotenv import load_dotenv

load_dotenv()


def things_list():
    url = os.getenv('THINGS_LIST')

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

