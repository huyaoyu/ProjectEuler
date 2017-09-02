
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
# Created: 2017-09-02
#
# Description
# ===========
#
# The naive solution of Problem 4 in Project Euler using brute force.
#
# For this problem there exits several elegant solutions. Some of these
# solutions do not require a computer program at all!
#
# And there exits two magical programming languages, j and k.
#
# This problem tells me that I have to learn to model things. Before you
# starting coding, a rational description is always needed. You have to
# try to model the problem, find out its characteristics, narrow down
# the possible solutions, think of alternative ways of representations,
# try reverse thinking. Then let the computer do the rest.
#
# For this particular problem, palindromic number can be tested by using its
# string representative. You don't have to check two 'half' portions, you just
# check if the entire string equals the its reverse. And for brute searching, 
# people tend to find a palindromic number from all possible products of 
# two 3-digits numbers, but not the reverse. Since it is relatively easy to
# test a palindromic number than to compose one.
# 

PEID = 4 # Problem ID in Project Euler.

BASE = 10

def make_base_list(n):
	"""
	Make a list contains all the bases.
	"""

	b = []

	for i in range(n, 0, -1):
		b.append(BASE**(i-1))

	return b

def bidirection_positions(n):
	"""
	Return two list contains the positions from two directions.
	"""

	# Check if n is an even number.
	if n & 1 == 0:
		# Even number.
		span = int(n / 2)
	else:
		span = int(int(n / 2) + 1)

	p0 = range(n, n - span, -1)
	p1 = range(span, 0, -1)

	return p0, p1

def split_number(n):
	"""
	split a number into digits.
	"""

	# Get the digits index.

	di = int(math.log10(n))

	currentNumber = n

	dList = []

	for i in range(di, -1, -1):
		base = BASE**i

		d = currentNumber // base
		r = currentNumber % base

		dList.append(d)

		currentNumber = r

	return dList

def compose_number(p0, p1, baseList, dList):
	"""
	Compose the number using bidirectional position lists.
	"""

	n = 0

	nBases = len(baseList)

	digits = [0] * nBases

	for i, j, k, m in zip(p0, p1, dList, reversed(dList)):
		digits[ i-1 ] = k
		digits[ j-1 ] = m

	for d, b in zip(digits, baseList):
		n = n + d * b

	return n

def get_palindromic_number(nDigits, maxNumber, minNumber):
	"""
	Return the palindromic number with maximum number of digits equals nDigits.
	"""

	for i in range(nDigits, 1, -1):
		# Make the base list.
		if 2 == i:
			i = i

		baseList = make_base_list(i)

		# Get the position lists.
		(p0, p1) = bidirection_positions(i)

		halfWidth = len(p0)

		for j in range(BASE**halfWidth - 1, BASE**(halfWidth-1) - 1, -1):
			# Split the number into digits.
			dList = split_number(j)

			pn = compose_number(p0, p1, baseList, dList)

			if pn <= maxNumber and pn >= minNumber:
				yield pn

def can_divided_by_3_digits_numbers(num):
	"""
	Return 1 if num could be divided by two 3-digits number.
	"""

	for i in range(100, 1000, 1):
		if num % i == 0:
			j = num // i
			if j > 99 and j < 1000:
				return 1, i, j

	return 0, 0, 0

def main():
	"""Main function."""

	print("This is Problem %03d in Project Euler.\n" % (PEID))

	baseList = make_base_list(6)
	(p0, p1) = bidirection_positions(6)
	dList = split_number(120)
	n = compose_number(p0, p1, baseList, dList)

	print("n = %d.\n" % (n))

	baseList = make_base_list(5)
	(p0, p1) = bidirection_positions(5)
	dList = split_number(120)
	n = compose_number(p0, p1, baseList, dList)

	print("n = %d.\n" % (n))

	print("Test sequence of palindromic numbers.\n")

	for n in get_palindromic_number(6, 999*999, 100*100):
		print("n = %d" % n)

		flag, factor0, factor1 = can_divided_by_3_digits_numbers(n)

		if 1 == flag:
			print("%d = %d * %d.\n" % (n, factor0, factor1))
			break

	print("Done.\n")
	
if __name__ == '__main__':
	main()
