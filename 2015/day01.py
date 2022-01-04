def calculate_floor(floor_coding: str) -> int:
    return floor_coding.count('(') - floor_coding.count(')')


def floor_numbers(floor_coding: str) -> int:
    floor = 0
    for i, instruction in enumerate(floor_coding):
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
        yield i, floor


def filter_char(char):
    return char == '(' or char == ')'


def main():
    with open('day01_input.txt', 'r') as input_file:
        text = input_file.read()
        input_sanitized = ''.join(filter(filter_char, text))
        print(calculate_floor(text))
        for position, floor in floor_numbers(text):
            if floor == -1:
                print(f'Entering basement at: {position + 1}')
                break


if __name__ == '__main__':
    main()
