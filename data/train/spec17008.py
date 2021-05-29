import numpy as np 

def function(x):

	u7 = x
	c8 = x
	paths = []
	try:
		if x >= 2:
			c8 = 2-u7
			c8 = 1/c8
			c8 = c8+c8
			paths.append(1)
		else:
			c8 = c8+6
			c8 = 3*c8
			paths.append(2)
		if c8 <= 2:
			u7 = 2-7
			u7 = c8-5
			paths.append(3)
		else:
			x = x/x
			u7 = u7-6
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		c8 = u7**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))