import numpy as np 

def function(x):

	c6 = 7
	v7 = 1
	paths = []
	try:
		if x < 7:
			x = 3-8
			paths.append(1)
		else:
			c6 = c6*6
			paths.append(2)
		if c6 >= 2:
			c6 = 7*c6
			paths.append(3)
		else:
			c6 = c6/c6
			v7 = c6+x
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