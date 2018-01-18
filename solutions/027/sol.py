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

class PrimeChecker:
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


def polynomial_gen(a, b):
    n = 0
    while True:
        yield n*n + a*n + b
        n += 1

p = PrimeChecker()
def prime_count(g):
    return len(list(takewhile(p.check, g)))

if __name__ == "__main__":
    from itertools import takewhile
    max_length = -1
    for a in range(-1000, 1000 + 1):
        for b in range(-1000, 1000 + 1):
            length = prime_count(polynomial_gen(a, b))
            if length > max_length:
                print("({},{}): {}".format(a, b, length))
                max_length = length
                max_coeff = (a, b)

    print("{} * {} = {}".format(max_coeff[0], max_coeff[1], max_coeff[0]*max_coeff[1]))
