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
# Created: 2017-09-04
#
# Description
# ===========
#
# The solution of Problem 6 in Project Euler.
#
# There are some interesting facts about the sum of the sequence of n^2.
#
# And it turns out that (1 + 2 + ... + n)^2 = 1^3 + 2^3 + ... + n^3.
# Amazing!
# 

PEID = 6 # Problem ID in Project Euler.

MAX = 100

def main():
	"""The main() function."""

	print("This is Problem 6 in Project Euler.\n")

	res = 0

	# Loop.
	for i in range(1, MAX, 1):
		for j in range(i+1, MAX+1, 1):
			res += i*j

	res *= 2

	print("res = %d.\n" % (res))


if __name__ == '__main__':
	main()