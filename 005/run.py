
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
# Created: 2017-09-03
#
# Description
# ===========
#
# The solution check for Problem 5 in Project Euler.
#
# This problem is relatively easier than the previous ones.
#
# Find the least common multiple among the numbers ranging from 1 to 20.
#
# In fact, this problem is equivalent to find the least common multiple
# among 11, 13, 14, 16, 17, 18, 19, 20. The solution could be obtained by
# hand.
#
# However, it is worth to be tried if I could come up with a program that 
# calculates the lest common multiple for any group of positive integers.
#

denominatorList = range(1, 21, 1)

if __name__ == '__main__':
	testNumber = 232792560

	for d in denominatorList:
		r = testNumber % d
		q = testNumber // d

		print("%d / %d = %d, %d." % (testNumber, d, q, r))

