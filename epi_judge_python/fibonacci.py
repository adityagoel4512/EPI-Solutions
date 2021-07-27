from test_framework import generic_test


def fibonacci(n: int) -> int:
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x+y	
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
