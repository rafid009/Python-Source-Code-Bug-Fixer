import numpy as np 

def function(x):

	c3 = 7
	c7 = x
	paths = []
	try:
		if c3 <= 9:
			c3 = 9/c7
			paths.append(1)
		else:
			c7 = 8/c7
			c3 = x/c7
			x = x+c7
			paths.append(2)
		if c3 > 8:
			c7 = c3-6
			c7 = c7/3
			paths.append(3)
		else:
			x = 7/x
			c3 = 9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))