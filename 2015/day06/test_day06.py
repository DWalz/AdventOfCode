import pytest
from day06 import (turn_on, turn_up, turn_off, turn_down, toggle, toggle_brightness,
                   count_lights, count_brightness, follow_instructions, BRIGHTNESS_LIGHT_FUNCTIONS)


@pytest.fixture
def lights():
    return [[False] * 5 for _ in range(5)]


@pytest.fixture
def lights_brightness():
    return[[0] * 5 for _ in range(5)]


def test_lights_turn_on(lights):
    turn_on(lights, 0, 0, 2, 2)
    assert lights == [
        [True, True, True, False, False],
        [True, True, True, False, False],
        [True, True, True, False, False],
        [False] * 5,
        [False] * 5
    ]


def test_lights_turn_up(lights_brightness):
    turn_up(lights_brightness, 0, 0, 2, 2)
    assert lights_brightness == [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    turn_up(lights_brightness, 0, 0, 1, 1)
    assert lights_brightness == [
        [2, 2, 1, 0, 0],
        [2, 2, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


def test_lights_turn_off(lights):
    turn_on(lights, 0, 0, 2, 2)
    turn_off(lights, 0, 0, 1, 1)
    assert lights == [
        [False, False, True, False, False],
        [False, False, True, False, False],
        [True, True, True, False, False],
        [False] * 5,
        [False] * 5
    ]


def test_lights_turn_down(lights_brightness):
    turn_up(lights_brightness, 0, 0, 2, 2)
    assert lights_brightness == [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    turn_down(lights_brightness, 0, 0, 1, 1)
    assert lights_brightness == [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


def test_lights_toggle(lights):
    turn_on(lights, 0, 0, 2, 2)
    toggle(lights, 1, 1, 3, 3)
    assert lights == [
        [True, True, True, False, False],
        [True, False, False, True, False],
        [True, False, False, True, False],
        [False, True, True, True, False],
        [False, False, False, False, False]
    ]


def test_lights_toggle_brightness(lights_brightness):
    toggle_brightness(lights_brightness, 0, 0, 2, 2)
    assert lights_brightness == [
        [2, 2, 2, 0, 0],
        [2, 2, 2, 0, 0],
        [2, 2, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    toggle_brightness(lights_brightness, 0, 0, 1, 1)
    assert lights_brightness == [
        [4, 4, 2, 0, 0],
        [4, 4, 2, 0, 0],
        [2, 2, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


@pytest.mark.parametrize('lights, expected_on', [
    ([[True, False], [True, False]], 2),
    ([[True, True], [True, True], [False, True], [False, False]], 5),
    ([[True, False], [False, False]], 1),
    ([[False, False], [False, False]], 0),
    ([[True, True, True, True], [True, True, True, True]], 8),
    ([], 0)
])
def test_count_lights(lights, expected_on):
    assert count_lights(lights) == expected_on


@pytest.mark.parametrize('lights_brightness, expected_brightness', [
    ([[1, 1, 1, 0, 0],
      [1, 1, 1, 0, 0],
      [1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]], 9),
    ([[0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]], 5),
    ([[4, 4, 0, 0, 0],
      [4, 4, 0, 0, 0],
      [0, 0, 0, 0, 7],
      [0, 0, 0, 3, 0],
      [0, 0, 0, 1, 0]], 27),
])
def test_count_brightness(lights_brightness, expected_brightness):
    assert count_lights(lights_brightness) == expected_brightness


@pytest.mark.parametrize('instructions, expected_result', [
    (['turn on 0,0 through 2,2'], [
        [True, True, True, False, False],
        [True, True, True, False, False],
        [True, True, True, False, False],
        [False] * 5,
        [False] * 5
    ]),
    (['turn on 0,0 through 2,2', 'turn off 0,0 through 1,1'], [
        [False, False, True, False, False],
        [False, False, True, False, False],
        [True, True, True, False, False],
        [False] * 5,
        [False] * 5
    ]),
    (['turn on 0,0 through 2,2', 'toggle 1,1 through 3,3'], [
        [True, True, True, False, False],
        [True, False, False, True, False],
        [True, False, False, True, False],
        [False, True, True, True, False],
        [False, False, False, False, False]
    ])
])
def test_follow_instructions(lights, instructions, expected_result):
    follow_instructions(lights, instructions)
    assert lights == expected_result


@pytest.mark.parametrize('instructions, expected_result', [
    (['turn on 0,0 through 2,2'], [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]),
    (['turn on 0,0 through 2,2', 'turn off 0,0 through 1,1'], [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]),
    (['turn on 0,0 through 2,2', 'toggle 1,1 through 3,3'], [
        [1, 1, 1, 0, 0],
        [1, 3, 3, 2, 0],
        [1, 3, 3, 2, 0],
        [0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0]
    ])
])
def test_follow_instructions_brightness(lights, instructions, expected_result):
    follow_instructions(lights, instructions,
                        function_set=BRIGHTNESS_LIGHT_FUNCTIONS)
    assert lights == expected_result
