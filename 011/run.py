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
# Created: 2017-09-17
#
# Description
# ===========
#
# The solution of Problem 11 in Project Euler.
#
# This code utilized the diagonal() function provided by numpy.
# 
# Remember that the opposite diagonals should be also tested.
#
#

PEID = 11 # Problem ID in Project Euler.

INPUT_MATRIX_FILE = "input-matrix.dat"

NUM_CONSECUTIVE   = 4

def find_max_multiple_product(numList, n):
	"""
	Find the maximum multiple product in numList with n consecutive numbers.

	"""

	lenNumList = len(numList)

	if n > lenNumList:
		# This is an error.
		print("find_max_multiple_product: The length of numList is less than n.\nlenNumList = %d, n = %d.\n" % (lenNumList, n))
		return -1

	maxProduct = 1

	lastIndex = lenNumList - n

	maxI = 0

	for i in range(0, lastIndex+1, 1):
		tempProduct = 1
		for j in range(0, n):
			tempProduct *= numList[i+j]

		if tempProduct > maxProduct:
			maxProduct = tempProduct
			maxI = i

	return maxProduct, maxI

def main():
	"""This is the main() function."""

	print("This is PEID %03d in Project Euler.\n" % (PEID))

	# Load the matrix from the input file.

	im = np.loadtxt(INPUT_MATRIX_FILE, dtype=int, delimiter=" ")

	print("The dimension of input matrix is (%d, %d).\n" % (im.shape[0], im.shape[1]))

	maxProduct     = 1
	maxI, tempMaxI = 0, 0
	maxJ, tempMaxJ = 0, 0
	maxType        = "Row"

	# Test all the diagonals (/).
	imlr = np.fliplr(im)
	for i in range(-1*(im.shape[0] - NUM_CONSECUTIVE), im.shape[1] - NUM_CONSECUTIVE + 1):
		tempMaxProduct, tempMaxJ = find_max_multiple_product(np.diagonal(imlr, offset = i), NUM_CONSECUTIVE)

		if tempMaxProduct > maxProduct:
			maxProduct = tempMaxProduct
			maxI = i
			maxJ = tempMaxJ
			maxType = "Diag/"
			print("maxI = %d, maxJ = %d, maxType = %s, maxProduct = %d.\n" % (maxI, maxJ, maxType, maxProduct))

	# Test all the diagonals (\).
	for i in range(-1*(im.shape[0] - NUM_CONSECUTIVE), im.shape[1] - NUM_CONSECUTIVE + 1):
		tempMaxProduct, tempMaxJ = find_max_multiple_product(np.diagonal(im, offset = i), NUM_CONSECUTIVE)

		if tempMaxProduct > maxProduct:
			maxProduct = tempMaxProduct
			maxI = i
			maxJ = tempMaxJ
			maxType = "Diag\\"
			print("maxI = %d, maxJ = %d, maxType = %s, maxProduct = %d.\n" % (maxI, maxJ, maxType, maxProduct))

	# Test all the rows.
	for i in range(0, im.shape[0]):
		tempMaxProduct, tempMaxJ = find_max_multiple_product(im[i, :], NUM_CONSECUTIVE)

		if tempMaxProduct > maxProduct:
			maxProduct = tempMaxProduct
			maxI = i
			maxJ = tempMaxJ
			maxType = "Row"
			print("maxI = %d, maxJ = %d, maxType = %s, maxProduct = %d.\n" % (maxI, maxJ, maxType, maxProduct))

	# Test all the columns.
	for i in range(0, im.shape[1]):
		tempMaxProduct, tempMaxI = find_max_multiple_product(im[:, i], NUM_CONSECUTIVE)

		if tempMaxProduct > maxProduct:
			maxProduct = tempMaxProduct
			maxI = tempMaxI
			maxJ = i
			maxType = "Col"
			print("maxI = %d, maxJ = %d, maxType = %s, maxProduct = %d.\n" % (maxI, maxJ, maxType, maxProduct))

	print("maxI = %d, maxJ = %d, maxType = %s, maxProduct = %d.\n" % (maxI, maxJ, maxType, maxProduct))

	return im

if __name__ == '__main__':
	im = main()

	# a = np.diagonal(im, offset = 0)

	# b = find_max_multiple_product([0, 1, 2, 3, 4, 5, 6, 0, 7], NUM_CONSECUTIVE)
