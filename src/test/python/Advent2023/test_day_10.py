from src.main.python.Advent2023.day_10 import part_one, part_two, possible_directions


def _example_input():
    return tuple(""".....
.S-7.
.|.|.
.L-J.
.....""".split('\n'))


def _example_input_two():
    return tuple("""-L|F7
7S-7|
L|7||
-L-J|
L|-JF""".split('\n'))


def _example_input_three():
    return tuple("""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split('\n'))


def _example_input_four():
    return tuple("""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""".split('\n'))


def _example_input_five():
    return tuple("""......................
..F----7F7F7F7F-7.....
..|F--7||||||||FJ.....
..||.FJ||||||||L7.....
.FJL7L7LJLJ||LJ.L-7...
.L--J.L7...LJS7F-7L7..
.....F-J..F7FJ|L7L7L7.
.....L7.F7||L7|.L7L7|.
......|FJLJ|FJ|F7|.LJ.
.....FJL-7.||.||||....
.....L---J.LJ.LJLJ....
......................""".split('\n'))


def _example_input_six():
    return tuple("""......................
.FF7FSF7F7F7F7F7F---7.
.L|LJ||||||||||||F--J.
.FL-7LJLJ||||||LJL-77.
.F--JF--7||LJLJ7F7FJ-.
.L---JF-JLJ.||-FJLJJ7.
.|F|F-JF---7F7-L7L|7|.
.|FFJF7L7F-JF7|JL---7.
.7-L-JL7||F7|L7F-7F7|.
.L.L7LFJ|||||FJL7||LJ.
.L7JLJL-JLJLJL--JLJ.L.
......................""".split('\n'))


def _start_dirs():
    return """.J||
.7SJ
.JF-
.7L7""".split('\n')


def test_possible_dirs():
    actual = {x for x in possible_directions((2, 1), _start_dirs())}
    expected = {(1, 0), (0, -1)}

    assert actual == expected


def test_part_one():
    actual = part_one(_example_input())
    expected = 4
    actual_two = part_one(_example_input_two())
    expected_two = 4
    actual_three = part_one(_example_input_three())
    expected_three = 8

    assert actual == expected
    assert actual_two == expected_two
    assert actual_three == expected_three


def test_part_two():
    actual_four = part_two(_example_input_four())
    expected_four = 4
    actual_five = part_two(_example_input_five())
    expected_five = 8
    actual_six = part_two(_example_input_six())
    expected_six = 10

    assert actual_four == expected_four
    assert actual_five == expected_five
    assert actual_six == expected_six
