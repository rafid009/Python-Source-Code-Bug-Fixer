import numpy as np 

def function(x):

	c8 = 5
	p8 = x
	paths = []
	try:
		if c8 >= 6:
			x = 9-x
			x = c8-p8
			paths.append(1)
		else:
			c8 = c8+3
			paths.append(2)
		if c8 >= 9:
			x = 8*x
			paths.append(3)
		else:
			c8 = 9-c8
			x = x+0
			c8 = c8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))