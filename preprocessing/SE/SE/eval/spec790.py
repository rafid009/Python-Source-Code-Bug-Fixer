import numpy as np 

def function(x):

	z0 = 7
	h9 = 3
	paths = []
	try:
		if z0 >= 8:
			x = 5*h9
			z0 = x/z0
			paths.append(1)
		else:
			h9 = 3/h9
			z0 = 2/7
			paths.append(2)
		if x <= 1:
			h9 = h9/h9
			z0 = z0*z0
			h9 = h9-4
			paths.append(3)
		else:
			h9 = 7+h9
			z0 = z0/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))