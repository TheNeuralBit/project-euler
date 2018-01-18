#! /usr/bin/env python

sum = 0
for i in range(1, 101):
  sum = sum + i
sumsquared = sum * sum

sum = 0
for i in range(1,101):
  sum = sum + i*i
print(sumsquared - sum)
