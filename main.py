import requests
import json
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
API_KEY: str = os.getenv('API_KEY')
BASE_URL: str = 'https://dictionary.yandex.net/api/v1/dicservice.json'


def get_langs():
    response = requests.get('{base_url}/getLangs'.format(base_url=BASE_URL),
                            params={'key': API_KEY})

    return response


def lookup(land: str, text: str, ui='ru'):
    response = requests.get('{base_url}/lookup'.format(base_url=BASE_URL),
                            params={'key': API_KEY, 'lang': land, 'text': text, 'ui': ui})

    return response


def menu():
    print('Добро пожаловать в словарь!\n')
    langs_response = get_langs()

    if langs_response.status_code != 200:
        print('Извините, не удалось получить список направлений перевода.\nПопробуйте воспользоваться позже.')
        exit(1)

    langs = langs_response.json()
    print('Выберите одно из доступных направлений перевода:')
    for index, land in enumerate(langs):
        if index % 10 == 0:
            print('\n')
        print(land, end=' ')

    while (lang := input('\n\nВведите направление: ')) not in langs:
        print('Такого направления нет. Попробуйте ещё раз')

    text = input('Введите слово или фразу для перевода: ')
    lookup_response = lookup(lang, text)
    if lookup_response.status_code != 200:
        print('Не удалось выполнить перевод:', lookup_response.text)
        exit(1)

    pprint.pprint(lookup_response.json())


if __name__ == '__main__':
    menu()
