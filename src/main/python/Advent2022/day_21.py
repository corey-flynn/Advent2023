"""
https://adventofcode.com/2022/day/21
--- Day 21: Monkey Math ---
"""
from typing import Dict

from src.main.python.utilities import LOGGER, timing


REV_OPERATORS = {
    '-': '+',
    '+': '-',
    '*': '/',
    '/': '*',
}


def collapse_eqn(d: Dict[str, str]):
    eqns = d.copy()
    for k, v in d.items():
        if v.isdigit():
            exec(f'{k} = {v}')
            eqns[k] = eval(v)
    while not isinstance(eqns['root'], (int, float)):
        for k, v in eqns.items():
            try:
                exec(f'{k} = {v}')
                eqns[k] = eval(v)
            except (NameError, TypeError):
                continue
    return eqns


@timing
def part_one(d: Dict[str, str]):
    return collapse_eqn(d)['root']


@timing
def part_two(d: Dict[str, str]):
    """
    I don't think this works for all solutions, specifically certain division
    solutions, but it worked for this set and I'm going to leave it
    """
    graph = dict()
    ce = collapse_eqn(d)
    eqn_order = list()
    for k, v in d.items():
        if v.isdigit():
            continue
        graph[v[:4]] = k
        graph[v[-4:]] = k
    start_node = 'humn'
    if d['root'][:4] in eqn_order:
        comp_monkey = ce[d['root'][:4]]
    else:
        comp_monkey = ce[d['root'][-4:]]
    while True:
        start_node = graph[start_node]
        if start_node == 'root':
            break
        eqn_order.insert(0, start_node)
    for k in eqn_order:
        eqn = d[k]
        left, op, right = eqn.split()
        if right not in eqn_order and right != 'humn':
            print(right)
            e = f'{comp_monkey} {REV_OPERATORS[op]} {ce[right]}'
        elif op == '-':
            e = f'-{comp_monkey} + {ce[left]}'
        else:
            e = f'{comp_monkey} {REV_OPERATORS[op]} {ce[left]}'
        comp_monkey = eval(e)
    return comp_monkey


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_21.txt', 'r') as f:
        input_ = {x.split(': ')[0]: x.split(': ')[1] for x in f.read().splitlines()}
    LOGGER.info(part_one(input_))  # 159591692827554
    LOGGER.info(part_two(input_))  # 3509819803065
