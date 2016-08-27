#! /usr/bin/env python

from math import sqrt

size = 2000000

primes = [True]*size

for i in range(2, int(sqrt(size)) + 2):
  if primes[i]:
    for k in range(i*2, size, i):
        primes[k] = False

sum = 0
for i in range(2, size):
  if primes[i]:
    sum = sum + i
    print(i)

print(sum)
