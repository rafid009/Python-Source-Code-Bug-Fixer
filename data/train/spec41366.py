import numpy as np 

def function(x):

	c9 = 1
	y3 = x
	paths = []
	try:
		if x >= 2:
			c9 = 1/c9
			paths.append(1)
		else:
			c9 = 1*c9
			c9 = c9-5
			paths.append(2)
		if c9 < 0:
			c9 = 0-5
			x = 6+y3
			c9 = c9+y3
			paths.append(3)
		else:
			y3 = y3+8
			c9 = y3*c9
			y3 = y3-3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		c9 = y3**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))