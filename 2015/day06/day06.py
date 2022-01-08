from typing import Callable, Iterable, List, Union

LightBinaryMatrix = List[List[bool]]
LightBrightnessMatrix = List[List[int]]


def turn_on(lights: LightBinaryMatrix,
            x1: int, y1: int,
            x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        lights[x][y1:y2 + 1] = [True] * (y2 - y1 + 1)


def turn_up(lights: LightBrightnessMatrix,
            x1: int, y1: int,
            x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 1


def turn_off(lights: LightBinaryMatrix,
             x1: int, y1: int,
             x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        lights[x][y1:y2 + 1] = [False] * (y2 - y1 + 1)


def turn_down(lights: LightBrightnessMatrix,
              x1: int, y1: int,
              x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = max(lights[x][y] - 1, 0)


def toggle(lights: LightBinaryMatrix,
           x1: int, y1: int,
           x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = not lights[x][y]


def toggle_brightness(lights: LightBrightnessMatrix,
                      x1: int, y1: int,
                      x2: int, y2: int) -> None:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 2


def count_lights(lights: LightBinaryMatrix) -> int:
    return sum(map(int, sum(lights, start=[])))


def count_brightness(lights: LightBrightnessMatrix) -> int:
    return sum(sum(row) for row in lights)


ORIGINAL_LIGHT_FUNCTIONS = (turn_on, turn_off, toggle)
BRIGHTNESS_LIGHT_FUNCTIONS = (turn_up, turn_down, toggle_brightness)


def follow_instructions(lights: Union[LightBinaryMatrix, LightBrightnessMatrix],
                        instructions: List[str],
                        function_set: Iterable[Callable] = ORIGINAL_LIGHT_FUNCTIONS) -> None:
    for instruction in instructions:
        lights_function = function_set[2]
        pos_idx = [1, 3]
        instruction = instruction.split()

        if instruction[0] == 'turn':
            pos_idx = [2, 4]
            lights_function = function_set[0] if instruction[1] == 'on' else function_set[1]

        pos = f'{instruction[pos_idx[0]]},{instruction[pos_idx[1]]}'.split(',')
        lights_function(lights,
                        int(pos[0]), int(pos[1]),
                        int(pos[2]), int(pos[3]))


def main():
    with open('day06_input.txt', 'r') as file:
        instructions = file.read().splitlines()

        lights = [[False] * 1000 for _ in range(1000)]
        follow_instructions(lights, instructions)

        lights_brightness = [[0] * 1000 for _ in range(1000)]
        follow_instructions(lights_brightness, instructions,
                            function_set=BRIGHTNESS_LIGHT_FUNCTIONS)

        print(f'Total lights on: {count_lights(lights)}')
        print(f'Total brightness: {count_brightness(lights_brightness)}')


if __name__ == '__main__':
    main()
