import numpy as np 

def function(x):

	c8 = 9
	z6 = x
	x = x
	paths = []
	try:
		if c8 < 4:
			x = x-8
			c8 = 0-c8
			paths.append(1)
		else:
			c8 = 2/c8
			z6 = z6*5
			x = c8-7
			paths.append(2)
		if z6 < 1:
			z6 = z6-6
			paths.append(3)
		else:
			z6 = c8-3
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))