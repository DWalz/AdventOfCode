import re
import json
from typing import Iterable


NUMBER_PATTERN = re.compile(r'(-?\d+)\s*[,\]}]')


# It's much faster to just match numbers in items, we know number values in json
# are only followed by comma (,), ], or } (aside whitespace)
def sum_json_object(json_string: str):
    return sum(int(match.group(1)) for match in re.finditer(NUMBER_PATTERN, json_string))


def sum_json_ignore(json_string: str, ignore_properties: Iterable[str]):
    objects = [json.loads(json_string), ]
    next_objects = []
    json_sum = 0
    while objects:
        for elem in objects:
            if type(elem) == dict:
                dict_values = []
                for value in elem.values():
                    if value in ignore_properties:
                        print
                        break
                    dict_values.append(value)
                else: # If we broke out of the inner loop we don't get here and ignore the entire dict
                    objects += dict_values
            if type(elem) == list:
                for item in elem:
                    next_objects.append(item)
            if type(elem) == int:
                json_sum += elem
        objects, next_objects = next_objects, []
    return json_sum


def main():
    with open('day12_input.txt', 'r') as file:
        json_input = file.read()
        print(f'Total sum of numbers: {sum_json_object(json_input)}')
        print(f'Total sum of numbers: {sum_json_object(json_input)}')
        print(f'Total sum of numbers (ignore \'red\'): {sum_json_ignore(json_input, ["red"])}')


if __name__ == '__main__':
    main()