"""
https://adventofcode.com/2022/day/6
--- Day 6: Tuning Trouble ---
"""
from src.main.python.utilities import LOGGER, timing


def get_unique_chars(message: str, chars: int) -> int:
    for i in range(len(message)):
        if len(set(message[i:i+chars])) == chars:
            return i + chars


@timing
def part_one(signal: str) -> int:
    return get_unique_chars(signal, 4)


@timing
def part_two(signal: str) -> int:
    return get_unique_chars(signal, 14)


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_06.txt', 'r') as f:
        packets = f.read()
    LOGGER.info(part_one(packets))  # 1804
    LOGGER.info(part_two(packets))  # 2508
