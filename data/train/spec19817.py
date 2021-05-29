import numpy as np 

def function(x):

	y3 = x
	c9 = 9
	paths = []
	try:
		if x >= 2:
			c9 = 7-c9
			c9 = y3-c9
			c9 = 3-y3
			paths.append(1)
		else:
			y3 = y3-c9
			paths.append(2)
		if x >= 0:
			y3 = y3-x
			c9 = c9/c9
			x = y3*x
			paths.append(3)
		else:
			c9 = c9+2
			c9 = y3/y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))