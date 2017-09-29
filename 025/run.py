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
# Created: 2017-09-29
#
# Description
# ===========
#
# The solution of Problem 25 in Project Euler.
#
# No brute force this time.
#
#

PEID = 25 # Problem ID in Project Euler.

MAX = 1000

def add(n0, n1):
	"""
	Return a indicator whether new digit is needed. 
	"""

	s = n0 + n1

	flagNewDigit = 0

	if s >= 10:
		flagNewDigit = 1

	return s, flagNewDigit

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	nDigits = 1

	n0 = 1
	n1 = 1

	count = 2

	while nDigits < MAX:
		s, flagNewDigit = add(n0, n1)

		if 1 == flagNewDigit:
			nDigits += 1
			n0 = n1 / 10
			n1 = s  / 10
		else:
			n0 = n1
			n1 = s

		count += 1

	print("count = %d.\n" % (count))
