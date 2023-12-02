"""
https://adventofcode.com/2023/day/2
--- Day 2: Cube Conundrum ---
"""
import re
from collections import Counter
from math import prod
from typing import Dict, List

from src.main.python.utilities import LOGGER, timing

GAME_REG = re.compile(r'Game (\d+): ')
CUBE_REG = re.compile(r'(\d+) (blue|green|red)')


def parse(games: List[str]) -> Dict[int, Counter]:
    """
    parse the lines and put them into a dictionary of game number
    to Counter objects
    :param games: line in the format of Game <n>: <n> <color>;
    :return: dictionary of games and Counters
    """
    d = dict()
    for game in games:
        d[int(GAME_REG.match(game).group(1))] = Counter({
            x[1]: x[0] for x in sorted(
                [(int(x[0]), x[1]) for x in CUBE_REG.findall(game)],
            )
        })
    return d


@timing
def part_one(games) -> int:
    possible_game = Counter({'red': 13, 'green': 14, 'blue': 15})
    return sum(k for k, v in parse(games).items() if len(possible_game - v) == 3)


@timing
def part_two(games) -> int:
    return sum(prod(x.values()) for x in parse(games).values())


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day02.txt', 'r') as f:
        input_ = f.readlines()
    LOGGER.info(part_one(input_))
    LOGGER.info(part_two(input_))
