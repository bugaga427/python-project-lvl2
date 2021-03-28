from gendiff.engine import generate_diff
from gendiff.formatters.stylish import render as stylish
from gendiff.engine import edit_message
import json


def test_json():
    before = json.load(open("tests/fixtures/json_before.json"))
    after = json.load(open("tests/fixtures/json_after.json"))
    result = open("tests/fixtures/diff.txt")
    print(edit_message(stylish(generate_diff(before, after))))
    assert edit_message(stylish(generate_diff(before, after))) == result.read()


def test_json_recursive():
    before = json.load(open('tests/fixtures/json_recursive_before.json'))
    after = json.load(open('tests/fixtures/json_recursive_after.json'))
    result = open("tests/fixtures/diff_recursive.txt")
    assert edit_message(stylish(generate_diff(before, after))) == result.read()
