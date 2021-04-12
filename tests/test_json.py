from gendiff.engine import get_diff
from gendiff.formatters.stylish import render as stylish
from gendiff.formatters.plain import render as plain
from gendiff.formatters.json import render as json_format
import json


def test_json():
    before = json.load(open("tests/fixtures/json_before.json"))
    after = json.load(open("tests/fixtures/json_after.json"))
    result = open("tests/fixtures/diff.txt")
    assert get_diff(before, after, stylish) == result.read()


def test_json_recursive():
    before = json.load(open('tests/fixtures/json_recursive_before.json'))
    after = json.load(open('tests/fixtures/json_recursive_after.json'))
    result = open("tests/fixtures/diff_recursive.txt")
    assert get_diff(before, after, stylish) == result.read()


def test_json_plain():
    before = json.load(open('tests/fixtures/json_recursive_before.json'))
    after = json.load(open('tests/fixtures/json_recursive_after.json'))
    result = open("tests/fixtures/diff_plain.txt")
    assert get_diff(before, after, plain) == result.read()


def test_json_json():
    before = json.load(open('tests/fixtures/json_recursive_before.json'))
    after = json.load(open('tests/fixtures/json_recursive_after.json'))
    result = open("tests/fixtures/diff_json.txt")
    assert get_diff(before, after, json_format) == result.read()
