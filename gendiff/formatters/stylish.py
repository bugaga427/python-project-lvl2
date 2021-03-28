def render(message, lvl=0):
    result = ""
    result += "{\n"
    for key, value in message:
        if isinstance(value, list):
            result += "    " * lvl + f"{key} {render(value, lvl + 1)}"
        else:
            result += "    " * lvl + f"{key} {value}\n"
    result += "    " * lvl + "}\n"
    return result
