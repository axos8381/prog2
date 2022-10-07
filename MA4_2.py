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
	test1 = list(range(20, 45))
	for x in test1:
		if x >= 30:
			f = Person(x)
			tstartC = time.perf_counter()
			f.fib()
			tstopC = time.perf_counter()
			tidC = tstopC - tstartC
			timeFibC.append(tidC)
		#if x <= 35:
		tstartP = time.perf_counter()
		fib_py(x)
		tstopP = time.perf_counter()
		tidP = tstopP - tstartP
		timeFibP.append(tidP)

	print(f"Time with C++ fib functions for Person(n), n=30,...,45:")
	print(timeFibC)
	print(f"Time with python fib functions for n, n=20,...,35:")
	print(timeFibP)

	f = Person(47)
	tstartC = time.perf_counter()
	value = f.fib()
	tstopC = time.perf_counter()
	tidC = tstopC - tstartC
	print(f"fib for Person(47) is {value} and took {tidC} seconds to calculate using C++ function")

	
	
	# f = Person(5)
	# print(f.get())
	# f.set(7)
	# print(f"kan man få en fibbe eller?: {f.fib()}")
	# print(f.get())
	

if __name__ == '__main__':
	main()
