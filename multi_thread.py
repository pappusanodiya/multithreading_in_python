import time
import threading

start = time.perf_counter()
def coffee():
	print("start preparing coffee ...")
	time.sleep(2)

	# I/O Bound Operation
	# network op / disk i/o printer op
	# ideal - not doing - wasting time
	# computing - operation - number crunching

	print("finished coffee..")
def tea():
	print("start preparing tea....")
	time.sleep(3)
	print("finished tea..")

t1 = threading.Thread( target=coffee )
t2 = threading.Thread( target=tea )

t1.start()
t2.start()

print("hi i m in main function")
t1.join()
t2.join()
print("my all thread completed ..")

end = time.perf_counter()
total = end - start
print("Total Time Consumed by CPU: " , total)


