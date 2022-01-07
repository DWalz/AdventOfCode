from typing import Callable


def get_present_area(dimensions: str) -> int:
    length, width, height = map(int, dimensions.split('x'))
    return 2 * sum(sides := [length * height, length * width, width * height]) + min(sides)


def get_present_ribbon(dimensions: str) -> int:
    length, width, height = map(int, dimensions.split('x'))
    return 2 * (length + width + height - max(length, width, height)) + length * width * height


def get_total(present_function: Callable, presents) -> int:
    return sum(map(present_function, presents.split('\n')))


def main():
    with open('day02_input.txt', 'r') as file:
        input = file.read()
        print(
            f'Total wrapping paper area: {get_total(get_present_area, input)}')
        print(f'Total ribbon length: {get_total(get_present_ribbon, input)}')


if __name__ == '__main__':
    main()
