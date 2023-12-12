from src.main.python.Advent2023.day_11 import part_one, part_two


def _example_input():
    return """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 374

    assert actual == expected


def test_part_two():
    actual10 = part_two(_example_input(), times=10)
    expected10 = 1030
    actual100 = part_two(_example_input(), times=100)
    expected100 = 8410

    assert actual10 == expected10
    assert actual100 == expected100
