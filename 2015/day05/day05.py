from typing import Callable, Collection


NAUGHTY_PHRASES = ('ab', 'cd', 'pq', 'xy')


def is_nice(text: str) -> bool:
    if any(phrase in text for phrase in NAUGHTY_PHRASES):
        return False
    if len([c for c in text if c in 'aeiou']) < 3:
        return False
    return any(text[i] == text[i+1] for i in range(len(text) - 1))


def is_nice_new(text: str) -> bool:
    if not any(text[i] == text[i + 2] for i in range(len(text) - 2)):
        return False
    return any(text[i] + text[i + 1] in text[i+2:] for i in range(len(text) - 2))


def count_nice_lines(nice_function: Callable, lines: Collection[str]) -> int:
    return sum(int(nice_function(line)) for line in lines)


def main():
    with open('day05_input.txt', 'r') as file:
        lines = file.read().splitlines()
        print(f'Nice lines: {count_nice_lines(is_nice, lines)}')
        print(f'Nice lines (new): {count_nice_lines(is_nice_new, lines)}')


if __name__ == '__main__':
    main()
