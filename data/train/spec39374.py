import numpy as np 

def function(x):

	z0 = 0
	z5 = x
	paths = []
	try:
		if z5 > 4:
			x = 4*x
			x = x-4
			z5 = x+z5
			paths.append(1)
		else:
			z0 = z0-4
			z0 = z0/2
			paths.append(2)
		if z0 > 2:
			z0 = x*5
			x = 5*6
			paths.append(3)
		else:
			x = z0*7
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))