def generate_diff(file_before, file_after):
    result = "{\n"
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        if key in file_before and key not in file_after:
            result += f"  - {key}: {file_before[key]}\n"
        elif key in file_after and key not in file_before:
            result += f"  + {key}: {file_after[key]}\n"
        else:
            if file_before[key] == file_after[key]:
                result += f"    {key}: {file_before[key]}\n"
            else:
                result += f"  - {key}: {file_before[key]}\n"
                result += f"  + {key}: {file_after[key]}\n"
    result += "}"
    return edit_message(result)


def edit_message(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message
