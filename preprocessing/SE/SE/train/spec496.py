import numpy as np 

def function(x):

	c1 = 7
	h5 = x
	x = x
	paths = []
	try:
		if c1 <= 7:
			h5 = x-h5
			c1 = c1+c1
			c1 = c1-3
			paths.append(1)
		else:
			h5 = x+c1
			paths.append(2)
		if h5 <= 1:
			h5 = 4+h5
			h5 = 1/x
			paths.append(3)
		else:
			c1 = h5/c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))