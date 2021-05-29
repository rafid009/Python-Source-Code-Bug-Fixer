import numpy as np 

def function(x):

	e3 = x
	z0 = 7
	paths = []
	try:
		if z0 > 2:
			z0 = 7+e3
			e3 = x/e3
			e3 = x+3
			paths.append(1)
		else:
			z0 = 3-z0
			paths.append(2)
		if z0 > 8:
			z0 = z0-6
			z0 = 2/z0
			e3 = e3/8
			paths.append(3)
		else:
			z0 = z0*8
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