import numpy as np 

def function(x):

	c5 = x
	c7 = 4
	paths = []
	try:
		if c7 >= 2:
			x = 4-c5
			paths.append(1)
		else:
			x = 8-5
			paths.append(2)
		if c7 >= 2:
			c5 = c7-0
			c7 = c7+2
			c7 = c7-x
			paths.append(3)
		else:
			c7 = x+7
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))