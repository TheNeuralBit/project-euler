from math import ceil, sqrt

def generate_triangle_numbers():
    n = 1
    s = n
    while True:
        yield s
        n += 1
        s += n

def find_all_divisors(n):
    rtrn = set([1, n])
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            rtrn.add(i)
            rtrn.add(int(n/i))
    return rtrn

if __name__ == "__main__":
    for t in generate_triangle_numbers():
        num_divisors = len(find_all_divisors(t))

        if num_divisors > 500:
            print("%d: %d" % (t, num_divisors))
            break
