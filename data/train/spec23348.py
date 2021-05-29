import numpy as np 

def function(x):

	c0 = 3
	c8 = 4
	paths = []
	try:
		if c0 < 2:
			c8 = c8-0
			x = 6*x
			x = x/4
			paths.append(1)
		else:
			c0 = c0*8
			c0 = 3*2
			c8 = c8-0
			paths.append(2)
		if x >= 8:
			c8 = x/6
			paths.append(3)
		else:
			c8 = c8/x
			c0 = c0*2
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