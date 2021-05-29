import numpy as np 

def function(x):

	c4 = 1
	i4 = 2
	paths = []
	try:
		if c4 < 9:
			c4 = c4/c4
			x = c4-5
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if c4 >= 1:
			c4 = 6-c4
			c4 = c4*7
			i4 = i4/5
			paths.append(3)
		else:
			x = x-c4
			i4 = i4+i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))