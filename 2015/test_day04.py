import pytest
from day04 import get_hash_with_prefix


@pytest.mark.parametrize('key, expected_answer', [
    (b'abcdef', 609043),
    (b'pqrstuv', 1048970)
])
def test_hash_with_prefix(key, expected_answer):
    assert get_hash_with_prefix(key, '00000') == expected_answer
