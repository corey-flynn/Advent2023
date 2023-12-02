"""
https://adventofcode.com/2023/day/1
--- Day 1: Trebuchet?! ---
"""
from typing import Iterable

from src.main.python.utilities import LOGGER, timing

SPELLED_DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def scan(s: str, vals: Iterable[str], scan_left: bool = True) -> str:
    """
    scan a string from left or right until a value in vals is found,
    then return that value.
    :param s: string to scan
    :param vals: values to search for
    :param scan_left: True to start at the beginning of the string
        or False to start from the end
    :return: first value found in string
    """
    for i in range(len(s)):
        if scan_left:
            sl = slice(i)
        else:
            sl = slice(-i-1, len(s))
        if any(str(x) in s[sl] for x in vals):
            val = [str(x) for x in vals if str(x) in s[sl]][0]
            return SPELLED_DIGITS.get(val, val)


def scan_both_ways(s: str, vals: Iterable[str]):
    return scan(s, vals) + scan(s, vals, scan_left=False)


@timing
def part_one(lines) -> int:
    vals = SPELLED_DIGITS.values()
    return sum([int(scan_both_ways(x, vals)) for x in lines])


@timing
def part_two(lines) -> int:
    vals = set(SPELLED_DIGITS.values()).union(SPELLED_DIGITS.keys())
    return sum([int(scan_both_ways(x, vals)) for x in lines])


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day01.txt', 'r') as f:
        input_ = f.readlines()
    LOGGER.info(part_one(input_))  # 56506 // 0.0462 sec
    LOGGER.info(part_two(input_))  # 56017 // 0.0539 sec
