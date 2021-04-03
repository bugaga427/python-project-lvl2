from gendiff.engine import generate_diff
from gendiff.formatters import stylish
from gendiff.engine import edit_message
import yaml


def test_yaml():
    before = yaml.load(
        open('tests/fixtures/yaml_before.yaml'),
        Loader=yaml.FullLoader
    )
    after = yaml.load(
        open('tests/fixtures/yaml_after.yaml'),
        Loader=yaml.FullLoader
    )
    result = open("tests/fixtures/diff.txt")
    assert edit_message(
        stylish.to_string(
            generate_diff(before, after, stylish.render))) == result.read()


def test_yaml_recursive():
    before = yaml.load(
        open('tests/fixtures/yaml_recursive_before.yaml'),
        Loader=yaml.FullLoader
    )
    after = yaml.load(
        open('tests/fixtures/yaml_recursive_after.yaml'),
        Loader=yaml.FullLoader
    )
    result = open("tests/fixtures/diff_recursive.txt")
    assert edit_message(
        stylish.to_string(
            generate_diff(before, after, stylish.render))) == result.read()
