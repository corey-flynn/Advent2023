"""
https://adventofcode.com/2022/day/9
--- Day 9: Rope Bridge ---
"""
from enum import Enum
from functools import lru_cache
from typing import List, Tuple

from src.main.python.utilities import LOGGER, timing


class Dir(Enum):
    U = (0, 1)
    D = (0, -1)
    L = (-1, 0)
    R = (1, 0)


@lru_cache
def tail_follow(head: Tuple[int], tail: Tuple[int]) -> Tuple[int]:
    diff = tuple(x[0] - x[1] for x in zip(head, tail))
    if any(abs(x) > 1 for x in diff):
        return tuple(
            tail[i] + 1 if x > 0 else tail[i] - 1 if x < 0 else tail[i]
            for i, x in enumerate(diff)
        )
    return tail


def followers(directions: List[List[str]], rope_len=1) -> List[Tuple[int]]:
    if rope_len < 1:
        return []
    head_xy = (0, 0)
    head_path = list()
    for dir_, len_ in directions:
        len_ = int(len_)
        for _ in range(len_):
            head_xy = tuple(sum(x) for x in zip(head_xy, Dir[dir_].value))
            head_path.append(head_xy)

    for _ in range(rope_len):
        tail_xy = (0, 0)
        tail_path = list()
        for head_xy in head_path:
            tail_xy = tail_follow(head_xy, tail_xy)
            tail_path.append(tail_xy)
        head_path = tail_path.copy()
    return tail_path


@timing
def part_one(directions: List[List[str]]) -> int:
    return len(set(followers(directions)))


@timing
def part_two(directions: List[List[str]]) -> int:
    return len(set(followers(directions, 9)))


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_09.txt', 'r') as f:
        input_ = [x.split() for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 6745
    LOGGER.info(part_two(input_))  # 2793
