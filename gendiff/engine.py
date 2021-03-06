def generate_diff(file_before, file_after):
    result = '{\n'
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        if key in file_before:
            if key in file_after:
                if file_before[key] == file_after[key]:
                    result += f'    {key}: {file_before[key]}\n'
                else:
                    result += f'  - {key}: {file_before[key]}\n'
                    result += f'  + {key}: {file_after[key]}\n'
            else:
                result += f'  - {key}: {file_before[key]}\n'
        else:
            result += f'  + {key}: {file_after[key]}\n'
    result += '}'
    return convert_to_json_style(result)


def convert_to_json_style(message):
    if 'False' in message:
        message = message.replace('False', 'false')
    if 'True' in message:
        message = message.replace('True', 'true')
    if 'None' in message:
        message = message.replace('None', 'null')
    return message
