import numpy as np 

def function(x):

	n0 = 2
	c1 = 9
	paths = []
	try:
		if x > 2:
			c1 = x*x
			x = 6+2
			n0 = c1+n0
			paths.append(1)
		else:
			n0 = n0/n0
			paths.append(2)
		if n0 >= 8:
			n0 = n0+2
			n0 = 1-x
			x = x*n0
			paths.append(3)
		else:
			n0 = n0-8
			c1 = 3/6
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