from src.main.python.Advent2023.day_01 import part_one, part_two


def _example_input():
    return """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split()


def _example_input_two():
    return """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split()


def test_part_one():
    actual = part_one(_example_input())
    expected = 142  # change with actual example solution

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input_two())
    expected = 281  # change with actual example solution

    assert actual == expected
