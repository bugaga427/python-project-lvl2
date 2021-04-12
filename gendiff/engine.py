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
    result = []
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        result.extend(check_keys(key, file_before, file_after))
    return result


def is_child(data):
    return isinstance(data, dict)


def check_keys(key, file1, file2):
    if key in file1 and key in file2:
        return check_values(key, file1, file2)
    elif key in file1:
        result = check_values(key, file1, file1)
        result[0][0] = "removed"
    elif key in file2:
        result = check_values(key, file2, file2)
        result[0][0] = "added"
    return result


def check_values(key, file1, file2):
    if file1[key] == file2[key]:
        value = file1[key]
        if is_child(value):
            value = generate_difference(file1[key], file2[key])
        return [["no changed", key, value]]
    else:
        value1 = file1[key]
        value2 = file2[key]
        if is_child(file1[key]) and is_child(file2[key]):
            return [["no changed", key, generate_difference(value1, value2)]]
        elif is_child(file1[key]):
            value1 = generate_difference(file1[key], file1[key])
        elif is_child(file2[key]):
            value2 = generate_difference(file2[key], file2[key])
        return [["updated", key, value1, value2]]
