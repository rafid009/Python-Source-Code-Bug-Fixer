import numpy as np 

def function(x):

	c4 = 3
	h2 = 0
	paths = []
	try:
		if c4 >= 5:
			x = h2/x
			h2 = h2+2
			c4 = 7/3
			paths.append(1)
		else:
			c4 = c4+4
			h2 = h2/c4
			x = x/c4
			paths.append(2)
		if c4 >= 1:
			h2 = x-h2
			h2 = 7*h2
			paths.append(3)
		else:
			x = 6/c4
			h2 = 6+h2
			c4 = h2*7
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