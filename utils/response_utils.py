import requests


def is_response_successful(response):
    if response.status_code == 200:
        return True
    print(response.status_code)
    return False
