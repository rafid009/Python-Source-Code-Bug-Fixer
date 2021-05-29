import numpy as np 

def function(x):

	o9 = 2
	c1 = x
	paths = []
	try:
		if x <= 2:
			x = 7/x
			o9 = o9+o9
			paths.append(1)
		else:
			x = 1/2
			x = x-4
			c1 = 3+x
			paths.append(2)
		if x < 5:
			x = c1-6
			paths.append(3)
		else:
			x = o9-c1
			c1 = 1/x
			c1 = 7-c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))