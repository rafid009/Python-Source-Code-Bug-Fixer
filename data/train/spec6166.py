import numpy as np 

def function(x):

	h0 = x
	c2 = 3
	paths = []
	try:
		if h0 <= 6:
			c2 = c2/h0
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if c2 <= 7:
			h0 = c2-h0
			c2 = 5+7
			paths.append(3)
		else:
			h0 = h0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))