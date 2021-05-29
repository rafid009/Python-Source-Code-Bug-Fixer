import numpy as np 

def function(x):

	c9 = x
	y1 = x
	paths = []
	try:
		if c9 > 2:
			c9 = y1-1
			y1 = 1*5
			paths.append(1)
		else:
			x = x*c9
			c9 = c9+y1
			paths.append(2)
		if y1 <= 6:
			y1 = 5+2
			x = y1-x
			paths.append(3)
		else:
			x = 3/x
			y1 = y1+2
			y1 = c9*8
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