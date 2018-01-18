from math import ceil, log10

def is_nth_power_sum(x, n):
    return sum(int(digit)**n for digit in str(x)) == x

def find_all_nth_power_sums(n):
    # First identify N, the highest number we have to check

    # ceil(log10(x)) is the number of digits needed to represent x
    # increment ndigits until we find a value where 9**n*ndigits (the nth power
    # sum of the largest possible number with ndigits) takes < ndigits to represent
    ndigits = 1
    while ceil(log10(9**n*ndigits)) >= ndigits: ndigits += 1
    N = 9**n*(ndigits-1)

    for i in range(2, N+1):
        if is_nth_power_sum(i, n): yield i

assert is_nth_power_sum(1634,4)
assert is_nth_power_sum(8208,4)
assert is_nth_power_sum(9474,4)

assert sum(find_all_nth_power_sums(4)) == 19316
fives = list(find_all_nth_power_sums(5))
print(fives)
print(sum(fives))
