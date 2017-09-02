
import threading
import time

# Author
# ======
#
# Yaoyu Hu <huyaoyu@sjtu.edu.cn>
#
# Date
# ====
#
# Created on 2017-09-02
#
# Description
# ===========
#
# Try out the threading module.
#
# This sample code is composed by referring to 
# http://www.w3big.com/python3/python3-multithreading.html
# 

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, threadID, name, delay):
		super(myThread, self).__init__()
		self.threadID = threadID
		self.name = name
		self.delay = delay
		
	def run(self):
		"""pass"""

		print("Thread %s started." % (self.name))

		threadLock.acquire()
		print_time(self.name, self.delay, 3)
		threadLock.release()

def print_time(threadName, delay, counter):
	"""pass"""

	while counter:
		time.sleep(delay)
		print("%s, %s" % (threadName, time.ctime( time.time() )))
		counter -= 1

threadLock = threading.Lock()
threads = []

if __name__ == "__main__":
	t1 = myThread(1, "Thread01", 1)
	t2 = myThread(2, "Thread02", 2)

	t1.start()
	t2.start()

	threads.append(t1)
	threads.append(t2)

	for t in threads:
		t.join()

	print("Done")


