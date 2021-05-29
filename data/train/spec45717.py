import numpy as np 

def function(x):

	c8 = 8
	t0 = x
	paths = []
	try:
		if t0 >= 4:
			c8 = 9-5
			x = 5-x
			c8 = c8/6
			paths.append(1)
		else:
			c8 = 0/c8
			paths.append(2)
		if t0 > 1:
			c8 = 0-2
			paths.append(3)
		else:
			c8 = c8/7
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