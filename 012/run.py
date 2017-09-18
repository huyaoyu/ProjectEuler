
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
# Created: 2017-09-18
#
# Description
# ===========
#
# The solution of Problem 12 in Project Euler.
#

PEID = 12 # Problem ID in Project Euler.

MAX = 500

def get_max_exponent(n, p):
	"""
	This function is borrowed from PEID 005.
	Get the maximum possible exponent m that satisfy n % p^m == 0. 
	"""

	m      = 0
	localN = n
	r      = 0

	while 0 == r:
		r = localN % p

		if 0 == r:
			m += 1
			localN = localN // p

	return m, localN

def prime_factorization(n):
	"""
	This function is borrowed from PEID 005.
	Return a dictionary that contains the results of its prime factorization.
	"""

	if 1 == n:
		return {1:1}

	# Duplicate n.
	localN = n

	# Find the square root of n.
	# s = int(math.sqrt(n)) + 1
	p = 2
	d = {}

	flagNonPrime = 0

	while True:
		# Check if p could evenly divide localN
		if 0 == localN % p:
			# Get the maximum exponent.
			m, localN = get_max_exponent(localN, p)

			# Save the prime number and exponent.
			d[p] = m

			flagNonPrime = 1

			if 1 == localN:
				break

		p += 1

	# Check if n is a prime number.
	if 0 == flagNonPrime:
		d[n] = 1

	return d

def transform_from_dict_to_lists(d):
	"""
	The element in dictionary d is split into two lists.
	"""

	# baseList = []
	# expList  = []
	# for base, exp in d.items():
	# 	baseList.append(base)
	# 	expList.append(exp)

	baseList = d.keys()
	expList  = d.values()

	return baseList, expList

def sum_of_arithmetic_series(first, last, n):
	"""Get the sum of a arithmetic series."""

	return (first + last) * n / 2

def main():
	"""
	This is the main() function.

	"""

	print("This is PEID %03d.\n" % (PEID))

	nDivisors   = 1
	firstNumber = 1
	lastNumber  = 1

	while nDivisors < MAX:
		s = sum_of_arithmetic_series(firstNumber, lastNumber, lastNumber - firstNumber + 1)
		d = prime_factorization(s)
		baseList, expList = transform_from_dict_to_lists(d)
		nDivisors = 1

		for e in expList:
			nDivisors *= e + 1

		print("lastNumber = %d, nDivisors = %d." % (lastNumber, nDivisors))

		lastNumber += 1

	print("The triangle number %d (lastNumber = %d) has %d divisors.\n" % (s, lastNumber - 1, nDivisors))

if __name__ == '__main__':
	main()
