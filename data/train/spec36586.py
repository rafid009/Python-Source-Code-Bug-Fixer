import numpy as np 

def function(x):

	a3 = x
	x7 = 8
	paths = []
	try:
		if x < 7:
			a3 = 9/x
			x = 0-x
			paths.append(1)
		else:
			x = x7/x
			x7 = 0*x7
			paths.append(2)
		if a3 < 0:
			a3 = x7-a3
			x = x*a3
			paths.append(3)
		else:
			x = x*x7
			a3 = a3*3
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))