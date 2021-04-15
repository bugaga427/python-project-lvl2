from gendiff.formatters.stylish import edit_message


def render(data):
    return edit_message(to_string(format(data)))


def format(data, key_path=""):
    result = []
    for item in data.keys():
        status = item[0]
        key = key_path + item[1]
        if status == "changed":
            old_value = data[item][0]
            new_value = data[item][1]
            result.extend(key_changed(key, old_value, new_value))
        elif status == "added":
            value_type, value = data[item]
            value = unpach_values(value, value_type)
            result.extend([f"Property '{key}' was added with value: {value}"])
        elif status == "removed":
            result.extend([f"Property '{key}' was removed"])
        elif status == "no change":
            value_type, value = data[item]
            if value_type == "children":
                result.extend(format(value, key + "."))
    return result


def key_changed(key, old_value, new_value):
    old_value = unpach_values(old_value[1], old_value[0])
    new_value = unpach_values(new_value[1], new_value[0])
    return [f"Property '{key}' was updated. From {old_value} to {new_value}"]


def unpach_values(value, value_type):
    if value_type == "children":
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def to_string(data):
    return "\n".join(data)
