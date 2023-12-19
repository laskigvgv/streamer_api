import requests


def make_api_call(url):
    response = requests.get(url)
    print(response.text)
