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
# The solution of Problem 17 in Project Euler.
#
# I have to admit that this problem is not about mathematics and programming.
# It is all about the different usages of the word "and" between British English  
# and American English. Furthermore, make sure to spell-check your words, like 
# "forty".
#

PEID = 17 # Problem ID in Project Euler.

LIMIT = 9999

MAX = 1000

# Prepared information.

wordDict =\
{\
 1:["one",       len("one")],\
 2:["two",       len("two")],\
 3:["three",     len("three")],\
 4:["four",      len("four")],\
 5:["five",      len("five")],\
 6:["six",       len("six")],\
 7:["seven",     len("seven")],\
 8:["eight",     len("eight")],\
 9:["nine",      len("nine")],\
10:["ten",       len("ten")],\
11:["eleven",    len("eleven")],\
12:["twelve",    len("twelve")],\
13:["thirteen",  len("thirteen")],\
14:["fourteen",  len("fourteen")],\
15:["fifteen",   len("fifteen")],\
16:["sixteen",   len("sixteen")],\
17:["seventeen", len("seventeen")],\
18:["eighteen",  len("eighteen")],\
19:["nineteen",  len("nineteen")],\
20:["twenty",    len("twenty")],\
30:["thirty",    len("thirty")],\
40:["forty",     len("forty")],\
50:["fifty",     len("fifty")],\
60:["sixty",     len("sixty")],\
70:["seventy",   len("seventy")],\
80:["eighty",    len("eighty")],\
90:["ninety",    len("ninety")]\
}

nameDict = \
{\
100: ["hundred",  len("hundred")],\
1000:["thousand", len("thousand")],\
0:   ["and",      len("end")]\
}

def translate(n, wd, nd):
	"""
	Translate a number.

	n - the integer number.
	wd - the word dictionary.
	nd - the name dictionary.
	"""

	global LIMIT

	if n > LIMIT:
		print("translate: Error. This function only accepts number below %d.\n" % (LIMIT))
		return "", 0

	s = ""
	count = 0
	flagThousand = 0
	flagHundred  = 0
	flagOver20   = 0

	r = n

	if r > 999:
		d = r // 1000
		r = r %  1000

		s += wd[d][0] + " " + nd[1000][0]
		count += wd[d][1] + nd[1000][1]

		flagThousand = 1

	if r > 99:
		d = r // 100
		r = r %  100

		if 1 == flagThousand:
			s += " "

		s += wd[d][0] + " " + nd[100][0]
		count += wd[d][1] + nd[100][1]

		flagHundred = 1

	if r > 19:
		if 1 == flagThousand or 1 == flagHundred:
			s += " " + nd[0][0] + " "
			count += nd[0][1]

		d = int(r // 10 * 10)
		r = r %  10

		s += wd[d][0]
		count += wd[d][1]

		flagOver20 = 1
	elif r > 0:
		if 1 == flagThousand or 1 == flagHundred:
			s += " " + nd[0][0] + " "
			count += nd[0][1]

		s += wd[r][0]
		count += wd[r][1]

	if 1 == flagOver20 and not 0 == r:
		s += "-"

		s += wd[r][0]
		count += wd[r][1]

	return s, count

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	testList = [\
	9999, 999, 99, 9,\
	8088, 8008,\
	7000, 7019,\
	606, 600,\
	55, 50,\
	4
	]

	for n in testList:
		s, count = translate(n, wordDict, nameDict)
		print("%4d, %s, count = %d.\n" % (n, s, count))

	accCount = 0

	for i in range(MAX+1):
		s, count = translate(i, wordDict, nameDict)

		accCount += count

	print("accCount = %d.\n" % (accCount))

if __name__ == '__main__':
	main()