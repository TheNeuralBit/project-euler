def gen_corners(size):
    curr = 1
    step = 2
    yield curr
    while step < size:
        for i in range(4):
            curr += step
            yield curr
        step += 2

assert sum(gen_corners(5)) == 101

if __name__ == "__main__":
    print(sum(gen_corners(1001)))
