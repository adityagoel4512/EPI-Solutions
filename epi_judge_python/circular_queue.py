from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Queue:
    def __init__(self, capacity: int) -> None:
        self._entries = [None] * capacity
        self._head = 0
        self._tail = 0
        self._num_elems = 0

    def enqueue(self, x: int) -> None:
        def resize():
            if self._head == self._tail and self._tail is not None:
                self._tail = len(self._entries)
                self._entries = self._entries[self._head:] + self._entries[:self._head] + [None for _ in self._entries]
                self._head = 0

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_elems += 1
        resize()

    def dequeue(self) -> int:
        head = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        self._num_elems -= 1
        return head

    def size(self) -> int:
        return self._num_elems

def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
