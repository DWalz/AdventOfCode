import pytest
from day18 import LightMatrix2D


@pytest.fixture
def lights_step0():
    return LightMatrix2D([
        [False, True, False, True, False, True],
        [False, False, False, True, True, False],
        [True, False, False, False, False, True],
        [False, False, True, False, False, False],
        [True, False, True, False, False, True],
        [True, True, True, True, False, False]
    ], 6, 6)


@pytest.fixture
def lights_step0_corner_on():
    return LightMatrix2D([
        [True, True, False, True, False, True],
        [False, False, False, True, True, False],
        [True, False, False, False, False, True],
        [False, False, True, False, False, False],
        [True, False, True, False, False, True],
        [True, True, True, True, False, True]
    ], 6, 6, corner_always_on=True)


@pytest.fixture
def lights_step1():
    return LightMatrix2D([
        [False, False, True, True, False, False],
        [False, False, True, True, False, True],
        [False, False, False, True, True, False],
        [False, False, False, False, False, False],
        [True, False, False, False, False, False],
        [True, False, True, True, False, False]
    ], 6, 6)


@pytest.fixture
def lights_step1_corner_on():
    return LightMatrix2D([
        [True, False, True, True, False, True],
        [True, True, True, True, False, True],
        [False, False, False, True, True, False],
        [False, False, False, False, False, False],
        [True, False, False, False, True, False],
        [True, False, True, True, True, True]
    ], 6, 6, corner_always_on=True)


@pytest.fixture
def lights_step4():
    return LightMatrix2D([
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, True, True, False, False],
        [False, False, True, True, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False]
    ], 6, 6)


def test_light_matrix_parse(lights_step0):
    assert LightMatrix2D.parse_from_rows_strings(
        '.#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..'.splitlines()
    ).lights == lights_step0.lights


def test_light_matrix_get_light(lights_step0):
    assert lights_step0.get_light_state(0, 0) == False
    assert lights_step0.get_light_state(3, 5) == True


def test_light_matrix_count_lights(lights_step0):
    assert lights_step0.get_lights_on() == 15


def test_light_matrix_next_frame(lights_step0, lights_step1):
    lights_step0.calculate_next_frame()
    assert lights_step0.lights == lights_step1.lights


def test_light_matrix_next_four_frames(lights_step0, lights_step4):
    lights_step0.calculate_next_frame()
    lights_step0.calculate_next_frame()
    lights_step0.calculate_next_frame()
    lights_step0.calculate_next_frame()
    assert lights_step0.lights == lights_step4.lights


def test_light_matrix_next_five_frames_corners_on(lights_step0_corner_on, lights_step1_corner_on):
    lights_step0_corner_on.calculate_next_frame()
    assert lights_step0_corner_on.lights == lights_step1_corner_on.lights
