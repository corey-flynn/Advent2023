"""
https://adventofcode.com/2022/day/18
--- Day 18: Boiling Boulders ---
"""
from collections import defaultdict

from src.main.python.utilities import LOGGER, timing


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.coord = self.x, self.y, self.z

    def distance(self, other):
        """find the distance to another point"""
        return (
                (self.x - other.x) ** 2
                + (self.y - other.y) ** 2
                + (self.z - other.z) ** 2
        ) ** 0.5


@timing
def part_one(lava_drops):
    counter = 0
    point_set = list()
    for point in lava_drops:
        counter += 6
        p = Point(*point)
        counter -= len(tuple(filter(lambda x: x.distance(p) == 1, point_set))) * 2
        point_set.append(p)
    return counter


@timing
def part_two(lava_drops):
    z_dict = defaultdict(set)
    for point in lava_drops:
        z_dict[point[2]].add(tuple(point[:2]))
    print(z_dict)
    return


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_18.txt', 'r') as f:
        input_ = [[int(y) for y in x.split(',')] for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 3542
    # LOGGER.info(part_two(input_))
