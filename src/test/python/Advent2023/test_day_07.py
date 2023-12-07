from src.main.python.Advent2023.day_07 import part_one, part_two


def _example_input():
    return """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 6440

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 5905

    assert actual == expected
