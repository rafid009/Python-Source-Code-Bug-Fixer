import numpy as np 

def function(x):

	z6 = 0
	c6 = 7
	paths = []
	try:
		if c6 < 8:
			z6 = z6+5
			x = x*4
			c6 = c6-x
			paths.append(1)
		else:
			c6 = c6*9
			paths.append(2)
		if x > 6:
			c6 = 6/x
			paths.append(3)
		else:
			c6 = c6-3
			z6 = 8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))