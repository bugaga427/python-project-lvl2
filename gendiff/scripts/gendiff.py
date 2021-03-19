from gendiff.engine import generate_diff
from gendiff.parsing import parsing_args


def main():
    file_before, file_after = parsing_args()
    print(generate_diff(file_before, file_after))


if __name__ == "__main__":
    main()
