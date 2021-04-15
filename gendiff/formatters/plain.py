from gendiff.formatters.stylish import edit_message


def render(data):
    return edit_message(to_string(format(data)))


def format(data, key_path=""):
    result = []
    for item in data.keys():
        status = item[0]
        key = key_path + item[1]
        if status == "added":
            value = unpach_values(data[item][1])
            result.append(f"Property '{key}' was added with value: {value}")
        elif status == "removed":
            result.append(f"Property '{key}' was removed")
        elif status == "changed":
            old_value = unpach_values(data[item][0][1])
            new_value = unpach_values(data[item][1][1])
            result.append(
                f"Property '{key}' was updated. From {old_value} to {new_value}"
            )
        else:
            value_type, value = data[item]
            if value_type == "children":
                result.extend(format(value, key + "."))
    return result


def unpach_values(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def to_string(data):
    return "\n".join(data)
