from src.main.python.Advent2022.day_13 import part_one, part_two


def _input():
    return [eval(x) for x in """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines() if x]


def test_part_one():
    expected = 13
    actual = part_one(_input())

    assert actual == expected


def test_part_two():
    expected = 140
    actual = part_two(_input())

    assert actual == expected
