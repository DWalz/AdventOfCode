from __future__ import annotations

import dataclasses
from functools import reduce
import operator
from typing import Iterable, Iterator, Mapping, Tuple


@dataclasses.dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __hash__(self) -> int:
        return hash(self.name)

    @staticmethod
    def parse_ingredient(string: str) -> Ingredient:
        name, _, capacity, _, durability, _, flavor, _, texture, _, calories = string.split()
        return Ingredient(
            name[:-1], 
            int(capacity[:-1]), 
            int(durability[:-1]), 
            int(flavor[:-1]), 
            int(texture[:-1]), 
            int(calories))


def cookie_score_and_calories(ingredients: Mapping[Ingredient, int]) -> Tuple[int, int]:
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for ingredient, amount in ingredients.items():
        capacity += amount * ingredient.capacity
        durability += amount * ingredient.durability
        flavor += amount * ingredient.flavor
        texture += amount * ingredient.texture
        calories += amount * ingredient.calories
    return reduce(operator.mul, map(lambda x: max(x, 0), (capacity, durability, flavor, texture)), 1), calories


def generate_permutation_sum(number_of_items: int, allowed_sum: int, *previous_permutations) -> Iterator[Iterable[int]]:
    if number_of_items == 1:
        yield allowed_sum - sum(previous_permutations)
    else:
        for amount in range(allowed_sum - sum(previous_permutations) + 1):
            for next_amounts in generate_permutation_sum(number_of_items - 1, allowed_sum, *previous_permutations, amount):
                if number_of_items == 2:
                    yield amount, next_amounts
                else:
                    yield amount, *next_amounts


def get_max_cookie_score(ingredients: Iterable[Ingredient], max_amount: int, calorie_amount: int = 0) -> int:
    max_score = 0
    for perm in generate_permutation_sum(len(ingredients), max_amount):
        cookie = dict(zip(ingredients, perm))
        score, calories = cookie_score_and_calories(cookie)
        if calorie_amount and calorie_amount != calories:
            continue
        max_score = max(score, max_score)
    return max_score


def main():
    with open('day15_input.txt', 'r') as file:
        ingredients = [Ingredient.parse_ingredient(ingredient_string) for ingredient_string in file.read().splitlines()]
        print(f'Best cookie score: {get_max_cookie_score(ingredients, 100)}')
        print('Best cookie score with 500 calories', 
            get_max_cookie_score(ingredients, 100, 500))
        


if __name__ == '__main__':
    main()
