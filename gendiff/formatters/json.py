import json


def render(data):
    return json.dumps(format(data), indent=4)


def format(data):
    result = {}
    for item in data:
        status, key = item[0], item[1]
        value = unpack_values(item[-1])
        if status == "added":
            result[key] = [status, value]
        elif status == "removed":
            result[key] = [status, value]
        elif status == "updated":
            old_value = unpack_values(item[2])
            result[key] = [status, old_value, value]
        elif status == "no changed":
            result[key] = value
    return result


def unpack_values(value):
    if isinstance(value, list):
        return format(value)
    return value
