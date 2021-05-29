import numpy as np 

def function(x):

	c6 = 9
	d8 = 6
	x = x
	paths = []
	try:
		if x < 6:
			c6 = c6-c6
			paths.append(1)
		else:
			x = c6/7
			x = x*9
			paths.append(2)
		if c6 >= 4:
			d8 = 6-3
			c6 = c6/c6
			paths.append(3)
		else:
			c6 = c6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))