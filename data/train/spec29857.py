import numpy as np 

def function(x):

	c1 = x
	h7 = 3
	paths = []
	try:
		if c1 > 0:
			h7 = h7+4
			paths.append(1)
		else:
			h7 = h7+9
			paths.append(2)
		if c1 > 0:
			c1 = c1*x
			h7 = h7/h7
			h7 = 2-3
			paths.append(3)
		else:
			c1 = c1*h7
			c1 = 8/5
			c1 = c1/c1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		c1 = h7**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))