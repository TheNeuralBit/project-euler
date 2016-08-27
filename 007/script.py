#! /usr/bin/env python
from math import ceil

def isPrime(n):
  for i in range(2, ceil(n/2) + 1):
    if n % i == 0: return False
  return True

numPrimes = 0
curr = 2
while numPrimes < 10001 :
  if isPrime(curr):
     numPrimes = numPrimes + 1
     print(curr)
  curr = curr + 1
print(curr)
