from typing import Iterable, Mapping, Tuple
from collections import defaultdict
from itertools import permutations


def calculate_happiness(table: Iterable[str], happiness_table: Mapping[str, Mapping[str, int]]):
    table_len = len(table)
    happiness = 0
    for i in range(len(table)):
        happiness += happiness_table[table[i]][table[(i + 1) % table_len]]
        happiness += happiness_table[table[i]][table[(i - 1) % table_len]]
    return happiness


def get_happiness_table(happiness_strings: Iterable[str], include_neutral: bool = False) -> Mapping[str, Mapping[str, int]]:
    happiness_table = defaultdict(dict)
    for happiness_string in happiness_strings:
        guest_main, _, gain_loose, happiness, _, _, _, _, _, _, guest2 = happiness_string.split()
        happiness_table[guest_main][guest2[:-1]] = int(happiness) * (1 if gain_loose == 'gain' else -1)
    if include_neutral:
        happiness_table['Neutral'] = {}
        for guest in happiness_table.keys():
            happiness_table[guest]['Neutral'] = 0
            happiness_table['Neutral'][guest] = 0
    return happiness_table


def get_max_happiness(happiness_table: Mapping[str, Mapping[str, int]]) -> int:
    return max(map(lambda x: calculate_happiness(x, happiness_table), permutations(happiness_table.keys())))
        


def main():
    with open('day13_input.txt', 'r') as file:
        happiness_instructions = file.read()
        happiness_table = get_happiness_table(happiness_instructions.splitlines())
        print(f'Maximum Happiness: {get_max_happiness(happiness_table)}')
        happiness_table = get_happiness_table(happiness_instructions.splitlines(), True)
        print(f'Maximum Happiness (with Neutral): {get_max_happiness(happiness_table)}')


if __name__ == '__main__':
    main()