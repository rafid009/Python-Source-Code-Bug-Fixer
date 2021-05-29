import numpy as np 

def function(x):

	g0 = 1
	c0 = x
	paths = []
	try:
		if x < 2:
			x = x-2
			c0 = 5/x
			g0 = 7/3
			paths.append(1)
		else:
			c0 = c0+9
			paths.append(2)
		if g0 >= 6:
			g0 = 3-g0
			c0 = 5+c0
			c0 = 8*3
			paths.append(3)
		else:
			g0 = g0-2
			c0 = 5+2
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		c0 = g0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))