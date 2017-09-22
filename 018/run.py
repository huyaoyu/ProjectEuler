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
# The solution of Problem 18 in Project Euler.
# 
# The code also works for PEID 067.
#
# The key is to search from the bottom to the top.
#
# I build a binary tree to do the recursive search. A flag should be 
# set to indicate whether the current node has found a maximum sum.
#

PEID = 18 # Problem ID in Project Euler.

class BiNode(object):
	"""docstring for BiNode"""
	def __init__(self, v, ln, rn):
		super(BiNode, self).__init__()
		self.v  = v   # value
		self.ln = ln # left node
		self.rn = rn # right node
		self.maxSum     = 0
		self.flagMaxSum = 0
	

def load_triangle(fn):
	"""
	Load the triangle from raw input file.

	"""

	# Open the file.
	fp = open(fn, "r")

	m = []
	n = []

	for line in fp:
		rowM = [int(x) for x in line.split()]
		m.append(rowM)

		rowN = [BiNode(x, None, None) for x in rowM]
		n.append(rowN)

	fp.close()

	# Build the tree.

	height = len(n)

	for i in range(height-2, -1, -1):
		numNodes = len(n[i])

		for j in range(numNodes):
			n[i][j].ln = n[i+1][j]
			n[i][j].rn = n[i+1][j+1]

	return n, m

def find_max_sum(bn):
	"""Find the maximum sum."""

	if 1 == bn.flagMaxSum:
		return bn.maxSum

	if not None == bn.ln:
		maxSumLn = find_max_sum(bn.ln)
	else:
		maxSumLn = 0

	if not None == bn.rn:
		maxSumRn = find_max_sum(bn.rn)
	else:
		maxSumRn = 0

	if maxSumLn >= maxSumRn:
		maxSum = maxSumLn
	else:
		maxSum = maxSumRn

	bn.maxSum = bn.v + maxSum
	bn.flagMaxSum = 1

	return bn.maxSum

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	n, m = load_triangle("raw-input-67.dat")
	# n, m = load_triangle("raw-input.dat")

	maxSum = find_max_sum(n[0][0])

	print("maxSum = %d.\n" % (maxSum))

	return n, m

if __name__ == '__main__':
	n, m = main()
