from test_framework import generic_test


def square_root(k: int) -> int:
    L = 0
    R = k
    # INTS[:L]**2 <= k
    # INTS[R:]**2 > k
    # INTS[L:R]**2 is unknown
    while L <= R:
        M = (L+R)//2
        if M**2 > k:
            R = M-1
        else:
            L = M+1
    return L-1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
