import requests

def get_python_vacancy:
    url = 'https://api.hh.ru/vacancies'
    params={
        'per_page': 100,
        'text': 'python'
        'area': 2
    }
