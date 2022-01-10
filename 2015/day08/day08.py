def get_escape_character_difference(*args: str):
    diff = 0
    for text in args:
        diff += len(text) - len(eval(text))
    return diff


def get_representation_difference(*args: str):
    diff = 0
    for text in args:
        diff += text.count('\\') + text.count('"') + 2
    return diff


def main():
    with open('day08_input.txt', 'r') as file:
        print('Difference string literals -> string print: ',
              get_escape_character_difference(*file.read().splitlines()))

    with open('day08_input.txt', 'r') as file:
        print('Difference string literals -> string representation: ',
              get_representation_difference(*file.read().splitlines()))


if __name__ == '__main__':
    main()
