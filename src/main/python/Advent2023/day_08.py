"""
https://adventofcode.com/2023/day/8
--- Day 8: Haunted Wasteland ---
"""
import re
from math import lcm
from itertools import cycle

from src.main.python.utilities import LOGGER, timing

START_NODE = 'AAA'
END_NODE = 'ZZZ'
MAP_REGEX = re.compile(r'(\w{3}) = \((\w{3}), (\w{3})\)')


def parse(lines):
    tree = dict()
    path, _, *maps = lines
    for map_ in maps:
        node, left, right = MAP_REGEX.match(map_).groups()
        tree[node] = {'L': left, 'R': right}
    return path, tree


@timing
def part_one(lines) -> int:
    path, tree = parse(lines)
    current_node = START_NODE
    for i, direction in enumerate(cycle(path)):
        current_node = tree[current_node][direction]
        if current_node == END_NODE:
            break
    return i + 1


@timing
def part_two(lines) -> int:
    """
    Honestly, I don't know why this works. But I printed out each step-length
    between multiple node.endswith('A') and node.endswith('Z') and it was always
    the same. From there, it's simply mathematics to get the LCM of each run.
    """
    path, tree = parse(lines)
    current_keys = {x for x in tree.keys() if x.endswith('A')}
    end_keys = {x for x in tree.keys() if x.endswith('Z')}
    steps = list()
    for key in current_keys:
        current_node = key
        for i, direction in enumerate(cycle(path)):
            current_node = tree[current_node][direction]
            if current_node in end_keys:
                steps.append(i+1)
                break
    return lcm(*steps)


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day08.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 19_951             // 0.0036 sec
    LOGGER.info(part_two(input_))  # 16_342_438_708_751 // 0.0166 sec
