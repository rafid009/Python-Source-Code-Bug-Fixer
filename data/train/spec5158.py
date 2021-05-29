import numpy as np 

def function(x):

	e5 = 2
	z0 = x
	paths = []
	try:
		if e5 >= 9:
			z0 = 4/z0
			e5 = 2*9
			paths.append(1)
		else:
			z0 = z0-2
			paths.append(2)
		if z0 <= 0:
			z0 = z0+z0
			x = x*9
			paths.append(3)
		else:
			e5 = e5-e5
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