import numpy as np 

def function(x):

	y5 = 3
	q2 = 1
	paths = []
	try:
		if x >= 6:
			x = 3*x
			paths.append(1)
		else:
			x = x*7
			x = y5-4
			paths.append(2)
		if x > 0:
			x = 7/y5
			q2 = 9*q2
			x = 8-q2
			paths.append(3)
		else:
			q2 = x*0
			y5 = y5+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))