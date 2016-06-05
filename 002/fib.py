#! /usr/bin/env python

last = 0
fib = 1
sum = 0
while fib < 4000000:
  if fib % 2 == 0:
    sum = sum + fib
    print fib
  temp = fib
  fib = fib + last
  last = temp
print sum
