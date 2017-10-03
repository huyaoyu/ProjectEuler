import os
import sys
import math

# This is PEID 027.

PEID = 27

LIMIT_A = 1000
LIMIT_B = 1000

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

def max_consecutive_primes(a, b):
	"""
	Return the maximum number of consecutive primes calculated
	by n^2 + a*n + b, starting from n = 0
	"""

	n = 0

	while True:
		q = n**2 + a * n + b

		if q <= 0:
			break

		if 0 == is_prime(q):
			break

		n += 1

	return n

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	n40 = max_consecutive_primes(1, 41)

	print("n40 -> %d.\n" % (n40))

	n80 = max_consecutive_primes(-79, 1601)

	print("n80 -> %d.\n" % (n80))

	maxN = 0
	maxA = 0
	maxB = 0

	flagStop = 0

	for b in range(LIMIT_B, 0, -1):
		if 1 == flagStop:
			break

		for a in range(-b-1, LIMIT_A+1, 1):
			if b < maxN:
				# No further effort is needed.
				flagStop = 1
				break

			# Find the number of primves from consecutive n values.
			np = max_consecutive_primes(a, b)

			if np > maxN:
				maxN = np
				maxA = a
				maxB = b

	print("maxA = %d, maxB = %d, maxN = %d.\n" % (maxA, maxB, maxN))
	