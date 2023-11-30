"""
https://adventofcode.com/2022/day/2
--- Day 2: Rock Paper Scissors ---
"""
from copy import deepcopy
from enum import IntEnum
from typing import List

from src.main.python.utilities import LOGGER, timing


class ShapeScore(IntEnum):
    rock = 1
    paper = 2
    scissors = 3


WINS = {
    ShapeScore.rock: ShapeScore.scissors,
    ShapeScore.paper: ShapeScore.rock,
    ShapeScore.scissors: ShapeScore.paper,
}

CODE_MAP = {
    'A': ShapeScore.rock,
    'B': ShapeScore.paper,
    'C': ShapeScore.scissors,
}


def rps(opp: ShapeScore, you: ShapeScore) -> int:
    if opp == you:
        return 3 + you
    if WINS[you] == opp:
        return 6 + you
    else:
        return 0 + you


@timing
def part_one(guide: List[List[str]]) -> int:
    guide = deepcopy(guide)
    counter = 0
    for game in guide:
        game[0] = CODE_MAP[game[0]]
        game[1] = CODE_MAP[chr(ord(game[1]) - 23)]
        counter += rps(*game)
    return counter


@timing
def part_two(guide: List[List[str]]) -> int:
    guide = deepcopy(guide)
    counter = 0
    for game in guide:
        game[0] = CODE_MAP[game[0]]
        if game[1] == 'X':
            game[1] = WINS[game[0].value]
        elif game[1] == 'Y':
            game[1] = game[0]
        elif game[1] == 'Z':
            game[1] = list(WINS.keys())[list(WINS.values()).index(game[0].value)]
        counter += rps(*game)
    return counter


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_02.txt', 'r') as f:
        games = [x.split() for x in f.readlines()]
    LOGGER.info(part_one(games))  # 17189
    LOGGER.info(part_two(games))  # 13490
