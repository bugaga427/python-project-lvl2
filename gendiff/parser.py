from gendiff.formatters.stylish import render as stylish
import argparse

FORMATS = {
    "stylish": stylish
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
