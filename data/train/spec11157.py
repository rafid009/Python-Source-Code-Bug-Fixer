import numpy as np 

def function(x):

	c0 = 3
	e7 = 6
	paths = []
	try:
		if e7 < 7:
			x = 4-x
			paths.append(1)
		else:
			c0 = 9*e7
			c0 = c0-c0
			c0 = e7*9
			paths.append(2)
		if c0 < 2:
			c0 = 1*9
			e7 = 5*1
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))