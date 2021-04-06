def format(data):
    result = {}
    for item in data:
        status, key = item[0], item[1]
        value = unpack_values(item[-1])
        if status == "added":
            result[f"  + {key}"] = value
        elif status == "removed":
            result[f"  - {key}"] = value
        elif status == "updated":
            old_value = unpack_values(item[2])
            result[f"  - {key}"] = old_value
            result[f"  + {key}"] = value
        elif status == "no changed":
            result[f"    {key}"] = value
    return result


def unpack_values(value):
    if isinstance(value, list):
        return format(value)
    return value


def to_string(data, lvl=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = to_string(value, lvl + 1)
        result += f"{'    ' * lvl}{key}: {value}\n"
    result += f"{'    ' * lvl}}}"
    return result
