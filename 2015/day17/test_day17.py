from day17 import generate_eggnog_combinations


def test_generate_eggnogg_combinations():
    containers = [20, 15, 10, 5, 5]
    expected_combinations = [
        (20, 5),
        (20, 5),
        (15, 10),
        (15, 5, 5)
    ]
    for combination, expected_combination in zip(generate_eggnog_combinations(25, containers), expected_combinations):
        assert set(combination) == set(expected_combination)


def test_generate_eggnogg_combinations_minimal():
    containers = [20, 15, 10, 5, 5]
    expected_combinations = [
        (20, 5),
        (20, 5),
        (15, 10)
    ]
    for combination, expected_combination in zip(
            generate_eggnog_combinations(25, containers, count_minimal=True), expected_combinations):
        assert set(combination) == set(expected_combination)
