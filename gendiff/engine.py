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
        return key_removed(before[key])
    elif key in after:
        return key_added(after[key])


def key_remained(before, after):
    if before == after:
        if is_child(before):
            return ("no change",
                    ["children", generate_difference(
                        before, after)])
        else:
            return "no change", ["value", before]
    else:
        if is_child(before) and is_child(after):
            return ("no change",
                    ["children", generate_difference(
                        before, after)])
        elif is_child(before):
            return ("changed",
                    [["children", generate_difference(
                        before, before)],
                        ["value", after]])
        elif is_child(after):
            return ("changed", [["value", before],
                    ["children", generate_difference(
                        after, after)]])
        else:
            return ("changed",
                    [["value", before], ["value", after]])


def key_added(after):
    if is_child(after):
        return "added", ["children", generate_difference(after, after)]
    return "added", ["value", after]


def key_removed(before):
    if is_child(before):
        return "removed", ["children", generate_difference(before, before)]
    return "removed", ["value", before]
