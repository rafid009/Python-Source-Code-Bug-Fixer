import numpy as np 

def function(x):

	h9 = x
	c7 = 2
	paths = []
	try:
		if c7 <= 7:
			c7 = c7-c7
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if h9 < 3:
			x = 8*x
			paths.append(3)
		else:
			x = 8/h9
			h9 = h9*h9
			h9 = h9*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))