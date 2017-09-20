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
# Created: 2017-09-20
#
# Description
# ===========
#
# The solution of Problem 13 in Project Euler.
#
# In fact, only the first 11 or 12 digits of each number are needed if only the
# first 10 digits of the final answer are required.
#
# Some people say that, in LISP, amazing things happens with only one "+" operator.
#

PEID = 13 # Problem ID in Project Euler.

INPUT_FILE = "raw-string.dat"
ROW = 100
COL = 50

class long_integer(object):
	"""docstring for long_integer"""
	def __init__(self):
		super(long_integer, self).__init__()
		
		self.digitHolder = np.array([0], dtype=np.int)

	def get_size(self):
		"""Return the size of the integer."""

		return self.digitHolder.shape[0]

	def resize(self, rs, d = 0):
		"""Resize the length of the integer."""

		# Make a copy of the original digitHolder.

		oriDH = self.digitHolder

		self.digitHolder = np.zeros([rs], dtype=np.int)

		for i in range(rs):
			if i < oriDH.shape[0]:
				self.digitHolder[i] = oriDH[i]
			else:
				self.digitHolder[i] = d

	def make(self, dh):
		"""
		Make a new integer by copying the values in dh.

		The values are copied in the reverse order.

		"""

		lenDH = dh.shape[0]

		self.digitHolder = np.zeros([lenDH], dtype=np.int)

		for i in range(lenDH):
			self.digitHolder[i] = int(dh[-1-i])

	def show(self, rightAlign = False, rightAlignPreFix = " ", rightAlignWidth = 80):
		"""
		Print the integer.

		The values should be printed in the reverse order.
		"""

		if True == rightAlign and rightAlignWidth > self.digitHolder.shape[0]:
			for i in range(rightAlignWidth - self.digitHolder.shape[0]):
				print("%s" % (rightAlignPreFix), end="")

		for i in range(self.digitHolder.shape[0]):
			print("%d" % (self.digitHolder[-1-i]), end="")

		print("")

	def get_digit(self, idx):
		"""
		Get the digit with the index idx.
		
		idx is zero based.
		"""

		if idx >= self.digitHolder.shape[0]:
			return 0
		elif idx >= 0:
			return self.digitHolder[idx]
		else:
			# Error.
			print("get_digit: Wrong idx. idx = %d.\n" % (idx))
			return -1

	def add(self, li):
		"""
		Add two long integer objects.
		"""

		# Get the sizes of the two integers.

		s0 = self.get_size()
		s1 = li.get_size()

		if s0 >= s1:
			s = s0
		else:
			s = s1
			self.resize(s)

		flag = 0

		for i in range(s):
			d0 = self.get_digit(i)
			d1 = li.get_digit(i)

			tempSum = d0 + d1 + flag

			if tempSum > 9:
				tempSum = tempSum % 10
				flag = 1
			else:
				flag = 0

			self.digitHolder[i] = tempSum

		if 1 == flag:
			self.resize(s+1, d=1)

def parse_raw_string_file(fn, row, col):
	"""
	This function parse the raw string stored in the file fn.

	The result will be stored in a numpy ndarray object.

	Each element of the ndarray object is a single number.

	fn - The file name.
	row - The number of rows.
	col - The number of columns.

	"""

	# Allocated memory.
	numMatrix = np.zeros([row, col], dtype=np.int)

	with open(fn, 'r') as fin:
		i = 0
		for line in fin:

			if not line:
				break

			j = 0
			for c in line:
				if "\n" == c:
					break

				numMatrix[i][j] = int(c)
				j += 1

			i += 1

	return numMatrix

def main():
	"""The main() function."""

	print("This is PEID %03d in Project Euler.\n" % (PEID))

	nm = parse_raw_string_file(INPUT_FILE, ROW, COL)

	print(nm)

	li  = long_integer()
	lit = long_integer()

	for i in range(ROW):
		lit.make( nm[i, :] )

		print("i = %d." % (i))

		li.show(rightAlign = True, rightAlignPreFix = " ", rightAlignWidth = 52)
		lit.show(rightAlign = True, rightAlignPreFix = " ", rightAlignWidth = 52)

		li.add(lit)
		li.show(rightAlign = True, rightAlignPreFix = " ", rightAlignWidth = 52)

		print("")

	return nm

if __name__ == '__main__':
	nm = main()

	# li = long_integer()

	# li.make(nm[0,:])

	# li1 = long_integer()
	# li2 = long_integer()
	# li1.make(np.array([2, 5, 0], dtype=np.int))
	# li2.make(np.array([9, 9, 9, 9], dtype=np.int))
