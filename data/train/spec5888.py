import numpy as np 

def function(x):

	c0 = x
	n0 = x
	x = 9
	paths = []
	try:
		if x >= 2:
			n0 = n0-x
			c0 = 0-5
			paths.append(1)
		else:
			x = 9/x
			x = 0/x
			c0 = c0-1
			paths.append(2)
		if n0 > 8:
			c0 = x*n0
			n0 = c0/7
			x = x*x
			paths.append(3)
		else:
			c0 = 9-0
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		c0 = n0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))