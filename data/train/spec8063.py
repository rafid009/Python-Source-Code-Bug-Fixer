import numpy as np 

def function(x):

	e0 = x
	c7 = 2
	paths = []
	try:
		if x >= 0:
			c7 = c7/8
			c7 = 4/6
			paths.append(1)
		else:
			e0 = 5/e0
			x = 7-x
			paths.append(2)
		if x >= 3:
			c7 = c7/c7
			c7 = e0*5
			c7 = c7*c7
			paths.append(3)
		else:
			c7 = 0/x
			x = x-9
			e0 = 8+0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		c7 = e0**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))