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
# Created: 2017-09-26
#
# Description
# ===========
#
# The solution of Problem 22 in Project Euler.
#
# First of all, the knowledge of ASCII codes is a plus. (ord() and chr() functions)
#
# Benefit from list.sort() function of Python.
#
# Then no magical things happened.
#

PEID = 22 # Problem ID in Project Euler.

INPUT_FILE = "p022_names.txt"

CHAR_A_CODE = 65

def calculate_score(name, charACode):
	"""Calculate the score of name."""

	score = 0

	for c in name:
		score += (ord(c) - charACode + 1)

	return score

def main():
	"""This is the main() function."""

	print("This is PEID %03d.\n" % (PEID))

	# Test calculate_score() function.
	scoreCOLIN = calculate_score("COLIN", CHAR_A_CODE)

	print("The score of COLIN is %d.\n" % (scoreCOLIN))

	# Open and read the file.
	fn = open(INPUT_FILE, "r")
	rawStrList = fn.read().split(",")

	for i in range(len(rawStrList)):
		oriStr = rawStrList[i]
		rawStrList[i] = oriStr.replace('"', '')

	print("rawStrList obtained.\n")

	rawStrList.sort()

	accScore = 0

	for i in range(len(rawStrList)):
		score = calculate_score(rawStrList[i], CHAR_A_CODE) * (i+1)
		accScore += score

	print("accScore = %d.\n" % (accScore))

	return rawStrList

if __name__ == '__main__':
	rawStrList = main()
