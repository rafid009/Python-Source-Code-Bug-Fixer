import numpy as np 

def function(x):

	c4 = 6
	y5 = 7
	paths = []
	try:
		if x >= 1:
			c4 = 0/c4
			paths.append(1)
		else:
			y5 = x+y5
			x = x-3
			paths.append(2)
		if y5 >= 3:
			x = x-0
			c4 = c4+8
			paths.append(3)
		else:
			x = x+6
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