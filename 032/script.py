#! /usr/bin/env python

def nthDigit(x , n):
  return ((x-x%10**n)/(10**n))%10

def panDigital(a, b, c):
  if str(a).find('0') != -1 or str(b).find('0') != -1 or str(c).find('0') != -1:
    return False
  for k in range(1, 10):
    numFound = 0
    for n in range(0, len(str(a))):
      if nthDigit(a, n) == k : numFound = numFound + 1
    for n in range(0, len(str(b))):
      if nthDigit(b, n) == k : numFound = numFound + 1
    for n in range(0, len(str(c))):
      if nthDigit(c, n) == k : numFound = numFound + 1
    if numFound != 1 : return False
  return True

for i in range(2, 10):
  for j in range(1000, 5000):
    product = i * j
    if panDigital(i, j, product):
      print str(i) + " * " + str(j) + " = " + str(product)

for i in range(10, 99):
  for j in range(100, 999):
    product = i * j
    if panDigital(i, j, product):
      print str(i) + " * " + str(j) + " = " + str(product)
