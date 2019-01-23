import os


def __boolean(value='') -> bool:
    if not value:
        return False
    value = value.upper()
    return True if value == 'TRUE' or value == '1' else False


def get_boolean(key: str) -> bool:
    return __boolean(os.getenv(key))


def get_list(key: str, splitter=',') -> list:
    value = os.getenv(key)
    if not value:
        return None
    if splitter is not ' ':
        value = value.replace(' ', '')
    return value.split(splitter)


def get_str(key):
    return os.getenv(key)
