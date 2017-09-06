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
# Created: 2017-09-06
#
# Description
# ===========
#
# The solution of Problem 7 in Project Euler.
#
# You can leverage the prime numbers already found in the program
# to test if the current number is a prime number. But based on my
# experience with the list functionality provided by Python, the
# overall efficiency is not promoted but decreased. At least on my
# current computer it is the case.
#

PEID = 7 # Problem ID in Project Euler.

targetCount = 10001

gCurrentPercentage = 0

def is_prime(n):
	"""
	This function is borrowed from PEID 003.

	Return 1 if n is a prime number.

	NOTE: 
	The maximum allowable n is not thoroughly tested.
	"""

	# Find the square root of n.

	p = int(math.sqrt(n))

	while p > 1:
		if n % p == 0:
			return 0

		p = p - 1

	return 1

def is_prime_ref(n, refList):
	"""
	Return 1 if n is a prime number.

	The test is based on the prime numbers already found and stored in refList.
	"""

	for p in refList:
		if n % p == 0:
			return 0

	return 1

def show_progress(current, total, intervalPercentage):
	"""Show progress."""

	global gCurrentPercentage

	# Check if current == 0.
	if 0 == current:
		gCurrentPercentage = 0

	p = current / total

	if p >= gCurrentPercentage + intervalPercentage:
		print("%2.1f%%" % (p*100))
		gCurrentPercentage += intervalPercentage
	elif current == total:
		print("100%")
		gCurrentPercentage = 1

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	primeList = [2]

	count = 1
	currentNumber = 3

	while count < targetCount:
		# Check if currentNumber is a prime number.
		# if 1 == is_prime_ref(currentNumber, primeList):
		if 1 == is_prime(currentNumber):
			primeList.append(currentNumber)
			count += 1
			show_progress(count, targetCount, 0.05)

		currentNumber += 2

	print("The %dth prime number is %d.\n" % (targetCount, primeList[-1]))

	return primeList

if __name__ == '__main__':
	pl = main()
