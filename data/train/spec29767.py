import numpy as np 

def function(x):

	c4 = x
	h4 = 0
	paths = []
	try:
		if h4 <= 1:
			c4 = c4+3
			x = 8/x
			paths.append(1)
		else:
			c4 = c4-h4
			x = x-x
			paths.append(2)
		if h4 > 4:
			x = x+c4
			paths.append(3)
		else:
			c4 = 4/2
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