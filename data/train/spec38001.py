import numpy as np 

def function(x):

	z0 = x
	c7 = 0
	paths = []
	try:
		if x >= 9:
			x = 9-5
			x = 5-x
			paths.append(1)
		else:
			z0 = 4*z0
			z0 = z0-0
			paths.append(2)
		if c7 >= 3:
			c7 = 3-c7
			c7 = 1-c7
			paths.append(3)
		else:
			c7 = c7*x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))