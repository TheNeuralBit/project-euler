def fibgen():
    lastlast = 1
    last = 1
    yield lastlast
    yield last
    while True:
        tmp = last + lastlast
        yield tmp

        lastlast = last
        last = tmp

LIM = 10**999
for i, n in enumerate(fibgen(), 1):
    if n >= LIM:
        print("{}, {}".format(i, n))
        break
