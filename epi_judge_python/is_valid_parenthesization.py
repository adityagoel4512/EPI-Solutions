from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    close_chars = {')': '(', ']': '[', '}': '{'}
    open_chars = []
    for c in s:
        if c in close_chars:
            if not open_chars or not(open_chars.pop() == close_chars[c]):
                return False
        else:
            open_chars.append(c)
    return [] == open_chars


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
