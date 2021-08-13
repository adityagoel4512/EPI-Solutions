import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A: List[Event]) -> int:
    E = [p for a in A for p in ((a.start, False), (a.finish, True))]
    E.sort()
    current_count = 0
    result = 0
    for e in E:
        if e[1]:
            # start of event
            current_count -= 1
        else:
            current_count += 1
        result = max(result, current_count)
    return result

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
