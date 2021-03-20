from gendiff.engine import generate_diff
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
    assert generate_diff(before, after) == result.read()
