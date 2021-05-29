import numpy as np 

def function(x):

	c8 = x
	k4 = 7
	paths = []
	try:
		if x > 2:
			k4 = k4*5
			x = x-2
			x = c8-4
			paths.append(1)
		else:
			k4 = 4*c8
			x = x/2
			paths.append(2)
		if k4 <= 2:
			c8 = 6-x
			k4 = k4-4
			x = x/1
			paths.append(3)
		else:
			x = c8/x
			x = 7/x
			c8 = c8/1
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