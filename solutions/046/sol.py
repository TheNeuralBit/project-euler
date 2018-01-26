from math import ceil

def sieve():
    prev_n = 2
    n = 1024
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

class Primes:
    def __init__(self):
        self.last = -1
        self.sieve = sieve()
        self.primes = set()

    def check(self, n):
        if self.last <= n:
            for i in self.sieve:
                self.primes.add(i)
                if i > n:
                    self.last = i
                    break
        return (n in self.primes)


def non_primes():
    last = 1
    for prime in sieve():
        yield from range(last+1, prime)
        last = prime

primes = Primes()

def goldbach(n):
    i = 1
    while True:
        diff = n - 2*i*i
        if diff < 0: return False
        if primes.check(diff): return (diff, i)
        i += 1

assert goldbach(9)  == (7,1)
assert goldbach(33) == (31,1)

for num in filter(lambda n: n % 2 == 1, non_primes()):
    g = goldbach(num)
    if g is False:
        print(num)
        break
