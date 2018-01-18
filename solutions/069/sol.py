from math import ceil
def sieve(n=1024):
    prev_n = 2
    prime = set()
    not_prime = set()
    while True:
        yield from bootstrapped_sieve(prime, not_prime, prev_n, n)
        prev_n = n
        n *= 2


def bootstrapped_sieve(prime, not_prime, prev_n, n):
    for i in prime:
        next_multiple = ceil(prev_n / i)
        for f in range(i*next_multiple, n+1, i):
            not_prime.add(f)

    for i in range(prev_n, n + 1):
        if i in not_prime:
            continue

        for f in range(i*2, n+1, i):
            not_prime.add(f)

        prime.add(i)
        yield i

import numpy as np
from itertools import takewhile

# Based on Euler's product formula:
# https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula
# - Initialize all totient(n) to n
# - Iterate through primes and multiply all their multiples by (1-1/p)
def gen_totients(N):
    totients = np.array(range(N+1),dtype=np.uint32)
    totients[1] = 1

    for prime in takewhile(lambda p: p <= N, sieve()):
        i = prime
        while i <= N:
            totients[i] *= (1-1/prime)
            i += prime

    return totients

if __name__ == "__main__":
    from operator import itemgetter
    print("Finding all phi(n)...")
    totients = gen_totients(1000000)
    print("Finding max n/phi(n)...")
    print(max(((i, i/totients[i]) for i in range(1,1000001)), key=itemgetter(1)))
