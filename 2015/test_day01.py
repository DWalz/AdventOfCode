from day01 import calculate_floor, floor_numbers


def test_one_floor_up():
    assert calculate_floor('(') == 1


def test_one_floor_down():
    assert calculate_floor(')') == -1


def test_floor_movement_result_0():
    assert calculate_floor('(())') == 0
    assert calculate_floor('()()') == 0


def test_floor_movement_positive():
    assert calculate_floor('(((') == 3
    assert calculate_floor('(()(()(') == 3
    assert calculate_floor('))(((((') == 3


def test_floor_movement_negative():
    assert calculate_floor('))(') == -1
    assert calculate_floor(')())())') == -3
    assert calculate_floor(')))') == -3


def test_floor_numbers_simple():
    floor_code = '()()'
    seq = floor_numbers(floor_code)
    for i in range(len(floor_code)):
        assert (i, calculate_floor(floor_code[:i + 1])) == next(seq)


def test_floor_numbers_complex():
    floor_code = '(((())))()((((((((())()(()))'
    seq = floor_numbers(floor_code)
    for i in range(len(floor_code)):
        assert (i, calculate_floor(floor_code[:i + 1])) == next(seq)
