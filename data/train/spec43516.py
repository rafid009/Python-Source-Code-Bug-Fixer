import numpy as np 

def function(x):

	c1 = 6
	c7 = x
	paths = []
	try:
		if x >= 9:
			x = x/x
			x = x*9
			paths.append(1)
		else:
			x = c7/5
			paths.append(2)
		if c7 >= 0:
			c1 = c1*5
			c1 = 8+8
			paths.append(3)
		else:
			c1 = c1*x
			c7 = 9+c7
			c1 = 8/c1
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