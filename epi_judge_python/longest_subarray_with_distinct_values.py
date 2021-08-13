from typing import List

from test_framework import generic_test

from collections import OrderedDict

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    current_subset = OrderedDict.fromkeys([]) # maintains map from entry -> index in A
    max_len = 0
    for i, entry in enumerate(A):
        if entry in current_subset:
            max_len = max(max_len, len(current_subset))
            prev_index = current_subset[entry]
            entries_to_evict = len(current_subset) - (i - prev_index)
            for _ in range(entries_to_evict):
                current_subset.popitem(last=False)
        current_subset[entry] = i
        current_subset.move_to_end(entry, last=True)    
    
    max_len = max(max_len, len(current_subset))

    return max_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
