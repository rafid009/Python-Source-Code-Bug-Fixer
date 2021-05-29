import numpy as np 

def function(x):

	h9 = x
	c3 = x
	paths = []
	try:
		if c3 <= 2:
			h9 = x-x
			paths.append(1)
		else:
			x = c3+c3
			c3 = c3+c3
			paths.append(2)
		if h9 <= 5:
			h9 = c3*h9
			h9 = h9-h9
			paths.append(3)
		else:
			c3 = c3+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))