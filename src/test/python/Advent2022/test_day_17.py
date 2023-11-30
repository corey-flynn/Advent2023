from src.main.python.Advent2022.day_17 import part_one, part_two


def _input():
    return """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


def test_part_one():
    expected = 3068
    actual = part_one(_input(), 2022)

    assert expected == actual


# def test_part_two():
#     expected = None
#     actual = part_two(_input(), 2022)
#
#     assert expected == actual
