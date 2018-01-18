from operator import itemgetter
from itertools import islice

def ordered_permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i, c in sorted(enumerate(s), key=itemgetter(1)):
            for perm in ordered_permutations(s[:i] + s[i+1:]):
                yield c+perm

def nth_permutation(s, n):
    return list(islice(ordered_permutations(s), n-1, n))[0]

assert nth_permutation('012', 3) == '102'

if __name__ == "__main__":
    print(nth_permutation('0123456789', 1000000))
