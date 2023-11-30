import logging
import heapq
import operator
from functools import wraps
from time import time
from typing import Dict, Iterable, Union

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
LOGGER = logging.getLogger()


def timing(f: callable):
    """
    https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    :param f: function
    :return:
    """
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        LOGGER.info(f'func:{f.__name__} took: {te-ts:2.4f} sec')
        return result
    return wrap


def range_inc(*args):
    """
    range including the max number
    :param args: same arguments passed to range builtin
    :return: range generator
    """
    args = list(args)
    if len(args) > 1:
        args[1] += 1
    else:
        args[0] += 1
    return range(*args)


def dijkstra(
        graph: Dict[tuple, Dict[tuple, int]],
        start,
        end=None,
) -> Union[int, dict]:
    """
    dijkstra's shortest path algorithm
    :param graph: nested dictionary of points to points with distance / weights
    :param start: start point
    :param end: end point
    :return: shortest distance between start and end
    """
    visited_nodes = set()
    queue = list()
    distances = {x: float('inf') for x in graph}
    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        visited_nodes.add(current_node)
        for adj_node, weight in graph[current_node].items():
            if adj_node in visited_nodes or adj_node not in distances:
                continue
            distance = distances[current_node] + weight
            if distances[adj_node] > distance:
                distances[adj_node] = distance
                heapq.heappush(queue, (distance, adj_node))
    if end:
        return distances[end]
    return distances


def to_ints(i: Iterable[str]) -> tuple:
    """
    build a tuple of integers from some iterable of strings
    :param i: iterable
    :return: tuple of integers
    """
    return tuple(int(x) for x in i)


def manhattan_distance(point_a: Iterable[int], point_b: Iterable[int]) -> int:
    """
    find a manhattan distance between two points
    """
    return sum(abs(operator.sub(*x)) for x in zip(point_a, point_b))


def key_by_val(d: dict, val):
    """return a dictionary key by its value"""
    return list(d.keys())[list(d.values()).index(val)]
