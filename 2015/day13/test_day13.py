import pytest
from day13 import get_happiness_table, calculate_happiness, get_max_happiness


@pytest.fixture
def happiness_table():
    return {
        'Alice': {
            'Bob': 54,
            'Carol': -79,
            'David': -2
        },
        'Bob': {
            'Alice': 83,
            'Carol': -7,
            'David': -63
        },
        'Carol': {
            'Alice': -62,
            'Bob': 60,
            'David': 55
        },
        'David': {
            'Alice': 46,
            'Bob': -7,
            'Carol': 41
        },
    }


def test_get_happiness_table(happiness_table):
    strings = [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.'
    ]
    assert get_happiness_table(strings) == happiness_table


def test_calculate_happiness(happiness_table):
    assert calculate_happiness(['Carol', 'Bob', 'David', 'Alice'], happiness_table) == \
        happiness_table['Carol']['Bob'] + happiness_table['Bob']['Carol'] + \
        happiness_table['David']['Bob'] + happiness_table['Bob']['David'] + \
        happiness_table['David']['Alice'] + happiness_table['Alice']['David'] + \
        happiness_table['Carol']['Alice'] + happiness_table['Alice']['Carol']


def test_get_max_happiness(happiness_table):
    assert get_max_happiness(happiness_table) == 330