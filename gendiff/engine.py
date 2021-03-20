def generate_diff(file_before, file_after):
    result = "{\n"
    keys = get_keys(file_before, file_after)
    for key in keys:
        result += generate_message(key, file_before, file_after)
    result += "}"
    return convert_to_json_style(result)


def get_keys(file1, file2):
    return sorted(set(file1) | set(file2))


def generate_message(key, file1, file2):
    if key in file1:
        if key in file2:
            if file1[key] == file2[key]:
                return f"    {key}: {file1[key]}\n"
            else:
                return f"  - {key}: {file1[key]}\n  + {key}: {file2[key]}\n"
        else:
            return f"  - {key}: {file1[key]}\n"
    else:
        return f"  + {key}: {file2[key]}\n"


def convert_to_json_style(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message
