import numpy as np 

def function(x):

	k4 = 4
	e7 = 7
	paths = []
	try:
		if x > 1:
			e7 = 9*e7
			x = 2*9
			paths.append(1)
		else:
			k4 = k4/e7
			paths.append(2)
		if x >= 1:
			e7 = e7/2
			e7 = e7/9
			x = 9/k4
			paths.append(3)
		else:
			k4 = k4*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))