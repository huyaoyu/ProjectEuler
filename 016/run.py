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
# Created: 2017-09-22
#
# Description
# ===========
#
# The solution of Problem 16 in Project Euler.
# 
# Today's dynamic or scripting programming language is so powerful that
# there is virtually no upper limit for integer.
#

PEID = 16 # Problem ID in Project Euler.

MAX = 1000

if __name__ == '__main__':
	s = str(2**MAX)

	acc = 0

	for c in s:
		v = int(c)

		acc += v

	print("acc = %d.\n" % (acc))
