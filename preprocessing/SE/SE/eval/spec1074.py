import numpy as np 

def function(x):

	c4 = 6
	y0 = x
	paths = []
	try:
		if c4 > 1:
			c4 = c4+3
			y0 = 2+6
			x = x/3
			paths.append(1)
		else:
			y0 = 8-x
			c4 = 1-y0
			y0 = y0+y0
			paths.append(2)
		if x >= 9:
			c4 = 3+c4
			x = c4/x
			paths.append(3)
		else:
			c4 = y0*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))