import numpy as np 

def function(x):

	z0 = x
	x8 = x
	paths = []
	try:
		if z0 < 9:
			x = x-8
			paths.append(1)
		else:
			z0 = 1/z0
			x = 1/x
			paths.append(2)
		if x8 >= 8:
			z0 = z0-x
			x8 = 8/x
			paths.append(3)
		else:
			z0 = x8*z0
			x8 = x8/4
			x8 = 8*x
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