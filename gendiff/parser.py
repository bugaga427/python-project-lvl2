import argparse
import json
import yaml


def generate_parser():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args


def get_arguments():
    if generate_parser().first_file.endswith('.json') and \
       generate_parser().second_file.endswith('.json'):
        arg1 = json.load(open(generate_parser().first_file))
        arg2 = json.load(open(generate_parser().second_file))

    elif generate_parser().first_file.endswith(('.yaml', '.yml')) and \
            generate_parser().second_file.endswith(('.yaml', '.yml')):
        arg1 = yaml.load(
            open(generate_parser().first_file),
            Loader=yaml.FullLoader
        )
        arg2 = yaml.load(
            open(generate_parser().second_file),
            Loader=yaml.FullLoader
        )

    return arg1, arg2
