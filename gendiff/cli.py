from gendiff.formatters.stylish import render as stylish
from gendiff.formatters.plain import render as plain
from gendiff.formatters.json import render as json_format
import argparse

FORMATS = {
    "stylish": stylish,
    "plain": plain,
    "json": json_format
}


def generate_parser():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        usage="%(prog)s [options] <first_file> <second_file>",
        description="Compares two configuration files \
        and show difference."
    )
    parser.add_argument("-f", "--format",
                        choices=FORMATS.keys(),
                        default="stylish",
                        help='output format (default: "stylish")'
                        )
    parser.add_argument("-V", "--version",
                        action="version",
                        version="%(prog)s 0.9.0")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args
