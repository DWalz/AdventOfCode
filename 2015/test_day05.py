import pytest
from day05 import is_nice, is_nice_new, count_nice_lines


@pytest.mark.parametrize('text, expected_result', [
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False)
])
def test_is_nice(text, expected_result):
    assert is_nice(text) == expected_result


def test_count_nice_lines():
    assert count_nice_lines(is_nice, [
        'ugknbfddgicrmopn',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb',
        'aaa']) == 2


@pytest.mark.parametrize('text, expected_result', [
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', False)
])
def test_is_nice_new(text, expected_result):
    assert is_nice_new(text) == expected_result


def test_count_nice_new_lines():
    assert count_nice_lines(is_nice_new, [
        'qjhvhtzxzqqjkmpb',
        'xxyxx',
        'uurcxstgmygtbstg',
        'ieodomkazucvgmuy'
    ]) == 2
