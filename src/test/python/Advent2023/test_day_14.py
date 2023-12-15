from src.main.python.Advent2023.day_14 import part_one, part_two


def _example_input():
    return """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 136

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 64

    assert actual == expected
