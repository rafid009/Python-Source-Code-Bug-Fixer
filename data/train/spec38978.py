import numpy as np 

def function(x):

	x5 = 7
	c1 = x
	paths = []
	try:
		if c1 <= 7:
			x = x+x5
			x5 = 9+c1
			c1 = c1-2
			paths.append(1)
		else:
			c1 = 1*x
			c1 = c1*7
			c1 = 8*x5
			paths.append(2)
		if c1 >= 8:
			x = 6-x
			x5 = 0+x5
			c1 = c1*9
			paths.append(3)
		else:
			x5 = 6-x5
			x5 = 2*x5
			c1 = c1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))