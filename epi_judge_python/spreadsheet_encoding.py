from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    result = 0
    m = 1
    for d in reversed(col):
        result += m * (ord(d) - ord('A') + 1)
        m *= 26
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
