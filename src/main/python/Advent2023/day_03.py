"""
https://adventofcode.com/2023/day/3
"""
import re
from collections import defaultdict

from src.main.python.utilities import LOGGER, timing


def adj_parts(a: int, b: int):
    """
    find all parts adjacent to a point (including the point)
    :param a:
    :param b:
    :return:
    """
    for a_ in a-1, a, a+1:
        for b_ in b-1, b, b+1:
            yield a_, b_


def parse(lines, gears=False):
    """
    parse the text, find all symbols (not including digits or .s)
    and yield either values adjacent to the symbol, or if the
    value is adjacent to a '*' and exactly one other is as well,
    yield those products.
    :param lines:
    :param gears:
    :return:
    """
    gear_dict = defaultdict(list)
    symbol_set = {
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.replace(r'\n', ''))
        if not val.isdigit() and val != '.'
    }
    for j, line in enumerate(lines):
        for nums in re.finditer(r'\d+', line):
            for i in range(nums.start(), nums.end()):
                intersection = set(adj_parts(i, j)).intersection(symbol_set)
                if intersection:
                    n = int(nums.group(0))
                    for sym in intersection:
                        x, y = sym
                        if lines[y][x] == '*':
                            gear_dict[(x, y)].append(n)
                    if not gears:
                        yield n
                    break
    if gears:
        for v in gear_dict.values():
            if len(v) == 2:
                yield v[0] * v[1]


@timing
def part_one(lines) -> int:
    return sum(parse(lines))


@timing
def part_two(lines) -> int:
    return sum(parse(lines, gears=True))


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day03.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 528799   // 0.0093 sec
    LOGGER.info(part_two(input_))  # 84907174 // 0.0089 sec
