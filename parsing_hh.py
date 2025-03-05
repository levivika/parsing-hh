import requests

def get_python_vacancy():
    url = 'https://api.hh.ru/vacancies'
    params={
        'per_page': 100,
        'text': 'python',
        'area': 2
    }

    response = requests.get(url, params=params)
    data = response.json()
    found = data['found']
    pages = data['pages']
    vacancies = []
    for i in range(0, pages+1):
        params['page'] = i
        response = requests.get(url, params=params)
        data =response.json()
        vacancies.extend(data['items'])
    pass

get_python_vacancy()