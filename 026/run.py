import os
import sys
import math

# This is PEID 026.

PEID = 26

MAX = 1000

def find_length_of_recurring_cycle(n):
	"""Return the length of a recurring cycle of 1/n."""

	lrc = 0

	# Find out the digits of n.
	nd = n / 10

	numerator = int(10**(nd+1))

	r = {}
	idx = 0

	while True:
		# Get the remainder.
		rmd = numerator % n

		if rmd in r:
			lrc = idx - r[rmd]
			break

		r[rmd] = idx

		idx += 1

		numerator = rmd * 10

	return lrc

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	# Prepare the input list.
	numberList = []

	for i in range(3, MAX):
		if 0 == i % 2 or 0 == i % 5:
			continue
		else:
			numberList.append(i)

	# Find the denominator with the longest recurring cycle.

	maxLRC = 0
	maxN   = 0

	for n in numberList:
		lrc = find_length_of_recurring_cycle(n)

		if lrc > maxLRC:
			maxLRC = lrc
			maxN   = n

	print("maxN = %d, maxLRC = %d.\n" % (maxN, maxLRC))
