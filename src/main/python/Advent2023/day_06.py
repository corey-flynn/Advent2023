"""
https://adventofcode.com/2023/day/6
--- Day 6: Wait For It ---
"""
from math import prod
from typing import List, Tuple

from src.main.python.utilities import LOGGER, timing


def parse(lines: List[str]) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    times, distance = lines
    return (
        tuple(int(x) for x in times.split()[1:]),
        tuple(int(x) for x in distance.split()[1:])
    )


def find_min_max_time(race: Tuple[int, int]):
    time, record = race
    min_time, max_time = 0, time
    while min_time * (time - min_time) <= record:
        min_time += 1
    while (time - max_time) * max_time <= record:
        max_time -= 1
    return min_time, max_time


@timing
def part_one(lines: List[str]) -> int:
    races = parse(lines)
    possible_records = list()
    for race in zip(*races):
        min_time, max_time = find_min_max_time(race)
        possible_records.append(1 + max_time - min_time)
    return prod(possible_records)


@timing
def part_two(lines: List[str]) -> int:
    races = tuple(map(int, (''.join(map(str, x)) for x in parse(lines))))
    min_time, max_time = find_min_max_time(races)
    return 1 + max_time - min_time


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day06.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 625_968    // 0.0001 sec
    LOGGER.info(part_two(input_))  # 43_663_323 // 1.0088 sec
