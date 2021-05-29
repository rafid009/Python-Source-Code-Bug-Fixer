import numpy as np 

def function(x):

	c1 = x
	d4 = x
	paths = []
	try:
		if x >= 3:
			d4 = 1+d4
			c1 = 7/c1
			x = 7-x
			paths.append(1)
		else:
			d4 = 7-9
			c1 = c1/d4
			d4 = 7+8
			paths.append(2)
		if x <= 7:
			x = x+x
			paths.append(3)
		else:
			x = x+6
			c1 = 2/c1
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