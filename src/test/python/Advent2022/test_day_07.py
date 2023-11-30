from src.main.python.Advent2022.day_07 import part_one, part_two


def _input():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()


def test_day_one():
    expected = 95_437
    actual = part_one(_input())

    assert expected == actual


def test_day_two():
    expected = 24933642
    actual = part_two(_input())

    assert expected == actual
