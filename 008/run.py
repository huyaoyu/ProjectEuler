
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
# Created: 2017-09-06
#
# Description
# ===========
#
# The solution of Problem 8 in Project Euler.
#

PEID = 8  # Problem ID in Project Euler.

strNumber = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

LENGTH = 13

def pre_process(str, c, length):
	"""
	Delete characters that around character c in the range of length.

	"""

	# Deep copy.

	s = "%s" % (str)

	pos = 0

	while True:
		# Find the position of c.
		pos = s.find(c)

		if -1 == pos:
			break
		else:
			lenStr = len(s)

			if pos < length:
				head = ""
			else:
				head = s[0:(pos - (length - 1))]

			if pos + length >= lenStr:
				tail = ""
			else:
				tail = s[(pos+length):]

			s = "%s%s" % (head, tail)

	return s

def test_pre_process():
	rawStr = "012345"
	c      = "0"
	length = 4
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "012345"
	c      = "5"
	length = 4
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "012345"
	c      = "0"
	length = 6
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "012345"
	c      = "5"
	length = 6
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "012345"
	c      = "0"
	length = 7
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "012345"
	c      = "5"
	length = 7
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "0123456"
	c      = "3"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "0123456"
	c      = "2"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "0123456"
	c      = "1"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "0123456"
	c      = "4"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "0123456"
	c      = "5"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

	rawStr = "01234563217"
	c      = "3"
	length = 3
	ppStr  = pre_process(rawStr, c, length)
	print("%s, c = %s, length = %d, ppStr = %s\n" % (rawStr, c, length, ppStr))

def main():
	"""The main() function."""

	print("This is PEID %03d in Project Euler.\n" % (PEID))

	print("len(strNumber) = %d.\n" % (len(strNumber)))

	# Search and replace in strNumber.
	rawStrNumber = strNumber.replace("\n", "")

	print("len(rawStrNumber) = %d.\n" % (len(rawStrNumber)))

	maxProd = 1
	pos = LENGTH

	lenRSN = len(rawStrNumber)

	while pos < lenRSN:
		
		sstr = rawStrNumber[(pos-LENGTH):pos]

		tempProd = 1

		for c in sstr:
			tempProd *= int(c)

			if tempProd > maxProd:
				maxProd = tempProd

		pos += 1

	print("maxProd = %d.\n" % (maxProd))

if __name__ == '__main__':
	main()
