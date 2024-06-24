import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


def get_langs():
    response = requests.get('{base_url}/lookup?key={key}&lang=ru-en&text=задача'.format(
        base_url=BASE_URL,
        key=API_KEY
    ))

    return response


result = json.loads(get_langs().text)
print(result)
