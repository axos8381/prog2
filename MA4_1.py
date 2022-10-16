#!/usr/bin/env python3


import random
import math
import matplotlib.pyplot as plt
import concurrent.futures as future
import time


def lessThanOne(num):
	if(num>1):
		return False
	else:
		return True


############################# 1.1 ####################


def monteCarlo(n,r):
	xcordInside = []
	ycordInside = []
	xcordOutside = []
	ycordOutside = []

	for i in range(n):
		y = random.uniform(-1*r,1*r)
		x = random.uniform(-1*r,1*r)
		absLen = math.sqrt( pow(x,2) + pow(y,2))

		if absLen > r:
			xcordOutside.append(x)
			ycordOutside.append(y)

		else:
			xcordInside.append(x)
			ycordInside.append(y)

	return xcordInside, ycordInside, xcordOutside, ycordOutside




############################# 1.2 ####################

def monteCarloSfar(n,d):
	p = lambda x : pow(x,2)#lambda is higher order function 1
	listOfPoints = [[p(random.uniform(-1,1)) for ii in range(d)] for jj in range(n)]#list comprehension is higher order function 2
	listOfPointsSquared = list(map(sum, listOfPoints))#map is higher order function 3
	listOfPointsSquaredInside = list(filter(lessThanOne, listOfPointsSquared))#filter is higher order function 4
	return pow(2,d) * len(listOfPointsSquaredInside)/n


############################# 1.3 ####################

def multiMonteCarloSfar(n,d):
	with future.ProcessPoolExecutor() as ex:
		nList = [int(n/10)]*10
		dList = [d]*10
		result = ex.map(_multiMonteCarloSfar, nList, dList)
	return sum(result)/n


def _multiMonteCarloSfar(n,d):
	p = lambda x : pow(x,2)
	listOfPoints = [[p(random.uniform(-1,1)) for ii in range(d)] for jj in range(n)]
	listOfPointsSquared = list(map(sum, listOfPoints))
	listOfPointsSquaredInside = list(filter(lessThanOne, listOfPointsSquared))
	return pow(2,d) * len(listOfPointsSquaredInside)


if __name__ == "__main__":

	################ 1.1 #######################
	# print("1.1")
	# print()
	# print(f"Python built in constant for pi: pi = {math.pi}")

	# print()
	nrOfPoints = 1000
	xListIn, yListIn, xListOut, yListOut = monteCarlo(nrOfPoints, 1)

	# print(f"Number of points inside the circle: nc = {len(xListIn)}, with total amount of points {nrOfPoints}")
	# print(f"Approximation of pi from Monte Carlo method, with n = {nrOfPoints}: pi = {4 * len(xListIn) / nrOfPoints}")


	fig, ax=plt.subplots(1)
	ax.set_aspect('equal')
	ax.scatter(xListIn, yListIn, c='r', alpha=0.8, edgecolors=None)
	ax.scatter(xListOut, yListOut, c='b', alpha=0.8, edgecolors=None)
	ax.set_title(f"plot with n = {nrOfPoints}")
	fig.savefig('pi_1000_points.png')

	# print()
	nrOfPoints = 10000
	xListIn, yListIn, xListOut, yListOut = monteCarlo(nrOfPoints, 1)

	# print(f"Number of points inside the circle: nc = {len(xListIn)}, with total amount of points {nrOfPoints}")
	# print(f"Approximation of pi from Monte Carlo method, with n = {nrOfPoints}: pi = {4 * len(xListIn) / nrOfPoints}")

	fig, ax=plt.subplots(1)
	ax.set_aspect('equal')
	ax.scatter(xListIn, yListIn, c='r', alpha=0.8, edgecolors=None)
	ax.scatter(xListOut, yListOut, c='b', alpha=0.8, edgecolors=None)
	ax.set_title(f"plot with n = {nrOfPoints}")
	fig.savefig('pi_10000_points.png')

	# print()
	nrOfPoints = 100000
	xListIn, yListIn, xListOut, yListOut = monteCarlo(nrOfPoints, 1)

	# print(f"Number of points inside the circle: nc = {len(xListIn)}, with total amount of points {nrOfPoints}")
	# print(f"Approximation of pi from Monte Carlo method, with n = {nrOfPoints}: pi = {4 * len(xListIn) / nrOfPoints}")

	fig, ax=plt.subplots(1)
	ax.set_aspect('equal')
	ax.scatter(xListIn, yListIn, c='r', alpha=0.8, edgecolors=None)
	ax.scatter(xListOut, yListOut, c='b', alpha=0.8, edgecolors=None)
	ax.set_title(f"plot with n = {nrOfPoints}")
	fig.savefig('pi_100000_points.png')

	################ 1.2 #######################
	# print()
	# print("1.2")
	# print()	
	# n = 100000
	# d = 11
	# calculatedVolume = monteCarloSfar(n,d)
	# theroeticalVolume = pow(math.pi,d/2) * pow(1,d) / math.gamma(1 + (d/2) )
	# print(f"Theoretical volume of d-dimensional sphere with radius 1 and {d} dimensions is: V = {theroeticalVolume}")
	# print(f"Calculated volume of d-dimensional sphere with radius 1 and {d} dimensions, useing n = {n} amount of points, is: V = {calculatedVolume}")

	# print()
	# n = 100000
	# d = 2
	# calculatedVolume = monteCarloSfar(n,d)
	# theroeticalVolume = pow(math.pi,d/2) * pow(1,d) / math.gamma(1 + (d/2) )
	# print(f"Theoretical volume of d-dimensional sphere with radius 1 and {d} dimensions is: V = {theroeticalVolume}")
	# print(f"Calculated volume of d-dimensional sphere with radius 1 and {d} dimensions, useing n = {n} amount of points, is: V = {calculatedVolume}")

#(n,d) = (100000, 2) => V_theory = 3.141592653589793 , V_theory = 3.141592653589793 , V_calculated ≈ 3.14
#(n,d) = (100000, 11) => V_theory = 3.141592653589793 , V_theory = 1.8841038793898994 , V_calculated ≈ 1.88


	################ 1.3 #######################
	# print()
	# print("1.3")
	# print()
	# tstart1 = time . perf_counter ()
	# calculatedVolume = monteCarloSfar(10000000,11)
	# tstop1 = time . perf_counter ()
	# print ( f" Measured time for code from 1.2 with (n,d) = (10000000,11) is : {tstop1 - tstart1} seconds ")
	#Takes ca 70 seconds

	# print()
	# tstart2 = time . perf_counter ()
	# multiCalculatedVolume = multiMonteCarloSfar(10000000,11)
	# tstop2 = time . perf_counter ()
	# print ( f" Measured time for code from 1.2 with (n,d) = (10000000,11) is : {tstop2 - tstart2} seconds ")
	#Takes ca 30 seconds

	#8 Threads, 4 cores on my computor
	#By Multiprocessing we devide it over the cores, by deviding 10 processes over 4 cores it takes about 3 times as fast
	#It is closer to dubbel the speed, but when doing smaler calculations it is closer to 3 timesa s fast with the code (up to d=8)



