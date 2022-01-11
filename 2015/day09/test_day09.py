import pytest
from day09 import get_path_length, find_shortest_path, find_shortest_path_start, Edge


@pytest.fixture
def edges():
    return [
        Edge(['London', 'Dublin'], 464),
        Edge(['London', 'Belfast'], 518),
        Edge(['Dublin', 'Belfast'], 141)
    ]


def test_get_path_length(edges):
    assert get_path_length(edges) == 464 + 518 + 141


# Dublin -> Belfast -> London = 141 + 518; Dublin -> London -> Belfast = 464 + 518
def test_find_shortest_path_start(edges):
    assert find_shortest_path_start('Dublin', [], edges)[1] == 141 + 518


# NOTE: We can't test for the paths itself since they are bi-directional
# (Yes we can but since there are no duplicate path lengths in the tests I don't need to)
def test_find_shortest_path(edges):
    assert find_shortest_path(edges)[1] == 464 + 141
