from src.main.python.Advent2022.day_01 import get_elf_dict, get_n_elves


def _input():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".split('\n')


def _expected_get_elf_dict():
    return {
        0: 6_000,
        1: 4_000,
        2: 11_000,
        3: 24_000,
        4: 10_000,
    }


def test_get_elf_dict():
    elf_list = _input()
    actual = get_elf_dict(elf_list)
    expected = _expected_get_elf_dict()

    assert actual == expected


def test_part_one():
    elf_list = _input()
    actual = get_n_elves(elf_list, 1)
    expected = 24_000

    assert actual == expected


def test_part_two():
    elf_list = _input()
    actual = get_n_elves(elf_list, 3)
    expected = 45_000

    assert actual == expected
