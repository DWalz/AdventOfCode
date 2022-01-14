import pytest
from day12 import sum_json_object, sum_json_ignore


@pytest.mark.parametrize('json_string, expected_sum', [
    ('[1,2,3]', 6),
    ('{"a":2,"b":4}', 6),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[]', 0)
])
def test_sum_json(json_string, expected_sum):
    assert sum_json_object(json_string) == expected_sum


@pytest.mark.parametrize('json_string_ignore, expected_sum', [
    ('[1,2,3]', 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6)
])
def test_sum_json_ignore(json_string_ignore, expected_sum):
    assert sum_json_ignore(json_string_ignore, ['red']) == expected_sum
