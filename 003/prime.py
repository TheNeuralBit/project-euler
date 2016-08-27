#! /usr/bin/env python
from math import ceil

num = 600851475143

def isPrime(k):
  for i in range(2, ceil(k/2) + 1):
    if k % i == 0 :
      return False
  return True

for i in range(2, 100000):
  if num % i == 0 and isPrime(i) :
    print(i)
