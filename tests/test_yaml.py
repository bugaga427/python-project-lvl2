from gendiff.engine import generate_diff, edit_message
from gendiff.formatters import stylish, plain
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


def test_yaml_plain():
    before = yaml.load(
        open('tests/fixtures/yaml_recursive_before.yaml'),
        Loader=yaml.FullLoader
    )
    after = yaml.load(
        open('tests/fixtures/yaml_recursive_after.yaml'),
        Loader=yaml.FullLoader
    )
    result = open("tests/fixtures/diff_plain.txt")
    assert edit_message(
        plain.to_string(
            generate_diff(before, after, plain.render))) == result.read()
