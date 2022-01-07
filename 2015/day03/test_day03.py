import pytest
from day03 import get_positions_santa, get_positions_santa_robot, get_number_of_positions


@pytest.mark.parametrize('directions, expected_positions', [
    ('', [(0, 0)]),
    ('>', [(0, 0), (1, 0)]),
    ('^', [(0, 0), (0, 1)]),
    ('v', [(0, 0), (0, -1)]),
    ('<', [(0, 0), (-1, 0)]),
    ('>>>v<', [(0, 0), (1, 0), (2, 0), (3, 0), (3, -1), (2, -1)])
])
def test_positions_from_directions(directions, expected_positions):
    positions = get_positions_santa(directions)
    for i, position in enumerate(positions):
        assert position == expected_positions[i]


@pytest.mark.parametrize('directions, expected_positions', [
    ('', [(0, 0)]),
    ('>', [(0, 0), (1, 0)]),
    ('^', [(0, 0), (0, 1)]),
    ('v', [(0, 0), (0, -1)]),
    ('<', [(0, 0), (-1, 0)]),
    ('>>>v<', [(0, 0), (1, 0), (1, 0), (2, 0), (1, -1), (1, 0)]),
    ('^>v<', [(0, 0), (0, 1), (1, 0), (0, 0), (0, 0)]),
    ('^v^v^v^v^v', [(0, 0), (0, 1), (0, -1), (0, 2), (0, -2),
     (0, 3), (0, -3), (0, 4), (0, -4), (0, 5), (0, -5)])
])
def test_positions_from_directions_robot(directions, expected_positions):
    positions = get_positions_santa_robot(directions)
    for i, position in enumerate(positions):
        assert position == expected_positions[i]


@pytest.mark.parametrize('directions, expected_number', [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2)
])
def test_position_numbers_from_directions(directions, expected_number):
    assert get_number_of_positions(
        get_positions_santa, directions) == expected_number
