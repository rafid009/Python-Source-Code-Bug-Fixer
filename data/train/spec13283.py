import numpy as np 

def function(x):

	n0 = x
	z0 = 0
	paths = []
	try:
		if z0 >= 9:
			n0 = 2-z0
			n0 = n0-8
			n0 = 8+x
			paths.append(1)
		else:
			z0 = 8-4
			x = 9*4
			x = 2+x
			paths.append(2)
		if z0 >= 8:
			z0 = z0/8
			paths.append(3)
		else:
			x = 0-4
			z0 = 7/z0
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