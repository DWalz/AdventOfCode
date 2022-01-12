import pytest
from day10 import look_and_say, look_and_say_chain, look_and_say_chain_generator


@pytest.mark.parametrize('number, expected_look_and_say', [
    ('1', '11'),
    ('11', '21'),
    ('111221', '312211'),
    ('312211', '13112221'),
    ('13112221', '1113213211'),
])
def test_look_and_say(number, expected_look_and_say):
    assert look_and_say(number) == expected_look_and_say


@pytest.mark.parametrize('number, iterations, expected_result', [
    ('1', 3, '1211'),
    ('13', 2, '3113'),
    ('11', 1, '21'),
    ('111221', 3, '1113213211')
])
def test_look_and_say_chain(number, iterations, expected_result):
    assert look_and_say_chain(number, iterations) == expected_result


def test_look_and_say_chain_generator():
    generator = look_and_say_chain_generator('1')
    assert next(generator) == '1'
    assert next(generator) == '11'
    assert next(generator) == '21'
    assert next(generator) == '1211'
    assert next(generator) == '111221'
    assert next(generator) == '312211'
