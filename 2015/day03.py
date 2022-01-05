from typing import Callable, Iterable, Tuple


DIRECTION_POSITION_CHANGES = {
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0)
}


def get_positions_santa(directions: str = '') -> Iterable[Tuple[int, int]]:
    position = [0, 0]
    yield tuple(position)
    for c in directions:
        change = DIRECTION_POSITION_CHANGES[c]
        position[0] += change[0]
        position[1] += change[1]
        yield tuple(position)


def get_positions_santa_robot(directions: str = '') -> Iterable[Tuple[int, int]]:
    position_santa = [0, 0]
    position_robot = [0, 0]
    yield tuple(position_santa)
    for i, c in enumerate(directions):
        change = DIRECTION_POSITION_CHANGES[c]
        if i & 1:
            position_robot[0] += change[0]
            position_robot[1] += change[1]
            yield tuple(position_robot)
        else:
            position_santa[0] += change[0]
            position_santa[1] += change[1]
            yield tuple(position_santa)


def get_number_of_positions(position_function: Callable, directions: str = '') -> int:
    return len(set(pos for pos in position_function(directions)))


def main():
    with open('day03_input.txt', 'r') as file:
        input = file.read()
        print('Visited houses Year 1 (Santa): '
              f'{get_number_of_positions(get_positions_santa, input)}')
        print('Visited houses Year 2 (Santa + Robot): '
              f'{get_number_of_positions(get_positions_santa_robot, input)}')


if __name__ == '__main__':
    main()
