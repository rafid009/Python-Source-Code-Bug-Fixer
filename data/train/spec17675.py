import numpy as np 

def function(x):

	a8 = 4
	z0 = 7
	paths = []
	try:
		if a8 > 3:
			z0 = z0/z0
			z0 = 8+z0
			z0 = x+8
			paths.append(1)
		else:
			a8 = a8+z0
			x = x-8
			paths.append(2)
		if z0 > 8:
			z0 = 1*4
			z0 = 5+z0
			paths.append(3)
		else:
			a8 = a8/4
			z0 = x/z0
			z0 = 3-a8
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