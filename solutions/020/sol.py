def factorial(n):
    rtrn = 1
    for i in range(2, n+1):
        rtrn *= i
    return rtrn

print(sum(int(c) for c in str(factorial(100))))
