import numpy as np 

def function(x):

	z0 = 6
	paths = []
	try:
		if z0 > 2:
			x = x*3
			z0 = 6+x
			paths.append(1)
		else:
			z0 = z0/z0
			x = x-4
			z0 = 4-z0
			paths.append(2)
		if x > 1:
			z0 = x/x
			x = x*9
			z0 = 5/z0
			paths.append(3)
		else:
			z0 = z0-4
			z0 = 0-9
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