import numpy as np 

def function(x):

	c4 = 9
	x9 = x
	paths = []
	try:
		if x9 > 7:
			x = 9-x
			c4 = c4+0
			c4 = 5+c4
			paths.append(1)
		else:
			c4 = 3/c4
			c4 = x9*x9
			paths.append(2)
		if x9 < 5:
			x = 6-x9
			x9 = c4-x9
			paths.append(3)
		else:
			c4 = c4*c4
			x9 = x9-x9
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		c4 = x9**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))