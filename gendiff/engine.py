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
    if 'False' in result:
        result = result.replace('False', 'false')
    if 'True' in result:
        result = result.replace('True', 'true')
    if 'None' in result:
        result = result.replace('None', 'null')
    return result
