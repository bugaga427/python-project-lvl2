from gendiff.engine import generate_diff


def test_json():
    before = "tests/fixtures/json_before.json"
    after = "tests/fixtures/json_after.json"
    result = open("tests/fixtures/diff.txt")
    assert generate_diff(before, after, "stylish") == result.read()


def test_json_recursive():
    before = 'tests/fixtures/json_recursive_before.json'
    after = 'tests/fixtures/json_recursive_after.json'
    result = open("tests/fixtures/diff_recursive.txt")
    assert generate_diff(before, after, "stylish") == result.read()


def test_json_plain():
    before = 'tests/fixtures/json_recursive_before.json'
    after = 'tests/fixtures/json_recursive_after.json'
    result = open("tests/fixtures/diff_plain.txt")
    assert generate_diff(before, after, "plain") == result.read()


def test_json_json():
    before = 'tests/fixtures/json_recursive_before.json'
    after = 'tests/fixtures/json_recursive_after.json'
    result = open("tests/fixtures/diff_json.txt")
    assert generate_diff(before, after, "json") == result.read()
