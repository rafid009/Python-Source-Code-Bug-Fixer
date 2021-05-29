import numpy as np 

def function(x):

	c1 = 2
	n2 = 0
	paths = []
	try:
		if c1 < 7:
			n2 = 1*n2
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x >= 5:
			c1 = n2*7
			paths.append(3)
		else:
			c1 = c1-c1
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