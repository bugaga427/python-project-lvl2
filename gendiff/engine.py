from gendiff.parsing import parsing_args
from gendiff.cli import generate_parser, FORMATS


def gendiff():
    parser = generate_parser()
    file_before, file_after = parsing_args()
    diff = get_diff(file_before, file_after, FORMATS[parser.format])
    print(diff)


def get_diff(file_before, file_after, format_name):
    return format_name(generate_difference(file_before, file_after))


def generate_difference(file_before, file_after):
    result = {}
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        status, value = check_keys(key, file_before, file_after)
        result[(status, key)] = value
    return result


def is_child(data):
    return isinstance(data, dict)


def check_keys(key, before, after):
    if key in before and key in after:
        return key_remained(before[key], after[key])
    elif key in before:
        return key_in_one_file(before[key], "removed")
    elif key in after:
        return key_in_one_file(after[key], "added")


def key_remained(before, after):
    if before == after:
        status = "no change"
        if is_child(before):
            value = ["children", generate_difference(before, after)]
        else:
            value = ["value", before]
    else:
        status = "changed"
        if is_child(before) and is_child(after):
            status = "no change"
            value = ["children", generate_difference(before, after)]
        elif is_child(before):
            value = [
                ["children", generate_difference(before, before)],
                ["value", after]
            ]
        elif is_child(after):
            value = [
                ["value", before],
                ["children", generate_difference(after, after)]
            ]
        else:
            value = [["value", before], ["value", after]]
    return status, value


def key_in_one_file(data, status):
    if is_child(data):
        return status, ["children", generate_difference(data, data)]
    return status, ["value", data]
