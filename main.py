from config.config import get_config
from utils.url_utils import is_valid_url, get_valid_input
from utils.number_utils import is_valid_number
from utils.favicon_utils import get_favicon_hash
from cip.cip_banner_search import get_cip_banner_search


def main():
    api_key = get_config("api_key.ini")
    if not api_key:
        print("API key is invalid or not found. Please check your api_key.ini file.")
        return

    url = get_valid_input("Input URL: ", is_valid_url)
    offset = get_valid_input("Input Number: ", is_valid_number)

    favicon_hash = get_favicon_hash(url)
    if favicon_hash:
        get_cip_banner_search(url, str(favicon_hash), offset, api_key)
    else:
        print("Failed to get favicon hash.")


if __name__ == "__main__":
    main()
