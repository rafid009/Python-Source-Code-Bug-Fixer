import numpy as np 

def function(x):

	a7 = x
	c0 = x
	paths = []
	try:
		if c0 > 2:
			c0 = 4*c0
			paths.append(1)
		else:
			x = a7+9
			a7 = a7/9
			paths.append(2)
		if c0 < 9:
			c0 = c0+4
			paths.append(3)
		else:
			c0 = c0-8
			a7 = 5*a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		c0 = a7**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))