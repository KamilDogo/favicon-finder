from urllib.parse import urlparse


def is_valid_url(url):
    try:
        result = urlparse(url)
        return bool(result.scheme and result.netloc)
    except:
        return False


def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please enter again.")
