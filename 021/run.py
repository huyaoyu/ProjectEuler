import os
import sys
import math
import numpy as np

# Author
# ======
#
# Yaoyu Hu <huyaoyu@sjtu.edu.cn>
#
# Date
# ====
#
# Created: 2017-09-25
#
# Description
# ===========
#
# The solution of Problem 21 in Project Euler.
#
# It is best to search below sqrt(n) when trying to calculate
# all the proper divisors of an integer n.
#
# Make sure to check the following two situations:
# (1) The two numbers of a pair are identical. And,
# (2) Whether [a, b] and [b, a] are treated as different pairs.
#

PEID = 21 # Problem ID in Project Euler.

MAX = 10000

def find_divisors(n):
	"""Return all the proper divisors of n."""

	pd = [1]

	sqrtN = int(math.sqrt(n))

	for d in range(2, sqrtN+1):
		if n % d == 0:
			pd.append(d)
			pd.append(int(n/d))

	return pd

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	print("Test find_divisors().\n")

	pd = find_divisors(220)

	print(pd)

	print("Sum of all the proper divisor of 220 is %d.\n" % (sum(pd)))

	flagList = np.zeros(MAX)

	AmicableNumberPairs = []

	for n in range(2, MAX+1):
		# Check if this number has been designated as Amicable number.
		if 1 == flagList[n-1]:
			continue

		# Get the list of proper divisors of n.
		pd  = find_divisors(n)
		sn0 = sum(pd)

		if sn0 > MAX:
			continue

		# Get the list of proper divisors of sn0.
		pd  = find_divisors(sn0)
		sn1 = sum(pd)

		if sn1 > MAX:
			continue

		if n == sn1 and not n == sn0:
			# Find a pair of Amicable numbers.
			AmicableNumberPairs.append([n, sn0])

			flagList[n - 1]   = 1
			flagList[sn0 - 1] = 1

	print(AmicableNumberPairs)

	acc = 0

	for anp in AmicableNumberPairs:
		acc += sum(anp)

	print("acc = %d.\n" % acc)

if __name__ == '__main__':
	main()