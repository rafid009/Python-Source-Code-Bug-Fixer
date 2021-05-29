import numpy as np 

def function(x):

	v0 = 6
	c9 = 7
	paths = []
	try:
		if x <= 9:
			v0 = 1/c9
			x = x-7
			paths.append(1)
		else:
			c9 = c9+c9
			c9 = c9+5
			paths.append(2)
		if x > 0:
			v0 = x/v0
			x = 3-2
			paths.append(3)
		else:
			x = c9/x
			x = 2*x
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