from src.main.python.Advent2022.day_04 import part_one, part_two, get_range_sets


def _input():
    s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
    print(s)
    return [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in s]


def _sample_ranges():
    return [1, 3], [3, 4], [6, 7], [8, 10]


def test_part_one():
    actual = part_one(_input())
    expected = 2

    assert actual == expected


def test_part_two():
    actual = part_two(_input())
    expected = 4

    assert actual == expected


def test_get_range_sets():
    actual = get_range_sets(*_sample_ranges())
    expected = [{1, 2, 3}, {3, 4}, {6, 7}, {8, 9, 10}]

    assert actual == expected


def test_get_range_sets_small():
    actual = get_range_sets(_sample_ranges()[0], _sample_ranges()[1])
    expected = [{1, 2, 3}, {3, 4}]

    assert actual == expected

