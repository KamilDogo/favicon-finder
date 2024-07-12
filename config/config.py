import configparser
import os
import re


def is_valid_api_key(api_key):
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{60}$")
    return bool(pattern.match(api_key))


def get_config(config_filename):
    config_path = os.path.join(os.path.dirname(__file__), config_filename)
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        api_key = config["KEY1"]["APIKEY"]
        if is_valid_api_key(api_key):
            return api_key
        else:
            print("Invalid API key format.")
            return None
    except Exception as e:
        print(f"[Error] {e}")
        return None
