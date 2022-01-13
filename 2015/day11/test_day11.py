import pytest
from day11 import next_password, generate_passwords, is_valid_password


@pytest.mark.parametrize('password, expected_next_password', [
    ('a', 'b'),
    ('j', 'k'),
    ('z', 'a'),
    ('aa', 'ab'),
    ('az', 'ba'),
    ('abzzz', 'acaaa'),
    ('aaacdefgz', 'aaacdefha')
])
def test_next_password(password, expected_next_password):
    assert next_password(password) == expected_next_password


@pytest.mark.parametrize('password, next_3_passwords', [
    ('a', ['b', 'c', 'd']),
    ('ay', ['az', 'ba', 'bb']),
    ('aaazzy', ['aaazzz', 'aabaaa', 'aabaab'])
])
def test_generate_passwords(password, next_3_passwords):
    passwords = generate_passwords(password)
    assert next(passwords) == password
    assert next(passwords) == next_3_passwords[0]
    assert next(passwords) == next_3_passwords[1]
    assert next(passwords) == next_3_passwords[2]


@pytest.mark.parametrize('password, is_valid', [
    ('hijklmmn', False),
    ('abbceffg', False),
    ('abbcegjk', False)
])
def test_is_valid_password(password, is_valid):
    assert is_valid_password(password) == is_valid
