from src.main.python.Advent2022.day_20 import part_one, part_two


def _input():
    return [int(x) for x in """1
2
-3
3
-2
0
4""".splitlines()]


def test_part_one():
    expected = 3
    actual = part_one(_input())

    assert expected == actual


def test_part_two():
    expected = 1_623_178_306
    actual = part_two(_input())

    assert expected == actual
