import numpy as np 

def function(x):

	c6 = x
	x9 = x
	paths = []
	try:
		if x >= 9:
			c6 = c6/4
			paths.append(1)
		else:
			x = x9*c6
			x = 1-7
			paths.append(2)
		if c6 >= 4:
			x = x/1
			c6 = x/c6
			c6 = 1-9
			paths.append(3)
		else:
			x = x/5
			c6 = x9+3
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		c6 = x9**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))