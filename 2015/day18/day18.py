from __future__ import annotations

from typing import Iterable, List
from dataclasses import dataclass


@dataclass
class LightMatrix2D:
    lights: List[List[int]]
    size_x: int
    size_y: int
    corner_always_on: bool = False

    @staticmethod
    def parse_from_rows_strings(rows_strings: Iterable[str], corner_always_on: bool = False) -> LightMatrix2D:
        size_x = len(rows_strings[0])
        size_y = len(rows_strings)
        lights = [[state == '#' for state in row] for row in rows_strings]
        if corner_always_on:
            lights[0][0] = True
            lights[0][size_x - 1] = True
            lights[size_y - 1][0] = True
            lights[size_y - 1][size_x - 1] = True
        return LightMatrix2D(lights, size_x, size_y, corner_always_on)

    def __repr__(self) -> str:
        return '\n'.join(' '.join(map(lambda x: x and '#' or '.', row)) for row in self.lights)

    def get_light_state(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            return False
        return self.lights[y][x]

    def get_lights_on(self) -> int:
        return sum(sum(row) for row in self.lights)

    def calculate_next_frame(self):
        new_lights = [[False for _ in range(self.size_x)]
                      for _ in range(self.size_y)]
        for x in range(self.size_x):
            for y in range(self.size_y):
                neighboring_light_count = sum(
                    (self.get_light_state(x - 1, y - 1),
                     self.get_light_state(x, y - 1),
                     self.get_light_state(x + 1, y - 1),
                     self.get_light_state(x - 1, y),
                     self.get_light_state(x + 1, y),
                     self.get_light_state(x - 1, y + 1),
                     self.get_light_state(x, y + 1),
                     self.get_light_state(x + 1, y + 1))
                )
                if neighboring_light_count == 3:
                    new_lights[y][x] = True
                elif neighboring_light_count == 2 and self.lights[y][x]:
                    new_lights[y][x] = True
                else:
                    new_lights[y][x] = False
        if self.corner_always_on:
            new_lights[0][0] = True
            new_lights[0][self.size_x - 1] = True
            new_lights[self.size_y - 1][0] = True
            new_lights[self.size_y - 1][self.size_x - 1] = True
        self.lights = new_lights


def main():
    with open('day18_input.txt', 'r') as file:
        lights_string = file.read().splitlines()
        lights = LightMatrix2D.parse_from_rows_strings(lights_string)
        lights_corner = LightMatrix2D.parse_from_rows_strings(
            lights_string, corner_always_on=True)
        for _ in range(100):
            lights.calculate_next_frame()
            lights_corner.calculate_next_frame()
        print('Lights turned ON after 100 iterations:', lights.get_lights_on())
        print('Lights turned ON after 100 iterations (corners always ON):',
              lights_corner.get_lights_on())


if __name__ == '__main__':
    main()
