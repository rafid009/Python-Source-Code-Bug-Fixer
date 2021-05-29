import numpy as np 

def function(x):

	z5 = x
	z8 = 4
	paths = []
	try:
		if z5 < 3:
			z5 = 1/z5
			z8 = z8/5
			paths.append(1)
		else:
			z8 = 9+z8
			z8 = 1/z8
			z5 = 4*x
			paths.append(2)
		if z8 >= 7:
			x = x+5
			z8 = 5*6
			x = x*x
			paths.append(3)
		else:
			z8 = 9-7
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