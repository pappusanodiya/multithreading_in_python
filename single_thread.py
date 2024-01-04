import time

start = time.perf_counter()
def coffee():
	print("start preparing coffee ...")
	time.sleep(2)
	print("finished coffee..")
def tea():
	print("start preparing tea....")
	time.sleep(3)
	print("finished tea..")

print("hi i m in main function")
coffee()
tea()

end = time.perf_counter()
total = end - start
print("Total Time Consumed by CPU: " , total)
