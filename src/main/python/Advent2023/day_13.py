"""
https://adventofcode.com/2023/day/13
"""
from itertools import groupby
from typing import List

from src.main.python.utilities import LOGGER, timing


def parse(lines: List[str]) -> List[List[List[str]]]:
    return [list(map(list, group)) for key, group in groupby(lines, bool) if key]


def find_mirror(map_: List[List[str]], diff_count: int = 0) -> int:
    """
    Find the mirror point in a 'map' where the number of different characters
    on either side of the point is equal to diff_count.

    The mirror point is an index splitting the 'map' into left and right parts
    such that the reversed left part has a specified number of character
    differences compared to the right part.
    """
    map_len = len(map_)
    for i in range(1, map_len):
        left, right = map_[:i], map_[i:]
        min_size = min(len(x) for x in (left, right))
        diffs = 0
        for y, line in enumerate(left[-min_size:]):
            for x, val in enumerate(line):
                diffs += int(val != right[:min_size][::-1][y][x])
                if diffs > diff_count:
                    break
        if diffs == diff_count:
            return i
    return 0


@timing
def part_one(lines) -> int:
    count = 0
    for map_ in parse(lines):
        count += (
                find_mirror(map_) * 100
                or find_mirror([x for x in zip(*map_)])
        )
    return count


@timing
def part_two(lines) -> int:
    count = 0
    for map_ in parse(lines):
        count += (
                find_mirror(map_, 1) * 100
                or find_mirror([x for x in zip(*map_)], 1)
        )
    return count


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day13.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 27_502 // 0.0068 sec
    LOGGER.info(part_two(input_))  # 31_947 // 0.0087 sec
