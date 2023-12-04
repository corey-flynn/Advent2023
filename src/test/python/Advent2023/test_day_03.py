from src.main.python.Advent2023.day_03 import part_one, part_two


def _example_input():
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 4_361

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 467_835

    assert actual == expected
