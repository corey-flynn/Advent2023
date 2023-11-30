from src.main.python.Advent2022.day_02 import part_one, part_two, rps, ShapeScore


def _sample_input():
    return [x.split() for x in """A Y
B X
C Z""".split('\n')]


def test_rps():
    """wins worth 6, ties worth 3, losses worth zero plus
    rock worth 1, paper worth 2, scissors worth 3
    """
    assert rps(ShapeScore.rock, ShapeScore.paper) == 2 + 6
    assert rps(ShapeScore.rock, ShapeScore.scissors) == 3 + 0
    assert rps(ShapeScore.rock, ShapeScore.rock) == 1 + 3


def test_part_one():
    actual = part_one(_sample_input())
    expected = 15

    assert actual == expected


def test_part_two():
    actual = part_two(_sample_input())
    expected = 12

    assert actual == expected
