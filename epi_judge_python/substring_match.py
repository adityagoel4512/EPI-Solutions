from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if s=='':
        return 0

    if len(t) < len(s):
        return -1
    def char_hashcode(c):
        # A-Z = 0-25
        # a-z = 26-51
        return ord(c)-ord('A') if c <= 'Z' else ord(c)-ord('a') + 26
    base = 52
    def compute_hash(length, st):
        value = 0
        for i in range(length):
            value *= base
            value += char_hashcode(st[i])
        return value

    s_hash = compute_hash(len(s), s)
    cur_hash = compute_hash(len(s), t) 
    
    if cur_hash == s_hash:
        return 0
   
    max_pow = base ** (len(s)-1)

    for i in range(len(s), len(t)+1):
        # cur_hash = hash of t[i-len(s):i]
        if cur_hash == s_hash:
            return i-len(s)
        if i != len(t):
            # roll hash
            cur_hash -= max_pow * char_hashcode(t[i-len(s)])
            cur_hash *= base
            cur_hash += char_hashcode(t[i])
    return -1 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
