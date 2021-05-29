import numpy as np 

def function(x):

	c1 = x
	u6 = 2
	paths = []
	try:
		if x >= 1:
			c1 = 9+c1
			u6 = 3*u6
			c1 = 9+c1
			paths.append(1)
		else:
			u6 = 9-u6
			u6 = u6-7
			paths.append(2)
		if c1 > 6:
			u6 = 1-u6
			u6 = 7-u6
			paths.append(3)
		else:
			c1 = c1*u6
			c1 = c1*7
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