from gendiff.engine import generate_diff
import yaml


def test_yaml():
    before = yaml.load(open('tests/fixtures/yaml_before.yaml'))
    after = yaml.load(open('tests/fixtures/yaml_after.yaml'))
    result = open("tests/fixtures/diff.txt")
    assert generate_diff(before, after) == result.read()
