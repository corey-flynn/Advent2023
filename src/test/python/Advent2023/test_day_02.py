from src.main.python.Advent2023.day_02 import part_one, part_two


def _example_input():
    return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 8

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 2_286

    assert actual == expected
