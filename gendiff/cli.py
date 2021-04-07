from gendiff.formatters import stylish, plain, json as json_format
import argparse

FORMATS = {
    "stylish": stylish,
    "plain": plain,
    "json": json_format
}


def generate_parser():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("-f", "--format",
                        choices=FORMATS.keys(),
                        default='stylish',
                        help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args
