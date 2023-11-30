"""
https://adventofcode.com/2022/day/15
--- Day 15: Beacon Exclusion Zone ---
"""
import json
import re
from collections import Counter
from typing import Dict, Generator, Iterable, Tuple, Set

from src.main.python.utilities import LOGGER, timing, to_ints, range_inc, manhattan_distance


class Sensor:
    """
    sensor object with local and beacon coordinates with some functionality
    for finding the edges
    """
    def __init__(self, coords: Tuple[int, int], beacon_coords: Tuple[int, int]):
        self.coords = coords
        self.beacon_coords = beacon_coords
        self.m_dist = manhattan_distance(self.coords, self.beacon_coords)

    def __repr__(self) -> str:
        return json.dumps(
            {
                'coords': self.coords,
                'beacon_coords': self.beacon_coords,
                'manhattan_distance': self.m_dist,
            },
        )

    @property
    def x(self) -> int:
        return self.coords[0]

    @property
    def y(self) -> int:
        return self.coords[1]

    def bbox(self) -> Dict[str, Tuple[int, int]]:
        return {
            'left': (self.coords[0] - self.m_dist, self.coords[1]),
            'right': (self.coords[0] + self.m_dist, self.coords[1]),
            'upper': (self.coords[0], self.coords[1] + self.m_dist),
            'lower': (self.coords[0], self.coords[1] - self.m_dist),
        }

    def upper_left(self) -> Generator[Tuple[int, int], None, None]:
        left_x, left_y = self.bbox()['left']
        return ((left_x + i, left_y + i) for i in range_inc(self.m_dist))

    def lower_left(self) -> Generator[Tuple[int, int], None, None]:
        left_x, left_y = self.bbox()['left']
        return ((left_x + i, left_y - i) for i in range_inc(self.m_dist))

    def upper_right(self) -> Generator[Tuple[int, int], None, None]:
        right_x, right_y = self.bbox()['right']
        return ((right_x - i, right_y + i) for i in range_inc(self.m_dist))

    def lower_right(self) -> Generator[Tuple[int, int], None, None]:
        right_x, right_y = self.bbox()['right']
        return ((right_x - i, right_y - i) for i in range_inc(self.m_dist))

    def outer_rim(self) -> Set[Tuple[int, int]]:
        return (
                {(x[0] - 1, x[1]) for x in self.upper_left()}
                | {(x[0], x[1] + 1) for x in self.upper_right()}
                | {(x[0] + 1, x[1]) for x in self.lower_right()}
                | {(x[0], x[1] - 1) for x in self.lower_left()}
        )


def read_input(i: Iterable[str]) -> Generator[Sensor, None, None]:
    reg = re.compile(
        r'.*x=(?P<sx>-?\d+), y=(?P<sy>-?\d+):'
        r'.*x=(?P<bx>-?\d+), y=(?P<by>-?\d+).*'
    )
    for row in i:
        row = reg.match(row).groupdict()
        yield Sensor(to_ints((row['sx'], row['sy'])), to_ints((row['bx'], row['by'])))


def row_coverage(sensors: Iterable[Sensor], row_index: int) -> Set[Tuple[int, int]]:
    """for some row, find all the places a beacon could be found"""
    row_slots = set()
    for s in sensors:
        if s.y >= row_index >= s.y - s.m_dist:
            dist = (s.y - row_index)
        elif s.y < row_index < s.y + s.m_dist:
            dist = (row_index - s.y)
        else:
            continue
        for r in range_inc(s.x-(s.m_dist-dist), s.x+(s.m_dist-dist)):
            row_slots.add((r, row_index))
    return row_slots


@timing
def part_one(i: Iterable[str], row_index: int = 10) -> int:
    beacon_set = set()
    sensors = set(read_input(i))
    for s in sensors:
        beacon_set.add(s.beacon_coords)
    return (
            len(row_coverage(sensors, row_index))
            - len(set(filter(lambda x: x[1] == row_index, beacon_set)))
    )


@timing
def part_two(i: Iterable[str]) -> int:
    """
    I hate this solution, but it works and I'm not going to give
    this any more of my time.

    Find all the points just outside of every box bounded by the manhattan distance,
    because there is only one place where (at least) four should intersect, take
    the most common point and use that as your solution.
    """
    sensors = set(read_input(i))
    c = Counter()
    for s in sensors:
        c.update(s.outer_rim())
    return c.most_common(1)[0][0][0] * 4_000_000 + c.most_common(1)[0][0][1]


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_15.txt', 'r') as f:
        input_ = f.read().splitlines()
    LOGGER.info(part_one(input_, row_index=2_000_000))  # 4582667
    LOGGER.info(part_two(input_))  # 10961118625406
