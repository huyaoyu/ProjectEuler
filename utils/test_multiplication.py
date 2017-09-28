
import time

MAX = 10000000

AVG_MAX = 10

if __name__ == '__main__':
	n = 1.0

	t = 0

	for j in range(AVG_MAX):
		print("%d, " % (j), end="")

		t0 = time.clock()

		for i in range(1, MAX):
			n *= i
			n /= i

		t1 = time.clock()

		time.sleep(0.1)

		t += t1 - t0

		print(t1 - t0)

	print(t)
	print(t/AVG_MAX)

