from src.main.python.Advent2022.day_08 import part_one, part_two


def _input():
    return [[int(y) for y in x] for x in """30373
25512
65332
33549
35390""".splitlines()]


def test_part_one():
    expected = 21
    actual = part_one(_input())

    assert expected == actual


def test_part_two():
    expected = 8
    actual = part_two(_input())

    assert expected == actual
