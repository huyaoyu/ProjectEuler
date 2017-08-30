
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
# Created: 2017-08-30
#
# Description
# ===========
#
# This is the solution of Problem 001 of Project Euler.
#
# There is a much more elegant way to solve this problem, that is to
# sum up all the multiples of 3 and 5 using arithmetic progression, then
# subtract the sum of multiples of 15 (the least common multiple), again,
# utilizing arithmetic progression.
#
# This program solves the problem in the most naive way.
# 

PEID = 1 # Problem ID in Project Euler.

MAX = 1000 # Maximum integer. The integers below MAX (not containing) are considered.

if __name__ == "__main__":
	print("This is Problem %03d from Project Euler." % (PEID))

	print("I'm going to solve it in the most naive way.\n")

	# Empty list.
	m = []

	for i in range(MAX):

		if i%3 == 0:
			# Check if i is the multiples of 3.
			m.append(i)
		elif i%5 == 0:
			# Check if i is the multiples of 5.
			m.append(i)
		else:
			# Do nothing.
			pass

	print("The valid integers are: \n")
	print(m)

	# Calculate the sum.
	s = sum(m)

	print("\nThe sum is %d." % (s))
