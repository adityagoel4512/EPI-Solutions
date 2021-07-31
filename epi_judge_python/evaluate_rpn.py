from test_framework import generic_test


def evaluate(expression: str) -> int:
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}
    values = []
    for tok in expression.split(','):
        if tok in operators:
            v1 = values.pop()
            v2 = values.pop()
            values.append(operators[tok](v2, v1))
        else:
            values.append(int(tok))
    return values[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
