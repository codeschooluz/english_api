import requests

url = 'http://127.0.0.1:8000/get'

dct1 = {
    'name': 'first-lesson',
    'question': 'name (plural) ?',
    'answer':'plurals'
}
dct2 = {
    'name':'first-lesson'
}

r = requests.get(url, params=dct2)
print(r.json())