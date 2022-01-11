from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Edge:
    nodes: List[str]
    distance: int

    @staticmethod
    def parse_edge(text: str) -> Edge:
        nodes, distance = text.split(' = ')
        return Edge(nodes.split(' to '), int(distance))


# NOTE: Since we know that each node is connected to every other node in the
# graph, we can skip finding Hamiltonian paths.
# NOTE: This is just the brute force approach since Held-Karp algorithm ist just
# marginally faster for such a small set of nodes. For bigger node sets Held-Karp
# definitely becomes more interesting, or even heuristic approaches
def find_shortest_path_start(start: str, path: List[Edge], edges: List[Edge]):
    if len(edges) == 1:
        path.append(edges[0])
        return path
    next_edges = [edge for edge in edges if start in edge.nodes]
    new_edges = [edge for edge in edges if start not in edge.nodes]
    possible_paths = []
    for next_edge in next_edges:
        new_start = next_edge.nodes[0] if next_edge.nodes[0] != start else next_edge.nodes[1]
        possible_paths.append(find_shortest_path_start(
            new_start, path + [next_edge], new_edges))
    return min(possible_paths, key=get_path_length)


def find_longest_path_start(start: str, path: List[Edge], edges: List[Edge]):
    if len(edges) == 1:
        path.append(edges[0])
        return path
    next_edges = [edge for edge in edges if start in edge.nodes]
    new_edges = [edge for edge in edges if start not in edge.nodes]
    possible_paths = []
    for next_edge in next_edges:
        new_start = next_edge.nodes[0] if next_edge.nodes[0] != start else next_edge.nodes[1]
        possible_paths.append(find_longest_path_start(
            new_start, path + [next_edge], new_edges))
    return max(possible_paths, key=get_path_length)


def find_shortest_path(edges: List[Edge]) -> Tuple[List[Edge], int]:
    nodes = set(sum((edge.nodes for edge in edges), start=[]))
    shortest_paths = [find_shortest_path_start(
        node, [], edges) for node in nodes]
    distances = [(path, get_path_length(path)) for path in shortest_paths]
    return min(distances, key=lambda x: x[1])


def find_longest_path(edges: List[Edge]) -> Tuple[List[Edge], int]:
    nodes = set(sum((edge.nodes for edge in edges), start=[]))
    shortest_paths = [find_longest_path_start(
        node, [], edges) for node in nodes]
    distances = [(path, get_path_length(path)) for path in shortest_paths]
    return max(distances, key=lambda x: x[1])


def get_path_length(path: List[Edge]):
    return sum(edge.distance for edge in path)


def main():
    with open('day09_input.txt', 'r') as file:
        edges = [Edge.parse_edge(line) for line in file.read().splitlines()]
        _, shortest_distance = find_shortest_path(edges)
        _, longest_distance = find_longest_path(edges)
        print(f'Shortest Path: {shortest_distance} units long.')
        print(f'Longest Path: {longest_distance} units long.')


if __name__ == '__main__':
    main()
