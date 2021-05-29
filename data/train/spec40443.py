import numpy as np 

def function(x):

	o4 = 8
	c8 = 8
	paths = []
	try:
		if c8 < 9:
			o4 = 4/o4
			o4 = o4/c8
			o4 = x+o4
			paths.append(1)
		else:
			o4 = o4+8
			c8 = 5*c8
			o4 = 3-3
			paths.append(2)
		if c8 >= 1:
			o4 = o4/3
			o4 = 0/o4
			paths.append(3)
		else:
			c8 = c8*5
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