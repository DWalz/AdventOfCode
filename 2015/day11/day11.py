# NOTE: Since I didn't have much time today and I kinda had to rush it, I resolved
# to only doing the brute force approach, that is, generating all possible passwords and
# filtering the valid ones.
# You can optimize this process by generating passwords that have a higher chance
# of being valid: Skip generation of a lot of passwords that have 'i' in them
# by jumping directly to 'j' in the respective 'column'


from typing import Iterator

import re


DOUBLES_PATTERN = re.compile(r'([a-z])\1')


def remove_double_characters(string: str) -> str:
    previous_char = string[0]
    new_string = string[0]
    for c in string[1:]:
        if c == previous_char:
            continue
        new_string += c
        previous_char = c
    return new_string


def next_password(password: str) -> str:
    new_password = ''
    for c in reversed(password):
        if (char_ord := ord(c)) == 122:
            new_password = 'a' + new_password
            continue
        new_password = chr(char_ord + 1) + new_password
        return password[:len(password) - len(new_password)] + new_password
    return new_password


def generate_passwords(start_password: str) -> Iterator[str]:
    password = start_password
    while True:
        yield password
        password = next_password(password)


def is_valid_password(password: str) -> bool:
    if any(c in password for c in 'iol'):
        return False
    matches = re.findall(DOUBLES_PATTERN, password)
    if len(set(matches)) < 2:
        return False
    return any(
        (ord(password[i]) == (ord(password[i + 1]) - 1)) and 
        (ord(password[i]) == (ord(password[i - 1]) + 1)) 
        for i in range(1, len(password) - 1))


def find_next_valid(start_password: str) -> str:
    passwords = generate_passwords(start_password)
    password = next(passwords)
    while not is_valid_password(password := next(passwords)):
        pass
    return password


def main():
    print(
        f'Next valid password after \'hepxcrrq\': {(next_pass := find_next_valid("hepxcrrq"))}')
    print(f'Next valid password after \'{next_pass}\': {find_next_valid(next_pass)}')


if __name__ == '__main__':
    main()