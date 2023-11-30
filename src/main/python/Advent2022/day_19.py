"""
https://adventofcode.com/2022/day/19
--- Day 19: Not Enough Minerals ---
"""
import re
from collections import Counter, deque
from copy import deepcopy
from math import prod
from typing import Dict, List

from src.main.python.utilities import LOGGER, timing


def read_blueprint(bp_strs: List[str]):
    reg = re.compile(
        r'Blueprint (?P<bp_no>\d+):.*'
        r'(?P<ore_robot_ore>\d+) ore.*'
        r'(?P<clay_robot_ore>\d+) ore.*'
        r'(?P<obsidian_robot_ore>\d+) ore and (?P<obsidian_robot_clay>\d+) clay.*'
        r'(?P<geode_robot_ore>\d+) ore and (?P<geode_robot_obsidian>\d+) obsidian.*'
    )
    for bp_str in bp_strs:
        yield reg.match(bp_str).groupdict()


def resource_bfs(bp_dict: Dict[str, Dict[str, int]], time: int):
    """
    BFS search to maximize all paths. It takes a long time to run, and while I've
    made some attempts at pruning the paths, some more would help.
    """
    queue = deque()
    start = (
        Counter({
            'ore': 1,
            'clay': 0,
            'obsidian': 0,
            'geode': 0,
        }),
        Counter({
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0,
        }),
    )
    # stop creating new machines if the sum of the costs of outputs equals the
    # number of robots
    resource_maxes = {
        'ore': 1.5 * sum((x['ore'] for x in bp_dict.values())),
        'clay': 1.5 * sum((x['clay'] for x in bp_dict.values())),
        'obsidian': 1.5 * sum((x['obsidian'] for x in bp_dict.values())),
        'geode': float('inf'),
    }
    # also don't make new machines when a certain number of geode machines have been
    # created
    robot_maxes = {
        'ore': 1,
        'clay': 1,
        'obsidian': 15,
        'geode': float('inf'),
    }
    geode_bots = 0
    max_geode = 0
    seen = dict()
    queue.append((0,) + start)

    while queue:
        minutes, robots, resources = queue.popleft()
        max_geode = max(max_geode, resources['geode'])
        tuple_values = tuple(robots.values())
        # for part one, I had the number of geode robots equal to
        # the max (ie if one path got to making geode machines faster,
        # ignore all other paths), but for part two that actually
        # wasn't the best path in all cases. by removing that assumption,
        # this uses a lot of memory (the below doesn't clean up the queue as well)
        if robots['geode'] - 1 > geode_bots:
            geode_bots = robots['geode']
        elif robots['geode'] < geode_bots - 1:
            continue
        if tuple_values in seen:
            if resources <= seen[tuple_values]:
                continue
        if minutes == time:
            continue
        seen[tuple_values] = resources

        for k, v in bp_dict.items():
            if (
                    v <= resources
                    and resources[k] <= resource_maxes[k]
                    and robot_maxes[k] > robots['geodes']
            ):
                bot, res = deepcopy(robots), deepcopy(resources)
                res -= v
                res.update(bot)
                bot.update([k])
                queue.append((minutes + 1, bot, res))
        if resources['ore'] <= resource_maxes['ore']:
            bot, res = deepcopy(robots), deepcopy(resources)
            res.update(bot)
            queue.append((minutes + 1, bot, res))
    return max_geode


def run_turns(i, turns):
    geode_dict = dict()
    for a in read_blueprint(i):
        bp_dict = {
            'geode': Counter({
                'ore': int(a['geode_robot_ore']),
                'obsidian': int(a['geode_robot_obsidian']),
            }),
            'obsidian': Counter({
                'ore': int(a['obsidian_robot_ore']),
                'clay': int(a['obsidian_robot_clay']),
            }),
            'clay': Counter({'ore': int(a['clay_robot_ore'])}),
            'ore': Counter({'ore': int(a['ore_robot_ore'])}),
        }
        geode_dict[int(a['bp_no'])] = resource_bfs(bp_dict, turns)
    return geode_dict


@timing
def part_one(i):
    geode_dict = run_turns(i, turns=24)
    return sum((k * v for k, v in geode_dict.items()))


@timing
def part_two(i):
    geode_dict = run_turns(i[:3], turns=32)
    return prod(geode_dict.values())


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_19.txt', 'r') as f:
        input_ = f.read().splitlines()
    LOGGER.info(part_one(input_))  # 1550
    LOGGER.info(part_two(input_))  # 18630
