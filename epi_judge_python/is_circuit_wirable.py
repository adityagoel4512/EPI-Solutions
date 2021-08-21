import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []

from collections import deque

def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    left, right = range(2)

    def dfs(vertex, required_colour):
        print(vertex.d, required_colour)
        if vertex.d == required_colour:
            return True
        elif vertex.d != required_colour:
            return False

        # vertex.d == -1
        vertex.d = required_colour

        new_colour = left if required_colour == right else right
        print(new_colour, vertex.edges)
        for neighbour in vertex.edges:
            print("neigbour", neighbour.d)
            if not(dfs(neighbour, new_colour)):
                return False

        return True

    return all(dfs(vertex, left) for vertex in graph if vertex.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
