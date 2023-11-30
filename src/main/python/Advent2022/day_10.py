"""
https://adventofcode.com/2022/day/10
--- Day 10: Cathode-Ray Tube ---
"""
from typing import List

from src.main.python.utilities import LOGGER, timing


@timing
def part_one(reg: List[str]) -> int:
    """
    keep track of cycles and total frequency where `noop` is one cycle and
    `addx <n>` is two cycles, where n is added after those cycles have completed
    :param reg: list of commands
    :return: the sum of the product of count and cycle number at the twentieth cycle
             and every fortieth cycle after that
    """
    cycle = 0
    counter = 1
    ret_list = []
    for inst in reg:
        if inst == 'noop':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                ret_list.append(counter * cycle)
        else:
            _, val = inst.split()
            for _ in range(2):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    ret_list.append(counter * cycle)
            counter += int(val)
    return sum(ret_list)


@timing
def part_two(reg) -> str:
    """
    Map out visually represented letters in a matrix. when counter is within 1 value of
    cycle modulo 40, represent that index of the cycle with a hash. arrays are selected
    by cycle // 40.
    :param reg: list of commands
    :return: a string version of the matrix for more easier reading
    """
    cycle = 0
    counter = 1
    ret_list = [[x for x in '.' * 40] for _ in range(6)]
    for i, inst in enumerate(reg):
        if inst == 'noop':
            if cycle % 40 in range(counter-1, counter+2):
                ret_list[cycle // 40][cycle % 40] = '#'
            cycle += 1
        else:
            _, val = inst.split()
            for _ in range(2):
                if cycle % 40 in range(counter-1, counter+2):
                    ret_list[cycle // 40][cycle % 40] = '#'
                cycle += 1
            counter += int(val)
    return '\n' + '\n'.join([''.join(x) for x in ret_list])


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_10.txt', 'r') as f:
        input_ = f.read().splitlines()
    LOGGER.info(part_one(input_))  # 13180
    LOGGER.info(part_two(input_))  # EZFCHJAB
