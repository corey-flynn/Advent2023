"""
https://adventofcode.com/2022/day/5
--- Day 5: Supply Stacks ---
"""
import re
from copy import deepcopy
from typing import Dict, List

from src.main.python.utilities import LOGGER


def read_crates(stacks) -> Dict[int, List[str]]:
    """
    read stack strings, transform into matrix, rotate matrix and return dictionary
    of stack names (range of numbers from 1 to n) and a list of crates in bottom-to-top
    order.
    """
    stacks = deepcopy(stacks)
    stacks = [list(x[1::4]) for x in stacks if not x[-1].isdigit()]
    flip_stacks = list(zip(*stacks[::-1]))
    return {i+1: [x for x in v if not x.isspace()] for i, v in enumerate(flip_stacks)}


def get_moves(move: str) -> (int, int, int):
    """get number of crates to be moved from some stack to another"""
    return tuple(int(x) for x in re.findall('\\d+', move))


def move_crates(
        move: str,
        stack_dict: Dict[int, List[str]],
        reverse: bool = True,
) -> None:
    """
    move crates from one stack to another with a move string in the format of
    "move <n> from <stack> to <stack>". This updates the dictionary inplace.
    :param move: string in the format of "move <n> from <stack> to <stack>"
    :param stack_dict: dictionary with stack and crate information
    :param reverse: whether the stack should be reversed before moving
    """
    if not reverse:
        reverse = -1
    n, from_, to_ = (int(x) for x in re.findall('\\d+', move))
    stack_dict[to_].extend(
        [stack_dict[from_].pop(-1) for _ in range(n)][::reverse]
    )


def part_one(stacks: List[str], moves: List[str]) -> str:
    """move crates from stacks one at a time"""
    stack_dict = read_crates(stacks)
    for move in moves:
        move_crates(move, stack_dict, reverse=True)
    return ''.join(x[-1] for x in stack_dict.values())


def part_two(stacks: List[str], moves: List[str]) -> str:
    """move crates from stacks while retraining order"""
    stack_dict = read_crates(stacks)
    for move in moves:
        move_crates(move, stack_dict, reverse=False)
    return ''.join(x[-1] for x in stack_dict.values())


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_05.txt', 'r') as f:
        crates = f.read().splitlines()
        ind = crates.index('')
        crates, instructions = crates[:ind], crates[ind+1:]
    LOGGER.info(part_one(crates, instructions))  # ZBDRNPMVH
    LOGGER.info(part_two(crates, instructions))  # WDLPFNNNB
