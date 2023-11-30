"""
https://adventofcode.com/2022/day/8
--- Day 8: Treetop Tree House ---
"""
from typing import Iterable, List

from src.main.python.utilities import LOGGER, timing


def takewhile_plusone(predicate: callable, iterable: Iterable):
    """same as the itertools version, but grabs an extra if available"""
    for x in iterable:
        yield x
        if not predicate(x):
            break


def get_next_biggest(l: List[int], i) -> float:
    """
    get the product of the number of values that are lower to a particular index
    on both the right and the left
    """
    tree = l[i]
    left = list(takewhile_plusone(lambda x: x < tree, l[:i][::-1]))
    right = list(takewhile_plusone(lambda x: x < tree, l[i+1:]))

    return len(left) * len(right)


@timing
def part_one(forest: List[List[int]]) -> int:
    """
    find the trees that are not obfuscated from view from the outside of the forest
    :param forest: matrix of tree heights
    :return: number of trees that visible from the outside of the forest
    """
    visible_tree_set = set()
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            if tree > max(row[:j] or [-1]) or tree > max(row[j+1:] or [-1]):
                visible_tree_set.add((i, j, tree))
    for j, row in enumerate(zip(*forest)):
        for i, tree in enumerate(row):
            if tree > max(row[:i] or [-1]) or tree > max(row[i+1:] or [-1]):
                visible_tree_set.add((i, j, tree))
    return len(visible_tree_set)


@timing
def part_two(forest: List[List[int]]) -> int:
    """
    get the value of the most scenic tree by how far it can see along the x and y
    axes (positive and negative).
    :param forest: matrix of tree heights
    :return: the value of the most scenic tree, in terms of scenic value
    """
    max_scenic = -1
    flipped_forest = list(zip(*forest))
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            scenic = get_next_biggest(row, j) * get_next_biggest(flipped_forest[j], i)
            if scenic > max_scenic:
                max_scenic = scenic
    return max_scenic


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_08.txt', 'r') as f:
        input_ = [[int(y) for y in x] for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 1779
    LOGGER.info(part_two(input_))  # 172224
