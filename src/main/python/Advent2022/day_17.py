"""
https://adventofcode.com/2022/day/17

"""
from itertools import cycle

from src.main.python.utilities import LOGGER, timing


ROCK_SHAPES = {
            0: ((2, 0), (3, 0), (4, 0), (5, 0)),
            1: ((3, 0), (2, 1), (3, 1), (4, 1), (3, 2)),
            2: ((4, 0), (3, 0), (2, 0), (4, 1), (4, 2)),
            3: ((2, 0), (2, 1), (2, 2), (2, 3)),
            4: ((2, 0), (3, 0), (2, 1), (3, 1)),
        }


class Chamber:
    def __init__(self, width):
        self.width = width
        self.fixed_rock_positions = {(x, 0) for x in range(7)}
        self.current_rock_number = 0
        self.current_rock = tuple()
        self.high_point = 0

    def _get_new_rock(self):
        self.current_rock = ROCK_SHAPES[self.current_rock_number % 5]
        self.current_rock = (
            (x[0], x[1] + self.high_point + 4) for x in self.current_rock
        )
        self.current_rock_number += 1

    def _column_merge(self):
        pass

    def rock_fall(self, direction):
        match direction:
            case '<': rotate = -1
            case _: rotate = 1
        if not self.current_rock:
            self._get_new_rock()
            self.current_rock = tuple(self.current_rock)
        temp_push = tuple((x[0] + rotate, x[1]) for x in self.current_rock)
        if (
                all([0 <= x[0] <= 6 for x in temp_push]) and
                all(x not in self.fixed_rock_positions for x in temp_push)
        ):
            self.current_rock = temp_push
        temp_drop = tuple((x[0], x[1] - 1) for x in self.current_rock)
        if all(x not in self.fixed_rock_positions for x in temp_drop):
            self.current_rock = temp_drop
        else:
            if max(x[1] for x in self.current_rock) > self.high_point:
                self.high_point = max(x[1] for x in self.current_rock)
            self.fixed_rock_positions.update(self.current_rock)
            self.current_rock = tuple()


@timing
def part_one(jet_dir: str, n):
    c = Chamber(7)
    for direction in cycle(jet_dir):
        c.rock_fall(direction)
        if c.current_rock_number == n + 1:
            break
    return c.high_point


@timing
def part_two(jet_dir: str, n):
    c = Chamber(7)
    for direction in cycle(jet_dir):
        c.rock_fall(direction)
        if c.current_rock_number == n + 1:
            break
    return c.high_point


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_17.txt', 'r') as f:
        input_ = f.read().replace('\n', '')
    LOGGER.info(part_one(input_, n=2022))  # 3219
    # LOGGER.info(part_two(input_, n=1_000_000_000_000))
