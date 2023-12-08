from src.main.python.Advent2023.day_08 import part_one, part_two


def _example_input():
    return """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split('\n')


def _example_input_two():
    return """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split('\n')


def _example_input_three():
    return """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 2

    actual_two = part_one(_example_input_two())
    expected_two = 6

    assert actual == expected
    assert actual_two == expected_two


def test_part_two():
    actual = part_two(_example_input_three())
    expected = 6

    assert actual == expected
