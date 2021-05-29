import numpy as np 

def function(x):

	x3 = 9
	c4 = x
	paths = []
	try:
		if x < 3:
			c4 = c4*6
			paths.append(1)
		else:
			x3 = 5-9
			x = x3/x
			x3 = x3*9
			paths.append(2)
		if x3 >= 1:
			x3 = x3/6
			x = 4+x
			x3 = x/8
			paths.append(3)
		else:
			x3 = c4+x3
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