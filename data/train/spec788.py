import numpy as np 

def function(x):

	u4 = 7
	c7 = 6
	x = x
	paths = []
	try:
		if c7 > 3:
			c7 = 3+c7
			x = x-7
			paths.append(1)
		else:
			c7 = 9/u4
			paths.append(2)
		if c7 < 0:
			c7 = c7+9
			paths.append(3)
		else:
			u4 = 5/u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))