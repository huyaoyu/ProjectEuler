
import os
import sys
import math

# Author
# ======
#
# Yaoyu Hu <huyaoyu@sjtu.edu.cn>
#
# Date
# ====
#
# Created: 2017-09-03
#
# Description
# ===========
#
# Calculates the lest common multiple for any group of positive integers.
#

def get_max_exponent(n, p):
	"""
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

def least_common_multiple(pfDictList):
	"""
	pfDictList contains the dictionaries of prime factorization.
	"""

	assembleDict = {}

	for d in pfDictList:
		# Get the list of keys of d.
		keys = list(d.keys())

		for k in keys:
			# Check if k is in assembleDict.
			if k in assembleDict:
				# k is one of the keys of assembleDict.
				exponentA = assembleDict[k]
				exponentK = d[k]

				if exponentK > exponentA:
					assembleDict[k] = exponentK
			else:
				# k is not one of the keys of assembleDict.
				assembleDict[k] = d[k]

	LCM = 1

	# Compose the least common multiple.
	for k, p in assembleDict.items():
		LCM = LCM * k**p

	return LCM

def show_pfd_info(numList, pfdList):
	"""
	numList: A list of input numbers.
	pfdList: A list of prime factorizations of each number in numList.
	"""

	for i in range(len(numList)):
		print("%d = " % (numList[i]), end = "")

		count = 0
		for k, p in pfdList[i].items():
			if 0 == count:
				print("%d^%d" % (k, p), end = "")
				count = 1
			else:
				print(" * %d^%d" % (k, p), end = "")

		print("")

if __name__ == '__main__':
	numberGroup = list(range(1, 21, 1))

	pfDictList = []

	for n in numberGroup:
		pfd = prime_factorization(n)

		pfDictList.append(pfd)

	# Show info.
	show_pfd_info(numberGroup, pfDictList)

	LCM = least_common_multiple(pfDictList)

	print("LCM = %d.\n" % (LCM))
