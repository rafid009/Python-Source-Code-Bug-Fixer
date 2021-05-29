import numpy as np 

def function(x):

	c0 = 5
	z8 = 2
	paths = []
	try:
		if z8 > 4:
			z8 = z8/z8
			x = 2*c0
			paths.append(1)
		else:
			z8 = c0/9
			c0 = c0+z8
			paths.append(2)
		if c0 > 0:
			z8 = 5/c0
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))