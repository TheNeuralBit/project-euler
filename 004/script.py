#! /usr/bin/env python

from math import ceil

def nthDigit(x , n):
  return ((x-x%10**n)/(10**n))%10

def isPalindrome(product):
  l = len(str(product)) - 1
  for i in range(0, ceil(l/2) + 1):
    if  nthDigit(product, l - i) != nthDigit(product, i): return False
  return True

max = 0
for i in range(100, 1000):
  for k in range(100, 1000):
    product = i*k
    if isPalindrome(product) and product > max: max =  product

print(max)
