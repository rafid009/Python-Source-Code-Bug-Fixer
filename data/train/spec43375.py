import numpy as np 

def function(x):

	c1 = 8
	r5 = 8
	paths = []
	try:
		if c1 >= 3:
			r5 = c1-4
			paths.append(1)
		else:
			c1 = c1+r5
			x = 9/x
			paths.append(2)
		if c1 < 6:
			x = x/c1
			paths.append(3)
		else:
			c1 = 2/c1
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