from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    # s1, s2, s3, s4 => cap at s1 caps s1, s2, s3, s4 => payroll = 4 * s1.
    #                => cap at k => if there are m salaries <= k and n salaries > k => n * k + preceding salaries

    current_payroll = 0.0
    for i, salary in enumerate(current_salaries):
        # current_payroll = sum(current_salaries[:i])
        remaining_payroll = target_payroll - current_payroll
        remaining_salaries = len(current_salaries)-i
        candidate_cap = remaining_payroll / remaining_salaries
        if candidate_cap <= salary:
            return candidate_cap
        current_payroll += salary

    # [20, 30, 40, 90, 100], 210
    # 0 210 5 => cand cap = 42
    # 20 190 4 => cand cap => 47.5
    # 50 160 3 => cand cap => 53.333
    # 90 120 2 => cand cap => 60
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
