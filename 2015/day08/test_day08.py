import pytest
from day08 import get_escape_character_difference, get_representation_difference


@pytest.mark.parametrize('text, expected_difference', [
    (r'""', 2),
    (r'"abc"', 2),
    (r'"aaa\"aaa"', 3),
    (r'"\x27"', 5),
])
def test_escape_character_difference(text, expected_difference):
    assert get_escape_character_difference(text) == expected_difference


def test_escape_character_difference_multiple():
    lines = (r'""', r'"abc"', r'"\x27"')
    assert get_escape_character_difference(*lines) == 9


@pytest.mark.parametrize('text, expected_difference', [
    (r'""', 4),
    (r'"abc"', 4),
    (r'"aaa\"aaa"', 6),
    (r'"\x27"', 5)
])
def test_representation_difference(text, expected_difference):
    assert get_representation_difference(text) == expected_difference


def test_representation_difference_multiple():
    lines = (r'""', r'"abc"', r'"\x27"')
    assert get_representation_difference(*lines) == 13
