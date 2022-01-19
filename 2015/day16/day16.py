from dataclasses import dataclass
from typing import Dict, Iterable, List


AuntProperties = Dict[str, int]


def parse_aunt(aunt_string: str) -> AuntProperties:
    aunt_number_string, aunt_properties_string = aunt_string.split(': ', maxsplit=1)
    aunt_properties = {'aunt_number': int(aunt_number_string.split()[1])}
    for property_string in aunt_properties_string.split(', '):
        property_name, property_value = property_string.split(': ')
        aunt_properties[property_name] = int(property_value)
    return aunt_properties



def match_aunts(properties: AuntProperties, aunts: Iterable[AuntProperties], 
               properties_greater: List[str] = [], properties_fewer: List[str] = []) -> List[int]:
    aunt_numbers = []
    for aunt in aunts:
        for property, value in aunt.items():
            if property == 'aunt_number': 
                continue
            if property in properties_greater:
                if not value > properties[property]:
                    break
                else: 
                    continue
            elif property in properties_fewer:
                if not value < properties[property]:
                    break
                else:
                    continue
            elif properties[property] != value:
                break
        else:
            aunt_numbers.append(aunt['aunt_number'])
    return aunt_numbers


def main():
    with open('day16_input.txt', 'r') as file:
        aunts = [parse_aunt(line) for line in file.read().splitlines()]
        properties = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        print(f'Aunts with properties: {match_aunts(properties, aunts)}')
        print('Aunts with properties (greater & fewer):',
            match_aunts(properties, aunts, ["cats", "trees"], ["pomeranians", "goldfish"]))


if __name__ == '__main__':
    main()