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
# Created: 2017-09-21
#
# Description
# ===========
#
# The solution of Problem 15 in Project Euler.
#
# The theoretical solution is based on the knowledge of the Pascal's triangle and
# the combination theory.
#
# I use this problem to do a practice of recursive function. Additionally, if the
# map is not a 2D grid, this method is also valid provided with the corrected
# topology information.
#
#

PEID = 15 # Problem ID in Project Euler.
ROW  = 21
COL  = 21

class MapNode(object):
	"""docstring for MapNode"""
	def __init__(self, idx, n2, n3):
		super(MapNode, self).__init__()
		self.n2 = n2
		self.n3 = n3

		self.idxStr = idx # String.

		self.sum = 0
		
def get_sum(mn):
	"""Get the sum of a MapNode object recursively."""

	if not mn.sum == 0:
		return mn.sum

	if not mn.n3 == None:
		s3 = get_sum(mn.n3)
	else:
		s3 = 0

	if not mn.n2 == None:
		s2 = get_sum(mn.n2)
	else:
		s2 = 0

	mn.sum = s3 + s2

	if mn.sum == 0:
		mn.sum = 1

	return mn.sum

def make_map(row, col):
	"""Make a map with row and col."""

	# Make the dictionary.

	idxStr = "%02d%02d" % (int(row), int(col))

	dictMap = {}

	for i in range(row):
		for j in range(col):
			idxStr = "%02d%02d" % (int(i), int(j))
			mn = MapNode(idxStr, None, None)

			dictMap[idxStr] = mn

	# Build topology.
	for i in range(row):
		for j in range(col):
			idxStr = "%02d%02d" % (int(i), int(j))

			mn = dictMap[idxStr]

			if 0 == i:
				n3 = None
			else:
				idxStrN3 = "%02d%02d" % (int(i-1), int(j))
				n3 = dictMap[idxStrN3]

			if 0 == j:
				n2 = None
			else:
				idxStrN2 = "%02d%02d" % (int(i), int(j-1))
				n2 = dictMap[idxStrN2]

			mn.n3 = n3
			mn.n2 = n2

	return dictMap

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	# Build the map.
	dictMap = make_map(ROW, COL)

	# Get the last node.
	idxStr = "%02d%02d" % (int(ROW-1), int(COL-1))

	# Calculate the summation.
	s = get_sum(dictMap[idxStr])

	print("s = %d.\n" % (s))

	return dictMap

if __name__ == '__main__':
	dictMap = main()
