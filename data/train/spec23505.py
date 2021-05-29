import numpy as np 

def function(x):

	d5 = x
	c5 = 2
	paths = []
	try:
		if d5 >= 6:
			d5 = 7*6
			paths.append(1)
		else:
			c5 = 6/4
			x = x/c5
			c5 = 1-x
			paths.append(2)
		if c5 < 6:
			d5 = 8+d5
			paths.append(3)
		else:
			x = d5/x
			c5 = c5*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))