#!/usr/bin/env python3.9

from person import Person
import time
from numba import njit


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))


@njit
def  fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	

def main():
	timeFibC = []
	timeFibP = []
	timeFibN = []
	test1 = list(range(20, 46))
	for x in test1:
		if x >= 30:
			f = Person(x)
			tstartC = time.perf_counter()
			f.fib()
			tstopC = time.perf_counter()
			tidC = tstopC - tstartC
			timeFibC.append(tidC)
		else:
			timeFibC.append(0)


		tstartN = time.perf_counter()
		fib_numba(x)
		tstopN = time.perf_counter()
		tidN = tstopN - tstartN
		timeFibP.append(tidN)

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
	f.fib()
	tstopC = time.perf_counter()
	tidC = tstopC - tstartC
	print(f"fib for Person(47) took {tidC} seconds to calculate using C++ function")

	tstartN = time.perf_counter()
	fib_numba(47)
	tstopN = time.perf_counter()
	tidN = tstopN - tstartN
	print(f"fib for fib(47) took {tidN} seconds to calculate using Python with numba function")


	

if __name__ == '__main__':
	main()
