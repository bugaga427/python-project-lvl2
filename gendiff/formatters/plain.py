line_list = []


def format(data, key_path=""):
    for item in data:
        status, key = item[0], key_path + item[1]
        value = unpack_values(item[-1])
        if status == "added":
            line_list.append(key_added(key, value))
        elif status == "removed":
            line_list.append(key_removed(key))
        elif status == "updated":
            old_value = unpack_values(item[2])
            line_list.append(key_updated(key, old_value, value))
        elif status == "no changed":
            value = item[-1]
            key_no_changed(key, value, key_path)
    return line_list


def key_added(key, value):
    return f"Property '{key}' was added with value: {value}"


def key_removed(key):
    return f"Property '{key}' was removed"


def key_updated(key, old_value, new_value):
    return f"Property '{key}' was updated. From {old_value} to {new_value}"


def key_no_changed(key, value, key_path):
    if isinstance(value, list):
        format(value, key + '.')


def unpack_values(value):
    if isinstance(value, list):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def to_string(data):
    data = "\n".join(format(data))
    line_list.clear()
    return data
