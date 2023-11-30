from src.main.python.Advent2022.day_09 import part_one, part_two


def _input1():
    return [x.split() for x in """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()]


def _input2():
    return [x.split() for x in """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()]


def test_part_one():
    expected = 13
    actual = part_one(_input1())

    assert expected == actual


def test_part_two():
    expected = 1
    actual = part_two(_input1())

    assert expected == actual


def test_part_two_large():
    expected = 36
    actual = part_two(_input2())

    assert expected == actual
