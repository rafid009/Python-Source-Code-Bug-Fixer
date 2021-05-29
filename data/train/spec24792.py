import numpy as np 

def function(x):

	c8 = x
	x1 = 4
	paths = []
	try:
		if c8 >= 9:
			x = 5*x
			c8 = c8*4
			x1 = 2/3
			paths.append(1)
		else:
			c8 = c8+3
			x = x1-x
			paths.append(2)
		if x1 <= 7:
			x = 3+5
			c8 = 0-c8
			x = 0-x
			paths.append(3)
		else:
			x = 7*x
			x = c8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))