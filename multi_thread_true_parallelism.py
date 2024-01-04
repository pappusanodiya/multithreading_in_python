import threading 
import time

start = time.perf_counter()

# CPU bound operation

def a():
	i = 1
	while i <= 100000000:
		i = i + 1
	print(i)

t1 = threading.Thread(target=a)
t2 = threading.Thread(target=a)
t3 = threading.Thread(target=a)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
total = end - start
print("Total Time Consumed by CPU: " , total)
