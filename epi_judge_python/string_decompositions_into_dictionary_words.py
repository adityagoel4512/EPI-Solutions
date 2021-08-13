from typing import List

from test_framework import generic_test

from collections import Counter 

def find_all_substrings(s: str, words: List[str]) -> List[int]:
    unit_size = len(words[0])
    word_counter = Counter(words)
    index_to_string = {i:s[i:i+unit_size] for i in range(0, len(s)-unit_size+1)}
    result = []
    for i in range(0, len(s)-(unit_size*len(words))+1):
        section_count = Counter(index_to_string[j] for j in range(i, i+(unit_size*len(words)), unit_size))
        if section_count == word_counter:
            result.append(i)
    return result
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
