import numpy as np 

def function(x):

	x8 = x
	c7 = x
	paths = []
	try:
		if c7 >= 8:
			c7 = 3-7
			c7 = 9-x8
			paths.append(1)
		else:
			c7 = c7+4
			x = x8/x
			paths.append(2)
		if x < 1:
			x8 = 7-x8
			paths.append(3)
		else:
			x8 = 2-1
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))