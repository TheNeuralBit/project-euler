# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def divisors(n):
	rtrn = [1]
	for i in range(2, int(n/2) + 1):
		if n % i == 0:
			rtrn.append(i)

	return rtrn

def amicables(n):
	amicables = set()
	for i in range(n):
		if i in amicables: continue
		sumdiv = sum(divisors(i))
		if i != sumdiv and sum(divisors(sumdiv)) == i:
			amicables.add(i)
			amicables.add(sumdiv)
	return amicables

#print(divisors(220))
a = amicables(10000)
print(a)

print(sum(a))
