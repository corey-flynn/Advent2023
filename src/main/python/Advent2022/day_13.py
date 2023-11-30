"""
https://adventofcode.com/2022/day/13
--- Day 13: Distress Signal ---
"""
import operator
from copy import deepcopy
from itertools import zip_longest
from typing import Iterable

from src.main.python.utilities import LOGGER, timing


def twosies(i: Iterable) -> iter:
    """take two elements at a time from an iterable"""
    a = iter(i)
    return zip_longest(a, a)


def fix_types(*args):
    """list elements that are not lists"""
    for arg in args:
        if not isinstance(arg, list):
            arg = [arg]
        yield arg


def recur_list(left: list, right: list) -> bool:
    """
    recursively denest list searching for the order of any two elements
    """
    if left is None:
        return True
    elif right is None:
        return False
    if not isinstance(left, type(right)):
        left, right = fix_types(left, right)
    if isinstance(left, list):
        for left_, right_ in zip_longest(left, right):
            rl = recur_list(left_, right_)
            if rl:
                return True
            elif rl is False:
                return False
    else:
        if left < right:
            return True
        elif right < left:
            return False


@timing
def part_one(packets) -> int:
    """take packets two at a time and count which are in the right order"""
    correct_order = 0
    for i, (left, right) in enumerate(twosies(deepcopy(packets))):
        if recur_list(left, right):
            correct_order += i + 1
    return correct_order


@timing
def part_two(packets) -> int:
    """bubble sort whole list"""
    packets = deepcopy(packets)
    correct_order = False
    dividers = [[[2]], [[6]]]
    packets.extend(deepcopy(dividers))
    while not correct_order:
        correct_order = True
        for i, left in enumerate(packets):
            try:
                right = packets[i+1]
            except IndexError:
                break
            if not recur_list(left, right):
                # switch adjacent elements in the wrong order, note the order is wrong
                packets[i] = right
                packets[i+1] = left
                correct_order = False
    return operator.mul(*map(lambda x: packets.index(x) + 1, dividers))


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_13.txt', 'r') as f:
        input_ = [eval(x) for x in f.read().splitlines() if x]
    LOGGER.info(part_one(input_))  # 5393
    LOGGER.info(part_two(input_))  # 26712
