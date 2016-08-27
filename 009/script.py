from math import sqrt

def search():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = sqrt(a*a+b*b)
            result = a + b + sqrt(a*a+b*b)
            if result == 1000:
                return (a, b, c)
            elif result > 1000:
                break

if __name__ == "__main__":
    a, b, c = search()
    print("%d^2 + %d^2 = %d^2" % (a, b, c))
    print("%d + %d + %d = 1000" % (a, b, c))
    print("%d*%d*%d = %d" % (a, b, c, a*b*c))
