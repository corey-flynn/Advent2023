"""
https://adventofcode.com/2023/day/12
"""
import re
from collections import defaultdict
from functools import lru_cache
from itertools import takewhile

from src.main.python.utilities import LOGGER, timing

REG_DOT = '[.?]'
REG_START = f'{REG_DOT}*'
REG_END = f'{REG_DOT}*'


def parse(lines):
    gears = list()
    for line in lines:
        s, pattern = line.split()
        gears.append((s, pattern.split(',')))
    return gears


@lru_cache(maxsize=None)
def acceptable_substrings(string, val):
    placements = list()
    for i in range(len(string)-1-val):
        ss = string[i:i+2+val]
        if '#' not in ss[0] and '#' not in ss[-1] and '.' not in ss[1:-1]:
            placements.append(i)
    return tuple(placements)


def find_potentials(string, pattern):
    string = '.' + string + '.'
    all_acceptable_placements = list()
    for val in pattern:
        val = int(val)
        all_acceptable_placements.append((val,) + acceptable_substrings(string, val))
    return all_acceptable_placements


def place_permutations(placements, requirements, current=(), idx=0):
    if idx == len(placements):
        if requirements.issubset(set(current)):
            return {current}
        else:
            return set()

    permutations = set()
    for value in placements[idx][1:]:
        if not current or value >= current[-1] + 2:
            new_current = current + tuple(range(value, value + placements[idx][0]))
            next_idx = idx + 1
            permutations.update(place_permutations(placements, requirements, new_current, next_idx))

    return permutations


@timing
def part_one(lines) -> int:
    count = 0
    for s, pattern in parse(lines):
        potentials = find_potentials(s, pattern)
        known_gears = set(i for i, char in enumerate(s) if char == '#')
        perms = place_permutations(potentials, requirements=known_gears)
        count += len(perms)
    return count


@timing
def part_two(lines) -> int:
    # TODO come back to this one, it's not right
    count = 0
    for s, pattern in parse(lines):
        s = '?'.join(s for _ in range(5))
        pattern = pattern * 5
        potentials = find_potentials(s, pattern)
        known_gears = set(i for i, char in enumerate(s) if char == '#')
        perms = place_permutations(potentials, requirements=known_gears)
        count += len(perms)
    return count


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day12.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 7007 // 0.1073 sec
    LOGGER.info(part_two(input_))
