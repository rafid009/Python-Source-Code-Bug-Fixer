import numpy as np 

def function(x):

	z8 = x
	z0 = x
	paths = []
	try:
		if z8 < 2:
			z8 = 8-x
			x = x/x
			paths.append(1)
		else:
			x = x-9
			z0 = 7+x
			paths.append(2)
		if x < 0:
			x = x-0
			paths.append(3)
		else:
			z0 = 3*z0
			z0 = 8/4
			x = x*x
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