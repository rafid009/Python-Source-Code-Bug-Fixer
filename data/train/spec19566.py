import numpy as np 

def function(x):

	z1 = x
	z5 = x
	paths = []
	try:
		if z1 > 1:
			z1 = 1*z1
			x = x/z5
			paths.append(1)
		else:
			z1 = z1*z1
			z1 = 9-z1
			paths.append(2)
		if z1 > 7:
			z5 = 0-3
			z1 = 9+z1
			paths.append(3)
		else:
			z5 = 9+5
			x = x/x
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