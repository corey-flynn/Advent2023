"""
https://adventofcode.com/2022/day/3
--- Day 3: Rucksack Reorganization ---
"""
from typing import List
from string import ascii_letters

from src.main.python.utilities import LOGGER


PRIORITY = dict(zip(ascii_letters, range(1, len(ascii_letters) + 1)))


def part_one(rucksacks: List[str]) -> int:
    counter = 0
    for el in rucksacks:
        half = len(el) // 2
        halfs = list(set(el[:half]).intersection(set(el[half:])))[0]
        counter += PRIORITY[halfs]
    return counter


def part_two(rucksacks: List[str]) -> int:
    counter = 0
    for i in range(len(rucksacks) // 3):
        r = i * 3
        counter += PRIORITY[
            list(set.intersection(*({y for y in x} for x in rucksacks[r:r+3])))[0]
        ]
    return counter


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_03.txt', 'r') as f:
        backpacks = [x.split()[0] for x in f.readlines()]
    LOGGER.info(part_one(backpacks))  # 7742
    LOGGER.info(part_two(backpacks))  # 7742
