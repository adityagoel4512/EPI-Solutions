from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    # M, N and M < N, j remaining
    # if we picked N, the total waiting time is K + 1/2j(j+1) * N + R + 1/2k(k+1) * M
    # if we picked M, K + 1/2j(j+1) * M + R + 1/2k(k+1) * N => k < j, M < N => pick M

    service_times.sort()

    acc = 0
    total = 0
    for service_time in service_times:
        total += acc
        acc += service_time
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
