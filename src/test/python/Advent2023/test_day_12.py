import pytest

from src.main.python.Advent2023.day_12 import part_one, part_two


def _example_input():
    return """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 21

    assert actual == expected


@pytest.mark.skip
def test_part_two():
    actual = part_two(_example_input())
    expected = 525152

    assert actual == expected
