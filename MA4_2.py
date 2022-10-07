#!/usr/bin/env python3.9

from person import Person
import time

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def  fib_numba(n):
	pass

def main():
	timeFibC = []
	timeFibP = []
	timeFibN = []
	test1 = list(range(30, 45))
	for x in test1:
		f = Person(x)
		tstartC = time.perf_counter()
		f.fib()
		tstopC = time.perf_counter()
		tidC = tstartC - tstopC
		timeFibC.append(tidC)

	print(timeFibC)


	
	
	# f = Person(5)
	# print(f.get())
	# f.set(7)
	# print(f"kan man få en fibbe eller?: {f.fib()}")
	# print(f.get())
	

if __name__ == '__main__':
	main()
