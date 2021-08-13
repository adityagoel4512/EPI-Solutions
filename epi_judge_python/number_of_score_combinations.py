from typing import List

from test_framework import generic_test

from functools import lru_cache
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:

    @lru_cache(None)
    def helper(cur_score, max_score_idx):
        if cur_score < 0 or max_score_idx < 0:
            return 0
        elif cur_score == 0:
            return 1
        return helper(cur_score-individual_play_scores[max_score_idx], max_score_idx) + (0 if max_score_idx == 0 else helper(cur_score, max_score_idx-1))

    return helper(final_score, len(individual_play_scores)-1)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
