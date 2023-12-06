from src.main.python.Advent2023.day_06 import part_one, part_two


def _example_input():
    return """Time:      7  15   30
Distance:  9  40  200""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 288

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 71_503

    assert actual == expected
