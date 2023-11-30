from src.main.python.Advent2022.day_21 import part_one, part_two


def _input():
    return {x.split(': ')[0]: x.split(': ')[1] for x in """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()}


def test_part_one():
    expected = 152
    actual = part_one(_input())

    assert expected == actual


def test_part_two():
    expected = 301
    actual = part_two(_input())

    assert expected == actual
