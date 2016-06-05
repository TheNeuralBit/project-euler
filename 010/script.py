#! /usr/bin/env python

from math import sqrt

size = 2000000

primes = [True]*size

for i in range(2, int(sqrt(size)) + 2):
  if primes[i]:
    print i
    k = i*i
    while k < size:
      if primes[k] and k % i == 0:
        primes[k] = False
#        print str(i) + " " + str(k)
      k = k + 1

sum = 0
for i in range(2,size):
  if primes[i]:
    sum = sum + i
    print i

print sum
