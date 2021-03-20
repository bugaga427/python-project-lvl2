def generate_diff(file_before, file_after):
    result = "{\n"
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        if key in file_before and key not in file_after:
            result += f"  - {key}: {file_before[key]}\n"
        elif key in file_after and key not in file_before:
            result += f"  + {key}: {file_after[key]}\n"
        else:
            result += check_values(key, file_before, file_after)
    result += "}"
    return edit_message(result)


def check_values(key, file1, file2):
    if file1[key] == file2[key]:
        return f"    {key}: {file1[key]}\n"
    else:
        return f"  - {key}: {file1[key]}\n  + {key}: {file2[key]}\n"


def edit_message(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message
