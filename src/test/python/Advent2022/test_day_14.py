from src.main.python.Advent2022.day_14 import part_one, part_two, to_ints


def _input():
    return [[to_ints(y.split(',')) for y in x.split(' -> ')] for x in
            """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()]


def test_day_one():
    expected = 24
    actual = part_one(_input())

    assert expected == actual


def test_part_two():
    expected = 93
    actual = part_two(_input())

    assert expected == actual
