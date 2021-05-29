import numpy as np 

def function(x):

	z1 = 7
	c6 = x
	paths = []
	try:
		if z1 <= 2:
			z1 = 7/z1
			z1 = 2/2
			c6 = c6/z1
			paths.append(1)
		else:
			z1 = z1+8
			z1 = 7/z1
			z1 = z1/9
			paths.append(2)
		if x >= 0:
			x = 7-x
			c6 = z1/z1
			c6 = 6+c6
			paths.append(3)
		else:
			c6 = x+5
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