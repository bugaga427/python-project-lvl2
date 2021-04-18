import json


def render(data):
    data = format(data)
    data = json.dumps(data, indent=4)
    return data


def format(data):
    result = {}
    for item in data.keys():
        status, key = item
        if status == "changed":
            old_value = check_value(data[item][0])
            new_value = check_value(data[item][1])
            value = ["updated", old_value, new_value]
        else:
            if status == "no change":
                value = check_value(data[item])
            else:
                value = [status, check_value(data[item])]
        result[key] = value
    return result


def is_child(value_type):
    return value_type == "children"


def check_value(value):
    value_type, value = value
    if is_child(value_type):
        value = format(value)
    return value
