"""
https://adventofcode.com/2022/day/20
--- Day 20: Grove Positioning System ---
"""
from typing import Dict, List, Tuple

from src.main.python.utilities import LOGGER, timing, key_by_val


def rotate_values(values: List[int], value_dict: Dict[float, Tuple[int, int]]):
    """
    with a list of orignal values in order and a dictionary of new positions,
    this rearranges the indices of the list based on their value
    :param values: value list, this will not be updated
    :param value_dict: value dictionary with current index as keys. this dictionary
                       is updated inplace
    :return: return the values of the dictionary sorted by their current value
    """
    v_len = len(values)
    max_ind = v_len - 1
    for i, n in enumerate(values):
        cur_i = key_by_val(value_dict, (i, n))
        orig_i, val = value_dict.pop(cur_i)
        # values that end up at index 0 are at the end of the list
        to_i = ((cur_i + val) % max_ind) or max_ind
        if val == 0:
            value_dict[cur_i] = (orig_i, val)
            continue
        if to_i < cur_i:
            rotate = -1
        else:
            rotate = 1
        for i_ in range(int(cur_i), int(to_i), rotate):
            bump_from_key = float(i_ + rotate) % v_len
            bump_to_key = float(i_) % v_len
            value_dict[bump_to_key] = value_dict.pop(bump_from_key)
        value_dict[to_i] = (i, val)
    return [x[1][1] for x in sorted(value_dict.items(), key=lambda v: v[0])]


@timing
def part_one(i: List[int]):
    value_dict = {float(i): (i, n) for i, n in enumerate(i)}
    decrypt = rotate_values(i, value_dict)
    # use modulo to work with testcase
    return (
            decrypt[(decrypt.index(0) + 1_000) % (len(i))]
            + decrypt[(decrypt.index(0) + 2_000) % (len(i))]
            + decrypt[(decrypt.index(0) + 3_000) % (len(i))]
    )


@timing
def part_two(i: List[int]):
    decryption_key = 811_589_153
    i = [x * decryption_key for x in i]
    value_dict = {float(i): (i, n) for i, n in enumerate(i)}
    for _ in range(10):
        decrypt = rotate_values(i, value_dict)
    # use modulo to work with testcase
    return (
            decrypt[(decrypt.index(0) + 1_000) % (len(i))]
            + decrypt[(decrypt.index(0) + 2_000) % (len(i))]
            + decrypt[(decrypt.index(0) + 3_000) % (len(i))]
    )


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_20.txt', 'r') as f:
        input_ = [int(x) for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 7713
    LOGGER.info(part_two(input_))  # 1664569352803
