import numpy as np 

def function(x):

	y9 = 2
	c9 = 1
	paths = []
	try:
		if y9 < 5:
			x = x*9
			paths.append(1)
		else:
			c9 = 1*c9
			c9 = 0-3
			c9 = c9-c9
			paths.append(2)
		if y9 >= 2:
			c9 = 1*c9
			c9 = c9-5
			c9 = c9/c9
			paths.append(3)
		else:
			x = y9/x
			y9 = 7/c9
			y9 = 8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))