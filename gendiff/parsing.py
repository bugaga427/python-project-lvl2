import json
import yaml


def parsing_args(file_before, file_after):
    if is_json(file_before, file_after):
        arg1 = json.load(open(file_before))
        arg2 = json.load(open(file_after))

    elif is_yaml(file_before, file_after):
        arg1 = yaml.load(open(file_before), Loader=yaml.FullLoader)
        arg2 = yaml.load(open(file_after), Loader=yaml.FullLoader)
    return arg1, arg2


def is_json(file1, file2):
    return file1.endswith(".json") and file2.endswith(".json")


def is_yaml(file1, file2):
    return file1.endswith((".yaml", ".yml")) and \
        file2.endswith((".yaml", ".yml"))
