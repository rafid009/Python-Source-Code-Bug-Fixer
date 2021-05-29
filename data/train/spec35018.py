import numpy as np 

def function(x):

	c9 = 8
	x4 = x
	paths = []
	try:
		if x > 2:
			x = 8+3
			x = x4*c9
			x = c9+0
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if c9 < 4:
			c9 = 2-c9
			paths.append(3)
		else:
			c9 = x4+x4
			x4 = x4-2
			x4 = 1-3
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