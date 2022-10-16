#!/usr/bin/env python3

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
	timeFibP1 = []
	timeFibN1 = []
	timeFibP2 = []
	timeFibN2 = []

	nPlot1 = list(range(30, 46))
	nPlot2 = list(range(20, 31))
	nPlotP1 = list(range(30, 44))
	for x in nPlot1:
		f = Person(x)
		tstartC = time.perf_counter()
		f.fib()
		tstopC = time.perf_counter()
		tidC = tstopC - tstartC
		timeFibC.append(tidC)

		tstartN = time.perf_counter()
		fib_numba(x)
		tstopN = time.perf_counter()
		tidN = tstopN - tstartN
		timeFibN1.append(tidN)
		if x < 44:
			tstartP = time.perf_counter()
			fib_py(x)
			tstopP = time.perf_counter()
			tidP = tstopP - tstartP
			timeFibP1.append(tidP)
		
		
	for x in nPlot2:
		tstartN = time.perf_counter()
		fib_numba(x)
		tstopN = time.perf_counter()
		tidN = tstopN - tstartN
		timeFibN2.append(tidN)

		tstartP = time.perf_counter()
		fib_py(x)
		tstopP = time.perf_counter()
		tidP = tstopP - tstartP
		timeFibP2.append(tidP)

	

	


		
		
		

	f = Person(47)
	tstartC = time.perf_counter()
	c47 = f.fib()
	tstopC = time.perf_counter()
	tidC = tstopC - tstartC
	print(f"fib for Person(47) took {tidC} seconds to calculate using C++ function, getting fib(47) = {c47}")

	tstartN = time.perf_counter()
	n47 = fib_numba(47)
	tstopN = time.perf_counter()
	tidN = tstopN - tstartN
	print(f"fib for fib(47) took {tidN} seconds to calculate using Python with numba function, getting fib(47) = {n47}")



	plt.figure(figsize=(5, 2.7), layout='constrained')
	plt.plot(nPlot1, timeFibN1, label='Numba Python')
	plt.plot(nPlot1, timeFibC, label='C++')
	plt.plot(nPlotP1, timeFibP1, label='Normal Python')
	
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title("Fibonacci calculations")
	plt.legend()
	plt.savefig('Fibonacci_plot_high_n.png')



	plt.figure(figsize=(5, 2.7), layout='constrained')
	plt.plot(nPlot2, timeFibP2, label='Normal Python')
	plt.plot(nPlot2, timeFibN2, label='Numba Python')
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title("Fibonacci calculations")
	plt.legend()
	plt.savefig('Fibonacci_plot_low_n.png')





# fib(47) = -1323752223 in c++
# fib(47) = 2971215073 in python with numba
#The reason why c++ dont get it right and instead gets a negative number is that
# the numbers size is to large for the memory. In c++ when you can store 2^n diffrent informations depending on the data type.
# numbers need to store both positive and negative values. For the first half postiive numbers are stored and for the second half
# negative numbers are stored. For "int" 2^32 is the size of the memory, that means all numbers larger than 2^31 will be negative.
# 2^31 - fib(47) < 0 therefore we get a negative number in c++.









	

if __name__ == '__main__':
	main()
