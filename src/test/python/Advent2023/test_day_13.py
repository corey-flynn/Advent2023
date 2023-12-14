from src.main.python.Advent2023.day_13 import part_one, part_two, parse, find_mirror


def _example_input():
    return """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split('\n')


def unit_one():
    return """.####..#.#.
..##..#.#..
.......#..#
#.##.##.###
#######.##.
######..#..
......#..##
#.##.###..#
.####..#.##
######..##.
#######.#..
#######.#..
######...#.
.####..#.##
#.##.###..#""".split('\n')


def test_part_one():
    actual = part_one(_example_input())
    expected = 405

    assert actual == expected


def test_unit_one():
    actual = find_mirror([x for x in zip(*parse(unit_one())[0])])
    expected = 3

    assert actual == expected


def test_part_two():
    actual = part_two(_example_input())
    expected = 400

    assert actual == expected
