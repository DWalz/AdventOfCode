from itertools import permutations
import pytest
from day15 import Ingredient, cookie_score_and_calories, get_max_cookie_score, generate_permutation_sum


@pytest.fixture
def ingredients():
    return (
        Ingredient('Butterscotch', -1, -2, 6, 3, 8),
        Ingredient('Cinnamon', 2, 3, -2, -1, 3)
    )


def test_cookie_score(ingredients): 
    assert cookie_score_and_calories({ingredients[0]: 44, ingredients[1]: 56})[0] == 62842880


def test_cookie_score_negative(ingredients):
    assert cookie_score_and_calories({ingredients[0]: 90, ingredients[1]: 10})[0] == 0


def test_get_max_cookie_score(ingredients):
    assert get_max_cookie_score(ingredients, 100) == 62842880


def test_get_max_cookie_score_calories(ingredients):
    assert get_max_cookie_score(ingredients, 100, 500) == 57600000


def test_generate_permutation_sum():
    expected_perms = (
        (0, 0, 3),
        (0, 1, 2),
        (0, 2, 1),
        (0, 3, 0),
        (1, 0, 2),
        (1, 1, 1),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
        (3, 0, 0)
    )
    for expected_perm, perm in zip(expected_perms, generate_permutation_sum(3, 3)):
        assert expected_perm == perm