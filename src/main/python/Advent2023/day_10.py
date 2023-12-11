"""
https://adventofcode.com/2023/day/10
"""
import sys
from typing import Tuple

from src.main.python.utilities import LOGGER, timing, agg_iterable


sys.setrecursionlimit(25_000)  # lol
DIRECTIONS = {
    '|': ((0, 1), (0, -1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, 1), (-1, 0)),
    'F': ((0, 1), (1, 0)),
}
START = 'S'


def find_first_value(lines, value=START):
    for j, line in enumerate(lines):
        for i, val in enumerate(line):
            if val == value:
                return i, j


def possible_directions(pos: Tuple[int, int], lines):
    """Find all paths that can also get back to the start pos."""
    for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        poss_val = lines[pos[1]+j][pos[0]+i]
        if poss_val == '.':
            continue
        if (-i, -j) in DIRECTIONS[poss_val]:
            yield i, j


def follow_path(lines):
    """Walk along the loop once."""
    start_pos = find_first_value(lines)
    dir_ = next(possible_directions(start_pos, lines))  # just pick one
    pos = agg_iterable(start_pos, dir_)
    path = [start_pos, pos]
    while pos != start_pos:
        # iter through the path until you find the start again
        # this works by finding the direction the pipe was just traveled
        # and returning the other direction which is added to the position
        # and appended to the path
        pipe_type: str = lines[pos[1]][pos[0]]
        prev_dir_: tuple = agg_iterable(dir_, (-1, -1), agg='mul')
        dir_ = [x for x in list(DIRECTIONS[pipe_type]) if x != prev_dir_][0]
        pos = agg_iterable(pos, dir_)
        path.append(pos)
    return path


def outsiders(map_, path, pos, outside_points=None, visited=None):
    if visited is None:
        visited = set()
    if outside_points is None:
        outside_points = set()
    for dir_ in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_pos = agg_iterable(pos, dir_)
        if new_pos in visited:
            continue
        else:
            visited.add(new_pos)
        if (
            new_pos not in path
            and 0 <= new_pos[1] < len(map_)
            and 0 <= new_pos[0] < len(map_[0])
        ):
            map_[new_pos[1]][new_pos[0]] = 'O'
            outsiders(map_, path, new_pos, outside_points, visited)


@timing
def part_one(lines) -> int:
    return len(follow_path(lines)) // 2


@timing
def part_two(lines) -> int:
    path = set(follow_path(lines))
    lines = list(lines)
    # replace S
    start_x, start_y = find_first_value(lines)
    for key, val in DIRECTIONS.items():
        if set(val) == {x for x in possible_directions((start_x, start_y), lines)}:
            lines[start_y] = lines[start_y].replace('S', key)
    replacements = {  # to make the picture easier to follow
        'F': '╔',
        'J': '╝',
        '7': '╗',
        'L': '╚',
        '-': '=',
        '|': '║',
    }
    for y, line in enumerate(lines):
        for key, val in replacements.items():
            line = line.replace(key, val)
        lines[y] = line
    map_ = [
        [val if (i, j) in path else '.' for i, val in enumerate(line)]
        for j, line in enumerate(lines)
    ]
    outsiders(map_, path, (0, 0))
    while True:
        try:
            dot_x, dot_y = find_first_value(map_, '.')
        except TypeError:
            break
        left_vals = ''.join([x for x in map_[dot_y][:dot_x]]).rsplit('O')[-1].replace('=', '')
        if not left_vals:
            dot_val = 'O'
        elif (left_vals.count('╔╝') + left_vals.count('╚╗') + left_vals.count('║')) % 2 == 1:
            dot_val = 'I'
        else:
            dot_val = 'O'
        map_[dot_y][dot_x] = dot_val
    # print()
    # for line in map_:
    #     print(''.join(line))  # uncomment to see a pretty picture
    return sum(s.count('I') for s in map_)


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day10.txt', 'r') as f:
        input_ = tuple(f.read().split('\n'))
    LOGGER.info(part_one(input_))  # 6_867 // 0.0515 sec
    LOGGER.info(part_two(input_))  # 595   // 0.6231 sec
