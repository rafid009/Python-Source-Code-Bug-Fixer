import numpy as np 

def function(x):

	h3 = x
	c0 = 1
	paths = []
	try:
		if c0 > 8:
			h3 = 0/h3
			c0 = h3/6
			x = x*8
			paths.append(1)
		else:
			c0 = c0+8
			c0 = 8+c0
			paths.append(2)
		if x <= 9:
			h3 = 0+2
			h3 = 6-h3
			paths.append(3)
		else:
			h3 = 7+c0
			x = c0+c0
			c0 = c0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))