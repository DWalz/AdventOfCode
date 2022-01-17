from __future__ import annotations

import dataclasses
from typing import Iterable, Iterator, Mapping


@dataclasses.dataclass
class Reindeer():
    name: str
    speed: int
    flying_time: int
    resting_time: int

    @staticmethod
    def parse_from_string(reindeer_string: str) -> Reindeer:
        name, _, _, speed_str, _, _, flying_time_str, _, _, _, _, _, _, restring_time_str, _ = reindeer_string.split()
        return Reindeer(name, int(speed_str), int(flying_time_str), int(restring_time_str))

    def __hash__(self) -> int:
        return hash(self.name)


def get_distance_after(reindeer: Reindeer, time: int) -> int:
    cycles, remaining_time = divmod(time, reindeer.flying_time + reindeer.resting_time)
    return cycles * reindeer.speed * reindeer.flying_time + \
        reindeer.speed * min(reindeer.flying_time, remaining_time)


def get_reindeer_distance(reindeer: Reindeer) -> Iterator[int]:
    is_flying = True
    cycle_time = reindeer.flying_time
    distance = 0
    while True:
        distance += reindeer.speed if is_flying else 0
        yield distance
        cycle_time -= 1
        if not cycle_time:
            cycle_time = reindeer.resting_time if is_flying else reindeer.flying_time
            is_flying = not is_flying



def get_reindeer_distances(*reindeers: Iterable[Reindeer]) -> Iterator[Mapping[Reindeer, int]]:
    reindeer_distance_generators = {reindeer: get_reindeer_distance(reindeer) for reindeer in reindeers}
    while True:
        yield {reindeer: next(reindeer_generator) for reindeer, reindeer_generator in reindeer_distance_generators.items()}


def get_reindeer_points(*reindeers: Iterable[Reindeer], time: int) -> Mapping[Reindeer, int]:
    distances = get_reindeer_distances(*reindeers)
    points = {reindeer: 0 for reindeer in reindeers}
    for _ in range(time):
        time_distances = next(distances)
        max_distance = max(time_distances.values())
        for reindeer, distance in time_distances.items():
            if distance == max_distance:
                points[reindeer] += 1
    return points


def main():
    with open('day14_input.txt', 'r') as file:
        reindeers = [Reindeer.parse_from_string(string) for string in file.read().splitlines()]
        print(f'Max distance after 2503 seconds: {max(map(lambda reindeer: get_distance_after(reindeer, time=2503), reindeers))}')
        print(f'Max points after 2503 seconds: {max(get_reindeer_points(*reindeers, time=2503).values())}')


if __name__ == '__main__':
    main()