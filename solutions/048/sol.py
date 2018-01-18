from itertools import repeat
from functools import reduce

# Return up the lower digits of n*n
def self_power(n, digits=10):
    return reduce(lambda acc, val: acc*val % 10**digits, repeat(n, n))

if __name__ == "__main__":
    print(reduce(lambda acc, val: (acc+val) % 10**10, (self_power(n) for n in range(1,1001))))
