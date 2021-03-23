from gendiff.engine import generate_diff
import json


def test_json():
    before = json.load(open("tests/fixtures/json_before.json"))
    after = json.load(open("tests/fixtures/json_after.json"))
    result = open("tests/fixtures/diff.txt")
    assert generate_diff(before, after) == result.read()


def test_json_recursive():
    before = json.load(open('tests/fixtures/json_recursive_before.json'))
    after = json.load(open('tests/fixtures/json_recursive_after.json'))
    result = open("tests/fixtures/diff_recursive.txt")
    assert generate_diff(before, after) == result.read()
