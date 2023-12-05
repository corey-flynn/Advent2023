"""
https://adventofcode.com/2023/day/4
--- Day 4: Scratchcards ---
"""
import re
from typing import Dict

from src.main.python.utilities import LOGGER, timing

CARD_REG = re.compile(r'Card\s+(\d+):\s+([\d\s]+)\s*\|\s+([\d\s]+)')


def parse(lines) -> Dict[int, int]:
    d = dict()
    for line in lines:
        game, winning, owned = CARD_REG.match(line).groups()
        winning_owned = [x for x in winning.split() if x in owned.split()]
        d[int(game)] = len(winning_owned)
    return d


def win_aggregator(wins: Dict[int, int]) -> int:
    """
    this is inefficient, and I'm sure there is either a pattern or tree that will
    make this quicker. I'll try a different method in the scala implementation
    :param wins: 
    :return: 
    """
    mults = {x: 1 for x in wins}
    for key, val in wins.items():
        for each in range(mults[key]):
            for i in range(key+1, key+1+val):
                mults[i] += 1
    return sum(mults.values())


@timing
def part_one(lines) -> int:
    return sum(2 ** (x - 1) for x in parse(lines).values() if x)


@timing
def part_two(lines) -> int:
    return win_aggregator(parse(lines))


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day04.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 22897   // 0.0083 sec
    LOGGER.info(part_two(input_))  # 5095824 // 2.0466 sec
