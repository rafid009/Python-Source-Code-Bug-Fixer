import numpy as np 

def function(x):

	z0 = 8
	c0 = 6
	x = x
	paths = []
	try:
		if c0 < 0:
			z0 = z0*z0
			c0 = 3*c0
			z0 = 9+z0
			paths.append(1)
		else:
			c0 = 2*x
			z0 = c0+c0
			paths.append(2)
		if z0 >= 0:
			z0 = 2/2
			x = x*3
			x = 5*x
			paths.append(3)
		else:
			c0 = c0*5
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