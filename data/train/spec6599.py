import numpy as np 

def function(x):

	n0 = 8
	c2 = x
	x = x
	paths = []
	try:
		if x <= 1:
			x = x*n0
			paths.append(1)
		else:
			n0 = 8/n0
			paths.append(2)
		if x < 4:
			c2 = c2-c2
			paths.append(3)
		else:
			c2 = c2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))