import numpy as np 

def function(x):

	z5 = 7
	n0 = x
	paths = []
	try:
		if n0 < 8:
			x = x*z5
			n0 = 2*n0
			x = 9-z5
			paths.append(1)
		else:
			x = 8/x
			x = x-7
			paths.append(2)
		if n0 < 8:
			x = x/7
			paths.append(3)
		else:
			n0 = n0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))