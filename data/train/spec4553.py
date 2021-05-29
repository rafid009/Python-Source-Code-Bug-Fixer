import numpy as np 

def function(x):

	c9 = x
	f4 = 9
	paths = []
	try:
		if f4 < 3:
			c9 = f4/2
			paths.append(1)
		else:
			c9 = 6-c9
			x = 8/2
			x = 0-x
			paths.append(2)
		if c9 <= 9:
			x = 8-c9
			c9 = 0*c9
			paths.append(3)
		else:
			c9 = c9-5
			f4 = 9+3
			c9 = 1/c9
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