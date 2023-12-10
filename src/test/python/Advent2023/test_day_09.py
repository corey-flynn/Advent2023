from src.main.python.Advent2023.day_09 import part_one, part_two, sequencer


def _example_input():
    return """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split('\n')


def neg_one_tier():
    return [6, 1, -4, -9, -14, -19, -24, -29, -34, -39, -44, -49, -54, -59, -64, -69, -74, -79, -84, -89, -94]


def test_neg():
    actual = sequencer(neg_one_tier())
    expected = -99

    assert actual == expected


def test_part_one():
    actual = part_one(_example_input())
    expected = 114

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 2

    assert actual == expected
