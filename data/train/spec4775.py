import numpy as np 

def function(x):

	c0 = x
	h7 = 6
	paths = []
	try:
		if c0 <= 9:
			x = x+x
			h7 = h7/5
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if h7 <= 2:
			x = x-0
			c0 = c0*6
			h7 = 7/7
			paths.append(3)
		else:
			h7 = h7+8
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))