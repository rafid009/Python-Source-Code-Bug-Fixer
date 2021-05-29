import numpy as np 

def function(x):

	c9 = 6
	c5 = x
	paths = []
	try:
		if x >= 1:
			c9 = 9-2
			c5 = 8/4
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if x > 7:
			c9 = 6-x
			paths.append(3)
		else:
			c9 = 6*2
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