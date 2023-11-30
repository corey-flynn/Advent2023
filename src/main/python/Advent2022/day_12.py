"""
https://adventofcode.com/2022/day/12
--- Day 12: Hill Climbing Algorithm ---
"""
from collections import defaultdict
from copy import deepcopy
from typing import List

from src.main.python.utilities import dijkstra, LOGGER, timing


class Graph:
    START = ord('S')
    END = ord('E')

    def __init__(self, matrix: List[List[int]]):
        self.start = tuple()
        self.end = tuple()
        self.matrix = deepcopy(matrix)
        self.graph = defaultdict(dict)
        self.lowpoints = list()

        self._find_endpoints()

    @property
    def max_i(self):
        """
        return the highest i-value
        """
        return len(self.matrix)

    @property
    def max_j(self):
        """
        return the highest j-value
        """
        return len(self.matrix[0])

    def _find_endpoints(self):
        """
        find the start point, end point, and all low points (ord('a') == 97)
        """
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                match val:
                    case self.START:
                        self.start = (i, j)
                        self.matrix[i][j] = ord('a')
                        self.lowpoints.append((i, j))
                    case self.END:
                        self.end = (i, j)
                        self.matrix[i][j] = ord('z')
                    case 97:
                        self.lowpoints.append((i, j))

    def shortest_path(self) -> int:
        """
        find the shortest path from some start to some end
        """
        return dijkstra(graph=self.graph, start=self.start, end=self.end)

    def find_from_any_a(self) -> int:
        """
        from many start points, find the shortest to a fixed endpoint
        """
        shortest_path = float('inf')
        for p in self.lowpoints:
            dist = dijkstra(graph=self.graph, start=p, end=self.end)
            if dist < shortest_path:
                shortest_path = dist
        return shortest_path

    def create_graph(self) -> None:
        """
        for each point, get matrix neighbors. if that neighbor is at most one value
        higher than the current node, create a (one-way) path to that node with
        a weight of `1`
        """
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                for point_ in zip([i, i, i+1, i-1], [j+1, j-1, j, j]):
                    if point_[0] in (self.max_i, -1) or point_[1] in (self.max_j, -1):
                        continue
                    neighbor_val = self.matrix[point_[0]][point_[1]]
                    if neighbor_val - val <= 1:
                        self.graph[(i, j)][point_] = 1


@timing
def part_one(i):
    g = Graph(i)
    g.create_graph()
    return g.shortest_path()


@timing
def part_two(i):
    g = Graph(i)
    g.create_graph()
    return g.find_from_any_a()


if __name__ == '__main__':
    with open('../../resources/Advent2022/day_12.txt', 'r') as f:
        input_ = [[ord(y) for y in x] for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 449
    LOGGER.info(part_two(input_))  # 443
