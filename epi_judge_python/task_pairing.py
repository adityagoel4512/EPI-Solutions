import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort()
    L = 0
    R = len(task_durations)-1
    res = []
    while L < R:
        res.append(PairedTasks(task_durations[L], task_durations[R]))
        L += 1
        R -= 1
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
