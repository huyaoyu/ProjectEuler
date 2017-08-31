
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
# Created: 2017-08-31
#
# Description
# ===========
#
# The naive solution of Problem 2 in Project Euler.
# 

PEID = 2 # Problem ID in Project Euler.

MAX = 4000000 # Upper bound for the Fibonacci sequence.

BINARY_ONE = 1

def get_Fibonacci_seq(m):
	"""Return a list contains the Fibonacci sequence smaller than n."""

	fib = []

	# Check if n > 2

	if m == 1:
		fib.append(1)
	elif m == 2:
		fib.append(1)
		fib.append(2)
	elif m > 2:
		fib.append(1)
		fib.append(2)

		i = 2

		while True:
			currentFib = fib[i-1] + fib[i-2]

			if currentFib > m:
				break
			else:
				fib.append(currentFib)
				i = i + 1
	else:
		print("get_Fibonacci_seq: Wrong m. m = %f.\n" % (m))

	return fib

def is_even(n):
	"""
	Return 1 if n is an even number.

	Warning: The maximum of n is not thoroughly tested.
	"""

	if n & BINARY_ONE == 1:
		# This is not an even number.
		return 0
	else:
		return 1

if __name__ == "__main__":
	print("This is Project Euler, Problem %03d.\n" % (PEID))

	print("Get the Fibonacci sequence under %d.\n" % (MAX))

	fib = get_Fibonacci_seq(MAX)

	# Obtain the number of values inside fib.

	nFib = len(fib)

	print("There are %d values in fib, with the last one being %d.\n" % (nFib, fib[-1]))

	print(fib)

	# Count the number of even number in fib.

	evenCount = 0
	flags = []

	for val in fib:
		if is_even(val) == 1:
			evenCount = evenCount + 1
			flags.append(1)
		else:
			flags.append(0)

	print("There are %d even values in fig.\n" % (evenCount))

	# Calculate the sum of even numbers.

	sum = 0

	for val, f in zip(flags, fib):
		sum = sum + val * f

	print("The sum of the even values is %d.\n" % (sum))
