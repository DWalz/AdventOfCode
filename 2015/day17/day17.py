from typing import Iterable, Iterator, List, Tuple
from itertools import chain, combinations


def generate_eggnog_combinations(
        total_eggnogg: int,
        containers: Iterable[int],
        count_minimal: bool = False) -> Iterator[Tuple[int]]:
    containers = list(containers)
    for l in range(1, len(containers) + 1):
        found_combination = False
        for possible_permutation in combinations(containers, l):
            if sum(possible_permutation) == total_eggnogg:
                found_combination = True
                yield possible_permutation
        if count_minimal and found_combination:
            break


def main():
    with open('day17_input.txt', 'r') as file:
        containers = [int(line) for line in file.read().splitlines()]
        print('Number of possible container combinations to store 150 l eggnogg:',
              len(list(generate_eggnog_combinations(150, containers))))
        print('Number of container combinations to store 150 l eggnogg with the least amount of containers:',
              len(list(generate_eggnog_combinations(150, containers, count_minimal=True))))


if __name__ == '__main__':
    main()
