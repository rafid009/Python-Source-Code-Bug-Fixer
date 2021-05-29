import numpy as np 

def function(x):

	c0 = 0
	h4 = 4
	paths = []
	try:
		if c0 < 5:
			c0 = h4-9
			c0 = c0-0
			paths.append(1)
		else:
			h4 = h4*7
			paths.append(2)
		if x < 8:
			c0 = c0/9
			c0 = c0-0
			paths.append(3)
		else:
			c0 = 6+0
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))