import json

from gendiff.engine import generate_diff


def test_json():
    before = json.load(open("tests/fixtures/json_before.json"))
    after = json.load(open("tests/fixtures/json_after.json"))
    result = open("tests/fixtures/json_diff.txt")
    assert generate_diff(before, after) == result.read()
