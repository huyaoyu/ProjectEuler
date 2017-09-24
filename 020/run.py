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
# Created: 2017-09-24
#
# Description
# ===========
#
# The solution of Problem 20 in Project Euler.
#
# Everybody seems to rely on some sort of big-number library.
#

PEID = 20 # Problem ID in Project Euler.

MAX = 100

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	f = math.factorial(MAX)

	print(f)

	# Turns f into string.

	s = str(f)

	acc = 0

	for c in s:
		acc += int(c)

	print("acc = %d.\n" % (acc))

