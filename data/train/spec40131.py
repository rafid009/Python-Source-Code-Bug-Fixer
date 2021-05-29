import numpy as np 

def function(x):

	j5 = x
	c9 = 5
	paths = []
	try:
		if c9 < 6:
			x = x+4
			x = x/7
			paths.append(1)
		else:
			c9 = c9*j5
			paths.append(2)
		if x >= 3:
			c9 = c9-9
			j5 = 4*j5
			paths.append(3)
		else:
			c9 = c9/3
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