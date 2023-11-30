"""
https://adventofcode.com/2022/day/4
--- Day 4: Camp Cleanup ---
"""
import csv
from typing import List

from src.main.python.utilities import range_inc, timing, LOGGER


def get_range_sets(*args: List[int]) -> List:
    ret = list()
    for arg in args:
        ret.append(set(range_inc(*arg)))
    return ret


@timing
def part_one(assignments: List[List[List[int]]]) -> int:
    counter = 0
    for pair in assignments:
        ranges = get_range_sets(*pair)
        if ranges[0].issubset(ranges[1]) or ranges[1].issubset(ranges[0]):
            counter += 1
    return counter


@timing
def part_two(assignments: List[List[List[int]]]) -> int:
    counter = 0
    for pair in assignments:
        ranges = get_range_sets(*pair)
        if ranges[0].intersection(ranges[1]) or ranges[1].intersection(ranges[0]):
            counter += 1
    return counter


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_04.txt', 'r') as f:
        backpacks = [[[int(z) for z in y.split('-')] for y in x] for x in csv.reader(f)]
    LOGGER.info(part_one(backpacks))  # 595
    LOGGER.info(part_two(backpacks))  # 952
