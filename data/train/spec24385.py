import numpy as np 

def function(x):

	z0 = x
	c7 = 1
	paths = []
	try:
		if c7 >= 2:
			c7 = c7+c7
			paths.append(1)
		else:
			x = x-8
			x = x+3
			c7 = 5-c7
			paths.append(2)
		if x >= 7:
			c7 = 9/9
			z0 = 9+3
			paths.append(3)
		else:
			x = x/7
			z0 = z0-c7
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