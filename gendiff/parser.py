import argparse
import json


def generate_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args


def get_arguments():
    arg1 = json.load(open(generate_parser().first_file))
    arg2 = json.load(open(generate_parser().second_file))
    return arg1, arg2
