from src.main.python.Advent2022.day_05 import part_one, part_two


def _input():
    r = """    [D]     
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()
    return r[:4], r[5:]


def test_part_one():
    expected = 'CMZ'
    actual = part_one(*_input())

    assert expected == actual


def test_part_two():
    expected = 'MCD'
    actual = part_two(*_input())

    assert expected == actual

