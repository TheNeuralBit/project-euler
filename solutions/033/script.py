#! /usr/bin/env python

def gcd(a ,b):
  if b == 0 :
    return a
  else :
    return gcd(b, a % b)

for num in range(10, 100):
  for denom in range(num + 1, 100):
    div = gcd(num, denom)
    numRed = num/div
    denomRed = denom/div

    num2 = num % 10
    num1 = (num - num2)/10
    denom2 = denom % 10
    denom1 = (denom - denom2)/10

    if(numRed == num1 and denomRed == denom2 and num2 == denom1) or (numRed == num2 and denomRed == denom1 and num1 == denom2):
      print(str(num) + " " + str(denom))
