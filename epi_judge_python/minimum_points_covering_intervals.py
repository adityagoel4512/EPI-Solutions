import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    # brute force => for increasing number of visits i = 1, ...: find all groups of that length and check if they cover every interval
    # d[i] =>
    intervals.sort(key=lambda interval: interval.right)
    # examine right points
    #[0, 3], [3, 4], [2, 6], [6, 9] -> [0, 3], [2, 6], [3, 4], [6, 9]
    result = 0
    i = 0
    while i < len(intervals):
        right = intervals[i].right
        while i != len(intervals)-1 and right >= intervals[i+1].left:
            i += 1
        i += 1
        result += 1
    return result

@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
