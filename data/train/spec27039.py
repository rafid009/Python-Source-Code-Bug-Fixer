import numpy as np 

def function(x):

	h0 = x
	c1 = 1
	paths = []
	try:
		if c1 >= 9:
			c1 = 9*c1
			h0 = 7*h0
			c1 = 1/c1
			paths.append(1)
		else:
			x = 9/x
			c1 = x-0
			h0 = h0-6
			paths.append(2)
		if h0 < 1:
			h0 = 1/h0
			x = 2*0
			x = x+x
			paths.append(3)
		else:
			h0 = 3+x
			c1 = 3+c1
			x = 7+8
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		c1 = h0**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))