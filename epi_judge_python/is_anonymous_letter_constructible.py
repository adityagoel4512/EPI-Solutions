from test_framework import generic_test

from collections import Counter
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_count = Counter(letter_text)
    magazine_count = Counter(magazine_text)
    return not (letter_count-magazine_count)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
