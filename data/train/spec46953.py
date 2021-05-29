import numpy as np 

def function(x):

	c7 = x
	h9 = 9
	paths = []
	try:
		if c7 > 5:
			x = x+0
			c7 = h9/c7
			c7 = c7*4
			paths.append(1)
		else:
			h9 = h9*x
			paths.append(2)
		if c7 > 9:
			h9 = 1-h9
			paths.append(3)
		else:
			c7 = x+c7
			h9 = h9/6
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