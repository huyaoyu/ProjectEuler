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
# Created: 2017-09-27
#
# Description
# ===========
#
# The solution of Problem 23 in Project Euler.
#
# Not as fast as those posted on the discussion thread.
#

PEID = 23 # Problem ID in Project Euler.

MAX = 28123

def find_divisors(n):
	"""
	This function is borrowed from PEID 021.

	Return all the proper divisors of n.
	"""

	pd = [1]

	sqrtN = int(math.sqrt(n))

	for d in range(2, sqrtN+1):
		if n % d == 0:
			pd.append(d)
			pair = int(n/d)
			if not pair == d:
				pd.append(pair)

	return pd

def sum_of_proper_divisors(n):
	"""Calculate the sum of all the proper divisors of n."""

	pd = find_divisors(n)

	return sum(pd)

def sum_of_proper_divisors2(n):
	s = 1

	sqrtN = int(math.sqrt(n))

	for d in range(2, sqrtN+1):
		if n % d == 0:
			s += d
			pair = int(n/d)
			if not pair == d:
				s += pair

	return s

if __name__ == '__main__':

	print("This is PEID %03d.\n" % (PEID))

	s28 = sum_of_proper_divisors(28)

	print("s28 = %d.\n" % (s28))

	s12 = sum_of_proper_divisors(12)

	print("s12 = %d.\n" % (s12))

	# Find all the abundant numbers below MAX.

	abundantNumberList = []
	abundantSumList = []

	for i in range(12, MAX+1):
		# Get the sum of all the proper divisors of i.
		s = sum_of_proper_divisors2(i)

		if s > i:
			# Abundant number.
			abundantNumberList.append(i)
			abundantSumList.append(s)

	# Find all the sum of two abundant numbers in abundantNumberList with the sum 
	# below MAX.

	print("Find all the valid numbers...\n")

	nANL = len(abundantNumberList)

	validIntegerList = []

	combinationDict = {}

	for i in range(nANL):
		ai = abundantNumberList[i]

		# print("ai = %d, " % (ai), end="")
		for j in range(i, nANL):
			aj = abundantNumberList[j]

			s = ai + aj

			if s <= MAX:
				if not (s in combinationDict):
					combinationDict[s] = [ai, aj]
			else:
				# print("aj = %d" % (aj))
				break

	# Find the valid numbers.

	for k in range(1, MAX):
		if not (k in combinationDict):
			validIntegerList.append(k)

	print("Sum = %d.\n" % (sum(validIntegerList)))
