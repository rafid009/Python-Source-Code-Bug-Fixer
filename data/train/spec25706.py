import numpy as np 

def function(x):

	c8 = 5
	c9 = x
	paths = []
	try:
		if x < 6:
			c8 = c8+2
			paths.append(1)
		else:
			x = x-4
			c9 = c9*8
			paths.append(2)
		if c8 >= 6:
			c8 = 9/x
			c8 = 3/8
			paths.append(3)
		else:
			c8 = 1-c8
			c8 = 6*c8
			x = 4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))