"""
https://adventofcode.com/2023/day/7
"""
from collections import Counter
from functools import cached_property
from typing import Dict, Union

from src.main.python.utilities import LOGGER, timing

CARD_ORDER = 'AKQJT98765432'


class Hand:
    """camel poker Hand class to sort hands. and storer bids."""
    def __init__(self, hand: str, bid: int, wild: Union[str, bool] = False):
        self.hand = hand
        self.bid = bid
        self.wild = wild

    def __gt__(self, other_hand):
        """
        Sorting the hands is relatively straight-forward, first by value
        of the hand (four of a kind, two-pair, etc.), then by comparing
        the current order of the cards. High cards only matter if they are
        higher in a certain index.

        built in python iterable sorting handles these cases, so this just
        handles the sorting logic flow.
        """
        if self.pattern == other_hand.pattern:
            return self.hand_numbers > other_hand.hand_numbers
        return self.pattern > other_hand.pattern

    @property
    def pattern(self):
        hand_pattern = list(sorted(Counter(self.hand).values(), reverse=True))
        if self.joker_count:
            hand_pattern.remove(self.joker_count)
            if hand_pattern:
                hand_pattern[0] += self.joker_count
            else:
                # if all jokers, then joker hand pattern will be (5,)
                hand_pattern = [5]
        return tuple(hand_pattern)

    @cached_property
    def hand_numbers(self):
        """Get value of card from defined order."""
        return tuple(self.card_order[::-1].index(x) for x in self.hand)

    @cached_property
    def card_order(self):
        """Use global order unless there is a wild, which will be last."""
        if self.wild:
            return CARD_ORDER.replace(self.wild, '') + self.wild
        else:
            return CARD_ORDER

    @cached_property
    def joker_count(self):
        """Find count of all Jokers."""
        if self.wild:
            return self.hand.count(self.wild)
        return 0


def parse(lines, wild: Union[str, bool] = False) -> Dict[str, Hand]:
    d = list()
    for line in lines:
        hand, bid = line.split()
        d.append((hand, Hand(hand=hand, bid=int(bid), wild=wild)))
    return d


@timing
def part_one(lines) -> int:
    games = parse(lines)
    return sum(
        x[1].bid * (i + 1) for i, x in
        enumerate(sorted(games, key=lambda x: x[1]))
    )


@timing
def part_two(lines) -> int:
    games = parse(lines, wild='J')
    return sum(
        x[1].bid * (i + 1) for i, x in
        enumerate(sorted(games, key=lambda x: x[1]))
    )


if __name__ == '__main__':
    with open('../../resources/Advent2023/Day07.txt', 'r') as f:
        input_ = f.read().split('\n')
    LOGGER.info(part_one(input_))  # 248_396_258 // 0.0812 sec
    LOGGER.info(part_two(input_))  # 246_436_046 // 0.0994 sec
