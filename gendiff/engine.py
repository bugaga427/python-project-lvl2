from gendiff.parsing import parsing_args
from gendiff.parser import generate_parser, FORMATS


def gendiff():
    parser = generate_parser()
    file_before, file_after = parsing_args()
    diff = generate_diff(file_before, file_after)
    if parser.format in FORMATS:
        print(edit_message(FORMATS[parser.format](diff)))
    else:
        print("This output format is not supported.")


def generate_diff(file_before, file_after):
    result = []
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        result.extend(check_keys(key, file_before, file_after))
    return result


def is_dict(data):
    return isinstance(data, dict)


def check_keys(key, file1, file2):
    if key in file1 and key in file2:
        return check_values(key, file1, file2)
    elif key in file1:
        result = check_values(key, file1, file1)
        result[0][0] = "  -" + result[0][0][3:]
        return result
    elif key in file2:
        result = check_values(key, file2, file2)
        result[0][0] = "  +" + result[0][0][3:]
        return result


def check_values(key, file1, file2):
    if file1[key] == file2[key]:
        value = file1[key]
        if is_dict(file1[key]):
            value = generate_diff(file1[key], file2[key])
        return [[f"    {key}:", value]]
    else:
        value1 = file1[key]
        value2 = file2[key]
        if is_dict(file1[key]) and is_dict(file2[key]):
            return [[f"    {key}:", generate_diff(file1[key], file2[key])]]
        elif is_dict(file1[key]):
            value1 = generate_diff(file1[key], file1[key])
        elif is_dict(file2[key]):
            value2 = generate_diff(file2[key], file2[key])
        return [[f"  - {key}:", value1],
                [f"  + {key}:", value2]]


def edit_message(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message[:-1]
