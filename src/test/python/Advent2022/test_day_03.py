from src.main.python.Advent2022.day_03 import part_one, part_two


def _example_input():
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 157

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 70

    assert actual == expected

