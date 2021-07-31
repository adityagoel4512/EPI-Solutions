from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # Each building is from East to West
    # If building is taller than all buildings after it, it has a sunset
    buildings_with_sunset = []
    for i, h in enumerate(sequence):
        while buildings_with_sunset and buildings_with_sunset[-1][1] <= h:
            buildings_with_sunset.pop()
        buildings_with_sunset.append((i, h))
    return [bi[0] for bi in reversed(buildings_with_sunset)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
