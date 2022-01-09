import pytest
from day07 import parse_instructions, simulate_network, INSTRUCTION_LUT


@pytest.fixture
def input():
    return '123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i'.splitlines()


def test_parse_input(input):
    assert parse_instructions(input) == (
        [  # wire set instr
            ('x', 123), ('y', 456)
        ], [  # node instr
            (('x', 'y'), INSTRUCTION_LUT['AND'], 'd'),
            (('x', 'y'), INSTRUCTION_LUT['OR'], 'e'),
            (('x', 2), INSTRUCTION_LUT['LSHIFT'], 'f'),
            (('y', 2), INSTRUCTION_LUT['RSHIFT'], 'g'),
            (('x'), INSTRUCTION_LUT['NOT'], 'h'),
            (('y'), INSTRUCTION_LUT['NOT'], 'i')
        ]
    )


def test_simulate_network(input):
    assert simulate_network(*parse_instructions(input)) == {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }
