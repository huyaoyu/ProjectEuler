
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
# Created: 2017-09-07
#
# Description
# ===========
#
# The solution of Problem 9 in Project Euler.
#
# There is a genius solution provided by the discussion thread in Project Euler.
#

PEID = 9  # Problem ID in Project Euler.

SUM = 1000

def main():
	"""The main() function."""

	print("This is PEID %03d in Project Euler.\n" % (PEID))

	for c in range(998, 4, -1):
		for b in range(SUM - c - 1, 3, -1):
			a = SUM - c - b

			if a > b:
				break

			if c**2 == a**2 + b**2:
				print("a = %d, b = %d, c = %d.\n" % (a, b, c))
				print("abc = %d.\n" % (a * b * c))

if __name__ == '__main__':
	main()

