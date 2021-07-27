from test_framework import generic_test
from string import hexdigits

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # convert to base 10
    m = 1
    num = 0
    for digit in reversed(num_as_string[num_as_string[0] == '-':]):
        num += int(digit, b1) * m
        m *= b1
    def build_string(n):
        if n == 0:
            return ''
        else:
            d, r = divmod(n, b2)
            return f'{build_string(d)}{hexdigits[r].upper()}'
    return ('-' if num_as_string[0] == '-' else '') + build_string(num)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
