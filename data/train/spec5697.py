import numpy as np 

def function(x):

	z0 = x
	h5 = x
	x = 2
	paths = []
	try:
		if h5 <= 8:
			h5 = h5-z0
			x = 3-x
			paths.append(1)
		else:
			x = 6*x
			h5 = 8-h5
			paths.append(2)
		if h5 <= 9:
			z0 = 9*h5
			x = 1+z0
			z0 = z0+1
			paths.append(3)
		else:
			h5 = 5+4
			x = x-2
			x = x-6
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		z0 = h5**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))