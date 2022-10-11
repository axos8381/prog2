#!/usr/bin/env python3.9

from person import Person
import time
from numba import njit
import matplotlib.pyplot as plt


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
		return(fib_numba(n-1) + fib_numba(n-2))
	

def main():
	timeFibC = []
	timeFibP = []
	timeFibN = []
	nValues = list(range(20, 46))
	nValuesP = list(range(20, 43))
	for x in nValues:
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
		timeFibN.append(tidN)
		if x < 43:
			tstartP = time.perf_counter()
			fib_py(x)
			tstopP = time.perf_counter()
			tidP = tstopP - tstartP
			timeFibP.append(tidP)
		

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



	plt.figure(figsize=(5, 2.7), layout='constrained')
	plt.plot(nValues, timeFibC, label='C++')
	plt.plot(nValuesP, timeFibP, label='Normal Python')
	plt.plot(nValues, timeFibN, label='Numba Python')
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title("Fibonacci calculations")
	plt.legend()
	plt.savefig('Fibonacci_plot.png')


	

if __name__ == '__main__':
	main()
