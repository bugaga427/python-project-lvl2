from gendiff.engine import generate_diff
from gendiff.formatters.stylish import render as stylish
from gendiff.formatters.plain import render as plain
from gendiff.formatters.json import render as json_format
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
    assert generate_diff(before, after, stylish) == result.read()


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
    assert generate_diff(before, after, stylish) == result.read()


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
    assert generate_diff(before, after, plain) == result.read()


def test_yaml_json():
    before = yaml.load(
        open('tests/fixtures/yaml_recursive_before.yaml'),
        Loader=yaml.FullLoader
    )
    after = yaml.load(
        open('tests/fixtures/yaml_recursive_after.yaml'),
        Loader=yaml.FullLoader
    )
    result = open("tests/fixtures/diff_json.txt")
    assert generate_diff(before, after, json_format) == result.read()
