import numpy as np 

def function(x):

	c6 = 0
	e7 = x
	paths = []
	try:
		if c6 < 4:
			e7 = e7+6
			e7 = e7/x
			paths.append(1)
		else:
			e7 = 5+e7
			paths.append(2)
		if x < 1:
			c6 = 2-c6
			paths.append(3)
		else:
			e7 = x*e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))