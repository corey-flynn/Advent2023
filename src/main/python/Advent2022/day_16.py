"""
https://adventofcode.com/2022/day/16
--- Day 16: Proboscidea Volcanium ---
"""
import re
from copy import deepcopy
from collections import defaultdict
from typing import Dict, Iterator, List, Tuple, Union

from src.main.python.utilities import LOGGER, timing, dijkstra


def parse_input(i: List[str]) -> Iterator[Dict[str, str]]:
    reg = re.compile(
        r'Valve (?P<valve>[A-Z]{2}) has flow rate=(?P<flow>\d+); '
        r'tunnels? leads? to valves? (?P<paths>.*)'
    )
    for row in i:
        d = reg.match(row).groupdict()
        d['paths'] = d['paths'].split(', ')
        yield d


class Graph:
    def __init__(self):
        self.valves = defaultdict(dict)
        self.weights = dict()

    def add_path(self, valve: str, flow: Union[str, int], paths: List[str]):
        """add paths in reverse"""
        for v in paths:
            self.valves[valve][v] = 1
        self.weights[valve] = int(flow)

    @property
    def nodes(self) -> List[str]:
        return list(self.valves.keys())


def get_max(
        d: Dict[str, Dict[str, int]],
        w: Dict[str, int],
        timer: int,
        start: str,
        value: int = 0,
        path: Tuple[str] = None,
        values: Dict[Tuple[str], int] = None,
) -> None:
    """

    :param d: Dictionary of Dictionaries of shortest paths to every value
    :param w: Dictionary of pressure values
    :param timer: remaining time on the timer
    :param start: current node
    :param value: running total of pressure released
    :param path: path taken to get to arrive at the level of pressure released
    :param values: Distionary to be updated with paths and pressure released
    :return: None, update values dict inplace
    """
    if not value:
        value = 0
    if not path:
        path = tuple()
    ww = deepcopy(w)
    if timer > 0:
        for k, v in d[start].items():
            new_time = timer - v - 1
            pressure = ww[k] * new_time
            if pressure > 0 and k not in path:
                get_max(d, ww, new_time, k, value + pressure, path + (k,), values)
                values[path + (k,)] = value + pressure


@timing
def part_one(i: List[str]):
    """
    Get all the paths and find the one that can release the most pressure in the
    allotted time
    """
    g = Graph()
    for ins in parse_input(i):
        g.add_path(**ins)
    timer = 30
    all_paths = {x: dijkstra(g.valves, x) for x in g.valves.keys()}
    values = dict()
    get_max(all_paths, g.weights, timer, 'AA', values=values)
    return max(values.values())


@timing
def part_two(i: List[str]):
    """
    this is disgusting. not proud of it one bit.

    find all the paths, then find all the disjoints of all the paths (takes forever).
    keep a total running of the sum of each path and return the maximum.
    """
    g = Graph()
    for ins in parse_input(i):
        g.add_path(**ins)
    timer = 26
    all_paths = {x: dijkstra(g.valves, x) for x in g.valves.keys()}
    values = dict()
    get_max(all_paths, g.weights, timer, 'AA', values=values)
    value_tuple = tuple((set(x[0]), x[1]) for x in values.items())
    max_path = 0
    for s in value_tuple:
        for s_ in value_tuple:
            if s[0].isdisjoint(s_[0]):
                if s[1] + s_[1] > max_path:
                    max_path = s[1] + s_[1]
    return max_path


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_16.txt', 'r') as f:
        input_ = f.read().splitlines()
    LOGGER.info(part_one(input_))  # 2265
    LOGGER.info(part_two(input_))  # 2811
