
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
# Created: 2017-09-01
#
# Description
# ===========
#
# The naive solution of Problem 3 in Project Euler using brute force.
# 

PEID = 3 # Problem ID in Project Euler.

MAX = 600851475143 # The target integer.

def is_prime(n):
	"""
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

if __name__ == "__main__":
	print("This is Problem %03d in Project Euler.\n" % (PEID))

	# Test is_prime()
	if 1 == is_prime(2):
		print("2 is a prime number.\n")

	if 1 == is_prime(3):
		print("3 is a prime number.\n")

	if 0 == is_prime(4):
		print("4 is not a prime number.\n")

	# Calculate the square root of MAX.
	s = int(math.sqrt(MAX))

	# check whether s is an even number.
	if 0 == s & 1:
		# Even number.
		s = s + 1 # Let's start from an odd number.

	while s > 1:
		if 1 == is_prime(s):
			if 0 == MAX % s:
				print("s = %d.\n" % (s))
				break

		s = s - 2 # Odd numbers only.

