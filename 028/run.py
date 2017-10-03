import os
import sys
import math

# This is PEID 028.

PEID = 28

MAX = 1001

def an(n):
	return (2 * n - 1)**2

def bn(n):
	return (2 * n - 2)**2 + 1

def cn(n):
	return n**2 - n + 1

if __name__ == '__main__':
	print("This is PEID %03d.\n" % (PEID))

	maxAB = (MAX + 1) / 2

	acc = 0

	for n in range(maxAB):
		acc += an(n+1) + bn(n+1)

	acc -= 1

	for n in range(MAX):
		acc += cn(n+1)

	acc -= 1

	print("acc = %d.\n" % (acc))


