"""
https://adventofcode.com/2022/day/11
--- Day 11: Monkey in the Middle ---
"""
import operator
import re
from math import prod
from typing import List

from src.main.python.utilities import LOGGER, timing

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '^': operator.pow,
}


class Monkey:
    def __init__(
            self,
            name: str,
            items: List[int],
            operation_type: str,
            operation_value: str,
            test_divisor: int,
            true_monkey: str,
            false_monkey: str,
    ):
        self.name = name
        self.items = items
        self.operation_type = operation_type
        self.operation_value = operation_value
        self.test_divisor = test_divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.inspections = 0

    def operation(self, x: int):
        self.inspections += 1
        if not self.operation_value.isdigit():
            y = x
        else:
            y = int(self.operation_value)
        return OPERATORS[self.operation_type](y, x)

    def test(self, x: int):
        if x % self.test_divisor == 0:
            return self.true_monkey
        return self.false_monkey


def create_monkey_dict(i: List[str]):
    monkey_dict = dict()
    for mon in i:
        mon_list = re.split(r'\s*\n\s*', mon)
        mon_list = [x.split(': ')[-1].lower() for x in mon_list]
        mon_object = Monkey(
            name=mon_list[0].rstrip(':'),
            items=[int(x) for x in mon_list[1].split(', ')],
            operation_type=mon_list[2].split(' ')[-2],
            operation_value=mon_list[2].split(' ')[-1],
            true_monkey=' '.join(mon_list[4].split(' ')[-2:]),
            false_monkey=' '.join(mon_list[5].split(' ')[-2:]),
            test_divisor=int(mon_list[3].split(' ')[-1]),
        )
        monkey_dict[mon_list[0].rstrip(':')] = mon_object
    return monkey_dict


@timing
def part_one(i: List[str]):
    monkey_dict = create_monkey_dict(i)
    for _ in range(20):
        for key, monkey in monkey_dict.items():
            while monkey.items:
                item = monkey.operation(monkey.items.pop(0)) // 3
                to_monkey = monkey.test(item)
                monkey_dict[to_monkey].items.append(item)
    return prod(sorted([x.inspections for x in monkey_dict.values()])[-2:])


@timing
def part_two(i: List[str]):
    """
    ok, this took a while to realize, but all of the values in the tests are primes.
    I figured that wasn't on accident, so I used the product of that value (because they
    are primes, this is the least common multiple) to mod all the ints before they got
    humungous — and it worked.

    I wasn't completely sure that it would work, so I looked into it:
    https://en.wikipedia.org/wiki/Residue_number_system
    """
    monkey_dict = create_monkey_dict(i)
    big_div_val = prod([x.test_divisor for x in monkey_dict.values()])
    for _ in range(10_000):
        for key, monkey in monkey_dict.items():
            while monkey.items:
                item = monkey.operation(monkey.items.pop(0)) % big_div_val
                to_monkey = monkey.test(item)
                monkey_dict[to_monkey].items.append(item)
    return prod(sorted([x.inspections for x in monkey_dict.values()])[-2:])


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_11.txt', 'r') as f:
        input_ = f.read().split('\n\n')
    LOGGER.info(part_one(input_))  # 50830
    LOGGER.info(part_two(input_))  # 14399640002
