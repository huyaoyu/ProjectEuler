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
# Created: 2017-09-23
#
# Description
# ===========
#
# The solution of Problem 19 in Project Euler.
#
# Python provides a package with the name of datetime. This package
# should do the trick. 
# 
# But I decided to do it by myself.
#
# And it turns out that 1200/7 is a fairly accurate approximation of
# this problem. Brilliant!
#
# 
#

PEID = 19 # Problem ID in Project Euler.

def is_leap_year(yyyy):
	"""
	Check if yyyy is a leap year.

	Return 1 if yyyy is a leap year.
	"""

	isLeapYear = 0

	if yyyy % 100 == 0:
		if yyyy % 400 == 0 and yyyy % 4 == 0:
			isLeapYear = 1
	else:
		if yyyy % 4 == 0:
			isLeapYear = 1

	return isLeapYear

class SingleYear(object):
	"""docstring for SingleYear"""
	def __init__(self, yyyy):
		super(SingleYear, self).__init__()
		self.yyyy = yyyy
		self.mIdx = 0
		self.wIdx = 1
		self.dIdx = 2
		
		self.daysList = []

		self.isLeapYear = is_leap_year(yyyy)

		self.daysInMonthList = []

	def make_days(self, start):
		"""
		Make description of every day in a year.

		start - The day index for the first day of a year. 1 for Sunday, 7 for Saturday.
		"""

		if 1 == self.isLeapYear:
			#                        1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12
			self.daysInMonthList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			#                        1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12
			self.daysInMonthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		monthName = 1
		weekday   = start

		for daysInMonth in self.daysInMonthList:
			for d in range(daysInMonth):
				self.daysList.append([monthName, weekday, d+1])

				weekday += 1

				if 8 <= weekday:
					weekday = 1

			monthName += 1

def main():
	"""The main() function."""

	print("This is PEID %03d.\n" % (PEID))

	y1900 = SingleYear(1900)

	y1900.make_days(2) # Monday is the second day of a week.

	syList = [y1900]

	for yyyy in range(1901, 2001, 1):
		y = SingleYear(yyyy)

		nextWeekday = syList[-1].daysList[-1][1] + 1

		if 8 == nextWeekday:
			nextWeekday = 1

		y.make_days(nextWeekday)

		syList.append(y)

	# Find the Sundays in January.
	syList2 = syList[1:]

	count = 0

	for y in syList2:
		for d in y.daysList:
			if d[y.dIdx] == 1 and d[y.wIdx] == 1:
				count += 1

	print("count = %d.\n" % (count))

	return syList

if __name__ == '__main__':
	syList = main()