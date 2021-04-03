from gendiff.cli import generate_parser
import json
import yaml


def parsing_args():
    if is_json(generate_parser().first_file, generate_parser().second_file):
        arg1 = json.load(open(generate_parser().first_file))
        arg2 = json.load(open(generate_parser().second_file))

    elif is_yaml(generate_parser().first_file, generate_parser().second_file):
        arg1 = yaml.load(
            open(generate_parser().first_file),
            Loader=yaml.FullLoader
        )
        arg2 = yaml.load(
            open(generate_parser().second_file),
            Loader=yaml.FullLoader
        )

    return arg1, arg2


def is_json(file1, file2):
    return file1.endswith(".json") and file2.endswith(".json")


def is_yaml(file1, file2):
    return file1.endswith((".yaml", ".yml")) and \
        file2.endswith((".yaml", ".yml"))
