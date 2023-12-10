"""
https://adventofcode.com/2023/day/9
"""
from typing import List, Tuple

from src.main.python.utilities import LOGGER, timing


def parse(lines: List[str]) -> Tuple[Tuple[int]]:
    return tuple(tuple(int(num) for num in line.split()) for line in lines)


def sequencer(seq: Tuple[int], next_val=None):
    """Recursive interval finder."""
    if next_val is None:
        next_val = seq[-1]
    seq = tuple(int(seq[i+1] - x) for i, x in enumerate(seq[:-1]))
    next_val += seq[-1]
    if any(seq):
        return sequencer(seq, next_val=next_val)
    else:
        return next_val


@timing
def part_one(lines) -> int:
    return sum(sequencer(line) for line in parse(lines))


@timing
def part_two(lines) -> int:
    """Same thing, backwards."""
    return sum(sequencer(line[::-1]) for line in parse(lines))


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day09.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 1_955_513_104 // 0.0090 sec
    LOGGER.info(part_two(input_))  # 1_131         // 0.0092 sec
