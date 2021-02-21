from gendiff.engine import generate_diff
from gendiff.parser import get_arguments


def main():
    file_before, file_after = get_arguments()
    print(generate_diff(file_before, file_after))


if __name__ == '__main__':
    main()
