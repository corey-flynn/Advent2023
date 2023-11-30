from src.main.python.Advent2022.day_18 import part_one, part_two


def _input():
    return [[int(y) for y in x.split(',')] for x in """1,1,1
2,1,1""".splitlines()]


def _input_large():
    return [[int(y) for y in x.split(',')] for x in """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()]


def test_part_one():
    expected = 10
    actual = part_one(_input())

    assert expected == actual


def test_part_one_large():
    expected = 64
    actual = part_one(_input_large())

    assert expected == actual


def test_part_two():
    expected = None
    actual = part_two(_input_large())

    assert expected == actual
