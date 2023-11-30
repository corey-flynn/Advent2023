"""
https://adventofcode.com/2022/day/14
--- Day 14: Regolith Reservoir ---
"""
from itertools import pairwise
from typing import Dict, List, Tuple

from src.main.python.utilities import LOGGER, timing, range_inc, to_ints


def extremes(rock_map: List[List[Tuple[int]]]) -> Dict[str, int]:
    """get the x and y extremes"""
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')
    for row in rock_map:
        for col in row:
            min_y = min(min_y, col[1])
            min_x = min(min_x, col[0])
            max_y = max(max_y, col[1])
            max_x = max(max_x, col[0])
    return dict(
        min_x=min_x,
        min_y=min_y,
        max_x=max_x,
        max_y=max_y,
    )


def coordinate_ranges(left: Tuple[int, int], right: Tuple[int, int]):
    """get the line points between two cartesian coordinates (0 or inf slope)"""
    if left[0] > right[0] or left[1] > right[1]:
        left, right = right, left
    return [
        tuple([x, y]) for x in range_inc(left[0], right[0])
        for y in range_inc(left[1], right[1])
    ]


def build_rocks(
        rock_map: List[List[Tuple[int, int]]],
        extreme_dict: Dict[str, int],
        floor: bool = False,
) -> Dict[Tuple[int, int], int]:
    """
    for some range of x and y, build a dictionary of points
    """
    min_x, max_x, min_y, max_y = map(
        extreme_dict.get, ('min_x', 'max_x', 'min_y', 'max_y')
    )
    rock_matrix = {
        (x, y): 0 for x in range_inc(min_x, max_x) for y in range_inc(min_y, max_y)
    }
    if floor:
        for coord in coordinate_ranges((min_x, max_y), (max_x, max_y)):
            rock_matrix[coord] = 1
    for row in rock_map:
        for left, right in pairwise(row):
            for coord in coordinate_ranges(left, right):
                rock_matrix[coord] = 1
    return rock_matrix


def drop_sand(
        rock_matrix: Dict[Tuple[int, int], int],
        start_point: Tuple[int, int] = (500, 0),
):
    """
    sand falls from a fixed point in the ceiling and continues to fall until it
    either the startpoint already has sand or falls off the map. if sand cannot fall
    down, it will try to fall left diagonally, then right diagonally.
    """
    current_sand = start_point
    down = lambda x, y: (x, y + 1)
    diag_l = lambda x, y: (x - 1, y + 1)
    diag_r = lambda x, y: (x + 1, y + 1)
    while True:
        if current_sand not in rock_matrix or rock_matrix[start_point] > 0:
            break
        elif rock_matrix.get(down(*current_sand), 0) == 0:
            current_sand = down(*current_sand)
            continue
        elif rock_matrix.get(diag_l(*current_sand), 0) == 0:
            current_sand = diag_l(*current_sand)
            continue
        elif rock_matrix.get(diag_r(*current_sand), 0) == 0:
            current_sand = diag_r(*current_sand)
            continue
        else:
            rock_matrix[current_sand] = 2
            current_sand = start_point


@timing
def part_one(rock_map):
    """
    no floor, if the sand falls to a place that isn't mapped, we're done counting
    """
    extreme_dict = extremes(rock_map)
    extreme_dict['min_y'] = 0  # ceiling
    rock_matrix = build_rocks(rock_map, extreme_dict, floor=False)
    drop_sand(rock_matrix)
    return len([x for x in rock_matrix.values() if x == 2])


@timing
def part_two(rock_map):
    """
    there is a floor present, and it's two below the old minimum. count until the sand
    reached back up to the ceiling. Because, at most, this can build an isosceles
    triangle we can use the sand entry point of 500 and y maximum and start point to
    find the width.
    """
    extreme_dict = extremes(rock_map)
    extreme_dict['min_x'] = 500 - extreme_dict['max_y'] - 2
    extreme_dict['max_x'] = 500 + extreme_dict['max_y'] + 2
    extreme_dict['max_y'] = extreme_dict['max_y'] + 2
    extreme_dict['min_y'] = 0  # ceiling
    rock_matrix = build_rocks(rock_map, extreme_dict, floor=True)
    drop_sand(rock_matrix)
    return len([x for x in rock_matrix.values() if x == 2])


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_14.txt', 'r') as f:
        input_ = [
            [to_ints(y.split(',')) for y in x.split(' -> ')]
            for x in f.read().splitlines()
        ]
    LOGGER.info(part_one(input_))  # 672
    LOGGER.info(part_two(input_))  # 26831
