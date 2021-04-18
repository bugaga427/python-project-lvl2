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
            old_value = check_value(data[item][0][1], data[item][0][0])
            new_value = check_value(data[item][1][1], data[item][1][0])
            value = ["updated", old_value, new_value]
        else:
            if status == "no change":
                value = check_value(data[item][1], data[item][0])
            else:
                value = [status, check_value(data[item][1], data[item][0])]
        result[key] = value
    return result


def is_child(value_type):
    return value_type == "children"


def check_value(value, value_type):
    if is_child(value_type):
        value = format(value)
    return value
