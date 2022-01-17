from turtle import distance
import pytest
from day14 import Reindeer, get_distance_after, get_reindeer_distance, get_reindeer_distances, get_reindeer_points


@pytest.fixture
def comet():
    return Reindeer('Comet', 14, 10, 127)


@pytest.fixture
def dancer():
    return Reindeer('Dancer', 16, 11, 162)


def test_reindeer_parse(comet):
    assert Reindeer.parse_from_string(
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.') == comet


@pytest.mark.parametrize('time, distance', [
    (1, 14),
    (10, 140),
    (12, 140),
    (1000, 1120)
])
def test_reindeer_distance_comet(time, comet, distance):
    assert get_distance_after(comet, time) == distance


@pytest.mark.parametrize('time, distance', [
    (1, 16),
    (10, 160),
    (11, 176),
    (138, 176),
    (1000, 1056)
])
def test_reindeer_distance_dancer(time, dancer, distance):
    assert get_distance_after(dancer, time) == distance


def test_get_reindeer_distance(dancer):
    distances = get_reindeer_distance(dancer)
    expected_distances = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 176, 176]
    for expected_distance in expected_distances:
        assert next(distances) == expected_distance


def test_get_reindeers_distances(comet, dancer):
    distances = get_reindeer_distances(comet, dancer)
    expected_distances = [
        {comet: 14, dancer: 16},
        {comet: 28, dancer: 32},
        {comet: 42, dancer: 48},
        {comet: 56, dancer: 64}
    ]
    for expected_distance in expected_distances:
        assert next(distances) == expected_distance


def test_get_reindeer_points(comet, dancer):
    assert get_reindeer_points(comet, dancer, time=1000) == {comet: 312, dancer: 689}