import requests
import mmh3
import base64
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def is_response_successful(response):
    return response.status_code == 200


def get_favicon_url(url):
    try:
        response = requests.get(url)
        if is_response_successful(response):
            soup = BeautifulSoup(response.text, "html.parser")
            icon_link = soup.find("link", rel=lambda x: x and "icon" in x.lower())
            if icon_link:
                return urljoin(url, icon_link.get("href"))
            parsed_url = urlparse(url)
            return urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", "favicon.ico")
    except requests.RequestException as e:
        print(f"[Error] {e}")
    return None


def get_favicon_hash(url):
    favicon_url = get_favicon_url(url)
    if not favicon_url:
        print("No favicon found.")
        return None

    try:
        response = requests.get(favicon_url)
        if is_response_successful(response):
            favicon_base64_data = base64.encodebytes(response.content).decode()
            favicon_hash = hex(mmh3.hash(favicon_base64_data))
            if favicon_hash.startswith("-"):
                favicon_hash = "-" + favicon_hash[3:]
            else:
                favicon_hash = favicon_hash[2:]
            return favicon_hash
    except requests.RequestException as e:
        print(f"[Error] {e}")
    return None
