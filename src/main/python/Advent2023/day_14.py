"""
https://adventofcode.com/2023/day/14
"""
import cProfile
from bisect import bisect_left, bisect_right
from itertools import cycle
from functools import cached_property, lru_cache

from src.main.python.utilities import LOGGER, timing, weak_lru


class CoordDict(dict):
    """A dictionary subclass to manage coordinates with rotation logic."""
    def __init__(self):
        super().__init__()
        self.rotate = False
        self._rotations = cycle(('up', 'left', 'down', 'right'))
        self.rotation = next(self._rotations)
        self.sorted_keys_value = lru_cache(maxsize=None)(self.sorted_keys_value)

    @cached_property
    def sorted_keys(self):
        return sorted([key for key in self.keys()])

    def sorted_keys_value(self, value, side=0):
        return tuple(key for key in self.sorted_keys if key[side] == value)

    def insert_nearest_j(self, x: int, y: int) -> tuple:
        """Inserts an element in the nearest position based on the current rotation direction."""
        match self.rotation:
            case 'up':
                rank_keys = self.sorted_keys_value(x)
                idx = bisect_left(rank_keys, (x, y)) - 1
                key = rank_keys[idx]
                stack_height = len(self[key])
                movers = (key[0], key[1]+stack_height+1)
            case 'right':
                rank_keys = self.sorted_keys_value(y, side=1)
                idx = bisect_left(rank_keys, (x, y))
                key = rank_keys[idx]
                stack_height = len(self[key])
                movers = (key[0]-stack_height-1, key[1])
            case 'down':
                rank_keys = self.sorted_keys_value(x)
                idx = bisect_right(rank_keys, (x, y))
                key = rank_keys[idx]
                stack_height = len(self[key])
                movers = (key[0], key[1]-stack_height-1)
            case 'left':
                rank_keys = self.sorted_keys_value(y, side=1)
                idx = bisect_left(rank_keys, (x, y)) - 1
                key = rank_keys[idx]
                stack_height = len(self[key])
                movers = (key[0]+stack_height+1, key[1])
            case _: pass
        self[key].append(movers)
        return rank_keys[idx]

    def flat_values(self) -> list:
        return [x for y in self.values() for x in y]

    def clear_values(self) -> None:
        if self.rotate:
            self.rotation = next(self._rotations)
        for key in self.keys():
            self[key] = list()


def parse(lines: list[str]) -> tuple[CoordDict, list[tuple[int, int]]]:
    cube_rocks = CoordDict()
    sphere_rocks = list()
    for j, line in enumerate(lines):
        for i, val in enumerate(line):
            match val:
                case '#': cube_rocks[(i+1, j+1)] = list()
                case 'O': sphere_rocks.append((i+1, j+1))
                case _: continue
            cube_rocks[(i+1, 0)] = list()  # top border
            cube_rocks[(i+1, len(lines[0])+1)] = list()  # bottom border
        cube_rocks[(0, j+1)] = list()  # left border
        cube_rocks[(len(lines[0])+1, j+1)] = list()  # right border
    return cube_rocks, sphere_rocks


def slide(fixed: CoordDict, moving: list[tuple[int, int]]) -> None:
    """Moves each element in 'moving' to the nearest position in 'fixed' based on the rotation logic."""
    for i, j in moving:
        fixed.insert_nearest_j(i, j)


def find_subsequence_cycles(nums: list[int], min_size: int = 4) -> int:
    """Finds the length of a repeating subsequence in a list of numbers."""
    for i in range(min_size, len(nums)):
        if nums[-i*2:-i] == nums[-i:]:
            return i


def get_offset(large_number: int, cycle_totals: list[int], cycle_length: int) -> int:
    """Calculates the value at a specific position in a repeating cycle."""
    position_in_cycle = (large_number - 1) % cycle_length
    return cycle_totals[position_in_cycle]


@timing
def part_one(lines) -> int:
    cubes, spheres = parse(lines)
    slide(cubes, spheres)
    return sum(len(lines)+1-x[1] for x in cubes.flat_values())


@timing
def part_two(lines) -> int:
    cubes, spheres = parse(lines)
    cubes.rotate = True
    cycle_totals = list()
    for i in range(2000):
        slide(cubes, spheres)
        spheres = cubes.flat_values()
        if cubes.rotation == 'right':
            total = sum(len(lines)+1-x[1] for x in cubes.flat_values())
            cycle_totals.append(total)
            if (i+1) % 100 == 0:
                ss_len = find_subsequence_cycles(cycle_totals)
                if ss_len:
                    return get_offset(1_000_000_000-((i+1)//4), cycle_totals[-ss_len:], ss_len)
        cubes.clear_values()


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day14.txt', 'r') as f:
        input_ = f.read().split('\n')
    # cProfile.run('part_two(input_)', sort='cumtime')
    LOGGER.info(part_one(input_))  # 102_497 // 0.1878 sec
    LOGGER.info(part_two(input_))  # 105_008 // 1.8761 sec
