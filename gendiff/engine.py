def generate_diff(file_before, file_after, nesting_lvl=0):
    result = "{\n"
    keys = sorted(set(file_before) | set(file_after))
    for key in keys:
        if key in file_before and key not in file_after:
            if isinstance(file_before.get(key), dict):
                result += "    " * nesting_lvl + key_deleted(
                    key, generate_diff(
                        file_before[key],
                        file_before[key],
                        nesting_lvl=nesting_lvl + 1
                    )
                )
            else:
                result += "    " * nesting_lvl + key_deleted(
                    key, file_before[key]
                )
        elif key in file_after and key not in file_before:
            if isinstance(file_after.get(key), dict):
                result += "    " * nesting_lvl + key_added(
                    key, generate_diff(
                        file_after[key],
                        file_after[key],
                        nesting_lvl=nesting_lvl + 1
                    )
                )
            else:
                result += "    " * nesting_lvl + key_added(key, file_after[key])
        else:
            if file_before[key] == file_after[key]:
                if isinstance(file_before.get(key), dict):
                    result += "    " * nesting_lvl + key_not_changed(
                        key, generate_diff(
                            file_before[key],
                            file_after[key],
                            nesting_lvl=nesting_lvl + 1
                        )
                    )
                else:
                    result += "    " * nesting_lvl + key_not_changed(
                        key, file_before[key]
                    )
            else:
                if isinstance(
                    file_before.get(key), dict
                ) and isinstance(
                    file_after[key], dict
                ):
                    result += "    " * nesting_lvl + key_not_changed(
                        key, generate_diff(
                            file_before[key],
                            file_after[key],
                            nesting_lvl=nesting_lvl + 1
                        )
                    )
                elif isinstance(
                    file_before.get(key), dict
                ) and not isinstance(
                    file_after[key], dict
                ):
                    result += "    " * nesting_lvl + key_deleted(
                        key, generate_diff(
                            file_before[key],
                            file_before[key],
                            nesting_lvl=nesting_lvl + 1
                        )
                    )
                    result += "    " * nesting_lvl + key_added(
                        key, file_after[key]
                    )
                elif not isinstance(
                    file_before.get(key), dict
                ) and isinstance(
                    file_after[key], dict
                ):
                    result += "    " * nesting_lvl + key_deleted(
                        key, file_before[key]
                    )
                    result += "    " * nesting_lvl + key_added(
                        key, generate_diff(
                            file_after[key],
                            file_after[key],
                            nesting_lvl=nesting_lvl + 1
                        )
                    )
                else:
                    result += "    " * nesting_lvl + key_deleted(
                        key, file_before[key]
                    )
                    result += "    " * nesting_lvl + key_added(
                        key, file_after[key]
                    )
    result += "    " * nesting_lvl + "}"
    return edit_message(result)


def key_deleted(key, value):
    return f"  - {key}: {value}\n"


def key_added(key, value):
    return f"  + {key}: {value}\n"


def key_not_changed(key, value):
    return f"    {key}: {value}\n"


def edit_message(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message
