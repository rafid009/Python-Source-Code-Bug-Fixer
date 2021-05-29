import numpy as np 

def function(x):

	c7 = 1
	c0 = x
	paths = []
	try:
		if x >= 4:
			c7 = c7-9
			c0 = c0+3
			paths.append(1)
		else:
			c0 = c0-3
			x = x*8
			x = x+x
			paths.append(2)
		if x <= 0:
			c7 = 9+2
			paths.append(3)
		else:
			c0 = 1/c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))