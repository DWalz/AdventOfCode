import operator
import ctypes
from typing import Callable, Iterable, List, Tuple, Union


WireName = str
Inputs = Iterable[Union[WireName, int]]
NodeInstruction = Tuple[Inputs, Callable, WireName]


INSTRUCTION_LUT = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
    'NOT': operator.invert,
    'ID': lambda x: x
}


def simulate_network(node_instructions: Iterable[NodeInstruction]):
    # `ctypes` doesn't allow for bit manimpulation on `c_ushort` so we have to
    # store them as int for the bit operations and cut eventual overflow and
    # interpretation as negative numbers (caused by NOT and RSHIFT) by double converting
    # - not the most satisfying solution

    wires = dict()
    node_instructions = list(node_instructions)

    # Nodes will only be consumed when the inputs are all available (in the `wires` dict)
    previous_len = -1
    while node_instructions:
        if previous_len == len(node_instructions):
            raise RuntimeError(
                'Network (partly) unreachable. Are some parts not connected?')
        previous_len = len(node_instructions)

        for node in node_instructions:
            inputs, function, output = node
            if any(type(input) == str and input not in wires for input in inputs):
                continue

            inputs = ((wires[input] if type(input) == str else input)
                      for input in inputs)

            wires[output] = ctypes.c_ushort(function(*inputs)).value
            node_instructions.remove(node)

    return wires


def convert_if_number(text: str) -> Union[str, int]:
    return int(text) if text.isdigit() else text


def parse_instructions(instruction_strings: Iterable[str]) -> List[NodeInstruction]:
    node_instructions = []

    for instruction in instruction_strings:
        input, output = instruction.split(' -> ')
        operation = input.split()

        if len(operation) == 1:
            inputs = (convert_if_number(operation[0]),)
            bin_operator = INSTRUCTION_LUT['ID']
        elif len(operation) == 2:
            inputs = (convert_if_number(operation[1]),)
            bin_operator = INSTRUCTION_LUT['NOT']
        else:
            inputs = (convert_if_number(operation[0]),
                      convert_if_number(operation[2]))
            bin_operator = INSTRUCTION_LUT[operation[1]]
        node_instructions.append((inputs, bin_operator, output))

    return node_instructions


def main():
    with open('day07_input.txt', 'r') as file:
        instructions = file.read().splitlines()
        parsed_instructions = parse_instructions(instructions)
        solution = simulate_network(parsed_instructions)

        print(f'Wire a value: {solution["a"]}')

        parsed_instructions = list(
            filter(lambda instruction: instruction[2] != 'b', parsed_instructions))
        parsed_instructions = parsed_instructions + \
            parse_instructions([f'{solution["a"]} -> b'])
        solution2 = simulate_network(parsed_instructions)

        print(f'Wire a value: {solution2["a"]}')


if __name__ == '__main__':
    main()
