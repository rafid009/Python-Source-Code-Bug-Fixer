import numpy as np 

def function(x):

	c0 = x
	e9 = x
	paths = []
	try:
		if x > 5:
			x = c0*x
			x = x-7
			paths.append(1)
		else:
			c0 = 4*e9
			c0 = x-c0
			c0 = c0+1
			paths.append(2)
		if x < 0:
			c0 = 0-4
			paths.append(3)
		else:
			e9 = e9+7
			x = 5/x
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