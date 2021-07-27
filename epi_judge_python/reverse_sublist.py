from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy = ListNode(0, L)
    # find first node of section and element before it
    prev = dummy
    first = dummy.next
    for _ in range(start-1):
        prev = first
        first = first.next

    if first is None:
        return L        
    ahead = first.next
    if ahead is None:
        return L
    for _ in range(finish-start):
        temp = ahead.next
        ahead.next = first
        first = ahead
        ahead = temp
    
    prev.next.next = ahead
    prev.next = first
    return dummy.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
