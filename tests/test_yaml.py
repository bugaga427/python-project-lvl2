from gendiff.engine import generate_diff


def test_yaml():
    before = 'tests/fixtures/yaml_before.yaml'
    after = 'tests/fixtures/yaml_after.yaml'
    result = open("tests/fixtures/diff.txt")
    assert generate_diff(before, after, "stylish") == result.read()


def test_yaml_recursive():
    before = 'tests/fixtures/yaml_recursive_before.yaml'
    after = 'tests/fixtures/yaml_recursive_after.yaml'
    result = open("tests/fixtures/diff_recursive.txt")
    assert generate_diff(before, after, "stylish") == result.read()


def test_yaml_plain():
    before = 'tests/fixtures/yaml_recursive_before.yaml'
    after = 'tests/fixtures/yaml_recursive_after.yaml'
    result = open("tests/fixtures/diff_plain.txt")
    assert generate_diff(before, after, "plain") == result.read()


def test_yaml_json():
    before = 'tests/fixtures/yaml_recursive_before.yaml'
    after = 'tests/fixtures/yaml_recursive_after.yaml'
    result = open("tests/fixtures/diff_json.txt")
    assert generate_diff(before, after, "json") == result.read()
