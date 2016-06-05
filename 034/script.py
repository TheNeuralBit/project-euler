#! /usr/bin/env python

import math

def nthDigit(x , n):
  return ((x-x%10**n)/(10**n))%10

def factorial(x):
  rtrn = 1
  for i in range(1, x + 1): rtrn = rtrn * i
  return rtrn

def factorialSum(x):
  rtrn = 0;
  for i in range(0, len(str(x))):
    rtrn = rtrn + factorial(nthDigit(x, i))
  return rtrn

# cannot be greater than 1999999
# after that all factSums are less than num
# (could stop a little earlier, but this is good enough)
for i in range(10, 1999999):
  numLess = 0
  factSum = factorialSum(i)
  if factSum == i : print i
