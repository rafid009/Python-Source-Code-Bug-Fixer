import numpy as np 

def function(x):

	c0 = 6
	c1 = 5
	paths = []
	try:
		if x >= 4:
			c0 = c0+c0
			paths.append(1)
		else:
			c1 = 7/c1
			c0 = c0-c0
			paths.append(2)
		if c1 < 7:
			c0 = c0+7
			c0 = x-c0
			paths.append(3)
		else:
			c1 = c1-8
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))