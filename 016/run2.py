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
# This code deliberately does not use the big integer functionality
# of Python. The long_integer class created in PEID 013 is borrowed.
# Since PEID 016 only require multiplication by 2, only the addition
# operation is needed.
#

PEID = 16 # Problem ID in Project Euler.

MAX = 1000

class long_integer(object):
	"""
	docstring for long_integer.

	This class is borrowed from PEID 013.
	"""
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

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	# Create a long_integer object.
	d = np.array([2])

	li = long_integer()
	li.make(d)

	for i in range(MAX-1):
		li.add(li)

	li.show()

	print("The sum of all the digits is %d.\n" % (sum(li.digitHolder)))
