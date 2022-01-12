import re
from typing import Generator, Iterator, Union


REPEATED_CHARACTER_PATTERN = re.compile(r'(.)\1*')


def look_and_say(text: str) -> str:
    new_number_string = ''
    for match in REPEATED_CHARACTER_PATTERN.finditer(text):
        new_number_string += str(match.end() - match.start())
        new_number_string += match.group()[0]
    return new_number_string


def look_and_say_chain(start_text: str, iterations: int) -> str:
    for _ in range(iterations):
        start_text = look_and_say(start_text)
    return start_text


def look_and_say_chain_generator(start_text: int) -> Iterator[int]:
    yield start_text
    while True:
        start_text = look_and_say(start_text)
        yield start_text


def main():
    print(
        f'\'1113222113\' after 40 iterations: {len(look_and_say_chain("1113222113", 40))} chars long')
    print(
        f'\'1113222113\' after 50 iterations: {len(look_and_say_chain("1113222113", 50))} chars long')


if __name__ == '__main__':
    main()
