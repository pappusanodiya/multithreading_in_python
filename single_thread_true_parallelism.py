import threading 
import time

start = time.perf_counter()

# CPU bound operation

def a():
	i = 1
	while i <= 100000000:
		i = i + 1
	print(i)

a()
end = time.perf_counter()
total = end - start
print("Total Time Consumed by CPU: " , total)
