import numpy as np 

def function(x):

	z0 = x
	c9 = x
	paths = []
	try:
		if z0 < 8:
			z0 = 6*z0
			z0 = 3-z0
			paths.append(1)
		else:
			x = x-8
			x = 2-3
			paths.append(2)
		if z0 >= 3:
			x = 6+x
			paths.append(3)
		else:
			z0 = z0-7
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))