import os


def get_dd_api_key():
    try:
        return os.environ['API_KEY']
    except KeyError:
        raise KeyError('API_KEY NOT SET')


API_KEY = get_dd_api_key()
