"""
https://adventofcode.com/2023/day/11
"""
from itertools import combinations

from src.main.python.utilities import LOGGER, timing, manhattan_distance


def find_expansions(lines):
    """Find empty space to expand."""
    rows = list()
    cols = list()
    for j, line in enumerate(lines):
        if set(line) == {'.'}:
            rows.append(j)
    for i, line in enumerate(zip(*lines)):
        if set(line) == {'.'}:
            cols.append(i)
    return rows, cols


def find_galaxies(space):
    """Find initially observed locations."""
    space_set = set()
    for j, line in enumerate(space):
        for i, val in enumerate(line):
            if val == '#':
                space_set.add((i, j))
    return space_set


def expand_galaxies(expansions, galaxies, times):
    """Expand universe at empty space n times."""
    times -= 1
    rows, cols = expansions
    expanded_galaxies = set()
    for i, j in galaxies:
        i_plus = len([x for x in filter(lambda x: x < i, cols)]) * times + i
        j_plus = len([x for x in filter(lambda x: x < j, rows)]) * times + j
        expanded_galaxies.add((i_plus, j_plus))
    return expanded_galaxies


@timing
def part_one(lines) -> int:
    galaxies = expand_galaxies(find_expansions(lines), find_galaxies(lines), times=2)
    return sum(manhattan_distance(a, b) for a, b in combinations(galaxies, 2))


@timing
def part_two(lines, times=1_000_000) -> int:
    # times added here just for testing purposes
    galaxies = expand_galaxies(find_expansions(lines), find_galaxies(lines), times=times)
    return sum(manhattan_distance(a, b) for a, b in combinations(galaxies, 2))


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day11.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 10_313_550      // 0.1055 sec
    LOGGER.info(part_two(input_))  # 611_998_089_572 // 0.1096 sec
