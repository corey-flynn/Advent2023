from src.main.python.Advent2022.day_12 import part_one, part_two


def _input():
    return [[ord(y) for y in x] for x in """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()]


def test_part_one():
    expected = 31
    actual = part_one(_input())

    assert expected == actual


def test_part_two():
    expected = 29
    actual = part_two(_input())

    assert expected == actual
