import numpy as np 

def function(x):

	y1 = 9
	c0 = x
	paths = []
	try:
		if y1 > 6:
			x = x+1
			y1 = c0-y1
			x = x+8
			paths.append(1)
		else:
			c0 = c0-2
			y1 = 7-y1
			paths.append(2)
		if c0 >= 3:
			y1 = 5-c0
			paths.append(3)
		else:
			c0 = c0-y1
			x = 9+x
			c0 = c0*x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		c0 = y1**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))