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
# Created: 2017-09-28
#
# Description
# ===========
#
# The solution of Problem 24 in Project Euler.
#
# You can rely on the powerful itertools package provided by python.
# However, I choose another way out.
#

PEID = 24 # Problem ID in Project Euler.

def find_digit_in_list(p, rn, rev):
	"""
	p - The list contains the sorted digits.
	rn - The required number.
	rev - The list in the reverse order.

	"""

	# Get the length of p.
	nP = len(p)

	if nP == 0:
		return

	if rn == 0:
		for d in p:
			rev.append(d)

		return

	# Calculate the step.
	step = math.factorial(nP - 1)

	# Get the index.
	idx = rn // step
	rem = rn %  step

	if rem == 0:
		idx -= 1

	d = p[idx]

	# Create a new list.
	newP = p[0:0+idx] + p[idx+1:]

	# Recursive execution.

	find_digit_in_list(newP, rem, rev)

	# Append to the reverse ordered list.
	rev.append(d)

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	# p   = [0, 1, 2, 3, 4]
	# rev = []
	# rn  = 100

	p   = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	rev = []
	rn  = 1000000

	find_digit_in_list(p, rn, rev)

	print(rev[::-1])

	for x in rev[::-1]: print("%d" % (x), end="")


