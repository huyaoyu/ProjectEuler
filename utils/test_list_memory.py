
import time

MAX = 1000000

AVG_MAX = 10

if __name__ == '__main__':
	t = 0


	t0 = time.clock()

	for i in range(1, MAX):
		l = []
		for j in range(AVG_MAX):
			l.append(j)

	t1 = time.clock()

	t = t1 - t0

	print(t)

