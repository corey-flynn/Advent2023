"""
https://adventofcode.com/2023/day/5
"""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import Dict, Generator, List, Tuple

from src.main.python.utilities import batched, LOGGER, timing


RATIO_TITLES = (
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
)


class RangeDict(dict):
    """A dictionary that allows accessing values based on a range of keys.

    This custom dictionary implementation is designed to return a value when
    a key falls within any of the specified ranges in the dictionary. It raises
    a ValueError if the key does not fall within any ranges.
    """
    @property
    def sorted_keys(self):
        return sorted(self.keys())

    @property
    def sorted_starts(self):
        return sorted(x[0] for x in self.keys())

    @property
    def sorted_stops(self):
        return sorted(x[1] for x in self.keys())

    def binary_key_search(self, item: int):
        """
        binary search to find only the range that contains the
        searched-for item.
        """
        idx = bisect_left(self.sorted_keys, (item,)) - 1
        if idx >= 0 and self.sorted_keys[idx][0] < item <= self.sorted_keys[idx][1]:
            return self.sorted_keys[idx]
        elif idx+1 < len(self.sorted_keys) and self.sorted_keys[idx+1][0] == item:
            return self.sorted_keys[idx+1]

    def get(self, item: int, default=None):
        key = self.binary_key_search(item)
        if key:
            return self[key]
        return default

    def get_range(self, start: int, stop: int):
        """
        a lot of logic here, but this finds ranges in the range dictionary
        and yields all ranges subtracted by their values. this is wildly efficient,
        but could be a little cleaner.
        """
        left_idx = bisect_left(self.sorted_stops, start)
        right_idx = bisect_right(self.sorted_starts, stop)
        ranges = self.sorted_keys[left_idx:right_idx]
        for r_start, r_stop in ranges:
            if r_start <= start < r_stop and not r_start <= stop < r_stop:
                sub = self[(r_start, r_stop)]
                yield start-sub, r_stop-sub
                start = r_stop+1
            elif not r_start <= start < r_stop and not r_start <= stop < r_stop:
                yield start, r_stop
                start = r_stop+1
            elif r_start <= start < r_stop and r_start <= stop < r_stop:
                sub = self[(r_start, r_stop)]
                yield start-sub, stop-sub
                start = r_stop+1
            else:
                yield start, stop
        if start < stop:
            yield start, stop


def recursive_map(
        d: Dict[str, RangeDict],
        level: str,
        start: int,
        stop: int,
) -> Generator[Tuple[int, int], None, None]:
    """
    recursively scan the dict of RangeDicts to find all mappings or all ranges
    """
    for r_start, r_stop in d[level].get_range(start, stop):
        if level != RATIO_TITLES[-1]:
            next_level = RATIO_TITLES[RATIO_TITLES.index(level)+1]
            for result in recursive_map(d=d, level=next_level, start=r_start, stop=r_stop):
                yield result
        else:
            for value in d[level].get_range(start, stop):
                yield value


def parse(lines) -> Tuple[List[int], Dict[str, RangeDict[range, int]]]:
    seeds, *maps = lines
    heading = ''
    d = defaultdict(RangeDict)
    for line in lines:
        if not line:
            heading = ''
            continue
        elif not line[0].isdigit():
            heading = line.replace(' map:', '')
            continue
        destination, source, range_ = (int(x) for x in line.split())
        d[heading][(source, source+range_-1)] = source - destination
    return [int(x) for x in seeds.split()[1:]], d


@timing
def part_one(lines) -> int:
    seeds, maps = parse(lines)
    low_val = float('inf')
    for val in seeds:
        for ratio in RATIO_TITLES:
            val -= maps[ratio].get(val, 0)
        if val < low_val:
            low_val = val
    return low_val


@timing
def part_two(lines) -> int:
    seeds, maps = parse(lines)
    low_val = float('inf')
    for start, range_ in batched(seeds, 2):
        locations = recursive_map(maps, level='seed-to-soil', start=start, stop=start+range_)
        val = min([x[0] for x in locations])
        if val < low_val:
            low_val = val
    return low_val


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day05.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 111_627_841 // 0.0007 sec
    LOGGER.info(part_two(input_))  # 69_323_688  // 0.0083 sec
