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
# Created: 2017-09-20
#
# Description
# ===========
#
# The solution of Problem 14 in Project Euler.
#
# The method use Hash table is much faster that the naive implementation.
#
# The strategy is starting from smaller number. And store the length of its
# Collatz sequence in to a python dictionary. When calculating the length
# of Collatz sequence of a new starting number, this dictionary is constantly 
# inquired to see if the current intermediate value is registered in the dictionary.
# If the current value is in the dictionary, then the corresponding length
# is added to the current length. After calculating the length of the current
# starting number, both the staring number and its length of Collatz sequence
# are registered in the dictionary for later use.
#

PEID = 14 # Problem ID in Project Euler.

MAX = 1000000

def Collatz_sequence(n):
	"""
	Return the Collatz sequence starting from n.
	"""

	temp = int(n)

	CS = [n]

	while temp > 1:
		if 1 == temp & 1:
			# Odd number.
			temp = int(3 * temp + 1)
		else:
			# Even number.
			temp = int(temp / 2)

		CS.append(temp)

	return CS

def length_of_Collatz_sequence_naive(n):
	"""
	Return the Collatz sequence starting from n.
	"""

	temp = int(n)

	count = 0

	while temp > 1:
		if 1 == temp & 1:
			# Odd number.
			temp = int(3 * temp + 1)
		else:
			# Even number.
			temp = int(temp / 2)

		count += 1

	return count + 1

gDictLengthsCollatzSeq = {2:2}

def length_of_Collatz_sequence(n):
	"""
	This function uses the global dictionary gDictLengthsCollatzSeq to store the lengths
	of different numbers.

	"""

	global gDictLengthsCollatzSeq

	count = 0

	temp = int(n)

	while temp > 1:
		if temp in gDictLengthsCollatzSeq:
			count += gDictLengthsCollatzSeq[temp]
			break

		if 1 == temp & 1:
			# Odd number.
			temp = int(3 * temp + 1)
		else:
			# Even number.
			temp = int(temp / 2)

		count += 1

	gDictLengthsCollatzSeq[n] = count

	return count

gCurrentPercentage = 0

def show_progress(current, total, intervalPercentage):
	"""
	This is borrowed from PEID 007.

	Show progress.
	"""

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
	"""This is the main() function."""

	print("This is PEID %03d.\n" % (PEID))

	maxLength = 0
	numMaxLen = 0
	csMaxLen  = []
	count     = 0

	for n in range(2, MAX + 1):
		tempLength = length_of_Collatz_sequence(n) # This is faster.
		# tempLength = length_of_Collatz_sequence_naive(n)

		if tempLength > maxLength:
			maxLength = tempLength
			numMaxLen = n

		count += 1

		show_progress(count, MAX - 3, 0.05)

	csMaxLen = Collatz_sequence(numMaxLen)

	print("maxLength = %d, numMaxLen = %d.\n" % (maxLength, numMaxLen))
	print(csMaxLen)
	print("The size of gDictLengthsCollatzSeq is %d.\n" % (len(gDictLengthsCollatzSeq)))

if __name__ == '__main__':
	main()
