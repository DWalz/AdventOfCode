# NOTE: I'm using the hashlib library in this one as it's a built-in library.
# I was contemplating writing my own MD5 algorithm but since Python is pretty slow and
# advanced bit manipulation is just tedious to do I don't think doing so is a great idea
# in plain Python.
# I do plan on writing the MD5 algorithm myself, but I'll do so in Cython and create a
# package to use in this task. I believe anything else would be madness.


import hashlib
from typing import Tuple


def get_md5_hashes(secret_key: bytes) -> Tuple[int, bytes]:
    number = 0
    while True:
        number += 1
        yield number, hashlib.md5(secret_key + bytes(str(number), 'utf-8')).digest()


def get_hash_with_prefix(secret_key: bytes, prefix: str) -> int:
    for i, hash in get_md5_hashes(secret_key):
        if hash.hex().startswith(prefix):
            return i


def main():
    key = b'iwrupvqb'
    print(f'Smallest solution for key {key} with prefix 00000: '
          f'{ get_hash_with_prefix(key, "00000") }')
    print(f'Smallest solution for key {key} with prefix 000000: '
          f'{ get_hash_with_prefix(key, "000000") }')


if __name__ == '__main__':
    main()
