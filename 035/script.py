#! /usr/bin/env python

from math import sqrt

def rotate(x):
  l = len(str(x)) - 1
  firstDigit = nthDigit(x, l)
  return int((x-firstDigit*(10**l))*10 + firstDigit)

def nthDigit(x , n):
  return ((x-x%10**n)/(10**n))%10

size = 1000000

primes = [True]*size

print("Calculating Primes....")
for i in range(2, int(sqrt(size)) + 2):
  if primes[i]:
    print(i)
    for k in range(2*i, size, i):
      primes[k] = False

print()
print()
print("Finding Circular...")
count = 0
for i in range(2,size):
  if primes[i] and str(i).find('0') == -1:
    length = len(str(i))
    curr = i
    circular = True
    for j in range(1, length):
      curr = rotate(curr)
#      if primes[curr]:
#        primes[curr] = False
      if not primes[curr]:
        circular = False
        break;
    if circular:
      print(i)
      count = count + 1

print("Number circular: %d" % count)
