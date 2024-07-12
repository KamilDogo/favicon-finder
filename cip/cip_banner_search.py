import requests
import json
from utils.response_utils import is_response_successful


def get_cip_banner_search(url, favicon_hash, offset, api_key):
    base_url = f"https://api.criminalip.io/v1/banner/search"
    headers = {"x-api-key": api_key}
    params = {"query": "favicon : {}".format(favicon_hash), "offset": offset}

    try:
        response = requests.get(base_url, params=params, headers=headers)
        if is_response_successful(response):
            get_ip_address(response.text)
        else:
            print(response.status_code)
    except requests.RequestException as e:
        print(f"[Error] {e}")


def get_ip_address(response_text):
    try:
        result_data = json.loads(response_text)
        result_list = result_data["data"]["result"]
        result_count = len(result_list)

        print(f"======== [ IP ADDRESS ] ========\n[ Found : {result_count} ]")
        for result in result_list:
            print(result["ip_address"])
    except (json.JSONDecodeError, KeyError) as e:
        print(f"[Error] {e}")
