import numpy as np 

def function(x):

	c6 = 2
	r4 = 1
	paths = []
	try:
		if x >= 5:
			r4 = 9*r4
			c6 = c6/r4
			c6 = x-2
			paths.append(1)
		else:
			c6 = r4/c6
			r4 = r4*6
			paths.append(2)
		if r4 >= 1:
			c6 = c6-0
			paths.append(3)
		else:
			c6 = c6/8
			c6 = c6*3
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