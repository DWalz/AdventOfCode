import pytest
from day16 import match_aunts, parse_aunt


@pytest.fixture
def aunts():
    return [
        {'aunt_number': 1, 'a': 4, 'b': 2},
        {'aunt_number': 2, 'a': 3, 'b': 6},
        {'aunt_number': 3, 'a': 3, 'c': 2}
    ]


@pytest.mark.parametrize('aunt_string, expected_aunt', [
    ('Sue 1: cars: 9, akitas: 3, goldfish: 0',
     {'aunt_number': 1, 'cars': 9, 'akitas': 3, 'goldfish': 0}),
    ('Sue 2: akitas: 9, children: 3, samoyeds: 9', 
     {'aunt_number': 2, 'akitas': 9, 'children': 3, 'samoyeds': 9}),
    ('Sue 3: trees: 6, cars: 6, children: 4', 
     {'aunt_number': 3, 'trees': 6, 'cars': 6, 'children': 4}),
])
def test_parse_aunt(aunt_string, expected_aunt):
    assert parse_aunt(aunt_string) == expected_aunt


def test_match_aunts(aunts):
    assert set(match_aunts({'a': 3, 'b': 6, 'c': 2}, aunts)) == {2, 3}


def test_match_aunts_greater_fewer(aunts):
    assert match_aunts({'a': 3, 'b': 6, 'c': 2}, aunts, ['a'], ['b']) == [1]
