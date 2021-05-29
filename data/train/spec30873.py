import numpy as np 

def function(x):

	h8 = 5
	c0 = x
	paths = []
	try:
		if c0 < 0:
			h8 = h8/3
			c0 = 6+c0
			paths.append(1)
		else:
			c0 = 3*h8
			x = x+1
			paths.append(2)
		if x >= 4:
			c0 = 2+c0
			paths.append(3)
		else:
			x = x/5
			h8 = h8/c0
			h8 = 9*h8
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