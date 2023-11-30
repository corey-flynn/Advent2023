import pytest

from src.main.python.Advent2022.day_19 import part_one, part_two


def _input():
    return """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()


# these take a while to run, marking skip to not tax my githooks on every push
@pytest.mark.skip
def test_part_one():
    expected = 33
    actual = part_one(_input())

    assert expected == actual


@pytest.mark.skip
def test_part_two():
    expected = 56 * 62
    actual = part_two(_input())

    assert expected == actual
